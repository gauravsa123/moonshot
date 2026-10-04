---
id: agents-agentic-rag
type: project
title: Agentic RAG
aliases: []
related:
  - ../sources/agents-agentic-rag-20230529-agenticrag-v01.md
  - ../skills/agentic-rag-architecture-and-orchestration.md
  - ../skills/multi-document-retrieval-and-indexing.md
  - ../skills/llm-tool-routing-and-function-calling.md
  - ../skills/evaluation-of-retrieval-and-generated-answers.md
  - ../skills/faiss-based-retrieval.md
  - ../skills/chunking.md
  - ../skills/similarity-metrics.md
  - ../skills/agent-based-retrieval-tool-routing-design.md
  - ../skills/comparative-evaluation-of-rag-responses.md
  - ../skills/mentoring-and-guiding-interns-in-workflow-design-and-implementation.md
source_refs:
  - ../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-1
  - ../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-2
  - ../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-3
  - ../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-4
  - ../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-5
  - ../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-6
  - ../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-7
  - ../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-8
  - ../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-9
  - ../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-11
  - ../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-14
  - ../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-15
  - ../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-16
  - ../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-17
  - ../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-18
---

# Agentic RAG

## Project summary

The available presentation explores adding agent reasoning and tool use to RAG, including routing among per-document vector and summary tools, multi-step and multi-document queries, and comparisons of generated responses. It also outlines vector/summary indexing and prompt, parser, and function-calling components for routing. The examples and performance statements are those reported by the deck; some multi-PDF results are inconsistent and have not been independently verified. The source requires visual review because embedded diagrams were only partially readable with local extraction.

## Sources

- [Agentic RAG presentation (2023-05-29)](../sources/agents-agentic-rag-20230529-agenticrag-v01.md) — needs review; text extracted from 19 slides, with incomplete visual interpretation of embedded media.

## Know-how needed

These are user-confirmed project requirements, not statements about the user's personal experience.

| Skill | Review status | Rationale |
|---|---|---|
| [Agentic RAG architecture and orchestration](../skills/agentic-rag-architecture-and-orchestration.md) | user-confirmed | The presentation centers on integrating agent reasoning, tool use, and multi-step retrieval into a RAG pipeline ([slide 2](../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-2), [slide 3](../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-3)). |
| [Multi-document retrieval and indexing](../skills/multi-document-retrieval-and-indexing.md) | user-confirmed | The workflow selects per-document vector or summary tools and discusses vector and summary indexes ([slide 3](../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-3), [slide 15](../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-15), [slide 16](../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-16)). |
| [LLM tool routing and function calling](../skills/llm-tool-routing-and-function-calling.md) | user-confirmed | The deck outlines prompt setup, output parsing, and function-calling-based routing to query engines ([slide 17](../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-17)). |
| [Evaluation of retrieval and generated answers](../skills/evaluation-of-retrieval-and-generated-answers.md) | user-confirmed | The user confirmed this broader project requirement; the deck documents specific response comparisons, not complete evaluation expertise ([slide 4](../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-4), [slide 9](../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-9), [slide 11](../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-11), [slide 14](../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-14)). |
| [FAISS-based retrieval](../skills/faiss-based-retrieval.md) | user-confirmed | Added by the user during project review. |
| [Chunking](../skills/chunking.md) | user-confirmed | Added by the user during project review. |
| [Similarity metrics](../skills/similarity-metrics.md) | user-confirmed | Added by the user during project review. |

## Skills shown by sources

These are capabilities represented in the source, not claims about the user's personal skills or contributions.

| Skill | Evidence status | Evidence |
|---|---|---|
| [Agent-based retrieval-tool routing design](../skills/agent-based-retrieval-tool-routing-design.md) | documented | The source depicts selection among per-document vector/summary tools and outlines prompt, parser, and function-calling routing ([slide 3](../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-3), [slide 17](../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-17)). |
| [Comparative evaluation of RAG responses](../skills/comparative-evaluation-of-rag-responses.md) | documented | The source presents side-by-side RAG/Agentic RAG response comparisons and reports timing and limitations ([slide 4](../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-4), [slide 6](../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-6), [slide 11](../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-11), [slide 14](../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-14)). |

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The source presents an agent-mediated RAG pipeline with retrieval and summary tools. | documented | [Slide 2](../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-2), [slide 3](../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-3) |
| The source presents response comparisons and routing/indexing components. | documented | [Slide 4](../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-4), [slide 5](../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-5), [slide 6](../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-6), [slide 15](../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-15), [slide 16](../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-16), [slide 17](../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-17) |
| The user's individual role or contribution is established by this source. | unknown | The title slide names three people but does not attribute specific work ([slide 1](../sources/agents-agentic-rag-20230529-agenticrag-v01.md#slide-1)). |

## User-reported contributions and outcomes

The following capability is user-reported; it is not established by the source:

| Contribution or capability | Status | Details |
|---|---|---|
| [Mentoring and guiding interns in workflow design and implementation](../skills/mentoring-and-guiding-interns-in-workflow-design-and-implementation.md) | user-reported | The user reports mentoring and guiding interns through workflow design and implementation for this project. |

## Review state

All seven know-how items are **user-confirmed**. The source visual review remains outstanding.
