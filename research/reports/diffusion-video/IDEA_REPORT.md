# Idea Discovery Report

**Direction**: Diffusion × Video Generation，基于 `paper-with-code-list.md` 与 `paper-reading/` 形成综述 wiki 并产出可执行 idea  
**Date**: 2026-07-15  
**Pipeline**: research-lit → idea-creator → novelty-check → research-review → research-refine-pipeline  
**Review mode**: same-family provisional（独立只读 jury；未调用外部异构模型）

## Executive Summary

本轮把 45 篇核心与近期相邻论文纳入 `research/wiki/`，从 16 个原始候选机械去重到 6 个，再经近期文献检查和独立评审收敛为 3 个可保留方向。首选是 **Verb-Causal：跨帧文本注意力的受控干预效应**：不声称“attention 就是解释”，而是用 matched-energy / matched-entropy 的 verb、noun、background 与随机变换对照，检验 verb-token attention 是否对运动具有特异干预效应。

当前没有运行 GPU pilot，也没有报告任何虚构结果。推荐下一步先完成不超过 2 GPU-hours 的 M0 falsification pilot；若 verb 干预相对负对照没有特异效应，立即停止该方向并切换至 Temporal-Curvature 诊断。

## Literature Landscape

### 生成主干

- DDPM/DDIM 建立噪声预测和少步采样基础；LDM 将生成搬到感知 latent。
- Flow Matching / Rectified Flow 以连续速度场和更直路径降低训练/采样难度；SD3 把 RF 与 MM-DiT 扩展到大规模图像生成。
- CogVideoX、Wan2.1 说明视频生成依赖时空 VAE、长序列 DiT/Flow、训练课程和 dense caption 的系统协同，而非单一模块。

### 控制与效率

- ControlNet → PixArt-δ → RelaCtrl：控制接口从完整副本转向 relevance-guided 稀疏条件分支。
- FancyVideo：帧特异文本条件改善运动；WISA：结构化物理条件；MoFu：多主体尺度和参考顺序；Lay2Story：布局可切换故事生成。
- 效率有四个正交杠杆：latent 压缩、路径/步数、主干 attention、条件分支。Sparse VideoGen、Sparse-vDiT、USV、DSA 与 instance-aware discretization 已使“泛化动态加速”高度拥挤。

完整综述见 `research/wiki/SUMMARY.md`；稳定研究空白见 `research/wiki/gap_map.md`。

## Ranked Ideas

### 1. Verb-Causal：跨帧文本注意力的受控干预效应 — RECOMMENDED

