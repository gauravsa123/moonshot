#!/usr/bin/env python3
"""Build a standalone project/skill explorer from the Markdown wiki."""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote, urlsplit


INVENTORY_STATUSES = {"processed", "needs review", "blocked"}
REQUIREMENT_STATUSES = {"suggested", "user-confirmed"}
EVIDENCE_STATUSES = {"documented", "inferred", "unknown"}
RELATIONSHIP_SECTIONS = {
    "requirement": (
        "Know-how needed",
        REQUIREMENT_STATUSES,
        (
            {"Skill", "Skill requirement", "Skill candidate"},
            {"Review status", "Status"},
            {"Rationale"},
        ),
    ),
    "source_evidence": (
        "Skills shown by sources",
        EVIDENCE_STATUSES,
        (
            {"Skill", "Skill or capability", "Capability", "Claim"},
            {"Evidence status", "Status"},
            {"Evidence"},
        ),
    ),
}
USER_REPORTED_SECTION = "Projects with user-reported use"
PROJECT_SECTIONS = (
    "Know-how needed",
    "Skills shown by sources",
    "User-reported contributions and outcomes",
)
SKILL_SECTIONS = (
    "Projects needing this skill",
    "Projects with user-reported use",
    "Projects showing this skill",
)
MARKDOWN_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


class MapBuildError(Exception):
    """Raised when wiki data cannot be represented without losing meaning."""


def _read_page(
    path: Path, *, strict_source_refs: bool = True
) -> tuple[str, str, dict[str, list[str] | str]]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise MapBuildError(f"{path}: missing YAML frontmatter")
    end = text.find("\n---", 4)
    if end < 0:
        raise MapBuildError(f"{path}: unterminated YAML frontmatter")

    frontmatter = text[4:end]
    body = text[end + 4 :].lstrip("\n")
    fields: dict[str, list[str] | str] = {}
    current_list: str | None = None
    previous_key: str | None = None
    for line_number, line in enumerate(frontmatter.splitlines(), start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        item = re.match(r"^\s*-\s*(.*?)\s*$", line)
        if item and current_list:
            value = item.group(1).strip("\"'")
            fields.setdefault(current_list, [])
            assert isinstance(fields[current_list], list)
            fields[current_list].append(value)
            continue
        if item and not current_list:
            if strict_source_refs and previous_key == "source_refs":
                raise MapBuildError(
                    f"{path}:{line_number}: malformed source_refs list"
                )
            continue
        match = re.match(r"^([A-Za-z_][\w-]*):\s*(.*?)\s*$", line)
        if not match:
            raise MapBuildError(
                f"{path}:{line_number}: malformed frontmatter field"
            )
        key, value = match.groups()
        previous_key = key
        current_list = None
        if value == "[]":
            fields[key] = []
        elif not value:
            fields[key] = []
            current_list = key
        else:
            fields[key] = value.strip("\"'")

    title = fields.get("title")
    if not isinstance(title, str) or not title.strip():
        raise MapBuildError(f"{path}: missing frontmatter title")
    return title.strip(), body, fields


def _section(body: str, heading: str, page: Path) -> str:
    heading_pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*$", re.MULTILINE
    )
    match = heading_pattern.search(body)
    if not match:
        raise MapBuildError(f"{page}: missing required section '## {heading}'")
    next_heading = re.search(r"^##\s+", body[match.end() :], re.MULTILINE)
    end = match.end() + next_heading.start() if next_heading else len(body)
    return body[match.end() : end]


def _split_table_row(line: str) -> list[str]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    cells: list[str] = []
    current: list[str] = []
    escaped = False
    for char in stripped:
        if char == "|" and not escaped:
            cells.append("".join(current).strip())
            current.clear()
        else:
            current.append(char)
        escaped = char == "\\" and not escaped
        if char != "\\":
            escaped = False
    cells.append("".join(current).strip())
    return cells


