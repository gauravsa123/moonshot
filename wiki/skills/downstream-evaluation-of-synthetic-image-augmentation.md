---
id: downstream-evaluation-of-synthetic-image-augmentation
type: skill
title: Evaluation of synthetic-data impact on downstream computer-vision models
aliases: []
related:
  - evaluation-of-generated-image-quality-and-similarity.md
  - computer-vision-object-detection-and-vehicle-classification.md
source_refs:
  - ../sources/gan-publication-gan-paper-formatted-2-pdf.md#classification-augmentation-results
  - ../sources/gan-exploration-20200717-gan-study-v3-pptx.md#slide-53
  - ../sources/gan-exploration-20200717-gan-study-v3-pptx.md#slide-56
  - ../sources/gan-exploration-ai-moonshot-gan-09122021-pptx.md#slide-8
  - ../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-44
  - ../sources/gan-ocr-20210505-gan-ocr-v1-pptx.md#slide-10
  - ../sources/gan-ocr-20210505-gan-ocr-v1-pptx.md#slide-11
---

# Evaluation of synthetic-data impact on downstream computer-vision models

Design and interpret experiments that compare downstream vision-model
performance with real, generated, and mixed training data.

## Projects needing this skill

- [GAN Publication: Advanced GAN for Tire-Defect Augmentation](../projects/gan-publication-advanced-gan-for-tire-defect-augmentation.md) — user-confirmed project requirement.
- [GAN Exploration, Image Synthesis, and Data Augmentation](../projects/gan-exploration-image-synthesis-and-augmentation.md) — user-confirmed project requirement.
- [GAN KAR Hackathon: Tire-Joint Defect Augmentation](../projects/gan-kar-tire-joint-defect-augmentation.md) — user-confirmed project requirement.
- [GAN for OCR Text-Image Generation and Preprocessing](../projects/gan-ocr-text-image-generation-and-preprocessing.md) — user-confirmed project requirement.

## Projects with user-reported use

- None recorded.

## Projects showing this skill

- [GAN Publication: Advanced GAN for Tire-Defect Augmentation](../projects/gan-publication-advanced-gan-for-tire-defect-augmentation.md) — the paper reports classifier-accuracy comparisons for real-only and GAN-augmented datasets; metrics have not been reproduced ([classification results](../sources/gan-publication-gan-paper-formatted-2-pdf.md#classification-augmentation-results)).
- [GAN Exploration, Image Synthesis, and Data Augmentation](../projects/gan-exploration-image-synthesis-and-augmentation.md) — the decks report conicity object-detection and tire-joint classification comparisons across real/generated dataset variants; the metrics are not independently reproduced ([object-detection results](../sources/gan-exploration-20200717-gan-study-v3-pptx.md#slide-56); [tire-joint experiments](../sources/gan-exploration-ai-moonshot-gan-09122021-pptx.md#slide-8)).
- [GAN KAR Hackathon: Tire-Joint Defect Augmentation](../projects/gan-kar-tire-joint-defect-augmentation.md) — the deck describes using generated images for an object-detection task and reports PCA-based distribution comparisons, but provides no detector score in extracted text ([application](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-19); [PCA summary](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-44)).
- [GAN for OCR Text-Image Generation and Preprocessing](../projects/gan-ocr-text-image-generation-and-preprocessing.md) — the deck frames enhancement as intended to improve character recognition but reports no downstream OCR score ([slide 10](../sources/gan-ocr-20210505-gan-ocr-v1-pptx.md#slide-10)).
