# Requirement-Linked Skill Node Colors Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Color every skill node targeted by at least one project-requirement edge amber.

**Architecture:** Derive a set of requirement-target skill node IDs from the complete edge list, independent of active relationship filters. Use that set to choose the skill-node fill color, preserving blue project nodes, pink Publications, and purple non-required skills. Add a distinct legend marker for requirement-linked skill nodes and regenerate the standalone graph.

**Tech Stack:** Inline JavaScript, CSS, and the existing Python graph generator.

---

### Task 1: Color requirement-linked skill nodes

**Files:**
- Modify: `scripts/skill_graph_template.html`
- Generate: `wiki/skill-graph.html`

- [x] **Step 1: Derive requirement-linked skill IDs**

After initial `edges` are created, store the target IDs for edges whose
`kind` is `"requirement"`:

```js
let requirementSkillIds = new Set(
  edges.filter(edge => edge.kind === "requirement").map(edge => edge.target)
);
```

In `installGraphData()`, recompute `requirementSkillIds` immediately after
replacing `edges`, so dropped Markdown uses the same rule. Do not consult
`visibleEdges()` or the requirement filter; node colors stay stable when
filters are toggled.

- [x] **Step 2: Apply the node color and add a legend marker**

In `drawNode()`, keep the existing project and publication colors. For skill
nodes, select `--requirement` when `requirementSkillIds.has(node.id)` and
`--skill` otherwise. Keep requirement edges amber and dashed.

Add a round amber legend swatch labeled **Project-required skill**, visually
distinct from the existing dashed requirement-edge swatch.

- [x] **Step 3: Regenerate the standalone graph**

Run `python3 scripts/build_skill_graph.py` to regenerate
`wiki/skill-graph.html`. Do not run tests or code reviews, as explicitly
requested by the user. Do not commit or push.
