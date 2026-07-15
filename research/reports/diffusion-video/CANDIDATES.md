# Candidate Research Ideas

Generated from the local survey and deduplicated against the initial 2025–2026 neighborhood scan. Scores are pre-review hypotheses, not claims.

| ID | Candidate | Core falsifiable claim | Minimum pilot | Main novelty threat |
|---|---|---|---|---|
| I1 | Verb-Causal：跨帧文本注意力的因果干预 | verb attention 的时间相位若是动作中介，则置乱 verb 而保持边际分布会定向破坏轨迹；noun/background 对照不应有同等效应 | FancyVideo，8–16 prompts，冻结/置乱/跨 prompt 交换，光流+身份+画质 | “attention is not explanation” 很常见；需靠严格干预与负对照形成贡献 |
| I2 | ControlAtlas：视频 DiT 的层—步—时频控制相关性图谱 | 视频控制贡献在 layer、denoising step、temporal band 上高度非均匀，图谱可预测稀疏控制位置 | 小型开源 video DiT + 一个控制支路；3×3×2 分组消融 | Sparse-vDiT/USV 已做主干稀疏；必须限定为 condition branch 与 control adherence |
| I3 | Temporal-Curvature：Flow 视频的时间子空间曲率诊断 | 时间差分子空间曲率比全局曲率更能预测 flicker/动作断裂；只在其峰值加密步数会定向改善时序指标 | Wan2.1-1.3B 或同级 flow video model，20 prompts，记录轨迹，无训练 | CACFM 已用曲率调图像蒸馏；贡献必须是视频子空间机制而非泛化 adaptive sampler |
| I4 | DynamicControlDepth：条件误差驱动的控制层预算 | 早期条件遵循误差可预测样本需要的控制层数，动态 top-k 优于固定 top-k Pareto | RelaCtrl，40 Canny/Depth 样本，4/8/11 控制块 | DyDiT、USV、DynamicControl 临近；新颖性中等且可能被视为工程组合 |
| I5 | PhysicsShortcutAudit：物理 prior 的反事实捷径审计 | 真正使用定量先验时，连续数值变化应产生方向正确、平滑的轨迹变化；类别/词汇捷径则不会 | WISA，3 类×6 prompts×4 prior 版本，跟踪速度/位移 | 依赖权重和内部 prior 接口；若接口不开放则不可执行 |
| I6 | FourierOrthogonality：多参考融合正交假设压力测试 | 同类主体/相似纹理使特征相关性升高，Fourier 求和的遗漏率随参考数非线性恶化 | MoFu 特征或可替代原型，20 组参考，无训练 | 方法权重/代码未公开；只能做替代实现时结论外推有限 |

## Mechanical filter

- 移除“通用动态视频加速”：Sparse VideoGen、Sparse-vDiT、USV、DSA 已覆盖相当大范围。
- 移除“运动感知 proxy token”作为主选：与现有 motion-adaptive attention 和动态稀疏邻域过近。
- 移除“物理+文本双门控”作为主选：WISA/CausalMotion 等相邻工作使方法空间拥挤，且评测边界模糊。
- 保留 I1/I2/I3，因为三者都可先做**诊断型、无需训练或少训练的 falsification pilot**，失败结果也能产出明确结论。

## Independent jury result

| Rank | ID | Novelty | Impact | Feasibility | Falsifiability | Compute fit | Total / 25 | Decision |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | I1 | 3 | 4 | 5 | 5 | 5 | 22 | keep；把 claim 限定为“受控干预效应” |
| 2 | I3 | 3 | 4 | 4 | 5 | 4 | 20 | revise；删除 sampler 主贡献，先做诊断 |
| 3 | I2 | 3 | 5 | 3 | 4 | 3 | 18 | revise；必须证明 held-out 预测性 |
| 4 | I4 | 2 | 3 | 4 | 5 | 4 | 18 | backup；新颖性较低 |
| 5 | I5 | 4 | 4 | 1 | 5 | 2 | 16 | reject now；接口不可得 |
| 6 | I6 | 3 | 2 | 1 | 4 | 3 | 13 | reject；权重不可得且结论外推弱 |

评审新增的重要近邻：I1 必须区别于 [Understanding Attention Mechanism in Video Diffusion Models](https://arxiv.org/abs/2504.12027) 的一般 attention perturbation，以及 [AttentionBender](https://arxiv.org/abs/2604.20936) 的 cross-attention creative probe；I3 必须区别于 [Few-Step Diffusion Sampling Through Instance-Aware Discretizations](https://arxiv.org/abs/2603.17671) 在 video flow model 上的实例自适应时间离散。

最终建议：**I1 → I3 → I2**。I1 立即进入 pilot；I3 只保留归一化后的子空间曲率诊断；I2 先验证 atlas 能否预测 held-out 条件上的稀疏控制布局。
