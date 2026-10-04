---
id: gan-exploration-20200925-gan-overview-pdf
type: source
title: GAN overview presentation (25 September 2020)
aliases: []
related:
  - ../projects/gan-exploration-image-synthesis-and-augmentation.md
source_refs: []
---

# GAN overview presentation (25 September 2020)

- **Status:** needs review
- **Original path:** `raw/GAN/Exploration/20200925_GAN_overview.pdf`
- **Extraction:** Text was extracted locally from all 18 pages with `pdftotext`.
  Figures and generated-image examples were not visually inspected.
- **Reason for review:** The deck relies on diagrams and image examples for
  GAN architecture and generated results; text extraction alone does not
  establish their contents or quality.
- **Original format:** PDF, 18 pages. No packages or external services were
  used for extraction.

## Summary

The presentation explains GAN fundamentals and proposes computer-vision
applications in surface-defect analysis. It illustrates conditional GAN
generation and tire-conicity experiments, then discusses Progressive GAN,
possible use cases, training challenges, and future work
([pages 2](#page-2), [4](#page-4), [7](#page-7), [8](#page-8),
[9](#page-9), [15](#page-15), [16](#page-16)).

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The deck describes generator/discriminator roles and synthetic image generation. | documented | [Page 2](#page-2). |
| Surface-defect augmentation and conditional generation are proposed. | documented | [Pages 4](#page-4), [7](#page-7). |
| Progressive GAN and tire-conicity image experiments are described. | documented | [Pages 8](#page-8), [9](#page-9). |
| Training instability, mode collapse, and data/compute constraints are discussed. | documented | [Page 15](#page-15). |
| The generated-image visuals establish a particular level of quality. | unknown | The embedded examples were not visually inspected. |

## Page references

### Page 1

Title slide names Generative Adversarial Networks and lists Gaurav Adke and
Saurabh Gupta with DCAD. It does not assign individual responsibilities.

### Page 2

Introduces the generator/discriminator objective and the production of new
samples resembling the training distribution.

### Page 4

Proposes GAN-based augmentation for steel-surface defect analysis, including
generating samples and labels for computer-vision model training.

### Page 7

Shows a conditional GAN diagram with labels provided to the generator and
discriminator. The diagram was not visually inspected.

### Page 8

Labels baseline real and generated tire-conicity images and lists image
quality and resolution as next steps. The images were not inspected.

### Page 9

Describes Progressive GAN and image-size progression up to 256x256.

### Page 12

Labels latent-vector variations including color, texture, zoom, and added
tire/column features. Visuals were not inspected.

### Page 14

Lists synthetic data augmentation, labeled data generation, image
preprocessing, and image-domain change as possible GAN applications.

### Page 15

Lists instability, hyperparameter sensitivity, mode collapse, high-resolution
training time, and data requirements as training challenges.

### Page 16

Lists future work including business validation, generic prototypes, feature
control, training-data benchmarking, and text-data exploration.
