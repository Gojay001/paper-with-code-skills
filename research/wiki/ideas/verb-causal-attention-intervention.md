---
type: idea
node_id: idea:verb-causal-attention-intervention
title: "Verb-Causal：跨帧文本注意力的受控干预效应"
stage: proposed
outcome: pending
added: 2026-07-15T04:18:14Z
based_on: ["paper:feng2024_fancyvideo_towards_dynamic", "paper:liu2025_understanding_attention_mechanism", "paper:cole2026_attentionbender_manipulating_crossattention"]
target_gaps: ["gap:G2"]
tags: ["video-generation", "attention", "causal-intervention", "motion", "diagnostics"]
---

# Verb-Causal：跨帧文本注意力的受控干预效应

**stage:** `proposed`  ·  **outcome:** `pending`

用匹配能量与熵的 token 级干预检验 verb attention 是否对视频运动产生特异效应。

## Thesis
若 verb-token 的跨帧 attention 对运动具有特异作用，则在保持范数、熵和时间边际统计的条件下置乱其时间相位，应定向改变动作轨迹；noun、background、random-token 和随机正交变换对照不应产生同等效应。首个阶段只主张受控干预效应，不把 attention 直接解释为完整因果中介。

## Key risks
一般 attention perturbation 与 cross-attention creative probing 已有近邻；必须用 matched-energy、matched-entropy、token-length、paired-seed 和负对照建立区别。若所有 token 干预同样破坏画质，则核心假设失败。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

