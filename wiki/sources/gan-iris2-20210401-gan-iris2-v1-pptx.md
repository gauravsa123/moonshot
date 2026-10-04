---
id: gan-iris2-20210401-gan-iris2-v1-pptx
type: source
title: GAN IRIS2 presentation
aliases: []
related:
  - ../projects/gan-iris2-multimodal-tire-imaging.md
source_refs: []
---

# GAN IRIS2 presentation

- **Status:** needs review
- **Original path:** `raw/GAN/IRIS2/20210401_GAN_IRIS2_V1.pptx`
- **Extraction:** Text was extracted locally from all 31 slides. The archive
  contains 161 embedded media files that were not rendered or visually
  inspected.
- **Reason for review:** Generated-image examples and architecture/result
  diagrams may contain details missing from text extraction; reported visual
  improvements have not been checked.
- **Original format:** PowerPoint, 31 slides. No packages or external
  services were used for extraction.

## Summary

The deck describes GAN image generation for IRIS2 tire data across Elevation,
Intensity, and four lighting modalities. It reports experiments with
training duration, transfer learning, UNET discriminators, EMA, WGAN-GP, and
increased output resolution. High-resolution approaches include two-GPU
processing and modifications to channel sizes and batch sizes
([dataset and modalities](#slide-8); [training refinements](#slide-24);
[resolution approaches](#slide-28)).

The slide text reports 10,840 images across the named modalities and lists
30,772 images as a future training target, without explaining the
relationship. Result images and plots remain uninspected.

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The project considers six IRIS2 image modalities and gives per-modality data counts. | documented | [Slide 8](#slide-8). |
| The deck describes GAN training and architecture experiments to improve image detail. | documented | [Slides 15](#slide-15), [16](#slide-16), [24](#slide-24). |
| The deck describes multi-GPU approaches for higher-resolution generation. | documented | [Slide 28](#slide-28). |
| The numerical counts and generated-image quality are independently verified. | unknown | The source figures and data artifacts were not inspected; the stated image totals are not reconciled in slide text. |
| Individual contributions are established by the deck. | unknown | The deck does not assign specific responsibilities to individuals. |

## Slide references

### Slide 1

Title slide: “GAN: IRIS2.”

### Slide 3

Describes an initial study using 1,007 images, 512x512 resized real images,
and 256x256 generated images. It says the model captures overall image
distribution but needs longer training to capture fine details; higher
resolution is listed as a next step.

### Slide 4

Labels generated samples. The images were not visually inspected.

### Slide 5

Labels interpolation results. The images were not visually inspected.

### Slide 8

Lists per-modality counts for Elevation, Intensity, and Light1–Light4, a
10,840 total, and 30,772 images as a future training target. It also lists
higher resolution and image-format exploration; the two dataset totals are
not reconciled in the slide text.

### Slide 15

Labels architecture modifications intended to capture finer details.

### Slide 16

Compares longer and shorter runs for Elevation and labels longer-run outputs
as capturing finer details. The images were not visually inspected.

### Slide 17

Labels longer-run training and transfer learning for Intensity. The images
were not visually inspected.

### Slide 18

Describes a memory issue, channel configuration, and reducing batch size for
256-size training.

### Slide 19

Labels UNET and StyleGAN architecture comparisons and identifies successive
Elevation training runs.

### Slide 20

Labels an exponential moving average of generator weights in an Elevation
experiment.

### Slide 21

Describes WGAN-GP loss and two approaches to calculating the gradient penalty.

### Slide 22

Labels baseline real and generated Elevation images. The images were not
visually inspected.

### Slide 23

Compares longer training and increased channel size as image-detail
improvements. The images were not visually inspected.

### Slide 24

Describes a UNET discriminator and exponential moving average of generator
weights as architecture/training modifications.

### Slide 25

Labels generated Elevation images using UNET and UNET with EMA. The images
were not visually inspected.

### Slide 26

Labels generated outputs for Intensity and Light1–Light4 using a UNET
discriminator. The images were not visually inspected.

### Slide 27

Mentions Atrous Spatial Pyramid Pooling (ASPP), decoder upsampling
convolutions, and TIFF images.

### Slide 28

Describes two high-resolution training approaches: batch-parallel processing
across two GPUs and modified layer channels with batch-size tuning. It reports
training to 512x512 and 1024x1024, with fine-detail improvement still needed.

### Slide 29

Labels an Elevation approach using two GPUs at 512x512. Visual output was not
inspected.

### Slide 30

Labels a Light1 approach using two GPUs at 512x512. Visual output was not
inspected.

### Slide 31

Labels an Elevation approach using modified layer channels at 1024x1024.
Visual output was not inspected.
