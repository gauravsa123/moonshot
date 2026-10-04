---
id: janus-vae-20220926-janus-rl-explo-vae-v08-pptx
type: source
title: Janus RL Exploration with VAE Representations (V08)
aliases: []
related:
  - ../projects/janus-vae-based-exploration-for-process-optimization.md
source_refs: []
---

# Janus RL Exploration with VAE Representations (V08)

- **Status:** needs review
- **Original path:** `raw/Janus/VAE/20220926_Janus_RL_explo-VAE_V08.pptx`
- **Extraction:** Text extracted from all 41 slides. The deck contains 82 embedded media items and three speaker-note files; the extracted notes contain only slide-number text.
- **Reason for review:** Cluster, embedding, and result plots remain visually uninspected; reported model and RL behavior has not been independently reproduced.
- **Original format:** PowerPoint presentation. The source under `raw/` was not modified.

## Summary

The September 2022 deck explores data analysis and reinforcement-learning
strategies for a Janus industrial process dataset, then presents VAE
representations of the dataset and fixed process parameters. It reports that
clusters are visible in the encoded representations, but does not specify the
VAE architecture, training configuration, quantitative clustering quality,
or a validated connection from those embeddings to an RL policy. The
presentation also discusses cluster-aware exploration, reachable quality
targets, reward design, and a possible CGAN-based exploration approach.

## Dataset preparation and feature analysis

### Slide 1

The cover reads “Janus: Reinforcement Learning” and lists Gaurav Adke and
“AI Squad, DCTI”; it does not assign individual authorship or implementation
responsibility.

### Slide 2

The deck describes a new dataset with 14,972 rows and 217 columns, including
six quality columns and 211 input columns. For records with the two selected
quality values, it reports 1,085 samples after filtering and 190 remaining
input columns after removing 21 all-zero columns. It also notes 35
low-variance input columns, identifies a block of STAM columns, and gives
limits and VAV target values. The extracted text does not establish the
downstream effect of each preprocessing choice.

### Slide 3

The presentation reports high multicollinearity among uncontrollable
parameters, including STAM parameters, and uses variance-inflation-factor
(VIF) analysis to identify candidate columns for reduction. It reports 47
columns above VIF 20 and 69 above VIF 5, and highlights near-zero-variance
columns. A suggestion to reduce collinearity among controllable columns is
framed as helpful for RL learning, not as a verified result.

### Slide 4

The deck shows descriptive analysis for the full dataset and the subset of
dropouts with quality values. Visual plots are not reviewed here.

## Clustering, prediction, and data variation

### Slide 5

The slide describes 19 groups for the new dataset, reports group counts and
outside-limit counts, and compares LR and RF. The clustering algorithm and
the meaning of every outside-limit count are not established by the
extracted text alone.

### Slide 6

UMAP and box plots are used to discuss cluster noisiness. The slide states
that less noisy clusters have lower variance than noisy clusters.

### Slide 7

The slide compares quality variation and states that less noisy clusters
show better RL-agent convergence. The plot remains uninspected, so the claim
and comparison are not independently evaluated.

### Slide 8

The slide compares a second neural-network version and repeats the stated
relationship between lower cluster noise and better RL-agent convergence.
The plot remains uninspected.

### Slide 9

The presentation reports random-forest, linear-regression, and neural-network
prediction metrics for two quality targets, discusses possible overfitting
and low-variance/collinear features, and reports samples outside the limits.
The visual table layout has not been reviewed; individual metric-to-model
assignments and the reported values are not independently verified.

### Slides 10–11

The deck presents another 19-group clustering result, VIF variants, and
quality-value variation plots. It does not identify all clustering settings
in the extracted text.

### Slide 12

DBSCAN is discussed as a way to identify noisy or outlier samples. The slide
states that large input variance prevents the clustering from fitting a few
clusters, and that changing `min_samples` to reduce cluster count creates
many outliers.

## Exploration, quality reachability, and reward design

### Slide 13

Next steps include reducing the number of dropouts used in RL training,
statistical shortlisting, real-time optimization, experiments with more
controllable variables, CGAN exploration, and further VAE work. The slide
notes a mismatch in VAE results without explaining or resolving it.

### Slides 14–15

The deck proposes using per-dropout quality percentiles to classify
hard-to-train, potentially reachable, and easier samples. It discusses the
limits of a single VAV target, cluster usability, and step rewards; the
claims are conditional on the prediction model and controllable parameters.

### Slide 16

