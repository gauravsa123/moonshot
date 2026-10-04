---
id: ddi-vru-20220221-ddi-similarity-v02-pptx
type: source
title: Similarity of road arcs for VRU risk analysis
aliases: []
related:
  - ../projects/ddi-vru-risk-and-multimodality.md
source_refs: []
---

# Similarity of road arcs for VRU risk analysis

- **Status:** needs review
- **Original path:** `raw/DDI/VRU/20220221_DDI_similarity_v02.pptx`
- **Extraction:** Slide text was extracted locally from all 29 slides. The
  archive contains 65 embedded media files that were not visually inspected;
  maps, plots, and other visual results remain unchecked.
- **Reason for review:** Text supports a high-level summary, but the extracted
  text does not capture all chart/map details. The original source was not
  modified.
- **Original format:** PowerPoint, 29 slides. No packages or external services
  were used for extraction.

## Summary

The deck explores road-arc similarity for accident-risk analysis, initially
using Portland Arity data and road-specific features. It compares K-means
clustering on encoded features with clustering on 16-dimensional
autoencoder-derived embeddings; the text reports no clear separation in the
original feature space and clearer separation in the embedding plots. SHAP and
permutation importance are used to inspect features contributing to clusters
([slides 2–9](#slide-2)).

Later material describes event-based clustering, MCA for categorical data,
autoencoder embeddings, UMAP, several clustering methods, and evaluating
clusters against event counts and severity. Utah data and identifying similar
arcs for new or sparse-history locations are part of the described extension
([slides 20](#slide-20), [22](#slide-22), [35](#slide-35)).

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The deck proposes using road-arc similarity with other information to improve risk-map prediction where accident history is sparse. | documented | [Slide 2](#slide-2). |
| The Portland POC uses road-specific features and compares feature-space and autoencoder-embedding clustering. | documented | [Slides 3–5](#slide-3). |
| SHAP and permutation importance are used to inspect cluster features. | documented | [Slides 7–9](#slide-7). |
| Later material describes MCA, autoencoder embeddings, UMAP, and event-based arc clustering for Utah data. | documented | [Slide 22](#slide-22). |
| The visual separation, cluster quality, or risk-prediction performance is independently validated. | unknown | Plots and detailed evaluation context were not visually inspected; extracted text does not establish independent validation. |

## Slide references

### Slide 2

The deck describes combining arc similarity with other inputs to improve
severity/risk-map prediction, cluster road-event hotspots, and address sparse
accident data using road features and other data sources.

### Slide 3

The Portland POC uses road-specific features and describes including event data
in similarity calculation and risk-map prediction.

### Slide 4

K-means clustering on encoded road features is shown; extracted text states
that the clusters had no clear distinction.

### Slide 5

Clustering on 16-dimensional autoencoder embeddings is described; extracted
text states that clearer cluster separation was observed.

### Slide 7

The deck describes permutation importance and SHAP for interpreting
autoencoder-derived embeddings.

### Slide 20

The slide discusses clustering events, MCA, autoencoder embeddings, UMAP,
evaluation metrics, and validation against severity values.

### Slide 22

The deck describes Utah event data, categorical-feature processing through
MCA, autoencoder embeddings, UMAP, clustering, and evaluating by event counts.

### Slide 35

The slide lists risk-class ranking and visualizing road-arc riskiness as
further work.
