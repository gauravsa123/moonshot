# Project Node Spacing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Nudge project nodes slightly outward from the center to reduce crowding while retaining the existing force-directed layout.

**Architecture:** Add a weak radial force to project nodes inside the existing center-force branch in the HTML graph template. Preserve all existing springs, repulsion, non-project behavior, filters, and the Publications anchor, then regenerate the standalone graph and log the change.

**Tech Stack:** Inline JavaScript in `scripts/skill_graph_template.html`, Python graph generator, Markdown maintenance log.

---

### Task 1: Add gentle outward spacing for project nodes

**Files:**
- Modify: `scripts/skill_graph_template.html` in `forceTick()`
- Generate: `wiki/skill-graph.html` using `scripts/build_skill_graph.py`
- Modify: `wiki/log.md`

- [x] **Step 1: Add a weak outward force to project nodes**

In `forceTick()`, keep the Publications anchor branch unchanged. In the
non-publication branch, apply a small outward force to projects before the
existing center attraction:

```js
    } else {
      const centerX = width / 2;
      const centerY = height / 2;
      if (node.type === "project") {
        node.vx += (node.x - centerX) * .00008 * alpha;
        node.vy += (node.y - centerY) * .00008 * alpha;
      }
      node.vx += (centerX - node.x) * .0004 * alpha;
      node.vy += (centerY - node.y) * .0004 * alpha;
    }
```

The outward component slightly counteracts center attraction only for project
nodes; keep all existing damping and position updates unchanged.

- [x] **Step 2: Regenerate the standalone graph**

Run:

```bash
python3 scripts/build_skill_graph.py
```

Expected: the command completes successfully and updates
`wiki/skill-graph.html` from the modified template. Do not run tests or a code
review, as requested.

- [x] **Step 3: Record the visual adjustment**

Append a dated `2026-10-14` entry to `wiki/log.md` describing the project-node
outward bias, graph regeneration, and unchanged non-project behavior. Preserve
all existing log entries.

- [x] **Step 4: Inspect the focused diff**

Run:

```bash
git diff -- scripts/skill_graph_template.html wiki/skill-graph.html wiki/log.md
```

Confirm the only graph behavior change is the project-only radial bias, the
generated graph contains the matching template update, and the log entry
matches the actual change. Do not commit or push.
