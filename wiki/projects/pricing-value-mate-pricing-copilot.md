---
id: pricing-value-mate-pricing-copilot
type: project
title: Value Mate Pricing Copilot
aliases: []
related:
  - ../sources/pricing-value-mate-20260422-deepdive-valuemate-pptx.md
  - ../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md
  - ../skills/pricing-analytics-and-margin-bridge-calculations-for-data-agents.md
  - ../skills/natural-language-to-sql-for-pricing-datasets.md
  - ../skills/agentic-workflow-orchestration-and-tool-integration.md
  - ../skills/query-understanding-planning-and-schema-pruning-for-text-to-sql.md
  - ../skills/schema-and-value-grounding-for-enterprise-sql-agents.md
  - ../skills/sql-validation-repair-and-dialect-aware-execution.md
  - ../skills/component-agnostic-data-service-integration-for-agents.md
  - ../skills/conversation-state-management-and-memory-isolation.md
  - ../skills/human-in-the-loop-clarification-and-recoverable-agent-workflows.md
  - ../skills/evaluation-of-data-agent-plans-and-answers.md
  - ../skills/observability-and-feedback-loops-for-data-agents.md
  - ../skills/enterprise-identity-and-access-control-for-agents.md
  - ../skills/streaming-api-and-ui-design-for-agent-workflows.md
  - ../skills/data-standardization-for-multi-region-pricing-analytics.md
  - ../skills/spec-driven-agent-product-delivery.md
  - ../skills/literature-review-for-agentic-workflow-design.md
  - ../skills/cross-functional-team-collaboration.md
  - ../skills/team-leadership-and-direction.md
  - ../skills/stakeholder-management.md
  - ../skills/leadership-communication.md
  - ../skills/decision-support-and-facilitation.md
  - ../skills/team-leadership-under-tight-deadlines.md
  - ../skills/problem-solving.md
source_refs:
  - ../sources/pricing-value-mate-20260422-deepdive-valuemate-pptx.md#objective-and-scope
  - ../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#objective-and-supported-scope
  - ../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#agent-development-and-architecture
---

# Value Mate Pricing Copilot

## Project summary

Two 2026 presentations describe Value Mate, a pricing analytics copilot for
business users querying sell-in, sell-out, and market-quantity data across
regions and B2C/B2B contexts. The April framework presents pricing analysis
use cases, an agentic workflow, natural-language query planning, SQL
validation, and a demo. The September deep dive develops the concept into a
more detailed Text-to-SQL architecture with workflow orchestration, state
management, human confirmation, SQL validation, observability/evaluation,
authentication, and data-access controls.

The sources describe an evolution in the proposed/implemented framework, but
do not independently establish which components were deployed or allocate
individual implementation responsibility.

## Sources

- [Value Mate Pricing Copilot Framework Deep Dive](../sources/pricing-value-mate-20260422-deepdive-valuemate-pptx.md) — **needs review**; 18 slides, 1 note, and 32 media items.
- [Value Mate / DOTI Agentix Pricing Copilot Deep Dive](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md) — **needs review**; 25 slides, 7 notes, and 72 media items.

## Know-how needed

These are suggested project requirements pending user review. They describe
project needs, not personal experience, skill, or mastery.

