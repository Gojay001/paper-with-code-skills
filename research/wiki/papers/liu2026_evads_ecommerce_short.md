---
type: paper
node_id: paper:liu2026_evads_ecommerce_short
title: "E-VAds: An E-commerce Short Videos Understanding Benchmark for MLLMs"
authors: ["Xianjie Liu", "Yiman Hu", "Liang Wu", "Ping Hu", "Yixiong Zou", "Jian Xu", "Bo Zheng"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2602.08355"
  doi: null
  s2: null
tags: []
added: 2026-07-15T09:01:45Z
---

# E-VAds: An E-commerce Short Videos Understanding Benchmark for MLLMs

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

> E-commerce short videos represent a high-revenue segment of the online video industry characterized by a goal-driven format and dense multi-modal signals. Current models often struggle with these videos because existing benchmarks focus primarily on general-purpose tasks and neglect the reasoning of commercial intent. In this work, we first propose a multi-modal information density assessment framework to quantify the complexity of this domain. Our evaluation reveals that e-commerce content exhibits substantially higher density across visual, audio, and textual modalities compared to mainstream datasets, establishing a more challenging frontier for video understanding. To address this gap, we introduce E-commerce Video Ads Benchmark, which is the first benchmark specifically designed for e-commerce short video understanding. We curated 3,961 high-quality videos from Taobao covering a wide range of product categories and used a multi-agent system to generate 19,785 open-ended Q&A pairs, which consist of five distinct tasks. Finally, we develop E-VAds-R1, an RL-based reasoning model featuring a multi-grained reward design called MG-GRPO. This strategy provides smooth guidance for early exploration while creating a non-linear incentive for expert-level precision. Experimental results demonstrate that E-VAds-R1 achieves a 109.2% performance gain in commercial intent reasoning with only a few hundred training samples. Data is available at https://github.com/TaobaoTmall-AlgorithmProducts/E-VAds_Benchmark.

