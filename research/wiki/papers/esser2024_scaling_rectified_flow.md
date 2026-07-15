---
type: paper
node_id: paper:esser2024_scaling_rectified_flow
title: "Scaling Rectified Flow Transformers for High-Resolution Image Synthesis"
authors: ["Patrick Esser", "Sumith Kulal", "Andreas Blattmann", "Rahim Entezari", "Jonas Müller", "Harry Saini", "Yam Levi", "Dominik Lorenz", "Axel Sauer", "Frederic Boesel", "Dustin Podell", "Tim Dockhorn", "Zion English", "Kyle Lacey", "Alex Goodwin", "Yannik Marek", "Robin Rombach"]
year: 2024
venue: "arXiv"
external_ids:
  arxiv: "2403.03206"
  doi: null
  s2: null
tags: []
added: 2026-07-15T04:12:36Z
---

# Scaling Rectified Flow Transformers for High-Resolution Image Synthesis

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

> Diffusion models create data from noise by inverting the forward paths of data towards noise and have emerged as a powerful generative modeling technique for high-dimensional, perceptual data such as images and videos. Rectified flow is a recent generative model formulation that connects data and noise in a straight line. Despite its better theoretical properties and conceptual simplicity, it is not yet decisively established as standard practice. In this work, we improve existing noise sampling techniques for training rectified flow models by biasing them towards perceptually relevant scales. Through a large-scale study, we demonstrate the superior performance of this approach compared to established diffusion formulations for high-resolution text-to-image synthesis. Additionally, we present a novel transformer-based architecture for text-to-image generation that uses separate weights for the two modalities and enables a bidirectional flow of information between image and text tokens, improving text comprehension, typography, and human preference ratings. We demonstrate that this architecture follows predictable scaling trends and correlates lower validation loss to improved text-to-image synthesis as measured by various metrics and human evaluations. Our largest models outperform state-of-the-art models, and we will make our experimental data, code, and model weights publicly available.

