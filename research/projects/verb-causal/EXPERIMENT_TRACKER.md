# Experiment Tracker

| Run ID | Milestone | Purpose | System / Variant | Split | Metrics | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| R001 | M0a | baseline + identity hook sanity | FancyVideo original / identity hook | 2 prompts × 1 seed | tensor equality, output delta, runtime | MUST | TODO | no pilot run in this workflow |
| R002 | M0b | intervention statistics matching | verb phase / random orthogonal | 2 prompts × 1 seed | energy, entropy, smoothness | MUST | TODO | gate: ≤1% / ≤2% |
| R003 | M0c | minimal falsification | 6 intervention groups | 4 prompts × 1 seed | residual flow, direction, DINO, LPIPS | MUST | TODO | hard cap 2 GPU-h total M0 |
| R004 | M1 | full paired matrix | 6 groups | 8 prompts × 2 seeds | pre-registered primary metrics | MUST | BLOCKED | blocked on M0 gate, not external blocker |
| R005 | M1 | camera-motion control | fixed-camera + global-flow subtraction | 8 prompts × 2 seeds | subject vs global flow | MUST | BLOCKED | run only if R004 signal exists |
| R006 | M1 | bootstrap / mixed-effects analysis | R004–R005 outputs | held-out analysis | effect, CI, interaction | MUST | BLOCKED | analysis only |
| R007 | M2 | step localization | early/mid/late | 4 prompts × 2 seeds | motion + quality | NICE | BLOCKED | requires C1 signal |
| R008 | M2 | layer localization | shallow/mid/deep | 4 prompts × 2 seeds | motion + quality | NICE | BLOCKED | requires C1 signal |
| R009 | M2 | held-out localization check | best window | 4 new prompts × 2 seeds | direction stability | NICE | BLOCKED | supports C2 only |

