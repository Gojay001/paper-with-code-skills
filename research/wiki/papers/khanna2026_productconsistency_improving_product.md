---
type: paper
node_id: paper:khanna2026_productconsistency_improving_product
title: "ProductConsistency: Improving Product Identity Preservation in Instruction-Based Image Editing via SFT and RL"
authors: ["Mukund Khanna", "Raj Singh Yadav", "Kunal Singh"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2606.19103"
  doi: null
  s2: null
tags: []
added: 2026-07-15T09:02:38Z
---

# ProductConsistency: Improving Product Identity Preservation in Instruction-Based Image Editing via SFT and RL

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

> Recent advances in instruction-based image editing have enabled models to perform complex visual edits from natural language instructions. However, in product-centric scenarios where preserving product features, branding, and textual elements are critical, current open and closed source models often struggle to maintain this fine-grained object identity. This issue is further compounded by the lack of datasets for instruction-based product image editing with text fidelity constraints, leaving it largely treated as an implicit capability of instruction-based image editing models. In this work, we introduce the ProductConsistency dataset which is designed to improve product-centric image editing. Our approach includes a supervised fine-tuning (SFT) dataset of 87k samples for product editing, a reinforcement learning (RL) dataset with 869 unique product images, and a new benchmark dataset, the ProductConsistency Benchmark, to allow rigorous and standardized evaluation of editing models. To guide RL training, we propose a Cyclic Consistency reward that enforces semantic preservation of product identity by using caption similarity between the original product description and captions generated from the edited image. We fine-tune both Qwen-Image-Edit-2511 and Flux.1-Kontext-dev using our dataset and demonstrate consistent improvements over baseline models in OCR and Perceptual metrics, and MLLM-based evaluations as well, indicating stronger product consistency, text rendering, and overall visual quality; with the Qwen-Image-Edit-2511 model achieving a 5x reduction in the character error rate. The code and pipeline is available at https://anonymous.4open.science/r/ProductConsistency-6FCC/README.md

