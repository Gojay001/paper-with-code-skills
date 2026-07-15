---
type: paper
node_id: paper:team2025_zimage_efficient_image
title: "Z-Image: An Efficient Image Generation Foundation Model with Single-Stream Diffusion Transformer"
authors: ["Z-Image Team", "Huanqia Cai", "Sihan Cao", "Ruoyi Du", "Peng Gao", "Aiming Hao", "Steven Hoi", "Zhaohui Hou", "Shijie Huang", "Dengyang Jiang", "Yuming Jiang", "Xin Jin", "Liangchen Li", "Zhen Li", "Zhong-Yu Li", "David Liu", "Dongyang Liu", "Qilong Wu", "Feng Yu", "Zechao Zhan", "Chi Zhang", "Shifeng Zhang", "Ruikai Zhou", "Shilin Zhou"]
year: 2025
venue: "arXiv"
external_ids:
  arxiv: "2511.22699"
  doi: null
  s2: null
tags: []
added: 2026-07-15T04:12:36Z
---

# Z-Image: An Efficient Image Generation Foundation Model with Single-Stream Diffusion Transformer

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

> The landscape of high-performance image generation models is currently dominated by proprietary systems, such as Nano Banana Pro and Seedream 4.0. Leading open-source alternatives, including Qwen-Image, Hunyuan-Image-3.0 and FLUX.2, are characterized by massive parameter counts (20B to 80B), making them impractical for inference, and fine-tuning on consumer-grade hardware. To address this gap, we propose Z-Image, an efficient 6B-parameter foundation generative model built upon a Scalable Single-Stream Diffusion Transformer (S3-DiT) architecture that challenges the "scale-at-all-costs" paradigm. By systematically optimizing the entire model lifecycle -- from a curated data infrastructure to a streamlined training curriculum -- we complete the full training workflow in just 314K H800 GPU hours (approx. $630K). Our few-step distillation scheme with reward post-training further yields Z-Image-Turbo, offering both sub-second inference latency on an enterprise-grade H800 GPU and compatibility with consumer-grade hardware (<16GB VRAM). Additionally, our omni-pre-training paradigm also enables efficient training of Z-Image-Edit, an editing model with impressive instruction-following capabilities. Both qualitative and quantitative experiments demonstrate that our model achieves performance comparable to or surpassing that of leading competitors across various dimensions. Most notably, Z-Image exhibits exceptional capabilities in photorealistic image generation and bilingual text rendering, delivering results that rival top-tier commercial models, thereby demonstrating that state-of-the-art results are achievable with significantly reduced computational overhead. We publicly release our code, weights, and online demo to foster the development of accessible, budget-friendly, yet state-of-the-art generative models.

