---
id: pricing-dynamic-pricing-20250418-dyp-deepdive-v2-pptx
type: source
title: Dynamic Pricing with Euromaster Deep Dive V2
aliases: []
related:
  - ../projects/pricing-dynamic-pricing-euromaster.md
source_refs: []
---

# Dynamic Pricing with Euromaster Deep Dive V2

- **Status:** needs review
- **Original path:** `raw/Pricing/Dynamic Pricing/20250418_DYP-DeepDive_V2.pptx`
- **Extraction:** Text extracted from 23 slides and 16 note files; 73 media items are present.
- **Reason for review:** Embedded plots and result tables remain uninspected; reported forecast and optimization results have not been independently reproduced.
- **Original format:** PowerPoint presentation. The source under `raw/` was not modified.

## Objective and contributors

### Slide 1

The title slide is dated 18 April 2025 and lists Gaurav A, Ved P, and
Ameya D. The remaining slides describe an optimization methodology,
shortlisting SKUs for a proof of concept, point-of-sale selection, and
forecasting.

## Optimization methodology

### Slide 4

The described pipeline forecasts next-week SKU volume, estimates price
elasticity to form price-volume pairs, optimizes price to maximize revenue
and margin using linear programming, then applies a controller to impose
business constraints.

## SKU grouping and point-of-sale selection

### Slides 5–6 and 8

The deck describes grouping SKUs because individual products may have low
volumes or insufficient price variation. Grouping options include season- or
diameter-level indexed prices, variation measures, and detrended/deseasoned
prices. It also describes creating “virtual twin” points of sale from
geobox-sales distributions using L1 distances to form test/control pairs.

## Weekly volume forecasting

### Slides 9–13

The source describes weekly country/geobox forecasts with calendar and lag
features, including a LightGBM model. It reports that additional modeling of
the number of contributing locations reduced observed forecast error, while
point-of-sale-level forecasting and uncertainty quantification are described
as future or in-progress work. Reported metrics have not been reproduced.

## Preprocessing, controller, and guardrails

### Slides 16–23

The deck revisits detrending, CPI-based price normalization, outlier removal,
and binning. It describes controller/guardrail considerations including
margin protection, price bounds, limiting price changes, consistency of
week-to-week changes, and rounding to familiar price endings.

## Competition and future analysis

### Slides 21–23

The source inventories available pricing, promotion, sales, and competitor
data, including update-frequency and coverage limitations. It also proposes
additional analysis of elasticity intervals, forecast variation, and
pricing-rule effects.

## Review notes

The deck lists three contributors on its cover but does not allocate
individual implementation responsibility. Its plots and tables remain
unreviewed, and source-reported model performance has not been independently
verified.
