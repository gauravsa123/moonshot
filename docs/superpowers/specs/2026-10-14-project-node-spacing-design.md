# Project Node Spacing Design

## Goal

Move project nodes slightly farther from the center of the skill graph to
reduce crowding while preserving the existing force-directed layout.

## Approved design

Apply a small, ongoing radial outward force to each visible project node,
directed from the canvas center. Keep the force proportional to the layout's
existing simulation alpha so the adjustment remains gentle and fluid. Preserve
the existing center attraction, pairwise repulsion, edge springs, and all
non-project node behavior.

The change is limited to project-node spacing in
`scripts/skill_graph_template.html` and the regenerated
`wiki/skill-graph.html`. The Publications anchor and all relationship filters
remain unchanged. Record the graph update in `wiki/log.md`.

## Alternatives considered

- Initialize project nodes farther from the center: simple, but the force
  layout can subsequently pull them back.
- Increase repulsion among project nodes: reduces overlap, but does not
  consistently move the project cluster away from the center.
- Apply a gentle radial outward force: directly addresses the requested
  placement while retaining fluid movement; selected.

## Validation

Regenerate the standalone graph and inspect the resulting change. Per the
user's instruction, do not run tests or a code review.
