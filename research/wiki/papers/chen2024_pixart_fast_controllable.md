---
type: paper
node_id: paper:chen2024_pixart_fast_controllable
title: "PIXART-δ: Fast and Controllable Image Generation with Latent Consistency Models"
authors: ["Junsong Chen", "Yue Wu", "Simian Luo", "Enze Xie", "Sayak Paul", "Ping Luo", "Hang Zhao", "Zhenguo Li"]
year: 2024
venue: "arXiv"
external_ids:
  arxiv: "2401.05252"
  doi: null
  s2: null
tags: []
added: 2026-07-15T04:12:36Z
---

# PIXART-δ: Fast and Controllable Image Generation with Latent Consistency Models

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

> This technical report introduces PIXART-δ, a text-to-image synthesis framework that integrates the Latent Consistency Model (LCM) and ControlNet into the advanced PIXART-α model. PIXART-α is recognized for its ability to generate high-quality images of 1024px resolution through a remarkably efficient training process. The integration of LCM in PIXART-δ significantly accelerates the inference speed, enabling the production of high-quality images in just 2-4 steps. Notably, PIXART-δ achieves a breakthrough 0.5 seconds for generating 1024x1024 pixel images, marking a 7x improvement over the PIXART-α. Additionally, PIXART-δ is designed to be efficiently trainable on 32GB V100 GPUs within a single day. With its 8-bit inference capability (von Platen et al., 2023), PIXART-δ can synthesize 1024px images within 8GB GPU memory constraints, greatly enhancing its usability and accessibility. Furthermore, incorporating a ControlNet-like module enables fine-grained control over text-to-image diffusion models. We introduce a novel ControlNet-Transformer architecture, specifically tailored for Transformers, achieving explicit controllability alongside high-quality image generation. As a state-of-the-art, open-source image generation model, PIXART-δ offers a promising alternative to the Stable Diffusion family of models, contributing significantly to text-to-image synthesis.

