# Research Contract — SKU-TraceBench

**Status:** active proposal; no experiment executed  
**Primary question:** 通用视频/主体相似度是否系统漏检 SKU 版本级错误，而属性分解的时序评价能否更准确预测商业不可发布？

## Claim boundary

- 允许主张：在明确数据、模型和人评协议内，所提评价更能检测 SKU 事实错误或预测可发布判断。
- 不允许主张：评价提高 CTR/转化；评价适用于所有国家/品类；自动分数等同法律合规。
- 在 pilot 通过前，不写“显著优于”“可靠解决”或任何正面结果。

## Independent variables

- 错误类型：geometry / color / material / logo / OCR / specification / SKU swap。
- 压力条件：view coverage / occlusion / motion amplitude / compression / shot boundary。
- 生成来源：controlled corruption 与至少两个独立 I2V model family。

## Primary outcomes

- 属性错误检测 AUROC / macro-F1。
- 同品牌近邻 SKU retrieval margin。
- 对盲人评“可发布/不可发布”的 AUROC、Spearman 与 calibration error。
- 最坏帧错误、漂移斜率、遮挡后恢复错误，而非只有视频平均分。

## Required baselines

- CLIP-I、DINO-I、LPIPS/SSIM 或对应视频聚合。
- OCR-only 与 Logo-only。
- 简单线性组合；所提时序/属性协议必须证明增量价值。
- OpenS2V/NexusScore 或可获得的最接近主体一致性 evaluator。

## Success gate

在 held-out SKU/类别上，对人工不可发布判断的 AUROC 比最强通用基线提高 ≥0.10，且 95% bootstrap CI 不跨 0；hard-negative SKU 识别和真实生成失败两项均通过。

## Kill gate

- 简单 DINO/CLIP + OCR 达到同等结果。
- 指标仅识别人工 corruption，不解释真实生成失败。
- 人评者对属性错误或可发布判断的一致性不足（Krippendorff's alpha < 0.60）。
- 结果依赖单一品类、单一模型或训练/测试 SKU 泄漏。

## Integrity and safety

- 使用许可清晰的商品资产；不暗示品牌背书。
- 按 SKU 分组切分，禁止同一 SKU 或近重复图片跨 train/test 泄漏。
- 记录 OCR、检测器、VLM 和模型版本；失败样本不得只做定性挑选。
- 保存预注册指标、样本清单、哈希和排除理由。
