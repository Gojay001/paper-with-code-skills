---
type: paper
node_id: paper:jiang2023_videobooth_diffusionbased_video
title: "VideoBooth: Diffusion-based Video Generation with Image Prompts"
authors: ["Yuming Jiang", "Tianxing Wu", "Shuai Yang", "Chenyang Si", "Dahua Lin", "Yu Qiao", "Chen Change Loy", "Ziwei Liu"]
year: 2023
venue: "arXiv"
external_ids:
  arxiv: "2312.00777"
  doi: null
  s2: null
tags: []
added: 2026-07-15T09:02:38Z
---

# VideoBooth: Diffusion-based Video Generation with Image Prompts

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

> Text-driven video generation witnesses rapid progress. However, merely using text prompts is not enough to depict the desired subject appearance that accurately aligns with users' intents, especially for customized content creation. In this paper, we study the task of video generation with image prompts, which provide more accurate and direct content control beyond the text prompts. Specifically, we propose a feed-forward framework VideoBooth, with two dedicated designs: 1) We propose to embed image prompts in a coarse-to-fine manner. Coarse visual embeddings from image encoder provide high-level encodings of image prompts, while fine visual embeddings from the proposed attention injection module provide multi-scale and detailed encoding of image prompts. These two complementary embeddings can faithfully capture the desired appearance. 2) In the attention injection module at fine level, multi-scale image prompts are fed into different cross-frame attention layers as additional keys and values. This extra spatial information refines the details in the first frame and then it is propagated to the remaining frames, which maintains temporal consistency. Extensive experiments demonstrate that VideoBooth achieves state-of-the-art performance in generating customized high-quality videos with subjects specified in image prompts. Notably, VideoBooth is a generalizable framework where a single model works for a wide range of image prompts with feed-forward pass.

