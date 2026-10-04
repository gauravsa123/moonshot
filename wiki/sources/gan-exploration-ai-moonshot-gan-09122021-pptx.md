---
id: gan-exploration-ai-moonshot-gan-09122021-pptx
type: source
title: AI Moonshot GAN summary and applications presentation
aliases: []
related:
  - ../projects/gan-exploration-image-synthesis-and-augmentation.md
source_refs: []
---

# AI Moonshot GAN summary and applications presentation

- **Status:** needs review
- **Original path:** `raw/GAN/Exploration/AI_Moonshot_GAN_09122021.pptx`
- **Extraction:** Text was extracted locally from all 30 slides. The archive
  contains 148 embedded media files that were not rendered or visually
  inspected. The date-like filename label is not used to infer a presentation
  date.
- **Reason for review:** Application results, diagrams, and generated images
  require visual review; numerical values below remain claims made by the
  presentation.
- **Original format:** PowerPoint, 30 slides. No packages or external
  services were used for extraction.

## Summary

The presentation summarizes GAN augmentation applications and development,
including tire-health and tire-joint classification, OCR and Hormiga
preprocessing, IRIS2 image generation, and an Azure ML GAN-training pipeline.
It describes selecting diverse generated samples, focusing augmentation on
poorly classified classes, latent interpolation/style merging, and
source-reported classification results ([slides 3](#slide-3),
[4](#slide-4), [6](#slide-6), [7](#slide-7), [8](#slide-8),
[12](#slide-12), [22](#slide-22)).

The deck also names a publication and white paper, both with progress-status
qualifiers, and discusses a future image-processing API. The API proposal is
not merged with the separate API Hackathon or APIGEE profiles in this wiki
([slides 13](#slide-13), [14](#slide-14)).

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The deck reports GAN augmentation experiments for tire-health and tire-joint classification. | documented | [Slides 3](#slide-3), [7](#slide-7), [8](#slide-8). |
| It describes filtering generated samples and using class-wise model performance to guide augmentation. | documented | [Slides 4](#slide-4), [5](#slide-5). |
| An Azure ML GAN training pipeline is described as a deliverable. | source-reported | [Slide 12](#slide-12); implementation artifacts have not been independently inspected. |
| A publication and white paper are documented as completed personal contributions. | unknown | [Slide 13](#slide-13) labels progress states and does not assign individual contributions. |
| The listed experiment results are independently validated. | unknown | The source material and result visuals have not been independently reviewed. |

## Slide references

### Slide 2

Summarizes GAN competency development, application domains, business use
cases, and deliverables; items are not treated as proof of individual
contribution.

### Slide 3

Reports a tire-health image-classification experiment, including class
imbalance, GAN-generated defective samples, and validation-accuracy values.

### Slide 4

Describes extracting unique generated images using VGG features and cosine
similarity to reduce near-duplicates.

### Slide 5

Describes using class-wise recall to target poorly classified classes and
mentions U-Net GAN and StyleGAN experiments.

### Slide 6

Labels style merging and latent-vector interpolation for image generation.
Examples were not visually inspected.

### Slide 7

Reports tire-health validation-accuracy comparisons for targeted augmentation
and merged images. Values are not independently reproduced.

### Slide 8

Reports tire-joint defect augmentation experiments and overall accuracy
values. These are source-reported results, not independently validated.

### Slide 9

Lists OCR-related GAN image generation as work in progress and describes
low-light image enhancement using EnlightenGAN.

### Slide 10

Describes Hormiga road-stone detection preprocessing and selective light
enhancement as work in progress.

### Slide 11

Summarizes use cases and notes image-size and dataset-size limitations.

### Slide 12

Describes an Azure ML low-code GAN training pipeline with image generation,
unique-image extraction, configurable trained weights, and possible API
publication. This slide does not independently establish deployment.

### Slide 13

Lists a white paper as in progress and a conference publication as accepted
and under printing; the slide does not establish individual authorship.

### Slide 14

Proposes an image-processing service API following an API hackathon idea and
notes that resources would be required for implementation.

### Slide 17

Summarizes the Moonshot activity, data synthesis, knowledge sharing, and
community/business applications.

### Slide 21

Describes tire-joint classification experiments and reports accuracy values
for real-data and GAN-augmentation variants.

### Slide 22

Describes IRIS2 image generation across six image modalities and identifies
higher-resolution generation as an area of work.

### Slide 27

Describes approaches for generating higher-resolution IRIS2 images using
multi-GPU processing or modified layer-channel configurations.
