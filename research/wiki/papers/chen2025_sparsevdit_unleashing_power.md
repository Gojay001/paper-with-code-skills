---
type: paper
node_id: paper:chen2025_sparsevdit_unleashing_power
title: "Sparse-vDiT: Unleashing the Power of Sparse Attention to Accelerate Video Diffusion Transformers"
authors: ["Pengtao Chen", "Xianfang Zeng", "Maosen Zhao", "Peng Ye", "Mingzhu Shen", "Wei Cheng", "Gang Yu", "Tao Chen"]
year: 2025
venue: "arXiv"
external_ids:
  arxiv: "2506.03065"
  doi: null
  s2: null
tags: []
added: 2026-07-15T04:16:22Z
---

# Sparse-vDiT: Unleashing the Power of Sparse Attention to Accelerate Video Diffusion Transformers

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

> While Diffusion Transformers (DiTs) have achieved breakthroughs in video generation, this long sequence generation task remains constrained by the quadratic complexity of attention mechanisms, resulting in significant inference latency. Through detailed analysis of attention maps in Video Diffusion Transformer (vDiT), we identify three recurring sparsity patterns: diagonal, multi-diagonal, and vertical-stripe structures. And even 3-6\% attention heads can be skipped. Crucially, these patterns exhibit strong layer-depth and head-position correlations but show limited dependence on the input content. Leveraging these findings, we propose Sparse-vDiT, a sparsity acceleration framework for vDiT comprising: 1) Pattern-optimized sparse kernels that replace dense attention with computationally efficient implementations for each identified sparsity pattern. 2) An offline sparse diffusion search algorithm that selects the optimal sparse computation strategy per layer and head via hardware-aware cost modeling. After determining the optimal configuration, we fuse heads within the same layer that share the same attention strategy, enhancing inference efficiency. Integrated into state-of-the-art vDiT models (CogVideoX1.5, HunyuanVideo, and Wan2.1), Sparse-vDiT achieves 2.09$\times$, 2.38$\times$, and 1.67$\times$ theoretical FLOP reduction, and actual inference speedups of 1.76$\times$, 1.85$\times$, and 1.58$\times$, respectively, while maintaining high visual fidelity, with PSNR values reaching 24.13, 27.09, and 22.59. Our work demonstrates that latent structural sparsity in vDiTs can be systematically exploited for long video synthesis.

