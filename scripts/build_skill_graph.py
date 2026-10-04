#!/usr/bin/env python3
"""Build a standalone project/skill force graph from the Markdown wiki."""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from collections import Counter
from pathlib import Path
from typing import Any

if __package__:
    from .build_skill_map import (
        EVIDENCE_STATUSES,
        MapBuildError,
        REQUIREMENT_STATUSES,
        _safe_json,
        load_wiki,
    )
else:
    from build_skill_map import (
        EVIDENCE_STATUSES,
        MapBuildError,
        REQUIREMENT_STATUSES,
        _safe_json,
        load_wiki,
    )


class SkillGraphBuildError(Exception):
    """Raised when graph-specific data cannot be represented safely."""


def load_alias_groups(
    path: Path, skill_paths: set[str]
) -> dict[str, dict[str, Any]]:
    """Load explicitly curated display labels and skill equivalence groups."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise SkillGraphBuildError(f"{path}: alias map is missing") from error
    except json.JSONDecodeError as error:
        raise SkillGraphBuildError(
            f"{path}:{error.lineno}:{error.colno}: invalid JSON: {error.msg}"
        ) from error

    if not isinstance(data, dict) or set(data) != {"groups"}:
        raise SkillGraphBuildError(
            f"{path}: expected an object containing only a 'groups' array"
        )
    groups = data["groups"]
    if not isinstance(groups, list):
        raise SkillGraphBuildError(f"{path}: 'groups' must be an array")

    by_skill: dict[str, dict[str, Any]] = {}
    labels: dict[str, int] = {}
    for index, group in enumerate(groups, start=1):
        context = f"{path}:groups[{index - 1}]"
        if not isinstance(group, dict) or set(group) != {"label", "skill_paths"}:
            raise SkillGraphBuildError(
                f"{context}: expected only 'label' and 'skill_paths'"
            )

        label = group["label"]
        if not isinstance(label, str) or not label.strip():
            raise SkillGraphBuildError(f"{context}: label must be a non-empty string")
        normalized_label = label.strip()
        label_key = normalized_label.casefold()
        if label_key in labels:
            raise SkillGraphBuildError(
                f"{context}: duplicate graph label {normalized_label!r} "
                f"(also in groups[{labels[label_key] - 1}])"
            )

        members = group["skill_paths"]
        if not isinstance(members, list) or not members:
            raise SkillGraphBuildError(
                f"{context}: 'skill_paths' must be a non-empty array"
            )
        if any(not isinstance(member, str) or not member for member in members):
            raise SkillGraphBuildError(
                f"{context}: each skill path must be a non-empty string"
            )
        if len(set(members)) != len(members):
            raise SkillGraphBuildError(f"{context}: duplicate skill path")

        unknown_paths = sorted(set(members) - skill_paths)
        if unknown_paths:
            raise SkillGraphBuildError(
                f"{context}: unknown skill path(s): {', '.join(unknown_paths)}"
            )

        member_paths = sorted(members)
        graph_id = (
            f"alias:{'|'.join(member_paths)}" if len(member_paths) > 1 else member_paths[0]
        )
        record = {
            "id": graph_id,
            "label": normalized_label,
            "skill_paths": member_paths,
        }
        for member in member_paths:
            if member in by_skill:
                raise SkillGraphBuildError(
                    f"{context}: {member!r} already belongs to "
                    f"{by_skill[member]['label']!r}"
                )
            by_skill[member] = record

        labels[label_key] = index

    return by_skill


def build_graph_data(root: Path) -> dict[str, Any]:
    """Convert the validated wiki records into shared project/skill nodes."""
    root = root.resolve()
    wiki_data = load_wiki(
        root, include_aliases=True, include_graph_metadata=True
    )
    skills_by_path = {skill["path"]: skill for skill in wiki_data["skills"]}
    alias_groups = load_alias_groups(
        root / "wiki" / "skill-graph-aliases.json", set(skills_by_path)
    )

    skill_nodes_by_id: dict[str, dict[str, Any]] = {}
    graph_skill_id_by_path: dict[str, str] = {}
    for skill in wiki_data["skills"]:
        path = skill["path"]
        group = alias_groups.get(path)
        graph_id = group["id"] if group else path
        short_title = skill.get("short_title", skill["title"])
        label = group["label"] if group else short_title
        node = skill_nodes_by_id.get(graph_id)
        if node is None:
            node = {
                "id": graph_id,
                "type": "skill",
                "label": label,
                "title": skill["title"],
                "pages": [],
                "search_terms": [],
            }
            skill_nodes_by_id[graph_id] = node
        node["pages"].append(
            {
                "path": path,
                "title": skill["title"],
                "definition": skill["definition"],
                "aliases": skill["aliases"],
                "href": path,
            }
        )
        node["search_terms"].extend(
            [short_title, skill["title"], *skill["aliases"]]
        )
        if group:
            node["search_terms"].append(group["label"])
        graph_skill_id_by_path[path] = graph_id

    project_nodes_by_path: dict[str, dict[str, Any]] = {}
    for project in wiki_data["projects"]:
        path = project["path"]
        project_nodes_by_path[path] = {
            "id": path,
            "type": "project",
            "label": project.get("short_title", project["title"]),
            "title": project["title"],
            "path": path,
            "href": path,
            "search_terms": [
                project.get("short_title", project["title"]),
                project["title"],
            ],
            "source_reviews": project["source_reviews"],
            "unmapped_claims": project["unmapped_claims"],
            "data_quality_notes": project["data_quality_notes"],
        }

    valid_statuses = {
        "requirement": REQUIREMENT_STATUSES,
        "source_evidence": EVIDENCE_STATUSES,
        "user_reported": {"user-reported"},
    }
    edges: list[dict[str, Any]] = []
    for relationship in wiki_data["relationships"]:
        kind = relationship["kind"]
        status = relationship["status"]
        if kind not in valid_statuses or status not in valid_statuses[kind]:
            raise SkillGraphBuildError(
                f"invalid relationship provenance/status: {kind!r}/{status!r}"
            )

        project_path = relationship["project_path"]
        skill_path = relationship["skill_path"]
        if project_path not in project_nodes_by_path:
            raise SkillGraphBuildError(
                f"relationship references unknown project {project_path!r}"
            )
        if skill_path not in graph_skill_id_by_path:
            raise SkillGraphBuildError(
                f"relationship references unknown skill {skill_path!r}"
            )
        edges.append(
            {
                "source": project_path,
                "target": graph_skill_id_by_path[skill_path],
                "kind": kind,
                "status": status,
                "rationale": relationship["rationale"],
                "evidence": relationship["evidence"],
            }
        )

    publication_rationale = (
        "The user reports personally authoring publication material "
        "associated with this project."
    )
    for project in wiki_data["projects"]:
        if project.get("publication_authorship") == "user-reported":
            edges.append(
                {
                    "source": "publication-hub",
                    "target": project["path"],
                    "kind": "publication_authorship",
                    "status": "user-reported",
                    "rationale": publication_rationale,
                    "evidence": [],
                }
            )

    edges.sort(
        key=lambda edge: (
            edge["source"],
            edge["target"],
            edge["kind"],
            edge["status"],
            edge["rationale"],
            tuple((item["label"], item["href"]) for item in edge["evidence"]),
        )
    )
    for index, edge in enumerate(edges):
        edge["id"] = f"edge-{index:05d}"

    publication_node = {
        "id": "publication-hub",
        "type": "publication",
        "label": "Publications",
        "title": "Publications",
        "search_terms": ["publications", "publication", "authorship"],
    }
    nodes = (
        list(project_nodes_by_path.values())
        + list(skill_nodes_by_id.values())
        + [publication_node]
    )
    nodes.sort(key=lambda node: (node["type"], node["id"]))
    counts = Counter(edge["kind"] for edge in edges)
    return {
        "nodes": nodes,
        "edges": edges,
        "source_inventory": wiki_data["source_inventory"],
        "counts": {
            "projects": len(project_nodes_by_path),
            "skill_nodes": len(skill_nodes_by_id),
            "canonical_skills": len(skills_by_path),
            "publication_nodes": 1,
            "relationships": dict(sorted(counts.items())),
        },
    }


def render_html(data: dict[str, Any]) -> str:
    """Embed validated graph data in the standalone HTML template."""
    template_path = Path(__file__).with_name("skill_graph_template.html")
    try:
        template = template_path.read_text(encoding="utf-8")
    except OSError as error:
        raise SkillGraphBuildError(
            f"{template_path}: could not read graph template: {error}"
        ) from error

    marker = "__GRAPH_DATA_JSON__"
    if template.count(marker) != 1:
        raise SkillGraphBuildError(
            f"{template_path}: expected exactly one {marker} data marker"
        )
    return template.replace(marker, _safe_json(data))


def write_html_atomically(output: Path, html: str) -> Path:
    """Replace the graph only after a complete temporary file is written."""
    output = output.resolve()
    if not output.parent.is_dir():
        raise SkillGraphBuildError(f"{output.parent}: output directory does not exist")

    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=output.parent,
            prefix=f".{output.name}.",
            suffix=".tmp",
            delete=False,
        ) as stream:
            temporary_path = Path(stream.name)
            stream.write(html)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary_path, output)
    except OSError as error:
        raise SkillGraphBuildError(
            f"{output}: could not write generated graph: {error}"
        ) from error
    finally:
        if temporary_path is not None:
            try:
                temporary_path.unlink()
            except FileNotFoundError:
                pass

    return output


def build_graph(root: Path, output: Path) -> tuple[dict[str, Any], Path]:
    """Build validated graph data and atomically write the standalone page."""
    data = build_graph_data(root)
    html = render_html(data)
    return data, write_html_atomically(output, html)


def main(argv: list[str] | None = None) -> int:
    project_root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=project_root,
        help="project root containing wiki/ (default: inferred from this script)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="output HTML path (default: <root>/wiki/skill-graph.html)",
    )
    args = parser.parse_args(argv)
    root = args.root.resolve()
    output = args.output or (root / "wiki" / "skill-graph.html")
    if not output.is_absolute():
        output = root / output

    try:
        data, output_path = build_graph(root, output)
    except (SkillGraphBuildError, MapBuildError, OSError) as error:
        print(f"Skill graph build failed: {error}", file=sys.stderr)
        return 1

    relationship_summary = ", ".join(
        f"{kind}={count}" for kind, count in data["counts"]["relationships"].items()
    )
    print(
        f"Generated {output_path}: {data['counts']['projects']} projects, "
        f"{data['counts']['canonical_skills']} canonical skills, "
        f"{data['counts']['skill_nodes']} graph skill nodes, "
        f"{data['counts']['publication_nodes']} publication node, "
        f"{len(data['edges'])} relationships ({relationship_summary})."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
