---
id: agents-latent-mas
type: project
title: Latent MAS
aliases: []
related:
  - ../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md
  - ../skills/latent-state-multi-agent-collaboration.md
  - ../skills/hidden-state-and-kv-cache-transfer.md
  - ../skills/agentic-workflow-orchestration-and-tool-integration.md
  - ../skills/context-compression.md
  - ../skills/plan-evaluation-against-ground-truth.md
  - ../skills/mlx-inference-with-open-weight-models.md
  - ../skills/research-paper-comprehension-and-implementation-adaptation.md
  - ../skills/pytorch-to-mlx-conversion.md
  - ../skills/applying-learned-research-techniques-to-project.md
  - ../skills/local-coding-agent-integration.md
  - ../skills/rapid-learning-and-research-of-complex-papers.md
  - ../skills/accessible-explanation-of-complex-algorithms.md
source_refs:
  - ../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-3
  - ../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-6
  - ../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-8
  - ../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-10
  - ../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-12
  - ../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-15
  - ../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-17
  - ../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-18
  - ../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-19
  - ../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-22
---

# Latent MAS

## Project summary

The presentation explores LatentMAS, a training-free approach to multi-agent
collaboration in which language-model agents pass continuous hidden-state
representations and KV-cache working memory instead of relying only on
text-generated messages. It presents this as a way to preserve intermediate
reasoning and reduce token-generation overhead, while noting trade-offs such
as the need for model-weight access, limited interpretability, and difficulty
handling tool calls and structured inputs ([slides 5–8](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-5),
[17–19](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-17),
[22](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-22)).

The deck describes a Price Copilot planning experiment: Qwen 4B/14B
models, 0 or 40 hidden steps, a Planner/Critic/Refiner setup, and 65 pricing
questions with GPT-5.1-generated ground-truth plans. It names LLM-as-a-judge,
embedding similarity, and token count as evaluation measures. The deck claims
better semantic closeness for harder questions but the extracted text provides
no numerical results for this experiment; its result visuals remain uninspected
([slides 10–12](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-10),
[16](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-16)).
Context compression, latent RAG/memory, broader agent use cases, and API-model
compatibility appear as applications or future work, not as completed
deliverables ([slides 8](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-8),
[13](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-13),
[18–19](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-18)).

The source title slide names Gaurav Adke and Ameya Divekar, but does not assign
individual roles or contributions. Personal contribution and mastery are
therefore unknown; none is inferred from the author list.

## Sources

- [Latent MAS presentation](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md)
  — **needs review**; text was extracted from all 25 slides, but 45 embedded
  media items and their visual context were not inspected.

## Know-how needed

These are project-specific requirements, not claims about personal experience
or demonstrated mastery. The user confirmed all ten requirements below.

| Skill | Review status | Rationale |
|---|---|---|
| [Latent-state multi-agent collaboration](../skills/latent-state-multi-agent-collaboration.md) | user-confirmed | The project centers on exchanging latent thoughts and shared state rather than only text messages ([slides 3–8](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-3), [15](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-15), [22](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-22)). |
| [Hidden-state and KV-cache transfer](../skills/hidden-state-and-kv-cache-transfer.md) | user-confirmed | The described mechanism depends on passing layer-wise KV state and aligning prior hidden representations for another agent/model ([slides 6](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-6), [15](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-15), [22](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-22)). |
| [Agentic workflow orchestration and tool integration](../skills/agentic-workflow-orchestration-and-tool-integration.md) | user-confirmed | The deck outlines a Planner/Critic/Refiner flow and identifies tool responses, schemas, and latent-state handoff as integration challenges ([slides 10](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-10), [17–18](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-17)). This general canonical skill is related, not a replacement for the distinct latent-collaboration topic. |
| [Context compression](../skills/context-compression.md) | user-confirmed | The deck proposes context compaction and lists further context-compression work; this requirement is separate from its latent RAG and latent-memory ideas ([slides 8](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-8), [13](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-13)). |
| [Plan evaluation against ground truth](../skills/plan-evaluation-against-ground-truth.md) | user-confirmed | The experiment compares plans with GPT-5.1-generated references using an LLM judge, embedding similarity, and token counts ([slides 10–12](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-10)). This is more specific than retrieval-answer evaluation. |
| [MLX inference with open-weight models](../skills/mlx-inference-with-open-weight-models.md) | user-confirmed | The described setup uses Qwen models with MLX on Apple Silicon ([slides 10](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-10), [22](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-22)). |
| [Research-paper comprehension and implementation (Latent MAS application)](../skills/research-paper-comprehension-and-implementation-adaptation.md) | user-confirmed | The project involves understanding and implementing techniques from the LatentMAS paper; this project-specific formulation reuses the closely matching canonical research-comprehension/adaptation page without treating similar research skills as aliases ([slides 15](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-15), [22](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-22)). |
| [PyTorch-to-MLX conversion](../skills/pytorch-to-mlx-conversion.md) | user-confirmed | The experiment converts Hugging Face/PyTorch Qwen models to MLX for Apple Silicon ([slide 10](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-10)). |
| [Applying learned research techniques to the project](../skills/applying-learned-research-techniques-to-project.md) | user-confirmed | The user confirmed applying techniques learned from research to this project as a distinct requirement, beyond paper comprehension or implementation adaptation. |
| [Local coding-agent integration](../skills/local-coding-agent-integration.md) | user-confirmed | The user confirmed local coding-agent integration as an innovative project requirement. |

