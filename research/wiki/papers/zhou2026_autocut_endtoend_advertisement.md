---
type: paper
node_id: paper:zhou2026_autocut_endtoend_advertisement
title: "AutoCut: End-to-end advertisement video editing based on multimodal discretization and controllable generation"
authors: ["Milton Zhou", "Sizhong Qin", "Yongzhi Li", "Quan Chen", "Peng Jiang"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2603.28366"
  doi: null
  s2: null
tags: []
added: 2026-07-15T09:01:57Z
---

# AutoCut: End-to-end advertisement video editing based on multimodal discretization and controllable generation

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

> Short-form videos have become a primary medium for digital advertising, requiring scalable and efficient content creation. However, current workflows and AI tools remain disjoint and modality-specific, leading to high production costs and low overall efficiency. To address this issue, we propose AutoCut, an end-to-end advertisement video editing framework based on multimodal discretization and controllable editing. AutoCut employs dedicated encoders to extract video and audio features, then applies residual vector quantization to discretize them into unified tokens aligned with textual representations, constructing a shared video-audio-text token space. Built upon a foundation model, we further develop a multimodal large language model for video editing through combined multimodal alignment and supervised fine-tuning, supporting tasks covering video selection and ordering, script generation, and background music selection within a unified editing framework. Finally, a complete production pipeline converts the predicted token sequences into deployable long video outputs. Experiments on real-world advertisement datasets show that AutoCut reduces production cost and iteration time while substantially improving consistency and controllability, paving the way for scalable video creation.

