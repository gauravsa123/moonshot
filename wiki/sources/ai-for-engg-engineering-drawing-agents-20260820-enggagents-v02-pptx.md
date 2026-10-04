---
id: ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx
type: source
title: Engineering Drawing Agents presentation (2026-08-20)
aliases: []
related:
  - ../projects/ai-for-engg-engineering-drawing-agents.md
source_refs: []
---

# Engineering Drawing Agents presentation (2026-08-20)

- **Status:** needs review
- **Original path:** `raw/AI for Engg/Engineering Drawing Agents/20260820_EnggAgents_v02.pptx`
- **Readability:** Text was extracted locally from all 36 slides. A Keynote PDF re-render and contact-sheet visual review covered all 36 rendered pages. Slides 24–25 contain only the titles “VLM Extraction” and “Graph Generation.” The 28 notes-slide files contain only slide-number text, not substantive speaker notes.
- **Reason for review:** Slide 36 explicitly leaves the graph-edge strategy unresolved (“Proximity and Projection ???”). A prior local PDF rendering reportedly showed “GAN”/2020 footer metadata on slide 1, while a Keynote re-render of the raw presentation did not; the renderer/source discrepancy is unresolved. Slide 10 lists startup explorations, and slides 30–31 show exploratory extraction and an Onshape-agent chat demo, but neither establishes a completed deployed system.
- **Original format:** PowerPoint, 36 slides; the package includes 68 media files. Source files under `raw/` were not modified.

## Summary

