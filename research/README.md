# Research Workspace

`research/` 按“知识 → 选题 → 项目 → 过程证据”组织。日常阅读优先进入 `wiki/` 和 `reports/`；带时间戳的历史版本统一放在各目录的 `archive/` 中。

## 快速入口

- [Diffusion 与 Video Generation 综述](wiki/DIFFUSION_VIDEO.md) · [HTML](wiki/DIFFUSION_VIDEO.html)
- [电商视频生成专题](wiki/ECOMMERCE_VIDEO.md) · [HTML](wiki/ECOMMERCE_VIDEO.html)
- [通用 Video Generation Idea 报告](reports/diffusion-video/IDEA_REPORT.md)
- [电商视频 Idea 报告](reports/ecommerce-video/IDEA_REPORT.md)
- [Verb-Causal 项目](projects/verb-causal/FINAL_PROPOSAL.md)
- [SKU-TraceBench 项目](projects/sku-tracebench/FINAL_PROPOSAL.md)
- [完整产物清单](MANIFEST.md)

## 目录结构

```text
research/
├── README.md                     # 本导航
├── MANIFEST.md                   # 全部研究产物索引
├── wiki/                         # 持久知识库
│   ├── DIFFUSION_VIDEO.md        # Diffusion / Video Generation 综述
│   ├── ECOMMERCE_VIDEO.md        # 电商视频专题
│   ├── gap_map.md                # 稳定 Gap 编号
│   ├── papers/                   # 论文节点
│   ├── ideas/                    # Idea 节点
│   ├── graph/                    # 关系图
│   └── archive/                  # Wiki 历史快照
├── reports/                      # Idea discovery 阶段报告
│   ├── diffusion-video/
│   │   └── archive/
│   └── ecommerce-video/
│       └── archive/
├── projects/                     # 已进入细化/实验计划的项目
│   ├── verb-causal/
│   │   └── archive/
│   └── sku-tracebench/
│       └── archive/
└── provenance/                   # Fan-out、jury 等过程证据
    ├── idea-discovery/
    └── research-review/
```

## 分类规则

| 内容 | 放置位置 |
|---|---|
| 单篇论文、Idea 节点、关系与 Gap | `wiki/` |
| 候选池、Idea Discovery 总报告 | `reports/<topic>/` |
| Research contract、proposal、review、experiment plan | `projects/<project>/` |
| 时间戳版本 | 相邻的 `archive/` |
| Agent fan-out、独立评审轨迹 | `provenance/` |

## 当前项目

### Verb-Causal

研究跨帧 verb-token attention 的受控干预效应。当前仍是实验前提案，入口为 `projects/verb-causal/FINAL_PROPOSAL.md`。

### SKU-TraceBench

研究电商生成视频的 SKU 版本级真实性评价，覆盖几何、颜色、材质、Logo、OCR、规格和跨帧漂移。入口为 `projects/sku-tracebench/FINAL_PROPOSAL.md`。

## 维护约定

1. 无时间戳文件代表当前版本；历史快照只进入 `archive/`。
2. 新论文和 Idea 继续写入 `wiki/`，不要在主题报告目录复制论文节点。
3. 新方向在 `reports/<topic>/` 形成报告；只有通过评审、进入实验设计后才建立 `projects/<project>/`。
4. Research Wiki 工具的根目录现在是 `research/wiki`。
