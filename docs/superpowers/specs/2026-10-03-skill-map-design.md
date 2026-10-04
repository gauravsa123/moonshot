# Interactive Wiki Skill Map Design

## Goal

Create an offline, searchable HTML explorer that maps the wiki's canonical AI
skills to projects while keeping project requirements, source-evidenced skills,
and user-reported capabilities visibly and semantically separate.

## Decision

Build a project–skill explorer rather than a node-link graph. With 29 projects
and 227 skills, a dense graph would make relationships difficult to inspect.
The explorer will let readers pivot between projects and skills, filter by
provenance, and follow links back to the authoritative wiki records.

## Architecture

- Markdown project profiles, canonical skill pages, and `wiki/source-inventory.csv`
  remain the source of truth. The map is a generated view; it is not a second
  place to edit claims or relationships.
- A Python 3 standard-library generator reads the wiki and emits one
  self-contained `wiki/skill-map.html`. The generated page uses embedded data
  and local JavaScript/CSS only: it makes no network requests and requires no
  server or external package.
- The generator reads each project profile's `Know-how needed` and
  `Skills shown by sources` tables, and each skill page's separate project
  lists. It reads source review status and reasons from the inventory.
- The map is linked from `wiki/index.md`; its generation and validation are
  recorded in `wiki/log.md`.

## Relationship model and provenance

Canonical-skill relationships connect a project page and a canonical skill
page and have one of these types:

1. **Project requirement** — taken only from `Know-how needed`; retain the
   `suggested` or `user-confirmed` review status and rationale.
2. **Source-evidenced skill or method** — taken only from `Skills shown by
   sources`; retain the `documented`, `inferred`, or `unknown` evidence status
   and the source links, including fragments and page/slide locations.
3. **User-reported capability** — taken only from the canonical skill page's
   `Projects with user-reported use` list. Present it as user-reported and link
   to the project and skill pages.

These are separate relationships, not confidence levels or stages in a
proficiency ladder. A requirement is never treated as personal experience.
The map does not infer capability from project membership, source content,
or a requirement. User-reported project outcomes that are not represented as
canonical skills are outside this skill map.

Some project profiles contain requirement or source-evidence table rows that
are not linked to a canonical skill page. Preserve these as project-level
entries under the same provenance category, with their original status,
description, and citations, and label them **Not mapped to a canonical skill**.
Do not invent canonical links, merge them into similar skill pages, or present
them as canonical-skill relationships.

If a project table uses a provenance status that is invalid for that section
(for example, `user-reported` in `Skills shown by sources`), do not convert it
to another relationship type or count it as source evidence. Preserve the
original row as a visible wiki data-quality note on the project detail,
explaining the inconsistent section/status; keep that note outside the three
provenance filters.

## Explorer behavior

- Provide **Projects** and **Skills** views with searchable lists. Selecting a
  project shows its linked skills grouped under the three provenance headings;
  selecting a skill shows its linked projects grouped the same way.
- Provide independent on/off filters for the three relationship types. Keep
  the provenance label visible when filters are used; color is not the only
  distinction.
- Show project and skill names, canonical definitions, relationship status,
  requirement rationale, source evidence citations, and links to the
  corresponding wiki pages where those fields exist. Preserve wiki citations
  embedded in requirement rationales as rationale references, without
  reclassifying a requirement as source evidence.
- Show every unlinked requirement and source-evidence table row on its project
  detail under the matching provenance heading, labeled as not mapped to a
  canonical skill; preserve its status, rationale/evidence text, and citations.
- Show malformed provenance rows as clearly labeled wiki data-quality notes,
  not as relationships in any of the three categories.
- Indicate source-review incompleteness at both corpus and project level:
  report inventory statuses and reasons for sources referenced by each
  project. Do not imply that a source has been fully reviewed merely because
  a wiki record exists.
- Show explicit empty states such as “No user-reported use recorded” rather
  than interpreting missing data as evidence that a capability was not used.
- Support keyboard navigation, semantic controls, readable contrast, and
  responsive layouts. Render wiki-derived text as text, not executable HTML.

## Refresh and failure behavior

Run the generator from the repository root with:

```sh
python3 scripts/build_skill_map.py
```

It replaces `wiki/skill-map.html` deterministically using the current wiki.
Missing required sections, malformed relationship rows, missing linked pages,
or unrecognized provenance/status values must produce a clear non-zero error;
the generator must not silently omit invalid relationships or substitute
success-shaped defaults.

## Validation and acceptance criteria

- The generated HTML opens directly from disk in a browser and remains
  functional without network access.
- Project and skill entries resolve to existing wiki pages. Every displayed
  relationship or project-level entry traces to its source Markdown row/list
  and retains the appropriate category and status.
- Rows with invalid provenance/status combinations remain visible as data
  quality notes and are excluded from relationship counts and filters.
- Filter combinations, project/skill search, selection details, empty states,
  citation links, and incomplete-review indicators work as specified.
- Generation is repeatable: identical wiki inputs produce identical HTML.
- Automated checks compare parsed map relationships with their Markdown
  sources, verify local links and category separation, and detect malformed
  or omitted relationships.
- The map makes no proficiency rating, ranking, or personal-mastery claim.

## Scope exclusions

- Do not modify files under `raw/`.
- Do not add inferred domain clusters, skill scores, proficiency levels,
  rankings, recommendations, or claims of individual contribution.
- Do not add user-reported outcomes unless they are already represented as
  canonical skill relationships in the wiki.
- Do not use external JavaScript/CSS libraries or host the map as a service.

## Files

- Create `scripts/build_skill_map.py` — validates and converts wiki records to
  the embedded map data and HTML.
- Create `wiki/skill-map.html` — generated, standalone interactive map.
- Modify `wiki/index.md` — add a prominent map link.
- Modify `wiki/log.md` — record the map's scope, provenance treatment, and
  validation outcome.
- Keep this design in `docs/superpowers/specs/`; do not duplicate its
  implementation detail in source records or skill profiles.
