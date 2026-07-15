# Experiment Plan

**Problem**: 区分 verb-token 的跨帧 attention 是否具有 motion-specific 受控干预效应，而非一般 attention 破坏。  
**Method Thesis**: 在匹配 attention 统计量与扰动强度后，verb temporal intervention 若仍比 noun/background/random 对照更强地改变运动，则支持一个收窄、可证伪的机制 claim。  
**Date**: 2026-07-15

## Claim Map

| Claim | Why It Matters | Minimum Convincing Evidence | Linked Blocks |
|---|---|---|---|
| C1 verb-specific effect | 区别于一般 attention perturbation | verb × intervention interaction 超过 pooled negative controls，且控制画质退化后仍存在 | B1, B2, B3 |
| C2 localized mechanism | 避免“所有层/步都一样”的空泛结论 | 至少一个 stage/layer window 显示更强效应，held-out prompt 方向一致 | B4 |
| C3 honest boundary | 防止把分布外破坏误称因果机制 | matched-statistics 检查；若不通过则明确 invalidation | B1, B5 |

## Paper Storyline

- Main paper must prove: 严格受控的 verb intervention 相对负对照是否存在 motion-specific effect。
- Appendix can support: tokenization audit、更多 prompts、层/步 window、替代 motion metric。
- Experiments intentionally cut: 新 controller 训练、长视频 SOTA、全模型 ControlAtlas、多数据集大扫榜。

## Experiment Blocks

### Block 1: Hook and Statistical-Matching Sanity

- Claim tested: C3
- Why this block exists: 先证明能准确读取/重写目标 attention，并保持非目标统计量。
- Dataset / split / task: 2 个固定镜头动作 prompt，1 seed，短视频。
- Compared systems: original、identity hook、verb phase permutation、matched random orthogonal perturbation。
- Metrics: tensor equality、L2 energy ratio、entropy delta、temporal smoothness delta、输出像素差。
- Setup details: identity hook 输出必须数值一致；干预后 energy 误差目标 ≤1%，entropy 误差目标 ≤2%。
- Success criterion: identity 无可见变化；匹配误差达标；单次生成成本允许 M0 总预算 ≤2 GPU-hours。
- Failure interpretation: hook 或统计匹配不可用，停止主线并换模型/实现。
- Table / figure target: Sanity table + intervention schematic。
- Priority: MUST-RUN

### Block 2: Minimal Falsification Matrix

- Claim tested: C1, C3
- Why this block exists: 用最小矩阵判断 verb 是否有特异效应。
- Dataset / split / task: 8 个预注册固定镜头动作 prompt，2 paired seeds。
- Compared systems: original、verb freeze、verb phase permutation、noun permutation、background permutation、random-token permutation。
- Metrics: subject residual-flow magnitude、direction agreement、trajectory smoothness、DINO identity、LPIPS/perceptual quality。
- Setup details: token spans 人工核对；每个 seed 跨干预共享初始噪声。
- Success criterion: verb intervention 对至少一个预注册 motion metric 的效应大于 pooled controls，且在控制 perceptual degradation 后仍方向一致。
- Failure interpretation: 若所有 token 同等破坏、或质量下降解释 motion 变化，则 C1 不成立。
- Table / figure target: Main effect table + paired effect plot。
- Priority: MUST-RUN

### Block 3: Negative-Control and Metric Robustness

- Claim tested: C1
- Why this block exists: 排除范数、熵、token 长度与 camera flow 的替代解释。
- Dataset / split / task: 与 B2 相同；仅对 B2 有信号的配置运行。
- Compared systems: matched-energy、matched-entropy、matched-token-length、random orthogonal、全局 camera-motion subtraction。
- Metrics: B2 metrics + global camera flow + confidence intervals。
- Success criterion: verb-specific interaction 对匹配策略与 camera subtraction 稳健。
- Failure interpretation: 信号是统计量或镜头运动伪影，降级或否定 claim。
- Table / figure target: Robustness table。
- Priority: MUST-RUN

### Block 4: Layer / Denoising-Stage Localization

- Claim tested: C2
- Why this block exists: 检验 effect 是否局部化，提供机制边界。
- Dataset / split / task: B2 中 4 个代表 prompt，2 seeds。
- Compared systems: early/mid/late steps × shallow/mid/deep layer group 的 verb phase intervention。
- Metrics: B2 motion/perceptual metrics。
- Success criterion: 至少一个窗口显著高于其余窗口，并在 held-out prompt 保持方向。
- Failure interpretation: effect 全局分散；保留 C1，删除 C2。
- Table / figure target: 2D heatmap。
- Priority: NICE-TO-HAVE，M0 通过后运行

### Block 5: Reproduction / Deletion Checks

- Claim tested: C1, C3
- Why this block exists: 验证 FancyVideo 基线与删除核心控制后的结论边界。
- Dataset / split / task: B2 prompts。
- Compared systems: original FancyVideo、identity hook、unmatched naive permutation、matched protocol。
- Metrics: 全部主指标。
- Success criterion: identity hook 复现；naive 与 matched 结论差异能说明控制协议必要性。
- Failure interpretation: hook 自身改行为或 matched protocol 无新增信息。
- Table / figure target: Ablation table。
- Priority: MUST-RUN

## Run Order and Milestones

| Milestone | Goal | Runs | Decision Gate | Cost | Risk |
|---|---|---:|---|---|---|
| M0a | 环境、checkpoint、identity hook | R001 | identity 输出一致 | 0.2–0.5 GPU-h | 权重/依赖不可用 |
| M0b | 统计量匹配 | R002 | energy ≤1%，entropy ≤2% | 0.2–0.5 GPU-h | rescaling 破坏局部结构 |
| M0c | 最小负对照矩阵 | R003 | verb effect > controls，或明确否定 | 0.8–1.0 GPU-h | 生成速度超预算 |
| M1 | 扩展 8 prompts × 2 seeds | R004–R006 | paired effect 稳定 | 2–6 GPU-h | 方差大 |
| M2 | stage/layer localization | R007–R009 | held-out 方向一致 | 2–4 GPU-h | 无局部化 |

## Compute and Data Budget

- Pilot hard cap: **2 GPU-hours per GPU** for M0；超出则标记 `needs manual pilot`，本轮不自动运行。
- Full must-run estimate after M0: 4–8 GPU-hours，取决于 checkpoint 与分辨率。
- Data preparation: 8–24 个预注册 prompt；无需训练数据。
- Human evaluation: pilot 不需要；若自动 motion/quality 指标冲突，再做小型盲评。
- Biggest bottleneck: FancyVideo 依赖和 attention hook 可用性；当前 Apple M4 Max 环境不等价于 CUDA GPU 实验环境。

## Risks and Mitigations

- Distribution shift: matched statistics + random orthogonal control + identity hook。
- Camera motion confound: 固定镜头 prompt + global-flow subtraction。
- Tokenization ambiguity: 固定模板 + tokenizer span audit。
- Multiple comparisons: 预注册 primary metric 和 pooled-control contrast；其余作为 exploratory。
- Weak effect: paired seeds、bootstrap CI；不通过即停止，不扩大样本“追显著”。

## Final Checklist

- [x] Main paper tables are covered
- [x] Novelty is isolated
- [x] Simplicity is defended
- [x] Frontier contribution is explicitly not claimed
- [x] Nice-to-have runs are separated from must-run runs

