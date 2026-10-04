# Skill Graph Short Titles and Publications Design

## Goal

Make graph labels concise where the wiki supplies `short_title`, and add a
distinct Publications hub that connects publication-related work to its
existing project nodes without overstating source evidence or authorship.

## Approved decisions

- For project and skill nodes, use a non-empty frontmatter `short_title` as the
  visible graph label; otherwise use `title`. Keep the full `title`, Markdown
  path, citations, aliases, and detail-page link available. Do not rename wiki
  pages or rewrite their canonical titles.
- Apply the same precedence in the Python builder and browser-side Markdown
  loader. Include both short and full titles in search.
- Add one distinct graph node named **Publications**, separate from projects
  and skills. Connect it to the existing project nodes for GAN Publication,
  Janus RL, Point Cloud, Browser Use, and Patents. Browser Use's two papers
  remain linked through the project's existing source records rather than
  becoming separate graph nodes.
- Show the hub's project links as user-reported authorship associations. The
  user confirmed personally authoring the publication material in all five
  areas, including the two Browser Use papers and the Patents white paper.
  Represent this only as `user-reported`, not as source-documented authorship.
- Record that confirmation in each relevant project's **User-reported
  contributions and outcomes** section. Preserve existing source-evidence
  statuses and publication-venue/status qualifications; authorship does not
  independently establish acceptance, venue, or publication status.
- Give the Publications node a distinct graph type and visual treatment.
  Keep its association edges separate from project-skill provenance filters;
  selecting it should show the associated project links and available
  publication-source links.

## Data flow and scope

The wiki remains authoritative. The existing Markdown loader parses optional
`short_title` for project and skill pages. The graph builder uses it only for
display/search labels and retains the original title and page path in node
details. The graph adds one hub node and user-reported association edges; it
does not create source nodes, merge skills, or infer authorship from source
citations.

The five project profiles are:

- `wiki/projects/gan-publication-advanced-gan-for-tire-defect-augmentation.md`
- `wiki/projects/janus-rl-process-optimization-and-visualization.md`
- `wiki/projects/ai-for-engg-point-cloud.md`
- `wiki/projects/agents-browser-use.md`
- `wiki/projects/patents-similarity-and-technology-mapping.md`

The existing project and skill node IDs, skill relationship kinds/statuses,
source inventory, and source review states remain unchanged. No files under
`raw/` are modified.

## Validation

- Pages with `short_title` use it as their graph label; pages without it fall
  back to `title`. Full titles remain visible in details and searchable.
- Python-built and browser-loaded Markdown graphs apply identical label rules.
- Exactly one Publications hub is present and linked to the five listed
  projects; each association is explicitly user-reported.
- Browser Use details retain links for both paper records. Patent white-paper
  authorship remains user-reported, and source-evidence statuses remain
  unchanged.
- Existing project-skill edges, provenance filters, source inventory, links,
  and generated-HTML determinism continue to validate.
