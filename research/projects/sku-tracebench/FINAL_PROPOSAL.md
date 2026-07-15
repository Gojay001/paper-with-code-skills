# Final Proposal — SKU-TraceBench

## One-sentence contribution

建立首个面向生成电商视频的 SKU 版本级真实性压力测试：通过相似 SKU hard negatives、属性分解的时序轨迹和商业可发布性校准，测出通用主体相似度遗漏的商品事实错误。

## Why now

E-CommerceVideo 已建立商品图到视频任务，ConsID-Gen/3DreamBooth 正在提升多视图身份，DreamActor-H1 已进入人—商品演示；但这些路线缺少共同的商品事实 success gate。OpenS2V-Nexus 仍是主体级评价，ProductConsistency 仍是图像级。没有可靠评价，任何“商品保持”方法都容易被平均相似度掩盖。

## Method

1. **SKU truth schema:** 从目录字段、多视图图像、Logo/OCR 区域和人工确认建立几何、颜色、材质、文字、规格与版本真值。
2. **Hard-negative graph:** 为每个 SKU 连接同品牌、同系列、只在口味/容量/颜色/包装版本上不同的近邻。
3. **Visible product tubes:** 检测/跟踪视频中的商品及关键属性区域，区分可见、遮挡和参考未覆盖状态。
4. **Attribute trajectories:** 逐帧计算 geometry/color/material/logo/OCR/SKU margins，聚合 mean、worst frame、drift slope、occlusion recovery 和 cross-shot state consistency。
5. **Human calibration:** 盲评属性错误、可信度和是否可发布，验证自动指标的增量预测，而非仅报告指标间相关。

## Dominant ablation

- generic similarity only
- + hard negatives
- + attribute decomposition
- + temporal trajectory statistics
- + visibility/reference-coverage awareness

只有最后三项在 held-out SKU 上带来稳定增量，才支持完整贡献。

## Feasibility

M0 不需要训练大型视频模型，可先用可控 corruption 和已有生成样本验证。M1 需要至少两个公开 I2V family 的输出；当前本机无 CUDA，生成需要后续 GPU 环境。没有 pilot 结果时保持 proposal 状态。

## Follow-on method

若 benchmark 成立，下一阶段用其训练/验证 Evidence-Bounded Camera：预测镜头轨迹的 SKU 风险，在固定风险预算下选择轨迹、补充参考或拒绝生成。
