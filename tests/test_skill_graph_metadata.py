import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_skill_map
import build_skill_graph


PROJECT_BODY = """\
# Synthetic Full Project Title

## Know-how needed

## Skills shown by sources

## User-reported contributions and outcomes
"""

SKILL_BODY = """\
# Synthetic Full Skill Title

A synthetic skill definition.

## Projects needing this skill

## Projects with user-reported use

## Projects showing this skill
"""


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
"""
        + PROJECT_BODY,
        encoding="utf-8",
    )
    (skills / "synthetic-skill.md").write_text(
        """\
---
type: skill
title: Synthetic Full Skill Title
short_title: "  Synthetic Skill  "
aliases: []
related: []
source_refs: []
---
"""
        + SKILL_BODY,
        encoding="utf-8",
    )
    return root


class GraphMetadataTests(unittest.TestCase):
    def temporary_wiki(self):
        temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(temporary_directory.cleanup)
        return make_temporary_wiki(Path(temporary_directory.name))

    def test_graph_metadata_is_opt_in_and_independent_of_aliases(self):
        root = self.temporary_wiki()
        default_data = build_skill_map.load_wiki(root)
        alias_data = build_skill_map.load_wiki(root, include_aliases=True)
        graph_data = build_skill_map.load_wiki(
            root, include_graph_metadata=True
        )

        for project in default_data["projects"]:
            self.assertNotIn("short_title", project)
            self.assertNotIn("publication_authorship", project)
        for skill in default_data["skills"]:
            self.assertNotIn("short_title", skill)
        self.assertNotIn("short_title", alias_data["projects"][0])
        self.assertNotIn("short_title", alias_data["skills"][0])
        self.assertIn("aliases", alias_data["skills"][0])

        project = graph_data["projects"][0]
        skill = graph_data["skills"][0]
        self.assertEqual(project["short_title"], "Synthetic Project")
        self.assertEqual(skill["short_title"], "Synthetic Skill")
        self.assertEqual(project["publication_authorship"], "user-reported")

    def test_short_title_can_be_a_graph_label_without_replacing_full_title(self):
        root = self.temporary_wiki()
        graph_data = build_skill_map.load_wiki(
            root, include_graph_metadata=True
        )

        project = graph_data["projects"][0]
        label = project.get("short_title", project["title"])
        self.assertEqual(label, "Synthetic Project")
        self.assertEqual(project["title"], "Synthetic Full Project Title")

        skill = graph_data["skills"][0]
        self.assertEqual(skill["short_title"], "Synthetic Skill")
        self.assertEqual(skill["title"], "Synthetic Full Skill Title")

    def test_browser_use_publication_authorship_is_loaded(self):
        root = self.temporary_wiki()
        browser_use_page = ROOT / "wiki/projects/agents-browser-use.md"
        _, _, fields = build_skill_map._read_page(browser_use_page)
        authorship = fields["publication_authorship"]
        self.assertEqual(authorship, "user-reported")

        project_path = root / "wiki/projects/synthetic-project.md"
        project_path.unlink()
        (root / "wiki/projects/agents-browser-use.md").write_text(
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
        graph_data = build_skill_map.load_wiki(
            root, include_graph_metadata=True
        )
        project = next(
            project
            for project in graph_data["projects"]
            if project["path"] == "projects/agents-browser-use.md"
        )
        self.assertEqual(project["publication_authorship"], "user-reported")

    def test_aliases_remain_independent_of_graph_metadata(self):
        aliases_only = build_skill_map.load_wiki(
            self.temporary_wiki(), include_aliases=True
        )
        self.assertNotIn("short_title", aliases_only["projects"][0])
        self.assertIn("aliases", aliases_only["skills"][0])

    def test_optional_short_title_is_trimmed(self):
        metadata = build_skill_map._optional_graph_metadata(
            {"short_title": "  Example title  "},
            Path("project.md"),
            project=True,
        )
        self.assertEqual(metadata["short_title"], "Example title")

    def test_empty_short_title_is_rejected(self):
        with self.assertRaises(build_skill_map.MapBuildError) as error:
            build_skill_map._optional_graph_metadata(
                {"short_title": "  "}, Path("project.md"), project=True
            )
        self.assertIn("project.md", str(error.exception))

    def test_list_short_title_is_rejected(self):
        with self.assertRaises(build_skill_map.MapBuildError):
            build_skill_map._optional_graph_metadata(
                {"short_title": ["A title"]},
                Path("project.md"),
                project=True,
            )

    def test_unrecognized_publication_authorship_is_rejected(self):
        with self.assertRaises(build_skill_map.MapBuildError):
            build_skill_map._optional_graph_metadata(
                {"publication_authorship": "documented"},
                Path("project.md"),
                project=True,
            )

    def test_publication_authorship_is_project_only(self):
        with self.assertRaises(build_skill_map.MapBuildError):
            build_skill_map._optional_graph_metadata(
                {"publication_authorship": "user-reported"},
                Path("skill.md"),
                project=False,
            )

    def test_graph_label_uses_short_title_and_preserves_full_title(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            wiki = root / "wiki"
            wiki.mkdir()
            (wiki / "skill-graph-aliases.json").write_text(
                '{"groups": []}', encoding="utf-8"
            )
            wiki_data = {
                "projects": [
                    {
                        "title": "Synthetic Full Project Title",
                        "short_title": "Synthetic Label",
                        "path": "projects/synthetic-project.md",
                        "source_reviews": [],
                        "unmapped_claims": [],
                        "data_quality_notes": [],
                    }
                ],
                "skills": [],
                "relationships": [],
                "source_inventory": [],
            }
            with patch(
                "build_skill_graph.load_wiki", return_value=wiki_data
            ) as load_wiki:
                graph_data = build_skill_graph.build_graph_data(root)
                load_wiki.assert_called_once_with(
                    root.resolve(),
                    include_aliases=True,
                    include_graph_metadata=True,
                )

        project = next(
            node for node in graph_data["nodes"] if node["type"] == "project"
        )
        self.assertEqual(project["label"], "Synthetic Label")
        self.assertEqual(project["title"], "Synthetic Full Project Title")
        self.assertIn("Synthetic Label", project["search_terms"])
        self.assertIn("Synthetic Full Project Title", project["search_terms"])

    def test_skill_short_title_is_applied(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            wiki = root / "wiki"
            wiki.mkdir()
            (wiki / "skill-graph-aliases.json").write_text(
                '{"groups": []}', encoding="utf-8"
            )
            wiki_data = {
                "projects": [],
                "skills": [
                    {
                        "title": "Full Skill Title",
                        "short_title": "Short Skill",
                        "path": "skills/full-skill-title.md",
                        "definition": "A test skill.",
                        "aliases": [],
                    }
                ],
                "relationships": [],
                "source_inventory": [],
            }
            with patch("build_skill_graph.load_wiki", return_value=wiki_data):
                graph_data = build_skill_graph.build_graph_data(root)

        skill = next(
            node for node in graph_data["nodes"] if node["type"] == "skill"
        )
        self.assertEqual(skill["label"], "Short Skill")
        self.assertEqual(skill["pages"][0]["title"], "Full Skill Title")
        self.assertIn("Short Skill", skill["search_terms"])
        self.assertIn("Full Skill Title", skill["search_terms"])

    def test_publications_hub_has_five_user_reported_project_links(self):
        graph_data = build_skill_graph.build_graph_data(ROOT)
        hub = next(
            node
            for node in graph_data["nodes"]
            if node["id"] == "publication-hub"
        )
        self.assertEqual(hub["type"], "publication")
        self.assertEqual(hub["label"], "Publications")
        self.assertEqual(hub["title"], "Publications")

        publication_edges = [
            edge
            for edge in graph_data["edges"]
            if edge["kind"] == "publication_authorship"
            and edge["source"] == "publication-hub"
        ]
        self.assertEqual(len(publication_edges), 5)
        self.assertTrue(
            all(edge["status"] == "user-reported" for edge in publication_edges)
        )
        self.assertEqual(
            {edge["target"] for edge in publication_edges},
            {
                "projects/gan-publication-advanced-gan-for-tire-defect-augmentation.md",
                "projects/janus-rl-process-optimization-and-visualization.md",
                "projects/ai-for-engg-point-cloud.md",
                "projects/agents-browser-use.md",
                "projects/patents-similarity-and-technology-mapping.md",
            },
        )
        self.assertTrue(
            all(
                edge["rationale"]
                == "The user reports personally authoring publication material associated with this project."
                and edge["evidence"] == []
                for edge in publication_edges
            )
        )


if __name__ == "__main__":
    unittest.main()
