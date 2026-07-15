# Review Summary

**Review type**: same-family provisional, independent read-only jury  
**Top ranking**: I1 Verb-Causal (22/25) → I3 Temporal-Curvature (20/25) → I2 ControlAtlas (18/25)

## Decisive Review Points

- I1 可执行且可证伪，但 attention manipulation 已有明显近邻。必须把区别收窄到 verb-specific、matched-statistics、negative controls 和 motion-specific outcomes。
- I3 的 adaptive sampler claim 被 CACFM、DSA 和 instance-aware discretization 挤压；只保留空间/时间子空间曲率诊断。
- I2 的 atlas 只有在 held-out condition/prompt 上预测布局时才不只是描述性消融。
- I5/I6 因关键接口或权重不可得被拒绝，不因“idea 不有趣”而拒绝。

## Strongest Objection to Selected Idea

置乱 attention 后视频变差，只能证明 tensor 参与网络，不足以证明 verb attention 是动作中介。干预还可能改变范数、熵、局部平滑性或整体网络分布。

## Required Revisions Applied

- claim 从“verb attention 是动作来源”降级为“verb-token 的受控干预效应”。
- 增加 matched-energy、matched-entropy、token-length、random orthogonal 与 token-type 负对照。
- paired seeds；motion 和 perceptual degradation 分开报告。
- 明确 kill gate：若负对照同等有效或画质退化解释全部 motion 变化，则停止。

## Remaining Unknowns

- 具体 checkpoint、hook 稳定性与单次推理成本尚未验证。
- 当前未运行 pilot，所有可行性估计仍需 M0 校验。
- 外部异构 reviewer 未运行，因此评分是 provisional，不是独立模型共识。

