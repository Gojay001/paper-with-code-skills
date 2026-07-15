---
type: paper
node_id: paper:lu2026_chordedit_onestep_lowenergy
title: "ChordEdit: One-Step Low-Energy Transport for Image Editing"
authors: ["Liangsi Lu", "Xuhang Chen", "Minzhe Guo", "Shichu Li", "Jingchao Wang", "Yang Shi"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2602.19083"
  doi: null
  s2: null
tags: []
added: 2026-07-15T04:12:36Z
---

# ChordEdit: One-Step Low-Energy Transport for Image Editing

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

> The advent of one-step text-to-image (T2I) models offers unprecedented synthesis speed. However, their application to text-guided image editing remains severely hampered, as forcing existing training-free editors into a single inference step fails. This failure manifests as severe object distortion and a critical loss of consistency in non-edited regions, resulting from the high-energy, erratic trajectories produced by naive vector arithmetic on the models' structured fields. To address this problem, we introduce ChordEdit, a model agnostic, training-free, and inversion-free method that facilitates high-fidelity one-step editing. We recast editing as a transport problem between the source and target distributions defined by the source and target text prompts. Leveraging dynamic optimal transport theory, we derive a principled, low-energy control strategy. This strategy yields a smoothed, variance-reduced editing field that is inherently stable, facilitating the field to be traversed in a single, large integration step. A theoretically grounded and experimentally validated approach allows ChordEdit to deliver fast, lightweight and precise edits, finally achieving true real-time editing on these challenging models.

