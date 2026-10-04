---
id: pricing-value-mate-20260908-doti-agentix-valuemate-pptx
type: source
title: Value Mate / DOTI Agentix Pricing Copilot Deep Dive
aliases: []
related:
  - ../projects/pricing-value-mate-pricing-copilot.md
source_refs: []
---

# Value Mate / DOTI Agentix Pricing Copilot Deep Dive

- **Status:** needs review
- **Original path:** `raw/Pricing/Value Mate/20260908_DOTI_AGENTIX_ValueMate.pptx`
- **Extraction:** Text extracted from 25 slides and 7 note files; 72 media items are present. Slides 4–5 have no extractable text.
- **Reason for review:** Diagrams, demos, and reported production/evaluation state remain uninspected and unverified; the cover date uses an unspecified day/month format.
- **Original format:** PowerPoint presentation. The source under `raw/` was not modified.

## Project team and cover

### Slides 1 and 3

The cover shows “Value Mate,” “pricing Copilot,” and `08/09/2026`, and lists
Varun M, Gaurav A, and Ameya D. A project-team slide lists Gaurav Adke as a
DOTI-DAI Senior Data Scientist among the technical team. The deck does not
assign individual ownership of the described components.

## Objective and supported scope

### Slide 6

The project objective is consistent pricing analytics across regions using
natural-language-to-SQL, with less analysis time and transparent operations.
The described data includes sell-in, sell-out, and market quantity for AMN
and EUR, with B2C/B2B use cases, margin bridges, period comparisons, filters,
tables, and visualizations.

## Agent development and architecture

### Slides 7–10

The presentation contrasts static tool-calling with a LangGraph workflow and
a context-aware agent, then describes a layered architecture with a web UI,
FastAPI/SSE API, agents, tool contracts, services, and replaceable providers
including Dremio, FAISS, rules/SQL building, and Postgres. The stated design
principle is to call capability contracts rather than platform-specific
SDKs.

## Literature review

### Slide 9

The slide summarizes a state-of-the-art workflow of query enhancement,
schema pruning, planning, and validation, to be integrated into agent nodes.

## Context management

### Slide 11

The deck describes separating a durable central conversation from a
stateless/disposable SQL worker, confirming tables, grounding filters to
stored values, checking SQL with EXPLAIN before reading rows, and preserving
short-term conversation state with checkpoints.

## Trustworthy Text-to-SQL workflow

### Slides 13, 18–20, and 23

The proposed workflow includes query enhancement, keyword extraction,
intent classification, schema pruning, planning, schema/syntax checks,
execution analysis, and human confirmation. The presentation specifies
controls such as validating SQL before execution, bounding repair attempts,
and stopping to ask rather than returning a confident but unchecked answer.

## Observability and evaluation

### Slides 12, 21–22

The deck describes traces, user feedback, approved-answer curation, expert
expectations, scorers/judges, offline evaluation, and promotion/rejection of
changes. Evaluation examples compare plans, SQL, and generated output against
ground truth. These descriptions are source claims; underlying metrics and
artifacts remain unreviewed.

## Authentication and access control

### Slide 17

The presentation proposes separate application and data-access controls,
including table/region authorization and identity integration between the
copilot and Dremio.

## Implementation and code structure

### Slide 14

The deck lists API, graph, node, agent, service, schema, configuration,
error, and utility layers. It also describes a specification/plan/test/code/
verification workflow, dead-code checks, and a coverage target. These are
statements in the source and do not identify who performed each activity.

## Demonstrations and use cases

### Slides 14 and 24

Examples include table/schema discovery, yearly sales and margin queries,
margin-change analysis, competition and market-volume comparisons, market
size by geography, and historical price/margin evolution.

## Speaker notes

The seven note files add detail about service contracts, state isolation,
EXPLAIN-before-read behavior, trace/feedback/evaluation flows, and
human-in-the-loop recovery. The notes describe some feedback and curation
steps as in production and other evaluation/release gates as planned; this
reported status has not been independently verified.

## Review notes

The cover date `08/09/2026` is ambiguous without a stated date convention.
The filename encodes `20260908`, but the exact date interpretation is not
assumed. Slides 4–5 contain no extracted text; 72 media items remain
uninspected.
