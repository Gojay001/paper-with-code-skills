---
type: paper
node_id: paper:xi2025_sparse_videogen_accelerating
title: "Sparse VideoGen: Accelerating Video Diffusion Transformers with Spatial-Temporal Sparsity"
authors: ["Haocheng Xi", "Shuo Yang", "Yilong Zhao", "Chenfeng Xu", "Muyang Li", "Xiuyu Li", "Yujun Lin", "Han Cai", "Jintao Zhang", "Dacheng Li", "Jianfei Chen", "Ion Stoica", "Kurt Keutzer", "Song Han"]
year: 2025
venue: "arXiv"
external_ids:
  arxiv: "2502.01776"
  doi: null
  s2: null
tags: []
added: 2026-07-15T04:16:22Z
---

# Sparse VideoGen: Accelerating Video Diffusion Transformers with Spatial-Temporal Sparsity

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

> Diffusion Transformers (DiTs) dominate video generation but their high computational cost severely limits real-world applicability, usually requiring tens of minutes to generate a few seconds of video even on high-performance GPUs. This inefficiency primarily arises from the quadratic computational complexity of 3D Full Attention with respect to the context length. In this paper, we propose a training-free framework termed Sparse VideoGen (SVG) that leverages the inherent sparsity in 3D Full Attention to boost inference efficiency. We reveal that the attention heads can be dynamically classified into two groups depending on distinct sparse patterns: (1) Spatial Head, where only spatially-related tokens within each frame dominate the attention output, and (2) Temporal Head, where only temporally-related tokens across different frames dominate. Based on this insight, SVG proposes an online profiling strategy to capture the dynamic sparse patterns and predicts the type of attention head. Combined with a novel hardware-efficient tensor layout transformation and customized kernel implementations, SVG achieves up to 2.28x and 2.33x end-to-end speedup on CogVideoX-v1.5 and HunyuanVideo, respectively, while preserving generation quality. Our code is open-sourced and is available at https://github.com/svg-project/Sparse-VideoGen

