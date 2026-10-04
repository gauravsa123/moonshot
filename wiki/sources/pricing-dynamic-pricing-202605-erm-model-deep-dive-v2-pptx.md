---
id: pricing-dynamic-pricing-202605-erm-model-deep-dive-v2-pptx
type: source
title: Euromaster Dynamic Price Optimization Model Deep Dive
aliases: []
related:
  - ../projects/pricing-dynamic-pricing-euromaster.md
source_refs: []
---

# Euromaster Dynamic Price Optimization Model Deep Dive

- **Status:** needs review
- **Original path:** `raw/Pricing/Dynamic Pricing/202605_ERM_Model deep-dive_V2.pptx`
- **Extraction:** Text extracted from 46 slides and 15 note files; 78 media items are present.
- **Reason for review:** Embedded plots and test/control evidence remain uninspected; reported performance and price effects have not been independently reproduced.
- **Original format:** PowerPoint presentation. The source under `raw/` was not modified.

## Scope

### Slides 1–2

The deck is a deep dive on the Euromaster dynamic-price-optimization model.
Its sections cover EAN-pair analysis, competitiveness, controller rules,
forecasting, and test/control outcomes.

## EAN-pair analysis

### Slides 3, 8–10, and 39

The presentation compares old and new test/control pairings, including
whether tire-rim-size and geobox distributions are balanced. One slide
describes selecting similar points of sale by comparing geobox-sales
distributions.

## Competitivity and controller rules

### Slides 4–5, 14–20, and 24–26

The deck examines test/control price-competitiveness ratios, observed price
gaps, and controller impacts. Named rules include product-line ordering,
minimum margins, and lower/upper price bounds. The source reports that
controller rules affected a substantial share of EAN prices; the underlying
plots and aggregation are not independently checked.

## Forecasting analysis

### Slides 6–7 and 21–22

The presentation compares forecast and actual test/control volumes and
proposes examining forecast differences, trends, and other time-series
features as possible performance drivers. Its figures and metrics remain
source-reported.

## Model evaluation

### Slides 12–13, 28–33, and 38–39

The deck investigates whether price competitiveness, elasticity estimates,
forecasting, controller rules, SKU pairing, and stock issues explain
test/control outcomes. It lists recommendations concerning the optimizer's
base price, competitiveness thresholds, psychological price points, and
reworking test/control pairs. These are recommendations and analyses in the
presentation, not independently validated effects.

## Inflection-point POC

### Slides 42–46

Several backup slides show geobox-wise inflection-point analyses by tire
diameter. A separate action slide assigns Gaurav follow-up work on
inflection-point identification; it does not establish completion or
individual implementation results.

## Review notes

The 46-slide deck contains 78 media items and 15 note files. The media remain
uninspected; all quantitative conclusions are source-reported and
unreproduced.
