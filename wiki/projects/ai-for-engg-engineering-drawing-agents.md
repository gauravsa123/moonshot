---
id: ai-for-engg-engineering-drawing-agents
type: project
title: Engineering Drawing Agents
aliases:
  - Agentic Workflow for Engineering Drawing Analysis
related:
  - ../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md
  - ../skills/engineering-drawing-gdt-design-for-manufacturability.md
  - ../skills/multimodal-drawing-segmentation-and-extraction.md
  - ../skills/engineering-drawing-knowledge-graph-modeling.md
  - ../skills/agentic-workflow-orchestration-and-tool-integration.md
  - ../skills/aks-deployment.md
  - ../skills/mongodb-persistent-storage-and-integration.md
  - ../skills/ui-creation.md
  - ../skills/image-processing-optimization.md
  - ../skills/deep-agent-workflow-design-and-implementation.md
  - ../skills/working-under-total-uncertainty.md
  - ../skills/developing-methodology-from-scratch.md
  - ../skills/complex-graph-creation-workflow-design.md
  - ../skills/robust-and-reliable-drawing-data-extraction.md
  - ../skills/project-roadmap-direction.md
  - ../skills/guiding-a-junior-data-scientist.md
  - ../skills/stakeholder-communication-and-workflow-pitching.md
  - ../skills/ai-exploration-to-delivery-and-deployment.md
  - ../skills/research-paper-comprehension-and-implementation-adaptation.md
  - ../skills/engineering-drawing-database-vision.md
source_refs:
  - ../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-3
  - ../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-15
  - ../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-16
  - ../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-20
  - ../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-23
  - ../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-29
  - ../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-34
---

# Engineering Drawing Agents

## Project summary

The presentation proposes an agentic workflow for turning engineering drawings and CAD inputs into structured information, linking drawing entities in a graph, and supporting drawing QA and downstream manufacturing decisions. It covers image/view segmentation, VLM-based extraction, cross-view and cross-drawing relationships, QA checks, agent planning and tool integration. Visual review also confirmed exploratory OCR/DXF/IGS extraction attempts and an Onshape-agent chat demo. The end-to-end system's deployment and validation are not established. The source remains needs review because slides 24–25 are title-only, slide 36 leaves a graph-edge question unresolved, and slide-1 footer metadata differs between PDF and Keynote renderings.

## Sources

- [Engineering drawing agents presentation (2026-08-20)](../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md) — **needs review**; all 36 rendered slides were visually reviewed, with title-only slides and a renderer-dependent footer discrepancy remaining unresolved.

## Know-how needed

All nine entries below are **user-confirmed project requirements**. They describe know-how needed for this project, not claims of personal mastery or source evidence. Agentic workflow orchestration and tool integration is a distinct skill from the existing Agentic RAG skill.

| Skill | Review status | Rationale |
|---|---|---|
| [Engineering drawing, GD&T, and design for manufacturability](../skills/engineering-drawing-gdt-design-for-manufacturability.md) | user-confirmed | The project concerns drawing interpretation, geometric dimensioning and tolerancing, and manufacturing-readiness checks. |
| [Multimodal drawing segmentation and extraction](../skills/multimodal-drawing-segmentation-and-extraction.md) | user-confirmed | The workflow must segment views and extract structured information from engineering drawing images and related inputs. |
| [Engineering drawing knowledge-graph modeling](../skills/engineering-drawing-knowledge-graph-modeling.md) | user-confirmed | Drawing entities and relationships need to be represented in a graph for linking and downstream use. |
| [Agentic workflow orchestration and tool integration](../skills/agentic-workflow-orchestration-and-tool-integration.md) | user-confirmed | The project calls for agent orchestration and integration with workflow tools; this skill remains distinct from Agentic RAG. |
| [AKS deployment](../skills/aks-deployment.md) | user-confirmed | AKS deployment is a confirmed project know-how requirement. |
| [MongoDB persistent storage and integration](../skills/mongodb-persistent-storage-and-integration.md) | user-confirmed | Persistent storage with MongoDB and its integration are confirmed project requirements. |
| [UI creation](../skills/ui-creation.md) | user-confirmed | User-interface creation is a confirmed project know-how requirement. |
| [Image processing optimization](../skills/image-processing-optimization.md) | user-confirmed | Image processing optimization is a confirmed project know-how requirement. |
| [Deep Agent workflow design and implementation](../skills/deep-agent-workflow-design-and-implementation.md) | user-confirmed | Designing and implementing Deep Agent workflows is a confirmed project know-how requirement. |

## Skills shown by sources

These capabilities are supported by the presentation; this section records source evidence only and does not attribute individual work or personal mastery.

