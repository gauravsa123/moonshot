# Interactive Wiki Skill Map Implementation Plan

> **For agentic workers:** The user chose inline execution and explicitly requested no test cases. Implement the steps below, then perform the documented manual validation.

**Goal:** Generate an offline, searchable HTML explorer that maps canonical skills to wiki projects while keeping requirements, source evidence, and user-reported capabilities separate.

**Architecture:** A Python 3 standard-library script parses project profiles, skill pages, and the source inventory into validated relationship data, then emits a self-contained HTML page with embedded data, CSS, and JavaScript. Markdown remains authoritative; the generated map is linked from the wiki index and recorded in the activity log.

**Tech Stack:** Python 3 standard library (`pathlib`, `csv`, `json`, `argparse`), standalone HTML/CSS/JavaScript.

---

## File map

- Create `scripts/build_skill_map.py` — parse/validate wiki records, render embedded data and explorer UI, and write `wiki/skill-map.html`.
- Create `wiki/skill-map.html` — generated output, not hand-edited.
- Modify `wiki/index.md` — prominent link to the generated map.
- Modify `wiki/log.md` — record generated output and validation without changing source-review statuses.

The approved design is in `docs/superpowers/specs/2026-10-03-skill-map-design.md`. Do not modify `raw/` or canonical project/skill claims for this derived view. Do not add tests or test cases.

### Task 1: Parse and validate wiki relationship data

**Files:**
- Create: `scripts/build_skill_map.py`
- Read: `AGENTS.md`, `wiki/projects/*.md`, `wiki/skills/*.md`, `wiki/source-inventory.csv`

- [ ] Read `AGENTS.md` and follow its provenance rules.
- [ ] Discover project and skill pages from their respective wiki directories in sorted path order. Read title and definition from page metadata/content.
- [ ] Parse project `Know-how needed` and `Skills shown by sources` tables. Parse user-reported relationships only from each skill's `Projects with user-reported use` list.
- [ ] Accept the wiki's equivalent table headings (`Skill`, `Skill requirement`, or `Skill candidate` with `Review status` or `Status`; and `Skill`, `Skill or capability`, `Capability`, or `Claim` with `Evidence status` or `Status`).
- [ ] Create distinct relationship types: `requirement` with `suggested`/`user-confirmed` status; `source_evidence` with `documented`/`inferred`/`unknown` status; and `user_reported` with `user-reported` status. Never infer personal use from project requirements or source evidence.
- [ ] For project-table rows whose first cell has no canonical skill link, retain the text as a project-level entry in `unmapped_claims`, with its provenance kind, status, rationale/evidence text, and citations. Label it “Not mapped to a canonical skill”; do not invent a canonical relationship.
- [ ] If a row's status is invalid for its table (such as `user-reported` in source evidence), retain its original row text/status in `data_quality_notes` on that project. Exclude it from provenance relationships and counts; do not silently relabel or discard it.
- [ ] Resolve Markdown links relative to the page containing them, validate that local targets exist and remain inside `wiki/`, then normalize links relative to `wiki/skill-map.html`.
- [ ] Extract citation links from both requirement rationales and source-evidence cells. Keep requirement rationale citations separate from source-evidenced-skill relationships.
- [ ] Join each project's source references to the inventory by source wiki page path. Return all inventory rows for corpus-wide counts and include linked source statuses/reasons on each project. Normalize inventory `wiki_page` values such as `wiki/sources/name.md` to `sources/name.md`.
- [ ] Reject missing required sections, malformed non-empty table rows, unsupported status values, malformed inventory rows, and broken/out-of-wiki links with a clear `MapBuildError`. Do not silently omit invalid records.
- [ ] Return data with top-level `source_inventory`, `projects`, `skills`, and `relationships` lists. Each project contains `unmapped_claims` and `data_quality_notes`; each canonical-skill relationship contains `project_path`, `skill_path`, `kind`, `status`, `rationale`, and cited `evidence` links.

### Task 2: Render the standalone searchable explorer

**Files:**
- Modify: `scripts/build_skill_map.py`

- [ ] Implement `render_html(data) -> str` with all CSS, JavaScript, and data embedded. Do not load external libraries or make network requests.
- [ ] Add searchable Projects and Skills views, independent checkboxes for the three relationship types, a selectable entity list, and a details region.
- [ ] In the project detail, group related skills by provenance and show requirement status/rationale, rationale references, source-evidence status/citations, user-reported labels, and source-review statuses/reasons.
- [ ] Include unlinked requirements and source-evidence rows under their matching provenance heading, clearly labeled “Not mapped to a canonical skill.”
- [ ] Display inconsistent-provenance rows in a separate “Wiki data-quality notes” section, outside all three provenance filters.
- [ ] In the skill detail, show its definition and linked projects grouped by the same provenance types. Show explicit empty states, including “No user-reported use recorded.”
- [ ] Derive the corpus review counts/banner from all inventory rows, including rows not referenced by a project. Display source review reasons without implying an unreviewed source is complete.
- [ ] Keep text provenance labels visible when filters are active; do not communicate categories by color alone. Use semantic controls, keyboard-operable selection, responsive layout, and text-only DOM insertion for wiki-derived content.
- [ ] Serialize embedded JSON safely so wiki text cannot terminate the data element or become executable markup.

### Task 3: Generate, integrate, and manually validate the map

**Files:**
- Modify: `scripts/build_skill_map.py`
- Create: `wiki/skill-map.html`
- Modify: `wiki/index.md`
- Modify: `wiki/log.md`

- [ ] Implement `build_map(root)` to parse and render fully before writing UTF-8 to `wiki/skill-map.html`. Use stable ordering and JSON serialization so identical wiki input produces identical HTML.
- [ ] Add CLI option `--root PATH`, defaulting to the repository root inferred from the script location. Print `MapBuildError` to stderr and return exit code 1 on invalid wiki input; return 0 on success. A parse/render error must not replace the previous map.
- [ ] Add `[Interactive skill map](skill-map.html)` near the top of `wiki/index.md`.
- [ ] Append a dated maintenance entry to `wiki/log.md` naming the map, generator, provenance separation, and manual validation. State that the inventory remains unchanged and source review remains incomplete; do not claim all source files were visually reviewed.
- [ ] Run `python3 scripts/build_skill_map.py`; confirm it exits 0 and creates `wiki/skill-map.html`.
- [ ] Run the generator a second time and compare the artifact contents; they must be identical.
- [ ] Open `wiki/skill-map.html` directly in a browser with networking unavailable. Manually confirm project and skill search, both views, each independent provenance filter, citations, empty states, corpus and project review warnings, and links back to wiki pages.
- [ ] Check that the generated map links resolve to existing project, skill, and source pages; confirm the index link resolves and `wiki/source-inventory.csv` was not changed.
- [ ] Confirm every project relationship-table row appears either as a canonical-skill relationship or as a labeled project-level entry, with none silently dropped.
- [ ] Confirm rows with invalid provenance/status combinations appear only as data-quality notes, not relationships.

No commit step is included: the current workspace is not a Git repository.
