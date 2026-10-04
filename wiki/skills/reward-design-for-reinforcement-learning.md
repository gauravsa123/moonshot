---
id: reward-design-for-reinforcement-learning
type: skill
title: Reward-function design and avoidance of unintended behavior
aliases: []
related:
  - reinforcement-learning-environment-state-action-reward-design.md
  - process-simulation-environment-design-for-reinforcement-learning.md
source_refs:
  - ../sources/janus-knowledge-sharing-20220309-rl-kss-1-pptx.md#slide-18
  - ../sources/janus-publication-janus-rl-overview-v01-docx.md#rl-and-optimization-outline
  - ../sources/janus-publication-rl-visualizations-pdf.md#environment-study-and-reward-functions
  - ../sources/janus-rl-20210713-janus-rl-v03-summary-pptx.md#slides-10-20
  - ../sources/janus-rl-20220516-janus-rl-v06-tiles-pptx.md#slides-9-12
  - ../sources/janus-vae-20220926-janus-rl-explo-vae-v08-pptx.md#slide-20
  - ../sources/janus-vae-20220926-janus-rl-explo-vae-v08-pptx.md#slide-30
---

# Reward-function design and avoidance of unintended behavior

Design reward signals that align agent incentives with task objectives,
anticipate interactions between rewards and penalties, and identify
unintended strategies caused by poorly specified objectives.

## Projects needing this skill

- [Janus Knowledge Sharing: Reinforcement Learning and DQN](../projects/janus-knowledge-sharing-reinforcement-learning-and-dqn.md) — user-confirmed project requirement.
- [Janus Deep RL for Industrial Process Optimization and Visualization](../projects/janus-rl-process-optimization-and-visualization.md) — user-confirmed project requirement.
- [Janus Reinforcement-Learning Training and Exploration](../projects/janus-rl-training-and-exploration.md) — user-confirmed project requirement.
- [Janus VAE-Based Exploration for Process Optimization](../projects/janus-vae-based-exploration-for-process-optimization.md) — user-confirmed project requirement.

## Projects with user-reported use

- None recorded.

## Projects showing this skill

- [Janus Knowledge Sharing: Reinforcement Learning and DQN](../projects/janus-knowledge-sharing-reinforcement-learning-and-dqn.md) — a slide discusses reward/penalty imbalance and unintended agent behavior; it does not establish a personally designed reward function ([reward design](../sources/janus-knowledge-sharing-20220309-rl-kss-1-pptx.md#slide-18)).
- [Janus Deep RL for Industrial Process Optimization and Visualization](../projects/janus-rl-process-optimization-and-visualization.md) — the sources discuss target-distance rewards, shaping, and penalties on infeasible/extreme values; individual reward-function authorship is not established ([overview](../sources/janus-publication-janus-rl-overview-v01-docx.md#rl-and-optimization-outline); [paper](../sources/janus-publication-rl-visualizations-pdf.md#environment-study-and-reward-functions)).
- [Janus Reinforcement-Learning Training and Exploration](../projects/janus-rl-training-and-exploration.md) — the presentations compare relative, absolute, sparse, and stepwise rewards for process targets; no individual reward-design responsibility is assigned ([V03](../sources/janus-rl-20210713-janus-rl-v03-summary-pptx.md#slides-10-20); [V06](../sources/janus-rl-20220516-janus-rl-v06-tiles-pptx.md#slides-9-12)).
- [Janus VAE-Based Exploration for Process Optimization](../projects/janus-vae-based-exploration-for-process-optimization.md) — the deck discusses max/zero/negative reward regions for two quality targets and proposes stepwise reward; plotted outcomes remain unreviewed ([target reward](../sources/janus-vae-20220926-janus-rl-explo-vae-v08-pptx.md#slide-20); [stepwise reward](../sources/janus-vae-20220926-janus-rl-explo-vae-v08-pptx.md#slide-30)).
