---
id: gan-kar-20210310-gan-hackathon-kar-v1-pptx
type: source
title: GAN KAR Hackathon presentation
aliases: []
related:
  - ../projects/gan-kar-tire-joint-defect-augmentation.md
source_refs: []
---

# GAN KAR Hackathon presentation

- **Status:** needs review
- **Original path:** `raw/GAN/KAR/20210310_GAN_Hackathon-KAR_V1.pptx`
- **Extraction:** Text was extracted locally from all 44 slides. The archive
  contains 223 embedded media files that were not rendered or visually
  inspected.
- **Reason for review:** Generated images, FID/PCA plots, and image-merging
  examples carry evidence that cannot be checked from extracted text alone.
  Reported values and conclusions have not been independently reproduced.
- **Original format:** PowerPoint, 44 slides. No packages or external
  services were used for extraction.

## Summary

The deck describes GAN augmentation for tire-joint Gap, Overlap, and Shift
defects, comparing training strategies, defect-to-defect interpolation,
style merging, and variants with OK images. It labels FID and PCA-based
comparisons and says generated images are intended for downstream object
detection ([training variants](#slide-5), [application](#slide-19),
[interpolation](#slide-21), [PCA summary](#slide-44)).

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| GAN augmentation is aimed at an imbalanced tire-joint defect dataset. | documented | [Slide 19](#slide-19). |
| The deck compares training GANs by defect and across defect categories. | documented | [Slides 5](#slide-5), [12](#slide-12). |
| Latent interpolation and style transfer are used to create or transform defect images. | documented | [Slides 21](#slide-21), [22](#slide-22). |
| FID and PCA results demonstrate a particular quality or generalization improvement. | unknown | The source labels results and states conclusions, but plots and calculations have not been reviewed. |
| Individual contributions or downstream object-detection performance are established. | unknown | Team members are listed without role assignments; detector performance is not reported in extracted text. |

## Slide references

### Slide 1

Title slide: “GAN: KAR Defects.”

### Slide 3

Lists two FID values, 163 and 146.9, under labels “FID – 100.” The slide text
does not explain the comparison; the numbers are not independently validated.

### Slide 4

Labels StyleGAN and combined-model outputs. Visuals were not inspected.

### Slide 5

Describes an experiment with individual GAN models for Gap, Shift, and
Overlap, and gives round-one image counts and a 256x256 generated-image size.

### Slide 12

Describes a GAN model trained across all defects using round-one and
round-two images.

### Slide 14

Labels interpolation between Gap, Overlap, and Shift defect categories.
Examples were not visually inspected.

### Slide 16

Labels style-merging images with input and target images. Visuals were not
inspected.

### Slide 19

Frames the application as augmentation of production-line tire-joint defect
images to reduce imbalance and says generated images are transferred to an
object-detection model. It does not report detector performance.

### Slide 21

Describes latent-vector interpolation to create defects and labels
transitions between defect categories.

### Slide 22

Describes a style-transfer GAN that combines content from an input image with
style/defect characteristics from a target image.

### Slide 24

Lists per-defect and OK-image GAN training as next steps and compares using
all images with using a corrected OK dataset.

### Slide 29

Lists the corrected OK dataset variant and class counts. The deck does not
describe the correction/quality-control procedure in detail.

### Slide 33

Lists training separate GANs for each defect and OK images.

### Slide 42

Summarizes direct defective-image generation and normal-to-defective image
generation as two augmentation approaches.

### Slide 43

Labels PCA plots and lists explained-variance values for real and augmented
data. Plot interpretation was not independently checked.

### Slide 44

States that PCA visualizations show improved distinction between defect
categories after augmentation. This conclusion is source-reported; the plot
and analysis were not visually inspected.
