---
id: gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx
type: source
title: GAN in Tire Health presentation
aliases: []
related:
  - ../projects/gan-tire-health-imbalanced-defect-augmentation.md
source_refs: []
---

# GAN in Tire Health presentation

- **Status:** needs review
- **Original path:** `raw/GAN/Tire Health/20211118_GAN_tire-health_V1_AI-review.pptx`
- **Extraction:** Text was extracted from all 27 slides using local
  PowerPoint Open XML parsing. The file contains 83 embedded media items and
  25 speaker-note files; notes contain no substantive text.
- **Reason for review:** Embedded images, charts, and generated-image
  examples were not visually inspected, so visual quality and result-table
  details remain unchecked.
- **Original format:** PowerPoint. The source under `raw/` was not modified.

## Summary

The deck describes GAN image augmentation for worn-defect classification in
aircraft tires, where rare defect classes have few real examples. It covers
class-specific GAN generation, VGG-feature/cosine-similarity filtering for
unique generated images, UNET GAN and StyleGAN variants, image merging, and
EfficientNetB1 classifier experiments. It also outlines Azure ML training and
retraining pipelines.

Reported validation-accuracy results vary by experiment: early
similarity-threshold variants are below or equal to the real-only baseline,
whereas later class-wise and merged-image variants report improvements. The
deck says improvement work was still in progress on one slide. Figures and
values have not been independently reviewed or reproduced.

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The deck frames the task as identifying worn-out aircraft-tire defects and using GAN augmentation to address class imbalance. | documented | [Slide 2](#slide-2). |
| It describes feature-embedding and cosine-similarity filtering to remove near-duplicate GAN images. | documented | [Slide 5](#slide-5). |
| It reports real-only and augmentation-variant classifier accuracies, including mixed results across variants. | documented | [Slides 8](#slide-8), [9](#slide-9), [12](#slide-12), and [15](#slide-15). Figures and values have not been visually checked. |
| An Azure ML training/retraining workflow is described; publishing it for REST API use is conditional/future wording. | documented | [Slides 17](#slide-17) and [18](#slide-18). |
| The title slide lists “Gaurav A, DCSI.” | documented | [Slide 1](#slide-1). This does not establish a specific role or contribution. |
| The image-quality improvements, score comparisons, or API deployment are independently verified. | unknown | Media and figures were not inspected; the deck describes the API path as a possible next step. |

## Slide references

### Slide 1

Title “GAN in Tire Health” and the text “Gaurav A, DCSI.”

### Slide 2

Frames an image-classification task to identify worn-out defects in aircraft
tires. It calls the dataset highly imbalanced and proposes GAN augmentation
to generate classes with fewer real examples.

### Slide 3

Shows original defect samples and extracted 256 × 256 patches for classifier
training. The sample images have not been visually inspected.

### Slide 4

Lists defect categories and real-image counts and describes training separate
GAN models for defect classes. It notes generated images were initially
considered for augmentation and that the displayed generated samples were not
used for classification training.

### Slide 5

Describes generating 500 samples per class, extracting pretrained VGG
features, computing cosine similarity, and keeping images below a selected
similarity threshold to reduce duplicates and mode-collapse effects.

### Slide 6

Compares counts of unique images for similarity cutoffs. The table layout and
values require visual inspection.

### Slide 7

Describes an Azure ML classifier workflow using EfficientNetB1, 16 output
classes, a 10% validation split, standard image augmentations, and class
weights for imbalance.

### Slide 8

Reports a real-only baseline accuracy of 0.82 and values of 0.76, 0.80, 0.82,
and 0.65 for variants using 80%, 85%, 90%, and 95% unique GAN images,
respectively. The text says GAN images were not improving results in these
experiments and describes the 90% uniqueness setting as beneficial.

### Slide 9

Describes subjective selection of generated images from five classes based
on feedback from named reviewers. It reports 0.78 and 0.75 for two
image-quality-selected augmentation variants against a 0.82 baseline.

### Slide 10

Lists baseline class-wise accuracies and identifies worse-classified
categories. It reports 0.83 for a UNET/StyleGAN augmentation variant and
characterizes UNET GAN samples as higher quality but less varied, while
StyleGAN samples have higher variation. The supporting visuals and table
remain unreviewed.

### Slide 11

Notes that some poorly classified defect categories appear similar and raises
possible class unification as an observation, not a completed change.

### Slide 12

Reports a class-wise experiment adding generated images for P22 and P24, with
a listed validation accuracy of 0.90.

### Slide 13

Introduces latent-vector interpolation for image merging.

### Slide 14

Describes style merging by passing different noise vectors at different
generator resolutions.

### Slide 15

Reports merged/interpolated images for poorly classified classes and a 0.91
accuracy for one variant; values and images remain unverified.

### Slide 16

Summarizes the deck's interpretation that augmentation and merging may help
under limited-data conditions, that similar classes may warrant
investigation, and that VGG-based unique-image extraction can reduce
near-duplicates. These are source claims, not independently validated
conclusions.

### Slide 17

Outlines Azure ML low-code training and retraining workflows, generation, and
unique-image extraction.

### Slide 18

Describes accessing generated images and weights and rerunning a pipeline with
custom parameters. The deck says a completed pipeline can be published for
REST API use; no deployed API is established.

### Slide 20

Labels initial generated-image results and says improvements are in progress.

### Slide 21

The deck says a GAN trained on all defect classes together does not converge
and proposes grouping classes using VGG feature embeddings.

### Slide 22

Shows clustered-image experiments; the visuals have not been inspected.

### Slide 23

Describes two GAN models trained for one cluster and marks a labeled-GAN
experiment as work in progress.

### Slides 24–25

Show combined-class image and style-merging experiments; visuals have not
been inspected.

### Slide 26

Lists four clusters of medium-count defect classes and describes GAN training
on grouped images. The displayed cluster relationships require visual review.

### Slide 27

Describes retraining a UNET-StyleGAN model using pretrained weights and
generating new images with unique-image extraction.