def _table_rows(
    section: str, allowed_headers: tuple[set[str], ...], page: Path
) -> list[list[str]]:
    lines = section.splitlines()
    table_start = next(
        (index for index, line in enumerate(lines) if "|" in line), None
    )
    if table_start is None:
        return []

    headers = tuple(_split_table_row(lines[table_start]))
    if len(headers) != len(allowed_headers) or any(
        value not in allowed for value, allowed in zip(headers, allowed_headers)
    ):
        raise MapBuildError(
            f"{page}: unsupported table columns {headers!r}"
        )
    if table_start + 1 >= len(lines):
        raise MapBuildError(f"{page}: table has no separator row")
    separator = _split_table_row(lines[table_start + 1])
    if len(separator) != len(allowed_headers) or not all(
        re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in separator
    ):
        raise MapBuildError(f"{page}: malformed table separator")

    rows: list[list[str]] = []
    for line_number, line in enumerate(lines[table_start + 2 :], start=table_start + 3):
        if not line.strip():
            continue
        if "|" not in line:
            continue
        cells = _split_table_row(line)
        if len(cells) != len(allowed_headers):
            raise MapBuildError(
                f"{page}:{line_number}: expected {len(allowed_headers)} table cells, got {len(cells)}"
            )
        rows.append(cells)
    return rows


def _plain_markdown(value: str) -> str:
    value = MARKDOWN_LINK.sub(lambda match: match.group(1), value)
    value = re.sub(r"(!?)\[([^\]]*)\]\([^)]*\)", r"\2", value)
    value = re.sub(r"[*_`~]{1,3}", "", value)
    return re.sub(r"\s+", " ", value).strip()


def _resolve_wiki_link(
    href: str, origin: Path, wiki_root: Path, context: str
) -> str:
    parsed = urlsplit(href.strip())
    if parsed.scheme or parsed.netloc:
        raise MapBuildError(f"{context}: external link is not supported: {href}")
    if not parsed.path:
        target = origin.resolve()
    else:
        target = (origin.parent / unquote(parsed.path)).resolve()
    wiki_root = wiki_root.resolve()
    if not target.is_relative_to(wiki_root):
        raise MapBuildError(f"{context}: link escapes wiki directory: {href}")
    if not target.is_file():
        raise MapBuildError(f"{context}: linked page does not exist: {href}")
    relative = target.relative_to(wiki_root).as_posix()
    return relative + (f"#{parsed.fragment}" if parsed.fragment else "")


def _links(value: str, origin: Path, wiki_root: Path, context: str) -> list[dict[str, str]]:
    result = []
    for match in MARKDOWN_LINK.finditer(value):
        result.append(
            {
                "label": _plain_markdown(match.group(1)),
                "href": _resolve_wiki_link(
                    match.group(2), origin, wiki_root, context
                ),
            }
        )
    return result


def _first_link(value: str, origin: Path, wiki_root: Path, context: str) -> dict[str, str]:
    links = _links(value, origin, wiki_root, context)
    if not links:
        raise MapBuildError(f"{context}: expected a local Markdown link")
    return links[0]


def _source_refs(fields: dict[str, list[str] | str], page: Path) -> list[str]:
    values = fields.get("source_refs", [])
    if isinstance(values, str):
        raise MapBuildError(f"{page}: source_refs must be a YAML list")
    return values


def _load_inventory(root: Path, wiki_root: Path) -> tuple[list[dict], dict[str, dict]]:
    path = wiki_root / "source-inventory.csv"
    if not path.is_file():
        raise MapBuildError(f"{path}: source inventory is missing")
    inventory: list[dict] = []
    by_page: dict[str, dict] = {}
    try:
        with path.open(encoding="utf-8", newline="") as stream:
            reader = csv.DictReader(stream)
            required = {"source_path", "status", "reason", "wiki_page"}
            if not reader.fieldnames or not required.issubset(reader.fieldnames):
                raise MapBuildError(
                    f"{path}: expected CSV columns {sorted(required)!r}"
                )
            for row_number, row in enumerate(reader, start=2):
                raw_page = (row.get("wiki_page") or "").strip()
                status = (row.get("status") or "").strip()
                if status not in INVENTORY_STATUSES:
                    raise MapBuildError(
                        f"{path}:{row_number}: invalid inventory status {status!r}"
                    )
                if not raw_page:
                    raise MapBuildError(
                        f"{path}:{row_number}: missing wiki_page"
                    )
                page_path = raw_page.removeprefix("wiki/")
                target = (root / raw_page).resolve()
                if not target.is_relative_to(wiki_root.resolve()) or not target.is_file():
                    raise MapBuildError(
                        f"{path}:{row_number}: inventory page does not exist in wiki: {raw_page}"
                    )
                record = {
                    "source_path": (row.get("source_path") or "").strip(),
                    "page_path": page_path,
                    "status": status,
                    "reason": (row.get("reason") or "").strip(),
                }
                if not record["source_path"]:
                    raise MapBuildError(
                        f"{path}:{row_number}: missing source_path"
                    )
                if page_path in by_page:
                    raise MapBuildError(
                        f"{path}:{row_number}: duplicate wiki_page {raw_page}"
                    )
                by_page[page_path] = record
                inventory.append(record)
    except csv.Error as error:
        raise MapBuildError(f"{path}: invalid CSV: {error}") from error
    return inventory, by_page


