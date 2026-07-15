# Research Contract: Verb-Causal

> Active working document for the selected idea. Load this file on session recovery instead of the full candidate pool.

## Selected Idea

- **Description**: 对视频生成 cross-frame attention 做 token-specific、matched-statistics 干预，检验 verb-token 时间结构是否对运动具有超出 noun/background/random 对照的特异效应。
- **Source**: `research/reports/diffusion-video/IDEA_REPORT.md`, Idea #1。
- **Selection rationale**: 独立 jury 22/25（最高）；假设最可证伪、无需重新训练主模型、M0 可限制在 2 GPU-hours。没有 pilot 结果，选择依据是问题质量、可执行性和明确 kill gate。

## Core Claims

1. **C1**: 匹配 energy、entropy、token length 和扰动强度后，verb temporal intervention 对 motion 的效应大于 noun/background/random controls。
2. **C2**: 若 C1 成立，该效应在部分 layer 或 denoising stage 更强，而非均匀分布。
3. **C3**: 若 perceptual degradation、camera motion 或统计量失配可解释效应，则不主张 motion-specific mechanism。

## Method Summary

在 FancyVideo 的 CTGM / cross-attention 路径记录 verb、subject noun、background token 的逐帧 attention scores。对相同 prompt 和 paired noise seed，分别执行 identity、verb freeze、verb temporal phase permutation、noun/background/random-token permutation，以及 matched random orthogonal perturbation。

每个干预重标定 attention energy 和 entropy，并检查时间平滑度与 token 长度。输出端用主体 residual optical flow、方向一致性和轨迹平滑度度量 motion，同时用 DINO/LPIPS 或等价指标记录身份和感知损伤。分析预注册 verb-vs-pooled-controls contrast，并把 perceptual damage 作为协变量；不以单张 attention 可视化支持 claim。

## Experiment Design

- **Datasets**: 无训练数据；8 个预注册固定镜头动作 prompt，pilot 2 seeds；M2 使用 4 个 held-out prompts。
- **Baselines**: original、identity hook、noun/background/random token permutation、random orthogonal perturbation、unmatched naive permutation。
- **Metrics**: primary = subject residual-flow direction agreement；secondary = flow magnitude、trajectory smoothness、DINO identity、LPIPS/perceptual quality、global camera flow。
- **Key hyperparameters**: intervention strength、phase permutation、layer group、denoising-stage window；M0 固定，不事后挑选。
- **Compute budget**: M0 ≤2 GPU-hours；full must-run 预计 4–8 GPU-hours。当前 Apple M4 Max 环境不作为 CUDA 成本证据。

## Baselines

| Method | Dataset | Metric | Score | Source |
|---|---|---|---|---|
| FancyVideo original | pre-registered prompts | all local metrics | pending reproduction | paper/repo; do not copy paper headline metrics into this contract |
| Identity hook | same prompts / paired seeds | output delta | pending | internal sanity baseline |
| Pooled negative controls | same prompts / paired seeds | motion + quality | pending | proposed protocol |

## Current Results

> No experiments were run during idea discovery. Do not convert feasibility estimates into results.

| Method | Dataset | Metric | Score | Notes |
|---|---|---|---|---|
| — | — | — | — | NOT RUN |

## Key Decisions

- Use “controlled intervention effect,” not “complete causal mediation.”
- Keep one dominant contribution: the diagnostic protocol; no new controller or model training in phase 1.
- Run M0 sanity and negative controls before expanding prompts or seeds.
- Kill the idea if verb effect does not exceed matched controls or is explained by perceptual damage.

## Status

- [x] Idea selected
- [ ] Baseline reproduced
- [ ] Main method implemented
- [ ] Representative dataset results
- [ ] Full dataset results
- [ ] Ablation studies
- [ ] Paper draft

## Next-Step Pointer

Run `research/projects/verb-causal/EXPERIMENT_PLAN.md` starting at R001. After results, use `/result-to-claim`; do not advance positive claims from this contract alone.