The deck proposes an agentic workflow for interpreting engineering drawings and CAD inputs, extracting structured drawing information, building a graph of related entities, and using that representation for drawing QA and downstream manufacturing decisions. It outlines segmentation and view classification; VLM-assisted extraction of features, dimensions, GD&T, datums, annotations, tables, and notes; deduplication and cross-view linking; graph construction; and agent-based quality checks. It also sketches deep-agent planning, tool and memory integration, deployment, and demo tasks. Visual review additionally confirmed an attempted OCR/DXF/IGS exploration and an Onshape-agent chat screenshot showing an L-shaped part interaction. These are design and prototype descriptions, not independently verified outcomes or proof of a completed deployment.

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The deck states an objective to build a structural engineering-drawing database and use it for automated quality analysis and downstream tasks. | documented | [Slide 5](#slide-5), [slide 11](#slide-11), [slide 33](#slide-33). |
| The workflow includes drawing/image segmentation, view classification, information extraction, deduplication, graph generation, and downstream tasks. | documented | [Slide 7](#slide-7), [slide 14](#slide-14), [slide 34](#slide-34). |
| Proposed graph entities and links include drawing features, dimensions, GD&T, notes, tables, cross-view projections, and relationships across drawings. | documented | [Slide 20](#slide-20), [slide 22](#slide-22), [slide 34](#slide-34), [slide 36](#slide-36). |
| The presentation lists dimension, tolerance, annotation, GD&T, and manufacturing-readiness checks. | documented | [Slide 15](#slide-15), [slide 16](#slide-16), [slide 34](#slide-34). |
| Slide 23 shows a segmentation pipeline and manual/ad-hoc bounding-box operations for merging, splitting, and extending boxes. | documented | [Slide 23](#slide-23). |
| The deck includes a structured extraction example with feature, dimension, GD&T, datum, surface-finish, annotation, and bounding-box fields. | documented | [Slide 29](#slide-29). |
| Individual contributors' roles or personal mastery are established. | unknown | The title slide names contributors but does not assign responsibilities ([slide 1](#slide-1)). |
| The rendered title slide contains unrelated-looking GAN/2020 metadata. | documented | The PDF-rendered title slide includes a “Ref file/subject: GAN” line and a 2020 creation date ([slide 1](#slide-1)); its relationship to this deck is unresolved. |

## Slide references

### Slide 1

Title: “Agentic Workflow for Engineering Drawing Analysis.” Lists Gaurav A, Praneet K, and Ameya D; it does not assign individual roles. The locally rendered page also includes a “Ref file/subject: GAN” metadata line and 2020 creation date; the discrepancy with the drawing-analysis title and deck filename is unresolved.

### Slide 3

Architecture of a drawing-review agent with engineering context and skills, memory types, tools, foundation models, MCP/Onshape, and a final response.

### Slide 5

Proposes a structural engineering-drawing database with structured information, semantic layer, image library, and graph connections for quality analysis and downstream uses including process planning, tool selection, cost estimation, and part modularity.

### Slide 6

Depicts a drawing-analysis agent combining engineering context with extracted drawing information for checks such as geometry mismatch, dimensions, and machining, followed by QA checks and report generation.

### Slide 7

Shows an information-extraction pipeline from PDF/TIFF/JPG through drawing-image reading, view segmentation/classification, extraction, deduplication/merging, graph generation/connections, and downstream tasks.

### Slide 10

Lists startup explorations named Synera (agentic engineering workflows) and Chapvision. The slide does not establish adoption or a project dependency.

### Slide 11

Defines the database and automated-QA objectives and lists drawing input formats (IGS, DXF, CATPart, JPG/TIFF), with stated strengths, limitations, and possible uses.

### Slide 13

Describes the focus on drawing content and structured extraction linked by a graph. Notes image-size variation, reading accuracy, and prompt tuning as challenges, and gives image and segment dimensions.

### Slide 14

Repeats the information-extraction pipeline shown on slide 7.

### Slide 15

Lists QA categories: dimension completeness and integrity, callout clarity, surface and tolerance, GD&T and datums, and manufacturing readiness.

### Slide 16

Contrasts predefined QA checks with dynamic checks using deep agents. Depicts an orchestrator, user queries, planning, delegated sub-agents, memory, context, graph/file-system tools, and VLM calls.

### Slide 18

Sketches deployment components and storage flow, including an LLM connection, VLM, MongoDB, frontend, AKS endpoint, and drawing-image processing through graph generation.

### Slide 19

Lists planned demo tasks and an approximate 10–15-minute upload-to-QA workflow, with streaming and partial reruns for small image changes. This records a stated workflow/task, not a verified runtime result.

### Slide 20

Describes graph-generation input as JSON extracted using a VLM, node types for drawing entities, engineering-logic edges, and potential connections across drawings.

### Slide 22

Describes cross-view projection updates, linking detail/section views to main-view callouts, connecting assemblies and parts, and downstream manufacturing uses.

### Slide 23

A locally inspected segmentation diagram labels an experimental pipeline and manual/ad-hoc correction commands. It shows contour detection, border removal, masked crops, and merge/split/extend bounding-box operations.

### Slide 24

Title “VLM Extraction”; the locally rendered page contains no readable content beyond the heading.

### Slide 25

Title “Graph Generation”; the locally rendered page contains no readable content beyond the heading.

### Slide 27

Combines image extraction of structured drawing details with CAD geometry, quality-check context, coordinate/dimensioning-graph information, an agentic worker, QA, and reporting.

### Slide 29

Shows an example structured extraction for sectional views, including features, dimensions, GD&T frames, datums, surface finishes, annotations, centerlines, and bounding boxes.

### Slide 30

Shows exploratory attempts at region-of-interest detection, aligning drawing images with IGES/DRG geometry, extracting dimensions and pixel coordinates for scale, OCR plus DXF data extraction, and reading IGS geometric primitives. These are labeled as attempted exploration, not a completed extraction pipeline.

### Slide 31

Shows an Onshape browser session beside an “Onshape Agent Chat” interface. The visible response describes creating an L-shaped part by adding vertical and horizontal extrusions. This is a demo screenshot and does not establish authorship, deployment, or production readiness.

### Slide 32

Depicts a DFM Analysis Agent connected to an Onshape MCP server and a DFM MCP server.

### Slide 33

Restates the drawing-understanding and QA objectives, input sources, pipeline areas, reference papers, and deep agents.

### Slide 34

Details view segmentation/classification, extraction and deduplication, graph entities and relations, cross-view/table linkages, QA queries, and downstream tasks.

### Slide 35

Lists literature and external references related to vision-language drawing interpretation, graph neural networks, CAD, and drawing review.

### Slide 36

Discusses possible graph construction approaches and references VectorGraphNET, MechVQA, and a RAG-pipeline paper. The edge-design text itself includes an unresolved question (“Proximity and Projection ???”).

## Open review questions

- Are the title-only slides 24–25 intentionally blank, or are expected VLM-extraction and graph-generation visuals missing?
- Are the repeated “GAN”/2020 footer metadata values stale template metadata, or do they refer to another source?
- What content, if any, was intended for sparse/blank slides such as 8–9 and 31?
- The slide-36 graph-edge strategy is explicitly unresolved in the deck; do not treat proximity/projection as a finalized design.
