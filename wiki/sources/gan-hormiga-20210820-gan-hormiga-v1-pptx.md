---
id: gan-hormiga-20210820-gan-hormiga-v1-pptx
type: source
title: GAN Hormiga presentation
aliases: []
related:
  - ../projects/gan-hormiga-road-image-generation-and-enhancement.md
source_refs: []
---

# GAN Hormiga presentation

- **Status:** needs review
- **Original path:** `raw/GAN/hormiga/20210820_GAN_hormiga_V1.pptx`
- **Extraction:** Text was extracted from all eight slides using local
  PowerPoint Open XML parsing. The file contains 48 embedded media items and
  seven speaker-note files; no substantive speaker-note text was found.
- **Reason for review:** Generated-image examples and enhancement results
  were not visually inspected; the deck gives little context for the
  “Hormiga” project name or its downstream objective.
- **Original format:** PowerPoint. The source under `raw/` was not modified.

## Summary

The deck compares direct GAN image generation with CycleGAN-style road-texture
transfer and image enhancement. It says direct GAN output is limited to
256 × 256 pixels relative to 1920 × 1080 input images, losing small stone
details, and requires separate labels. CycleGAN is proposed to change road
texture, wetness, and shadow without separate labels. Pretrained seasonal
CycleGAN and Enlighten examples are shown; Retinex is another enhancement
approach. No quantitative evaluation or downstream task is specified in the
extracted text.

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The deck compares direct GAN generation with CycleGAN-style texture transfer and states different labeling implications. | documented | [Slide 2](#slide-2); [slide 4](#slide-4). |
| The deck identifies a 1920 × 1080 input / 256 × 256 output limitation and says fine stones are not captured. | documented | [Slide 2](#slide-2); supporting images were not inspected. |
| Pretrained seasonal CycleGANs and Retinex/Enlighten enhancement approaches are presented. | documented | [Slides 5](#slide-5), [6](#slide-6), and [7](#slide-7). |
| “Hormiga” denotes a specific downstream task, and the approaches improve that task. | unknown | The deck does not define the name or report downstream metrics. |

## Slide references

### Slide 1

Title slide: “GAN: Hormiga.” It does not define the project name or list an
individual role.

### Slide 2

Describes direct GAN training over images and notes that generated images
would need separate labeling. It records original images at 1920 × 1080 and
GAN output at 256 × 256, with small stones and fine details not captured.

### Slide 3

Labels GAN-generated results and gives the output size as 256 × 256. The
images were not visually inspected.

### Slide 4

Proposes CycleGAN as a style/texture-transfer approach, naming changes in
road texture, wetness, and shadow. It says separate labeling is not needed
for this approach.

### Slide 5

Shows a pretrained CycleGAN model for summer-to-winter transfer. The visual
result was not inspected.

### Slide 6

Shows a pretrained CycleGAN model for winter-to-summer transfer. The visual
result was not inspected.

### Slide 7

Lists real images alongside Retinex and Enlighten image-enhancement outputs.
The examples were not visually inspected.

### Slide 8

Identifies Enlighten as a pretrained model that could be customized for the
dataset. The slide does not report a completed customization or quantitative
result.
