---
id: ai-for-engg-point-cloud-v01-part-constraints-pptx
type: source
title: Point Cloud part constraints presentation
aliases: []
related:
  - ../projects/ai-for-engg-point-cloud.md
source_refs: []
---

# Point Cloud part constraints presentation

- **Status:** needs review
- **Original path:** `raw/AI for Engg/Point Cloud/v01_part_constraints.pptx`
- **Readability:** Text was extracted locally from all 11 slides, and a Keynote PDF re-render and contact-sheet visual review covered all slides. Nine notes-slide files contain only slide-number text; no substantive speaker notes were found.
- **Reason for review:** The visual pass confirmed the contact-constraint diagrams, VAE/critic and attention proposals, and before/after scaling plots, but exact plotted values and performance effects cannot be reliably read or reproduced. The slide 6 optimization notation remains ambiguous, and every slide footer identifies the reference subject as “GAN” with a 2020 creation date despite the Point Cloud title.
- **Original format:** PowerPoint, 11 slides. The source under `raw/` was not modified; no packages were installed and no external services were used.

## Summary

The presentation explores reconstructing point clouds with a VAE and adding constraints to make reconstructed multi-part geometry more coherent. It discusses shared MLPs in PointNet, contact-zone constraints based on fitted lines and distances, structural attributes such as symmetry/contact/length, a PointNet critic and adversarial loss, self-attention for learning relations, point-level contact descriptors, and coordinate scaling in the reconstruction loss. These are proposals and open questions in the deck, not evidence of a completed or validated system.

## Evidence

| Claim | Status | Evidence |
|---|---|---|
| The presentation describes a point-cloud reconstruction approach using a VAE. | documented | [Slide 2](#slide-2). |
| It explains PointNet's shared MLP as applying the same learned mapping to each point, independent of point ordering. | documented | [Slide 3](#slide-3). |
| It proposes restricting contact constraints to relevant points and discusses rigid-part versus point-level optimization. | documented | [Slides 5](#slide-5) and [6](#slide-6). |
| It proposes fitting lines or polynomials to part edges and constraining their distance within tolerances, with contact-zone point coordinates as decision variables. | documented | [Slide 6](#slide-6). |
| It proposes using symmetry, contact, and length relations as structural attributes for actor-critic training. | documented | [Slide 7](#slide-7). |
| It proposes a PointNet-based critic and an adversarial loss for decoder training; the deck explicitly says timing and effectiveness need testing. | documented | [Slide 8](#slide-8). |
| It considers self-attention for learning global point relations and a U-Net-based autoencoder with attention. | documented | [Slide 9](#slide-9). |
| It suggests point-level contact indicators and contact-edge distance from the centroid as shape features. | documented | [Slide 10](#slide-10). |
| It describes coordinate-range variation as a scaling issue for XY reconstruction loss and proposes scaling inputs and outputs based on input geometry for loss calculation. | documented | [Slide 11](#slide-11). |
| Individual roles, implementation ownership, or personal mastery are established. | unknown | The readable title slide names “AI Squad, DCTI” but assigns no individual roles or skills ([slide 1](#slide-1)). |

## Slide references

### Slide 1

Title: “Point Cloud”; identifies “AI Squad, DCTI.” No individual role attribution is present. The footer says “Ref file/subject: GAN” and “Created on: 25/09/2020” throughout the deck; its relationship to the Point Cloud material is unresolved.

### Slide 2

States “Reconstruction” and “Reconstructed using VAE.”

### Slide 3

Explains shared MLPs in PointNet: the same MLP is applied to every point, sharing weights across points, while point ordering is irrelevant. The accompanying diagram compares pointwise MLP layers and a PointNet-style architecture.

### Slide 4

“Thank you.”

### Slide 5

Introduces contact constraints and Chamfer distance between points. It says only selected points should be considered for contact constraints, since other points will not be modified; box-level constraints are described in terms of centroid and size. Two alternatives are noted: rigidly moving the entire part or modifying the function to work with points.

### Slide 6

Proposes fitting lines or polynomials to edges from two parts, using line distance with Shapely's `LineString.distance` to keep separation within tolerance. It suggests `numpy.polyfit` and identifies coordinates of contact-zone points as decision variables. Some notation in the slide is incomplete or ambiguous.

### Slide 7

Discusses latent constraints on a structural VAE. It proposes symmetry, contact, and length information as relation attributes for actor-critic training, based on an assumption that training reconstruction captures realism.

### Slide 8

Proposes a PointNet-based critic to estimate whether a point cloud is properly constrained and an adversarial loss to encourage more coherent decoder output. The slide suggests adding the loss after initial reconstruction learning and restricting it to decoder training, but marks the approach as needing tests and leaves a further optimization-as-adversarial-loss idea open.

### Slide 9

Explores self-attention for learning relations, including a U-Net-based autoencoder with attention layers and the idea that attention can learn global relations among input tokens. Several papers and a Point-Attention-Net repository are cited. The slide also plots training and validation accuracy, but the chart does not establish a reproducible comparative result.

### Slide 10

Poses the use of additional shape features to encode relations beyond part-level one-hot vectors. Suggestions include identifying which points share contact and measuring each point's contact-edge distance from a centroid for attention weighting.

### Slide 11

Describes a coordinate-scaling issue for parts positioned across different XY ranges: larger coordinate values can dominate MSE reconstruction loss. It notes that independently rescaling parts could interfere with integration, then proposes scaling inputs and outputs using the input geometry for loss calculation. The before/after plots visually show point-cloud shape comparisons, but the small axis labels and absent metric summary do not establish the quantitative effect.

## Open review questions

- What quantitative result, if any, do the slide 9 accuracy curves and slide 11 before/after plots represent? Their plotted values are not reliably legible and no metric summary is given.
- What are the exact geometric constraints and optimization behavior intended by the incomplete notation on slide 6?
- Were the adversarial and attention-based proposals implemented or tested beyond what is stated in the slides?