def _definition(body: str, title: str) -> str:
    match = re.search(r"^#\s+.+$", body, re.MULTILINE)
    if not match:
        raise MapBuildError(f"skill page is missing '# {title}' heading")
    after_title = body[match.end() :]
    next_heading = re.search(r"^##\s+", after_title, re.MULTILINE)
    text = after_title[: next_heading.start()] if next_heading else after_title
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip() and not line.lstrip().startswith("<!--")
    ]
    return _plain_markdown(" ".join(lines))


def _parse_skill_list(
    section: str, page: Path, wiki_root: Path, project_paths: set[str]
) -> list[dict[str, str]]:
    result = []
    for line_number, line in enumerate(section.splitlines(), start=1):
        stripped = line.strip()
        if not stripped.startswith("- "):
            continue
        if re.match(r"-\s+(?:None|No)\b", stripped, re.IGNORECASE):
            continue
        project = _first_link(
            stripped[2:], page, wiki_root, f"{page}:user-reported list line {line_number}"
        )
        if project["href"] not in project_paths:
            raise MapBuildError(
                f"{page}: user-reported list links to unknown project {project['href']}"
            )
        result.append(project)
    return result


def load_wiki(root: Path, *, include_aliases: bool = False) -> dict:
    root = root.resolve()
    wiki_root = root / "wiki"
    projects_dir = wiki_root / "projects"
    skills_dir = wiki_root / "skills"
    if not projects_dir.is_dir() or not skills_dir.is_dir():
        raise MapBuildError(f"{root}: expected wiki/projects and wiki/skills")

    inventory, inventory_by_page = _load_inventory(root, wiki_root)
    project_files = sorted(projects_dir.glob("*.md"))
    skill_files = sorted(skills_dir.glob("*.md"))
    if not project_files or not skill_files:
        raise MapBuildError(f"{wiki_root}: project or skill pages are missing")

    projects: list[dict] = []
    project_by_path: dict[str, dict] = {}
    source_page_paths = {
        path.resolve() for path in (wiki_root / "sources").glob("*.md")
    }
    for page in project_files:
        title, body, fields = _read_page(page)
        if fields.get("type") != "project":
            raise MapBuildError(f"{page}: frontmatter type must be 'project'")
        for heading in PROJECT_SECTIONS:
            _section(body, heading, page)
        path = page.resolve().relative_to(wiki_root.resolve()).as_posix()
        project = {
            "title": title,
            "path": path,
            "source_reviews": [],
            "unmapped_claims": [],
            "data_quality_notes": [],
        }
        seen_sources: set[str] = set()
        for source_ref in _source_refs(fields, page):
            normalized = _resolve_wiki_link(
                source_ref, page, wiki_root, f"{page}:source_refs"
            )
            source_page = normalized.split("#", 1)[0]
            target = (wiki_root / source_page).resolve()
            if target not in source_page_paths:
                raise MapBuildError(
                    f"{page}: source_refs must target an indexed source page: {source_ref}"
                )
            if source_page in seen_sources:
                continue
            seen_sources.add(source_page)
            record = inventory_by_page.get(source_page)
            if not record:
                raise MapBuildError(
                    f"{page}: source page is missing from inventory: {source_page}"
                )
            project["source_reviews"].append(dict(record))
        projects.append(project)
        project_by_path[path] = project

    skills: list[dict] = []
    skill_by_path: dict[str, dict] = {}
    for page in skill_files:
        title, body, fields = _read_page(page, strict_source_refs=False)
        if fields.get("type") != "skill":
            raise MapBuildError(f"{page}: frontmatter type must be 'skill'")
        for heading in SKILL_SECTIONS:
            _section(body, heading, page)
        path = page.resolve().relative_to(wiki_root.resolve()).as_posix()
        skill = {
            "title": title,
            "path": path,
            "definition": _definition(body, title),
        }
        if include_aliases:
            aliases = fields.get("aliases", [])
            if not isinstance(aliases, list) or any(
                not isinstance(alias, str) for alias in aliases
            ):
                raise MapBuildError(
                    f"{page}: aliases must be a YAML list of strings"
                )
            skill["aliases"] = aliases
        skills.append(skill)
        skill_by_path[path] = skill

    relationships: list[dict] = []
    for page in project_files:
        project_path = page.resolve().relative_to(wiki_root.resolve()).as_posix()
        project = project_by_path[project_path]
        for kind, (heading, valid_statuses, allowed_headers) in RELATIONSHIP_SECTIONS.items():
            section = _section(_read_page(page)[1], heading, page)
            for row_number, cells in enumerate(
                _table_rows(section, allowed_headers, page), start=1
            ):
                context = f"{page}:{heading} row {row_number}"
                first_cell_links = _links(cells[0], page, wiki_root, context)
                skill_link = next(
                    (link for link in first_cell_links if link["href"] in skill_by_path),
                    None,
                )
                claim = _plain_markdown(cells[0])
                if not claim:
                    raise MapBuildError(f"{context}: empty skill/capability cell")
                status = _plain_markdown(cells[1])
                rationale = _plain_markdown(cells[2])
                citations = _links(
                    cells[2],
                    page,
                    wiki_root,
                    context,
                )
                if status not in valid_statuses:
                    if kind == "source_evidence" and status == "user-reported":
                        project["data_quality_notes"].append(
                            {
                                "section": heading,
                                "claim": claim,
                                "status": status,
                                "details": rationale,
                                "evidence": citations,
                            }
                        )
                        continue
                    raise MapBuildError(f"{context}: invalid status {status!r}")
                if skill_link is None:
                    project["unmapped_claims"].append(
                        {
                            "kind": kind,
                            "claim": claim,
                            "status": status,
                            "details": rationale,
                            "evidence": citations
                            + [
                                link
                                for link in first_cell_links
                                if link not in citations
                            ],
                        }
                    )
                    continue
                skill_path = skill_link["href"]
                relationships.append(
                    {
                        "project_path": project_path,
                        "skill_path": skill_path,
                        "kind": kind,
                        "status": status,
                        "rationale": rationale,
                        "evidence": citations,
                    }
                )

    project_paths = set(project_by_path)
    for page in skill_files:
        skill_path = page.resolve().relative_to(wiki_root.resolve()).as_posix()
        _, body, _ = _read_page(page, strict_source_refs=False)
        section = _section(body, USER_REPORTED_SECTION, page)
        for project_link in _parse_skill_list(
            section, page, wiki_root, project_paths
        ):
            relationships.append(
                {
                    "project_path": project_link["href"],
                    "skill_path": skill_path,
                    "kind": "user_reported",
                    "status": "user-reported",
                    "rationale": "User-reported capability.",
                    "evidence": [],
                }
            )

    return {
        "source_inventory": inventory,
        "projects": projects,
        "skills": skills,
        "relationships": relationships,
    }


