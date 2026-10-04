---
id: agents-robotics
type: project
title: Robotics with Multi-Agent Systems
aliases:
  - Robotics with MAS
related:
  - ../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md
  - ../skills/agentic-workflow-orchestration-and-tool-integration.md
  - ../skills/robotic-manipulation-and-action-primitives.md
  - ../skills/vlm-vla-integration-for-robotics.md
  - ../skills/reinforcement-learning-for-robotics.md
  - ../skills/simulation-to-real-transfer-for-robotics.md
  - ../skills/latent-state-multi-agent-collaboration.md
  - ../skills/thought-leadership-in-agentic-ai-for-robotics-proposal.md
source_refs:
  - ../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-2
  - ../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-3
  - ../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-6
  - ../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-8
---

# Robotics with Multi-Agent Systems

## Project summary

The presentation outlines a multi-agent robotics framework rather than
documenting a verified deployment. Its text describes a planner that selects
high-level tasks and a controller that translates them into low-level
actuator commands, with possible coordination between multiple robots. It
lists camera images, actuator coordinates, gripper forces, and depth maps as
observations, and object proximity or successful pickup as reward signals.
OpenVLA, vision-language models (VLMs), reinforcement learning (RL),
imitation learning, and action primitives appear as candidate methods or
components ([slides 2](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-2),
[6](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-6)).

The action roadmap proposes experiments in Genesis simulation, camera and
other sensor integration, external control of a Franka arm, a primitive-action
library, VLM-based step planning, and OpenVLA conversion of steps to actions.
It also names RL as an alternative for task-specific motions, multi-agent
coordination, latent collaboration, and a simulation-to-real path involving
SO100 and Rover robots with Jetson Nano ([slide 3](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-3)).
These are roadmap items, not evidence that the experiments, hardware
integration, or deployment were completed.

Later slides cite robotics and agent-workflow material and give a possible
adaptive-RL workflow: an LLM breaks down a task and selects an arm, while an
RL agent designs training code. A separate “Implementation Steps” list
suggests VLM backbones, perception/planning and execution/reflection roles,
shared observations, reflection and communication loops, and simulation and
benchmarking in RoboCasa ([slides 7–8](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-7)).
These slides present research references and proposals; they do not establish
their implementation or evaluation.

The title slide names Gaurav Adke and DAI/DOTI but does not assign individual
roles or contributions. Personal responsibility, skill, and mastery are not
inferred.

## Sources

- [Robotics with MAS](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md)
  — **needs review**; text was extracted from all eight slides, but embedded
  media and picture content were not visually inspected.

## Know-how needed

These are user-confirmed project requirements, not claims about the user's
personal experience, skill, or mastery.

| Skill | Review status | Rationale |
|---|---|---|
| [Agentic workflow orchestration and tool integration](../skills/agentic-workflow-orchestration-and-tool-integration.md) | user-confirmed | The proposed planner/controller split and coordination among robot agents call for orchestration across high-level decisions and execution; the slide text does not establish a completed implementation. This workflow skill remains distinct from Agentic RAG. |
| [Robotics manipulation and action primitives](../skills/robotic-manipulation-and-action-primitives.md) | user-confirmed | The roadmap names Franka-arm manipulation, low-level actuator commands, and building a library of reusable action primitives ([slides 3](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-3), [6](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-6)). |
| [VLM/VLA integration for robotics](../skills/vlm-vla-integration-for-robotics.md) | user-confirmed | The proposal connects camera, depth, force, and coordinate observations with VLM planning and OpenVLA action generation ([slides 3](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-3), [6](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-6)). |
| [Reinforcement learning for robotics](../skills/reinforcement-learning-for-robotics.md) | user-confirmed | RL appears as an alternative to VLA-based action generation and as a proposed adaptive policy/training-code workflow ([slides 3](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-3), [8](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-8)). |
| [Simulation-to-real transfer for robotics](../skills/simulation-to-real-transfer-for-robotics.md) | user-confirmed | The roadmap names Genesis simulation and a possible transition to SO100 and Rover hardware with Jetson Nano ([slide 3](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-3); framework concept on [slide 6](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-6)). |
| [Latent-state multi-agent collaboration](../skills/latent-state-multi-agent-collaboration.md) | user-confirmed | The deck names latent collaboration as an exploration area ([slides 2](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-2), [3](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-3), [6](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-6)). The related canonical skill may apply if this means latent-state exchange; the deck does not describe the mechanism, so equivalence is not assumed. |

## Skills shown by sources

The entries describe methods or concepts in the presentation, not personal
skills or evidence of individual implementation.

| Skill or capability | Evidence status | Evidence |
|---|---|---|
| Planner/controller decomposition for robotic tasks | documented | Slide text assigns high-level task decisions to a planner and low-level actuator commands to a controller ([slides 2](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-2), [6](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-6)). |
| Multimodal, reward-oriented robotics framework | documented | The framework text lists camera views, coordinates, gripper forces, depth maps, and rewards for object proximity or pickup ([slide 6](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-6)). |
| VLM planning and OpenVLA step-to-action approach | documented | The roadmap explicitly proposes VLM-based step planning and using OpenVLA to convert steps into actions ([slide 3](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-3)). |
| Multi-robot coordination and latent-collaboration exploration | documented | Coordination of two or more robots and latent collaboration are named in the framework and roadmap; no implementation detail or result is established ([slides 3](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-3), [6](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-6)). |
| Individual role, contribution, or mastery | unknown | The title slide gives a name and DAI/DOTI affiliation text but assigns no individual responsibilities ([slide 1](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-1)). |

## User-reported contributions and outcomes

| Contribution | Evidence status | Notes |
|---|---|---|
| [Thought leadership in developing proposal for Agentic AI for Robotics](../skills/thought-leadership-in-agentic-ai-for-robotics-proposal.md) | user-reported | Supplied by the user; distinct from the deck's source-documented proposal content and not evidence of personal skill or mastery. |

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The deck proposes a multi-agent robotics architecture with a high-level planner, low-level controller, and observations/rewards for robotic operation. | documented | [Slides 2](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-2), [6](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-6). |
| Franka manipulation, Genesis experiments, primitive actions, VLM planning, OpenVLA action generation, RL alternatives, robot coordination, and SO100/Rover sim-to-real are completed deliverables. | unknown | They appear as roadmap ideas and alternatives, not completion reports ([slide 3](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-3)). |
| The deck proposes adaptive RL and lists VLM-based multi-robot implementation steps. | documented | [Slide 8](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-8); these are presented as a proposed workflow, not reported results. |
| The source establishes individual authors' roles, contributions, or personal mastery. | unknown | The title slide names Gaurav Adke and DAI/DOTI without assigning responsibilities ([slide 1](../sources/agents-robotics-20260226-agenticrobitic-v01-pptx.md#slide-1)). |

## Review state

All six know-how requirements are `user-confirmed`; this records project needs,
not personal skill or mastery. The separate contribution above is
`user-reported`, not source-documented. The source remains **needs review**
because embedded media and picture content were not visually inspected. No
technical performance results are asserted from the text extraction, and
personal role or mastery is not inferred from the deck.
