---
id: masternaut-can-bus-reverse-engineering
type: project
title: Masternaut CAN-Bus Reverse Engineering with Deep Learning
short_title: CAN-Bus
aliases:
  - CAN Reversing
related:
  - ../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md
  - ../skills/cnn-based-representation-of-non-image-one-dimensional-signals.md
source_refs:
  - ../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slide-3
  - ../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-8-10
  - ../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-25-28
  - ../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-25-28
---

# Masternaut CAN-Bus Reverse Engineering with Deep Learning

## Project summary

The presentation describes a deep-learning approach to identify vehicle
signals in encoded CAN-bus logs and infer unknown signal bit positions and
lengths. It converts candidate bit windows, endianness, and signedness into
interpretive-convolution features; classifies signal patterns; addresses
extreme class imbalance; and applies masking and continuity-based scoring to
recover candidate decodings. It also discusses topological features, CNN
embeddings, data scaling, and memory-efficient dataset generation.

The 30-slide deck contains reported classification and decoding results, but
its 72 embedded media items have not been visually inspected and the results
have not been independently reproduced.

## Sources

- [CAN bus reversing using deep learning](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md) — **needs review**; text extracted from 30 slides, 72 media items remain uninspected.

## Know-how needed

These requirements distinguish suggestions that remain pending from a
user-confirmed project need. They describe project needs, not personal
experience, skill, or mastery.

| Skill requirement | Status | Rationale |
|---|---|---|
| Vehicle CAN protocol analysis and signal reverse engineering | suggested | The task identifies signal meanings and decodes OEM-encoded vehicle CAN data ([context](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slide-3); [manual decoding](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-4-7)). |
| CAN-log preprocessing and bit-level signal representation | suggested | The workflow converts hexadecimal records using candidate bit starts, lengths, endianness, and signedness ([decoding setup](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-4-7); [features](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-8-10)). |
| Interpretive-convolution feature engineering for unknown CAN layouts | suggested | Multiple convolution windows and bit-layout permutations produce a 716-value feature representation ([feature construction](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-8-10)). |
| Sequence-model classification of CAN signals | suggested | The deck describes LSTM classification over 100-timestep windows and also evaluates CNN representations ([LSTM input](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-8-10); [CNN models](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-19-21)). |
| Class-imbalance mitigation for rare vehicle-signal detection | suggested | A target signal may be one positive class against many negative CAN IDs; the deck discusses several balancing measures ([imbalance](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-11-17)). |
| Wavelet and correlation methods for filtering improbable negative samples | suggested | Wavelet coefficients and cross-correlation are proposed to remove dissimilar negative examples; the deck reports filtering up to 60% ([wavelet filtering](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-11-17)). |
| Minority-class augmentation with temporal transforms and generative models | suggested | Temporal shifts/flips and diffusion-based generation are described for minority-signal data augmentation ([augmentation](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-11-17)). |
| Recall-oriented threshold selection and imbalanced-class evaluation | suggested | The presentation explicitly chooses thresholds to preserve recall and shows thresholded signal-classification examples ([results](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-11-17); [thresholded results](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-19-21)). |
| Topological data analysis for signal-feature comparison | suggested | The deck proposes comparing topological features and persistence diagrams to the original signal representation ([topological analysis](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-11-17)). |
| Scalable TensorFlow input pipelines for large signal datasets | suggested | A dataset generator is used to stream batches for a dataset said to reach 138,000 samples, with memory use and class weighting discussed ([dataset generator](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-22-24)). |
| Per-signal statistical scaling for time-series features | suggested | Per-arbitration-ID feature statistics are stored and used to scale values across time steps ([scaling](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-22-24)). |
| Progressive masking and probability maps for CAN bit-boundary inference | suggested | The deck reuses a classifier under progressive masking to identify likely start and end bits ([masking](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-25-28)). |
| Candidate-decoding scoring using continuity and switching behavior | suggested | Candidate decoded curves are ranked using continuity and switch-rate measures ([candidate scoring](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-25-28)). |
| CNN transfer features and embedding visualization for CAN signals | suggested | The deck treats convolution features as images, compares pretrained ResNet/VGG features, and shows t-SNE plots ([CNN embeddings](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-19-21)). |
| [CNN-based representation of non-image one-dimensional signals](../skills/cnn-based-representation-of-non-image-one-dimensional-signals.md) | user-confirmed | The user grouped CNN use outside image domains with representing one-dimensional signals as CNN input; the deck describes treating signal features as images and comparing pretrained CNN representations ([CNN models](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-19-21)). |

## Skills shown by sources

These entries describe methods and claims present in the presentation, not
personal skill or individual implementation contribution.

| Capability | Evidence status | Evidence |
|---|---|---|
| The workflow targets CAN signal identification and bit-layout recovery from encoded vehicle logs. | documented | [Problem and manual decoding](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slide-3); [two-stage task](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-25-28). |
| Interpretive convolutions enumerate candidate bit layouts to create signal features for a sequence classifier. | documented | [Feature construction](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-8-10). |
| Imbalance handling, data augmentation, and recall-oriented thresholds are discussed for rare signal classification. | documented | [Imbalance and filtering](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-11-17); [augmentation and thresholds](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-19-21). |
| Start/end-bit candidates are ranked using probability maps and signal-shape scores. | documented | [Masking and scoring](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-25-28). |
| CNN models are explored on image-like representations of one-dimensional CAN signal features. | documented | [CNN models](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slides-19-21). |

## Attribution and scope uncertainty

| Claim | Status | Evidence |
|---|---|---|
| The user is credited by name on the presentation cover. | documented | [Title slide](../sources/masternaut-can-20230527-can-reverse-dldc-pptx.md#slide-1). |
| The cover attribution establishes which individual implemented each method or result. | unknown | The presentation does not allocate individual responsibilities. |
| Reported classification, filtering, or decoding results have been independently reproduced. | unknown | Figures remain unreviewed and no independent reproduction was performed. |

## User-reported contributions and outcomes

No personal contributions or outcomes have been user-reported for this
project.

## Review state

Text was extracted from all 30 slides. The deck contains 21 speaker-note files,
two of which include additional reference/context text, and 72 embedded media
items that remain uninspected. Reported classification and bit-decoding
results have not been reproduced. The user chose to retain the original 14
requirements as suggestions, grouped two related CNN ideas into one
requirement, and confirmed that added requirement. No personal implementation
claim is made.
