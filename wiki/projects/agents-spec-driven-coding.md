---
id: agents-spec-driven-coding
type: project
title: Spec-Driven Coding
aliases: []
related:
  - ../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md
  - ../skills/agentic-workflow-orchestration-and-tool-integration.md
  - ../skills/requirements-analysis-and-specification-writing.md
  - ../skills/spec-driven-development-workflow-design.md
  - ../skills/test-driven-implementation-verification-and-code-review.md
  - ../skills/config-driven-data-validation-and-streamlit-deployment.md
  - ../skills/learning-new-techniques.md
  - ../skills/methodology-to-syllabus-development.md
  - ../skills/training-team-members.md
  - ../skills/team-upskilling.md
source_refs:
  - ../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md#slide-2
  - ../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md#slide-3
  - ../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md#slide-4
  - ../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md#slide-5
  - ../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md#slide-6
---

# Spec-Driven Coding

## Project summary

The presentation contrasts IDE code completion and “vibe coding” for small
patches or quick experiments with spec-driven coding for feature development.
It outlines a requirements/design/tasks/execute flow and names GitHub Spec-Kit,
Superpowers, and Amazon Kiro as toolkits. Its Superpowers example emphasizes
refining intent, writing a bounded specification, breaking work into
stepwise plans, and executing with checkpoints, tests, and review. Coding
guardrails stress clear instructions, decomposing large objectives, and
managing technical debt ([slides 2–5](../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md#slide-2)).

The final slide describes a workshop exercise: a Streamlit data-quality app
that flags missing IDs, invalid values, and duplicates, with one allowed-values
rule moved into JSON configuration and a deployment to Streamlit Community
Cloud. The deck describes this as a workshop plan; it does not establish that
the extension or deployment was completed ([slide 6](../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md#slide-6)).

The title slide lists “Varun M, Gaurav ADAI,” but does not attribute individual
roles, implementation, or mastery. No personal contribution or skill is
inferred from the names.

## Sources

- [Spec Driven Coding presentation](../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md) — **needs review**; text was extracted from all six slides, but embedded visuals were not inspected.

## Know-how needed

These are project-specific suggestions, not claims about personal experience or
mastery. The linked existing skill concerns only the delegated agent-workflow
component; it is not a synonym for spec-driven development. All five
requirements were confirmed by the user and have canonical skill pages.

| Skill | Review status | Rationale |
|---|---|---|
| [Requirements analysis and specification writing](../skills/requirements-analysis-and-specification-writing.md) | user-confirmed | The workflow calls for translating a problem into user intent, requirements, acceptance criteria, constraints, and explicit non-goals ([slides 3–4](../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md#slide-3)). |
| [Spec-driven development workflow design](../skills/spec-driven-development-workflow-design.md) | user-confirmed | The deck frames spec-driven coding as a feature-development process linking requirements, design, tasks, and execution ([slides 2–4](../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md#slide-2)). |
| [Agentic workflow orchestration and tool integration](../skills/agentic-workflow-orchestration-and-tool-integration.md) | user-confirmed | The Superpowers example calls for delegated implementation tasks, a worktree, and human checkpoints; this existing node is relevant to that component only ([slide 4](../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md#slide-4)). |
| [Test-driven implementation, verification, and code review](../skills/test-driven-implementation-verification-and-code-review.md) | user-confirmed | The plan/execution guidance explicitly includes test-driven steps, verification, testing, and review ([slide 4](../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md#slide-4)). |
| [Config-driven data validation and Streamlit deployment](../skills/config-driven-data-validation-and-streamlit-deployment.md) | user-confirmed | The workshop proposes moving an allowed-values rule into JSON configuration for a Streamlit data-quality app, then deploying it ([slide 6](../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md#slide-6)). |

## Skills shown by sources

These are methods and capabilities represented in the presentation, not claims
about any individual's personal skills or role.

| Skill or capability | Evidence status | Evidence |
|---|---|---|
| Requirements-to-design-to-task-to-execution workflow | documented | The deck lists requirements, user stories with acceptance criteria, design, discrete tasks, and execution ([slide 3](../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md#slide-3)). |
| Specification design with explicit scope boundaries | documented | The Superpowers example describes user intent, boundaries, non-goals, constraints, and a stepwise breakdown ([slide 4](../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md#slide-4)). |
| Implementation planning with task delegation and human checkpoints | documented | The presentation describes milestones, exact file paths, worktree use, subagent-driven implementation, and human checkpoints ([slide 4](../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md#slide-4)). |
| Test-driven execution, verification, and code review | documented | Test-driven steps, verification, testing, and review are called out as part of the workflow ([slide 4](../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md#slide-4)). |
| Configurable data-quality validation in a Streamlit workshop | documented | The final slide describes a JSON-configured allowed-values rule for a data-quality app and a planned Streamlit Community Cloud deployment; it does not verify completion ([slide 6](../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md#slide-6)). |
| Individual contribution, role, or personal mastery | unknown | The title slide lists names but does not assign responsibilities or establish personal skill ([slide 1](../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md#slide-1)). |

## User-reported contributions and outcomes

| Contribution or capability | Status | Details |
|---|---|---|
| [Learning new techniques](../skills/learning-new-techniques.md) | user-reported | The user reported learning new techniques in connection with this project. |
| [Methodology-to-syllabus development](../skills/methodology-to-syllabus-development.md) | user-reported | The user reported converting methodology into a syllabus. |
| [Training team members](../skills/training-team-members.md) | user-reported | The user reported training team members. |
| [Team upskilling](../skills/team-upskilling.md) | user-reported | The user reported upskilling in connection with this project. |

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The deck presents spec-driven coding as suited to feature development, contrasting it with code completion and “vibe coding” for smaller patches and quick experiments. | documented | [Slide 2](../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md#slide-2) |
| The presentation names GitHub Spec-Kit, Superpowers, and Amazon Kiro and describes a requirements/design/tasks/execute progression. | documented | [Slide 3](../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md#slide-3) |
| The Superpowers example includes brainstorming, scoped specs, plans, worktrees, delegated tasks, human checkpoints, testing, and review. | documented | [Slide 4](../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md#slide-4) |
| The deck presents clear instructions, decomposition of large objectives, and technical-debt management as coding guardrails. | documented | [Slide 5](../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md#slide-5) |
| The workshop extension and deployment are completed deliverables. | unknown | The deck describes the exercise and intended deployment, but does not establish completion ([slide 6](../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md#slide-6)). |
| The named presenters' individual roles or mastery are established. | unknown | No individual contribution or expertise is attributed ([slide 1](../sources/agents-spec-driven-coding-v02-20260820-specdrivencoding-pptx.md#slide-1)). |

## Review state

All five know-how needs are `user-confirmed` project requirements, not claims
about personal mastery. The four additional capabilities are separately
recorded as user-reported and are not source-corroborated by the presentation.
The source remains `needs review` because visuals were not inspected.
Technical/specification/quality review is deferred as requested.
