# E-Commerce Video Idea Discovery Report

**Direction:** 电商视频生成：商品真实性、镜头控制与广告叙事  
**Date:** 2026-07-15  
**Pipeline:** research-lit → idea-creator → novelty-check → research-review → research-refine-pipeline  
**Review mode:** same-family provisional；独立只读 jury；未运行 GPU pilot

## Executive Summary

本轮把电商视频专题扩展到 76 篇论文节点，其中包括商品图直生视频、人—商品演示、广告分镜/剪辑、品牌植入、商业意图理解、多视图身份和商品插入。结论是：领域已经解决了“让商品出现在视频里”的多个子问题，但尚未可靠解决“生成内容是否仍是正在售卖的那个 SKU”。

推荐先推进 **SKU-TraceBench**，用相似 SKU hard negatives、逐属性时序轨迹和未观测视角压力测试建立商业级真实性评价；再以此支持方法型 Idea **Evidence-Bounded Camera**，让镜头运动受参考证据和可校准身份风险约束。当前没有运行实验，也没有报告正面结果。

完整综述见 `research/wiki/ECOMMERCE_VIDEO.md`，稳定空白见 `research/wiki/gap_map.md` 的 G11–G20。

## Landscape

1. **商品图 → 展示视频：** E-CommerceVideo 建立直接任务和数据；VideoBooth、ConsID-Gen、3DreamBooth 从主体、多视图与 3D 角度提高身份保持。
2. **人物—商品演示：** AnchorCrafter 与 DreamActor-H1 已联合人物、商品、动作和遮挡；剩余难点是商品 affordance、精细接触、功能状态和包装事实。
3. **广告规划/剪辑：** Narrative Weaver 生成长程分镜；VC-LLM、Tree-of-AdEditor、AutoCut 从真实素材生成成片。像素生成与素材编排仍未统一。
4. **卖点/品牌：** KD-CVG 注入广告知识，BrandFusion 优化品牌植入，E-VAds/AD-MIR 提供商业意图理解；但理解分数尚未被证明是安全的生成奖励。
5. **生成—真实混合：** PLACID、InsertAnywhere、SimInsert、Point2Insert 支持对象插入，但自然融合指标不等于 SKU 正确。

## Ranked Ideas

### 1. SKU-TraceBench — RECOMMENDED

- **Hypothesis:** 相比通用 CLIP/DINO/VBench，显式分解几何、颜色、材质、Logo、OCR、规格和 SKU 版本，并报告逐帧漂移与 hard-negative margin，会更准确预测“商业可发布”判断。
- **Dominant contribution:** SKU-version-level video fidelity benchmark；不是更多生成模块。
- **Stress axes:** 相似 SKU 交换、未观测视角、遮挡恢复、运动/相机幅度、分辨率/压缩、跨 shot 状态。
- **Closest work:** E-CommerceVideo 已定义任务；OpenS2V-Nexus/ConsIDVid-Bench 评主体或多视图一致性；ProductConsistency 评图像商品编辑。
- **Required differentiation:** 近邻 SKU 可判别、属性级时序失真、与盲人评可发布率的校准。
- **Jury:** 22/25, KEEP。
- **Success gate:** 组合指标在 held-out SKU 上对人工不可发布判断的 AUROC 至少比最强通用相似度基线高 0.10，并能稳定区分同品牌近邻 SKU。
- **Kill gate:** 简单 DINO/CLIP + OCR 已达到同等相关性；或指标只检测人工合成 corruption，不能解释真实模型失败。

### 2. Evidence-Bounded Camera — TOP METHOD IDEA

