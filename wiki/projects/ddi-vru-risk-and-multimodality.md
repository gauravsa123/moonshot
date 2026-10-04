---
id: ddi-vru-risk-and-multimodality
type: project
title: DDI Safer Roads: VRU Risk and Multimodality
aliases:
  - DDI VRU
related:
  - ../sources/ddi-vru-20220221-ddi-similarity-v02-pptx.md
  - ../sources/ddi-vru-20220323-ddi-severity-v03-pptx.md
  - ../sources/ddi-vru-20220712-multimodality-v02-pptx.md
  - ../sources/ddi-vru-ddi-mulitmodality-summary-3105-pptx.md
  - ../skills/road-safety-analytics-and-vru-risk-assessment.md
  - ../skills/geospatial-road-network-analysis-road-arcs-and-map-matching.md
  - ../skills/multimodal-data-integration-and-feature-engineering.md
  - ../skills/unsupervised-and-deep-clustering-of-mixed-categorical-data.md
  - ../skills/road-segment-similarity-search-and-risk-ranking.md
  - ../skills/accident-risk-severity-modeling-and-evaluation.md
  - ../skills/model-and-cluster-interpretability.md
  - ../skills/spatial-temporal-hotspot-analysis-and-risk-mapping.md
  - ../skills/outlier-anomaly-detection-for-road-segment-clusters.md
  - ../skills/causal-inference-and-counterfactual-explanations.md
source_refs:
  - ../sources/ddi-vru-20220221-ddi-similarity-v02-pptx.md#slide-2
  - ../sources/ddi-vru-20220221-ddi-similarity-v02-pptx.md#slide-22
  - ../sources/ddi-vru-20220323-ddi-severity-v03-pptx.md#slide-2
  - ../sources/ddi-vru-20220712-multimodality-v02-pptx.md#slide-7
  - ../sources/ddi-vru-20220712-multimodality-v02-pptx.md#slide-15
  - ../sources/ddi-vru-20220712-multimodality-v02-pptx.md#slide-38
  - ../sources/ddi-vru-ddi-mulitmodality-summary-3105-pptx.md#slide-3
  - ../sources/ddi-vru-ddi-mulitmodality-summary-3105-pptx.md#slide-8
---

# DDI Safer Roads: VRU Risk and Multimodality

## Project summary

