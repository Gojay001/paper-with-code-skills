---
type: paper
node_id: paper:zhao2024_dynamic_diffusion_transformer
title: "Dynamic Diffusion Transformer"
authors: ["Wangbo Zhao", "Yizeng Han", "Jiasheng Tang", "Kai Wang", "Yibing Song", "Gao Huang", "Fan Wang", "Yang You"]
year: 2024
venue: "arXiv"
external_ids:
  arxiv: "2410.03456"
  doi: null
  s2: null
tags: []
added: 2026-07-15T04:16:22Z
---

# Dynamic Diffusion Transformer

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

> Diffusion Transformer (DiT), an emerging diffusion model for image generation, has demonstrated superior performance but suffers from substantial computational costs. Our investigations reveal that these costs stem from the static inference paradigm, which inevitably introduces redundant computation in certain diffusion timesteps and spatial regions. To address this inefficiency, we propose Dynamic Diffusion Transformer (DyDiT), an architecture that dynamically adjusts its computation along both timestep and spatial dimensions during generation. Specifically, we introduce a Timestep-wise Dynamic Width (TDW) approach that adapts model width conditioned on the generation timesteps. In addition, we design a Spatial-wise Dynamic Token (SDT) strategy to avoid redundant computation at unnecessary spatial locations. Extensive experiments on various datasets and different-sized models verify the superiority of DyDiT. Notably, with <3% additional fine-tuning iterations, our method reduces the FLOPs of DiT-XL by 51%, accelerates generation by 1.73, and achieves a competitive FID score of 2.07 on ImageNet. The code is publicly available at https://github.com/NUS-HPC-AI-Lab/ Dynamic-Diffusion-Transformer.

