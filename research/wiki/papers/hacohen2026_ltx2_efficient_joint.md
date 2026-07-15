---
type: paper
node_id: paper:hacohen2026_ltx2_efficient_joint
title: "LTX-2: Efficient Joint Audio-Visual Foundation Model"
authors: ["Yoav HaCohen", "Benny Brazowski", "Nisan Chiprut", "Yaki Bitterman", "Andrew Kvochko", "Avishai Berkowitz", "Daniel Shalem", "Daphna Lifschitz", "Dudu Moshe", "Eitan Porat", "Eitan Richardson", "Guy Shiran", "Itay Chachy", "Jonathan Chetboun", "Michael Finkelson", "Michael Kupchick", "Nir Zabari", "Nitzan Guetta", "Noa Kotler", "Ofir Bibi", "Ori Gordon", "Poriya Panet", "Roi Benita", "Shahar Armon", "Victor Kulikov", "Yaron Inger", "Yonatan Shiftan", "Zeev Melumian", "Zeev Farbman"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2601.03233"
  doi: null
  s2: null
tags: []
added: 2026-07-15T04:12:36Z
---

# LTX-2: Efficient Joint Audio-Visual Foundation Model

## One-line thesis
_TODO: fill in after reading._

## Problem / Gap
_TODO._

## Method
_TODO._

## Key Results
_TODO._

## Assumptions
_TODO._

## Limitations / Failure Modes
_TODO._

## Reusable Ingredients
_TODO._

## Open Questions
_TODO._

## Claims
_TODO._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
_TODO._

## Abstract (original)

> Recent text-to-video diffusion models can generate compelling video sequences, yet they remain silent -- missing the semantic, emotional, and atmospheric cues that audio provides. We introduce LTX-2, an open-source foundational model capable of generating high-quality, temporally synchronized audiovisual content in a unified manner. LTX-2 consists of an asymmetric dual-stream transformer with a 14B-parameter video stream and a 5B-parameter audio stream, coupled through bidirectional audio-video cross-attention layers with temporal positional embeddings and cross-modality AdaLN for shared timestep conditioning. This architecture enables efficient training and inference of a unified audiovisual model while allocating more capacity for video generation than audio generation. We employ a multilingual text encoder for broader prompt understanding and introduce a modality-aware classifier-free guidance (modality-CFG) mechanism for improved audiovisual alignment and controllability. Beyond generating speech, LTX-2 produces rich, coherent audio tracks that follow the characters, environment, style, and emotion of each scene -- complete with natural background and foley elements. In our evaluations, the model achieves state-of-the-art audiovisual quality and prompt adherence among open-source systems, while delivering results comparable to proprietary models at a fraction of their computational cost and inference time. All model weights and code are publicly released.

