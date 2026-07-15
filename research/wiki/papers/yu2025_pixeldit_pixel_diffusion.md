---
type: paper
node_id: paper:yu2025_pixeldit_pixel_diffusion
title: "PixelDiT: Pixel Diffusion Transformers for Image Generation"
authors: ["Yongsheng Yu", "Wei Xiong", "Weili Nie", "Yichen Sheng", "Shiqiu Liu", "Jiebo Luo"]
year: 2025
venue: "arXiv"
external_ids:
  arxiv: "2511.20645"
  doi: null
  s2: null
tags: []
added: 2026-07-15T04:12:36Z
---

# PixelDiT: Pixel Diffusion Transformers for Image Generation

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

> Latent-space modeling has been the standard for Diffusion Transformers (DiTs). However, it relies on a two-stage pipeline where the pretrained autoencoder introduces lossy reconstruction, leading to error accumulation while hindering joint optimization. To address these issues, we propose PixelDiT, a single-stage, end-to-end model that eliminates the need for the autoencoder and learns the diffusion process directly in the pixel space. PixelDiT adopts a fully transformer-based architecture shaped by a dual-level design: a patch-level DiT that captures global semantics and a pixel-level DiT that refines texture details, enabling efficient training of a pixel-space diffusion model while preserving fine details. PixelDiT achieves 1.61 FID on ImageNet 256 and 1.81 FID on ImageNet 512, surpassing existing pixel generative models. We further extend PixelDiT to text-to-image generation and pretrain it at the 10242resolution in pixel space. It achieves 0.74 on GenEval and 83.5 on DPG-bench, approaching the best latent diffusion models. Code: https://github.com/NVlabs/PixelDiT

