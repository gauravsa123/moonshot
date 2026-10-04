# Source Evidence Visibility Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Remove the Source evidence filter while showing evidence edges only between nodes surfaced by the remaining relationship toggles.

**Architecture:** Keep source-evidence data intact. First derive the endpoint set from currently enabled non-evidence edges, then include evidence edges only when both endpoints are in that set. This preserves search/selection node visibility without letting evidence edges introduce additional nodes.

**Tech Stack:** Inline JavaScript/HTML and the existing Python graph generator.

---

### Task 1: Remove the source-evidence toggle

**Files:**
- Modify: `scripts/skill_graph_template.html`
- Generate: `wiki/skill-graph.html`

- [x] **Step 1: Remove the checkbox and conditionally expose evidence edges**

Remove only the Source evidence checkbox; preserve User-reported and Project
requirements checkboxes. Replace `visibleEdges()` with:

```js
function visibleEdges() {
  const enabledEdges = edges.filter(edge => {
    if (edge.kind === "source_evidence") return false;
    const filterName = edge.kind === "publication_authorship" ? "user_reported" : edge.kind;
    return filters[filterName]?.checked;
  });
  const enabledNodeIds = new Set();
  for (const edge of enabledEdges) {
    enabledNodeIds.add(edge.source);
    enabledNodeIds.add(edge.target);
  }
  const visible = new Set([
    ...enabledEdges,
    ...edges.filter(edge => edge.kind === "source_evidence"
      && enabledNodeIds.has(edge.source)
      && enabledNodeIds.has(edge.target)),
  ]);
  return edges.filter(edge => visible.has(edge));
}
```

Do not remove source-evidence edges from graph data or detail panels. With this
rule, the two skills connected only by source evidence remain hidden unless
search or selection brings their nodes into view; their evidence edges do not
appear from search or selection alone.

- [x] **Step 2: Regenerate the standalone graph**

Run `python3 scripts/build_skill_graph.py` to regenerate
`wiki/skill-graph.html`. Do not run tests or code reviews, as explicitly
requested by the user. Do not commit or push.
