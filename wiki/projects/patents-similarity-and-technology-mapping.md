---
id: patents-similarity-and-technology-mapping
type: project
title: Patent Similarity and Technology-to-Tire Mapping
aliases:
  - Patent Knowledge Mining
related:
  - ../sources/patents-patent-20201112-patents-study-v4-pptx.md
  - ../sources/patents-patent-twp-km-patent-similarity-v2-docx.md
  - ../sources/patents-patent-patent-study-summary-v1-docx.md
  - ../skills/patent-document-similarity-and-knowledge-mining.md
  - ../skills/nlp-preprocessing-for-technical-and-patent-text.md
  - ../skills/bag-of-words-tfidf-and-cosine-similarity-for-retrieval.md
  - ../skills/word-and-document-embeddings-for-patent-similarity.md
  - ../skills/comparative-evaluation-of-document-similarity-methods.md
  - ../skills/section-aware-patent-similarity.md
  - ../skills/scalable-similarity-for-large-patent-corpora.md
  - ../skills/patent-clustering-and-technology-component-mapping.md
  - ../skills/patent-keyword-extraction-and-domain-dictionary-construction.md
  - ../skills/patent-landscape-network-visualization.md
  - ../skills/natural-language-invention-to-patent-retrieval.md
  - ../skills/translating-nlp-research-into-patent-analysis-prototypes.md
source_refs:
  - ../sources/patents-patent-20201112-patents-study-v4-pptx.md#slide-1
  - ../sources/patents-patent-twp-km-patent-similarity-v2-docx.md#patent-corpus-and-experiments
  - ../sources/patents-patent-patent-study-summary-v1-docx.md#patent-use-cases
---

# Patent Similarity and Technology-to-Tire Mapping

## Project summary

Three sources cover patent text similarity and a related technology-to-tire
component mapping use case. Two overlapping technical documents compare
bag-of-words and TF-IDF baselines with GloVe, Word2Vec, and Doc2Vec
representations on an AI-and-tire patent corpus. They describe query-patent
similarity, section-level comparisons, patent-landscape network plots, and
matching invention text to patents. A short presentation separately outlines
extracting technology and tire-domain terms and grouping patents to support
technology/component mapping.

The technical documents report different corpus totals (4,115 and 4,116) in
their own sections. The brief mapping presentation is marked work in progress;
the sources do not establish that it was a completed implementation of the
technical similarity study.

## Sources

- [Technology vs. Tire Component Mapping POC](../sources/patents-patent-20201112-patents-study-v4-pptx.md) — **needs review**; 2 slides and 14 media items.
- [A Knowledge Mining Approach to Patents: Similarity Applications](../sources/patents-patent-twp-km-patent-similarity-v2-docx.md) — **needs review**; 171 non-empty paragraphs and 13 media items.
- [Overview of Knowledge Mining in Patents: Similarity Applications](../sources/patents-patent-patent-study-summary-v1-docx.md) — **needs review**; 185 non-empty paragraphs and 12 media items.

## Know-how needed

These are suggested project requirements pending user review. They describe
project needs, not personal experience, skill, or mastery.