- **Hypothesis**：在保持 attention 范数、熵与时间边际统计时，置乱 verb-token 的时间相位会定向改变动作轨迹；noun、background、random-token 与随机正交变换不应产生同等效应。
- **Dominant contribution**：针对 verb-token 的严格负对照干预协议与可证伪诊断，而非新的 attention 模块。
- **Pilot**：NOT RUN。设计为 8 个动作 prompt × 2 seeds × 6 interventions；FancyVideo；目标 ≤2 GPU-hours。
- **Novelty**：CONDITIONAL。近邻 [Understanding Attention Mechanism](https://arxiv.org/abs/2504.12027) 已做一般空间/时间 attention 扰动，[AttentionBender](https://arxiv.org/abs/2604.20936) 已做 Video DiT cross-attention 操纵。剩余区分点是 verb 特异、边际统计匹配、严格负对照与 motion-specific outcome。
- **Jury**：22/25；KEEP。最大风险是所有 attention 扰动都只造成分布外画质破坏。
- **Success gate**：verb 时间置乱对 motion-direction / tracked displacement 的效应显著大于 noun/background/random 对照，同时画质下降不显著更大。
- **Kill gate**：效应可由 attention energy、entropy 或总体画质下降解释；或跨 seed/prompt 不稳定。

### 2. Temporal-Curvature：Flow 视频的时间子空间曲率诊断 — BACKUP A

- **Hypothesis**：在归一化 latent scale、camera motion 与 codec 后，时间差分子空间曲率对 flicker/动作断裂具有超出全局曲率、速度范数、local truncation error 与帧置信度的增量预测力。
- **Pilot**：NOT RUN。20 prompts，记录 20–30 步 flow trajectory，无训练。
- **Novelty**：CONDITIONAL。CACFM、DSA 和 [instance-aware discretization](https://arxiv.org/abs/2603.17671) 已覆盖自适应采样，因此 sampler 被降为可选下游验证，主贡献只保留子空间诊断。
- **Jury**：20/25；REVISE。最大风险是“曲率”只是坐标、有限差分或镜头运动伪量。
- **Gate**：held-out prompt 上的增量预测显著，且对 codec/checkpoint 稳健。

### 3. ControlAtlas：视频 DiT 的层—步—时频控制相关性图谱 — BACKUP B

- **Hypothesis**：低成本 condition-branch probe 得到的 layer × denoising-step × temporal-band atlas，能在 held-out prompt/condition 上预测有效的稀疏控制布局。
- **Pilot**：NOT RUN。先做 3×3×2 分组消融，不训练新主干。
- **Novelty**：CONDITIONAL。主干 attention 稀疏和层/步探测拥挤；区别必须限定在 condition branch、control adherence、temporal frequency 和 held-out 预测性。
- **Jury**：18/25；REVISE。最大风险是只得到描述性热图，不能跨条件预测。
- **Gate**：相同 FLOPs 下优于随机、均匀和 layer-only placement。

### 4. DynamicControlDepth — BACKUP ONLY

早期条件遵循误差驱动的动态控制深度。Pilot 便宜且可证伪，但与 RelaCtrl、DyDiT、DynamicControl、USV 的组合痕迹明显；仅当 ControlAtlas 无法落地时保留。Jury 18/25。

## Eliminated Ideas

- **PhysicsShortcutAudit**：科学问题有价值，但 WISA 的可编辑 29 维 prior 和内部路由接口尚未确认；当前 feasibility 1/5，等待官方接口。
- **FourierOrthogonality**：MoFu 权重/特征不可得；证伪启发式“近似正交”也不能直接否定方法，外推价值弱。
- **Motion-aware proxy / generic dynamic acceleration**：被 Sparse VideoGen、Sparse-vDiT、USV、DSA 和 motion-adaptive attention 明显挤压。
- **四步视频蒸馏、adaptive VAE、多条件物理门控**：工程成本或邻域拥挤度过高，不适合本轮低成本首个 pilot。

## Novelty Boundary

| Idea | Closest work | What is already covered | Required differentiation |
|---|---|---|---|
| Verb-Causal | Understanding Attention Mechanism; AttentionBender; FancyVideo | 一般 attention 扰动、cross-attention 操纵、帧特异文本引导 | verb 特异、统计匹配、负对照、motion outcome、paired seeds |
| Temporal-Curvature | CACFM; Few-Step Instance-Aware Discretization; DSA | 曲率关键区、实例自适应 timestep、按帧动态步数 | 空间/时间子空间的归一化诊断与增量预测，不以 sampler 为主 claim |
| ControlAtlas | RelaCtrl; Causality in Video Diffusers; Sparse-vDiT; USV | 图像控制层相关性、视频层/步冗余、主干稀疏 | condition branch × control adherence × temporal frequency × held-out layout prediction |

## Critical Review and Revision

独立 jury 的最强批评是：I1 的 attention 置乱可能只证明“该张量参与网络”，并不能证明 verb attention 是动作的完整因果中介。修订后采用以下约束：

1. 论文第一阶段只主张 **controlled intervention effect**。
2. 所有干预匹配 L2 energy、entropy、token length 和时间平滑度。
3. 加入 noun、background、random token、random orthogonal transform 与全局画质破坏对照。
4. 使用 paired seeds；motion 与 perceptual degradation 分开建模。
5. 若效应不能跨 prompt/seed 泛化，方向终止，不升级为新方法。

## Refined Proposal

- Proposal: `research/projects/verb-causal/FINAL_PROPOSAL.md`
- Review summary: `research/projects/verb-causal/REVIEW_SUMMARY.md`
- Experiment plan: `research/projects/verb-causal/EXPERIMENT_PLAN.md`
- Tracker: `research/projects/verb-causal/EXPERIMENT_TRACKER.md`
- Active research contract: `research/projects/verb-causal/research_contract.md`

## Next Steps

- [ ] 获取可运行 FancyVideo checkpoint 与 attention hook，确认单次生成耗时。
- [ ] 运行 R001–R003 的 M0 sanity / matched-statistics / negative-control pilot。
- [ ] 仅在 M0 通过后扩展 prompt 与 seeds；否则切换 Temporal-Curvature。
- [ ] 实验完成后运行 `/result-to-claim` 与 `/ablation-planner`，不要提前写正面结论。

