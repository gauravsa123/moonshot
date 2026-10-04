---
id: janus-latent-constraints-controlled-generation
type: project
title: Janus Latent Constraints: Controlled Generation for Images and Tabular Data
aliases:
  - Janus Latent Constraints
related:
  - ../sources/janus-latent-constraints-20230207-latentconstraint-3ai-v01-pptx.md
  - ../sources/janus-latent-constraints-20240423-janus-p2-latant-v01-pptx.md
  - ../skills/vae-latent-representation-learning.md
  - ../skills/latent-space-constraints-for-controlled-generation.md
  - ../skills/actor-critic-optimization-of-latent-transformations.md
  - ../skills/disentangled-latent-representations-for-controllable-attributes.md
  - ../skills/distance-regularization-for-minimal-change-generation.md
  - ../skills/conditional-generation-for-tabular-data-and-feature-constraints.md
  - ../skills/vae-reconstruction-and-kl-regularization-tradeoffs.md
  - ../skills/evaluation-of-constrained-generative-data.md
  - ../skills/context-conditioned-image-generation-from-structured-metadata.md
  - ../skills/research-paper-comprehension-and-implementation-adaptation.md
  - ../skills/applying-learned-research-techniques-to-project.md
  - ../skills/knowledge-sharing-and-technical-dissemination.md
source_refs:
  - ../sources/janus-latent-constraints-20230207-latentconstraint-3ai-v01-pptx.md#slide-4
  - ../sources/janus-latent-constraints-20230207-latentconstraint-3ai-v01-pptx.md#slide-6
  - ../sources/janus-latent-constraints-20230207-latentconstraint-3ai-v01-pptx.md#slide-13
  - ../sources/janus-latent-constraints-20240423-janus-p2-latant-v01-pptx.md#slide-3
  - ../sources/janus-latent-constraints-20240423-janus-p2-latant-v01-pptx.md#slide-13
---

# Janus Latent Constraints: Controlled Generation for Images and Tabular Data

## Project summary

Two presentations describe latent-space methods for generating samples with
specified attributes. The 2023 deck proposes actor/critic-guided latent
transformations from a VAE representation, with distance regularization to
limit unintended changes; it covers both image attributes and tabular
examples. The 2024 deck focuses on controlled exploration of tabular latent
spaces, distinguishing fixed and controllable variables and showing variants
with different distance penalties and latent-space constraints.

The decks describe related terminology and objectives, but do not establish
that the same implementation or model was used across both. Results are
qualitative in the extracted text; the 91 embedded media items have not been
visually reviewed.

## Sources

- [Conditional generation from latent embeddings for tabular and image data](../sources/janus-latent-constraints-20230207-latentconstraint-3ai-v01-pptx.md) —
  **needs review**; 44 embedded media items remain uninspected.
- [Janus Phase 2 latent constraints for controlled tabular generation](../sources/janus-latent-constraints-20240423-janus-p2-latant-v01-pptx.md) —
  **needs review**; 47 embedded media items remain uninspected.

## Know-how needed

These user-confirmed requirements describe project needs, not personal
experience, skill, or mastery.

