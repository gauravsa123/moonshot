# Publications Node Outer Anchor Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Keep the Publications node visibly outside the project cluster while retaining slight force-directed motion.

**Architecture:** Add a responsive right-side anchor for the Publications node, vertically centered with its label facing inward. Exclude its authorship links from spring attraction and replace global centering for that node with a soft restoring force; retain repulsion and all other nodes' existing force behavior. Re-anchor when the canvas is resized and regenerate the standalone graph.

**Tech Stack:** Inline JavaScript/HTML and the existing Python graph generator.

---

### Task 1: Soft-anchor the Publications hub

**Files:**
- Modify: `scripts/skill_graph_template.html`
- Generate: `wiki/skill-graph.html`

- [x] **Step 1: Add the responsive outer anchor**

Define the anchor near the layout helpers:

```js
function publicationAnchorPoint() {
  return {x: width - 24, y: height / 2};
}
```

After `sizeCanvas()` initializes or adjusts the other node positions, place the
hub at that anchor and clear its velocity. This gives new graphs and resized
canvases a visible starting position. Align the Publications label to the
left from the right-side node by setting canvas `textAlign` to `"right"` and
drawing it at `node.x - radius - 5`.

- [x] **Step 2: Preserve motion without pulling the hub into the cluster**

In the edge-spring loop in `forceTick()`, skip `publication_authorship` edges.
Keep the hub in pairwise repulsion, but do not apply center gravity to it.
Instead, apply a soft restoring force toward `publicationAnchorPoint()`:

```js
if (node.type === "publication") {
  const anchor = publicationAnchorPoint();
  node.vx += (anchor.x - node.x) * 0.006;
  node.vy += (anchor.y - node.y) * 0.006;
} else {
  node.vx += (width / 2 - node.x) * 0.0004 * alpha;
  node.vy += (height / 2 - node.y) * 0.0004 * alpha;
}
```

Keep the existing damping and position update after this branch. Do not alter
the Project or User-reported filters or the authored-work edge data.

- [x] **Step 3: Regenerate the standalone graph**

Run `python3 scripts/build_skill_graph.py` to regenerate
`wiki/skill-graph.html`. Do not run tests or code reviews, as explicitly
requested by the user. Do not commit or push.
