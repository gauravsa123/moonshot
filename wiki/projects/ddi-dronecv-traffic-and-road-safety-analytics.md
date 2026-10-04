---
id: ddi-dronecv-traffic-and-road-safety-analytics
type: project
title: DDI DroneCV Traffic and Road-Safety Analytics
aliases:
  - Drone CV
related:
  - ../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md
  - ../skills/computer-vision-object-detection-and-vehicle-classification.md
  - ../skills/multi-object-tracking-and-video-trajectory-estimation.md
  - ../skills/video-preprocessing-and-data-augmentation.md
  - ../skills/camera-calibration-and-pixel-to-world-measurement.md
  - ../skills/traffic-flow-analysis-and-transportation-metrics.md
  - ../skills/surrogate-road-safety-analysis-using-proximity-ttc-and-pet.md
  - ../skills/temporal-traffic-event-detection-from-trajectories-and-velocity-profiles.md
  - ../skills/road-user-and-traffic-safety-domain-analysis.md
  - ../skills/problem-solving.md
  - ../skills/cross-domain-concept-application.md
  - ../skills/deep-learning.md
  - ../skills/computer-vision.md
source_refs:
  - ../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-3
  - ../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-7
  - ../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-10
  - ../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-15
  - ../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-18
  - ../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-30
  - ../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-39
---

# DDI DroneCV Traffic and Road-Safety Analytics

## Project summary

The presentation describes a computer-vision workflow for analyzing road
traffic and safety from drone video, with some methods described as transferable
to fixed-camera CCTV. Its pipeline covers vehicle detection and tracking,
per-frame vehicle metadata, trajectories, speed and distance estimates, and
post-processing for traffic flow and safety analysis ([slides 3](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-3),
[7](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-7),
[18](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-18)).

The deck discusses traffic density and flux, lane changes, wrong-way movement,
speeding, braking and acceleration, and vehicle proximity. It describes
trajectory-based time-to-conflict (TTC) and post-encroachment-time (PET)
analyses; the TTC work is marked WIP, and the PET section notes camera motion
as a source of error ([slides 15–19](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-15),
[30](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-30),
[39–42](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-39)).

The task slide assigns YOLO model exploration and two-stage detection to
“Gaurav,” but this is an assignment in the presentation, not confirmation of
completion or a verified personal skill ([slide 3](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-3)).

## Sources

- [Drone CV traffic and road-safety analytics presentation](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md) — **needs review**; text was extracted from all 42 slides, but embedded media was not visually inspected.

## Know-how needed

These are user-confirmed project requirements, not claims about personal
experience, skill, or mastery.

| Skill | Review status | Rationale |
|---|---|---|
| [Computer-vision object detection and vehicle classification](../skills/computer-vision-object-detection-and-vehicle-classification.md) | user-confirmed | The task list names YOLO and two-stage detection, while the analytics cover multiple road-user classes ([slides 3](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-3), [6](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-6)). |
| [Multi-object tracking and video-based trajectory estimation](../skills/multi-object-tracking-and-video-trajectory-estimation.md) | user-confirmed | The deck uses track IDs, per-frame bounding boxes, trajectories, and vehicle positions and velocities ([slides 7](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-7), [9](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-9)). |
| [Video preprocessing and data augmentation](../skills/video-preprocessing-and-data-augmentation.md) | user-confirmed | The task breakdown includes augmentation, image up/down-sampling, enhancement, shadow removal, denoising, and road-marking removal ([slide 3](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-3)). |
| [Camera calibration and pixel-to-world measurement](../skills/camera-calibration-and-pixel-to-world-measurement.md) | user-confirmed | The deck describes pixel-to-meter conversion with a fixed calibrated camera and notes camera motion can affect PET estimates ([slides 7](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-7), [30](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-30)). |
| [Traffic-flow analysis and transportation metrics](../skills/traffic-flow-analysis-and-transportation-metrics.md) | user-confirmed | The presentation discusses vehicle counts, speed distributions, traffic density, traffic flux, flow, and fundamental diagrams ([slides 4](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-4), [18](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-18), [36](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-36)). |
| [Surrogate road-safety analysis using proximity, TTC, and PET](../skills/surrogate-road-safety-analysis-using-proximity-ttc-and-pet.md) | user-confirmed | The workflow identifies adjacent/intersecting trajectories, proximity, time-to-conflict, and post-encroachment-time events ([slides 10–17](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-10), [30](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-30)). |
| [Temporal traffic-event detection from trajectories and velocity profiles](../skills/temporal-traffic-event-detection-from-trajectories-and-velocity-profiles.md) | user-confirmed | The deck proposes identifying lane changes, speeding, braking, acceleration, and wrong-way events from tracked motion ([slides 22–27](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-22), [37](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-37), [39](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-39)). |
| [Road-user and traffic-safety domain analysis](../skills/road-user-and-traffic-safety-domain-analysis.md) | user-confirmed | The project frames analytic outputs around traffic operations, pedestrian crossings, lane behavior, and conflict/near-miss events ([slides 18–21](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-18)). |
| [Problem solving](../skills/problem-solving.md) | user-confirmed | The user added problem solving as know-how needed for this project. |
| [Cross-domain concept application](../skills/cross-domain-concept-application.md) | user-confirmed | The user highlighted applying stock-market concepts to vehicle-motion analysis; the presentation describes a MACD-inspired acceleration/braking analysis ([slide 25](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-25)). |
| [Deep learning](../skills/deep-learning.md) | user-confirmed | The user added deep learning as know-how needed for the project's object-detection work. |
| [Computer vision](../skills/computer-vision.md) | user-confirmed | The user added computer vision as broader know-how, distinct from the specific object-detection/classification requirement. |

## Skills shown by sources

These entries describe methods represented in the presentation, not personal
skills or proof of individual implementation.

| Skill or capability | Evidence status | Evidence |
|---|---|---|
| Vehicle detection, tracking, and trajectory analytics | documented | The deck describes detection/classification tasks, track outputs, trajectories, and their use in traffic analysis ([slides 3](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-3), [7–10](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-7)). |
| Traffic-flow metrics from video | documented | Traffic density, flux, vehicle counts, velocity distributions, and flow analysis are described ([slides 18–19](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-18), [36](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-36)). |
| Trajectory-based proximity and conflict analysis | documented | The presentation describes adjacent/intersecting trajectories, TTC calculations, and PET analysis ([slides 10–17](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-10), [30](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-30)). |
| Cross-domain use of a market-analysis concept for vehicle-motion analysis | documented | The deck explicitly calls the MACD concept stock-market-inspired and applies moving-average convergence/divergence analysis to vehicle acceleration/braking ([slide 25](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-25)). |
| Individual implementation, completion, or mastery | unknown | The presentation includes a named work assignment, but does not establish that assigned work was completed or demonstrate individual mastery ([slide 3](../sources/ddi-dronecv-20230131-dronecv-v2-pptx.md#slide-3)). |

## User-reported contributions and outcomes

No personal contributions or outcomes have been user-reported for this project.

## Review state

All twelve know-how requirements are `user-confirmed`; this records project
needs, not personal skill or mastery. The source remains `needs review` because
its 84 embedded media files were not visually inspected. The deck
marks the TTC work as WIP and describes a PET limitation related to camera
motion; no unverified performance result or personal contribution is inferred.
