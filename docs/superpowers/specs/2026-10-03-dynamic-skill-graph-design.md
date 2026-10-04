# Dynamic AI Skills Graph Design

## Goal

Create a concise, interactive force-directed graph of the AI project wiki so
recurring skills can be explored now and compiled into a portfolio later. Keep
the wiki as the authoritative source and preserve the difference between
project requirements, source evidence, and user-reported capabilities.

## Decision

Build a shared project–skill network as a standalone, offline HTML page. Each
canonical skill is represented by one shared node connected to every project
that references it; an explicitly reviewed equivalence group may share one
graph node while retaining all original wiki pages. The default view shows
source-evidenced and user-reported relationships; project requirements are
available through a separate filter and are hidden initially.

Do not invent skill domains, proficiency levels, or rankings. Normalize only
clear aliases, not related-but-distinct skills. Keep original wiki titles,
claims, statuses, and citations available from graph details.

## Data and provenance

- Project Markdown, canonical skill pages, and `wiki/source-inventory.csv`
  remain authoritative. The graph is a generated view and does not rewrite
  claims or source records.
- Each project–skill edge retains its provenance and status:
  - **Project requirement**: from `Know-how needed`; retain `suggested` or
    `user-confirmed`.
  - **Source evidence**: from `Skills shown by sources`; retain
    `documented`, `inferred`, or `unknown`, plus source citations.
  - **User-reported use**: from the skill page's `Projects with user-reported
    use` list; retain the user-reported label.
- Source evidence means a method or skill is represented in project material;
  it does not establish the user's individual contribution. Requirements are
  not evidence of personal experience. The interface will state this
  distinction in its legend and details.
- Keep unmatched project claims in project details with their existing
  provenance; do not invent skill nodes for them.
- Existing, explicitly declared wiki aliases may be used. Any additional
  cross-page equivalence must be recorded in a graph-only alias map and
  individually reviewed. No fuzzy matching or automatic umbrella grouping.
  Alias mappings affect graph aggregation and labels only; they do not merge or
  rename wiki pages.
- Node size represents the number of distinct projects connected through the
  currently visible relationship types. Label it as project coverage, never as
  proficiency or strength.

## Architecture and data flow

- Add a Python standard-library builder under `scripts/` that reuses the
  existing wiki parser in `scripts/build_skill_map.py`, rather than
  reimplementing the project-table and evidence rules.
- The builder validates wiki page types, required sections, relationship
  statuses, local links, and alias-map references before rendering.
- Generate `wiki/skill-graph.html` with embedded data and inline CSS/JavaScript.
  Title it **AI Skills & Projects**. The page makes no network requests and
  requires no server or external packages. Keep the existing
  `wiki/skill-map.html` explorer unchanged.
- Provide a client-side Markdown drop-in loader for wiki project and skill
  notes, adapted to the wiki's frontmatter, tables, and ordinary Markdown
  links. Resolve local links from each note's virtual wiki path so detail links
  still target the corresponding page under `wiki/`. It must preserve
  provenance and citation text. If parsing or validation fails, report the
  error and keep the currently displayed graph. Re-running the Python builder
  remains the canonical way to refresh the complete graph.
- Link the generated graph from `wiki/index.md` and record its scope and
  validation in `wiki/log.md`.

## Graph presentation and behavior

- Use a device-pixel-ratio-aware canvas and a gently moving force layout with
  bounded repulsion, spring links, center gravity, and damping. Keep the
  initial graph responsive at the current scale of 29 projects and 227
  canonical skills; if future data grows beyond the graph skill's approximate
  300-node performance threshold, use a spatial grid or equivalent bounded
  neighbor search.
- Distinguish project and skill nodes by shape. Use edge color and pattern,
  plus a visible legend, to distinguish documented, inferred, unknown,
  user-reported, and requirement relationships.
- Render multiple relationship types between the same project and skill as
  individually filterable, slightly offset edges so none are hidden beneath
  another.
- Use a restrained dark palette with a readable light-mode variant that
  follows the operating-system preference. Do not rely on color alone.
- Keep the default canvas uncluttered: show project labels and labels for
  hovered, selected, searched, or sufficiently zoomed nodes. Search matches
  retain their neighboring nodes.
- Support node dragging, background pan, cursor-anchored zoom, hover-neighbor
  highlighting, search, independent provenance filters, and click selection.
- A semantic detail panel shows the selected project's or skill's full title,
  definition, connected nodes, relationship status, rationale, source review
  status where available, citations, and local wiki links. Render wiki text as
  text, not executable HTML.
- Surface corpus and per-project source-review status from the inventory so
  unreviewed sources are not mistaken for fully reviewed evidence.
- Provide keyboard-operable controls, visible focus, responsive layout, and
  explicit empty/error states.

## Refresh and failure behavior

Run the builder from the project root. It deterministically replaces the
generated graph from the current wiki and alias map. Missing required sections,
unsupported table shapes, invalid statuses, broken links, or invalid alias
references must produce a clear non-zero error; never silently omit
relationships or substitute defaults.

The drop-in loader accepts Markdown using the same wiki conventions. Invalid
or incomplete input must leave the current graph intact and identify the
problem. The HTML remains usable offline after it is generated.

## Validation and acceptance criteria

- The generated HTML opens directly from disk and works without network access.
- Every graph edge maps to a valid wiki relationship with the original
  provenance, status, and available citations; no requirement is presented as
  personal experience.
- Alias aggregation is deterministic, uses only explicit mappings, and keeps
  all original wiki page links accessible.
- Unmapped claims remain project details and do not become inferred canonical
  skill nodes.
- Provenance filters, search and neighbor focus, drag/pan/zoom, detail links,
  citation display, keyboard controls, and light/dark themes work.
- Markdown drop-in behavior is checked for valid project/skill pages,
  malformed pages, and preservation of the existing view after an error.
- Local links resolve, all expected project and skill pages are accounted for,
  unreviewed-source status is visible, and repeated builds from identical
  inputs produce identical HTML.
- Do not add test-case files; perform focused manual validation of the graph
  against wiki records.

## Scope exclusions

- Do not edit, move, or delete anything under `raw/`.
- Do not add inferred domain clusters, broad concept rollups, proficiency
  scores, rankings, recommendations, or personal-contribution claims.
- Do not change canonical wiki titles or combine distinct skill meanings.
- Do not replace or remove the existing project–skill explorer.
- Do not use external libraries, network services, or hosted data.

## Files

- Create `scripts/build_skill_graph.py` and a graph-only alias map if approved
  mappings are needed.
- Create generated `wiki/skill-graph.html`.
- Modify `wiki/index.md` and `wiki/log.md` to link and record the graph.
- Keep this design in `docs/superpowers/specs/`; do not duplicate its
  implementation detail in source records or skill profiles.
