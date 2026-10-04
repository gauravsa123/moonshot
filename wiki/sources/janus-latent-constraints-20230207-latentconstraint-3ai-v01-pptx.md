---
id: janus-latent-constraints-20230207-latentconstraint-3ai-v01-pptx
type: source
title: Conditional generation from latent embeddings for tabular and image data
aliases: []
related:
  - ../projects/janus-latent-constraints-controlled-generation.md
source_refs: []
---

# Conditional generation from latent embeddings for tabular and image data

- **Status:** needs review
- **Original path:** `raw/Janus/Latent Constraints/20230207_LatentConstraint_3AI_V01.pptx`
- **Extraction:** Text was extracted from all 15 slides. The file contains 44
  embedded media items and no speaker-note files.
- **Reason for review:** Latent-space diagrams, image results, and tabular
  examples remain uninspected; the deck gives no quantitative evaluation.
- **Original format:** PowerPoint. The source under `raw/` was not modified.

## Summary

The deck proposes applying desired attributes to samples by transforming
latent vectors from a pretrained VAE, rather than retraining the base
generator. An actor/critic method is described for moving latent vectors
toward a target attribute, while distance regularization is intended to
preserve other properties and variation. Examples cover facial attributes
and tabular data, including Wine-quality classes and a free-sulfur-dioxide
feature. The source reports qualitative promise but no quantitative
evaluation.

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The proposed method aims to apply new conditions without retraining the unconditional generator. | documented | [Objective](#slide-4); [conclusions](#slide-14). |
| An actor/critic-style latent transformation is guided by a critic's probability of the desired attribute. | documented | [Latent transformation](#slide-6); diagrams remain unreviewed. |
| Distance regularization is intended to keep transformed vectors near their original positions and reduce loss of variation. | documented | [Distance-penalty rationale](#slide-7); [illustrated comparison](#slide-8), whose figures remain unreviewed. |
| The method is applied to tabular examples, including class and selected-feature changes. | documented | [Tabular methodology](#slide-10); [examples](#slide-11)–[13](#slide-13). |
| A changed target attribute preserves all other dependent features. | contradicted | The deck notes that total sulfur dioxide also changed when free sulfur dioxide was modified, despite that dependency not being explicitly given to the actor/critic ([slide 13](#slide-13)). |
| Conditional-generation quality and downstream benefit are measured. | unknown | No quantitative metrics or downstream evaluation are reported in extracted text. |

## Slide references

### Slide 1

Title: “Conditional generation from latent embeddings for Tabular and Image
data.” The title slide lists Gaurav Adke and Michelin.

### Slide 2

Outlines conditional generation, latent constraints, image results, tabular
conditioning, and conclusions.

### Slide 3

Introduces conditional VAE, conditional GAN, and conditional diffusion as
approaches that can require extra training; notes that adding conditions may
require retraining the model.

### Slide 4

States the objective: apply conditions to generation outputs without
retraining the unconditional generative model. Uses a VAE and a representative
latent space with facial attributes.

### Slide 5

Describes challenges in interpreting high-dimensional latent spaces and
producing realistic, desired-attribute outputs.

### Slide 6

Shows latent-vector transformation using an actor/critic-style model and a
critic probability for the desired attribute.

### Slide 7

Explains distance regularization as a way to keep transformations near
original vectors and preserve variation.

### Slide 8

Compares transformations with and without a distance penalty for a blond-hair
attribute. The images were not visually inspected.

### Slide 9

Shows sampled and transformed image vectors; visual results remain
uninspected.

### Slide 10

Outlines applying latent constraints to tabular data: train a VAE, encode
samples, train an actor/critic, transform a latent vector, and decode to check
the requested attribute. Wine data is named as an example.

### Slide 11

Describes changing a Wine-quality class from 2 to 3 with a stated least-change
goal; the data and results were not independently evaluated.

### Slide 12

Describes selecting attributes, binning them into categories, and conditioning
latent transformations on selected values; temperature limits are given as a
physical-constraint example.

### Slide 13

Shows a free-sulfur-dioxide feature-bin change while retaining the same Wine
quality class. The deck notes that total sulfur dioxide, a dependent feature,
also changed even though it was not explicitly expressed to the actor/critic.

### Slide 14

Claims promising image and tabular results, proposes rule/reward-based
conditions, discusses reconstruction versus ELBO/KL emphasis, notes mode
collapse and base-generator quality as limitations, and lists diffusion as
future work. These claims are not independently verified.

### Slide 15

“Thank you.”