The four presentations describe an effort to identify and characterize road
segments that may pose higher risk to vulnerable road users (VRUs), including
pedestrians and cyclists. They frame this as a systemic, network-wide risk
problem: use road characteristics and other contextual evidence to assess
locations even when prior crashes are sparse or absent ([summary slides 3–5](../sources/ddi-vru-ddi-mulitmodality-summary-3105-pptx.md#slide-3),
[arc-similarity slide 2](../sources/ddi-vru-20220221-ddi-similarity-v02-pptx.md#slide-2)).

The described data and approaches include accident/event records, road-network
features, points of interest (POIs), GPS/time, weather, and satellite imagery;
categorical-feature analysis, autoencoder-based embeddings, MCA, UMAP,
clustering, feature importance, and road-arc similarity. The decks describe
pedestrian-, cyclist-, vehicle-, and mixed-arc groupings, with cluster
interpretation and map visualization as outputs ([multimodality pipeline](../sources/ddi-vru-20220712-multimodality-v02-pptx.md#slide-7),
[summary pipeline](../sources/ddi-vru-ddi-mulitmodality-summary-3105-pptx.md#slide-7)).

The results are exploratory and include explicit limitations: POI-distance
features were reported to dilute VRU-specific cluster separation, and several
slides label further work as in progress or future scope. Planned causal and
counterfactual analyses and proposed time-series deep-learning models are not
treated as completed deliverables ([multimodality slides 15](../sources/ddi-vru-20220712-multimodality-v02-pptx.md#slide-15),
[30](../sources/ddi-vru-20220712-multimodality-v02-pptx.md#slide-30),
[38–39](../sources/ddi-vru-20220712-multimodality-v02-pptx.md#slide-38)).

## Sources

- [Similarity of road arcs for VRU risk analysis](../sources/ddi-vru-20220221-ddi-similarity-v02-pptx.md) — **needs review**; text extracted from 29 slides; embedded media not visually inspected.
- [Arc severity risk map](../sources/ddi-vru-20220323-ddi-severity-v03-pptx.md) — **needs review**; text extracted from 3 slides; embedded media not visually inspected.
- [Multimodality exploration for VRU risk analysis](../sources/ddi-vru-20220712-multimodality-v02-pptx.md) — **needs review**; text extracted from 47 slides; embedded media not visually inspected.
- [DDI Safer Roads multimodality summary](../sources/ddi-vru-ddi-mulitmodality-summary-3105-pptx.md) — **needs review**; text extracted from 35 slides; embedded media not visually inspected.

## Know-how needed

These are user-confirmed project requirements, not claims about personal
experience, skill, or mastery.

| Skill | Review status | Rationale |
|---|---|---|
| [Road-safety analytics and vulnerable-road-user risk assessment](../skills/road-safety-analytics-and-vru-risk-assessment.md) | user-confirmed | The project frames a systemic risk approach for pedestrian/cyclist safety, including risk where crash history is sparse ([summary slides 3–5](../sources/ddi-vru-ddi-mulitmodality-summary-3105-pptx.md#slide-3)). |
| [Geospatial road-network analysis, road-arc representation, and map matching](../skills/geospatial-road-network-analysis-road-arcs-and-map-matching.md) | user-confirmed | The analyses represent road segments as arcs, extract POIs, map-match, compare regions/counties, and visualize clusters on maps ([summary slide 7](../sources/ddi-vru-ddi-mulitmodality-summary-3105-pptx.md#slide-7); [exploration slide 29](../sources/ddi-vru-20220712-multimodality-v02-pptx.md#slide-29)). |
| [Multimodal data integration and feature engineering](../skills/multimodal-data-integration-and-feature-engineering.md) | user-confirmed | The work combines accident/event data with road features, POIs, GPS, time, weather, and satellite imagery ([summary slides 6–8](../sources/ddi-vru-ddi-mulitmodality-summary-3105-pptx.md#slide-6)). |
| [Unsupervised and deep clustering of mixed/categorical data](../skills/unsupervised-and-deep-clustering-of-mixed-categorical-data.md) | user-confirmed | The presentations use or explore MCA, autoencoder embeddings, UMAP, K-means, GMM, hierarchical clustering, and DBSCAN ([arc-similarity slides 4–5](../sources/ddi-vru-20220221-ddi-similarity-v02-pptx.md#slide-4); [multimodality slides 23](../sources/ddi-vru-20220712-multimodality-v02-pptx.md#slide-23), [38](../sources/ddi-vru-20220712-multimodality-v02-pptx.md#slide-38)). |
| [Road-segment similarity search and risk ranking](../skills/road-segment-similarity-search-and-risk-ranking.md) | user-confirmed | The project compares arcs to identify similar locations and discusses ranking and threshold selection for output counts ([arc-similarity slides 2–3](../sources/ddi-vru-20220221-ddi-similarity-v02-pptx.md#slide-2); [multimodality slides 30–35](../sources/ddi-vru-20220712-multimodality-v02-pptx.md#slide-30)). |
| [Accident-risk and severity modeling with evaluation](../skills/accident-risk-severity-modeling-and-evaluation.md) | user-confirmed | A severity deck defines region/time accident labels and severity sums; other material discusses validating clusters against severity and comparing evaluation scores ([severity slide 2](../sources/ddi-vru-20220323-ddi-severity-v03-pptx.md#slide-2); [similarity slide 20](../sources/ddi-vru-20220221-ddi-similarity-v02-pptx.md#slide-20)). |
| [Model and cluster interpretability](../skills/model-and-cluster-interpretability.md) | user-confirmed | The decks use SHAP, permutation importance, cluster-wise counts, and relative-frequency methods to characterize groups ([similarity slides 7–9](../sources/ddi-vru-20220221-ddi-similarity-v02-pptx.md#slide-7); [multimodality slides 9–12](../sources/ddi-vru-20220712-multimodality-v02-pptx.md#slide-9)). |
| [Spatial-temporal hotspot analysis and risk-map visualization](../skills/spatial-temporal-hotspot-analysis-and-risk-mapping.md) | user-confirmed | The work discusses regional/hourly accident labels, county-level comparisons, event counts, and map-based candidate hotspots ([severity slide 2](../sources/ddi-vru-20220323-ddi-severity-v03-pptx.md#slide-2); [multimodality slides 13–18](../sources/ddi-vru-20220712-multimodality-v02-pptx.md#slide-13)). |
| [Outlier and anomaly detection for road-segment clusters](../skills/outlier-anomaly-detection-for-road-segment-clusters.md) | user-confirmed | Later slides apply DBSCAN to identify outliers in pedestrian, cyclist, and vehicle arc clusters ([multimodality slides 40–47](../sources/ddi-vru-20220712-multimodality-v02-pptx.md#slide-40)). |
| [Causal inference and counterfactual explanations](../skills/causal-inference-and-counterfactual-explanations.md) | user-confirmed | These appear as future exploration for explaining cluster patterns and VRU predictions, not established deliverables ([multimodality slides 30](../sources/ddi-vru-20220712-multimodality-v02-pptx.md#slide-30), [38](../sources/ddi-vru-20220712-multimodality-v02-pptx.md#slide-38)). |

## Skills shown by sources

These entries describe methods and approaches in the presentations, not
personal skills or proof of an individual's implementation.

| Skill or capability | Evidence status | Evidence |
|---|---|---|
| Arc clustering and learned embedding analysis | documented | The similarity deck compares K-means on original features with autoencoder embeddings and later describes MCA/AE/UMAP clustering ([similarity slides 4–5](../sources/ddi-vru-20220221-ddi-similarity-v02-pptx.md#slide-4), [22](../sources/ddi-vru-20220221-ddi-similarity-v02-pptx.md#slide-22)). |
| Feature and cluster interpretation | documented | SHAP, permutation importance, cluster-wise counts, and relative frequencies are described as interpretation methods ([similarity slides 7–9](../sources/ddi-vru-20220221-ddi-similarity-v02-pptx.md#slide-7); [multimodality slides 9–12](../sources/ddi-vru-20220712-multimodality-v02-pptx.md#slide-9)). |
| VRU-oriented road-arc grouping and similarity | documented | The multimodality workflow describes VRU-specific clustering and comparison with other arcs to identify similar locations ([multimodality slides 7](../sources/ddi-vru-20220712-multimodality-v02-pptx.md#slide-7), [23](../sources/ddi-vru-20220712-multimodality-v02-pptx.md#slide-23)). |
| POI-distance features reliably separate VRU and non-VRU accidents | unknown | The source reports that POI-distance information diluted VRU-specific features and that its effect remained under investigation ([multimodality slide 15](../sources/ddi-vru-20220712-multimodality-v02-pptx.md#slide-15)). |
| Individual contribution, role, or mastery | unknown | The presentation content does not establish individual roles or personal mastery. |

## User-reported contributions and outcomes

No personal contributions or outcomes have been user-reported for this project.

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The project frames VRU risk assessment as a network-wide problem, including road segments without prior crashes. | documented | [Summary slides 3–5](../sources/ddi-vru-ddi-mulitmodality-summary-3105-pptx.md#slide-3). |
| The presentations combine road, accident, event, POI, and other contextual data in clustering and similarity workflows. | documented | [Summary slides 6–8](../sources/ddi-vru-ddi-mulitmodality-summary-3105-pptx.md#slide-6); [multimodality slide 23](../sources/ddi-vru-20220712-multimodality-v02-pptx.md#slide-23). |
| A risk-map formulation uses region/hour GPS density as input, binary accident labels, and summed accident severity. | documented | [Severity slide 2](../sources/ddi-vru-20220323-ddi-severity-v03-pptx.md#slide-2). |
| POI distance improves separation of VRU-specific and non-VRU clusters. | unknown | The deck reports that POI distance diluted VRU-specific features and marks further analysis as work in progress ([multimodality slide 15](../sources/ddi-vru-20220712-multimodality-v02-pptx.md#slide-15)). |
| The proposed causal/counterfactual and deep time-series models are completed deliverables. | unknown | They are listed as future or exploratory directions ([multimodality slides 30](../sources/ddi-vru-20220712-multimodality-v02-pptx.md#slide-30), [38–39](../sources/ddi-vru-20220712-multimodality-v02-pptx.md#slide-38)). |

## Review state

All ten know-how requirements are `user-confirmed`; this records project
needs, not personal experience or mastery. All four sources remain `needs
review` because embedded media was not visually inspected. Roadmap items,
current analyses, and limitations are distinguished; no personal role or
mastery is inferred.
