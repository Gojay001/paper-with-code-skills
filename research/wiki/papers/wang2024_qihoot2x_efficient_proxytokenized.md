---
type: paper
node_id: paper:wang2024_qihoot2x_efficient_proxytokenized
title: "Qihoo-T2X: An Efficient Proxy-Tokenized Diffusion Transformer for Text-to-Any-Task"
authors: ["Jing Wang", "Ao Ma", "Jiasong Feng", "Dawei Leng", "Yuhui Yin", "Xiaodan Liang"]
year: 2024
venue: "arXiv"
external_ids:
  arxiv: "2409.04005"
  doi: null
  s2: null
tags: []
added: 2026-07-15T04:12:36Z
---

# Qihoo-T2X: An Efficient Proxy-Tokenized Diffusion Transformer for Text-to-Any-Task

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

> The global self-attention mechanism in diffusion transformers involves redundant computation due to the sparse and redundant nature of visual information, and the attention map of tokens within a spatial window shows significant similarity. To address this redundancy, we propose the Proxy-Tokenized Diffusion Transformer (PT-DiT), which employs sparse representative token attention (where the number of representative tokens is much smaller than the total number of tokens) to model global visual information efficiently. Specifically, within each transformer block, we compute an averaging token from each spatial-temporal window to serve as a proxy token for that region. The global semantics are captured through the self-attention of these proxy tokens and then injected into all latent tokens via cross-attention. Simultaneously, we introduce window and shift window attention to address the limitations in detail modeling caused by the sparse attention mechanism. Building on the well-designed PT-DiT, we further develop the Qihoo-T2X family, which includes a variety of models for T2I, T2V, and T2MV tasks. Experimental results show that PT-DiT achieves competitive performance while reducing the computational complexity in both image and video generation tasks (e.g., a 49% reduction compared to DiT and a 34% reduction compared to PixArt-$α$). The visual exhibition and source code of Qihoo-T2X is available at https://360cvgroup.github.io/Qihoo-T2X/.

