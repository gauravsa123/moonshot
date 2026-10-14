# Reset Selection Button Design

## Goal

Provide a visible control for clearing the active graph selection and returning
the details panel to its welcome state.

## Approved design

Add an always-available **Reset selection** button to the graph controls
toolbar, using the existing toolbar button styling. Route the button and the
Escape key through a shared reset helper that clears the selected node,
keyboard focus, hover highlight, and focus-neighbor highlighting, then
restores the welcome detail panel and redraws the graph.

Give the Reset selection button a light-blue background and blue-tinted
border, with theme-aware foreground/background colors that preserve text
contrast in dark mode. Do not change the appearance of other controls.

The reset does not change search text/results, relationship filters, zoom, or
pan. Pressing it when no node is selected is safe and simply clears any
remaining focus or hover state.

Update `scripts/skill_graph_template.html`, regenerate
`wiki/skill-graph.html`, and record the change in `wiki/log.md`. Do not modify
the graph data or other node-selection behavior.

## Alternatives considered

- Place the button beside the Network heading: close to the canvas, but adds
  another item to the heading row.
- Place the button in the details panel: contextually close to selection
  information, but less discoverable as a graph-wide control.
- Place it in the graph controls toolbar: reuses the existing control styling
  and layout; selected.

## Validation

Regenerate the standalone graph and inspect the focused diff to confirm the
button and Escape key share the same reset behavior. Per the user's standing
instruction, do not run tests or a code review.
