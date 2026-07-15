---
type: idea
node_id: idea:risk-routed-product-lock
title: "Risk-Routed Product Lock：商品高风险区域的生成—真实路由"
stage: proposed
outcome: pending
added: 2026-07-15T09:04:45Z
based_on: ["paper:jin2025_insertanywhere_geometrically_grounded", "paper:tarrs2026_placid_identitypreserving_multiobject", "paper:chen2026_siminsert_seamless_video", "paper:zhou2026_point2insert_video_object"]
target_gaps: ["gap:G16", "gap:G17", "gap:G19"]
tags: ["e-commerce", "video-generation", "product-insertion", "risk-routing", "hybrid-generation"]
---

# Risk-Routed Product Lock：商品高风险区域的生成—真实路由

**stage:** `proposed`  ·  **outcome:** `pending`

学习哪些时空区域必须锁定真实商品证据，哪些区域可安全生成。

## Thesis
基于SKU属性、目标视角、遮挡和文字区域预测时空事实风险，并在保留/warp/插入/生成之间路由，应在相同真实度预算下优于固定mask、全生成和全插入。

## Key risks
非常接近InsertAnywhere、PLACID和工程合成流水线；若风险分配器没有跨SKU泛化和明确消融，不能作为独立算法贡献。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

