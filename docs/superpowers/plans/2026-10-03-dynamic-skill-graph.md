# Dynamic AI Skills Graph Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate a concise, offline force-directed graph linking canonical AI skills to projects while preserving relationship provenance and citations.

**Architecture:** Reuse `load_wiki()` from `scripts/build_skill_map.py` to validate and load the authoritative wiki. A graph builder applies only explicit alias mappings and injects serialized data into a self-contained HTML template. The template provides a canvas force graph, provenance filters, details, and a Markdown drop-in parser adapted to the wiki format.

**Tech Stack:** Python 3 standard library; standalone HTML, CSS, and JavaScript Canvas; no external libraries or network requests.

---

## File map

- Create `scripts/build_skill_graph.py` — load wiki data, validate/apply explicit graph aliases, create a graph data model, render the template, and write the generated artifact deterministically.
- Modify `scripts/build_skill_map.py` — add an opt-in `include_aliases` argument to `load_wiki()` so the graph can index skill-page aliases without changing the existing explorer's default data/output.
- Create `scripts/skill_graph_template.html` — complete standalone graph UI with data markers, force layout, accessible controls/details, and a browser-side Markdown loader.
- Create `wiki/skill-graph-aliases.json` — reviewed graph-only alias groups. Start with an empty `groups` array; do not invent equivalences.
- Create generated `wiki/skill-graph.html` — offline graph, not hand-edited.
- Modify `wiki/index.md` — link the graph while keeping the existing skill map link.
- Modify `wiki/log.md` — record generation and manual validation without changing source-review statuses.

The approved design is `docs/superpowers/specs/2026-10-03-dynamic-skill-graph-design.md`. Follow the provenance rules in `AGENTS.md`; do not edit anything under `raw/`. Do not create test-case files. This workspace is not a Git repository, so do not include commit steps.

### Task 1: Define and validate graph aliases

**Files:**
- Create: `wiki/skill-graph-aliases.json`
- Create: `scripts/build_skill_graph.py`
- Read: `scripts/build_skill_map.py`, `wiki/skills/*.md`

- [ ] Add an initially empty mapping file:

```json
{
  "groups": []
}
```

- [ ] Add `load_alias_groups(path, skill_paths) -> dict[str, dict]` to read UTF-8 JSON and reject invalid JSON, unknown skill paths, duplicate members, empty labels, empty `skill_paths`, or any page assigned to multiple groups. A one-page entry changes only the graph display label; a multi-page entry aggregates only an explicitly approved equivalence.
- [ ] Use this schema for each curated graph label or approved equivalence group:

```json
{
  "groups": [
    {
      "label": "Concise common keyword",
      "skill_paths": ["skills/canonical-skill.md"]
    }
  ]
}
```

- [ ] Apply no cross-page groups initially. Include each skill's `aliases` in search terms, but do not merge separate skill pages without an explicit group in the mapping file.
- [ ] Make validation errors identify the mapping file and offending group or skill path; do not fall back to an empty mapping when a non-empty file is malformed.

### Task 2: Build the normalized graph data

**Files:**
- Modify: `scripts/build_skill_graph.py`
- Modify: `scripts/build_skill_map.py`
- Read: `AGENTS.md`, `wiki/projects/*.md`, `wiki/skills/*.md`, `wiki/source-inventory.csv`

- [ ] Import and call `load_wiki(root)` from the existing map builder instead of duplicating its project-table, evidence, inventory, and Markdown-link parsing.
- [ ] Add `include_aliases: bool = False` to `load_wiki()`. Only when true, validate each skill page's `aliases` frontmatter as a string list and add it to the returned skill record; have the graph call `load_wiki(root, include_aliases=True)`. The default call must preserve the current explorer's data and output.
- [ ] Convert each project to a stable node ID equal to its wiki-relative page path, such as `projects/project-name.md`; convert each canonical skill to `skills/skill-name.md`.
- [ ] Keep a separate graph node for every project. For an approved multi-page group, use `alias:` followed by the sorted member paths joined with `|` as its stable ID; for a one-page display-label entry, keep that skill path as its ID. Preserve every original skill path, title, definition, and wiki link on the node. Leave non-grouped skills as individual nodes using their wiki titles.
- [ ] Convert each parsed relationship to an edge without dropping fields:

```python
{
    "source": project_path,
    "target": graph_skill_id,
    "kind": relationship["kind"],
    "status": relationship["status"],
    "rationale": relationship["rationale"],
    "evidence": relationship["evidence"],
}
```

- [ ] Preserve `source_inventory`, project `source_reviews`, `unmapped_claims`, and `data_quality_notes` in the graph data for the detail panel.
- [ ] Keep project requirements, source evidence, and user-reported relationships distinct. Never infer a personal relationship from requirements, project membership, or source evidence.
- [ ] Add graph-data validation: each edge endpoint exists, provenance/status pairs match `AGENTS.md`, all skill-page paths in groups exist, and unmatched claims remain in project detail data rather than becoming graph skill nodes.
- [ ] Create stable, sorted output by node ID, relationship endpoints/kind/status, and source path; preserve relationship multiplicity when one project/skill pair has more than one provenance.

### Task 3: Implement canvas layout and graph rendering

**Files:**
- Create: `scripts/skill_graph_template.html`

