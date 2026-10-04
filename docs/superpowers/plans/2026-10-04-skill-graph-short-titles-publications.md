# Skill Graph Short Titles and Publications Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Use optional Markdown `short_title` values as concise graph labels and add a Publications hub connected to five user-reported authored-work project profiles.

**Architecture:** Extend the existing wiki loader with opt-in graph metadata so the legacy skill map output stays unchanged. The graph builder will use short titles, create one publication node and five user-reported authorship links, and preserve full titles and source records. The standalone HTML renderer and Markdown drop-in parser will understand the same metadata and display the new node type.

**Tech Stack:** Python 3 standard library, `unittest`, inline JavaScript/HTML/CSS.

---

## File map

- Modify `scripts/build_skill_map.py` to validate optional graph metadata while keeping the default `load_wiki()` result unchanged.
- Modify `scripts/build_skill_graph.py` to choose graph labels and construct the Publications node/edges.
- Modify `scripts/skill_graph_template.html` to render the new node type, preserve short/full titles, and parse the metadata in dropped Markdown.
- Update the five cited project pages under `wiki/projects/` with user-reported authorship and the graph metadata field.
- Create `tests/test_skill_graph_metadata.py` with focused standard-library unit and integration tests.
- Regenerate `wiki/skill-graph.html` and append a maintenance entry to `wiki/log.md`. `wiki/index.md` already links to the graph and does not need changes.

No source files under `raw/` are changed. The working tree already contains
uncommitted user edits, so do not commit or push this work; preserve and
integrate those edits. The current user worktree has 17 `short_title` fields;
that is a worktree observation only, not a committed-input assumption or a
test dependency.

## Task 1: Load short-title and authorship metadata

**Files:**
- Modify: `scripts/build_skill_map.py`
- Modify: the five project pages listed below
- Create: `tests/test_skill_graph_metadata.py`

Project pages:

- `wiki/projects/gan-publication-advanced-gan-for-tire-defect-augmentation.md`
- `wiki/projects/janus-rl-process-optimization-and-visualization.md`
- `wiki/projects/ai-for-engg-point-cloud.md`
- `wiki/projects/agents-browser-use.md`
- `wiki/projects/patents-similarity-and-technology-mapping.md`

- [x] **Step 1: Add failing loader tests**

Create `tests/test_skill_graph_metadata.py` with tests using a temporary wiki
fixture containing one synthetic project and one synthetic skill with padded
`short_title` values. The fixture should include the required sections and an
empty `source-inventory.csv`; do not load unrelated project pages to test short
titles. For the Browser Use authorship check, read only that profile's
`publication_authorship` frontmatter value, assert it is `user-reported`, and
put it in a one-project temporary fixture. Keep the fixture title and all other
metadata fixed and synthetic; do not depend on Browser Use's live title or other
frontmatter, and do not load the full wiki. For example:

