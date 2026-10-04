---
id: gan-kar-tire-joint-defect-augmentation
type: project
title: GAN KAR Hackathon: Tire-Joint Defect Augmentation
short_title: GAN Hackathon
aliases:
  - GAN KAR Defects
related:
  - ../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md
  - gan-exploration-image-synthesis-and-augmentation.md
  - ../skills/deep-learning.md
  - ../skills/computer-vision.md
  - ../skills/gan-architecture-selection-and-implementation.md
  - ../skills/conditional-and-controlled-gan-image-generation.md
  - ../skills/gan-based-image-to-image-translation-and-synthetic-data-generation.md
  - ../skills/evaluation-of-generated-image-quality-and-similarity.md
  - ../skills/downstream-evaluation-of-synthetic-image-augmentation.md
  - ../skills/applied-research-for-image-augmentation-use-cases.md
  - ../skills/statistical-analysis-of-image-feature-distributions-using-pca.md
  - ../skills/dataset-curation-and-defect-label-quality-control.md
  - ../skills/pca-based-visualization-of-image-augmentation-effects.md
source_refs:
  - ../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-5
  - ../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-19
  - ../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-21
  - ../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-43
  - ../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-44
---

# GAN KAR Hackathon: Tire-Joint Defect Augmentation

## Project summary

The presentation describes GAN-based augmentation for production-line tire
joint defects, focusing on the imbalanced Gap, Overlap, and Shift categories.
It compares training separate GANs per defect with a model trained across
defect categories, generates 256x256 samples, and explores latent-vector
interpolation and style transfer to add or change defects
([experiments](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-5);
[interpolation and style transfer](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-21)).

Later slides describe separate GANs for defect and OK images, including a
variant using a corrected OK dataset. The presentation reports FID labels and
PCA plots comparing real and augmented data, but the axes, plots, images, and
reported conclusions have not been visually inspected or independently
validated ([dataset variants](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-29);
[PCA summary](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-44)).

The deck says generated images are transferred to an object-detection model
and lists team members without assigning individual roles. This KAR profile
is kept separate from the broader GAN Exploration profile, although that
profile also refers to tire-joint augmentation.

## Sources

- [GAN KAR Hackathon presentation](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md) —
  **needs review**; slide text was extracted, but embedded media, generated
  images, and PCA plots were not visually inspected.

## Know-how needed

These are user-confirmed project requirements, not claims about personal
experience, skill, or mastery.

| Skill | Review status | Rationale |
|---|---|---|
| [Deep learning](../skills/deep-learning.md) | user-confirmed | The project trains GAN models for tire-defect image generation ([training variants](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-12)). |
| [Computer vision](../skills/computer-vision.md) | user-confirmed | The generated samples are intended for a tire-defect object-detection workflow ([objective and current state](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-19)). |
| [GAN architecture selection and implementation](../skills/gan-architecture-selection-and-implementation.md) | user-confirmed | The deck compares per-defect and all-defect training strategies and labels StyleGAN-based image merging ([slides 5](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-5), [16](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-16)). |
| [Conditional and controlled GAN image generation](../skills/conditional-and-controlled-gan-image-generation.md) | user-confirmed | Latent interpolation and style transfer are explored to move between defect types and add defects to normal images ([slides 21](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-21), [22](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-22)). |
| [GAN-based image-to-image translation and synthetic-data generation](../skills/gan-based-image-to-image-translation-and-synthetic-data-generation.md) | user-confirmed | The project generates defective images to supplement imbalanced Gap, Overlap, and Shift classes ([objective](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-19)). |
| [Evaluation of generated-image quality and similarity](../skills/evaluation-of-generated-image-quality-and-similarity.md) | user-confirmed | The deck labels FID comparisons, although its extracted text does not explain the compared variants or validate the values ([slide 3](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-3)). |
| [Evaluation of synthetic-data impact on downstream computer-vision models](../skills/downstream-evaluation-of-synthetic-image-augmentation.md) | user-confirmed | Generated samples are intended for object detection, and the deck analyzes the data distribution after augmentation ([slide 19](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-19); [PCA summary](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-44)). |
| [Applied research and experiment design for manufacturing-image augmentation](../skills/applied-research-for-image-augmentation-use-cases.md) | user-confirmed | The presentation compares defect-generation strategies and different dataset variants for the production-line use case ([variants](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-24)). |
| [Statistical analysis of image-feature distributions using PCA](../skills/statistical-analysis-of-image-feature-distributions-using-pca.md) | user-confirmed | The summary describes PCA plots and explained-variance values to compare real and augmented datasets ([slides 43](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-43), [44](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-44)). |
| [Dataset curation and defect-label quality control](../skills/dataset-curation-and-defect-label-quality-control.md) | user-confirmed | The deck compares an OK dataset with a corrected variant intended to remove defective images ([slide 29](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-29)). |
| [PCA-based visualization of image-augmentation effects](../skills/pca-based-visualization-of-image-augmentation-effects.md) | user-confirmed | PCA distribution plots are used to communicate the class-distribution changes associated with augmentation ([PCA analysis](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-44)). |

## Skills shown by sources

These entries describe methods represented in the presentation, not personal
skills or proof of individual implementation.

| Skill or capability | Evidence status | Evidence |
|---|---|---|
| GAN generation for Gap, Overlap, and Shift defect classes | documented | The presentation describes per-defect and all-defect training approaches and labels generated samples ([slides 5](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-5), [12](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-12)). |
| Latent interpolation and style transfer for defect manipulation | documented | The slides describe interpolation between defects and transferring style/defect characteristics ([slides 21](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-21), [22](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-22)). |
| FID and PCA-based comparisons | documented | The deck reports FID labels and PCA/explained-variance comparisons; the calculations, plots, and conclusions are not independently verified ([slides 3](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-3), [43](../sources/gan-kar-20210310-gan-hackathon-kar-v1-pptx.md#slide-43)). |
| Individual contribution or object-detection outcome | unknown | The presentation lists team members but does not assign individual roles; it does not provide a downstream detector performance result. |

## User-reported contributions and outcomes

| Contribution or outcome | Status | Details |
|---|---|---|
| PCA-based explanation of image-augmentation effectiveness | user-reported | The user reports that GAN-based augmentation helped improve an image-classification model and that PCA distribution plots showed better separation of images within labels after augmentation. This account is not independently verified; the source plots remain unreviewed. |

## Review state

The user confirmed all eleven know-how requirements. The user also
reported personally using PCA distribution plots to explain the observed
image-classification improvement; this remains user-reported rather than
source-attributed. The source remains `needs review` because embedded media
and PCA plots have not been visually inspected.