def _safe_json(data: dict) -> str:
    return (
        json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        .replace("&", "\\u0026")
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )


def render_html(data: dict) -> str:
    payload = _safe_json(data)
    return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AI Skill Map</title>
<style>
:root{color-scheme:light;--ink:#172238;--muted:#52627a;--line:#d8e0ea;--paper:#f4f7fb;--blue:#155eef;--violet:#6941c6;--green:#027a48;--amber:#93370d}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
main{max-width:1440px;margin:auto;padding:28px}h1,h2,h3,p{margin-top:0}h1{font-size:clamp(1.7rem,3vw,2.5rem);margin-bottom:4px}h2{font-size:1.25rem}h3{font-size:1rem;margin:16px 0 8px}
.subtle,.muted{color:var(--muted)}.source-summary{padding:12px 16px;border:1px solid #fdb022;background:#fffaeb;border-radius:10px;margin:20px 0}
.toolbar{display:grid;grid-template-columns:auto minmax(220px,1fr) minmax(300px,1.5fr);gap:14px;align-items:center;padding:16px;background:#fff;border:1px solid var(--line);border-radius:12px}
.switch{display:flex;gap:6px}.switch button,.filters label,.selectable{border:1px solid var(--line);background:#fff;border-radius:8px;padding:9px 12px}
button,input{font:inherit;color:inherit}.switch button{cursor:pointer}.switch button[aria-pressed="true"]{background:#eff4ff;border-color:#84adff;color:#1849a9}
input[type=search]{width:100%;padding:10px 12px;border:1px solid var(--line);border-radius:8px}
.filters{display:flex;flex-wrap:wrap;gap:8px;border:0;padding:0;margin:0}.filters legend{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
.filters label{display:flex;align-items:center;gap:7px;cursor:pointer;font-size:.9rem}.filters input{accent-color:var(--blue)}
.workspace{display:grid;grid-template-columns:minmax(230px,320px) minmax(0,1fr);gap:18px;margin-top:18px;align-items:start}
.list,.detail{background:#fff;border:1px solid var(--line);border-radius:12px}.list{padding:14px;position:sticky;top:16px;max-height:calc(100vh - 32px);overflow:auto}.list h2{font-size:1rem;margin-bottom:8px}
.selectable{display:block;width:100%;text-align:left;margin-top:7px;cursor:pointer}.selectable:hover,.selectable[aria-current="true"]{border-color:#84adff;background:#eff4ff}
.detail{padding:22px;min-height:340px}.detail-head{display:flex;justify-content:space-between;gap:16px;align-items:start}.detail-head a,.wikilink{color:#1849a9;text-decoration:underline;text-underline-offset:2px}
.group{border-top:1px solid var(--line);margin-top:18px;padding-top:2px}.relation{padding:10px 12px;margin:8px 0;background:#f8fafc;border-left:4px solid var(--blue);border-radius:4px}
.relation.source_evidence{border-color:var(--violet)}.relation.user_reported{border-color:var(--green)}.badge{display:inline-block;border-radius:999px;background:#eff4ff;padding:2px 9px;font-size:.82rem;font-weight:650}
.badge.source_evidence{background:#f4f3ff;color:#5925dc}.badge.user_reported{background:#ecfdf3;color:#027a48}.badge.requirement{color:#1849a9}
.citations,.source-list{display:flex;flex-wrap:wrap;gap:8px;margin-top:6px}.source-item{padding:8px 10px;background:#fffaeb;border:1px solid #fedf89;border-radius:8px;margin:8px 0}
.empty{color:var(--muted);font-style:italic}.counts{display:flex;gap:18px;flex-wrap:wrap;margin:15px 0}.count{padding:10px 14px;background:#fff;border:1px solid var(--line);border-radius:10px}
:focus-visible{outline:3px solid #155eef;outline-offset:2px}
@media(max-width:900px){.toolbar{grid-template-columns:1fr}.workspace{grid-template-columns:1fr}.list{position:static;max-height:36vh}}
@media(max-width:540px){main{padding:14px}.detail{padding:16px}.filters{display:grid;grid-template-columns:1fr 1fr}}
</style>
</head>
<body>
<main>
<header>
<h1>AI skill map</h1>
<p class="subtle">Explore how skills relate to projects. Requirements, source evidence, and user-reported capabilities are separate kinds of evidence—not proficiency levels.</p>
<div class="counts" id="counts" aria-live="polite"></div>
<div class="source-summary" id="source-summary" role="status"></div>
</header>
<section class="toolbar" aria-label="Map controls">
<div class="switch" role="group" aria-label="Choose entity view">
<button type="button" aria-label="Projects view" aria-pressed="true" data-view="projects">Projects</button>
<button type="button" aria-label="Skills view" aria-pressed="false" data-view="skills">Skills</button>
</div>
<label>
<span class="muted">Search</span>
<input type="search" id="search" aria-label="Search projects and skills" placeholder="Search projects and skills">
</label>
<fieldset class="filters">
<legend>Show relationship types</legend>
<label><input type="checkbox" name="requirement" checked> Project requirements</label>
<label><input type="checkbox" name="source_evidence" checked> Source evidence</label>
<label><input type="checkbox" name="user_reported" checked> User-reported</label>
</fieldset>
</section>
<div class="workspace">
<aside class="list" aria-label="Results">
<h2 id="list-title">Projects</h2>
<div id="results"></div>
</aside>
<section class="detail" id="detail" aria-live="polite" aria-label="Selected project or skill">
<p class="empty">Choose a project or skill to inspect its relationships.</p>
</section>
</div>
</main>
<script id="map-data" type="application/json">""" + payload + """</script>
<script>
"use strict";
const data=JSON.parse(document.getElementById("map-data").textContent);
const kinds=["requirement","source_evidence","user_reported"];
const labels={requirement:"Project requirement",source_evidence:"Source-evidenced skill or method",user_reported:"User-reported capability"};
const enabled=Object.fromEntries(kinds.map(kind=>[kind,true]));
let view="projects", selected=null, query="";
const projectByPath=new Map(data.projects.map(item=>[item.path,item]));
const skillByPath=new Map(data.skills.map(item=>[item.path,item]));
const resultNode=document.getElementById("results"), detailNode=document.getElementById("detail");
function textNode(tag,text,className){const node=document.createElement(tag);node.textContent=text;if(className)node.className=className;return node}
function addLink(parent,href,label,className="wikilink"){const link=document.createElement("a");link.href=href;link.textContent=label;link.className=className;parent.append(link);return link}
function visibleRelationships(){return data.relationships.filter(row=>enabled[row.kind])}
function relatedText(item,kind){
 const rels=visibleRelationships().filter(row=>kind==="projects"?row.project_path===item.path:row.skill_path===item.path);
 const linked=rels.map(row=>{
  const other=kind==="projects"?skillByPath.get(row.skill_path):projectByPath.get(row.project_path);
  return [other?.title||"",row.rationale||"",...(row.evidence||[]).map(ref=>ref.label)].join(" ");
 }).join(" ");
 const unmapped=kind==="projects"?(item.unmapped_claims||[]).filter(row=>enabled[row.kind]).map(row=>[row.claim,row.details,...(row.evidence||[]).map(ref=>ref.label)].join(" ")).join(" "):"";
 return linked+" "+unmapped;
}
function matching(item){
 const own=view==="projects"?item.title:item.title+" "+item.definition;
 return (own+" "+relatedText(item,view)).toLocaleLowerCase().includes(query.toLocaleLowerCase());
}
function renderList(){
 const items=view==="projects"?data.projects:data.skills;
 document.getElementById("list-title").textContent=view==="projects"?"Projects":"Skills";
 resultNode.replaceChildren();
 const filtered=items.filter(matching);
 for(const item of filtered){
  const button=document.createElement("button");button.type="button";button.className="selectable";
  button.textContent=item.title;button.setAttribute("aria-current",String(selected===item.path));
  button.addEventListener("click",()=>{selected=item.path;renderList();renderDetail()});resultNode.append(button);
 }
 if(!filtered.length)resultNode.append(textNode("p","No matching projects or skills.","empty"));
}
function appendRelationship(group,row,other){
 const card=document.createElement("article");card.className="relation "+row.kind;
 const heading=document.createElement("div");heading.append(addLink(heading,other.path,other.title));card.append(heading);
 const meta=document.createElement("p");meta.append(textNode("span",labels[row.kind],"badge "+row.kind)," ");
 const status=row.status==="user-reported"?"user-reported":row.status;
 meta.append(textNode("span",status,"muted"));card.append(meta);
 if(row.rationale)card.append(textNode("p",row.rationale));
 if(row.evidence&&row.evidence.length){const refs=document.createElement("div");refs.className="citations";for(const ref of row.evidence)addLink(refs,ref.href,ref.label);card.append(refs)}
 group.append(card);
}
function appendUnmapped(group,row){
 const card=document.createElement("article");card.className="relation "+row.kind;
 card.append(textNode("div",row.claim));
 const meta=document.createElement("p");meta.append(textNode("span","Not mapped to a canonical skill","badge "+row.kind)," ",textNode("span",row.status,"muted"));card.append(meta);
 if(row.details)card.append(textNode("p",row.details));
 if(row.evidence&&row.evidence.length){const refs=document.createElement("div");refs.className="citations";for(const ref of row.evidence)addLink(refs,ref.href,ref.label);card.append(refs)}
 group.append(card);
}
function appendGroups(container,rows,isProject,unmappedClaims=[]){
 for(const kind of kinds){
  const section=document.createElement("section");section.className="group";
  section.append(textNode("h3",labels[kind]));
  const matches=rows.filter(row=>row.kind===kind&&enabled[kind]);
  const unmapped=isProject?unmappedClaims.filter(row=>row.kind===kind):[];
  if(!enabled[kind])section.append(textNode("p","Hidden by filter.","empty"));
  else if(!matches.length&&!unmapped.length)section.append(textNode("p",kind==="user_reported"?"No user-reported use recorded.":"No relationship recorded.","empty"));
  else {
   for(const row of matches){
    const other=isProject?skillByPath.get(row.skill_path):projectByPath.get(row.project_path);
    if(other)appendRelationship(section,row,other);
   }
   for(const row of unmapped)appendUnmapped(section,row);
  }
  container.append(section);
 }
}
function renderDetail(){
 detailNode.replaceChildren();
 const entity=(view==="projects"?projectByPath:skillByPath).get(selected);
 if(!entity){detailNode.append(textNode("p","Choose a project or skill to inspect its relationships.","empty"));return}
 const header=document.createElement("div");header.className="detail-head";
 const title=textNode("h2",entity.title);header.append(title);
 addLink(header,entity.path,"Open wiki page");detailNode.append(header);
 if(view==="skills"&&entity.definition)detailNode.append(textNode("p",entity.definition));
 const rows=visibleRelationships().filter(row=>view==="projects"?row.project_path===entity.path:row.skill_path===entity.path);
 appendGroups(detailNode,rows,view==="projects",view==="projects"?entity.unmapped_claims:[]);
 if(view==="projects"){
  const review=document.createElement("section");review.className="group";review.append(textNode("h3","Source review status"));
  if(!entity.source_reviews.length)review.append(textNode("p","No source inventory records are linked to this project.","empty"));
  else for(const source of entity.source_reviews){
   const item=document.createElement("article");item.className="source-item";
   addLink(item,source.page_path,source.page_path.split("/").pop());
   item.append(textNode("p",source.status+" — "+(source.reason||"No review reason recorded.")));
   review.append(item);
  }
  detailNode.append(review);
  if(entity.data_quality_notes.length){
   const notes=document.createElement("section");notes.className="group";notes.append(textNode("h3","Wiki data-quality notes"));
   for(const note of entity.data_quality_notes){
    const item=document.createElement("article");item.className="source-item";
    item.append(textNode("strong","Not included in relationship categories: "+note.status));
    item.append(textNode("p",note.claim));
    if(note.details)item.append(textNode("p",note.details));
    if(note.evidence&&note.evidence.length){const refs=document.createElement("div");refs.className="citations";for(const ref of note.evidence)addLink(refs,ref.href,ref.label);item.append(refs)}
    notes.append(item);
   }
   detailNode.append(notes);
  }
 }
}
function renderCounts(){
 document.getElementById("counts").replaceChildren(
  textNode("div",data.projects.length+" projects","count"),
  textNode("div",data.skills.length+" canonical skills","count"),
  textNode("div",data.relationships.length+" canonical-skill links","count"),
  textNode("div",data.projects.reduce((total,project)=>total+project.unmapped_claims.length,0)+" project-level entries not mapped to canonical skills","count")
 );
 const counts=Object.fromEntries(["processed","needs review","blocked"].map(status=>[status,data.source_inventory.filter(row=>row.status===status).length]));
 document.getElementById("source-summary").textContent="Source review: "+counts.processed+" processed, "+counts["needs review"]+" needs review, "+counts.blocked+" blocked. Inventory statuses describe source review completeness; a wiki record alone does not mean a source is fully reviewed.";
}
document.querySelectorAll("[data-view]").forEach(button=>button.addEventListener("click",()=>{
 view=button.dataset.view;selected=null;
 document.querySelectorAll("[data-view]").forEach(item=>item.setAttribute("aria-pressed",String(item===button)));
 renderList();renderDetail();
}));
document.getElementById("search").addEventListener("input",event=>{query=event.target.value.trim();renderList()});
document.querySelectorAll(".filters input").forEach(input=>input.addEventListener("change",()=>{
 enabled[input.name]=input.checked;renderList();renderDetail();
}));
renderCounts();renderList();
</script>
</body>
</html>
"""


def build_map(root: Path) -> Path:
    root = root.resolve()
    data = load_wiki(root)
    rendered = render_html(data)
    output = root / "wiki" / "skill-map.html"
    output.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=".skill-map-", suffix=".html", dir=output.parent
    )
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(rendered)
            stream.write("\n")
        os.replace(temporary_name, output)
    except Exception:
        try:
            os.unlink(temporary_name)
        except FileNotFoundError:
            pass
        raise
    return output


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="wiki repository root (defaults to the script's parent project)",
    )
    args = parser.parse_args(argv)
    try:
        output = build_map(args.root)
    except MapBuildError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print(f"Generated {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
