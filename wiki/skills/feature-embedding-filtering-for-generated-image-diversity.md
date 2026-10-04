---
id: feature-embedding-filtering-for-generated-image-diversity
type: skill
title: Feature-embedding filtering for generated-image diversity
aliases:
  - VGG-feature similarity filtering for GAN samples
related:
  - similarity-metrics.md
  - gan-based-image-to-image-translation-and-synthetic-data-generation.md
  - evaluation-of-generated-image-quality-and-similarity.md
source_refs:
  - ../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-5
  - ../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-6
---

# Feature-embedding filtering for generated-image diversity

Use learned visual embeddings and pairwise similarity to identify and filter
near-duplicate generated images, preserving sample diversity when augmenting
limited datasets.

## Projects needing this skill

- [GAN Tire Health: Imbalanced Aircraft-Tire Defect Augmentation](../projects/gan-tire-health-imbalanced-defect-augmentation.md) — user-confirmed project requirement.

## Projects with user-reported use

- None recorded.

## Projects showing this skill

- [GAN Tire Health: Imbalanced Aircraft-Tire Defect Augmentation](../projects/gan-tire-health-imbalanced-defect-augmentation.md) — the presentation describes extracting pretrained VGG features, computing cosine similarity, and filtering generated samples by similarity threshold; this source does not establish an individual's role ([slide 5](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-5); [slide 6](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-6)).
