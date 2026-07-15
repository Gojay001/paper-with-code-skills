---
type: paper
node_id: paper:team2026_mova_towards_scalable
title: "MOVA: Towards Scalable and Synchronized Video-Audio Generation"
authors: ["SII-OpenMOSS Team", ":", "Donghua Yu", "Mingshu Chen", "Qi Chen", "Qi Luo", "Qianyi Wu", "Qinyuan Cheng", "Ruixiao Li", "Tianyi Liang", "Wenbo Zhang", "Wenming Tu", "Xiangyu Peng", "Yang Gao", "Yanru Huo", "Ying Zhu", "Yinze Luo", "Yiyang Zhang", "Yuerong Song", "Zhe Xu", "Zhiyu Zhang", "Chenchen Yang", "Cheng Chang", "Chushu Zhou", "Hanfu Chen", "Hongnan Ma", "Jiaxi Li", "Jingqi Tong", "Junxi Liu", "Ke Chen", "Shimin Li", "Shiqi Jiang", "Songlin Wang", "Wei Jiang", "Zhaoye Fei", "Zhiyuan Ning", "Chunguo Li", "Chenhui Li", "Ziwei He", "Zengfeng Huang", "Xie Chen", "Xipeng Qiu"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2602.08794"
  doi: null
  s2: null
tags: []
added: 2026-07-15T04:12:36Z
---

# MOVA: Towards Scalable and Synchronized Video-Audio Generation

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

> Audio is indispensable for real-world video, yet generation models have largely overlooked audio components. Current approaches to producing audio-visual content often rely on cascaded pipelines, which increase cost, accumulate errors, and degrade overall quality. While systems such as Veo 3 and Sora 2 emphasize the value of simultaneous generation, joint multimodal modeling introduces unique challenges in architecture, data, and training. Moreover, the closed-source nature of existing systems limits progress in the field. In this work, we introduce MOVA (MOSS Video and Audio), an open-source model capable of generating high-quality, synchronized audio-visual content, including realistic lip-synced speech, environment-aware sound effects, and content-aligned music. MOVA employs a Mixture-of-Experts (MoE) architecture, with a total of 32B parameters, of which 18B are active during inference. It supports IT2VA (Image-Text to Video-Audio) generation task. By releasing the model weights and code, we aim to advance research and foster a vibrant community of creators. The released codebase features comprehensive support for efficient inference, LoRA fine-tuning, and prompt enhancement.

