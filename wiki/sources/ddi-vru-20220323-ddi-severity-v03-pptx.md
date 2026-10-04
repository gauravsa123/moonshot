---
id: ddi-vru-20220323-ddi-severity-v03-pptx
type: source
title: Arc severity risk map
aliases: []
related:
  - ../projects/ddi-vru-risk-and-multimodality.md
source_refs: []
---

# Arc severity risk map

- **Status:** needs review
- **Original path:** `raw/DDI/VRU/20220323_DDI_severity_v03.pptx`
- **Extraction:** Slide text was extracted locally from all 3 slides. The
  archive contains 17 embedded media files; the risk-map visualization was not
  visually inspected.
- **Reason for review:** The deck is brief and its key risk-map representation
  is visual; extracted text alone may not capture its full design.
- **Original format:** PowerPoint, 3 slides. No packages or external services
  were used for extraction.

## Summary

The presentation describes an accident-risk map formulation. GPS density is
averaged by region and hour across selected days; each region/time cell has a
binary accident-occurrence label, and the summed severity of accidents is
another output ([slide 2](#slide-2)).

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The risk-map input includes GPS density averaged by region and hour across days. | documented | [Slide 2](#slide-2). |
| The outputs include binary accident labels and a sum of accident severity for each region/time cell. | documented | [Slide 2](#slide-2). |
| The risk-map visualization or its performance is established by text extraction alone. | unknown | The slide's visual was not inspected and no performance evaluation is described in the extracted text. |

## Slide references

### Slide 1

Title: “Arcs Severity.”

### Slide 2

Risk-map formulation: GPS density averaged for a region and hour across days,
a binary accident/no-accident label for each cell/time, and summed accident
severity for each region/time. A repository issue is listed as a reference;
it was not independently reviewed.

### Slide 3

“Thank You.”
