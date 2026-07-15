---
type: paper
node_id: paper:cao2025_relactrl_relevanceguided_efficient
title: "RelaCtrl: Relevance-Guided Efficient Control for Diffusion Transformers"
authors: ["Ke Cao", "Jing Wang", "Ao Ma", "Jiasong Feng", "Xuanhua He", "Run Ling", "Haowei Liu", "Jian Lu", "Wei Feng", "Haozhe Wang", "Hongjuan Pei", "Yihua Shao", "Zhanjie Zhang", "Jie Zhang"]
year: 2025
venue: "arXiv"
external_ids:
  arxiv: "2502.14377"
  doi: null
  s2: null
tags: []
added: 2026-07-15T04:12:36Z
---

# RelaCtrl: Relevance-Guided Efficient Control for Diffusion Transformers

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

> The Diffusion Transformer plays a pivotal role in advancing text-to-image and text-to-video generation, owing primarily to its inherent scalability. However, existing controlled diffusion transformer methods incur significant parameter and computational overheads and suffer from inefficient resource allocation due to their failure to account for the varying relevance of control information across different transformer layers. To address this, we propose the Relevance-Guided Efficient Controllable Generation framework, RelaCtrl, enabling efficient and resource-optimized integration of control signals into the Diffusion Transformer. First, we evaluate the relevance of each layer in the Diffusion Transformer to the control information by assessing the "ControlNet Relevance Score"-i.e., the impact of skipping each control layer on both the quality of generation and the control effectiveness during inference. Based on the strength of the relevance, we then tailor the positioning, parameter scale, and modeling capacity of the control layers to reduce unnecessary parameters and redundant computations. Additionally, to further improve efficiency, we replace the self-attention and FFN in the commonly used copy block with the carefully designed Two-Dimensional Shuffle Mixer (TDSM), enabling efficient implementation of both the token mixer and channel mixer. Both qualitative and quantitative experimental results demonstrate that our approach achieves superior performance with only 15% of the parameters and computational complexity compared to PixArt-delta.

