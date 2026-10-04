---
id: janus-rl-20210830-janus-rl-v04-share-pptx
type: source
title: Janus RL V04: Transformed Data
aliases: []
related:
  - ../projects/janus-rl-training-and-exploration.md
source_refs: []
---

# Janus RL V04: Transformed Data

- **Status:** needs review
- **Original path:** `raw/Janus/RL/20210830_Janus_RL_V04_share.pptx`
- **Extraction:** Text extracted from all 27 slides; 26 speaker-note files and 151 media items are present. The note text mostly consists of slide numbers.
- **Reason for review:** Most slides contain result plots or diagrams and embedded media remains uninspected; reported outcomes have not been reproduced.
- **Original format:** PowerPoint presentation. The source under `raw/` was not modified.

## Summary

The deck reports experiments on a transformed Janus dataset with 782 rows,
228 features, 98 variable parameters, 130 fixed parameters, and six targets.
It discusses feature importance, prediction models, DQN and actor-critic
variants for discrete actions, A2C/DDPG for continuous actions, reward
choices, inference from multiple starts, and high-dimensionality challenges.

## Dataset and RL experiments

### Slides 2-6

The presentation compares linear regression, random forest, and neural
networks as process prediction models. It describes discretizing continuous
variables for DQN/A2C, and continuous-action A2C/DDPG experiments using
selected variables. It notes that predictor behavior and low feature
importance can affect agent training.

### Slides 7-17

Slides compare permutation-based and bifurcated DQN action outputs, actor
critic with discrete and continuous actions, relative and discrete rewards,
and policy behavior from multiple random starts. Reported issues include
action-space growth for permutation outputs, high variance, convergence
sensitivity to prediction surfaces, and training instability. The reported
outcomes have not been independently checked.

## Proposed follow-up work

### Slides 18-27

The deck proposes narrowing search bands using nearest samples, dimensionality
reduction with feature selection or autoencoders, removing correlated
features, and using standard RL libraries. It also documents a Gym
environment replay-buffer reference bug and experiments with whole-dataset
training and dropout subsets.

## Review notes

The 151 embedded media items include most experiment plots and remain
uninspected. The cover credits Gaurav Adke but does not establish individual
ownership of implementation or results.
