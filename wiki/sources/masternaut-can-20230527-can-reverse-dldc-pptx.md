---
id: masternaut-can-20230527-can-reverse-dldc-pptx
type: source
title: CAN bus reversing using deep learning
aliases: []
related:
  - ../projects/masternaut-can-bus-reverse-engineering.md
source_refs: []
---

# CAN bus reversing using deep learning

- **Status:** needs review
- **Original path:** `raw/Masternaut/CAN/20230527_can_reverse_DLDC.pptx`
- **Extraction:** Text extracted from all 30 slides; 21 speaker-note files and 72 media items are present. Two notes contain additional reference/context text.
- **Reason for review:** Figures and embedded media remain uninspected; reported model and decoding results have not been independently reproduced.
- **Original format:** PowerPoint presentation. The source under `raw/` was not modified.

## Summary

The presentation describes a two-stage approach to reverse-engineer CAN
signals: classify CAN IDs by signal type, then infer candidate start bits,
lengths, endianness, and signedness. Interpretive convolutions enumerate
bit-layout possibilities to produce 716 features; sequence and CNN models are
discussed for classification. Additional topics include class imbalance,
wavelet-based negative filtering, data augmentation, per-ID scaling,
topological analysis, and candidate-decoding scores.

## Title slide

### Slide 1

The cover title is “CAN reversing using Deep learning,” dated 27 May 2023,
and names Gaurav Adke.

## CAN protocol and task

### Slide 3

The deck introduces CAN as a communication protocol used by vehicle
electronic control units and motivates decoding encoded vehicle signals such
as engine RPM, speed, and odometer.

### Slides 4-7

The manual workflow starts from labeled CAN logs, signal IDs, timestamps, and
hexadecimal records. Known bit positions, lengths, and endianness convert
bits to numeric time series. The reverse-engineering task is harder because
those layout details are unknown and signal classes are highly imbalanced.

## Feature construction and classification

### Slides 8-10

Interpretive convolutions apply multiple window lengths and permutations of
endianness and signedness to raw CAN bits. The presentation reports 716
candidate values per timestep and 100-timestep input segments. It describes
an LSTM classifier with 100-by-716 inputs.

### Slides 19-21

The deck presents classification examples, recall-oriented thresholds, and
alternative CNN/transfer-feature representations. Figures and reported
performance remain unreviewed.

## Imbalance, augmentation, and diagnostics

### Slides 11-17

The presentation discusses the one-positive-versus-many-negative structure,
wavelet/cross-correlation filtering of improbable negatives, temporal
augmentation of minority samples, and diffusion-based generation as work in
progress. It also proposes topological feature comparisons. A slide reports
filtering up to 60% of negative samples; this has not been independently
verified.

### Slides 22-24

The deck describes streaming large datasets through a TensorFlow dataset
generator and storing per-arbitration-ID statistics for time-series scaling.
It mentions data reaching 138,000 samples for four brands.

## Recovering unknown bit boundaries

### Slides 25-28

The presentation describes progressive masking and classifier probability
maps to shortlist possible start/end bits, then ranks candidate decoded curves
using continuity and switch-rate scores. Example Engine RPM candidates are
shown for a limited training set; figures and results remain unreviewed.

## Abstract and interpretive convolutions

### Slides 29-30

The closing abstract summarizes the proposed classification and imbalance
approach. The final slide describes interpretive convolutions and cites prior
CAN-signal classification research.

## Speaker-note references

The note for slide 12 names an introductory wavelet-transform article. The
note for slide 16 includes a conceptual explanation of topology and
persistence-related analysis. These notes add context but do not verify the
reported results.
