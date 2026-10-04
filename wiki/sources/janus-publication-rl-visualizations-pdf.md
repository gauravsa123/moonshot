---
id: janus-publication-rl-visualizations-pdf
type: source
title: Visualization techniques for training deep RL agents in continuous spaces
aliases: []
related:
  - ../projects/janus-rl-process-optimization-and-visualization.md
source_refs: []
---

# Visualization techniques for training deep RL agents in continuous spaces

- **Status:** needs review
- **Original path:** `raw/Janus/Publication/RL_visualizations.pdf`
- **Extraction:** Text was extracted from all eight pages. Charts, diagrams,
  and plot details remain visually unreviewed.
- **Reason for review:** The paper's figures contain core evidence about agent
  behavior and convergence; results and visual claims have not been
  independently reproduced.
- **Original format:** PDF. The source under `raw/` was not modified.

## Abstract

The paper presents visualization techniques for understanding and debugging
deep-RL agents in high-dimensional continuous state/action spaces, using
rubber-mix production-process optimization as its example. It organizes
visualizations around the environment, training dynamics, learned policy,
and policy performance. The title page lists Gaurav Adke as first author,
followed by Ameya Divekar and Guillaume Ramelet, with Michelin affiliations.

## Problem setup

The simulated production environment maps fixed and controllable process
parameters to product-quality outputs. The agent changes controllable
parameters, receives rewards based on proximity to target quality, and
terminates episodes at target attainment or a maximum number of steps. The
visualization demonstrations use four controllable parameters and two quality
outputs. The paper identifies DDPG as the actor-critic algorithm used for
demonstration.

## Visualization methods

### Environment study and reward functions

Reward contours are plotted against target-quality values and input
parameters. The paper compares sparse and distance-based reward behavior and
visualizes the underlying process-prediction model, including random-forest
surfaces. It states that smoother distance-based reward gradients can
facilitate learning and that joint plots can reveal feasible input ranges.

### Training dynamics

The paper describes plots for quality outputs, controllable variables,
cumulative rewards, and target-output errors over training. These are
presented as ways to monitor convergence, instability, and training duration.

### Trained policy and exploration

Proposed visualizations include action scatter/vector plots, action
distributions, variable co-occurrence, episode trajectories, exploration
coverage, replay-buffer states, policy start/end states, and critic values.
PCA is used to reduce state dimensionality for several plots. The paper
describes an exploration issue where the agent sampled only part of the
observation space and says the sampling procedure was corrected.

### Environment dynamics and policy evaluation

The paper plots predicted quality outputs and distances to targets across
test episodes, including tolerance regions and different fixed-parameter
settings. It presents these views as a way to identify target combinations
that remain difficult for the learned policy.

## Reported outcomes and limitations

The paper says that the visualizations help debug reward functions, inspect
training convergence, compare policies, identify insufficient exploration,
and analyze possible multiple solutions. It describes the demonstrated agent
as approaching target-quality regions. These are source-reported conclusions;
the figures have not been inspected and results have not been independently
reproduced. The paper states that the techniques were developed for a
particular process-optimization problem and could be extended to other RL
algorithms.

## Content map

The eight-page document contains the title and abstract on page 1, problem
setup and the visualization taxonomy on pages 1–2, reward and training
visualizations on pages 2–3, policy/exploration plots on pages 4–6,
environment-performance plots and conclusions on pages 7–8, and references
on page 8. Figures remain unreviewed.
