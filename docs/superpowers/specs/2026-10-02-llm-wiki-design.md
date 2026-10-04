# LLM Wiki Design

## Goal

Create a persistent, source-grounded Markdown wiki from the AI project archive in `raw/`. The wiki should accumulate and connect knowledge across projects, then provide a reliable foundation for later AI skill maps, charts, and portfolio material.

The design follows the persistent-wiki pattern described in Andrej Karpathy's personal knowledge-base gist: immutable raw sources, an LLM-maintained wiki, and explicit instructions for ingestion and upkeep. It also adopts Graphify's emphasis on entities and relationships, while keeping the Markdown wiki—not a separate graph database—as the canonical knowledge layer.

## Scope

The first milestone builds and populates the wiki from the existing archive, processing one project/topic folder at a time. The user reviews and updates each project's know-how profile before the next folder; detailed source/page quality review is consolidated at the end. Each project page gets a user-curated profile: the LLM suggests skills needed to work on the project, and the user can accept, remove, rename, regroup, or add skills. The wiki also supports future incremental ingestion.

The initial milestone does not build the portfolio, skill chart, or a standalone graph application. It records enough consistent, source-linked information for those to be generated later as derived views.

## Architecture and information model

- `raw/` remains the immutable source archive. The LLM reads it but does not modify it.
- A root `AGENTS.md` defines the wiki structure, metadata conventions, evidence rules, and workflows for ingestion, querying, and maintenance.
- `wiki/` contains the persistent Markdown knowledge base:
  - `index.md`: categorized catalog of wiki pages and short descriptions.
  - `log.md`: append-only record of ingestions, queries filed on request, and health checks.
  - `projects/`: evolving synthesis pages for project/topic folders.
  - `sources/`: one record page per source document, with a summary when readable, processing status and any failure reason, and a link to the original relative path.
  - `concepts/`: shared AI concepts and methods identified across projects.
  - `skills/`: a reusable, user-refined AI skill taxonomy and its skill pages.
- Pages use ordinary Markdown links and consistent frontmatter so they remain portable and can be browsed with tools such as Obsidian. Graph views and later portfolio/map outputs are derived from page links and metadata; they are not independently maintained sources of truth.

Frontmatter records stable IDs, page type, taxonomy/category, aliases, related pages, and source references as applicable. Each project page keeps three distinct views:

- **Know-how needed:** candidate skills required or useful to work on the project. The LLM proposes these based on project material and domain context; each remains a suggestion until the user confirms or edits it. The user can add, remove, rename, or regroup skills. Reuse canonical skill pages and aliases when suitable.
- **Skills shown by sources:** skills that the documents indicate were used or demonstrated. These have source citations and an evidence status. A project's required-skill suggestions must not be presented as proof that the user personally demonstrated those skills.
- **User-reported contributions and outcomes:** personal capabilities, contributions, and outcomes confirmed by the user. Record these with a separate `user-reported` provenance/status, not as `documented` or `inferred` source evidence. Attribute them to the user, preserve their qualifications, and do not independently assert an uncorroborated characterization such as “state-of-the-art.” Outcomes are not skill pages.

Claims attributed to sources about a skill, tool, method, outcome, or personal contribution have an evidence status:

- `documented`: directly supported by a cited source.
- `inferred`: a reasonable interpretation that is explicitly labeled as inferred and linked to its supporting evidence.
- `unknown`: not established by the sources. Personal role or contribution details may be separately recorded as user-reported when confirmed by the user, but that confirmation does not change source-evidence status.

`user-reported` is a separate provenance/status for user-confirmed personal
claims; it is not one of the source evidence statuses. A user report remains
user-reported unless corroborating source evidence is separately established.

The initial skill taxonomy is proposed from project evidence and domain-relevant know-how, then refined by the user during project-by-project review. Related skills should be connected without forcing every project into a preselected framework.

Canonical skill pages aggregate projects under three separate headings:
**Projects needing this skill** for reviewed project requirements, **Projects
with user-reported use** for capabilities or contributions reported by the
user, and **Projects showing this skill** only for source-supported claims.
User reports are not source evidence. Project-reported contributions may have
skill pages; outcomes such as publication or trade-secret status do not.