## Skills shown by sources

The source documents approaches and an experiment, but it does not attribute
technical work or mastery to any individual. These source-evidenced
capabilities describe the material only.

| Skill or capability | Evidence status | Evidence |
|---|---|---|
| Latent-state communication and KV-cache working-memory transfer | documented | [Slides 5–8](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-5), [15](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-15), [22](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-22). |
| Plan generation and comparison using a Planner/Critic/Refiner setup | documented | [Slides 10–12](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-10), [16](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-16). The claimed semantic improvement is not quantitatively verifiable from extracted text. |
| Latent context compression, retrieval, and memory applications | documented | Presented as potential uses or future exploration, not completed system features ([slides 8](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-8), [13](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-13)). |

## User-reported contributions and outcomes

The following capabilities are reported by the user, not established by the
presentation. They are not source-documented claims or evidence of project
implementation.

| Capability | Status | Details |
|---|---|---|
| [Rapid learning and quick research of complex papers](../skills/rapid-learning-and-research-of-complex-papers.md) | user-reported | The user reports rapidly learning and researching complex papers. This page is distinct from the project's confirmed requirement for research-paper comprehension and implementation; the presentation does not establish this personal capability. |
| [Accessible explanation of complex algorithms](../skills/accessible-explanation-of-complex-algorithms.md) | user-reported | The user reports sharing and explaining the complex algorithm to a wider audience in accessible language. The presentation does not establish this personal capability. |

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The deck describes latent collaboration as passing model hidden states and KV-cache memory between agents, and contrasts this with text-only communication. | documented | [Slides 3–8](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-3), [15](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-15), [22](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-22). |
| The deck describes a Price Copilot SQL-planning experiment with Qwen models, 0/40 hidden steps, 65 questions, GPT-5.1 reference plans, and three evaluation measures. | documented | [Slide 10](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-10). |
| The deck states semantic-plan improvement for more complex questions, but extracted text contains no numerical scores or token totals for this experiment. | documented | The statement and comparison labels appear on [slides 11–12](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-11); figures were not visually inspected. |
| A long-form slide summary reports benchmark claims of up to about 14.6% higher accuracy, 70–84% fewer output tokens, and about 4× faster inference. | documented | [Slide 15](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-15). These are claims in the deck's summary of the cited paper, not results of the Price Copilot experiment. |
| Context compression, latent RAG and memory, wider agent use cases, and API-model compatibility are completed project deliverables. | unknown | The deck frames these as applications, future steps, or open work ([slides 8](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-8), [13](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-13), [18–19](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-18), [22](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-22)). |
| Individual roles, implementation ownership, or personal mastery are established. | unknown | The title slide names two people and an organization, but assigns no individual responsibilities ([slide 1](../sources/agents-latent-mas-20260112-latentmas-v01-pptx.md#slide-1)). |

## Review state

The source remains **needs review** because embedded visuals were not
inspected. All ten know-how requirements are `user-confirmed` project
requirements, not claims about personal mastery. The two reported capabilities
remain separate from source evidence. The full technical, specification, and
quality self-review and local link validation were completed after ingestion.
