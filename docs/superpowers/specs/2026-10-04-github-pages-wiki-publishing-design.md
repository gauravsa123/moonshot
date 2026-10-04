# GitHub Pages Publishing for the AI Wiki

## Goal

Publish the existing interactive graph at
`https://gauravsa123.github.io/moonshot/skill-graph.html` without moving or
duplicating wiki files in the repository. Include the linked wiki pages needed
by the graph; exclude repository content outside `wiki/`, including `raw/`.

## Approved approach

Use GitHub Actions to deploy the existing `wiki/` directory as the Pages
artifact root. The workflow will:

1. Run only on pushes to `main` that change wiki files, graph-builder inputs,
   or the workflow itself. Manual dispatch is intentionally omitted so a
   workflow definition selected from a non-main branch cannot deploy the site.
2. Run `python3 scripts/build_skill_graph.py` from the repository root so the
   published graph is regenerated from the current wiki.
3. Upload `wiki/` as the artifact root and deploy it using GitHub Pages Actions.

The repository copy remains at `wiki/skill-graph.html`; deployment maps that
directory's contents to the site root, so the published URL is
`/skill-graph.html`. The `projects/`, `skills/`, and `sources/` directories stay
alongside the graph in the artifact, preserving its relative detail and
evidence links. Other repository directories are not uploaded.

## Alternatives considered

- Publishing the repository root from a branch is simpler but exposes unrelated
  tracked content, keeps the graph under `/wiki/skill-graph.html`, and does not
  publish only the selected `wiki/` folder.
- Copying the wiki into `docs/` or another tracked publishing directory would
  duplicate or restructure the source files.

## Public content and rendering

The complete `wiki/` directory will be publicly available through Pages,
including Markdown project, skill, and source records, the index and log, the
existing skill map, and the generated graph. The user explicitly approved
publishing this wiki content. Files outside `wiki/` are excluded.

The deployment is static and does not convert Markdown pages into styled wiki
pages. Graph links to Markdown records resolve to the deployed files, which may
be presented as plain Markdown by the browser.

## Workflow and access

Use GitHub Pages Actions rather than branch-root publishing. Grant only the
Pages deployment permissions required by the official Pages Actions flow, use
the `github-pages` deployment environment, and prevent overlapping deployments
with workflow concurrency. Since only `main` pushes trigger deployment, do not
add a manual dispatch trigger. Configure the repository's Pages source as
**GitHub Actions** once before the first successful deployment.

## Validation

- Parse/check the workflow and confirm only `main` pushes to wiki and
  graph-builder paths trigger publishing; no manual dispatch event is present.
- Run the existing graph builder and confirm it succeeds.
- Confirm the Pages artifact contains the wiki tree with the graph at its root
  and does not contain repository paths outside `wiki/`.
- Confirm the deployed graph URL and representative project, skill, and source
  links resolve.
- Confirm a failing graph build prevents deployment.
