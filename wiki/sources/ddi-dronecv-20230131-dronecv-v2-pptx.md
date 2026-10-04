---
id: ddi-dronecv-20230131-dronecv-v2-pptx
type: source
title: Drone CV traffic and road-safety analytics presentation
aliases: []
related:
  - ../projects/ddi-dronecv-traffic-and-road-safety-analytics.md
source_refs: []
---

# Drone CV traffic and road-safety analytics presentation

- **Status:** needs review
- **Original path:** `raw/DDI/DroneCV/20230131_DroneCV_v2.pptx`
- **Extraction:** Slide text was extracted locally from all 42 slides using the
  presentation's OOXML. The archive contains 84 embedded media files that were
  not rendered or visually inspected; diagrams, figures, and any image-only
  details remain unchecked.
- **Reason for review:** Text supports a high-level summary, but visual content
  may contain information absent from the extracted text. The source remains
  unmodified.
- **Original format:** PowerPoint, 42 slides. No packages or external services
  were used for extraction.

## Summary

The presentation describes a traffic-analysis pipeline for drone video:
vehicle detection and tracking, per-frame metadata, trajectories, speeds,
distances, traffic-flow metrics, and safety-related event analysis. It also
discusses fixed-camera CCTV transfer, provided camera position is suitable for
the relevant measurements ([slides 3](#slide-3), [7](#slide-7),
[18](#slide-18), [30](#slide-30)).

It describes vehicle proximity and intersecting/adjacent trajectories as
inputs to TTC analysis; TTC is marked WIP. A generic PET algorithm is described
for drone and CCTV feeds with a constant camera position, and a rotating drone
is noted as a source of PET error ([slides 10–17](#slide-10), [30](#slide-30),
[40](#slide-40)). Traffic outputs include density, flux, vehicle counts and
speeds, lane changes, wrong-way movement, speeding, braking, and acceleration
events ([slides 18–19](#slide-18), [32–39](#slide-32)).

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The deck describes detecting/tracking vehicles and deriving per-frame records, trajectories, speeds, and distances. | documented | [Slides 3](#slide-3), [7](#slide-7), [9](#slide-9), [33](#slide-33). |
| The proposed traffic analyses include density, flux, vehicle-speed distributions, and traffic-flow patterns. | documented | [Slides 4](#slide-4), [18](#slide-18), [36](#slide-36). |
| TTC and PET are discussed as trajectory-based safety measures; the TTC section is marked WIP and PET is sensitive to camera motion. | documented | [Slides 15–17](#slide-15), [30](#slide-30), [40](#slide-40). |
| The task slide assigns YOLO model exploration and two-stage detection to a person named “Gaurav.” | documented | [Slide 3](#slide-3); the slide does not establish completion or identify the named person beyond the first name. |
| The assigned work or any named individual's implementation and mastery are established as completed. | unknown | The extracted text lists tasks and assignments but does not verify completion or individual mastery. |

## Slide references

### Slide 1

Title slide: “Drone CV.”

### Slide 2

“Thank You.”

### Slide 3

Task breakdown for data collection and labeling, augmentation, image
preprocessing, object-detection model exploration, two-stage detection, and
traffic/safety post-processing. The text assigns YOLO exploration and
two-stage detection to “Gaurav”; it does not confirm completion.

### Slide 4

Traffic-analysis ideas include counts, direction, speeds, distance, traffic
density and flow, vehicle trajectories, and related reference links.

### Slide 5

The extracted text focuses on safety analysis: proximity, lane changes,
potential near-misses, and TTC.

### Slide 6

The slide lists vehicle counts, directions, speeds, distances, traffic
analysis references, and intersection-safety services.

### Slide 7

The deck describes tracking output (vehicle type, tracking ID, bounding box,
frame rate), distance and velocity estimates, relative motion, vehicle
distributions, trajectory coordinates, and trajectory plots.

### Slide 8

The slide lists basic per-vehicle traffic measures, velocity distributions, and
plots by vehicle type.

### Slide 9

The slide describes trajectory extraction, vehicle centers, distances,
velocities, and trajectory plots.

### Slide 10

The slide describes intersecting and adjacent trajectories and per-frame
vehicle positions as inputs to proximity analysis.

### Slide 11

The slide discusses adjacent-trajectory distance distributions and possible
thresholds for same-lane and parallel-lane grouping.

### Slide 12

The slide considers temporal distances between vehicles in each frame and
percentile ranges for separating same-lane and parallel-lane cases.

### Slide 13

Examples are listed for intersecting trajectories.

### Slide 14

Examples are listed for adjacent trajectories. Extracted text notes a missed
truck, a possible threshold adjustment, and a tracking loss.

### Slide 15

TTC is derived from proximity vehicles, leading/trailing relationships,
distance, and relative velocity. The section is marked WIP and contains example
calculations, not a complete validation.

### Slide 16

The slide gives WIP TTC examples for intersecting and adjacent trajectories.

### Slide 17

The slide gives further TTC examples, including cases with acceleration.

### Slide 18

The deck summarizes traffic and safety outputs, including vehicle counts and
speeds, density, flux, speeding, abrupt speed changes, proximity, TTC, PET,
wrong-way driving, and VRU movement.

### Slide 19

This slide provides a second traffic/safety output summary, including volume,
velocity, lane changes, near misses, TTC, PET, and braking/acceleration events.

### Slide 20

The slide lists intersection safety services, including vehicle/VRU detection,
trajectories, speeds, TTC, near misses, PET, and dashboard analytics.

### Slide 21

The slide discusses market services for highway tailgating risk and risky road
exits.

### Slide 22

The slide labels traffic flux/density and braking, acceleration, speeding,
lane-change, and wrong-side detections as extra work.

### Slide 23

The slide describes velocity distributions and uses a simple moving average
for velocity plots.

### Slide 24

The slide describes percentile-based speeding/under-speeding identification
and the option of injecting speed limits after calibration.

### Slide 25

The slide describes a moving-average/MACD-inspired method for acceleration and
braking analysis.

### Slide 26

The extracted text lists example accelerating and braking vehicles and
mentions a possible effect of trucks.

### Slide 27

The extracted text lists further example accelerating and braking vehicles.

### Slide 28

The slide presents traffic density and flux plots; visual details were not
inspected.

### Slide 29

The slide presents trajectory plots; visual details were not inspected.

### Slide 30

The slide describes PET as a gap-time measure and says the generic algorithm is
intended for drone and CCTV feeds with a constant camera position; drone
rotation can make PET exceed the actual value.

### Slide 31

The slide lists links to related source presentations.

### Slide 32

The slide repeats the traffic and safety output summary, including traffic
metrics and TTC/PET events.

### Slide 33

The slide describes per-frame tracked information, primary variables, and
post-processing, including a possible conversion from pixels to meters using
a fixed calibrated camera.

### Slide 34

The extracted text describes vehicle counts and velocities by category.

### Slide 35

The extracted text describes velocity distributions and percentile-based
speeding/under-speeding events.

### Slide 36

The slide defines traffic density as vehicles per unit road length and flux as
vehicles per unit time, and notes possible relationships with congestion.

### Slide 37

The slide describes analyzing vehicle velocity profiles for braking,
acceleration, and speeding events.

### Slide 38

The slide describes extracting tailgating occurrences from proximity between
vehicles in the same lane.

### Slide 39

The slide describes traffic-flow and lane-change analysis using trajectories.
It also mentions assessing dedicated cycle/motorcycle lanes for vehicle
breaches.

### Slide 40

The slide repeats the PET method and its fixed-camera-position qualification.

### Slide 41

The slide lists an evaluation of multiple junctions based on low-PET event
counts; the extracted text includes region-level counts.

### Slide 42

The slide describes monitoring vehicle speeds near a pedestrian crossing, with
expected speed reduction and a region of interest. Visual details were not
inspected.
