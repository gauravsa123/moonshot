---
id: janus-rl-20230418-janus-paperreview-v10-pptx
type: source
title: Janus RL Paper Review V10
aliases: []
related:
  - ../projects/janus-rl-training-and-exploration.md
source_refs: []
---

# Janus RL Paper Review V10

- **Status:** needs review
- **Original path:** `raw/Janus/RL/20230418_Janus_PaperReview_V10.pptx`
- **Extraction:** Text extracted from all 14 slides; 12 speaker-note files and 38 media items are present. The note text mostly consists of slide numbers.
- **Reason for review:** Figures and cited paper details remain unreviewed; several slides cover unrelated latent-manipulation and diffusion topics.
- **Original format:** PowerPoint presentation. The source under `raw/` was not modified.

## Summary

Slides 2–7 review reinforcement-learning approaches for high-dimensional
chemical-process control and a simulated beer-fermentation environment.
Slides 8–14 switch to latent manipulation, distance regularization, and
diffusion-model content and are not treated as evidence for the Janus RL
project profile.

## RL paper and simulator review

### Slides 2-5

The deck summarizes factorial/dynamic policy programming and a fast-food
approximation for vinyl-acetate process control. Topics include KL-divergence
regularization for policy updates, continuous states with discrete actions,
factorized agents, and simulator transitions that model process lags and
combined effects. It contrasts this process simulator with the then-described
Janus setup, where transitions were approximated using actions and quality
was modeled separately.

### Slides 6-7

The presentation describes a beer-fermentation simulation with temperature
control, process end conditions, and reward values for success, steps, and
failure. It mentions evaluating the environment using Stable-Baselines3
Soft Actor-Critic. Results and cited materials were not independently
checked.

## Non-RL content

Slides 8–14 discuss latent-space manipulation, distance regularization, and
diffusion. Their presence is retained as a source-scope caveat and not
attributed to the RL project.
