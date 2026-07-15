---
type: paper
node_id: paper:ling2025_mofu_scaleaware_modulation
title: "MoFu: Scale-Aware Modulation and Fourier Fusion for Multi-Subject Video Generation"
authors: ["Run Ling", "Ke Cao", "Jian Lu", "Ao Ma", "Haowei Liu", "Runze He", "Changwei Wang", "Rongtao Xu", "Yihua Shao", "Zhanjie Zhang", "Peng Wu", "Guibing Guo", "Wei Feng", "Zheng Zhang", "Jingjing Lv", "Junjie Shen", "Ching Law", "Xingwei Wang"]
year: 2025
venue: "arXiv"
external_ids:
  arxiv: "2512.22310"
  doi: null
  s2: null
tags: []
added: 2026-07-15T04:12:36Z
---

# MoFu: Scale-Aware Modulation and Fourier Fusion for Multi-Subject Video Generation

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

> Multi-subject video generation aims to synthesize videos from textual prompts and multiple reference images, ensuring that each subject preserves natural scale and visual fidelity. However, current methods face two challenges: scale inconsistency, where variations in subject size lead to unnatural generation, and permutation sensitivity, where the order of reference inputs causes subject distortion. In this paper, we propose MoFu, a unified framework that tackles both challenges. For scale inconsistency, we introduce Scale-Aware Modulation (SMO), an LLM-guided module that extracts implicit scale cues from the prompt and modulates features to ensure consistent subject sizes. To address permutation sensitivity, we present a simple yet effective Fourier Fusion strategy that processes the frequency information of reference features via the Fast Fourier Transform to produce a unified representation. Besides, we design a Scale-Permutation Stability Loss to jointly encourage scale-consistent and permutation-invariant generation. To further evaluate these challenges, we establish a dedicated benchmark with controlled variations in subject scale and reference permutation. Extensive experiments demonstrate that MoFu significantly outperforms existing methods in preserving natural scale, subject fidelity, and overall visual quality.

