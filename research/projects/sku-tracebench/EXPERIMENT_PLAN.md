# Experiment Plan — SKU-TraceBench

## M0: metric sanity（CPU/轻量，先做）

- 30–50 SKU，每个至少 2 个近邻变体、3–6 个视图。
- 从真实商品图/短视频构造单因素 corruption：字符替换、Logo warp、局部色偏、轮廓变形、纹理替换、跨帧渐进漂移、遮挡后错误恢复。
- 检查每个子指标是否对目标错误单调、对非目标变化相对不敏感。
- Kill：明显无法区分同品牌近邻 SKU，或错误类型强串扰。

## M1: real generation failures

- 至少两个独立开源 I2V family；每 SKU 统一镜头模板与 paired seeds。
- 镜头：static/push-in/pan/orbit-small/orbit-large；按参考覆盖区分 observed/unobserved surface。
- 输出固定版本、分辨率、采样参数和随机种子；不得只保留好样本。
- 比较 generic similarity、OCR/Logo 单项、简单组合与完整时序协议。

## M2: blind human calibration

- 每段视频至少 3 名评审；先看商品真值资产，再看匿名输出。
- 标签：各属性是否错误、错误最严重帧、可信度、是否可发布、主要拒绝原因。
- 报告一致性、置信区间、按品类/材质/运动分层结果。

## M3: external validity

- held-out 类别与长尾材质；同品牌相似 SKU 专项。
- 视频压缩、降采样和 OCR 不可读时的 abstention/calibration。
- 若可获得 E-CommerceVideo 或 ConsIDVid 测试集，做外部重现；不可获得时明确限制。

## Statistics

- SKU-level bootstrap，禁止把帧当独立样本夸大 n。
- 主指标预注册：不可发布 AUROC 增量与 hard-negative retrieval margin。
- 次指标：macro-F1、Spearman、ECE、worst-frame recall。
- 多重比较使用 Holm 校正；同时报告效应量和 95% CI。

## Compute

- M0 可本地运行；M1 需要 GPU/现成输出。
- 首轮 GPU pilot 上限建议 4 GPU-hours；未确认环境前不启动。
