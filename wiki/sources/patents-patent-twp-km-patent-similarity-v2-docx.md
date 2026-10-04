---
id: patents-patent-twp-km-patent-similarity-v2-docx
type: source
title: A Knowledge Mining Approach to Patents: Similarity Applications
aliases: []
related:
  - ../projects/patents-similarity-and-technology-mapping.md
source_refs: []
---

# A Knowledge Mining Approach to Patents: Similarity Applications

- **Status:** needs review
- **Original path:** `raw/Patents/Patent/TWP_KM_Patent_Similarity_v2.docx`
- **Extraction:** Text extracted from 171 non-empty paragraphs; 13 media items are present.
- **Reason for review:** Figures/tables remain uninspected; reported comparisons are qualitative and have not been independently reproduced.
- **Original format:** Word document. The source under `raw/` was not modified.

## Summary

The document describes a proof-of-concept study of patent document similarity
using a corpus reported as 4,115 AI- and tire-domain patents. Methods include
TF-IDF/cosine similarity, GloVe, Word2Vec, Doc2Vec, and embedding vectors
weighted by TF-IDF. Examples compare query-patent results and patent sections,
then describe sorting, network-plot, and free-text invention-query use cases.

## Author and objective

### Objective and introduction

The document names Gaurav Adke and frames the work as an overview and
proof-of-concept comparison of text-similarity methods on patent documents.
It introduces vector-space document similarity and cosine closeness.

## Text preprocessing

### Preprocessing

The document discusses lowercasing, stop-word removal, stemming,
lemmatization, tokenization, number/punctuation handling, URL/HTML removal,
ASCII normalization, and vocabulary pruning. It cautions that aggressive
preprocessing may be inappropriate for technical terms and scientific texts.

## Methods and experiments

### Bag of words and TF-IDF

The document explains sparse binary/one-hot and n-gram representations,
TF-IDF weighting, normalization, and cosine similarity, including
bag-of-words limitations for word order and semantics.

### Word and document embeddings

It describes Word2Vec (CBOW and Skip-Gram), GloVe, and Doc2Vec, and compares
general and patent-domain pretrained embeddings. The experiment list also
includes TF-IDF-weighted embedding averages.

### Patent corpus and experiments

The document reports an Orbit corpus of 4,115 patents from AI and tire
domains. It compares TF-IDF, pretrained GloVe, patent-corpus Word2Vec,
pretrained patent Word2Vec, weighted embedding combinations, and Doc2Vec.
The examples use query patent 133 and compare claims and description text.

### Method comparison and observations

The document describes qualitative comparison using overlap among retrieved
patents and a TF-IDF/GloVe baseline. It reports that weighted embeddings
provided semantically useful results, while Doc2Vec scores were lower on the
available training corpus and broad-domain pretrained embeddings may not
generalize well to the technical domains. Figures and tables remain
unreviewed.

## Similarity by patent section

The document compares claims and descriptions across a subset reported as
1,634 patents. It characterizes claims as conveying the exact scope of an
innovation and descriptions as providing broader context and usability
information; further study of abstracts, inventors, citations, and other
sections is proposed.

## Limitations and scaling

The document discusses loss of context in TF-IDF, compute/inference cost for
large corpora, and Doc2Vec training-data requirements. It reports using
vectorized matrix multiplication to accelerate cosine calculations.

## Patent use cases

The proof-of-concept examples include sorting patents by similarity to a
query patent, visualizing a patent landscape as a NetworkX graph, and
retrieving patents related to free-text invention descriptions. The text-query
use case is identified as needing further improvement.

## Future work

The document proposes an MVP using a Python application or Power BI,
technology/tire-component mapping, and keyword extraction. These are future
directions, not evidence of completed product delivery.

## Review notes

The document lists Gaurav Adke as author but does not assign individual
responsibility for each experiment. Embedded figures and result tables remain
uninspected; comparisons have not been independently reproduced.
