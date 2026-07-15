---
type: paper
node_id: paper:satish2026_physvideogenerator_towards_physically
title: "PhysVideoGenerator: Towards Physically Aware Video Generation via Latent Physics Guidance"
authors: ["Siddarth Nilol Kundur Satish", "Devesh Jaiswal", "Hongyu Chen", "Abhishek Bakshi"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2601.03665"
  doi: null
  s2: null
tags: []
added: 2026-07-15T04:17:40Z
---

# PhysVideoGenerator: Towards Physically Aware Video Generation via Latent Physics Guidance

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

> Current video generation models produce high-quality aesthetic videos but often struggle to learn representations of real-world physics dynamics, resulting in artifacts such as unnatural object collisions, inconsistent gravity, and temporal flickering. In this work, we propose PhysVideoGenerator, a proof-of-concept framework that explicitly embeds a learnable physics prior into the video generation process. We introduce a lightweight predictor network, PredictorP, which regresses high-level physical features extracted from a pre-trained Video Joint Embedding Predictive Architecture (V-JEPA 2) directly from noisy diffusion latents. These predicted physics tokens are injected into the temporal attention layers of a DiT-based generator (Latte) via a dedicated cross-attention mechanism. Our primary contribution is demonstrating the technical feasibility of this joint training paradigm: we show that diffusion latents contain sufficient information to recover V-JEPA 2 physical representations, and that multi-task optimization remains stable over training. This report documents the architectural design, technical challenges, and validation of training stability, establishing a foundation for future large-scale evaluation of physics-aware generative models.