| Skill | Review status | Rationale |
|---|---|---|
| [Pricing analytics and margin-bridge calculations for data agents](../skills/pricing-analytics-and-margin-bridge-calculations-for-data-agents.md) | user-confirmed | The intended agent answers pricing questions about margin, volume, market share, competition, and margin bridges ([scope](../sources/pricing-value-mate-20260422-deepdive-valuemate-pptx.md#objective-and-scope); [use cases](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#demonstrations-and-use-cases)). |
| [Natural-language-to-SQL for multi-table pricing datasets](../skills/natural-language-to-sql-for-pricing-datasets.md) | user-confirmed | The project centers on flexible natural-language queries over several pricing datasets and database views ([objective](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#objective-and-supported-scope)). |
| [Agentic workflow orchestration and tool integration](../skills/agentic-workflow-orchestration-and-tool-integration.md) | user-confirmed | The deck describes router, planning, SQL, output, retrieval, and human-in-the-loop components coordinated as an agent workflow ([framework](../sources/pricing-value-mate-20260422-deepdive-valuemate-pptx.md#agent-workflow-and-query-example); [architecture](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#agent-development-and-architecture)). |
| [Query understanding, planning, and schema pruning for Text-to-SQL](../skills/query-understanding-planning-and-schema-pruning-for-text-to-sql.md) | user-confirmed | The workflow uses query enhancement, intent/keyword extraction, schema pruning, planning, and SQL validation before execution ([workflow](../sources/pricing-value-mate-20260422-deepdive-valuemate-pptx.md#agent-workflow-and-query-example); [reliability](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#trustworthy-text-to-sql-workflow)). |
| [Schema and data-value grounding with retrieval for enterprise SQL agents](../skills/schema-and-value-grounding-for-enterprise-sql-agents.md) | user-confirmed | The detailed design describes authorized-view selection and grounding spoken filters to stored values, with retrieval services and FAISS in the architecture ([context management](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#context-management); [speaker notes](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#speaker-notes)). |
| [SQL validation, repair, and dialect-aware execution](../skills/sql-validation-repair-and-dialect-aware-execution.md) | user-confirmed | The sources discuss schema-aware checks, syntax checks, EXPLAIN, controlled repair/retry, failed-query analysis, and Dremio/SQLite dialect differences ([validation](../sources/pricing-value-mate-20260422-deepdive-valuemate-pptx.md#validation-and-evaluation); [reliability](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#trustworthy-text-to-sql-workflow)). |
| [Component-agnostic database and service integration for agent systems](../skills/component-agnostic-data-service-integration-for-agents.md) | user-confirmed | The architecture separates agent capabilities from Dremio, retrieval, domain rules, and storage providers ([architecture](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#agent-development-and-architecture)). |
| [Conversation-state management and memory isolation for agents](../skills/conversation-state-management-and-memory-isolation.md) | user-confirmed | The later deck separates durable conversation state from disposable SQL execution, and describes checkpointed state and scoped memory ([context management](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#context-management)). |
| [Human-in-the-loop clarification and recoverable execution](../skills/human-in-the-loop-clarification-and-recoverable-agent-workflows.md) | user-confirmed | The workflow pauses for table/filter/formula confirmation and resumes from checkpoints rather than guessing when a gate fails ([reliability](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#trustworthy-text-to-sql-workflow)). |
| [Evaluation of data-agent plans, SQL, and answers against ground truth](../skills/evaluation-of-data-agent-plans-and-answers.md) | user-confirmed | The decks propose plan-quality and execution measures and show output comparison with ground truth ([evaluation](../sources/pricing-value-mate-20260422-deepdive-valuemate-pptx.md#validation-and-evaluation); [evaluation](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#observability-and-evaluation)). |
| [Agent observability and feedback-driven quality/release loops](../skills/observability-and-feedback-loops-for-data-agents.md) | user-confirmed | The 2026 deep dive describes trace capture, feedback, curated answers, expert expectations, offline evaluation, and promotion/rejection gates ([observability](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#observability-and-evaluation)). |
| [Enterprise identity, authorization, and data-access controls for agents](../skills/enterprise-identity-and-access-control-for-agents.md) | user-confirmed | The security design separates application access from Dremio data access and describes table/region authorization and identity integration ([access control](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#authentication-and-access-control)). |
| [Streaming APIs and interactive UI for agent workflows](../skills/streaming-api-and-ui-design-for-agent-workflows.md) | user-confirmed | The architecture includes a web UI, FastAPI, server-sent events, typed results/errors, and interactive confirmation ([architecture](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#agent-development-and-architecture)). |
| [Data standardization across regions and heterogeneous pricing sources](../skills/data-standardization-for-multi-region-pricing-analytics.md) | user-confirmed | The decks identify inconsistent variables and heterogeneous sources as an integration challenge and follow-up task ([challenges and next steps](../sources/pricing-value-mate-20260422-deepdive-valuemate-pptx.md#data-access-implementation-and-next-steps); [scope](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#objective-and-supported-scope)). |
| [Spec-driven and test-covered delivery of maintainable agentic products](../skills/spec-driven-agent-product-delivery.md) | user-confirmed | The code-structure slide describes a spec/plan/test/implementation/verification workflow and coverage target ([implementation practices](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#implementation-and-code-structure)). |
| [Comprehensive literature review to finalize agentic workflow design](../skills/literature-review-for-agentic-workflow-design.md) | user-confirmed | Added by the user; both decks include literature-review sections that discuss approaches relevant to the workflow ([April review](../sources/pricing-value-mate-20260422-deepdive-valuemate-pptx.md#literature-review); [September review](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#literature-review)). |
| [Cross-functional team collaboration](../skills/cross-functional-team-collaboration.md) | user-confirmed | Added by the user as relevant to working across technical teams, business stakeholders, and early adopters ([project team](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#project-team-and-cover)). |
| [Team leadership](../skills/team-leadership-and-direction.md) | user-confirmed | Added by the user as a project need; the source identifies a cross-functional team but does not establish individual leadership contributions ([project team](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#project-team-and-cover)). |
| [Stakeholder management](../skills/stakeholder-management.md) | user-confirmed | Added by the user; the project involves business stakeholders, sponsors, and early adopters whose needs and feedback inform the product ([project team](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#project-team-and-cover); [objective](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#objective-and-supported-scope)). |
| [Leadership communication](../skills/leadership-communication.md) | user-confirmed | Added by the user as a project need for communicating product objectives, system design, and progress to decision-makers. |
| [Decision support and facilitation](../skills/decision-support-and-facilitation.md) | user-confirmed | Added by the user; Value Mate is intended to provide transparent pricing analytics that help pricers make business decisions ([objective](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#objective-and-supported-scope)). |
| [Team leadership under tight deadlines](../skills/team-leadership-under-tight-deadlines.md) | user-confirmed | Added by the user as a project need; no specific deadline or personal leadership outcome is established in the sources. |
| [Problem solving](../skills/problem-solving.md) | user-confirmed | Added by the user as the ability to devise useful solutions at critical project stages; the deck lists product and workflow challenges ([challenges](../sources/pricing-value-mate-20260422-deepdive-valuemate-pptx.md#data-access-implementation-and-next-steps); [challenges](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#implementation-and-code-structure)). |

## Skills shown by sources

These entries describe source content, not personal mastery or individual
implementation responsibility.

| Skill | Evidence status | Evidence |
|---|---|---|
| [Pricing analytics and margin-bridge calculations for data agents](../skills/pricing-analytics-and-margin-bridge-calculations-for-data-agents.md) | documented | The presentations list pricing questions and calculations involving sales, margins, competition, market size, and margin bridges ([analytics scope](../sources/pricing-value-mate-20260422-deepdive-valuemate-pptx.md#objective-and-scope); [examples](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#demonstrations-and-use-cases)). |
| [Comprehensive literature review to finalize agentic workflow design](../skills/literature-review-for-agentic-workflow-design.md) | documented | Both presentations contain literature-review sections relevant to Text-to-SQL workflow design; neither establishes review completeness or individual responsibility ([April review](../sources/pricing-value-mate-20260422-deepdive-valuemate-pptx.md#literature-review); [September review](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#literature-review)). |
| [Natural-language-to-SQL for multi-table pricing datasets](../skills/natural-language-to-sql-for-pricing-datasets.md) | documented | The sources describe query-to-plan-to-SQL workflows over pricing datasets ([workflow](../sources/pricing-value-mate-20260422-deepdive-valuemate-pptx.md#agent-workflow-and-query-example); [architecture](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#agent-development-and-architecture)). |
| [Agentic workflow orchestration and tool integration](../skills/agentic-workflow-orchestration-and-tool-integration.md) | documented | The presentations describe routing, planning, SQL, database tools, and output nodes in a coordinated workflow ([workflow](../sources/pricing-value-mate-20260422-deepdive-valuemate-pptx.md#agent-workflow-and-query-example); [architecture](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#agent-development-and-architecture)). |
| [Query understanding, planning, and schema pruning for Text-to-SQL](../skills/query-understanding-planning-and-schema-pruning-for-text-to-sql.md) | documented | Query enhancement, intent/keyword extraction, schema pruning, planning, and SQL checking are described ([workflow](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#trustworthy-text-to-sql-workflow)). |
| [Schema and data-value grounding with retrieval for enterprise SQL agents](../skills/schema-and-value-grounding-for-enterprise-sql-agents.md) | documented | The deck and speaker notes describe authorized-view selection, stored-value grounding, and retrieval services ([context](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#context-management); [notes](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#speaker-notes)). |
| [SQL validation, repair, and dialect-aware execution](../skills/sql-validation-repair-and-dialect-aware-execution.md) | documented | Schema, syntax, destructive-operation, and EXPLAIN checks plus controlled repair are described ([validation](../sources/pricing-value-mate-20260422-deepdive-valuemate-pptx.md#validation-and-evaluation); [Text-to-SQL workflow](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#trustworthy-text-to-sql-workflow)). |
| [Component-agnostic database and service integration for agent systems](../skills/component-agnostic-data-service-integration-for-agents.md) | documented | The later deck describes capability contracts and replaceable database, retrieval, domain, and storage providers ([architecture](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#agent-development-and-architecture)). |
| [Conversation-state management and memory isolation for agents](../skills/conversation-state-management-and-memory-isolation.md) | documented | The later deck and speaker notes describe context separation, state checkpoints, and disposable execution state ([context](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#context-management); [notes](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#speaker-notes)). |
| [Human-in-the-loop clarification and recoverable execution](../skills/human-in-the-loop-clarification-and-recoverable-agent-workflows.md) | documented | Table/filter confirmations, checkpointed pauses, and recoverable execution are described ([Text-to-SQL workflow](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#trustworthy-text-to-sql-workflow); [notes](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#speaker-notes)). |
| [Evaluation of data-agent plans, SQL, and answers against ground truth](../skills/evaluation-of-data-agent-plans-and-answers.md) | documented | The sources describe plan-quality criteria and output comparison against ground truth ([evaluation](../sources/pricing-value-mate-20260422-deepdive-valuemate-pptx.md#validation-and-evaluation); [later evaluation](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#observability-and-evaluation)). |
| [Agent observability and feedback-driven quality/release loops](../skills/observability-and-feedback-loops-for-data-agents.md) | documented | The speaker notes and slides describe tracing, user feedback, approved-answer curation, evaluation, and a release gate ([observability](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#observability-and-evaluation)). |
| [Enterprise identity, authorization, and data-access controls for agents](../skills/enterprise-identity-and-access-control-for-agents.md) | documented | Application/database identity and table/region access controls are outlined ([access control](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#authentication-and-access-control)). |
| [Streaming APIs and interactive UI for agent workflows](../skills/streaming-api-and-ui-design-for-agent-workflows.md) | documented | The architecture describes a web UI, FastAPI/SSE, typed results/errors, and interaction gates ([architecture](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#agent-development-and-architecture)). |
| [Spec-driven and test-covered delivery of maintainable agentic products](../skills/spec-driven-agent-product-delivery.md) | documented | The code-structure slide lists spec/plan/test/verify practices, dead-code checks, and a coverage target ([implementation practices](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#implementation-and-code-structure)). |

## Attribution and scope uncertainty

| Claim | Status | Evidence |
|---|---|---|
| The September deck lists Gaurav Adke as a DOTI-DAI Senior Data Scientist on the project team. | documented | [Project team](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#project-team-and-cover). |
| The team listing establishes Gaurav's responsibility for specific features or implementation outcomes. | unknown | The presentation does not map named individuals to specific components or completed work. |
| The speaker notes describe parts of the tracing/feedback workflow as in production. | documented | [Speaker notes](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#speaker-notes). This is source-reported and has not been independently verified. |
| The April and September presentations describe the same deployed code/version. | unknown | The decks share the Value Mate / pricing-copilot framing, but implementation lineage is not independently established. |

## User-reported contributions and outcomes

No personal contributions or outcomes have been user-reported for this
project.

## Review state

Text was extracted from both presentations (43 slides total), including
speaker notes from the September deck. The two April slides with no extracted
text and all 104 embedded media items remain uninspected. Reported product
state, metrics, and team responsibilities have not been independently
verified. Twenty-three know-how requirements have been user-confirmed. The seven
user-added soft-skill requirements remain project needs, not claims about
personal experience; source material does not assign individual leadership
or stakeholder responsibilities.
