# Final Proposal: Verb-Causal

**Problem Anchor**: 现有视频生成工作显示帧特异文本条件与跨帧 attention 操作能改变动作和一致性，但尚不清楚 verb-token 的时间结构是否对运动具有超出一般 attention 破坏的特异作用。  
**Verdict**: READY FOR FALSIFICATION PILOT  
**Date**: 2026-07-15

## Final Method Thesis

构建一套统计量匹配的 token-level attention intervention protocol：在保持 attention 的 L2 energy、entropy、token length、时间边际分布和总体扰动强度时，分别冻结、时间相位置乱或跨 prompt 交换 verb、noun、background 与随机 token。若 verb 干预相对负对照对 tracked motion direction / displacement 产生稳定的特异效应，而视觉质量下降没有同等放大，则支持“verb-token cross-frame attention 对生成运动具有可测的受控干预效应”。

## Dominant Contribution

不是新 attention 层，也不是把 attention map 当解释；唯一主贡献是一个**可证伪、统计匹配、带严格负对照的视频文本—运动机制诊断协议**。

## Method

1. 在 FancyVideo 的 CTGM / cross-attention 路径定位 verb、subject noun、background token 的跨帧 attention scores。
2. 构造六组干预：original、verb temporal freeze、verb phase permutation、noun permutation、background permutation、matched random orthogonal perturbation。
3. 对每个干预进行 energy/entropy rescaling，保持 attention score 的边际统计和扰动幅度一致；同一 prompt 使用 paired noise seed。
4. 用光流/跟踪器得到 motion magnitude、direction agreement、trajectory smoothness；用 DINO/LPIPS 或等价指标记录主体与感知质量。
5. 用 mixed-effects 或 paired bootstrap 分离 token type × intervention 的交互效应和总体质量退化。

## Claims

- **C1（主 claim）**：匹配统计量后，verb-token 时间结构的干预对运动指标有大于 noun/background/random 对照的特异效应。
- **C2（机制边界）**：该效应集中在特定去噪阶段或层，而不是所有 cross-attention 均匀产生。
- **C3（限制性 claim）**：若画质破坏可以完全解释运动变化，则 attention 只被证明参与计算，不能称为 motion-specific mechanism。

## Minimum Convincing Evidence

- ≥8 动作 prompt、≥2 paired seeds、完整负对照。
- 干预前后的 energy、entropy、扰动范数匹配检查通过。
- verb vs pooled negative controls 的 motion effect 方向稳定，并在 bootstrap 置信区间上分离。
- perceptual degradation 作为协变量后，verb-specific interaction 仍存在。
- 至少一次层或去噪阶段 deletion check，排除“所有位置都一样”的解释。

## Intentionally Rejected Complexity

- 不训练新的 attention controller。
- 不把 I2 ControlAtlas 全部并入首个实验。
- 不在 pilot 阶段加入新数据集或长视频 benchmark。
- 不声称完整因果中介，不声称改进 SOTA 生成质量。

## Main Risks

- FancyVideo 权重、hook 或运行成本不可用：先做环境与单样本 M0，失败即切换到可 hook 的公开视频模型。
- attention 扰动分布外：通过 matched-statistics 与随机正交对照诊断。
- verb tokenization 不稳定：预注册 prompt 模板并人工核对 tokenizer spans。
- motion metric 被镜头运动污染：使用固定镜头 prompt，并分离全局 camera flow 与主体 residual flow。

## Next Action

执行 `research/projects/verb-causal/EXPERIMENT_PLAN.md` 的 R001–R003；任何正面结果在 `/result-to-claim` 前都只记为 pilot signal。

