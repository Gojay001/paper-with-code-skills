---
type: paper
node_id: paper:cheng2026_recommendation_generation_unifying
title: "Recommendation as Generation: Unifying Personalized Video Generation and Recommendation at Industrial Scale"
authors: ["Yanhua Cheng", "Bo Wang", "Haotian Zhang", "Xinyuan Gao", "Zhihui Yin", "Ben Xue", "Yongzhi Li", "Jieting Xue", "Ye Ma", "Minquan Wang", "Jiahui Li", "Tianyu Xu", "Zhiqiang Liu", "Xiao Lin", "Shiyang Wen", "Changcheng Li", "Liu Liu", "Quan Chen", "Peng Jiang", "Kun Gai"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2606.25496"
  doi: null
  s2: null
tags: []
added: 2026-07-15T09:01:57Z
---

# Recommendation as Generation: Unifying Personalized Video Generation and Recommendation at Industrial Scale

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

> Traditional short-video recommendation systems match user interest to a fixed pool of pre-produced videos, which limits their ability to capture fine-grained and dynamic preferences. We propose Recommendation-as-Generation (RaG), a new paradigm that generates personalized videos on demand from inferred user interest. Our framework unifies generative recommendation and video generation through shared semantic IDs (SIDs), which disentangle video representation into content semantics and creative style semantics, enabling both fine-grained modeling of user interest and controllable generation of interest-aligned videos. We further develop Video Generation Agents (VGAs) that are conditioned on inferred SIDs to drive hierarchical planning and refinement for video creation, including visual composition, audio alignment, and artistic effect enhancement. To optimize the framework, we effectively introduce a synergistic cross-domain reward learning mechanism that jointly enforces interest alignment, user feedback, and video quality assessment. We deploy RaG on an industrial-scale platform with over 400 million daily active users and evaluate it in a revenue-critical advertising scenario. Online A/B tests show up to 1.87% ad revenue improvement compared to a strong production GRM baseline, demonstrating its effectiveness in driving further revenue gains beyond generative recommendation. Our results highlight a closed-loop generative system as a promising paradigm for integrating personalized video generation into recommendation.

