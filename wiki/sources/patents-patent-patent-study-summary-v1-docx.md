---
id: patents-patent-patent-study-summary-v1-docx
type: source
title: Overview of Knowledge Mining in Patents: Similarity Applications
aliases: []
related:
  - ../projects/patents-similarity-and-technology-mapping.md
source_refs: []
---

# Overview of Knowledge Mining in Patents: Similarity Applications

- **Status:** needs review
- **Original path:** `raw/Patents/Patent/patent_study_summary_v1.docx`
- **Extraction:** Text extracted from 185 non-empty paragraphs; 12 media items are present.
- **Reason for review:** Figures/tables remain uninspected; reported comparisons are qualitative and have not been independently reproduced.
- **Original format:** Word document. The source under `raw/` was not modified.

## Summary

This overview substantially overlaps the longer patent-similarity document.
It describes NLP preprocessing, TF-IDF/cosine similarity, Word2Vec, GloVe,
Doc2Vec, a patent corpus, query-based comparisons, section-aware similarity,
and proof-of-concept retrieval/landscape visualizations. It reports both
4,115 and 4,116 patents in different sections.

## Document objective

The document is prepared by Gaurav Adke and scopes the work as finding
patents by document similarity. It summarizes NLP preprocessing and document
vector representations.

## Methods and experiments

### Text preparation and vector methods

The overview discusses standard NLP preprocessing and bag-of-words/TF-IDF,
cosine similarity, Word2Vec, GloVe, and Doc2Vec representations.

### Patent corpus and method comparison

The overview reports an Orbit corpus of 4,115 patents from AI and tire
domains, then describes a comparison of general-domain and patent-domain
embeddings, TF-IDF, and Doc2Vec. It gives examples of query patent results
and compares claims with detailed descriptions.

### Similarity results and limitations

The document reports embedding methods as more semantically meaningful than
bag-of-words baselines and discusses corpus-size/generalization and runtime
limitations. Its tables and media have not been inspected, so results remain
source-reported only.

## Patent use cases

The overview describes sorting patents against a reference patent,
visualizing patent similarity networks, and matching free-text invention
descriptions to patent claims. It also names technology/tire-component
mapping and a data application/dashboard as future work.

## Review notes

The document's learning summary refers to 4,116 patents, while its corpus
description says 4,115. This internal difference is preserved for review.
It names Gaurav Adke as preparer but does not allocate individual method or
implementation responsibility. The 12 embedded media items and reported
results remain unreviewed.