```python
from tempfile import TemporaryDirectory
import unittest
from pathlib import Path

from scripts.build_skill_map import (
    MapBuildError,
    _read_page,
    _optional_graph_metadata,
    load_wiki,
)


ROOT = Path(__file__).resolve().parents[1]


def make_temporary_wiki(root):
    wiki = root / "wiki"
    projects = wiki / "projects"
    skills = wiki / "skills"
    projects.mkdir(parents=True)
    skills.mkdir()
    (wiki / "source-inventory.csv").write_text(
        "source_path,status,reason,wiki_page\n", encoding="utf-8"
    )
    (projects / "synthetic-project.md").write_text(
        """\
---
type: project
title: Synthetic Full Project Title
short_title: "  Synthetic Project  "
publication_authorship: user-reported
source_refs: []
---
# Synthetic Full Project Title

## Know-how needed

## Skills shown by sources

## User-reported contributions and outcomes
""",
        encoding="utf-8",
    )
    (skills / "synthetic-skill.md").write_text(
        """\
---
type: skill
title: Synthetic Full Skill Title
short_title: "  Synthetic Skill  "
aliases: []
source_refs: []
---
# Synthetic Full Skill Title

A synthetic skill definition.

## Projects needing this skill

## Projects with user-reported use

## Projects showing this skill
""",
        encoding="utf-8",
    )
    return root


class GraphMetadataTests(unittest.TestCase):
    def test_graph_metadata_is_opt_in_and_titles_are_preserved(self):
        with TemporaryDirectory() as temporary_directory:
            root = make_temporary_wiki(Path(temporary_directory))
            legacy = load_wiki(root)
            graph = load_wiki(root, include_graph_metadata=True)

        self.assertNotIn("short_title", legacy["projects"][0])
        self.assertNotIn("publication_authorship", legacy["projects"][0])
        self.assertNotIn("short_title", legacy["skills"][0])
        project = graph["projects"][0]
        self.assertEqual(project["short_title"], "Synthetic Project")
        self.assertEqual(project["title"], "Synthetic Full Project Title")
        self.assertEqual(project["publication_authorship"], "user-reported")

    def test_browser_use_publication_authorship_is_loaded(self):
        with TemporaryDirectory() as temporary_directory:
            root = make_temporary_wiki(Path(temporary_directory))
            browser_use_page = ROOT / "wiki/projects/agents-browser-use.md"
            _, _, fields = _read_page(browser_use_page)
            authorship = fields["publication_authorship"]
            self.assertEqual(authorship, "user-reported")

            (root / "wiki/projects/synthetic-project.md").unlink()
            fixture_page = root / "wiki/projects/agents-browser-use.md"
            fixture_page.write_text(
                f"""\
---
type: project
title: Synthetic Browser Use Authorship Fixture
short_title: "  Synthetic Browser Use  "
publication_authorship: {authorship}
source_refs: []
---
# Synthetic Browser Use Authorship Fixture

## Know-how needed

## Skills shown by sources

## User-reported contributions and outcomes
""",
                encoding="utf-8",
            )
            graph = load_wiki(root, include_graph_metadata=True)
            project = graph["projects"][0]
            self.assertEqual(
                project["title"], "Synthetic Browser Use Authorship Fixture"
            )
            self.assertEqual(project["publication_authorship"], authorship)

    def test_invalid_and_empty_metadata_is_rejected(self):
        with self.assertRaises(MapBuildError):
            _optional_graph_metadata(
                {"short_title": []}, Path("invalid.md"), project=True
            )
        with self.assertRaises(MapBuildError):
            _optional_graph_metadata(
                {"short_title": "  "}, Path("invalid.md"), project=True
            )
        with self.assertRaises(MapBuildError):
            _optional_graph_metadata(
                {"publication_authorship": "documented"},
                Path("invalid.md"),
                project=True,
            )


if __name__ == "__main__":
    unittest.main()
```

- [x] **Step 2: Run the new tests and confirm they fail**

Run: `python3 -m unittest discover -s tests -p 'test_skill_graph_metadata.py' -v`

Expected: import/test failure because `include_graph_metadata` and the project
metadata are not implemented yet.

- [x] **Step 3: Extend `load_wiki()` without changing default output**

Add `include_graph_metadata: bool = False` to `load_wiki()`. When enabled,
validate and include optional project/skill `short_title` values and optional
project `publication_authorship`. A present `short_title` must be a non-empty
string after trimming. A present `publication_authorship` must equal
`"user-reported"`; reject other values with `MapBuildError` naming the page.
Keep `include_aliases` independent and preserve all existing default keys and
the default skill-map output.

Add this validator and apply its returned fields only when
`include_graph_metadata` is true:

