---
id: patents-patent-20201112-patents-study-v4-pptx
type: source
title: Technology vs. Tire Component Mapping POC
aliases: []
related:
  - ../projects/patents-similarity-and-technology-mapping.md
source_refs: []
---

# Technology vs. Tire Component Mapping POC

- **Status:** needs review
- **Original path:** `raw/Patents/Patent/20201112_Patents_study_V4.pptx`
- **Extraction:** Text extracted from both slides; 2 speaker-note files and 14 media items are present.
- **Reason for review:** Media remain uninspected; the filename date and the slide's `01/04/2021` date do not align clearly, and the use case is explicitly marked work in progress.
- **Original format:** PowerPoint presentation. The source under `raw/` was not modified.

## Summary

The two-slide use case concerns mapping technologies to tire components from
patent text. It proposes extracting technology and tire-domain terms, counting
patents that contain term combinations, then generating document vectors and
clustering patents to derive technology/component groupings.

## Objectives

### Slide 1

The slide describes extracting technology keywords and tire-domain terms
from unstructured patent data, identifying unique terms, and counting patents
containing combinations. It labels the work in progress.

## Similarity and clustering

### Slide 2

The slide proposes creating patent document vectors, clustering similar
patents, and deriving lists of technologies and tire domains from the
clusters. It identifies domain-dictionary creation as a potential use.

## Review notes

The filename encodes `20201112`, while the first slide shows `01/04/2021`,
whose month/day order is ambiguous and conflicts with the filename date.
Individual authorship is not identified in the extracted slide text.
