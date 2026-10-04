# Wiki maintenance contract

This file defines how to create, update, query, and check the Markdown wiki in
`wiki/`. The Markdown pages are authoritative; `raw/` is an immutable source
archive. Do not edit, rename, move, or delete anything under `raw/`.

## Page metadata

Every wiki page uses YAML frontmatter with these common keys:

```yaml
---
id: stable-page-id
type: project
title: Human-readable title
aliases: []
related: []
source_refs: []
---
```

- `id` is a stable, unique identifier; do not change it just to rename a page.
- `type` is exactly one of `project`, `source`, `concept`, or `skill`.
- `title` is the page's human-readable title.
- `aliases` lists alternate names, not unconfirmed equivalences.
- `related` contains relative Markdown links to related wiki pages.
- `source_refs` contains relative links to the source pages supporting the
  page. Include page or slide fragments when available.

Use ordinary relative Markdown links. Keep source references traceable from the
wiki to the corresponding original file path recorded on its source page.

## Evidence and claims

Use these evidence labels for source claims, including skills shown by sources:

- `documented`: the source directly states or depicts the claim.
- `inferred`: the claim is a reasoned interpretation of cited source material;
  mark it explicitly as an inference.
- `unknown`: the available evidence does not establish the claim.

Record source-evidenced claims in an Evidence table with columns `Claim`,
`Status`, and `Evidence`. `documented` and `inferred` claims must link to the
supporting source page and include page or slide locations whenever available.
Do not present an inference as documented fact. Leave unsupported personal role
or contribution details as `unknown`; do not infer them from filenames, titles,
or project requirements.

User-confirmed statements about personal contributions, capabilities, or
outcomes have a separate provenance/status, `user-reported`. This is not a
source-evidence status and must never be relabeled `documented` or `inferred`
unless independent source evidence supports the claim. Attribute these
statements as user reports, retain their qualifications, and do not embellish
them. Project requirements remain separate from both source-evidenced claims
and user-reported personal claims.

## Project skill profiles

Every project page keeps the following three sections distinct:

## Know-how needed

List capabilities useful or necessary to work on the project. These are
project requirements, not claims about the user's personal experience.

| Skill | Review status | Rationale |
|---|---|---|
| [Candidate skill](../skills/candidate-skill.md) | suggested | Why it may be useful for this project |

The only review statuses are `suggested` and `user-confirmed`. Suggest domain-
relevant candidates with a brief rationale, then ask the user to confirm, edit,
or reject them before treating accepted terms as canonical skill taxonomy
entries. The user may add, remove, rename, or regroup suggestions. Remove
rejected suggestions; do not retain them as skill requirements or count them.
Never treat a suggested or user-confirmed requirement as proof that the user
personally demonstrated that skill.

## Skills shown by sources

List only skills supported by source evidence, separately from know-how needs.

| Skill | Evidence status | Evidence |
|---|---|---|
| [Skill](../skills/skill.md) | documented | [Source](../sources/source-page.md#slide-3) |

Use only `documented`, `inferred`, or `unknown` as evidence statuses, following
the evidence rules above. A required skill is not automatically a demonstrated
skill. Unknown personal contribution remains unknown until evidence or explicit
user confirmation establishes it.

## User-reported contributions and outcomes

Record user-confirmed personal contributions, capabilities, and outcomes
separately from project requirements and source-evidenced skills. Use
`user-reported` as their provenance/status until independent source material
corroborates them; do not put them in a source Evidence table as documented or
inferred claims. Attribute statements to the user and avoid upgrading a user's
characterization into an independently asserted fact. Outcomes such as
publications or trade secrets are recorded here, not as skill pages.

| Contribution or outcome | Status | Details |
|---|---|---|
| User-reported item | user-reported | User-confirmed description; not source-corroborated |

## Canonical skill pages

Each canonical skill page has the common frontmatter and a brief definition.
List aliases and parent/related skill links, and keep these project lists
separate:

```markdown
## Projects needing this skill

## Projects with user-reported use

## Projects showing this skill
```

The first list links project pages where the skill is in the reviewed
know-how-needed profile; the second links projects where the user reported
using or demonstrating the capability; the third links projects whose sources
show the skill, with evidence links/statuses. Do not combine similar skill
terms, rename one as an alias of another, or otherwise merge their meanings
without the user's confirmation.

## Ingestion and review

Process exactly one leaf project/topic folder at a time. A leaf folder is a
folder containing source files to be considered together. After each folder,
present the know-how-needed suggestions and wait for the user's confirmation or
edits before starting the next folder. Defer the full source/page quality review
until all folders have been processed; accumulate extraction limitations,
conflicts, and validation findings for that consolidated review.

For every source file, record exactly one inventory status:

- `processed` when its contents were successfully reviewed and represented.
- `needs review` when extraction is incomplete, ambiguous, or needs human
  inspection; state the reason.
- `blocked` when it could not be processed; state the reason.

Every `needs review` or `blocked` entry must have a useful reason. Do not count
either as processed. Do not guess source contents from filenames. If a source
cannot be read reliably, report that limitation rather than filling gaps.

For each leaf folder:

1. Review its source files without modifying `raw/`; create or update source
   records with exact original paths, status/reason, readable summaries when
   supported, and page/slide citations when available.
2. Create or update the related project page, keeping know-how candidates,
   source-evidenced skills, and user-reported contributions/outcomes separate.
   Suggest domain-relevant know-how skills with rationales and ask the user to
   confirm or edit the list before marking items `user-confirmed` or
   canonicalizing accepted skills. Record role/contribution details as
   `unknown` unless explicitly user-reported or supported by source evidence;
   use `user-reported` for user reports, not source evidence statuses.
3. Update the relevant concept and canonical skill pages only when supported
   by evidence or accepted in user review. Maintain links and the separate
   project lists on skill pages.
4. Update `wiki/source-inventory.csv`, `wiki/index.md`, and `wiki/log.md`
   alongside the linked page changes. Keep inventory paths exact and statuses
   consistent with the source records. Index all created or updated pages.
5. Present the project's know-how suggestions and rationale; wait for the
   user's confirmation, removal, rename, regrouping, or additions before
   starting the next leaf folder. Record source statuses, evidence questions,
   and page changes for the final consolidated review rather than asking for a
   full source/page audit after each folder.

### Incremental ingestion

Apply the same one-leaf-folder workflow to new or changed source files. Update
existing pages without silently overwriting earlier conclusions; preserve and
surface conflicting evidence for review. Update the inventory, linked pages,
index, and log together.

## Queries and health checks

For a wiki query, start at [`wiki/index.md`](wiki/index.md), then consult
relevant pages. Cite the wiki pages and source references used in the answer.
File an answer into the wiki only when the user requests it.

A health check reports broken links or source references, unindexed or orphan
pages, unsupported claims, conflicts, stale conclusions, and unreviewed
inferences. Report findings without silently rewriting disputes or changing
conclusions; ask for review where needed.

## Example

The following is an illustrative schema example only. Its linked paths are
placeholders, not claims that these pages or source ingestions exist.

```yaml
---
id: example-project
type: project
title: Example project
aliases: []
related:
  - ../skills/example-skill.md
source_refs:
  - ../sources/example-source.md#slide-3
---
```

```markdown
## Know-how needed

| Skill | Review status | Rationale |
|---|---|---|
| [Example skill](../skills/example-skill.md) | suggested | The project description may call for this capability; ask the user to review. |

## Skills shown by sources

| Skill | Evidence status | Evidence |
|---|---|---|
| [Example skill](../skills/example-skill.md) | documented | [Example source](../sources/example-source.md#slide-3) |
```
