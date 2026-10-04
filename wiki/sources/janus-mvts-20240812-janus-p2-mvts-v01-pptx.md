---
id: janus-mvts-20240812-janus-p2-mvts-v01-pptx
type: source
title: Janus Transformers for multivariate time series
aliases: []
related:
  - ../projects/janus-mvts-transformer-predictive-modeling.md
source_refs: []
---

# Janus Transformers for multivariate time series

- **Status:** needs review
- **Original path:** `raw/Janus/MVTS/20240812_Janus_p2_MVTS_V01.pptx`
- **Extraction:** Text was extracted from all 34 slides. The file contains 79
  embedded media items and 30 speaker-note files; three notes repeat a
  description of the masking pattern.
- **Reason for review:** Charts, attribution plots, and embedding visualizations
  remain uninspected. The deck contains multiple datasets and workstreams, and
  reported regression results have not been independently reproduced.
- **Original format:** PowerPoint. The source under `raw/` was not modified.

## Summary

The presentation covers multivariate time-series Transformers for
representation learning and regression, including masked-value reconstruction,
unsupervised pretraining, semi-supervised/multitask learning, and feature
attribution. It reports a Beijing PM2.5 regression test R² of 0.76 and
describes a proposed Janus rubber-mix quality model based on sensor sequences
with limited quality labels. Separate sections cover Gaussian Mixture
Regression on an obfuscated tabular dataset. The source gives several
experiment values, but plots and table layout remain unreviewed and results
were not reproduced.

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| A Transformer encoder is used for multivariate time-series regression and representation learning. | documented | [Architecture](#slide-30); [regression results](#slide-26). |
| Masked-value reconstruction is proposed as unsupervised pretraining, with geometric/Markov masking and loss on masked values. | documented | [Pretraining design](#slide-18); [masking details](#slide-31). |
| A multitask approach combines imputation and regression for limited labels. | documented | [Pretraining and multitask notes](#slide-20); [proposed Janus model](#slide-25). |
| The deck reports a Beijing PM2.5 test R² of 0.76. | documented | [Results](#slide-26) and [slide 32](#slide-32); metrics were not independently reproduced. |
| Explainability methods and feature-attribution examples are included. | documented | [Methods](#slide-13); [Integrated Gradients](#slide-14); [DeepLIFT](#slide-15). |
| Gaussian Mixture Regression is explored on obfuscated tabular data. | documented | [GMR method](#slide-10); [GMR exploration](#slide-28). |
| The Beijing PM2.5 results establish performance on Janus rubber-mix quality prediction. | unknown | The presentation discusses these as distinct data contexts; no transfer result is reported. |
| The approaches have been deployed or independently validated. | unknown | The deck labels some work as in progress and gives no deployment or independent reproduction evidence. |

## Slide references

### Slide 1

Title: “Janus – Transformers (MVTS).” The slide lists Gaurav Adke and DAI
Squad, DOTI; it does not state an individual role.

### Slide 2

Labels a regression study for the Beijing PM2.5 quality dataset.

### Slide 3

“MVTS Reconstruction + Regression” with sparse additional extracted text.

### Slide 4

Shows a Ray Tune trial for Beijing PM2.5 regression with batch size 16,
`d_model` 128, learning rate 0.00023, and six layers.

### Slide 5

Shows average loss per sample across an epoch and 300 total epochs; the curve
was not visually inspected.

### Slide 6

Shows hyperparameter tuning by validation loss for the same listed trial.

### Slide 7

Shows another loss curve for the selected settings; visual details remain
unreviewed.

### Slide 8

“Thank You.”

### Slide 9

Introduces Gaussian Mixture Regression (GMR) and GMM clustering on a
dataset with categorical columns.

### Slide 10

Describes selecting a Gaussian count with AIC/BIC, fitting by expectation
maximization, and predicting conditional outputs from input features.

### Slide 11

Shows a five-Gaussian result for Janus dataset W with categorical columns.

### Slide 12

Lists GMR, GLLiM, and locally linear embedding implementation references.

### Slide 13

Lists Integrated Gradients, DeepLIFT, Noise Tunnel, Feature Ablation, and
Captum for feature attribution, including individual and batch analysis.

### Slide 14

Describes Integrated Gradients attribution over a 24-hour Beijing PM2.5
sequence, with positive and negative feature attributions.

### Slide 15

Compares DeepLIFT attributions for the same sequence; the deck notes that one
feature is less prominent than in the Integrated Gradients result.

### Slide 16

Lists transformer interpretability and layer-attribution references.

### Slide 17

“Backup.”

### Slide 18

Describes unsupervised pretraining from masked time-series values, using a
geometric distribution and Markov process for mask spans and MSE on masked
positions.

### Slide 19

Shows sparse text for unsupervised input reconstruction; the figure remains
unreviewed.

### Slide 20

Describes semi-supervised pretraining with frozen Transformer layers,
regression heads, and multitask imputation/regression. It lists R² values and
work-in-progress notes.

### Slide 21

States that embeddings appear more separated when regression is added to
imputation; the t-SNE visual was not inspected.

### Slide 22

Compares experiment configurations and reports several R²/loss values. Table
formatting and plots were not visually reviewed, so individual entries may
need confirmation.

### Slide 23

Lists open questions about learned representations, masking, embedding plots,
and comparisons with classical approaches such as ARIMA and Holt-Winters.

### Slide 24

Contains sparse text (“janus”).

### Slide 25

Describes a proposed Janus model to predict rubber-mix quality from process
sensor curves, notes limited quality readings, and labels a semi-supervised
approach as work in progress.

### Slide 26

Reports Beijing PM2.5 test R² of 0.76 and hyperparameter tuning with Ray Tune;
learning-rate scheduling is marked in progress.

### Slide 27

Repeats explainability methods and Integrated Gradients attribution for
Beijing PM2.5 data.

### Slide 28

Describes initial GMR experiments on obfuscated dataset W, with possible
future integration into time-series data.

### Slide 29

Summarizes a 2020 IBM Research paper on multivariate time-series
representation learning and lists its code repository.

### Slide 30

Describes adapting a Transformer encoder for supervised time-series learning,
including a regression head, linear input projection, learnable positional
embeddings, and batch normalization.

### Slide 31

Explains masked-time-series pretraining, geometric/Markov mask spans, loss on
masked elements, and suitability for limited-label datasets.

### Slide 32

Repeats the Beijing PM2.5 test R² of 0.76 and Ray Tune result summary.

### Slide 33

Proposes multitask imputation and regression, reports unsupervised fine-tuned
R² 0.70 versus multitask R² 0.76, and marks the approach as work in progress.

### Slide 34

Combines input and layer attribution discussion, naming Integrated Gradients,
DeepLIFT, Noise Tunnel, Feature Ablation, Captum, and attention-score work in
progress.
