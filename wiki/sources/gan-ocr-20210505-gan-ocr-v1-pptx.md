---
id: gan-ocr-20210505-gan-ocr-v1-pptx
type: source
title: GAN OCR presentation
aliases: []
related:
  - ../projects/gan-ocr-text-image-generation-and-preprocessing.md
source_refs: []
---

# GAN OCR presentation

- **Status:** needs review
- **Original path:** `raw/GAN/OCR/20210505_GAN_ocr_V1.pptx`
- **Extraction:** Text was extracted locally from all 14 slides. The archive
  contains 57 embedded media files that were not rendered or visually
  inspected.
- **Reason for review:** Generated text images and enhancement examples may
  contain evidence not represented in extracted text. Character fidelity and
  enhancement results require visual or downstream OCR review.
- **Original format:** PowerPoint, 14 slides. No packages or external
  services were used for extraction.

## Summary

The presentation covers GAN generation and enhancement for OCR images. It
labels CycleGAN and conditional StyleGAN results, text-patch domain
adaptation, and separate horizontal/vertical generated-image dimensions.
It reports that overall image content was captured but exact characters were
not, and identifies a specialized GAN/OCR loss as a needed improvement
([approaches](#slide-5), [text patches](#slide-7),
[generation uses](#slide-10), [limitation](#slide-11),
[loss direction](#slide-12)).

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The deck describes GAN-generated OCR text images and domain adaptation. | documented | [Slides 5](#slide-5), [7](#slide-7). |
| It separates horizontal and vertical text-image samples. | documented | [Slide 10](#slide-10). |
| Generated image content is reported to resemble the source while exact letters remain inaccurate. | documented | [Slide 11](#slide-11). |
| A specialized OCR loss is proposed or required, rather than established as implemented. | documented | [Slide 12](#slide-12). |
| The generated images improve OCR recognition accuracy. | unknown | The extracted text does not report a downstream OCR metric; visuals remain uninspected. |
| Image-enhancement methods and their effectiveness are established. | unknown | Slides label enhancement, but text extraction does not describe methods or measured impact. |

## Slide references

### Slide 1

Title slide: “GAN: OCR.”

### Slide 2

Lists 3,788 images and gives Catalog (1,967) and Actual (1,821) counts. The
deck does not explain the distinction.

### Slide 5

Labels CycleGAN results. The generated images were not visually inspected.

### Slide 6

Labels conditional StyleGAN results. The generated images were not visually
inspected.

### Slide 7

Labels domain adaptation using text-patch images as input.

### Slide 9

Also labels domain adaptation for text-patch images; the slide's visual
details were not inspected.

### Slide 10

Describes separate horizontal and vertical generated text-image sizes
(96x400 and 384x96) and lists image enhancement as preprocessing for better
character recognition.

### Slide 11

Reports that overall content appears in generated images but exact letters
are not matched; states a specialized loss is required for letters and
numbers. Images were not inspected.

### Slide 12

Links to TextBoxGAN and labels a network using OCR loss together with GAN
loss. The slide does not establish that this loss was implemented in the
project.

### Slide 13

Labels OCR image preprocessing enhancement. The method and result were not
described in extracted text.

### Slide 14

Also labels OCR image enhancement; visual details were not inspected.
