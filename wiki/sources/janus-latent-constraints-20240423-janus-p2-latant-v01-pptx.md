---
id: janus-latent-constraints-20240423-janus-p2-latant-v01-pptx
type: source
title: Janus Phase 2 latent constraints for controlled tabular generation
aliases: []
related:
  - ../projects/janus-latent-constraints-controlled-generation.md
source_refs: []
---

# Janus Phase 2 latent constraints for controlled tabular generation

- **Status:** needs review
- **Original path:** `raw/Janus/Latent Constraints/20240423_Janus_p2_latant_V01.pptx`
- **Extraction:** Text was extracted from all 25 slides. The file contains 47
  embedded media items and 23 speaker-note files; no substantive note text
  was found.
- **Reason for review:** Latent-space plots and result visuals remain
  uninspected; several slides contain little extracted text, and no
  quantitative evaluation is stated.
- **Original format:** PowerPoint. The source under `raw/` was not modified.

## Summary

This deck focuses on controlled exploration of tabular latent spaces. It
separates fixed and controllable variables, discusses KL-based relationships
between latent representations, and applies latent constraints in different
spaces. Synthetic data and a scenario with a target output variable are used
in result slides; distance-penalty settings of 0.3, 0.5, and 0.7 are shown.
The source also flags reconstruction quality as needing improvement for
additional controllable variables. Plots and outcomes were not visually
reviewed, and quantitative performance measures are not given in extracted
text.

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The approach distinguishes fixed and controllable variables in latent space. | documented | [Controlled-space concepts](#slide-3)–[6](#slide-6). |
| A main latent representation is described as disentangled with respect to fixed parameters while retaining target/output variation. | documented | [Scenario results](#slide-7); [synthetic-data results](#slide-8). |
| Distance-penalty settings of 0.3, 0.5, and 0.7 are compared. | documented | [Slides 9](#slide-9)–[11](#slide-11); plotted results were not visually checked. |
| Additional controllable variables may require reconstruction trade-offs or loss-weight changes. | documented | [Slide 13](#slide-13) notes reconstruction needs improvement; [slide 14](#slide-14) adds a control-latent layer. |
| Constraint operations are explored in multiple latent spaces. | documented | [Slides 17](#slide-17)–[23](#slide-23); plots remain uninspected. |
| The reported variants improve realism or satisfy constraints quantitatively. | unknown | Extracted text gives no quantitative metrics, and result figures were not inspected. |

## Slide references

### Slide 1

Title: “Janus: Latent Constraints — Latent space exploration for controlled
generation of Tabular Data.” It lists Gaurav Adke and AI Squad, DCTI.

### Slide 2

Shows a generated-data artifact path; its contents were not opened.

### Slide 3

Introduces fixed and controllable latent spaces, refers to a VAER paper, and
poses a question about disentangling controllable directions. The acronym
“VAER” is not expanded in the extracted text.

### Slide 4

Outlines latent disentanglement, fixed versus controllable variables, and
results for a scenario; notes an issue with entangled input variables.

### Slide 5

Describes separating fixed variables into a main latent space and adding a
Gaussian-prior loss.

### Slide 6

Shows an approach that leaves quality entangled so a latent constraint can
select a desired quality value.

### Slide 7

Describes a scenario in which the main latent is disentangled with respect to
fixed parameters while the output variable remains controllable.

### Slide 8

Shows synthetic-data results and binned output values; fixed and controllable
columns are described.

### Slide 9

Shows latent-constraint results for target variable 5 with a distance penalty
of 0.3.

### Slide 10

Shows variation results with a distance penalty of 0.5.

### Slide 11

Shows variation results with a distance penalty of 0.7.

### Slide 12

Contains sparse extracted text; visual content remains unreviewed.

### Slide 13

Treats `T_workshop` as controllable, notes that reconstruction needs
improvement, and suggests reducing a reconstruction weight for a controllable
representation.

### Slide 14

Treats `T_workshop` and `Hs` as controllable and adds a linear layer between
control and main latents for a KL loss.

### Slide 15

Mentions a Gaussian normal constraint on the main controllable latent space.

### Slide 16

Contains only a section heading in extracted text; visual content remains
unreviewed.

### Slide 17

Shows latent constraints applied in a control-latent space while changing
disentanglement with respect to output values.

### Slide 18

Adds a distance penalty in a control/KL latent space.

### Slide 19

Shows a related variant with the distance penalty in the control/KL latent
space; diagrams remain unreviewed.

### Slide 20

Shows constraints applied in the main latent space.

### Slide 21

Shows a variant that adds output-value disentanglement in the main latent
space.

### Slide 22

Shows synthetic-data results with fixed and controllable variables.

### Slide 23

States that a closer latent-space distance produces less variation in fixed
variables; the plot was not visually inspected.

### Slide 24

“Thank you.”

### Slide 25

Contains sparse extracted text referring to “With Y”; visual content remains
unreviewed.
