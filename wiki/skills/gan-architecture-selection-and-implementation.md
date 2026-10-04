---
id: gan-architecture-selection-and-implementation
type: skill
title: GAN architecture selection and implementation
aliases: []
related:
  - gan-based-image-to-image-translation-and-synthetic-data-generation.md
source_refs:
  - ../sources/gan-hormiga-20210820-gan-hormiga-v1-pptx.md#slide-2
  - ../sources/gan-hormiga-20210820-gan-hormiga-v1-pptx.md#slide-4
  - ../sources/gan-publication-gan-paper-formatted-2-pdf.md#architecture
  - ../sources/gan-exploration-gan-overview-v01-docx.md#gan-implementation-on-open-dataset
  - ../sources/gan-exploration-ai-moonshot-gan-01072021-pptx.md#slide-6
  - ../sources/gan-exploration-20200717-gan-study-v5-pptx.md#slide-9
  - ../sources/gan-exploration-20200925-gan-overview-pdf.md#page-9
  - ../sources/gan-iris2-20210401-gan-iris2-v1-pptx.md#slide-19
  - ../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-12
  - ../sources/gan-ocr-20210505-gan-ocr-v1-pptx.md#slide-6
---

# GAN architecture selection and implementation

Select, adapt, and implement GAN architectures for a target image-generation
task, accounting for conditioning, data, output quality, and compute needs.

## Projects needing this skill

- [GAN Hormiga: Road-Image Generation and Enhancement](../projects/gan-hormiga-road-image-generation-and-enhancement.md) — user-confirmed project requirement.
- [GAN Publication: Advanced GAN for Tire-Defect Augmentation](../projects/gan-publication-advanced-gan-for-tire-defect-augmentation.md) — user-confirmed project requirement.
- [GAN Exploration, Image Synthesis, and Data Augmentation](../projects/gan-exploration-image-synthesis-and-augmentation.md) — user-confirmed project requirement.
- [GAN for IRIS2 Multimodal Tire Imaging](../projects/gan-iris2-multimodal-tire-imaging.md) — user-confirmed project requirement.
- [GAN KAR Hackathon: Tire-Joint Defect Augmentation](../projects/gan-kar-tire-joint-defect-augmentation.md) — user-confirmed project requirement.
- [GAN for OCR Text-Image Generation and Preprocessing](../projects/gan-ocr-text-image-generation-and-preprocessing.md) — user-confirmed project requirement.

## Projects with user-reported use

- None recorded.

## Projects showing this skill

- [GAN Hormiga: Road-Image Generation and Enhancement](../projects/gan-hormiga-road-image-generation-and-enhancement.md) — the deck contrasts direct GAN generation and a CycleGAN style-transfer approach, without establishing personal implementation responsibility ([slides 2](../sources/gan-hormiga-20210820-gan-hormiga-v1-pptx.md#slide-2), [4](../sources/gan-hormiga-20210820-gan-hormiga-v1-pptx.md#slide-4)).
- [GAN Publication: Advanced GAN for Tire-Defect Augmentation](../projects/gan-publication-advanced-gan-for-tire-defect-augmentation.md) — the paper describes a StyleGAN-based model with a U-Net discriminator; this does not establish an individual's implementation role ([architecture](../sources/gan-publication-gan-paper-formatted-2-pdf.md#architecture)).
- [GAN Exploration, Image Synthesis, and Data Augmentation](../projects/gan-exploration-image-synthesis-and-augmentation.md) — sources discuss architecture variants including progressive growth for tire-conicity images; this does not establish an individual's role ([open dataset](../sources/gan-exploration-gan-overview-v01-docx.md#gan-implementation-on-open-dataset); [V5 progressive GAN](../sources/gan-exploration-20200717-gan-study-v5-pptx.md#slide-9); [overview PDF](../sources/gan-exploration-20200925-gan-overview-pdf.md#page-9); [Moonshot variants](../sources/gan-exploration-ai-moonshot-gan-01072021-pptx.md#slide-6)).
- [GAN for IRIS2 Multimodal Tire Imaging](../projects/gan-iris2-multimodal-tire-imaging.md) — the deck labels UNET/StyleGAN and discriminator modifications for IRIS2 image generation; visual results were not inspected ([slide 19](../sources/gan-iris2-20210401-gan-iris2-v1-pptx.md#slide-19)).
- [GAN KAR Hackathon: Tire-Joint Defect Augmentation](../projects/gan-kar-tire-joint-defect-augmentation.md) — the deck compares GAN training approaches for separate and combined defect categories ([slides 5](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-5), [12](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-12)).
- [GAN for OCR Text-Image Generation and Preprocessing](../projects/gan-ocr-text-image-generation-and-preprocessing.md) — the presentation labels CycleGAN and conditional StyleGAN results for OCR text images, but does not describe all implementation details ([slides 5](../sources/gan-ocr-20210505-gan-ocr-v1-pptx.md#slide-5), [6](../sources/gan-ocr-20210505-gan-ocr-v1-pptx.md#slide-6)).
