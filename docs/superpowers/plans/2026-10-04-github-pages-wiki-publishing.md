# GitHub Pages Wiki Publishing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish the existing AI wiki from GitHub Pages at `https://gauravsa123.github.io/moonshot/skill-graph.html` without moving or duplicating wiki files in the repository.

**Architecture:** A GitHub Actions workflow regenerates the graph from the repository's existing wiki and uploads only `wiki/` as the Pages artifact root. GitHub Pages deploys that artifact at the project-site root, preserving relative links to the project, skill, and source Markdown files while excluding repository paths outside `wiki/`.

**Tech Stack:** GitHub Actions, GitHub Pages deployment actions, Python 3 standard library.

---

## File map

- Create `.github/workflows/publish-wiki-pages.yml` — triggers deployment from `main`, runs the existing graph generator, and publishes only `wiki/`.
- Keep `wiki/skill-graph.html`, `wiki/projects/`, `wiki/skills/`, and `wiki/sources/` at their current repository paths. Do not create a second copy under `docs/` or the repository root.
- No changes are required to the graph builder, graph template, wiki links, or raw archive for this deployment.

## Task 1: Add the Pages deployment workflow

**Files:**
- Create: `.github/workflows/publish-wiki-pages.yml`

- [ ] **Step 1: Create the workflow with scoped triggers and permissions**

Create `.github/workflows/publish-wiki-pages.yml` with:

```yaml
name: Publish wiki to GitHub Pages

on:
  push:
    branches:
      - main
    paths:
      - "wiki/**"
      - "scripts/build_skill_graph.py"
      - "scripts/build_skill_map.py"
      - "scripts/skill_graph_template.html"
      - ".github/workflows/publish-wiki-pages.yml"

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: true

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Check out repository
        uses: actions/checkout@v6

      - name: Build graph
        run: python3 scripts/build_skill_graph.py

      - name: Configure Pages
        uses: actions/configure-pages@v5

      - name: Upload wiki artifact
        uses: actions/upload-pages-artifact@v4
        with:
          path: wiki

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

- [ ] **Step 2: Check the change for whitespace errors**

Run:

```bash
git diff --check
```

Expected: no output and exit status 0.

- [ ] **Step 3: Commit the workflow**

Run:

```bash
git add .github/workflows/publish-wiki-pages.yml
git commit -m "Publish wiki through GitHub Pages" -m "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
```

Expected: one commit adding only the Pages workflow.

## Task 2: Build and deploy the wiki

**Files:**
- Modify via generator: `wiki/skill-graph.html` only if the graph inputs changed.
- Deploy artifact: the contents of `wiki/`; do not add a tracked staging or duplicate directory.

- [ ] **Step 1: Configure the repository's Pages source**

In `https://github.com/gauravsa123/moonshot/settings/pages`, set **Build and deployment → Source** to **GitHub Actions**. Do not select branch-root publishing.

Expected: the Pages settings identify GitHub Actions as the deployment source.

- [ ] **Step 2: Run the graph builder locally**

From the repository root, run:

```bash
python3 scripts/build_skill_graph.py
```

Expected: exit status 0 and a generated graph reporting 29 projects, 227 canonical skills, and 389 relationships.

- [ ] **Step 3: Confirm the graph build did not create unrelated changes**

Run:

```bash
git diff -- wiki/skill-graph.html
```

Expected: no output because the committed graph is already generated from the current wiki. If this command shows a graph change, stop and inspect the generated diff before deployment.

- [ ] **Step 4: Push the approved spec and workflow commits to `main`**

Run:

```bash
git push origin main
```

Expected: the push succeeds and triggers **Publish wiki to GitHub Pages**. Only pushes to `main` trigger publishing; there is no manual dispatch. The build job uploads `wiki/` only; paths such as `scripts/` and `raw/` are not part of the artifact.

- [ ] **Step 5: Confirm the Actions deployment**

Open the repository's **Actions** tab and inspect the latest **Publish wiki to GitHub Pages** run.

Expected: graph generation, artifact upload, and Pages deployment all succeed; the deployment environment reports the Pages URL.

- [ ] **Step 6: Smoke-test the published graph and linked wiki records**

Run:

```bash
curl -fsS https://gauravsa123.github.io/moonshot/skill-graph.html -o /dev/null
curl -fsS https://gauravsa123.github.io/moonshot/projects/agents-agentic-rag.md -o /dev/null
curl -fsS https://gauravsa123.github.io/moonshot/skills/agentic-workflow-orchestration-and-tool-integration.md -o /dev/null
curl -fsS https://gauravsa123.github.io/moonshot/sources/agents-agentic-rag-20230529-agenticrag-v01.md -o /dev/null
```

Expected: all four requests return successfully. Open the graph URL and select a project and skill to confirm that their detail and evidence links resolve.

## Deployment properties

- The repository continues to store the graph at `wiki/skill-graph.html`.
- The deployed site maps the contents of `wiki/` to its root, producing `/skill-graph.html`.
- Project, skill, and source Markdown files are public static files and may display as plain Markdown rather than styled wiki pages.
- The workflow fails before deployment if the graph builder fails; the previous successful deployment is not replaced by an invalid build.
- No raw files or repository content outside `wiki/` are uploaded.