- [ ] Create a semantic page titled **AI Skills & Projects** with one canvas, a search field, independent provenance controls, an accessible legend, a detail panel, and an empty/error status region. Keep all CSS and JavaScript inline and include one replaceable JSON data marker.
- [ ] Implement canvas sizing using `devicePixelRatio`, then implement force ticks with pairwise repulsion cut off by distance, spring links, weak center gravity, velocity damping, and an alpha floor. Use the graph skill's baseline values: repulsion cutoff around 300 px, spring rest length around 85 px, damping around 0.82, and alpha floor around 0.03.
- [ ] Distinguish project and skill nodes by shape. Style each relationship using both color and pattern: documented evidence solid violet, inferred evidence dashed violet, unknown evidence dotted neutral, user-reported solid green, and requirements dashed amber.
- [ ] Draw same-endpoint relationships as slightly offset edges; toggling one provenance must not hide or remove another relationship between the same nodes.
- [ ] Make force simulation and node sizing derive from visible relationships. Size skill nodes by distinct connected-project count in the active filters and label this as project coverage, not proficiency.

### Task 4: Add graph interaction, details, and accessible controls

**Files:**
- Modify: `scripts/skill_graph_template.html`

- [ ] Implement node dragging, background pan, cursor-anchored wheel zoom, hover-neighbor highlighting, click selection, and search that retains matching nodes and their neighbors.
- [ ] Implement independent relationship filters and update only visible edges and project-coverage node sizes when a filter changes.
- [ ] Limit labels to project nodes and hovered, selected, searched, or sufficiently zoomed nodes. Keep full titles in the detail panel.
- [ ] On selection, render project/skill definitions, all connected relationships, statuses, rationales, citations, source-review records, unmapped claims, data-quality notes, and original wiki-page links. Use `textContent` or equivalent text-only insertion for all wiki content.
- [ ] Add a light theme using `prefers-color-scheme`, visible focus styles, keyboard-operable controls, responsive layout, and explicit empty/error states.

### Task 5: Add Markdown loading and safe HTML generation

**Files:**
- Modify: `scripts/skill_graph_template.html`
- Modify: `scripts/build_skill_graph.py`

- [ ] Add a drop target and file picker that accept Markdown project and skill notes. Establish each dropped note's virtual wiki path from its frontmatter type and file name, then resolve ordinary relative Markdown links from that path.
- [ ] Implement browser parsing for the wiki's YAML frontmatter, required project sections, supported Markdown table headers, and skill-page user-reported project lists. Keep the supported grammar explicit; reject malformed rows and unsupported statuses with a readable error.
- [ ] Require each dropped project/skill note set to resolve every project and skill page referenced by its parsed relationships. Source citations may target source notes that are not included in the drop batch; preserve their wiki-relative links and rely on the embedded inventory snapshot for review status.
- [ ] Build dropped data in temporary state; replace the visible graph only after the batch parses and validates. On error, show the failing file/section/row and leave the current graph and selection data unchanged.
- [ ] Preserve evidence-status and citation text in dropped data. Retain page-relative wiki URLs for detail links. Treat embedded source-inventory data as the generated baseline; the Python builder is required to refresh inventory changes.
- [ ] Reuse `_safe_json()` from `scripts/build_skill_map.py` to serialize sorted graph data, escaping `<`, `>`, `&`, U+2028, and U+2029 before insertion into the template. Ensure page text is never interpolated as executable HTML.
- [ ] Render fully before writing. Write to a temporary file in the destination directory, then atomically replace the target only after the write succeeds; clean up the temporary file on failure so an existing graph is preserved.

### Task 6: Integrate the generated graph and validate it

**Files:**
- Modify: `scripts/build_skill_graph.py`
- Create: `wiki/skill-graph.html`
- Modify: `wiki/index.md`
- Modify: `wiki/log.md`

- [ ] Add a CLI with `--root PATH` defaulting to the project root inferred from `__file__`, and `--output PATH` defaulting to `wiki/skill-graph.html`. Print a clear error to stderr and exit 1 on invalid input; exit 0 after writing the graph.
- [ ] Add `[AI Skills & Projects](skill-graph.html)` near the top of `wiki/index.md`, preserving the existing `[Interactive skill map](skill-map.html)` link.
- [ ] Append a dated `wiki/log.md` entry recording the graph builder, offline output, provenance separation, manual validation, unchanged inventory, and remaining source-review status.
- [ ] Run `python3 scripts/build_skill_graph.py`; confirm it exits 0 and reports 29 project nodes and 227 canonical skill pages before any cross-page groups are added.
- [ ] Confirm the loader accounts for all 321 requirement rows and all 158 source-evidence rows: 307 requirement rows and 51 source-evidence rows become edges, 14 requirements and 106 source-evidence claims remain in project details, and the one invalid source-evidence/user-reported row remains a data-quality note. Confirm all 31 user-reported links remain distinct.
- [ ] Confirm all 53 source-inventory rows and their current `needs review` statuses remain represented; do not claim source review is complete.
- [ ] Run `python3 scripts/build_skill_graph.py`, record `shasum -a 256 wiki/skill-graph.html`, run the builder again, and compare the new SHA-256 value; identical wiki and alias inputs must produce identical HTML.
- [ ] Open `wiki/skill-graph.html` directly from disk with networking unavailable. Manually check default filters, requirements toggle, separate same-pair edges, search/focus, drag/pan/zoom, details, citations, source warnings, light/dark theme, keyboard focus, and responsive layout.
- [ ] Drop valid project/skill Markdown files and confirm parsed relationships preserve provenance. Then drop an existing `wiki/sources/*.md` page (an unsupported note type) and confirm an explicit error appears while the prior graph remains unchanged.
- [ ] Resolve the generated index link, project/skill/source links, and citation fragments. Confirm `wiki/skill-map.html` still exists and `wiki/source-inventory.csv` is unchanged.

No automated test files or test-case files are added; use the focused build and manual checks above.