### Engineering Drawing Agents user-reported records

The following confirmed personal contribution/capability records and outcomes
are attributed to the user and use `user-reported` provenance, not source
evidence. The complex graph-workflow description is the user's
characterization, not an independently asserted “state-of-the-art” claim.

| Contribution or capability | Provenance |
|---|---|
| Working under total uncertainty | user-reported |
| Developing methodology from scratch | user-reported |
| Inventing a complex workflow for graph creation, characterized by the user as state-of-the-art | user-reported |
| Making drawing data extraction robust and reliable | user-reported |
| Deciding the project roadmap | user-reported |
| Guiding a junior data scientist | user-reported |
| Communicating with a stakeholder to pitch the workflow for the stakeholder's problem | user-reported |
| Converting the work from AI exploration to delivery/deployment | user-reported |
| Understanding complex research papers and adapting implementation to the topic | user-reported |
| Proposing a broader, efficient engineering-drawing database | user-reported |

| Outcome | Provenance |
|---|---|
| Trade secret | user-reported |
| Publication | user-reported |

## Ingestion and maintenance workflow

### Initial archive

1. Inventory the source files under `raw/`, grouping them by their existing project/topic folders.
2. Process one folder at a time. For each source, extract and summarize readable content, create or update its source page, and cite the original relative path and page/slide locations when available.
3. Integrate the source summaries into the relevant project, concept, and skill pages. On the project page, separately list know-how needs, source-evidenced skills, and user-reported contributions/outcomes. Present suggested skills to the user so they can confirm, add, remove, rename, or regroup them before treating them as canonical. Update cross-links and `index.md`; append an entry to `log.md`.
4. Present the proposed know-how skills for that project, let the user confirm or edit them, and wait for that response before moving to the next folder. Record file statuses, source-evidence questions, and extraction limitations for a consolidated review after all folders have been processed.

### Incremental updates

When new documents are added to `raw/`, use the same workflow for their project/topic folder. Incorporate new evidence into existing pages, preserve disagreements between sources, and record the update in the log. Do not silently overwrite earlier conclusions.

### Queries and wiki health

For wiki questions, consult `index.md` first, then relevant pages. Answers cite the wiki pages and source references used. A query result is filed as a new wiki page only when the user asks for it.

A health check reviews source references, Markdown links, index coverage, orphan pages, missing cross-links, unsupported claims, contradictory or stale conclusions, and unreviewed inferences. Findings are reported for review; the check must not silently rewrite disputed content.

## Error handling and evidence

Every inventoried source receives an explicit status: `processed`, `needs review`, or `blocked` with a reason. Unreadable, partially extracted, or ambiguous content is surfaced as such and is not counted as successfully ingested. The LLM must not fill extraction gaps from filenames or present unsupported details as source facts.

When sources conflict, retain citations to both positions and flag the conflict rather than deciding without evidence. Inferences are allowed when useful, but must be labeled and traceable. Missing personal role or contribution information is asked of the user or left unknown.

## Validation and acceptance criteria

The inspected baseline contains 53 source documents. The first inventory records the exact file set processed so additions or removals during ingestion are visible.

For the initial archive:

- Every file in the recorded inventory has an explicit ingestion status; none is silently omitted.
- Every processed source has a wiki source page linking to the original file.
- Source-backed claims link to evidence, with page/slide references where extraction makes them available.
- Inferences and unknowns are distinguishable from documented claims.
- Every project page has separate know-how-needed, source-evidenced-skills, and user-reported contributions/outcomes sections. Suggested or confirmed project requirements are not represented as personally demonstrated skills; user reports use `user-reported` provenance rather than source evidence labels; and the user can update the proposed taxonomy during each folder review.
- Every wiki page is listed in `index.md`; internal links and references to existing raw files resolve.
- The final consolidated report exposes all blocked or review-needed sources, evidence questions, and page/link validation findings for user review.

For future incremental ingestion, verify that the new source is inventoried, its related wiki pages and links are updated, and the log records the change. Graph/chart/portfolio generation is a later milestone and must consume the wiki rather than become a competing source of truth.
