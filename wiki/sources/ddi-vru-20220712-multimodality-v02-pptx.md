---
id: ddi-vru-20220712-multimodality-v02-pptx
type: source
title: Multimodality exploration for VRU risk analysis
aliases: []
related:
  - ../projects/ddi-vru-risk-and-multimodality.md
source_refs: []
---

# Multimodality exploration for VRU risk analysis

- **Status:** needs review
- **Original path:** `raw/DDI/VRU/20220712_multimodality_v02.pptx`
- **Extraction:** Slide text was extracted locally from all 47 slides. The
  archive contains 119 embedded media files that were not visually inspected;
  maps, cluster plots, and comparisons remain unchecked.
- **Reason for review:** Several claims depend on plotted cluster structure,
  maps, thresholds, and visual results not captured by text extraction.
- **Original format:** PowerPoint, 47 slides. No packages or external services
  were used for extraction.

## Summary

The deck explores clustering accident-related road arcs by user type and
context. Features include accident types, POI distances, road attributes,
weather, time, and other contextual variables. It describes separate
pedestrian-, cyclist-, vehicle-, and mixed-feature groupings and interprets
clusters using feature importance and relative frequencies ([slides 4–12](#slide-4),
[23](#slide-23)).

The presentation reports that POI-distance features diluted VRU-specific
patterns and that their impact remained under investigation. Later slides
discuss similarity thresholds, DBSCAN outliers, and possible model extensions,
including time-series deep-learning approaches; these future directions are
not treated as completed work ([slides 15](#slide-15), [30](#slide-30),
[38–41](#slide-38)).

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The deck describes clustering road arcs using POI and other contextual features, with separate user-type feature groupings. | documented | [Slides 4–9](#slide-4), [23](#slide-23). |
| Cluster interpretation uses descriptive counts, relative frequencies, and model-based feature importance. | documented | [Slides 9–12](#slide-9), [20–24](#slide-20). |
| POI-distance features improved separation of VRU-specific and non-VRU arcs. | unknown | The deck instead states that POI-distance information diluted VRU-specific features and that further investigation was in progress ([slide 15](#slide-15)). |
| DBSCAN outlier analysis and deep time-series models are both completed project deliverables. | unknown | DBSCAN results are presented, while LSTM/1D convolution models appear as proposed future exploration ([slides 39–41](#slide-39)). |

## Slide references

### Slide 4

The slide presents accident-type plots with county-level comparisons.

### Slide 7

The multimodality pipeline lists accident/POI data, deep clustering, MCA,
autoencoding, UMAP, feature interpretation, mapping, and similarity evaluation.

### Slide 9

The deck describes cluster interpretation using VRU presence, variable counts,
relative frequencies, and model-based important features.

### Slide 11

The slide explains using relative frequencies to distinguish unusually common
or uncommon variables in a cluster from features with high overall counts.

### Slide 13

The slide presents candidate VRU-specific arcs from Tampa as possible
hotspots; map details were not visually inspected.

### Slide 15

The slide reports that POI-distance information diluted VRU-specific features
and labels further analysis as work in progress.

### Slide 20

The slide proposes studying cluster-wise variable counts and using descriptive
analysis to infer patterns.

### Slide 23

The pipeline includes accident and POI data, deep clustering, relative
frequency analysis, map visualization, similar-arc evaluation, and event counts.

### Slide 29

The slide outlines data collection, POI extraction, map matching, clustering,
cluster interpretation, similar-arc search, event aggregation, and mapping.

### Slide 30

The slide lists GPS, weather, and time information and proposes ranking arcs
and exploring counterfactual explanations or causal methods.

### Slide 38

The slide lists further clustering/feature-analysis work, DBSCAN outlier
identification, and counterfactual explanations.

### Slide 39

The slide lists deep-learning models for time, POI, weather, GPS, and satellite
imagery data as future exploration, including LSTM and 1D convolutions.

### Slide 40

The slide surveys outlier/anomaly detection methods including autoencoders,
KNN, isolation forests, IQR, Z scores, one-class SVM, DBSCAN, and local outlier
factor.

### Slide 41

The slide presents DBSCAN results for pedestrian arcs and states that
deep-clustering and DBSCAN results can be complementary. Visual plots were not
inspected.
