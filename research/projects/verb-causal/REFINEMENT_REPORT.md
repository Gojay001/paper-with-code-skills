# Refinement Report

## Starting Idea

对 FancyVideo 的 verb attention 做冻结、置乱和交换，证明跨帧文本注意导致动作。

## Problems Found

- “证明导致”过强；一般 attention perturbation 和 cross-attention probing 已存在。
- 没有匹配扰动能量、熵和时间平滑度，容易把分布外破坏误判为语义机制。
- 没有明确 noun/background/random token 负对照。
- 容易同时膨胀成 ControlAtlas 或新 controller，失去单一贡献。

## Refinement Applied

- 冻结 Problem Anchor：verb-token 时间结构是否具有 motion-specific intervention effect。
- 把 dominant contribution 固定为诊断协议。
- 设计统计量匹配、paired seed、负对照和 perceptual covariate。
- 明确两级决策门：M0 falsification → M1 robustness；M0 不通过即终止。
- 把层/步定位降为 supporting ablation，而非完整三维 atlas。

## Final Planning Gate

- **Final thesis**: verb-token temporal structure has a measurable, statistically controlled intervention effect on motion, if and only if it exceeds matched token/control perturbations.
- **Dominant contribution**: controlled diagnostic protocol.
- **Rejected complexity**: new training, controller, broad atlas, SOTA claims.
- **Reviewer concerns still active**: distribution shift, camera motion, tokenizer spans, checkpoint accessibility.
- **Frontier primitive**: absent; the work is a mechanism study, not a frontier architecture paper.

