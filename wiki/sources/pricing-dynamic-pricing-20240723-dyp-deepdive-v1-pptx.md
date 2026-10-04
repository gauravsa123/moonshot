---
id: pricing-dynamic-pricing-20240723-dyp-deepdive-v1-pptx
type: source
title: Dynamic Pricing — Euromaster Deep Dive V1
aliases: []
related:
  - ../projects/pricing-dynamic-pricing-euromaster.md
source_refs: []
---

# Dynamic Pricing — Euromaster Deep Dive V1

- **Status:** needs review
- **Original path:** `raw/Pricing/Dynamic Pricing/20240723_DYP-DeepDive_V1.pptx`
- **Extraction:** Text extracted from 36 slides and 33 note files; 91 media items are present.
- **Reason for review:** Embedded plots and other media remain uninspected; reported model-fit and pricing results have not been independently reproduced.
- **Original format:** PowerPoint presentation. The source under `raw/` was not modified.

## Objective and dataset

### Slides 2–3

The deck frames the analysis as estimating Euromaster tire-demand elasticity
at ZIP/geobox and diameter levels, and examining how competitive price ratios
relate to sales volumes and margins. The stated example covers French
Euromaster data from January 2020 through July 2023 and Norauto data from
July 2021 through January 2023, for summer passenger-car/SUV tires and
selected diameters.

## Hierarchical elasticity model

### Slides 4–5, 11–12, and 23–24

The presentation contrasts no-pooling and partial-pooling approaches for
geographic clusters, then describes Bayesian regression with priors,
posterior distributions, and credible intervals. It reports Gelman Bayesian
R-squared values of 0.51 at diameter level and 0.2 at geobox level; these
reported figures have not been reproduced.

## Data preprocessing

### Slides 6–9 and 22

The deck describes volume detrending using market change rates, price
normalization including CPI-based de-inflation, weekly-spike outlier
handling, and binning/rolling up observations with similar prices or low
transaction volumes. It notes that volume-weighted prices may introduce
artificial positive elasticity.

## Competition analysis

### Slides 13–14 and 32

Competition analysis considers Euromaster and Norauto price/volume data.
Another slide describes extracting competing SKUs from tire attributes and
using daily price movement correlation and time-series similarity (DTW) to
identify competing products.

## Optimization and results

### Slides 15–17 and 25

The deck reports filtering departments/geoboxes with scope for price
increases and comparing mean versus optimal price ratios. Its profit
optimization example assumes synthetic costs. It proposes validating
elasticity against pricing rules as a future step.

## Thompson sampling and non-stationary elasticity

### Slides 21, 26, and 29

An internship-experiment section compares Thompson sampling with nonlinear
least squares, describing uncertainty bounds and sensitivity to outliers.
The deck distinguishes stationary elasticity estimated from historical
curves from non-stationary elasticity adapted over time using Thompson
sampling. These slides do not establish production deployment.

## Review notes

The 36-slide presentation includes repeated summary/result slides and 33 note
files. Media and plots remain unreviewed; numerical results are source-reported
only.