For each dropout, controllable parameters are sampled 2,000 times and passed
through a neural-network prediction model. The presentation describes
storing two quality outputs and summary statistics (including percentiles)
for 14,972 dropouts, then plotting the resulting distributions to inspect
whether target or tolerance regions appear reachable.

### Slide 17

The slide illustrates repeated sampling of four controllable parameters for
one dropout, using a neural-network prediction model to estimate the
resulting quality distribution.

### Slide 18

The slide describes plotting statistical information from all dropout
explorations to assess whether quality values can reach target or tolerance
regions.

### Slide 19

The slide shows dropout samples outside the tolerance limits and extracted
counts, but the corresponding plot has not been reviewed.

### Slide 20

The presentation describes an RL reward with its maximum at the VAV target,
zero at the limits, and negative values outside either quality limit. It
states that both quality targets must be reachable within the explored
minimum–maximum ranges for this setup to converge.

### Slide 21

The slide presents examples where the minimum–maximum reachability condition
is met or not met, and notes that some groups lack a common target.

### Slide 22

The slide examines whether target values are accessible for all dropouts in
a cluster. It states that cluster 0 lacks a single common target and that
the same problem occurs in the other clusters; the figures remain
unreviewed.

### Slide 23

The presentation compares cluster-level quality distributions and notes
slightly better convergence for one group; the figures remain unreviewed.

### Slides 24–29

The presentation explores binning by quality means or ranges, the difficulty
of satisfying two quality targets using bins formed on only one target, and
rules for selecting samples and target values using overlaps between
distribution ranges. It reports a subset of samples that meet joint
min–max criteria, but the reported counts and results are not reproduced.

### Slide 30

The deck describes stepwise reward as a way for the RL agent to select a
target within tolerance limits. It reports that a policy may not generalize
from one dropout to others; these claims have not been independently
validated.

### Slide 31

The slide summarizes the role of target reachability in convergence,
limitations for extreme dropout groups, and a need to test more controllable
variables.

### Slide 32

The deck suggests nearest-bin lookup during inference and mentions
evolutionary algorithms as a related approach; it does not establish
deployment.

## Generative exploration and VAE representations

### Slides 33–34

The slides show UMAP representations of clusters; the plots have not been
visually reviewed.

### Slide 35

The deck proposes training a conditional GAN for a cluster and generating
samples to support exploration for a single-dropout RL model. The slide
describes a proposal, not a completed or evaluated augmentation system.

### Slides 36–37

The presentation revisits reward behavior and gives examples comparing
samples across datasets, clusters, and prediction models. The visual
comparisons remain uninspected.

### Slide 38

The slide states that a VAE is trained on the dataset after all-zero
features are removed and shows encoded points colored by cluster. Extracted
text says that clusters are visible after encoding. It does not give the
VAE architecture, latent dimension, training objective, quantitative
cluster metrics, or a comparison against a baseline.

### Slide 39

The slide shows cluster-wise VAE plots; they remain visually uninspected.

### Slide 40

The deck shows VAE encodings using only fixed parameters and identifies
feature ranges associated with raw-material properties and weather
conditions. The plots remain unreviewed.

### Slide 41

The closing slide identifies large variation in predicted outputs as a
difficulty in defining target rewards.

## Attribution and scope uncertainty

| Claim | Status | Evidence |
|---|---|---|
| The user personally implemented or evaluated every method in the deck. | unknown | The cover lists a name and team but does not assign individual responsibilities ([slide 1](#slide-1)). |
| VAE embeddings improve RL convergence or policy quality. | unknown | The deck shows encoded data and states that clusters are visible, but supplies no quantitative comparison or validated embedding-to-policy result ([slides 38–40](#slide-38)). |
| The reported prediction and RL results have been independently reproduced. | unknown | Result plots remain uninspected, and no reproduction was performed ([slides 7–11](#slide-7); [slides 20–31](#slide-20)). |
| The CGAN augmentation approach was completed or deployed. | unknown | The deck presents it under exploration and next steps ([slide 13](#slide-13); [slide 35](#slide-35)). |

## Review notes

All 82 embedded media items remain uninspected, including the UMAP
representations and quality/convergence plots. The three speaker-note files
contain only slide-number text (`2`, `3`, and `27`). The deck's filename
contains the date `20220926`, while slide 2 refers to a new dataset from
September 2022; the cover does not state a presentation date. Reported model
metrics, sample counts, and convergence observations have not been
independently reproduced.
