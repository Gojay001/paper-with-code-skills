---
type: paper
node_id: paper:kim2025_learning_zeroshot_subjectdriven
title: "Learning Zero-Shot Subject-Driven Video Generation Using 1% Compute"
authors: ["Daneul Kim", "Jingxu Zhang", "Wonjoon Jin", "Sunghyun Cho", "Qi Dai", "Jaesik Park", "Chong Luo"]
year: 2025
venue: "arXiv"
external_ids:
  arxiv: "2504.17816"
  doi: null
  s2: null
tags: []
added: 2026-07-15T09:01:45Z
---

# Learning Zero-Shot Subject-Driven Video Generation Using 1% Compute

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

> Subject-driven video generation (SDV-Gen) aims to produce videos of a specific subject by adapting a pretrained video model, enabling personalized and application-driven content creation. To achieve this goal, per-subject tuning methods require approximately 200 A100 GPU hours to generate a customized video, whereas zero-shot methods avoid per-subject tuning but typically rely on millions of subject-video pairs for the supervision, incurring massive network fine-tuning costs (10K-200K A100 GPU hours). We propose a data- and compute-efficient zero-shot SDV-Gen framework that avoids test-time per-subject tuning and the use of large-scale subject-video pairs. Our key idea decomposes SDV-Gen into (i) identity injection learned from subject-image pairs and (ii) motion-awareness preservation maintained by a small set of arbitrary videos. We optimize the two tasks with stochastic switching, using random reference-frame sampling and image-token dropout to prevent trivial first-frame copying. Our gradient analysis shows that the two objectives rapidly evolve toward nearly orthogonal update subspaces, explaining the stable optimization. Using CogVideoX-5B, we adapt a single model with 200K subject-image pairs and 4,000 arbitrary videos in 288 A100 GPU hours. This yields about 1% of compute compared to prior zero-shot baselines (i.e., 0.4% of VACE and 2.8% of Phantom) while using no subject-video pairs, yet remaining competitive in subject fidelity and motion quality. We show that the same recipe transfers to Wan 2.2-5B.

