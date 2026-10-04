---
id: gan-exploration-20200717-gan-study-v5-pptx
type: source
title: GAN study V5 presentation
aliases: []
related:
  - ../projects/gan-exploration-image-synthesis-and-augmentation.md
source_refs: []
---

# GAN study V5 presentation

- **Status:** needs review
- **Original path:** `raw/GAN/Exploration/20200717_GAN_study_V5.pptx`
- **Extraction:** Text was extracted locally from all 35 slides. The archive
  contains 164 embedded media files that were not rendered or visually
  inspected.
- **Reason for review:** The deck is image-heavy; generated samples, plots,
  and diagrams may contain details missing from text extraction.
- **Original format:** PowerPoint, 35 slides. No packages or external services
  were used for extraction.

## Summary

This version introduces GAN concepts and image-generation use cases, then
describes steel-surface defects, tire-conicity image generation, Progressive
GAN, training difficulties, and possible applications. It reports a
three-way FID comparison for Progressive GAN and differential augmentation,
but the images and results have not been independently inspected
([slides 2](#slide-2), [4](#slide-4), [9](#slide-9),
[27](#slide-27), [28](#slide-28)).

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The deck presents GANs for synthetic image generation and surface-defect data augmentation. | documented | [Slides 2](#slide-2), [4](#slide-4). |
| Progressive GAN is used in tire-conicity image experiments at increasing resolutions. | documented | [Slide 9](#slide-9). |
| GAN training instability, mode collapse, training time, and data needs are discussed. | documented | [Slide 15](#slide-15). |
| The deck reports FID values for differential augmentation experiments. | documented | [Slides 27](#slide-27), [28](#slide-28). |
| Image quality or reported FID results are validated by this source record. | unknown | Embedded images and metric calculations were not reviewed. |

## Slide references

### Slide 2

Explains the generator/discriminator objective and frames GANs as a way to
generate samples similar to, but not copies of, training data.

### Slide 4

Proposes GAN use for steel-surface defect analysis, including synthetic
samples and labels to address data imbalance.

### Slide 9

Describes progressive layer growth and training across image sizes from 4x4
to 256x256 for tire-conicity images.

### Slide 12

Labels latent-vector variation examples involving color, texture, zoom, and
the addition of tire/column features. Visuals were not inspected.

### Slide 15

Lists instability, hyperparameter sensitivity, mode collapse, training time,
and training-data requirements as challenges.

### Slide 27

Summarizes stated GAN training-data needs, CPU training times, and FID as an
evaluation measure.

### Slide 28

Reports FID values for Progressive GAN runs with and without differential
augmentation. Values are not independently reproduced.

### Slide 33

Labels mode collapse and lists techniques and future experiments intended to
address variation in generated images.
