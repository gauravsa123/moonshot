---
id: gan-exploration-20200717-gan-study-v3-pptx
type: source
title: GAN study V3 presentation
aliases: []
related:
  - ../projects/gan-exploration-image-synthesis-and-augmentation.md
source_refs: []
---

# GAN study V3 presentation

- **Status:** needs review
- **Original path:** `raw/GAN/Exploration/20200717_GAN_study_V3.pptx`
- **Extraction:** Text was extracted locally from all 89 slides. The archive
  contains 331 embedded media files that were not rendered or visually
  inspected.
- **Reason for review:** Generated-image examples, plots, and diagrams may
  contain details missing from text extraction. The deck includes repeated
  material and dated sections later than its filename; no single presentation
  date is inferred from the filename.
- **Original format:** PowerPoint, 89 slides. No packages or external services
  were used for extraction.

## Summary

The deck moves from GAN-based defect-image generation and tire-conicity
experiments to Progressive GAN, mode-collapse mitigation, differential
augmentation, and StyleGAN. It also describes a YOLOv3 experiment comparing
real, generated, and mixed conicity images, with reported mAP measurements and
planned follow-up experiments ([slides 2](#slide-2), [17](#slide-17),
[31](#slide-31), [50](#slide-50), [56](#slide-56), [58](#slide-58)).

The deck reports particular training settings, cloud-platform observations,
and FID results; these are reported claims, not independently reproduced
results. Embedded images and plots remain uninspected.

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| GAN augmentation is proposed for synthetic surface-defect examples and data imbalance. | documented | [Slide 2](#slide-2). |
| Progressive GAN and Wasserstein loss with gradient penalty are presented as approaches to image quality and mode-collapse challenges. | documented | [Slide 17](#slide-17). |
| Differential augmentation and FID comparisons are reported for the tire-conicity experiments. | documented | [Slides 31](#slide-31), [34](#slide-34). |
| A YOLOv3 object-detection experiment compared dataset variants containing real and generated samples. | documented | [Slides 50](#slide-50), [53](#slide-53), [56](#slide-56). |
| The reported model scores or generated-image visuals are independently validated by this source record. | unknown | The figures and reported experimental values have not been independently reviewed. |

## Slide references

### Slide 2

Proposes generative models for steel-surface defect image generation and
automated labels to augment a training dataset.

### Slide 13

Describes Progressive GAN and image-size growth from 4x4 through 256x256 in
the tire-conicity experiments.

### Slide 17

Labels mode collapse and lists feature matching, minibatch discrimination,
equalized learning rate, instance noise, and Wasserstein gradient penalty
among approaches under exploration.

### Slide 24

Shows latent-vector variations described as changes to color, texture, zoom,
and added tire/column features. The images were not visually inspected.

### Slide 31

Describes differential augmentation as useful for limited training data and
for reducing discriminator overfitting.

### Slide 34

Reports FID comparisons for Progressive GAN training with and without
differential augmentation. The values are deck-reported and were not
independently reproduced.

### Slide 50

Describes a YOLOv3 experiment on conicity-line object detection, including
single- and double-line classes and a held-out test set.

### Slide 53

Lists the annotation and training workflow, including Kili labeling,
conversion to Pascal VOC format, and model evaluation.

### Slide 55

Explains mean Average Precision and the role of precision-recall curves and
IoU thresholds in the reported evaluation.

### Slide 56

Reports mAP results for five real/generated dataset variants. The highest
listed mAP is 96.5715 for the variant combining real images with selected
generated images; the result was not independently reproduced.

### Slide 57

Lists observations about real and generated image performance, quality
selection, and image resizing. These are deck claims and have not been
independently verified.

### Slide 58

Lists next experiments for varying the real/fake image ratio and generated
image quality.

### Slide 60

Summarizes StyleGAN as a progression from Progressive GAN and describes
quality, interpolation, and latent-factor disentanglement as intended benefits.

### Slide 63

Lists training-step, channel, latent-size, batch-size, and learning-rate
choices and compares WGAN-GP and BCE training observations.

### Slide 64

Reports different observed training behavior on TensorFlow versions and cloud
platforms; the cause is listed for further investigation.

### Slide 70

Labels an IMLE GAN/few-shot learning topic as work in progress.
