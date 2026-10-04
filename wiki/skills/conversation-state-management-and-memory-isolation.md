---
id: conversation-state-management-and-memory-isolation
type: skill
title: Conversation-state management and memory isolation for agents
aliases: []
related:
  - context-compression.md
source_refs:
  - ../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#context-management
  - ../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#speaker-notes
---

# Conversation-state management and memory isolation for agents

Managing durable conversation context separately from transient execution
state, retries, errors, and database results.

## Projects needing this skill

- [Value Mate Pricing Copilot](../projects/pricing-value-mate-pricing-copilot.md) — user-confirmed project requirement.

## Projects with user-reported use

- None recorded.

## Projects showing this skill

- [Value Mate Pricing Copilot](../projects/pricing-value-mate-pricing-copilot.md) — the design separates a durable conversation from a disposable SQL worker and describes checkpoints and scoped memory ([context](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#context-management); [speaker notes](../sources/pricing-value-mate-20260908-doti-agentix-valuemate-pptx.md#speaker-notes)).
