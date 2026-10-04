---
id: gan-api-hackathon-20211116-api-hackathon-v002-pptx
type: source
title: GAN API Hackathon presentation
aliases: []
related:
  - ../projects/gan-api-hackathon-image-preprocessing-service.md
source_refs: []
---

# GAN API Hackathon presentation

- **Status:** needs review
- **Original path:** `raw/GAN/API Hackathon/20211116_API_hackathon_v002.pptx`
- **Extraction:** Slide text was extracted locally from all 11 slides. The
  archive contains 34 embedded media files that were not rendered or visually
  inspected; diagrams and demo examples remain unchecked.
- **Reason for review:** Text supports a summary of the proposal, but the
  uninspected media may contain visual results or implementation details not
  present in extracted text. The source was not modified.
- **Original format:** PowerPoint, 11 slides. No packages or external services
  were used for extraction.

## Summary

The deck proposes an API-based suite of image-preprocessing methods intended
to improve inputs for computer-vision models, particularly dark, blurry, or
noisy images. It describes lighting enhancement, deblurring, denoising,
style/domain transfer, and GAN-based image generation for augmentation
([slides 2–5](#slide-2)).

The presentation names several approaches, including LLNet, LIME, Deep
Retinex, EnlightenGAN, Blur2Sharp, RIDNet, Fast Style Transfer, and StyleGAN-2.
It proposes API management and usage policies and claims potential accuracy
and productivity gains. The extracted text does not establish those claims
independently or confirm production deployment ([slides 3–7](#slide-3)).

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The presentation identifies poor-lighting, blur, and noise as image-preprocessing challenges. | documented | [Slide 2](#slide-2). |
| The proposed suite includes image enhancement, deblurring, denoising, style/domain transfer, and image generation. | documented | [Slides 4–5](#slide-4). |
| The deck names example deep-learning models and image-transformation approaches. | documented | [Slides 3–4](#slide-3). |
| API usage policies include access types, frequency limits, and model recency. | documented | [Slide 7](#slide-7). |
| The API service was deployed or achieved independently validated performance gains. | unknown | The presentation describes a proposal/demo and claims value, but extracted text does not establish production use or independent validation ([slides 5–6](#slide-5)). |
| Individual team-member roles or implementation contributions are established. | unknown | The title slide lists names but does not assign individual responsibilities ([slide 1](#slide-1)). |

## Slide references

### Slide 1

Title slide: “Image Preprocessing with State Of Art Models — API Hackathon.”
It lists team members, including Gaurav Adke, without assigning individual
roles.

### Slide 2

The motivation describes low-light, blurry, and noisy image inputs and states
that preprocessing can affect computer-vision model performance.

### Slide 3

The deck discusses evolving state-of-the-art low-light enhancement approaches,
names LLNet, LIME, Deep Retinex, and EnlightenGAN, and proposes adapting
research to internal use cases through an API-management layer.

### Slide 4

The API suite lists light enhancement, blur-to-sharp processing, denoising,
style/domain transfer, GAN generation, and image generation for augmentation.
Named approaches include EnlightenGAN, Blur2Sharp, RIDNet, Fast Style Transfer,
and StyleGAN-2.

### Slide 5

The slide proposes an API for deep-learning-based image preprocessing and
shows image input, processing, and output at a high level.

### Slide 6

The slide claims increased training/test accuracy and up to 80% data-scientist
productivity gain, and mentions a possible new revenue stream. The figures are
not independently validated in the extracted text.

### Slide 7

The deck proposes open/secured access, usage-frequency limits, and
recency-based service/model policies.

### Slides 9–10

The presentation labels demo and sample EnlightenGAN examples. Their visual
content was not inspected.
