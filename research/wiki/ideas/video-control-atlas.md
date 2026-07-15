---
type: idea
node_id: idea:video-control-atlas
title: "ControlAtlas：视频 DiT 的层—步—时频控制相关性图谱"
stage: proposed
outcome: pending
added: 2026-07-15T04:18:14Z
based_on: ["paper:cao2025_relactrl_relevanceguided_efficient", "paper:yang2024_cogvideox_texttovideo_diffusion", "paper:bai2026_causality_video_diffusers"]
target_gaps: ["gap:G1"]
tags: ["video-generation", "controllable-generation", "diffusion-transformer", "efficiency", "mechanistic-analysis"]
---

# ControlAtlas：视频 DiT 的层—步—时频控制相关性图谱

**stage:** `proposed`  ·  **outcome:** `pending`

用低成本控制 probe 预测 held-out 条件下的稀疏控制布局。

## Thesis
控制分支对条件遵循的贡献在 layer、denoising step 与 temporal frequency 上非均匀；若低成本 probe 得到的 atlas 能在 held-out prompts 和条件类型上预测有效布局，并在相同 FLOPs 下优于随机、均匀及 layer-only 基线，则 atlas 不只是描述性热图。

## Key risks
主干 attention 稀疏与层/步探测已拥挤；必须限定为 condition branch、control adherence 与 temporal frequency，并证明跨样本或跨条件预测性。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

