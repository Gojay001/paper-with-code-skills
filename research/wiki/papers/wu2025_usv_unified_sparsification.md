---
type: paper
node_id: paper:wu2025_usv_unified_sparsification
title: "USV: Unified Sparsification for Accelerating Video Diffusion Models"
authors: ["Xinjian Wu", "Hongmei Wang", "Yuan Zhou", "Qinglin Lu"]
year: 2025
venue: "arXiv"
external_ids:
  arxiv: "2512.05754"
  doi: null
  s2: null
tags: []
added: 2026-07-15T04:16:22Z
---

# USV: Unified Sparsification for Accelerating Video Diffusion Models

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

> The scalability of high-fidelity video diffusion models (VDMs) is constrained by two key sources of redundancy: the quadratic complexity of global spatio-temporal attention and the computational overhead of long iterative denoising trajectories. Existing accelerators -- such as sparse attention and step-distilled samplers -- typically target a single dimension in isolation and quickly encounter diminishing returns, as the remaining bottlenecks become dominant. In this work, we introduce USV (Unified Sparsification for Video diffusion models), an end-to-end trainable framework that overcomes this limitation by jointly orchestrating sparsification across both the model's internal computation and its sampling process. USV learns a dynamic, data- and timestep-dependent sparsification policy that prunes redundant attention connections, adaptively merges semantically similar tokens, and reduces denoising steps, treating them not as independent tricks but as coordinated actions within a single optimization objective. This multi-dimensional co-design enables strong mutual reinforcement among previously disjoint acceleration strategies. Extensive experiments on large-scale video generation benchmarks demonstrate that USV achieves up to 83.3% speedup in the denoising process and 22.7% end-to-end acceleration, while maintaining high visual fidelity. Our results highlight unified, dynamic sparsification as a practical path toward efficient, high-quality video generation.

