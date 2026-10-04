---
id: janus-rl-20210713-janus-rl-v03-summary-pptx
type: source
title: Janus RL V03: Experiments and Learnings
aliases: []
related:
  - ../projects/janus-rl-training-and-exploration.md
source_refs: []
---

# Janus RL V03: Experiments and Learnings

- **Status:** needs review
- **Original path:** `raw/Janus/RL/20210713_Janus_RL_V03_summary.pptx`
- **Extraction:** Text extracted from all 62 slides; 58 speaker-note files and 174 media items are present. The note text mostly consists of slide numbers.
- **Reason for review:** Figures and embedded media remain uninspected; reported training behavior and outcomes have not been reproduced.
- **Original format:** PowerPoint presentation. The source under `raw/` was not modified.

## Summary

The presentation describes RL experiments for multivariable rubber-mix
optimization, progressing from dummy and synthetic datasets to transformed
process data. It discusses prediction models as environment simulators,
reward comparisons, state/action design, branching Q networks, policy
gradient and actor-critic approaches, exponential moving/weight averaging,
all-action training, and inference. It also contains experiments on a
Swedish claims dataset and synthetic regression data; these are examples, not
the rubber-mix data.

## Problem and experimental setup

### Slide 3

The stated objective is a deep-RL controller for real-time rubber-mix
manufacturing. The presentation frames the task as nonlinear, multi-variable
and multi-objective, with process settings as controllable inputs, raw
material properties as fixed inputs, and six quality metrics as outputs.

### Slides 5-9

The deck outlines rubber-process datasets and analogous RL experiments,
including single-input/output, multi-input/single-output, and multi-input/
multi-output tasks. Linear regression and random forests are discussed as
prediction models for the environment. Other slides describe a Swedish
claims example and synthetic regression data.

## RL methods and findings

### Slides 10-20

The presentation compares relative, absolute, sparse/discrete, and
incremental rewards; permutation-based versus branched action models; DQN,
policy-gradient, REINFORCE, and actor-critic methods; and training changes
such as exponential averaging and all-action updates. It reports that
relative rewards and actor-critic variants showed favorable convergence in
some experiments, while hyperparameter sensitivity, variance, exploration,
and local optima remained concerns. These are source-reported findings, not
independently verified results.

### Slides 31-62

Later material expands on dummy datasets, multi-output reward shaping,
random-forest and linear-model surfaces, Q-network variants, actor-critic
training, inference, and proposed follow-up work such as A3C, continuous
control on transformed rubber data, and performance metrics. Slide 57 lists
inverse RL and SARSA as planned work.

## Review notes

Slide 5 and repeated slide 22 contain dense dataset diagrams whose visual
details need review. The embedded media remain uninspected. The presentation
cover credits Gaurav Adke; it does not allocate individual responsibility
for the work.