- **Hypothesis:** 目标视角相对参考视图覆盖越低，身份风险越高；经校准的风险模型可在固定 SKU 风险下，选择 orbit/pan/push-in 幅度、请求补充视图或 abstain，从而最大化安全动态性。
- **Dominant contribution:** risk-constrained camera generation with abstention；不是新的多视图 encoder。
- **Closest work:** ConsID-Gen、3DreamBooth 已做多视图身份，CameraCtrl/MotionCtrl 已做镜头控制，但两条线通常独立评测。
- **Required differentiation:** risk-coverage calibration、未观测表面错误率、同风险下最大镜头运动范围。
- **Jury:** 21/25, REVISE。
- **Success gate:** held-out SKU 上 calibration error 可接受，且相同人工 SKU 错误率下显著增加镜头运动，或相同运动下显著降低错误。
- **Kill gate:** 风险只由参考图数量或相机角度启发式决定；跨品类不校准；安全策略只是把视频冻结。

### 3. Risk-Routed Product Lock — SYSTEM BACKUP

- **Hypothesis:** 根据商品属性、目标视角、遮挡和文字区域预测事实风险，并在 retain/warp/insert/generate 之间做时空路由，可优于固定 mask、全生成和全插入。
- **Closest work:** PLACID、InsertAnywhere、SimInsert 与常规生成式合成。
- **Jury:** 19/25, REVISE。
- **Boundary:** 只有学习式风险分配器和跨 SKU 泛化可构成贡献；“OCR critic + 重生成”本身不够新。

### 4. Product-Frequency Router — ARCHIVED

把低频几何、中频材质、高频 Logo/OCR 路由到不同层和时间步。ConsisID 已做人脸身份分频，InnoAds-Composer 已做条件重要性路由。独立 jury 给 16/25；除非先通过干预证明商品属性有稳定、可泛化的路由规律，否则不推进。

## Novelty Boundary

| Idea | Already covered | Remaining defensible claim |
|---|---|---|
| SKU-TraceBench | 电商视频数据、通用主体/多视图指标、图像商品一致性 | SKU 版本级 hard negatives + 属性时序轨迹 + 商业可用性校准 |
| Evidence-Bounded Camera | 多视图/3D 身份；相机轨迹控制 | 可校准身份风险约束、risk-coverage、abstention |
| Risk-Routed Product Lock | 对象插入、mask 合成、背景保持 | 学习式事实风险路由，而非固定区域流水线 |
| Product-Frequency Router | 人脸频率分解、条件路由 | 当前无足够边界，已停止 |

## Critical Review

最大的反对意见是 benchmark inflation：如果只是把 OCR、Logo、颜色分数相加，SKU-TraceBench 不构成研究贡献。修订后必须满足：

1. 使用同品牌、同包装家族、仅容量/口味/颜色不同的 hard negatives。
2. 把错误定位到可见轨迹，并报告平均分之外的最坏帧、漂移斜率和遮挡后恢复。
3. 区分参考已覆盖表面与未覆盖表面，避免用不可验证的背面“看起来像”冒充正确。
4. 以盲人评的属性错误和可发布判断校准，而非只与另一个自动指标相关。
5. 在真实生成失败和可控 corruption 两类数据上都成立；只在合成错误上有效则终止。

## Refined Proposal

- Proposal: `research/projects/sku-tracebench/FINAL_PROPOSAL.md`
- Review summary: `research/projects/sku-tracebench/REVIEW_SUMMARY.md`
- Experiment plan: `research/projects/sku-tracebench/EXPERIMENT_PLAN.md`
- Tracker: `research/projects/sku-tracebench/EXPERIMENT_TRACKER.md`
- Contract: `research/projects/sku-tracebench/research_contract.md`

## Next Steps

- [ ] 先收集 30–50 个许可清晰、含相似变体和多视图的 SKU，定义属性真值与可见区域。
- [ ] 仅做 corruption sanity：字符替换、Logo warp、色偏、局部几何和跨帧漂移，验证每个子指标的单调性。
- [ ] 再评估至少两个公开 I2V 基座的真实输出；当前本机无 CUDA，不宣称已运行。
- [ ] 进行盲人评并验证对可发布判断的增量预测；失败即停止 benchmark claim。
- [ ] 只有 SKU-TraceBench gate 通过后，启动 Evidence-Bounded Camera。
