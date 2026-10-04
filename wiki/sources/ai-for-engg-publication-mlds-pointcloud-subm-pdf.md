---
id: ai-for-engg-publication-mlds-pointcloud-subm-pdf
type: source
title: End-to-end point cloud based generative model for multi-part engineering designs
aliases: []
related:
  - ../projects/ai-for-engg-point-cloud.md
source_refs: []
---

# End-to-end point cloud based generative model for multi-part engineering designs

- **Status:** needs review
- **Original path:** `raw/AI for Engg/Publication/mlds_pointcloud_subm.pdf`
- **Readability:** Text was extracted locally from all 7 pages. The paper's figures were not visually inspected, so figure-specific details and plotted results remain unchecked.
- **Reason for review:** The extracted text and figure captions are readable, but several diagrams and result figures carry evidence for the architecture and reported improvements that text extraction alone cannot fully verify.
- **Original format:** PDF, 7 pages. The source under `raw/` was not modified; no packages were installed and no external services were used.

## User-provided context

The user confirms this manuscript is the MLDS publication associated with the Point Cloud project. The manuscript itself does not state publication or acceptance details; its visual review remains outstanding.

## Summary

The paper describes an end-to-end point-cloud generative model for multi-part engineering designs, using PointNet-based VAEs for individual parts and a shape-VAE for their arrangement. It reports experiments with trainable structural embeddings and multi-head self-attention to improve inter-part relations, as well as comparisons of increasing, decreasing, and cyclic schedules for the VAE KL-divergence weight (β). Because actual design shapes were confidential, the reported experiments use synthetic geometric data. The paper reports reconstruction and sampling behavior on that data; it does not establish deployment on real designs or publication acceptance.

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The paper presents a PointNet-based generative model for point-cloud engineering designs with multiple constrained parts. | documented | [Page 1](#page-1). |
| The model uses separate part VAEs and a shape-VAE, and proposes structural embeddings and multi-head self-attention to capture inter-part relations. | documented | [Pages 3](#page-3) and [4](#page-4). |
| Experiments compare β schedules and describe reconstruction-versus-sampling trade-offs; the reported dataset contains 3,750 synthetic samples of roughly 3,000 points each. | documented | [Pages 4](#page-4) and [5](#page-5). |
| The manuscript reports improved inter-part coherence with structural embeddings and self-attention, while describing limitations and future work. | documented | [Pages 5](#page-5) and [6](#page-6); figure-dependent details need visual review. |
| The manuscript's author list includes Gaurav Adke. | documented | [Page 1](#page-1). This does not establish an individual role or contribution. |
| The PDF establishes that the work was published or accepted for publication. | unknown | The readable pages identify a manuscript and its authors but do not state a publication venue, acceptance, or publication details ([page 1](#page-1)). |

## Page references

### Page 1

Title, author list (including Gaurav Adke), abstract, and claimed contributions. The abstract describes a PointNet-based permutation-invariant generative model with structural embeddings, self-attention, and balancing reconstruction and generative capabilities. It states that results use synthetic data because actual design shapes are confidential.

### Page 2

Related work and methodology. The paper frames the task as learning relations among multiple parts in point-cloud data rather than imposing constraints after generation.

### Page 3

Synthetic constrained-shape setup, separate PointNet-based part VAEs, and the shape-VAE. It introduces structural embeddings as an approach to improve local and global accuracy.

### Page 4

Structural embeddings built from global shape information and a shape signature; multi-head self-attention for part encoding; and experiments varying the KL-divergence weight β.

### Page 5

The synthetic dataset is described as 3,750 samples of roughly 3,000 points each. The paper discusses baseline shape-VAE results, structural-embedding results, self-attention results, and β-annealing trade-offs.

### Page 6

Conclusions report improvements from structural embeddings and multi-head self-attention on the synthetic experiments and suggest future work with other generative architectures and PointNet++.

### Page 7

References.
