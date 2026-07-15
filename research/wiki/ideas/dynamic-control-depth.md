---
type: idea
node_id: idea:dynamic-control-depth
title: "DynamicControlDepth：条件误差驱动的控制层预算"
stage: proposed
outcome: pending
added: 2026-07-15T04:18:14Z
based_on: ["paper:cao2025_relactrl_relevanceguided_efficient", "paper:zhao2024_dynamic_diffusion_transformer", "paper:wu2025_usv_unified_sparsification"]
target_gaps: ["gap:G4"]
tags: ["controllable-generation", "dynamic-compute", "efficiency", "backup"]
---

# DynamicControlDepth：条件误差驱动的控制层预算

**stage:** `proposed`  ·  **outcome:** `pending`

用早期条件遵循误差按样本选择控制深度。

## Thesis
若早期条件遵循误差能够跨条件类型预测样本所需控制容量，动态 top-k 控制层应在相同平均 FLOPs 下优于固定 top-k，并在相同控制精度下降低计算。

## Key risks
与 RelaCtrl、DyDiT、DynamicControl 和 USV 的组合痕迹明显，新颖性较低；仅作为 ControlAtlas 不可执行时的备选。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