| Skill | Review status | Rationale |
|---|---|---|
| [Patent document similarity and knowledge mining](../skills/patent-document-similarity-and-knowledge-mining.md) | user-confirmed | The documents frame semantic and lexical similarity over patent collections as the central use case ([objective](../sources/patents-patent-twp-km-patent-similarity-v2-docx.md#author-and-objective)). |
| [NLP preprocessing for technical and patent text](../skills/nlp-preprocessing-for-technical-and-patent-text.md) | user-confirmed | The sources detail tokenization, normalization, stop-word handling, stemming/lemmatization, and text cleanup, with cautions for technical terminology ([preprocessing](../sources/patents-patent-twp-km-patent-similarity-v2-docx.md#text-preprocessing)). |
| [Bag-of-words, TF-IDF, and cosine-similarity retrieval](../skills/bag-of-words-tfidf-and-cosine-similarity-for-retrieval.md) | user-confirmed | TF-IDF and cosine similarity are described as a baseline for document vectors and query-patent search ([TF-IDF baseline](../sources/patents-patent-twp-km-patent-similarity-v2-docx.md#bag-of-words-and-tf-idf)). |
| [Word/document embeddings and domain adaptation for patent similarity](../skills/word-and-document-embeddings-for-patent-similarity.md) | user-confirmed | GloVe, Word2Vec, and Doc2Vec experiments include patent-specific and general-domain embeddings, with domain generalization limits discussed ([embedding methods](../sources/patents-patent-twp-km-patent-similarity-v2-docx.md#word-and-document-embeddings); [observations](../sources/patents-patent-twp-km-patent-similarity-v2-docx.md#method-comparison-and-observations)). |
| [Comparative evaluation of document-similarity methods](../skills/comparative-evaluation-of-document-similarity-methods.md) | user-confirmed | Similar patents from several methods are compared against a baseline by overlap and query results; assessments are qualitative in the source ([comparison](../sources/patents-patent-twp-km-patent-similarity-v2-docx.md#method-comparison-and-observations)). |
| [Section-aware patent similarity using claims and descriptions](../skills/section-aware-patent-similarity.md) | user-confirmed | The documents compare claims and descriptions and explain their different roles in conveying exact scope versus context ([patent-section comparison](../sources/patents-patent-twp-km-patent-similarity-v2-docx.md#similarity-by-patent-section)). |
| [Scalable vectorized similarity for large patent corpora](../skills/scalable-similarity-for-large-patent-corpora.md) | user-confirmed | The sources note compute and inference constraints and describe vectorized matrix multiplication for cosine similarity ([limitations](../sources/patents-patent-twp-km-patent-similarity-v2-docx.md#limitations-and-scaling)). |
| [Patent clustering and technology/component mapping](../skills/patent-clustering-and-technology-component-mapping.md) | user-confirmed | The short POC proposes document vectors and clusters to derive technology and tire-domain groupings ([mapping use case](../sources/patents-patent-20201112-patents-study-v4-pptx.md#slide-2)). |
| [Patent keyword extraction and domain-dictionary construction](../skills/patent-keyword-extraction-and-domain-dictionary-construction.md) | user-confirmed | The mapping presentation calls for extracting unique technology and tire terms; the technical documents identify keyword extraction as a use case ([mapping objectives](../sources/patents-patent-20201112-patents-study-v4-pptx.md#slide-1); [future work](../sources/patents-patent-patent-study-summary-v1-docx.md#patent-use-cases)). |
| [Patent-landscape network visualization](../skills/patent-landscape-network-visualization.md) | user-confirmed | The documents describe plotting patents as a similarity network and filtering edges by similarity thresholds ([landscape and query use cases](../sources/patents-patent-twp-km-patent-similarity-v2-docx.md#patent-use-cases)). |
| [Natural-language invention-to-patent retrieval](../skills/natural-language-invention-to-patent-retrieval.md) | user-confirmed | A POC compares free-text invention descriptions to patent claims and notes that keyword methods may improve it ([invention-text query](../sources/patents-patent-twp-km-patent-similarity-v2-docx.md#patent-use-cases)). |
| [Translating NLP research into patent-analysis prototypes](../skills/translating-nlp-research-into-patent-analysis-prototypes.md) | user-confirmed | The sources describe POC use cases and future Python/Power BI app work, while implementation and maturity boundaries remain distinct ([POCs](../sources/patents-patent-twp-km-patent-similarity-v2-docx.md#patent-use-cases); [future work](../sources/patents-patent-twp-km-patent-similarity-v2-docx.md#future-work)). |

## Skills shown by sources

These entries describe source content, not personal mastery or individual
implementation responsibility.

| Skill | Evidence status | Evidence |
|---|---|---|
| [Patent document similarity and knowledge mining](../skills/patent-document-similarity-and-knowledge-mining.md) | documented | The document describes a patent-similarity study and query-based POC ([objective](../sources/patents-patent-twp-km-patent-similarity-v2-docx.md#author-and-objective); [use cases](../sources/patents-patent-twp-km-patent-similarity-v2-docx.md#patent-use-cases)). |
| [NLP preprocessing for technical and patent text](../skills/nlp-preprocessing-for-technical-and-patent-text.md) | documented | The document describes normalization, tokenization, stemming/lemmatization, and other preprocessing methods ([preprocessing](../sources/patents-patent-twp-km-patent-similarity-v2-docx.md#text-preprocessing)). |
| [Bag-of-words, TF-IDF, and cosine-similarity retrieval](../skills/bag-of-words-tfidf-and-cosine-similarity-for-retrieval.md) | documented | TF-IDF and cosine similarity are described and used as a patent-similarity baseline ([baseline](../sources/patents-patent-twp-km-patent-similarity-v2-docx.md#bag-of-words-and-tf-idf)). |
| [Word/document embeddings and domain adaptation for patent similarity](../skills/word-and-document-embeddings-for-patent-similarity.md) | documented | GloVe, Word2Vec, and Doc2Vec approaches and domain-specific variants are compared ([embeddings](../sources/patents-patent-twp-km-patent-similarity-v2-docx.md#word-and-document-embeddings); [comparison](../sources/patents-patent-twp-km-patent-similarity-v2-docx.md#method-comparison-and-observations)). |
| [Comparative evaluation of document-similarity methods](../skills/comparative-evaluation-of-document-similarity-methods.md) | documented | The source reports qualitative comparisons of retrieved patent sets against a baseline ([comparison](../sources/patents-patent-twp-km-patent-similarity-v2-docx.md#method-comparison-and-observations)). |
| [Section-aware patent similarity using claims and descriptions](../skills/section-aware-patent-similarity.md) | documented | The document compares claims and descriptions as separate similarity inputs ([section comparison](../sources/patents-patent-twp-km-patent-similarity-v2-docx.md#similarity-by-patent-section)). |
| [Scalable vectorized similarity for large patent corpora](../skills/scalable-similarity-for-large-patent-corpora.md) | documented | The source discusses scaling constraints and reports vectorized matrix multiplication for cosine calculations ([scaling](../sources/patents-patent-twp-km-patent-similarity-v2-docx.md#limitations-and-scaling)). |
| [Patent-landscape network visualization](../skills/patent-landscape-network-visualization.md) | documented | The source describes plotting patent similarities as a NetworkX graph ([use cases](../sources/patents-patent-twp-km-patent-similarity-v2-docx.md#patent-use-cases)). |
| [Natural-language invention-to-patent retrieval](../skills/natural-language-invention-to-patent-retrieval.md) | documented | The source describes matching free-text invention descriptions to patent claims ([use cases](../sources/patents-patent-twp-km-patent-similarity-v2-docx.md#patent-use-cases)). |

## Attribution and scope uncertainty

| Claim | Status | Evidence |
|---|---|---|
| The documents list Gaurav Adke as author/preparer. | documented | [Technical document](../sources/patents-patent-twp-km-patent-similarity-v2-docx.md#author-and-objective); [overview](../sources/patents-patent-patent-study-summary-v1-docx.md#document-objective). |
| The source credits establish which individual implemented each method or POC. | unknown | The documents do not allocate method-level responsibilities; the mapping deck is marked work in progress. |
| All reported corpus sizes and similarity results are internally consistent and independently reproduced. | unknown | The summary reports both 4,115 and 4,116 patents in different sections; figures/media remain unreviewed and no reproduction was performed. |
| The technology/tire mapping POC and the document-similarity study are one completed implementation. | unknown | The sources cover related use cases but do not establish their implementation lineage or completion. |

## User-reported contributions and outcomes

| Contribution or outcome | Status | Details |
|---|---|---|
| White paper publication | user-reported | The user identified this as a project outcome; publication venue/date and personal role were not specified. |

## Review state

Text was extracted from all three sources: the PPTX has two slides and 14
media items; the DOCX files have 171 and 185 non-empty paragraphs and 13 and
12 media items, respectively. Media and figures remain uninspected. The
technical documents substantially overlap but are not identical; their
reported patent totals differ. Twelve know-how candidates await user review.