```python
def _optional_graph_metadata(
    fields: dict[str, list[str] | str], page: Path, *, project: bool
) -> dict[str, str]:
    result: dict[str, str] = {}
    if "short_title" in fields:
        short_title = fields["short_title"]
        if not isinstance(short_title, str) or not short_title.strip():
            raise MapBuildError(f"{page}: short_title must be a non-empty string")
        result["short_title"] = short_title.strip()
    if "publication_authorship" in fields:
        authorship = fields["publication_authorship"]
        if not project or authorship != "user-reported":
            raise MapBuildError(
                f"{page}: publication_authorship must be 'user-reported' "
                "on a project page"
            )
        result["publication_authorship"] = authorship
    return result
```

- [x] **Step 4: Record the user's authorship reports in the project pages**

Add `publication_authorship: user-reported` to each of the five project
frontmatter blocks. In each existing **User-reported contributions and
outcomes** section, record that the user reports personally authoring the
publication material associated with that project:

- GAN Publication: the paper/manuscript.
- Janus RL: the project's publication material; leave venue/publication status
  unknown.
- Point Cloud: the MLDS manuscript; retain the existing user-reported
  publication outcome and do not upgrade it to source-documented.
- Browser Use: both papers; retain the separate user-reported conference
  acceptance/talk outcomes and the three `needs review` source records.
- Patents: the white paper; update the existing user-reported row so it no
  longer says the user's personal role is unspecified, but keep venue/date
  unspecified.

Do not alter Evidence-table statuses, source inventory entries, or claims
about acceptance, venue, publication status, implementation ownership, or
personal mastery.

- [x] **Step 5: Run the tests and confirm the loader contract**

Run: `python3 -m unittest discover -s tests -p 'test_skill_graph_metadata.py' -v`

Expected: the fixture tests prove that default `load_wiki()` omits graph-only
metadata and graph mode trims short titles without replacing full titles. The
authorship loader test asserts Browser Use's real authorship field is
`user-reported`, then verifies the loader carries that value into a fixture
with a fixed synthetic title and controlled metadata.

## Task 2: Build short labels and the Publications hub

**Files:**
- Modify: `scripts/build_skill_graph.py`
- Modify: `tests/test_skill_graph_metadata.py`

- [x] **Step 1: Add failing graph-data tests**

Add these imports at the top of the test file:

```python
from tempfile import TemporaryDirectory
from unittest.mock import patch

from scripts.build_skill_graph import build_graph_data
```

Append these methods inside `GraphMetadataTests`:

```python
    def test_graph_label_uses_short_title_and_preserves_full_title(self):
        wiki_data = {
            "projects": [{
                "title": "Synthetic Full Project Title",
                "short_title": "Synthetic Label",
                "path": "projects/synthetic-project.md",
                "source_reviews": [],
                "unmapped_claims": [],
                "data_quality_notes": [],
            }],
            "skills": [],
            "relationships": [],
            "source_inventory": [],
        }
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "wiki").mkdir()
            (root / "wiki" / "skill-graph-aliases.json").write_text(
                '{"groups": []}', encoding="utf-8"
            )
            with patch(
                "scripts.build_skill_graph.load_wiki",
                return_value=wiki_data,
            ):
                data = build_graph_data(root)

        project = next(node for node in data["nodes"] if node["type"] == "project")
        self.assertEqual(project["label"], "Synthetic Label")
        self.assertEqual(project["title"], "Synthetic Full Project Title")

    def test_skill_short_title_is_applied(self):
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "wiki").mkdir()
            (root / "wiki" / "skill-graph-aliases.json").write_text(
                '{"groups": []}', encoding="utf-8"
            )
            wiki_data = {
                "projects": [],
                "skills": [{
                    "title": "Full Skill Title",
                    "short_title": "Short Skill",
                    "path": "skills/full-skill-title.md",
                    "definition": "A test skill.",
                    "aliases": [],
                }],
                "relationships": [],
                "source_inventory": [],
            }
            with patch(
                "scripts.build_skill_graph.load_wiki",
                return_value=wiki_data,
            ):
                data = build_graph_data(root)

        skill = next(node for node in data["nodes"] if node["type"] == "skill")
        self.assertEqual(skill["label"], "Short Skill")
        self.assertEqual(skill["pages"][0]["title"], "Full Skill Title")

    def test_publications_hub_has_five_user_reported_project_links(self):
        data = build_graph_data(ROOT)
        nodes = {node["id"]: node for node in data["nodes"]}
        self.assertEqual(nodes["publication-hub"]["type"], "publication")
        self.assertEqual(nodes["publication-hub"]["label"], "Publications")

        associations = [
            edge for edge in data["edges"]
            if edge["kind"] == "publication_authorship"
        ]
        self.assertEqual(len(associations), 5)
        self.assertEqual(
            {edge["target"] for edge in associations},
            {
                "projects/gan-publication-advanced-gan-for-tire-defect-augmentation.md",
                "projects/janus-rl-process-optimization-and-visualization.md",
                "projects/ai-for-engg-point-cloud.md",
                "projects/agents-browser-use.md",
                "projects/patents-similarity-and-technology-mapping.md",
            },
        )
        self.assertTrue(all(edge["source"] == "publication-hub" for edge in associations))
        self.assertTrue(all(edge["status"] == "user-reported" for edge in associations))
```

