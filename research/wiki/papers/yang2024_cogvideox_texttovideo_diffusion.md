---
type: paper
node_id: paper:yang2024_cogvideox_texttovideo_diffusion
title: "CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer"
authors: ["Zhuoyi Yang", "Jiayan Teng", "Wendi Zheng", "Ming Ding", "Shiyu Huang", "Jiazheng Xu", "Yuanming Yang", "Wenyi Hong", "Xiaohan Zhang", "Guanyu Feng", "Da Yin", "Yuxuan Zhang", "Weihan Wang", "Yean Cheng", "Bin Xu", "Xiaotao Gu", "Yuxiao Dong", "Jie Tang"]
year: 2024
venue: "arXiv"
external_ids:
  arxiv: "2408.06072"
  doi: null
  s2: null
tags: []
added: 2026-07-15T04:12:36Z
---

# CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer

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

> We present CogVideoX, a large-scale text-to-video generation model based on diffusion transformer, which can generate 10-second continuous videos aligned with text prompt, with a frame rate of 16 fps and resolution of 768 * 1360 pixels. Previous video generation models often had limited movement and short durations, and is difficult to generate videos with coherent narratives based on text. We propose several designs to address these issues. First, we propose a 3D Variational Autoencoder (VAE) to compress videos along both spatial and temporal dimensions, to improve both compression rate and video fidelity. Second, to improve the text-video alignment, we propose an expert transformer with the expert adaptive LayerNorm to facilitate the deep fusion between the two modalities. Third, by employing a progressive training and multi-resolution frame pack technique, CogVideoX is adept at producing coherent, long-duration, different shape videos characterized by significant motions. In addition, we develop an effective text-video data processing pipeline that includes various data preprocessing strategies and a video captioning method, greatly contributing to the generation quality and semantic alignment. Results show that CogVideoX demonstrates state-of-the-art performance across both multiple machine metrics and human evaluations. The model weight of both 3D Causal VAE, Video caption model and CogVideoX are publicly available at https://github.com/THUDM/CogVideo.

