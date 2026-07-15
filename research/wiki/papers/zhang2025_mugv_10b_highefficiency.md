---
type: paper
node_id: paper:zhang2025_mugv_10b_highefficiency
title: "MUG-V 10B: High-efficiency Training Pipeline for Large Video Generation Models"
authors: ["Yongshun Zhang", "Zhongyi Fan", "Yonghang Zhang", "Zhangzikang Li", "Weifeng Chen", "Zhongwei Feng", "Chaoyue Wang", "Peng Hou", "Anxiang Zeng"]
year: 2025
venue: "arXiv"
external_ids:
  arxiv: "2510.17519"
  doi: null
  s2: null
tags: []
added: 2026-07-15T09:01:57Z
---

# MUG-V 10B: High-efficiency Training Pipeline for Large Video Generation Models

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

> In recent years, large-scale generative models for visual content (\textit{e.g.,} images, videos, and 3D objects/scenes) have made remarkable progress. However, training large-scale video generation models remains particularly challenging and resource-intensive due to cross-modal text-video alignment, the long sequences involved, and the complex spatiotemporal dependencies. To address these challenges, we present a training framework that optimizes four pillars: (i) data processing, (ii) model architecture, (iii) training strategy, and (iv) infrastructure for large-scale video generation models. These optimizations delivered significant efficiency gains and performance improvements across all stages of data preprocessing, video compression, parameter scaling, curriculum-based pretraining, and alignment-focused post-training. Our resulting model, MUG-V 10B, matches recent state-of-the-art video generators overall and, on e-commerce-oriented video generation tasks, surpasses leading open-source baselines in human evaluations. More importantly, we open-source the complete stack, including model weights, Megatron-Core-based large-scale training code, and inference pipelines for video generation and enhancement. To our knowledge, this is the first public release of large-scale video generation training code that exploits Megatron-Core to achieve high training efficiency and near-linear multi-node scaling, details are available in https://github.com/Shopee-MUG/MUG-V.

