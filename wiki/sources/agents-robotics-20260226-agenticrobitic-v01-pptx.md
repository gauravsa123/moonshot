---
id: agents-robotics-20260226-agenticrobitic-v01-pptx
type: source
title: Robotics with MAS
aliases: []
related:
  - ../projects/agents-robotics.md
source_refs: []
---

# Robotics with MAS

- **Status:** needs review
- **Original path:** `raw/Agents/Robotics/20260226_AgenticRobitic_v01.pptx`
- **Extraction:** Text was extracted locally from all 8 slides. The PPTX archive contains 17 embedded media files, with picture objects on slides 2, 5, and 8. These visuals were not rendered or visually inspected; visual relationships, diagram details, and the picture-only content on slide 5 therefore remain unchecked. The six notes-slide files contain only slide-number text, not substantive speaker notes.
- **Reason for review:** Text extraction supports a summary of the written content, but visual content was not inspected and may contain information not present in the extracted text.
- **Original format:** PowerPoint, 8 slides. The source under `raw/` was not modified; no packages were installed and no external services or links were used.

## Summary

The deck outlines a multi-agent robotics framework in which a planner selects
high-level tasks and a controller translates them into low-level actuator
commands. It names multi-robot coordination and latent collaboration as areas
of exploration, and lists camera images, actuator coordinates, gripper forces,
and depth maps as observations. Example rewards include proximity to an object
and picking it up ([slides 2](#slide-2), [6](#slide-6)).

The roadmap proposes Genesis simulation experiments, sensor integration,
Franka-arm manipulation with external action inputs, an action-primitive
library, VLM-based planning, and OpenVLA conversion of steps to actions. It
also mentions RL alternatives, multi-agent coordination, and a possible
simulation-to-real path involving SO100 and Rover robots with Jetson Nano
([slide 3](#slide-3)). These are presented as roadmap topics, not as verified
completed implementations.

The final content slides cite research material and outline a possible
LLM-guided adaptive-RL workflow and multi-robot implementation steps, including
VLM backbones, perception/planning and execution/reflection roles, shared
observations, reflection/communication loops, and simulation/benchmarking
([slides 7](#slide-7), [8](#slide-8)). The deck supplies no verified
performance results in its extracted text. The title slide names Gaurav Adke
and DAI/DOTI but does not assign individual roles or establish personal
mastery ([slide 1](#slide-1)).

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The framework text separates high-level planning from low-level actuator control and lists sensors, observations, and reward examples. | documented | [Slides 2](#slide-2), [6](#slide-6). |
| The deck proposes experiments and development directions including Genesis, Franka, action primitives, VLM/OpenVLA, RL, multi-robot coordination, and sim-to-real work. | documented | [Slide 3](#slide-3). These are roadmap items, not evidence of completion. |
| A possible adaptive-RL and multi-robot workflow is outlined with LLM task decomposition, arm selection, VLM roles, reflection, shared observations, and simulation/benchmarks. | documented | [Slide 8](#slide-8). This is proposed material, not an evaluated result. |
| The source establishes individual roles, contributions, or personal mastery. | unknown | The title slide contains a name and DAI/DOTI affiliation text but no responsibility assignments ([slide 1](#slide-1)). |

## Slide references

### Slide 1

Title: “Robotics with MAS”; shows the text “Gaurav Adke” and “DAI/DOTI.” No
individual role or contribution is assigned.

### Slide 2

Titled “Learning Paradigms” and “Framework.” The extracted labels include
Planner Agent 1/2, Controller, Latent Collaboration, high-level tasks,
low-level actuator commands, Simulation Environment, OpenVLA, VLM models,
observations, reward function, reinforcement and imitation learning, action
primitives, rule-based methods, and robotic operations. The diagram imagery
was not inspected.

### Slide 3

“Action Roadmap” lists Genesis simulation experiments; integration of camera,
coordinate, depth, and force sensors; external-action-input manipulation of a
Franka arm; a primitive-action library; VLM-based step planning; OpenVLA
conversion of steps to actions; RL as an alternative for task-specific
motions; multi-agent robot coordination; latent collaboration; and
sim-to-real work with SO100 and Rover using Jetson Nano. The items are
roadmap text.

### Slide 4

“Thank You.”

### Slide 5

“Action Roadmap” and “Humanoid.” A picture object is present, but its visual
content was not inspected.

### Slide 6

“Framework” text describes MAS for robotic navigation: a planner decides
tasks; a controller converts them to actuator actions such as joint rotations
and gripper openings; the system explores coordination of two or more robots
and latent collaboration. It lists camera views, actuator coordinates,
gripper forces, depth maps, and rewards such as object proximity and pickup.
OpenVLA, RL, VLMs, imitation learning, primitives, and Genesis-to-real are
named. An accompanying text block summarizes this framework but does not
provide experimental results.

### Slide 7

“Papers” lists an embodied multi-agent systems review and links/resources on
VLM-based VLA robotic manipulation, RT-2, VLM-based agentic workflow design,
ManiAgent, VLA models, and the RobotecAI RAI repository. The cited materials
were not opened or independently checked.

### Slide 8

“Papers” cites “LLMs for designing robotic workflow” and outlines adaptive RL
policy development using an agentic system: an LLM decomposes a task and
selects an arm based on reach/angles, while an RL agent designs training code.
Its “Implementation Steps” propose VLM backbones fine-tuned for VLA output,
perception/planning and execution/reflection roles, shared observations,
reflection and communication loops, and simulation/benchmarking in RoboCasa.
These are proposals in the slide, not evidence that they were implemented.
