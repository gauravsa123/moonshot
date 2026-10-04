---
id: janus-knowledge-sharing-20220309-rl-kss-1-pptx
type: source
title: Reinforcement Learning knowledge-sharing presentation
aliases: []
related:
  - ../projects/janus-knowledge-sharing-reinforcement-learning-and-dqn.md
source_refs: []
---

# Reinforcement Learning knowledge-sharing presentation

- **Status:** needs review
- **Original path:** `raw/Janus/Knowledge Sharing/20220309_RL_KSS_1.pptx`
- **Extraction:** Text was extracted from all 31 slides. The file contains 61
  embedded media items and 13 speaker-note files; five note files contain
  external resource links.
- **Reason for review:** Embedded media and diagrams remain uninspected, later
  slides include sparse or placeholder-like extracted text, and the filename
  date (2022-03-09) conflicts with the cover-slide date (16 January 2023).
- **Original format:** PowerPoint. The source under `raw/` was not modified.

## Summary

The deck introduces reinforcement learning (RL), Markov decision processes,
model-based versus model-free methods, deep RL, and value-based learning. Its
DQN section covers Q-learning, Q-value estimation, epsilon-greedy exploration,
experience replay, and a target network, with CartPole as the example
environment. It also surveys reward-design pitfalls, application areas, and
image-based RL tasks. The deck includes learning-resource links and a Google
Colab URL, but the referenced notebook and embedded visual material were not
inspected.

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The deck explains RL terminology, model-based/model-free approaches, and MDP elements. | documented | [Slides 4](#slide-4), [5](#slide-5), [10](#slide-10), and [11](#slide-11). |
| Deep RL and DQN are introduced with value estimation, Q-learning, epsilon-greedy exploration, experience replay, and a target network. | documented | [Slides 12](#slide-12) and [20](#slide-20)–[24](#slide-24). |
| Reward design can produce unintended behavior when penalties and rewards are imbalanced. | documented | [Slide 18](#slide-18); the examples and visuals remain unreviewed. |
| The deck discusses image-based RL and computer-vision tasks, including localization, tracking, detection, and registration. | documented | [Slides 13](#slide-13)–[16](#slide-16) and [31](#slide-31). |
| A DQN demo was successfully run, or its training performance was measured. | unknown | A demo and Colab URL are mentioned, but the notebook, embedded material, and quantitative results were not inspected. |
| The user personally presented or authored the material. | unknown | The cover lists “Gaurav Adke,” but the deck does not state an individual role or contribution. |
| The presentation took place on a specific date. | unknown | The filename includes `20220309`, while the cover says “16th January, 2023.” |

## Slide references

### Slide 1

Title slide: “Reinforcement Learning,” “Gaurav Adke,” and “16th January,
2023.” This date conflicts with the date-like prefix in the source filename.

### Slide 2

Lists the talk outline: RL concepts and examples, practical applications,
algorithms, deep RL, learning resources, image-domain RL, and a DQN demo.

### Slide 3

Classifies supervised and unsupervised learning as data-driven and RL as
task-driven learning from mistakes.

### Slide 4

Defines RL as learning through interaction with an environment to maximize a
reward signal over a sequence of decisions.

### Slide 5

Defines agent, state, action, environment, reward, policy, and value.

### Slide 6

Mentions RL from human feedback (RLHF) in connection with ChatGPT and links to
an online article.

### Slide 7

Uses CartPole to illustrate state variables, actions, reward, and environment;
also lists Mountain Car, Breakout, and robot pick-and-drop examples.

### Slide 8

Links to an OpenAI article about emergent tool use.

### Slide 9

Surveys proposed RL applications in industrial automation, autonomous driving,
marketing and bidding, aircraft and robot control, games, energy optimization,
healthcare, and finance.

### Slide 10

Contrasts model-based RL, where environment dynamics are known and planning is
possible, with model-free RL, which learns from interaction and exploration.

### Slide 11

Introduces the Markov decision process, its state and action sets, transition
probabilities, rewards, discount factor, and state-action value.

### Slide 12

Explains deep RL as using neural networks to estimate action values when a
state-action table is impractical.

### Slide 13

Contrasts simulated environments with structured variables against image-based
environments using CNN-based agents.

### Slide 14

Lists games, robotics, and autonomous driving as image-based RL environments.

### Slide 15

Lists object localization, tracking, and detection as RL/computer-vision tasks.

### Slide 16

Shows image registration and image transformations as RL/computer-vision tasks.

### Slide 17

Contains the heading “RL Algorithms”; details may be present only in the
unreviewed media.

### Slide 18

Discusses reward design, optimization objectives, penalties, episode
termination, and unintended behavior from misaligned rewards.

### Slide 19

Lists learning resources, including David Silver's RL lectures, Sutton and
Barto's book, a deep-RL bootcamp, OpenAI Spinning Up, and debugging resources.

### Slide 20

Introduces Q-learning and a Q-table through repeated play and state-action
value examples.

### Slide 21

Explains the table-size problem in large environments and proposes a neural
network to model Q-values.

### Slide 22

Describes greedy and epsilon-greedy action selection.

### Slide 23

Describes experience replay and a target network for DQN training.

### Slide 24

Labels a DQN algorithm and links to Gym and a Google Colab notebook. The
notebook was not opened or evaluated.

### Slide 25

Describes the CartPole actions, state variables, reward, and environment.

### Slide 26

“Thank You.”

### Slide 27

“RL Demo”; extracted text does not describe the demo.

### Slide 28

“RL Applications” with a single extracted character; visual content remains
unreviewed.

### Slide 29

Contains sparse extracted text (“Reinforcement Learning” and “z”); visual
content remains unreviewed.

### Slide 30

Mentions an explanation of the RL Q-table training process.

### Slide 31

“RL for CV” with links to computer-vision and RL references.

## Speaker-note references

Five of the 13 speaker-note files contain external links, including:

- [DeepSense AI: What is reinforcement learning?](https://deepsense.ai/what-is-reinforcement-learning-the-complete-guide/)
- [Neptune.ai: Reinforcement-learning applications](https://neptune.ai/blog/reinforcement-learning-applications)
- [Introduction to RL and Markov decision processes](https://towardsdatascience.com/introduction-to-reinforcement-learning-markov-decision-process-44c533ebf8da)
- [V7 Labs: Deep reinforcement learning guide](https://www.v7labs.com/blog/deep-reinforcement-learning-guide)
- [OpenAI Spinning Up: Key concepts in RL](https://spinningup.openai.com/en/latest/spinningup/rl_intro2.html)

These links were extracted from the notes; their contents were not independently
reviewed.
