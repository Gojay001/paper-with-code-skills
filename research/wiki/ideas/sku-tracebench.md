---
type: idea
node_id: idea:sku-tracebench
title: "SKU-TraceBench：电商视频商品真实性压力测试"
stage: proposed
outcome: pending
added: 2026-07-15T09:04:45Z
based_on: ["paper:deng2025_ecommercevideo_benchmark_approach", "paper:yuan2025_opens2vnexus_detailed_benchmark", "paper:khanna2026_productconsistency_improving_product", "paper:wu2026_considgen_viewconsistent_identitypreserving"]
target_gaps: ["gap:G11", "gap:G12", "gap:G19", "gap:G20"]
tags: ["e-commerce", "video-generation", "benchmark", "product-identity", "sku-fidelity"]
---

# SKU-TraceBench：电商视频商品真实性压力测试

**stage:** `proposed`  ·  **outcome:** `pending`

以相似SKU hard negatives和逐属性时序轨迹衡量商业级商品真实性。

## Thesis
若评价显式分解几何、颜色、材质、Logo、OCR、规格和版本，并按视角、遮挡与运动强度分层，则比通用主体相似度更能预测商家对生成视频的可发布判断。

## Key risks
E-CommerceVideo、OpenS2V-Nexus、ConsIDVid-Bench与ProductConsistency已覆盖相邻评价；必须证明SKU版本级可判别性和人评相关性，而不是简单堆指标。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

