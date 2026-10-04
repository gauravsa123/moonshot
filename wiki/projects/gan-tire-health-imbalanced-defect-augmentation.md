---
id: gan-tire-health-imbalanced-defect-augmentation
type: project
title: GAN Tire Health: Imbalanced Aircraft-Tire Defect Augmentation
aliases:
  - GAN in Tire Health
related:
  - ../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md
  - ../projects/gan-exploration-image-synthesis-and-augmentation.md
  - ../skills/deep-learning.md
  - ../skills/computer-vision.md
  - ../skills/gan-architecture-selection-and-implementation.md
  - ../skills/gan-training-stability-loss-regularization-and-hyperparameter-optimization.md
  - ../skills/gan-based-image-to-image-translation-and-synthetic-data-generation.md
  - ../skills/dataset-curation-and-defect-label-quality-control.md
  - ../skills/similarity-metrics.md
  - ../skills/evaluation-of-generated-image-quality-and-similarity.md
  - ../skills/downstream-evaluation-of-synthetic-image-augmentation.md
  - ../skills/transfer-learning-for-gan-image-generation.md
  - ../skills/conditional-and-controlled-gan-image-generation.md
  - ../skills/applied-research-for-image-augmentation-use-cases.md
  - ../skills/translating-research-into-end-to-end-reusable-pipelines.md
  - ../skills/feature-embedding-filtering-for-generated-image-diversity.md
  - ../skills/product-minded-design-of-end-to-end-ai-pipelines.md
  - ../skills/class-imbalance-mitigation-for-image-classification.md
source_refs:
  - ../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-2
  - ../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-5
  - ../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-8
  - ../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-17
---

# GAN Tire Health: Imbalanced Aircraft-Tire Defect Augmentation

## Project summary

The presentation describes using GAN-generated images to augment minority
classes in an imbalanced aircraft-tire worn-defect dataset. It covers
class-specific GAN generation, VGG-feature/cosine-similarity filtering of
near-duplicate generated samples, and downstream classification experiments
using EfficientNetB1. It compares UNET GAN and StyleGAN image characteristics,
latent/style merging, and an Azure ML training/retraining and image-generation
pipeline ([overview](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-2);
[unique-image extraction](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-5);
[pipeline](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-17)).

The results are variant-specific and mixed: several threshold-based
augmentation variants do not improve on the 0.82 baseline, while later
class-wise and merged-image variants report validation accuracies up to 0.91.
The deck also labels some results as in progress. These are presentation-
reported results, not independently reproduced
([results](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-8);
[class-wise and merged variants](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-15)).

## Sources

- [GAN in Tire Health presentation](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md) —
  **needs review**; text was extracted from all 27 slides, but 83 embedded
  media items and result visuals were not visually inspected.

## Know-how needed

These are user-confirmed project requirements, not claims about personal
experience, skill, contribution, or mastery.

