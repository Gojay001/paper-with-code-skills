---
type: paper
node_id: paper:ma2025_lay2story_extending_diffusion
title: "Lay2Story: Extending Diffusion Transformers for Layout-Togglable Story Generation"
authors: ["Ao Ma", "Jiasong Feng", "Ke Cao", "Jing Wang", "Yun Wang", "Quanwei Zhang", "Zhanjie Zhang"]
year: 2025
venue: "arXiv"
external_ids:
  arxiv: "2508.08949"
  doi: null
  s2: null
tags: []
added: 2026-07-15T04:12:36Z
---

# Lay2Story: Extending Diffusion Transformers for Layout-Togglable Story Generation

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

> Storytelling tasks involving generating consistent subjects have gained significant attention recently. However, existing methods, whether training-free or training-based, continue to face challenges in maintaining subject consistency due to the lack of fine-grained guidance and inter-frame interaction. Additionally, the scarcity of high-quality data in this field makes it difficult to precisely control storytelling tasks, including the subject's position, appearance, clothing, expression, and posture, thereby hindering further advancements. In this paper, we demonstrate that layout conditions, such as the subject's position and detailed attributes, effectively facilitate fine-grained interactions between frames. This not only strengthens the consistency of the generated frame sequence but also allows for precise control over the subject's position, appearance, and other key details. Building on this, we introduce an advanced storytelling task: Layout-Togglable Storytelling, which enables precise subject control by incorporating layout conditions. To address the lack of high-quality datasets with layout annotations for this task, we develop Lay2Story-1M, which contains over 1 million 720p and higher-resolution images, processed from approximately 11,300 hours of cartoon videos. Building on Lay2Story-1M, we create Lay2Story-Bench, a benchmark with 3,000 prompts designed to evaluate the performance of different methods on this task. Furthermore, we propose Lay2Story, a robust framework based on the Diffusion Transformers (DiTs) architecture for Layout-Togglable Storytelling tasks. Through both qualitative and quantitative experiments, we find that our method outperforms the previous state-of-the-art (SOTA) techniques, achieving the best results in terms of consistency, semantic correlation, and aesthetic quality.

