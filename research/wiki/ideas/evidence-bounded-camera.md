---
type: idea
node_id: idea:evidence-bounded-camera
title: "Evidence-Bounded Camera：证据约束的商品镜头生成"
stage: proposed
outcome: pending
added: 2026-07-15T09:04:45Z
based_on: ["paper:wu2026_considgen_viewconsistent_identitypreserving", "paper:ko2026_3dreambooth_highfidelity_subjectdriven", "paper:he2024_cameractrl_enabling_camera", "paper:wang2023_motionctrl_unified_flexible"]
target_gaps: ["gap:G12", "gap:G13", "gap:G16", "gap:G20"]
tags: ["e-commerce", "video-generation", "camera-control", "risk-calibration", "multi-view"]
---

# Evidence-Bounded Camera：证据约束的商品镜头生成

**stage:** `proposed`  ·  **outcome:** `pending`

用可校准的视角覆盖—身份风险模型约束镜头轨迹，并允许请求更多参考或拒绝生成。

## Thesis
目标镜头越过商品参考视图覆盖时，SKU身份风险应可被校准预测；在固定风险预算下自适应缩小或改写镜头轨迹，可比固定orbit获得更大的安全运动范围。

## Key risks
ConsID-Gen和3DreamBooth已有多视图几何；贡献必须是校准风险、risk-coverage曲线与abstention，而不是按参考图数量改prompt。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

