---
id: gan-publication-gan-paper-formatted-2-pdf
type: source
title: Application of GAN for Reducing Data Imbalance under Limited Dataset
aliases: []
related:
  - ../projects/gan-publication-advanced-gan-for-tire-defect-augmentation.md
source_refs: []
---

# Application of GAN for Reducing Data Imbalance under Limited Dataset

- **Status:** needs review
- **Original path:** `raw/GAN/Publication/GAN_paper_formatted_2.pdf`
- **Readability:** Text was extracted locally from all nine pages.
- **Reason for review:** Figures and PCA plots were not visually inspected;
  reported FID/classification results have not been independently reproduced.
- **Original format:** PDF, nine pages. The source under `raw/` was not
  modified.

## Paper overview

The paper presents an advanced GAN for augmenting a limited, imbalanced
tire-joint nonconformity dataset. Its abstract says the approach combines
architectural and training improvements, reports better FID than StyleGAN,
and claims a 12% improvement in downstream classification accuracy. The
paper's figures and metrics are not independently validated here.

The title page lists Gaurav Adke as the author and Michelin India Private
Limited as the affiliation. The source does not assign individual
implementation responsibilities or state publication acceptance details.

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The paper proposes an advanced StyleGAN-based model for image augmentation of tire-joint nonconformity classes. | documented | [Abstract and introduction](#paper-overview); [methodology](#methodology). |
| The described method uses a U-Net discriminator, differentiable augmentation, WGAN-GP with a consistency term, and EMA generator weights. | documented | [Methodology](#methodology). |
| The paper reports lower FID values for its Advanced GAN than StyleGAN across three nonconformity classes. | documented | [FID comparisons](#fid-comparisons); values are reported by the paper and not independently checked. |
| The paper reports classification-accuracy comparisons using real-only and GAN-augmented datasets, plus PCA analyses of class distributions. | documented | [Experiments and results](#experiments-and-results). |
| The abstract claims a 12% classification-accuracy improvement; Table 3 lists 0.85 for the Stage 2 real dataset and 0.97 for Stage 2 real plus all generated images, a difference of 0.12. | documented | [Abstract](#paper-overview); [classification results](#classification-augmentation-results). The paper does not explicitly say this pair is the basis of its 12% claim. |
| Gaurav Adke is listed as the paper's author. | documented | [Authorship and publication status](#authorship-and-publication-status). This does not establish specific individual contributions. |
| The paper was accepted or published, or establishes who implemented each method. | unknown | The extracted text gives no venue or acceptance status and does not assign individual technical roles ([authorship and publication status](#authorship-and-publication-status)). |

## Related work

The paper surveys GAN applications in image augmentation and discusses prior
work on StyleGAN, training stability, regularization, and augmentation for
limited-data settings. Its account is a literature review in the manuscript,
not an independent assessment of the cited studies.

## Methodology

### Architecture

The work is based on StyleGAN. The paper describes extending it with a U-Net
discriminator intended to give global and pixel-level feedback while leaving
the generator unchanged. See the paper's methodology discussion and its
architecture figures; the figures have not been visually inspected.

### Data augmentation

The paper discusses differentiable transformations applied to both real and
generated images during GAN training. It compares three data-generation
approaches: an individual GAN per defect, a single model for defective images,
and separate models for each defect plus normal images. It also lists
single-noise generation, style merging, and latent interpolation.

### Loss and training stability

The described loss uses WGAN-GP with an additional consistency term. The paper
also attributes smoother training and lower FID to exponential moving
averaging of generator weights. These descriptions document what the paper
proposes; they do not independently establish code-level implementation.

## Experiments and results

### Dataset and protocol

The paper says data were collected in two stages: 1,183 samples in Stage 1,
then 1,108 additional samples, for 2,291 in total. It describes a real-image
test set held out at 10%, with the remaining 90% used for training and
validation. Classification values are reported as averages across multiple
classifier models. These figures are source-reported, not reproduced.

### FID comparisons

The paper reports the following FID values for StyleGAN versus its Advanced
GAN:

| Architecture | NC 1 | NC 2 | NC 3 |
|---|---:|---:|---:|
| StyleGAN | 165.6 | 162.0 | 161.1 |
| Advanced GAN | 96.3 | 93.8 | 95.7 |

The paper interprets lower FID as improved generated-image quality and
variation. The image figures and metric calculations have not been reviewed.

### Classification augmentation results

Table 3 reports these classification accuracies:

| Dataset setup | Reported accuracy |
|---|---:|
| Stage 1 real dataset | 0.73 |
| Stage 1 GAN-generated-image augmentation | 0.79 |
| Stage 2 real dataset | 0.85 |
| Stage 2 real plus Stage 1 GAN-generated images | 0.89 |
| Stage 2 real plus Stage 2 GAN-generated-image augmentation | 0.92 |
| Stage 2 real plus all generated-image augmentation | 0.97 |

The comparisons span different dataset stages and augmentation setups; they
should not be read as a single controlled before/after comparison. The
abstract's 12% claim may correspond to the 0.85-to-0.97 difference, but the
paper does not explicitly identify that calculation.

### PCA analysis

The text says the paper plots the top two principal components for real-only
and GAN-augmented image datasets and claims improved distinction among
conforming and nonconforming categories after augmentation. Figures 4 and 5
were not visually inspected, so the graphical evidence and interpretation
remain unreviewed.

## Limitations and future work

The conclusion states that experiments were limited to 256 × 256 images due
to compute and processing-time constraints. It says effectiveness on larger
datasets remains to be studied and proposes future work with StyleGAN2 and
class-wise augmentation for categories with lower recall.

## Authorship and publication status

The title page lists Gaurav Adke as author and Michelin India Private Limited
as affiliation. Acknowledgements thank dataset and review contributors. The
paper does not specify individual technical responsibilities, a publication
venue, or acceptance status; none is inferred from the formatted filename or
author line.