| Skill candidate | Status | Rationale |
|---|---|---|
| [VAE-based latent representation learning and generative modeling](../skills/vae-latent-representation-learning.md) | user-confirmed | The 2023 deck encodes samples into VAE latent representations; the later deck discusses main, fixed, and controllable latent spaces ([VAE representation](../sources/janus-latent-constraints-20230207-latentconstraint-3ai-v01-pptx.md#slide-4); [latent spaces](../sources/janus-latent-constraints-20240423-janus-p2-latant-v01-pptx.md#slide-5)). |
| [Latent-space constraints for controlled conditional generation](../skills/latent-space-constraints-for-controlled-generation.md) | user-confirmed | Both decks describe transforming or constraining latent vectors to obtain a requested attribute without retraining the base generator ([objective](../sources/janus-latent-constraints-20230207-latentconstraint-3ai-v01-pptx.md#slide-4); [controlled exploration](../sources/janus-latent-constraints-20240423-janus-p2-latant-v01-pptx.md#slide-6)). |
| [Actor-critic optimization of latent transformations](../skills/actor-critic-optimization-of-latent-transformations.md) | user-confirmed | The 2023 approach uses a transition function/actor and a critic score to move encoded samples toward desired attributes ([actor/critic](../sources/janus-latent-constraints-20230207-latentconstraint-3ai-v01-pptx.md#slide-6)). |
| [Disentangled latent representations for fixed and controllable attributes](../skills/disentangled-latent-representations-for-controllable-attributes.md) | user-confirmed | The 2024 deck separates fixed variables from controllable/output variables and explores where to apply latent constraints ([controlled-space design](../sources/janus-latent-constraints-20240423-janus-p2-latant-v01-pptx.md#slide-3); [results](../sources/janus-latent-constraints-20240423-janus-p2-latant-v01-pptx.md#slide-7)). |
| [Distance regularization for minimal-change generation](../skills/distance-regularization-for-minimal-change-generation.md) | user-confirmed | A distance penalty is used to keep transformed vectors near the input and reduce changes to non-target features ([2023 rationale](../sources/janus-latent-constraints-20230207-latentconstraint-3ai-v01-pptx.md#slide-7); [2024 variants](../sources/janus-latent-constraints-20240423-janus-p2-latant-v01-pptx.md#slide-9)). |
| [Conditional generation for tabular data and feature constraints](../skills/conditional-generation-for-tabular-data-and-feature-constraints.md) | user-confirmed | The decks describe changing class/feature bins and treating selected tabular attributes as controllable while retaining other features ([Wine examples](../sources/janus-latent-constraints-20230207-latentconstraint-3ai-v01-pptx.md#slide-10); [synthetic-data results](../sources/janus-latent-constraints-20240423-janus-p2-latant-v01-pptx.md#slide-8)). |
| [VAE reconstruction and KL-regularization trade-offs](../skills/vae-reconstruction-and-kl-regularization-tradeoffs.md) | user-confirmed | The 2023 conclusion discusses reconstruction versus ELBO/KL emphasis; the 2024 deck notes reconstruction limitations and changes loss components ([conclusion](../sources/janus-latent-constraints-20230207-latentconstraint-3ai-v01-pptx.md#slide-14); [reconstruction note](../sources/janus-latent-constraints-20240423-janus-p2-latant-v01-pptx.md#slide-13)). |
| [Evaluation of constrained generation for realism and feature preservation](../skills/evaluation-of-constrained-generative-data.md) | user-confirmed | The examples require checking requested labels and changes to other features; one Wine example notes an unintended dependent-feature change ([tabular results](../sources/janus-latent-constraints-20230207-latentconstraint-3ai-v01-pptx.md#slide-13); [fixed-variable results](../sources/janus-latent-constraints-20240423-janus-p2-latant-v01-pptx.md#slide-23)). |
| [Context-conditioned image generation from structured metadata](../skills/context-conditioned-image-generation-from-structured-metadata.md) | user-confirmed | The 2023 deck includes VAE latent transformations toward facial attributes such as hair, glasses, age, and expression ([attribute conditions](../sources/janus-latent-constraints-20230207-latentconstraint-3ai-v01-pptx.md#slide-4)). |
| [Research-paper comprehension and implementation adaptation](../skills/research-paper-comprehension-and-implementation-adaptation.md) | user-confirmed | The user added comprehension of a complex AI paper; the decks refer to research informing the latent-space approach ([2023 reference](../sources/janus-latent-constraints-20230207-latentconstraint-3ai-v01-pptx.md#slide-6); [2024 paper reference](../sources/janus-latent-constraints-20240423-janus-p2-latant-v01-pptx.md#slide-3)). |
| [Applying learned research techniques to a project](../skills/applying-learned-research-techniques-to-project.md) | user-confirmed | The user added research-to-implementation for tabular data; the sources describe VAE/latent-constraint approaches applied to Wine and synthetic tabular examples ([Wine workflow](../sources/janus-latent-constraints-20230207-latentconstraint-3ai-v01-pptx.md#slide-10); [scenario results](../sources/janus-latent-constraints-20240423-janus-p2-latant-v01-pptx.md#slide-7)). |

## Skills shown by sources

These entries describe methods and results present in the material, not
personal skill or individual contribution.

| Capability | Evidence status | Evidence |
|---|---|---|
| Latent-vector transformations are proposed for applying desired attributes without retraining the base generator. | documented | [2023 objective](../sources/janus-latent-constraints-20230207-latentconstraint-3ai-v01-pptx.md#slide-4); [conclusion](../sources/janus-latent-constraints-20230207-latentconstraint-3ai-v01-pptx.md#slide-14). |
| Actor/critic guidance and distance penalties are described for latent transformations. | documented | [2023 approach](../sources/janus-latent-constraints-20230207-latentconstraint-3ai-v01-pptx.md#slide-6); [penalty](../sources/janus-latent-constraints-20230207-latentconstraint-3ai-v01-pptx.md#slide-7). |
| The 2024 deck explores fixed/controllable latent dimensions and alternate locations for applying constraints. | documented | [Latent design](../sources/janus-latent-constraints-20240423-janus-p2-latant-v01-pptx.md#slide-5); [constraint variants](../sources/janus-latent-constraints-20240423-janus-p2-latant-v01-pptx.md#slide-17). |
| A tabular example records an unintended change in a dependent feature. | documented | Total sulfur dioxide changes while free sulfur dioxide is modified ([slide 13](../sources/janus-latent-constraints-20230207-latentconstraint-3ai-v01-pptx.md#slide-13)). |
| The user reports a conference talk at the 3AI online event associated with this work. | user-reported | The user added this contribution during profile review; the talk title and event date were not provided. |

## Attribution and scope uncertainty

| Claim | Status | Evidence |
|---|---|---|
| The two presentations use the same implementation or trained model. | unknown | Similar terms and goals appear in both sources, but no implementation lineage is stated. |
| The methods produce quantitatively validated improvements in realism, diversity, or downstream performance. | unknown | Results figures remain uninspected and extracted text reports no quantitative evaluation. |
| An individual's implementation role in the generative-model work is established. | unknown | The title slides list names/teams but do not assign implementation responsibilities. The user separately reports a conference talk. |
| “VAER” in the 2024 presentation has a specific expanded meaning. | unknown | The acronym is not expanded in extracted text ([slide 3](../sources/janus-latent-constraints-20240423-janus-p2-latant-v01-pptx.md#slide-3)). |

## User-reported contributions and outcomes

The user reports a conference talk at a 3AI online event associated with this
work. The talk title and date were not provided.

## Review state

Text was extracted from both decks. The 2023 presentation has 44 embedded
media items and no speaker-note files. The 2024 presentation has 47 embedded
media items and 23 speaker-note files with no substantive note text. All 91
media items and result plots remain unreviewed; no quantitative evaluation
was independently verified. The user confirmed 11 know-how requirements, including two additions:
complex-paper comprehension and applying research to tabular implementation.
The user separately reported a conference talk at a 3AI online event.