| Skill | Evidence status | Evidence |
|---|---|---|
| [Multimodal drawing segmentation and extraction](../skills/multimodal-drawing-segmentation-and-extraction.md) | documented | The deck outlines view segmentation, classification, structured extraction, an extraction example, and attempted OCR/DXF/IGS exploration ([slides 7](../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-7), [23](../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-23), [29](../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-29), [30](../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-30), [34](../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-34)). |
| [Engineering drawing knowledge-graph modeling](../skills/engineering-drawing-knowledge-graph-modeling.md) | documented | The proposed graph connects drawing entities through dimensions, projections, tables, annotations, and other engineering relationships ([slides 20](../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-20), [22](../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-22), [34](../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-34)). |
| [Engineering drawing, GD&T, and design for manufacturability](../skills/engineering-drawing-gdt-design-for-manufacturability.md) | documented | The presentation lists dimension, tolerance, callout, GD&T, manufacturing-readiness, and machining checks and depicts a DFM agent ([slides 15](../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-15), [16](../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-16), [32](../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-32), [34](../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-34)). |
| [Agentic workflow orchestration and tool integration](../skills/agentic-workflow-orchestration-and-tool-integration.md) | documented | The deck depicts an agent architecture and planner delegating work to sub-agents and tools ([slides 3](../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-3), [16](../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-16), [32](../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-32)). |
| [UI creation](../skills/ui-creation.md) | documented | Slide 31 shows an Onshape browser workspace beside an “Onshape Agent Chat” interface; it does not establish who built the interface or whether it was production-ready ([slide 31](../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-31)). |

## User-reported contributions and outcomes

The following contributions and capabilities are user-reported and are not corroborated by the source. The source record's `unknown` status for individual contributor roles remains unchanged. The complex graph-workflow entry reflects the user's own characterization; the “state-of-the-art” description is attributed to the user, not independently asserted here.

| Contribution or capability | Status | User-reported description |
|---|---|---|
| [Working under total uncertainty](../skills/working-under-total-uncertainty.md) | user-reported | The user reports working under total uncertainty. |
| [Developing methodology from scratch](../skills/developing-methodology-from-scratch.md) | user-reported | The user reports developing methodology from scratch. |
| [Complex graph-creation workflow design](../skills/complex-graph-creation-workflow-design.md) | user-reported | The user reports inventing a complex workflow for graph creation and characterizes it as state-of-the-art. |
| [Robust and reliable drawing data extraction](../skills/robust-and-reliable-drawing-data-extraction.md) | user-reported | The user reports making drawing data extraction robust and reliable. |
| [Project roadmap direction](../skills/project-roadmap-direction.md) | user-reported | The user reports deciding the project roadmap. |
| [Guiding a junior data scientist](../skills/guiding-a-junior-data-scientist.md) | user-reported | The user reports guiding a junior data scientist. |
| [Stakeholder communication and workflow pitching](../skills/stakeholder-communication-and-workflow-pitching.md) | user-reported | The user reports communicating with a stakeholder to pitch the workflow for the stakeholder's problem. |
| [Transitioning AI exploration to delivery and deployment](../skills/ai-exploration-to-delivery-and-deployment.md) | user-reported | The user reports converting the work from AI exploration to delivery and deployment. |
| [Research-paper comprehension and implementation adaptation](../skills/research-paper-comprehension-and-implementation-adaptation.md) | user-reported | The user reports understanding complex research papers and adapting implementation to the topic. |
| [Engineering-drawing database vision](../skills/engineering-drawing-database-vision.md) | user-reported | The user reports proposing a broader, efficient engineering-drawing database. |

### Outcomes

| Outcome | Status | User-reported description |
|---|---|---|
| Trade secret | user-reported | The user reports a trade-secret outcome. |
| Publication | user-reported | The user reports a publication outcome. |

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The stated objective is a structural engineering-drawing database supporting automated quality analysis and downstream tasks. | documented | [Slides 5](../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-5), [11](../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-11), [33](../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-33). |
| The presentation describes a workflow from drawing segmentation and extraction to graph generation and QA. | documented | [Slides 7](../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-7), [27](../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-27), [34](../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-34). |
| Slide 23 documents an experimental segmentation flow with manual/ad-hoc bounding-box correction operations. | documented | [Slide 23](../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-23). |
| Individual roles and contributions are established by the source. | unknown | The title slide names people but does not attribute tasks or roles ([slide 1](../sources/ai-for-engg-engineering-drawing-agents-20260820-enggagents-v02-pptx.md#slide-1)). |

## Review state

All nine know-how requirements are **user-confirmed**. The contributions and outcomes above remain **user-reported**, not source-documented. The presentation remains **needs review**; see the source record for extraction limitations and open questions. User confirmation of requirements and reported contributions does not change the source status.
