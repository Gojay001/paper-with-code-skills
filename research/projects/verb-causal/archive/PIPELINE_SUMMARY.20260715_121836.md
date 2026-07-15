# Pipeline Summary

**Problem**: 帧特异文本 attention 对视频运动的作用仍缺少严格负对照干预。  
**Final Method Thesis**: 匹配 attention 统计量后，verb-token 时间结构若相对 noun/background/random 对照仍产生 motion-specific effect，才支持收窄的机制 claim。  
**Final Verdict**: READY FOR FALSIFICATION PILOT  
**Date**: 2026-07-15

## Final Deliverables

- Proposal: `research/projects/verb-causal/FINAL_PROPOSAL.md`
- Review summary: `research/projects/verb-causal/REVIEW_SUMMARY.md`
- Experiment plan: `research/projects/verb-causal/EXPERIMENT_PLAN.md`
- Experiment tracker: `research/projects/verb-causal/EXPERIMENT_TRACKER.md`

## Contribution Snapshot

- Dominant contribution: matched-statistics, token-specific intervention protocol。
- Optional supporting contribution: layer / denoising-stage localization。
- Explicitly rejected complexity: new controller, full ControlAtlas, new training, SOTA claim。

## Must-Prove Claims

- C1: verb intervention effect exceeds matched negative controls after conditioning on perceptual damage。
- C3: result is not explained by energy、entropy、token length、hook behavior or camera motion。

## First Runs to Launch

1. R001 baseline + identity hook sanity。
2. R002 attention statistics matching。
3. R003 minimal verb/noun/background/random falsification matrix。

## Main Risks

- Attention hook / checkpoint unavailable: switch implementation or stop before costly runs。
- Generic distribution damage: matched controls and kill gate。

## Next Action

Proceed to `/run-experiment` only after a CUDA-capable environment and checkpoint are confirmed; then run M0 under the 2 GPU-hour cap.

