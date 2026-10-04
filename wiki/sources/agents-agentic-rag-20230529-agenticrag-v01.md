---
id: agents-agentic-rag-20230529-agenticrag-v01
type: source
title: Agentic RAG (2023-05-29)
aliases: []
related:
  - ../projects/agents-agentic-rag.md
source_refs: []
---

# Agentic RAG (2023-05-29)

- **Status:** needs review
- **Original path:** `raw/Agents/Agentic RAG/20230529_AgenticRAG_V01.pptx`
- **Extraction:** Text was extracted from all 19 slides in presentation order using the local PPTX XML. The package contains 15 media files; local OCR on slide-linked image instances recovered some diagram labels but not their full visual structure. There are no chart objects, and the 11 notes-slide files contain no note text. Because image-only detail and diagram relationships could not be verified reliably, this source needs visual review.

## Summary

The deck presents Agentic RAG as adding agent reasoning and automated tool use to a retrieval-augmented generation pipeline. It describes intent recognition, routing to retrieval or summary tools, multi-step refinement, multi-document handling, and optional evaluation or supervision. The examples compare simple/naive RAG with agentic responses, and the later slides outline vector and summary indexes and a prompt/parser/function-calling approach to routing. The deck also reports experiments involving multiple PDFs and Llama 3 with open embeddings. Some multi-PDF answers and evaluation statements are inconsistent across slides; they are recorded as examples in the presentation, not as independently verified findings.

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The deck describes agent reasoning, automated tool use, and intent-based routing as additions to RAG. | documented | [Slide 2](#slide-2) |
| It depicts separate vector and summary tools for documents and an agent selecting tools. | documented | [Slide 3](#slide-3) |
| It compares simple/naive and agentic responses and reports quality or timing observations. | documented | [Slide 4](#slide-4), [slide 5](#slide-5), [slide 6](#slide-6), [slide 11](#slide-11), [slide 14](#slide-14) |
| Multi-PDF examples contain conflicting answers and evaluation statements. | documented | [Slide 7](#slide-7), [slide 8](#slide-8), [slide 9](#slide-9), [slide 18](#slide-18) |
| Individual roles and contributions for the names listed on the opening slide cannot be determined from the deck. | unknown | [Slide 1](#slide-1) lists Varun M, Tanmay N, and Gaurav A without attributing tasks. |

## Slide references

### Slide 1

Title slide: “Agentic RAG: Agentic Retrieval Augmented Generation”; lists Varun M, Tanmay N, and Gaurav A without assigning roles.

### Slide 2

Defines Agentic RAG as integrating an agentic workflow into RAG. Lists intent recognition, tool routing, multi-step and multi-document processing, and optional evaluation/supervision as benefits.

### Slide 3

Shows a multi-document processing design with per-document vector and summary tools and agent selection, including similarity retrieval as the number of documents grows.

### Slide 4

Compares simple RAG and Agentic RAG responses to a document-summary query. The slide says the agent compiles a summary from chunks.

### Slide 5

Compares responses to a tire-size question. The slide characterizes the simple-RAG response as not detailed and the agent response as combining content from multiple nodes.

### Slide 6

Compares responses to a USTMA expansion query and reports that the agent chose a vector tool and responded in 10 seconds, versus 6 minutes for the other method.

### Slide 7

Multi-PDF example asking for authors of MetaGPT and LongLora papers. The displayed responses provide inconsistent and partly unsupported author lists.

### Slide 8

Multi-PDF example asking for a common evaluation dataset; the displayed responses disagree.

### Slide 9

Shows responses to an unrelated “How is life?” query, including unsupported contextual assumptions in the displayed answers.

### Slide 10

“Thank you.”

### Slide 11

Lists issues with naive RAG: difficulty choosing a tool, supervising the process, avoiding answers not grounded in documents, and using external information.

### Slide 12

Shows a Chrome Incognito query response based on a Google manual.

### Slide 13

Shows a Chrome installation query response that states the information is not in the cited manual context.

### Slide 14

Lists benefits such as relating multiple PDFs and comparing information; notes concerns about open-source LLM hallucinations and reports a preference for OpenAI function calling and speed in the presented comparison.

### Slide 15

Describes vector-index RAG as storing nodes as vectors and retrieving top-k semantically similar nodes.

### Slide 16

Describes summary-index RAG as extracting and indexing summaries to support retrieval across text chunks.

### Slide 17

Outlines routing setup using a prompt, an output parser, and a function-calling endpoint that selects retrieval tools.

### Slide 18

Describes a multi-PDF Agentic RAG setup using Llama 3 and open embeddings and discusses MetaGPT and SWE-Bench evaluation. The slide’s dataset statements are retained as claims made in the deck, not independently validated facts.

### Slide 19

Backup slide with links to two Agentic RAG articles.
