---
type: paper
node_id: paper:liu2026_consistencypreserving_diverse_video
title: "Consistency-Preserving Diverse Video Generation"
authors: ["Xinshuang Liu", "Runfa Blark Li", "Truong Nguyen"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2602.15287"
  doi: null
  s2: null
tags: []
added: 2026-07-15T04:16:22Z
---

# Consistency-Preserving Diverse Video Generation

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

> Text-to-video generation is expensive, so only a few samples are typically produced per prompt. In this low-sample regime, maximizing the value of each batch requires high cross-video diversity. Recent methods improve diversity for image generation, but for videos they often degrade within-video temporal consistency and require costly backpropagation through a video decoder. We propose a joint-sampling framework for flow-matching video generators that improves batch diversity while preserving temporal consistency. Our approach applies diversity-driven updates and then removes only the components that would decrease a temporal-consistency objective. To avoid image-space gradients, we compute both objectives with lightweight latent-space models, avoiding video decoding and decoder backpropagation. Experiments on a state-of-the-art text-to-video flow-matching model show diversity close to strong joint-sampling baselines while substantially improving temporal consistency and color naturalness. Our code is available at https://github.com/XinshuangL/Diverse-Video.

