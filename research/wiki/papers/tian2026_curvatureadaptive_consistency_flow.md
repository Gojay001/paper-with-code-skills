---
type: paper
node_id: paper:tian2026_curvatureadaptive_consistency_flow
title: "Curvature-Adaptive Consistency Flow Matching: Autonomous Trajectory Optimization via Reinforcement Learning"
authors: ["Songtao Tian", "Guhan Chen", "Bohan Li", "Jingyi Ma", "Zixiong Yu"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2606.22394"
  doi: null
  s2: null
tags: []
added: 2026-07-15T04:16:22Z
---

# Curvature-Adaptive Consistency Flow Matching: Autonomous Trajectory Optimization via Reinforcement Learning

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

> Consistency distillation has significantly accelerated the inference of diffusion models. In this work, we reveal an intriguing asymmetry: while Logit-Normal sampling priors are highly efficacious for standard iterative generation, consistency distillation exhibits a distinctly different difficulty profile (e.g., U-shaped). We identify that the primary optimization bottlenecks reside at the boundary stages (initialization or final refinement) rather than the intermediate steps. To address the limitations of static sampling in accommodating evolving learning requirements, we propose Curvature-Adaptive Consistency Flow Matching (CACFM). By formulating distillation as a dynamic decision process, CACFM employs a lightweight Reinforcement Learning agent to actively probe Probability Flow ODE trajectories, automatically constructing an efficiency-oriented curriculum that prioritizes critical regions without manual scheduling. Integrated with a novel Flow Distribution Matching Distillation (DMD) objective, our approach achieves new state-of-the-art results on large-scale models such as FLUX and SDXL. It effectively mitigates structural deformities and preserves high-frequency details in extreme few-step regimes, achieving unprecedented visual fidelity.