| Skill | Review status | Rationale |
|---|---|---|
| [Deep learning](../skills/deep-learning.md) | user-confirmed | The deck covers GAN models and an EfficientNetB1 downstream classifier ([classifier setup](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-7)). |
| [Computer vision](../skills/computer-vision.md) | user-confirmed | The task is patch-based visual classification of worn aircraft-tire defects ([task overview](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-2); [image patches](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-3)). |
| [GAN architecture selection and implementation](../skills/gan-architecture-selection-and-implementation.md) | user-confirmed | The deck compares per-defect models, UNET GAN, StyleGAN, and grouped-class approaches ([generation variants](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-4); [model comparison](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-10)). |
| [GAN training stability, loss/regularization choices, and hyperparameter optimization](../skills/gan-training-stability-loss-regularization-and-hyperparameter-optimization.md) | user-confirmed | The deck discusses mode collapse, limited variation, and non-convergence when training on combined classes ([unique images](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-5); [combined-class training](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-21)). |
| [GAN-based image-to-image translation and synthetic-data generation](../skills/gan-based-image-to-image-translation-and-synthetic-data-generation.md) | user-confirmed | GAN-generated examples are used to augment defect classes with relatively few real samples ([generation counts](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-4); [augmentation results](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-8)). |
| [Dataset curation and defect-label quality control](../skills/dataset-curation-and-defect-label-quality-control.md) | user-confirmed | The work tracks class-wise real-image counts and selects generated examples for augmentation ([class counts](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-4); [subjective image-quality selection](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-9)). |
| [Similarity metrics](../skills/similarity-metrics.md) | user-confirmed | Near-duplicate filtering uses pretrained VGG feature embeddings and cosine similarity with a selected threshold ([unique-image extraction](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-5)). |
| [Evaluation of generated-image quality and similarity](../skills/evaluation-of-generated-image-quality-and-similarity.md) | user-confirmed | The deck compares image quality and variation between UNET GAN and StyleGAN and records subjective quality selection ([model comparison](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-10); [image-quality review](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-9)). |
| [Evaluation of synthetic-data impact on downstream computer-vision models](../skills/downstream-evaluation-of-synthetic-image-augmentation.md) | user-confirmed | Validation accuracy and per-class accuracy are compared across real-only, GAN-augmented, and merged-image variants ([results](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-8); [merged-image results](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-15)). |
| [Transfer learning and fine-tuning for GAN image generation](../skills/transfer-learning-for-gan-image-generation.md) | user-confirmed | The pipeline slides describe retraining GANs using previously trained weights ([retraining pipeline](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-17); [transfer learning](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-27)). |
| [Conditional and controlled GAN image generation](../skills/conditional-and-controlled-gan-image-generation.md) | user-confirmed | The presentation explores latent-vector interpolation and style merging to create combined images ([image merging](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-13); [style merging](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-14)). |
| [Applied research for image-augmentation use cases](../skills/applied-research-for-image-augmentation-use-cases.md) | user-confirmed | Multiple augmentation thresholds, selected image-quality subsets, and class-specific combinations are compared experimentally ([experiments](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-8); [class-wise experiments](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-12)). |
| [Translating research into end-to-end reusable pipelines](../skills/translating-research-into-end-to-end-reusable-pipelines.md) | user-confirmed | The deck describes Azure ML workflows for training, retraining, generating images, and extracting unique samples ([pipeline](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-17)). |
| [Feature-embedding filtering for generated-image diversity](../skills/feature-embedding-filtering-for-generated-image-diversity.md) | user-confirmed | The user added innovative use of image embeddings to identify distinct generated images; the source describes VGG features and similarity filtering ([unique-image extraction](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-5)). |
| [Product-minded design of end-to-end AI pipelines](../skills/product-minded-design-of-end-to-end-ai-pipelines.md) | user-confirmed | The user added product mindset in creating an end-to-end GAN pipeline; the source describes a low-code training/retraining and generation workflow ([pipeline](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-17)). |
| [Class-imbalance mitigation for image classification](../skills/class-imbalance-mitigation-for-image-classification.md) | user-confirmed | The user added tackling data imbalance; the deck describes class weighting and targeted augmentation for underrepresented defect classes ([classifier setup](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-7); [class-wise experiments](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-12)). |

## Skills shown by sources

These entries describe methods represented in the deck, not an individual's
personal skill or project contribution.

| Capability | Evidence status | Evidence |
|---|---|---|
| The presentation describes GAN augmentation for minority aircraft-tire defect classes and class-wise classifier evaluation. | documented | [Overview](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-2); [classifier results](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-10). |
| The deck describes VGG feature embeddings and cosine-similarity filtering to retain unique generated images. | documented | [Unique-image extraction](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-5). |
| The deck reports mixed downstream results: some uniqueness-threshold variants are below or equal to the 0.82 baseline, while later class-wise and merged-image variants report up to 0.91. | documented | [Threshold results](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-8); [class-wise results](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-15). The visual tables and values have not been checked. |
| The deck describes a low-code Azure ML workflow with custom training/generation parameters and a possible REST API path. | documented | [Pipeline](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-17); [custom parameters and API option](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-18). Product mindset is not directly stated. |
| Product-oriented design is evident in the way the configurable workflow is presented for reuse. | inferred | [Pipeline](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-17); [custom parameters and API option](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-18). This does not establish an individual's mindset or a deployed service. |
| An Azure ML training/retraining and image-generation pipeline is described; REST API publication is framed as a possible next step, not a verified deployment. | documented | [Pipeline](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-17); [REST API next step](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-18). |
| The title slide lists “Gaurav A, DCSI”; the individual's specific role and contribution are not established. | documented | [Title slide](../sources/gan-tire-health-20211118-gan-tire-health-v1-ai-review-pptx.md#slide-1). |

## User-reported contributions and outcomes

No personal contributions or outcomes have been user-reported for this
project.

## Review state

All 27 slide texts were extracted and 25 speaker-note files were checked; no
substantive note text was found. The 83 embedded media items and result visuals remain unreviewed. Reported
classifier scores and subjective image-quality claims have not been
independently validated. The user confirmed 16 know-how requirements: the 13
proposed items and three additions covering feature-embedding filtering,
product-minded pipeline design, and class-imbalance mitigation. These remain
project requirements, not claims of personal mastery.
