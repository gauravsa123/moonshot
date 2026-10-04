---
id: janus-rl-20220516-janus-rl-v06-tiles-pptx
type: source
title: Janus RL V06: Exploration and Dropout Analysis
aliases: []
related:
  - ../projects/janus-rl-training-and-exploration.md
source_refs: []
---

# Janus RL V06: Exploration and Dropout Analysis

- **Status:** needs review
- **Original path:** `raw/Janus/RL/20220516_Janus_RL_V06_Tiles.pptx`
- **Extraction:** Text extracted from all 12 slides; seven speaker-note files and 14 media items are present. The notes contain only slide numbers.
- **Reason for review:** Result tables and plots remain visually unreviewed; reported variant percentages have not been independently reproduced.
- **Original format:** PowerPoint presentation. The source under `raw/` was not modified.

## Summary

The presentation reviews Janus RL methodology and explores dropout
heterogeneity, data exploration, reward changes, and experience-replay
sampling. It mentions histogram, parallel-coordinate, scatter, box, UMAP,
and clustering analyses; accessible target ranges; stepwise rewards; and
possible VAE/CGAN-based exploration.

## Exploration and training

### Slides 2-8

The deck maps RL competency and experiments across dummy and obfuscated
datasets, action/reward methods, prediction models, and state-space analysis.
It proposes or discusses dropout clustering, replay-buffer size and sample
age, increased penalties for actions outside limits, sub-clustering, and
exploration diagnostics.

### Slides 9-12

The slides describe difficulty converging when some dropout groups have no
shared accessible target, and propose stepwise rewards that adapt to
state-dependent quality ranges. A final table reports variant percentages
for reaching an acceptable range; those values are not reproduced here.

## Review notes

Slides 5–6 contain unresolved brainstorming questions about trip points,
shortlisted samples, and reward changes. The 14 embedded media items,
including result visuals, remain uninspected.
