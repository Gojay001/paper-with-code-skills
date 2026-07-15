---
type: paper
node_id: paper:zhang2025_ustydit_ultrahigh_quality
title: "U-StyDiT: Ultra-high Quality Artistic Style Transfer Using Diffusion Transformers"
authors: ["Zhanjie Zhang", "Ao Ma", "Ke Cao", "Jing Wang", "Shanyuan Liu", "Yuhang Ma", "Bo Cheng", "Dawei Leng", "Yuhui Yin"]
year: 2025
venue: "arXiv"
external_ids:
  arxiv: "2503.08157"
  doi: null
  s2: null
tags: []
added: 2026-07-15T04:12:36Z
---

# U-StyDiT: Ultra-high Quality Artistic Style Transfer Using Diffusion Transformers

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

> Ultra-high quality artistic style transfer refers to repainting an ultra-high quality content image using the style information learned from the style image. Existing artistic style transfer methods can be categorized into style reconstruction-based and content-style disentanglement-based style transfer approaches. Although these methods can generate some artistic stylized images, they still exhibit obvious artifacts and disharmonious patterns, which hinder their ability to produce ultra-high quality artistic stylized images. To address these issues, we propose a novel artistic image style transfer method, U-StyDiT, which is built on transformer-based diffusion (DiT) and learns content-style disentanglement, generating ultra-high quality artistic stylized images. Specifically, we first design a Multi-view Style Modulator (MSM) to learn style information from a style image from local and global perspectives, conditioning U-StyDiT to generate stylized images with the learned style information. Then, we introduce a StyDiT Block to learn content and style conditions simultaneously from a style image. Additionally, we propose an ultra-high quality artistic image dataset, Aes4M, comprising 10 categories, each containing 400,000 style images. This dataset effectively solves the problem that the existing style transfer methods cannot produce high-quality artistic stylized images due to the size of the dataset and the quality of the images in the dataset. Finally, the extensive qualitative and quantitative experiments validate that our U-StyDiT can create higher quality stylized images compared to state-of-the-art artistic style transfer methods. To our knowledge, our proposed method is the first to address the generation of ultra-high quality stylized images using transformer-based diffusion.

