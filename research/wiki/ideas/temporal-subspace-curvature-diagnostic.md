---
type: idea
node_id: idea:temporal-subspace-curvature-diagnostic
title: "Temporal-Curvature：Flow 视频的时间子空间曲率诊断"
stage: proposed
outcome: pending
added: 2026-07-15T04:18:14Z
based_on: ["paper:lipman2022_flow_matching_generative", "paper:wan2025_wan_open_advanced", "paper:tian2026_curvatureadaptive_consistency_flow", "paper:yuan2026_fewstep_diffusion_sampling"]
target_gaps: ["gap:G3"]
tags: ["video-generation", "flow-matching", "trajectory-geometry", "temporal-consistency", "diagnostics"]
---

# Temporal-Curvature：Flow 视频的时间子空间曲率诊断

**stage:** `proposed`  ·  **outcome:** `pending`

比较空间外观、时间差分和全局轨迹量对闪烁与动作断裂的增量预测力。

## Thesis
经过 latent scale、camera motion 与 codec 归一化后，时间差分子空间曲率若仍显著优于全局曲率、速度范数、local truncation error 和帧置信度预测 flicker/动作断裂，则它揭示了视频 Flow 轨迹的特异失败机制。自适应采样只作为下游验证，不是第一阶段主贡献。

## Key risks
曲率可能是坐标或有限差分伪量；CACFM、DSA 和实例自适应时间离散已覆盖采样调度邻域。需要跨 prompt、codec 和至少两个 checkpoint 的 held-out 验证。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