Place the new import with the other module imports at the top of the test file.
Insert the new methods above the existing `if __name__ == "__main__":`
block so that it remains the final block in the file.

- [x] **Step 2: Run the graph tests and confirm they fail**

Run: `python3 -m unittest discover -s tests -p 'test_skill_graph_metadata.py' -v`

Expected: failures because graph labels still use `title` and there is no
publication node or publication-authorship edge.

- [x] **Step 3: Update the builder data model**

Call `load_wiki(root, include_aliases=True, include_graph_metadata=True)`.
For ungrouped project and skill nodes, set `label` to `short_title` when
present and otherwise to `title`; keep each node's `title` as the full title.
Preserve explicit alias-group labels for grouped skills. Keep both short and
full titles in search terms.

Add one node with `id: "publication-hub"`, `type: "publication"`, and label and
title `"Publications"`. For each project whose `publication_authorship` is
`"user-reported"`, add one edge:

```python
{
    "id": stable_edge_id,
    "source": "publication-hub",
    "target": project["path"],
    "kind": "publication_authorship",
    "status": "user-reported",
    "rationale": "The user reports personally authoring publication material associated with this project.",
    "evidence": [],
}
```

Sort these edges with the existing deterministic edge sort. Add a
`publication_nodes` count and include it in the build summary while keeping
project and skill counts unchanged. Do not turn source records into nodes or
infer venue/publication status.

- [x] **Step 4: Run the tests and confirm graph data**

Run: `python3 -m unittest tests.test_skill_graph_metadata -v`

Expected: the synthetic graph-label test uses a supplied short title while
retaining the full title; graph data also contains one Publications node, five
user-reported authorship edges, and unchanged project/skill IDs.

## Task 3: Render and preview the new node type

**Files:**
- Modify: `scripts/skill_graph_template.html`
- Modify: `tests/test_skill_graph_metadata.py`

- [x] **Step 1: Render short titles without losing canonical titles**

In the embedded JavaScript parser, return trimmed `short_title` and optional
`publication_authorship` from `makeDroppedPage()`. Validate them with the same
rules as `load_wiki()`. Use short title as the project/skill label and keep
the full page title in node data, project details, skill-page details, and
search terms. For skill nodes, keep the existing explicit alias-group label
precedence.

In `graphDataFromDroppedPages()`, create the Publications node when at least
one dropped project has `publication_authorship: user-reported`; connect it
only to marked project nodes with the same `publication_authorship` edge
shape as the Python builder. Preserve the existing all-or-nothing load
behavior on parse errors.

- [x] **Step 2: Add the visual and detail treatment for publications**

