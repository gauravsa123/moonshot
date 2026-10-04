---
id: agents-latent-mas-20260112-latentmas-v01-pptx
type: source
title: Latent MAS presentation
aliases: []
related:
  - ../projects/agents-latent-mas.md
source_refs: []
---

# Latent MAS presentation

- **Status:** needs review
- **Original path:** `raw/Agents/Latent MAS/20260112_LatentMAS_v01.pptx`
- **Readability:** Slide text was extracted locally from all 25 slides. The 23 notes-slide files were also parsed; two contain supplemental reference URLs, with no substantive narrative notes. The deck contains 45 embedded media files.
- **Reason for review:** Embedded media, diagrams, screenshots, and result visuals were not rendered or visually inspected; no OCR was performed on images. The text extraction supports a summary of the slide content but cannot verify visual relationships or plotted results. In particular, the text states semantic-plan improvement without giving numeric results for the Price Copilot experiment.
- **Original format:** PowerPoint, 25 slides. The source under `raw/` was not modified; no packages were installed and no external services or links were used.

## Summary

The deck introduces latent collaboration between language-model agents: instead
of exchanging only generated text, agents exchange continuous hidden states
and KV-cache state as latent working memory. It presents this as potentially
more expressive, lower-token, and faster than text-mediated multi-agent
communication, while also identifying open-weight access, interpretability,
and tool/API integration as limitations.

The deck describes an experiment applying LatentMAS to Price Copilot planning.
It names Qwen 4B and 14B models, 0 and 40 hidden steps, conversion from
Hugging Face/PyTorch to MLX for Apple Silicon, 65 pricing questions with
GPT-5.1-generated ground-truth plans, and LLM-as-a-judge, embedding similarity,
and token count as evaluation measures. A Planner/Critic/Refiner configuration
and SQL-plan examples are shown. The deck claims semantic improvement for
complex questions, but the extracted text does not provide numeric outcomes
for this experiment; the result visuals were not reviewed. Context compression, latent RAG and
memory, easier-to-use components, and broader multi-agent use cases are
presented as potential applications or future work, not verified deliverables.

