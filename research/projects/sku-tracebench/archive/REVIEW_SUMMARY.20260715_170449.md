# Review Summary — E-Commerce Video Ideas

**Mode:** same-family provisional independent jury  
**Result:** SKU-TraceBench 22/25 KEEP；Evidence-Bounded Camera 21/25 REVISE；Risk-Routed Product Lock 19/25 REVISE；Product-Frequency Router 16/25 DROP。

## Strongest criticism

SKU-TraceBench 面临 benchmark inflation：E-CommerceVideo、OpenS2V-Nexus、ConsIDVid-Bench 和 ProductConsistency 已覆盖相邻评测。仅增加 OCR/Logo 指标不够。

## Required revision landed

- 唯一贡献锁定为 SKU 版本级可判别性，而非通用质量综合分。
- 必须使用相似 SKU hard negatives、属性时序漂移、未观测视角、遮挡恢复和运动分层。
- 必须验证自动指标对人工商业可用性判断的增量预测。
- Evidence-Bounded Camera 被形式化为可校准 risk-coverage + abstention，不允许退化成 prompt heuristic。
- Product-Frequency Router 已归档，除非先获得因果路由证据。

## Acceptance gate

当前为 proposal，不构成实验结论。只有 `ecommerce_video_research_contract.md` 的 success gate 通过，才能升级为 active/piloted claim。
