---
id: agents-browser-use-conference-101719-final-pdf
type: source
title: Vision-Powered RAG Agents for Organizational Software and Web Operations
aliases: []
related:
  - ../projects/agents-browser-use.md
source_refs: []
---

# Vision-Powered RAG Agents for Organizational Software and Web Operations

- **Status:** needs review
- **Original path:** `raw/Agents/Browser Use/conference_101719_final.pdf`
- **Extraction:** Text extracted from all 8 pages; figures and screenshots were not visually inspected. Workflow and result details shown only visually may be missing.

## Summary

The paper presents AgentTaskX for navigating enterprise and open websites. It separates planning from browser execution, uses enterprise documentation through RAG to supply procedural context, maps extracted clickable controls to XPath and screenshot bounding-box IDs, and limits actions to a predefined set. The execution loop uses observation and reflection. The paper presents open-site and Workday examples, reports a 24% improvement associated with RAG for internal pages, and discusses a 40% end-to-end web-automation benchmark alongside other system/human figures. Those reported measurements are retained as claims in the paper, not independently validated. Its evaluation and screenshots need visual follow-up.

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| AgentTaskX is presented as an autonomous web agent using enterprise knowledge and RAG. | documented | [Page 1](#page-1), [page 2](#page-2) |
| The described design separates planning and execution and grounds actions through clickable-element XPath and bounding-box identifiers. | documented | [Pages 2–4](#page-2) |
| The paper reports experiments on open websites and Workday and discusses accuracy, reflection, token cost, and limitations. | documented | [Pages 4–6](#page-4) |
| Individual author responsibilities or the user's personal mastery are established by the paper. | unknown | The paper's author listing and collective descriptions do not assign individual responsibilities ([page 1](#page-1)). |

## Page references

### Page 1

Title and author list; abstract states the aim of autonomous web tasks grounded in enterprise knowledge and summarizes the claimed RAG, XPath, bounding-box, tool-calling, and reflection contributions. The introduction begins.

### Page 2

Continues the introduction and related work; lists contributions and begins the methodology. The methodology describes the planner/executor division and use of enterprise software documentation with RAG.

### Page 3

Continues the methodology, including Selenium-based execution, clickable-element XPath extraction, bounding-box IDs, and the Knowledge Hub/action/observation components.

### Page 4

Shows the action set and observation-space details, then begins the experiments. It describes the open-site and Workday evaluation setup and the use of screenshots, reasoning, and reflection.

### Page 5

Discusses evaluation measures and reports an internal-webpage improvement associated with RAG, a 40% end-to-end benchmark, system/human accuracy figures, and reflection-related observations. The paper also discusses limitations and future work.

### Page 6

Continues discussion/conclusion and reference material. The text describes system determinism, XPath extraction, bounding-box IDs, a constrained action set, and reflection, as well as limitations in scrolling and evolving enterprise applications.

### Page 7

Continues references and includes the example-agent-step figure for an open website.

### Page 8

Contains figures showing an unsuccessful internal-site example and a successful example with RAG integration.
