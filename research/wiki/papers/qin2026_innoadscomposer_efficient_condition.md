---
type: paper
node_id: paper:qin2026_innoadscomposer_efficient_condition
title: "InnoAds-Composer: Efficient Condition Composition for E-Commerce Poster Generation"
authors: ["Yuxin Qin", "Ke Cao", "Haowei Liu", "Ao Ma", "Fengheng Li", "Honghe Zhu", "Zheng Zhang", "Run Ling", "Wei Feng", "Xuanhua He", "Zhanjie Zhang", "Zhen Guo", "Haoyi Bian", "Jingjing Lv", "Junjie Shen", "Ching Law"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2603.05898"
  doi: null
  s2: null
tags: []
added: 2026-07-15T04:12:36Z
---

# InnoAds-Composer: Efficient Condition Composition for E-Commerce Poster Generation

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

> E-commerce product poster generation aims to automatically synthesize a single image that effectively conveys product information by presenting a subject, text, and a designed style. Recent diffusion models with fine-grained and efficient controllability have advanced product poster synthesis, yet they typically rely on multi-stage pipelines, and simultaneous control over subject, text, and style remains underexplored. Such naive multi-stage pipelines also show three issues: poor subject fidelity, inaccurate text, and inconsistent style. To address these issues, we propose InnoAds-Composer, a single-stage framework that enables efficient tri-conditional control tokens over subject, glyph, and style. To alleviate the quadratic overhead introduced by naive tri-conditional token concatenation, we perform importance analysis over layers and timesteps and route each condition only to the most responsive positions, thereby shortening the active token sequence. Besides, to improve the accuracy of Chinese text rendering, we design a Text Feature Enhancement Module (TFEM) that integrates features from both glyph images and glyph crops. To support training and evaluation, we also construct a high-quality e-commerce product poster dataset and benchmark, which is the first dataset that jointly contains subject, text, and style conditions. Extensive experiments demonstrate that InnoAds-Composer significantly outperforms existing product poster methods without obviously increasing inference latency.