Update `visibleEdges()` so `publication_authorship` edges follow the existing
User-reported filter. Add an edge label of **User-reported authorship** and a
distinct dashed style in the user color. Give `type: "publication"` a unique
node shape and color; do not include its edges in skill project-coverage
counts. Keep the node label visible when selected, hovered, searched, or
zoomed.

Extend `renderDetail()` to display the publication-node type without reading
skill-only `pages`. List each linked project using its button/link and state
that authorship is user-reported. For a project node with a short label, show
the canonical full title in details. Keep project details' source-review
links available so Browser Use's two paper records can be opened from its
project node. Update the search label, canvas accessible description, and
legend to include Publications.

- [x] **Step 3: Rebuild and validate the dropped-note preview**

Run: `python3 scripts/build_skill_graph.py`

Expected: the generated graph contains 29 projects, 227 skill nodes, one
Publications node, and five publication-authorship edges.

Open `wiki/skill-graph.html` in a browser and create two temporary Markdown
files named `preview-project.md` and `demo-skill.md`. Drop them together.
Use these complete contents:

```markdown
---
type: project
title: Preview Project Full Name
short_title: Preview Project
publication_authorship: user-reported
aliases: []
related: []
source_refs: []
---
# Preview Project Full Name

## Know-how needed

| Skill | Review status | Rationale |
|---|---|---|
| [Demo skill](../skills/demo-skill.md) | user-confirmed | Preview relationship. |

## Skills shown by sources

| Skill | Evidence status | Evidence |
|---|---|---|

## User-reported contributions and outcomes

The user reports personally authoring publication material for this project.
```

```markdown
---
type: skill
title: Demonstration skill
short_title: Demo skill
aliases: []
related: []
source_refs: []
---
# Demonstration skill

A skill page used to preview graph metadata.

## Projects needing this skill

- [Preview Project Full Name](../projects/preview-project.md) — user-confirmed requirement.

## Projects with user-reported use

- None recorded.

## Projects showing this skill

- None recorded.
```

Confirm the graph shows `Preview Project`, retains `Preview Project Full Name`
in details, adds the Publications node linked to the project, and preserves the
prior graph after a drop failure. For the failure check, change the project's
frontmatter to `publication_authorship: unsupported` and drop the pair again.

No JavaScript test runner exists in the repository; perform this browser
validation manually rather than adding a test/runtime dependency.

## Task 4: Validate wiki records and generated output

**Files:**
- Modify: `wiki/log.md`
- Generated: `wiki/skill-graph.html`

- [x] **Step 1: Run focused tests and rebuild**

Run:

```bash
python3 -m unittest discover -s tests -p 'test_skill_graph_metadata.py' -v
python3 scripts/build_skill_graph.py
```

Expected: all tests pass; the build reports 29 projects, 227 canonical skills,
one publication node, five publication-authorship associations, and the
existing project-skill relationships.

- [x] **Step 2: Verify provenance and links**

Check that each of the five profile sections records authorship as
`user-reported`; the publication edges have status `user-reported`; and no
Evidence-table row is upgraded as a result. Confirm Browser Use details expose
both conference-paper source records, and the Patents white paper row retains
its user-reported outcome while venue/date remain unspecified.

Confirm every publication edge endpoint exists, every project and skill page
still has a detail link, and source inventory statuses remain unchanged.

- [x] **Step 3: Verify deterministic HTML**

Run:

```bash
python3 scripts/build_skill_graph.py
shasum -a 256 wiki/skill-graph.html
python3 scripts/build_skill_graph.py
shasum -a 256 wiki/skill-graph.html
```

Expected: the two SHA-256 values match when wiki inputs are unchanged.

- [x] **Step 4: Record the completed graph change**

Append a dated entry to `wiki/log.md` describing optional short-title labels,
the single Publications hub, five user-reported authorship links, preserved
source/evidence statuses, and the focused validation results. Do not change
`wiki/index.md`; it already links to the generated graph.
