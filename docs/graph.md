---
name: skill-graph-resume
description: Build an interactive, Obsidian-style force-directed graph of skills and projects (a "living resume") from a folder of Markdown notes or a simple skills/projects list. Use whenever the user wants a skill map, skills graph, project-skill network, knowledge graph visualization, portfolio or resume visualization, or wants to turn a wiki / Obsidian vault of [[wikilinks]] into a dynamic graph, even if they don't say "graph". Outputs one self-contained HTML file that can be published as an artifact or hosted anywhere.
---

# Skill Graph Resume

Turns notes about projects and skills into a single self-contained HTML page: glowing nodes, physics-based layout, drag/zoom/pan, hover-highlighting of neighbours, search, category filters, and a click-through detail panel. No external libraries or network calls.

## Bundled files
- `assets/template.html` - the complete graph app. Data lives between `/*DATA_START*/` and `/*DATA_END*/` markers.
- `scripts/build_graph.py` - parses a notes folder and injects data into the template.
- `references/customizing.md` - how to tweak look, physics and behaviour. Read only if the user asks for changes.

## Workflow

### 1. Get the data
Ask for (or locate in uploads) one of:
- a folder / zip of `.md` notes (a wiki or Obsidian vault), or
- a plain list of projects with the skills each used.

Expected note format (all frontmatter optional):
```
---
type: project        # or skill
category: ML         # skills only; drives node colour and filter chips
year: 2022           # projects only
---
Built X using [[Python]], [[XGBoost]] and [[SQL]].
```
- Edges come from `[[wikilinks]]` (aliases like `[[X|alias]]` and headings `[[X#h]]` are stripped).
- If `type` is missing: names/tags containing "project" are projects, everything else is a skill.
- Linked names with no note of their own become skills in category "Other". Report these warnings so the user can add categories.
- If notes use a different convention (tags, folders, tables), adapt `parse()` in the script rather than asking the user to reformat.

### 2. Build
```bash
python scripts/build_graph.py <notes_dir> /mnt/user-data/outputs/skill-graph.html --title "Name - Skill Graph" --dump-json /tmp/data.json
```
Check the printed counts and warnings. Sanity-check `/tmp/data.json`: every project has links, categories are sensible (merge near-duplicates like "ML" / "Machine Learning").

### 3. Deliver
- In a surface with the Artifact tool, publish the HTML file (it follows the hosted-page rules: self-contained, no remote assets, storage not required).
- Otherwise present the file; it opens by double-click in any browser.
- Tell the user they can also drag-and-drop `.md` files straight onto the page to reload it with new data, and that a skills-only update just means re-running step 2.

### 4. Iterate
Common follow-ups (see `references/customizing.md`): colours per category, node size by years/usage instead of degree, a timeline filter by year, a light/dark default, a skill-to-skill link style, a title/legend.

## How the template works (for rebuilding from scratch)
1. **Data model**: `SKILLS = {name: category}`, `PROJECTS = [{name, year, desc, skills[]}]`. `build()` turns this into nodes (type project/skill) and links (project-skill), computes degree and neighbour sets, and assigns a palette colour per category.
2. **Physics** (`tick()`): pairwise repulsion (inverse-square, cut off at 300px), spring links with rest length ~85, weak centre gravity, velocity damping 0.82. `alpha` cools to a floor of 0.03 so the graph stays gently alive and reacts when nodes are dragged.
3. **Rendering** (`draw()`): one `<canvas>`, devicePixelRatio-aware. Each node gets a radial-gradient glow plus a solid core; projects get a ring and a slow pulse. Labels show for projects, hovered/selected nodes, matches, and everything once zoomed in.
4. **Focus mode**: hovering or selecting dims all non-neighbours and edges to ~10%, and brightens edges to the focused node in the neighbour's category colour.
5. **Interaction**: pointer events for drag-node vs pan-background, wheel zoom anchored at the cursor, click (movement < 4px) selects and opens the panel with clickable neighbour chips.
6. **Filters**: category chips toggle visibility; the search box matches node names and keeps their neighbours visible.
7. **Theming**: CSS variables with `prefers-color-scheme` dark variant; canvas reads the variables each frame.
8. **Drop-in loader**: a `drop` handler re-parses dropped `.md` files client-side with the same rules as the Python script. Keep the two parsers consistent when editing either.

## Gotchas
- Keep everything inline and library-free; remote scripts/fonts are blocked in hosted artifacts.
- Beyond ~300 nodes the O(n^2) repulsion gets slow; raise the cutoff distance cost or add a spatial grid.
- Never put raw user text into the page without escaping if you extend the detail panel (descriptions are inserted via innerHTML).