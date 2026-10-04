---
id: gan-exploration-ai-moonshot-gan-01072021-pptx
type: source
title: AI Moonshot GAN methods and applications presentation
aliases: []
related:
  - ../projects/gan-exploration-image-synthesis-and-augmentation.md
source_refs: []
---

# AI Moonshot GAN methods and applications presentation

- **Status:** needs review
- **Original path:** `raw/GAN/Exploration/AI_Moonshot_GAN_01072021.pptx`
- **Extraction:** Text was extracted locally from all 31 slides. The archive
  contains 125 embedded media files that were not rendered or visually
  inspected. The date-like filename label is not used to infer a presentation
  date.
- **Reason for review:** The deck includes image results, diagrams, and plots
  not represented fully by extracted text.
- **Original format:** PowerPoint, 31 slides. No packages or external
  services were used for extraction.

## Summary

The deck presents GAN development as a data-synthesis Moonshot and summarizes
architectural, training, and stability improvements. It covers StyleGAN and
UNET variants, differential augmentation, exponential moving averages,
WGAN-GP and other losses/regularizers, FID comparisons, and application
experiments in tire-joint defects, IRIS2, and tire health
([slides 3](#slide-3), [5](#slide-5), [8](#slide-8),
[10](#slide-10), [11](#slide-11), [12](#slide-12),
[15](#slide-15), [20](#slide-20)).

The deck labels white-paper/publication work and additional data domains as
deliverables or future work; those statements do not establish completion or
individual contribution.

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The deck describes GAN architecture and training improvements for limited-data image generation. | documented | [Slides 5](#slide-5), [8](#slide-8), [10](#slide-10). |
| FID values are reported for multiple GAN configurations. | documented | [Slide 11](#slide-11). |
| GAN methods are applied to tire-joint defects, IRIS2 modalities, and tire-health images. | documented | [Slides 12](#slide-12), [15](#slide-15), [20](#slide-20). |
| A paper or white paper is complete or personally authored by a particular individual. | unknown | The deck labels deliverables as in progress and does not assign individual roles. |
| Generated-image quality is established by the source record. | unknown | Embedded result images and plots were not visually inspected. |

## Slide references

### Slide 2

Summarizes GAN competency development, white-paper and publication work, code
sharing, community activity, and business applications. Several items are
labeled as in progress.

### Slide 3

Maps data synthesis across image, tabular, text, time-series, and 3D domains;
lists compute, efficient training, research, and image-generation methods.

### Slide 5

Summarizes StyleGAN/UNET/StyleGAN2, differential augmentation, exponential
weight averaging, loss functions, regularization, and intended improvements.

### Slide 6

Describes StyleGAN, UNET-GAN, and label-based conditional generation as
architectural approaches for style/content control and image details.

### Slide 8

Explains differential augmentation and exponential weight averaging as
training improvements for limited-data settings.

### Slide 10

Lists WGAN-GP, hinge loss, R1 regularization, consistency regularization,
Le-Cam divergence, and perceptual-path-length regularization.

### Slide 11

Reports FID values for baseline Progressive GAN, tuned StyleGAN, and an
improved architecture. The calculations and visuals were not independently
checked.

### Slide 12

Describes GAN augmentation for tire-joint defects and lists participating
team members, without assigning specific individual responsibilities.

### Slide 15

Describes IRIS2 image modalities and multi-GPU training for higher-resolution
generated images.

### Slide 17

Describes sharing code through a Michelin GitLab project, sharing know-how
through a white paper, and building expert-community and business
applications. These are presented as activities or plans, not individual
contributions verified by this source record.

### Slide 20

Labels a tire-health image-generation application and lists it as work
addressing an imbalanced dataset.

### Slide 21

Lists future work on architecture, stability, multi-GPU training, compute
time, papers, an interface, and augmentation in other data domains.

### Slide 25

Surveys synthetic-data methods across image, tabular, text, time-series, and
3D domains; this is a scope overview, not evidence that each was implemented.

### Slide 29

Summarizes StyleGAN2 changes and their intended artifact-reduction and
training-speed benefits.

### Slide 30

Labels exponential moving averaging of generator weights and a sample curve.
The curve was not visually inspected.