Slide 15 includes a long-form summary of the cited LatentMAS paper and reports
benchmark claims of up to about 14.6% higher accuracy, 70–84% fewer output
tokens, and about 4× faster inference. These statements are attributed to that
deck summary and are kept separate from the Price Copilot experiment.

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The deck introduces latent collaboration and contrasts text messages with sharing latent representations between agents. | documented | [Slides 3](#slide-3)–[8](#slide-8). |
| It describes hidden states as carrying intermediate reasoning and proposes KV-cache transfer as latent working memory. | documented | [Slides 5](#slide-5), [6](#slide-6), [15](#slide-15), and [22](#slide-22). |
| The deck identifies potential efficiency benefits as well as model-access, interpretability, and tool-calling limitations. | documented | [Slides 7](#slide-7), [15](#slide-15), [17](#slide-17), and [22](#slide-22). |
| A Price Copilot SQL-planning experiment uses Qwen, 0/40 hidden steps, 65 questions, and GPT-5.1-generated ground-truth plans, with LLM-judge, embedding-similarity, and token-count comparisons. | documented | [Slide 10](#slide-10). |
| The deck claims improved semantic closeness on complex questions; the extracted text supplies no numeric results for this experiment. | documented | [Slides 11](#slide-11)–[12](#slide-12); result visuals were not inspected. |
| The work replicated the paper implementation with Qwen and was being extended to multi-agent use cases; API-model compatibility remained exploratory. | documented | [Slide 22](#slide-22). |
| Context compression, latent RAG/memory, and wider agent applications are completed implementations. | unknown | They are presented as applications, future steps, or investigations ([slides 8](#slide-8), [13](#slide-13), [18](#slide-18), [19](#slide-19), [22](#slide-22)). |
| Individual author roles, contributions, or mastery are established. | unknown | The title slide lists Gaurav Adke, Ameya Divekar, and DAI/DOTI, without assigning individual roles ([slide 1](#slide-1)). |

## Slide references

### Slide 1

Title: “Latent MAS”; lists Gaurav Adke, Ameya Divekar, and DAI/DOTI. No
individual responsibilities are assigned.

### Slide 2

Agenda topics include latent collaboration, latent reasoning transfer,
multi-agent use cases, context compression, latent RAG, latent memory, and
experimentation on Price Copilot planning.

### Slide 3

Introduces latent collaboration through a human analogy between text messages
and direct sharing of mental context, then contrasts text-based agent
reflection with latent communication.

### Slide 4

Cites the LatentMAS paper and labels KV-cache exchange, training-based methods,
and methods requiring no additional training.

### Slide 5

Describes hidden states as continuous representations that can carry
exploration and planning context not expressed in the selected discrete token
sequence.

### Slide 6

Explains queries, keys, values, and attention, then presents KV cache as
latent working memory transferred between agents. The deck characterizes
receiving this state as analogous to receiving the prior agent's
input/output.

### Slide 7

Compares text-mediated and latent collaboration. Alongside claimed benefits
such as fewer tokens and faster reasoning, it lists trade-offs: API-only
models cannot be used, and latent/tool interactions are less interpretable
and require embedding-based tool calling.

### Slide 8

Lists potential applications: multi-agent planning and analysis, context
compaction, latent RAG, latent memory, and quick experimentation. These are
presented as possibilities, not as completed features.

### Slide 9

Introduces experimentation, cites the paper, and mentions reasoning-intensive
datasets and efficiency gains. No experiment metrics are given in the
extracted text.

### Slide 10

Describes the Price Copilot planning experiment: single-agent baseline versus
LatentMAS-generated SQL plans; Qwen 4B/14B, hidden-step counts of 0/40,
Hugging Face/PyTorch-to-MLX conversion for Apple Silicon, 65 pricing questions
with GPT-5.1-generated reference plans, and LLM-judge, embedding-similarity,
and token-count measures. The multi-agent roles are Planner, Critic, and
Refiner.

### Slide 11

Labels baseline, LatentMAS, and ground truth for comparisons on two pricing
questions. The extracted text does not expose numeric results; visuals were
not reviewed.

### Slide 12

States that semantic closeness improves on complex questions requiring longer
plans and labels a comparison of LatentMAS and GPT-5.1 token counts. The
extracted text does not provide numeric scores or totals; visuals were not
reviewed.

### Slide 13

Lists future work on an easy-to-use component for agentic use cases and
exploration of context compression.

### Slide 14

Closing slide.

### Slide 15

Contains a long-form LatentMAS overview: training-free latent collaboration,
hidden-state “thoughts,” shared layer-wise KV caches, input-space alignment,
theoretical and practical claims, limitations, and applications. It reports
up to about 14.6% higher accuracy, 70–84% fewer output tokens, and about 4×
faster inference on cited benchmark tasks. These are claims in the deck's
paper summary, not the Price Copilot results.

### Slide 16

Contains example SQL-plan steps for total tonnage and top-five SKU margin
growth questions, alongside natural-language planning steps.

### Slide 17

Notes that real multi-agent workflows may need to pass tool responses,
schemas, and other inputs along with latent state, rather than only replacing
agent text with embeddings. It cites a related paper.

### Slide 18

Lists Sales Ticket Agent, Agentic Claim Manager, and Pricing Copilot as
possible use cases; identifies implementation work and open-weight/API
constraints; and proposes latent representations or lightweight projections
for tool choice. It also suggests latent reflection steps.

### Slide 19

Discusses KV-cache growth, possible clipping, hidden-step generation and
redundancy, and TODOs for PCA/latent visualizations and comparisons. These
items are exploratory questions, not all completed work.

### Slide 20

Provides literature-review text on latent reasoning and cross-model latent
collaboration, contrasting single-model latent reasoning with inter-agent
state sharing and describing the referenced LatentMAS framework.

### Slide 21

Cites Coconut and includes TODOs for inspecting received latent information,
visualizing exploration, and further explanation of latent iterative
reasoning.

### Slide 22

States that the LatentMAS paper implementation was replicated with Qwen and
that extension to the team's multi-agent use case and API-based models was in
progress. It summarizes hidden-layer output sharing, KV-cache working memory,
and input realignment.

### Slide 23

Lists related multi-agent literature and links, including ideas for combining
reflection with latent embeddings and reward.

### Slide 24

Lists possible Moonshot multi-agent applications in data collection and
analysis, marketing content, project planning, and sales analysis.

### Slide 25

Lists possible CAD/PLM workflows involving geometry comparisons, analysis,
prompted CAD changes, and PLM integration, as well as robotic agents. These
are use-case ideas rather than evidence of completed implementations.
