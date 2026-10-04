---
id: agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx
type: source
title: Spec Driven Coding presentation
aliases: []
related:
  - ../projects/agents-spec-driven-coding.md
source_refs: []
---

# Spec Driven Coding presentation

- **Status:** needs review
- **Original path:** `raw/Agents/Spec Driven Coding/v02_20260820_SpecDrivenCoding.pptx`
- **Extraction:** Local text extraction covered all six slides; the five notes-slide files contained no substantive notes. The deck contains 23 embedded media items and eight picture objects. Visuals were not inspected, so diagrams, illustrations, and other image-only details may be missing.

## Summary

The six-slide presentation contrasts code completion and “vibe coding” for
small patches or quick experiments with spec-driven coding for feature
development. It lists GitHub Spec-Kit, Superpowers, and Amazon Kiro and presents
a requirements/design/tasks/execute progression. Its Superpowers example
describes brainstorming, bounded specifications, stepwise plans, test-driven
steps, worktrees, subagent-driven implementation, human checkpoints, testing,
and code review. A coding-guardrails slide recommends thinking through the
workflow and outcome, breaking large objectives into subtasks, writing clear
instructions, and managing technical debt.

The closing workshop slide describes a Streamlit data-quality app that flags
missing IDs, invalid values, and duplicates. The proposed extension uses JSON
configuration for one allowed-values rule and includes deployment to Streamlit
Community Cloud. These are workshop instructions, not evidence that the app
was extended or deployed. The title slide lists “Varun M, Gaurav ADAI” without
assigning individual roles or contributions.

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The presentation contrasts small-patch code completion/vibe coding with spec-driven feature development. | documented | [Slide 2](#slide-2) |
| GitHub Spec-Kit, Superpowers, and Amazon Kiro are named as toolkits, with requirements, design, tasks, and execution as workflow elements. | documented | [Slide 3](#slide-3) |
| The Superpowers workflow includes brainstorming, scope and non-goals, stepwise planning, worktree-based execution, task delegation, human checkpoints, tests, and code review. | documented | [Slide 4](#slide-4) |
| Clear instructions, task decomposition, and technical-debt management are presented as coding guardrails. | documented | [Slide 5](#slide-5) |
| The Streamlit exercise proposes JSON-configured allowed-values validation and deployment to Streamlit Community Cloud. | documented | [Slide 6](#slide-6) |
| The workshop extension or deployment was completed by a named presenter. | unknown | Slide 6 describes the workshop task but does not report completion or assign individual responsibility; see [slide 1](#slide-1) and [slide 6](#slide-6). |
| Individual presenter roles or personal mastery are established. | unknown | The title slide lists names but assigns no individual work or expertise ([slide 1](#slide-1)). |

## Slide references

### Slide 1

Title: “Spec Driven Coding.” The title slide lists “Varun M, Gaurav ADAI”; no
roles or contributions are attributed.

### Slide 2

Contrasts code completion in IDEs and “vibe coding” for small code patches,
quick experimentation, and modifications with spec-driven coding for feature
development. It associates ad-hoc development with chaotic code, a poorly
maintained code trail, and possible difficulty managing large-scale
development.

### Slide 3

Names GitHub Spec-Kit, Superpowers, and Amazon Kiro. Lists requirements with
user stories and acceptance criteria, design with technical architecture and
implementation approach, discrete trackable tasks, and execution. Also labels
the stages “Spec,” “Plan,” “Execute,” and “Brainstorming.”

### Slide 4

Describes Superpowers brainstorming as refining ideas through questions and
alternatives; a spec as defining what to build, intent, boundaries, non-goals,
constraints, and a stepwise breakdown; and a plan as milestones and
implementation tasks. The execution notes mention exact file paths,
commits/verifications, test-driven steps, worktrees, subagent-driven
implementation, human checkpoints, testing, and code review.

### Slide 5

Lists guardrails: consider the full workflow and expected outcome, decompose
large objectives into subtasks, make implementation instructions specific,
clear, and concise, and manage technical debt while remaining responsible for
delivered code.

### Slide 6

Describes a Streamlit workshop app for finding missing IDs, invalid values,
and duplicates in a dataset and producing a quality score. The proposed
extension moves an allowed-values rule into a JSON file rather than hardcoding
it, then deploys the app to Streamlit Community Cloud. The slide does not say
that the extension or deployment has been completed.
