# Paper-with-Code Skills

[English](README.md) | **中文**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Skills](https://img.shields.io/badge/Cursor-Skills-blue) ![Papers](https://img.shields.io/badge/Deep%20Learning-Papers-green) ![Reading](https://img.shields.io/badge/Paper-Reading-orange)

一个把**论文整理**与**论文精读**流程沉淀为 **Cursor / Claude Code / Codex** 通用 Agent Skills 的仓库。它既维护一份分类的「论文 + 代码」清单，又能把任意论文转换成三栏批注的精读 HTML，让「收集 → 整理 → 精读」形成闭环。

这两个 Skill 与具体领域**无关**，适用于任何研究方向。[`paper-with-code-list.md`](paper-with-code-list.md) 中现有的分类只是**作者本人的研究方向**，仅作起点示例——**分类体系由你自行定义**（见[论文清单与自定义分类](#论文清单与自定义分类)）。

## 这个仓库做什么

| 能力 | 说明 | 产物 |
|------|------|------|
| **论文整理** | 给定论文简称/线索，自动检索全称、arXiv 链接、会议年份、官方代码与框架，按分类写入清单并按 arXiv 编号排序 | [`paper-with-code-list.md`](paper-with-code-list.md) 中的表格行 |
| **论文精读** | 给定论文（链接或清单中的行），生成「原文 · 中文翻译 · 解析」三栏批注 HTML，含费曼速读、结构化十问、深挖追问与逻辑图 | `paper-reading/{slug}.html` |

两个能力以 [Agent Skill](https://agentskills.io/specification) 形式实现，源码放在 `skills/`（唯一维护位置）。各工具通过符号链接自动发现：

| 工具 | 发现路径 |
|------|----------|
| **Cursor** | `.cursor/skills/` → `skills/` |
| **Claude Code** | `.claude/skills/` → `skills/` |
| **Codex** | `.agents/skills/` → `skills/` |

用自然语言描述需求即可，对应 Skill 会被自动加载。

## 仓库结构

```
paper-with-code-skills/
├── README.md                       # 英文说明
├── README.zh-CN.md                 # 本文件：中文说明
├── paper-with-code-list.md         # 论文清单（示例分类，Title|Paper|Conf|Code）
├── paper-reading/                  # 精读 HTML 输出目录
│   ├── ddpm.html                   # DDPM 三栏精读示例
│   └── assets/{slug}/              # 各篇精读用到的图片资源
├── skills/                         # Skill 源码（在此编辑）
│   ├── add-paper-to-list/          # Skill 1：整理论文进清单
│   │   ├── SKILL.md                # 工作流、检索来源、表格格式、排序规则
│   │   └── categories.md           # 用户措辞 ↔ 清单章节 ↔ 锚点 映射表
│   └── paper-logic-reading/        # Skill 2：论文三栏精读
│       ├── SKILL.md                # 工作流、保真性铁律、深度解析要求
│       ├── template.html           # 三栏 HTML 骨架（KaTeX / 五色高亮 / sticky 导航）
│       └── examples.md             # DDPM 精读示例的元数据与命令
├── .cursor/skills/                 # → skills/（Cursor）
├── .claude/skills/                 # → skills/（Claude Code）
└── .agents/skills/                 # → skills/（Codex）
```

## 用法

无需手动调用脚本——在 Cursor、Claude Code 或 Codex 中打开本仓库，用自然语言描述需求，对应 Skill 会被自动加载并执行。

> **说明：** macOS/Linux 下 clone 后符号链接可直接使用；若工具未识别 Skill，请重启 agent 会话。Windows 若不支持符号链接，需手动将 `skills/` 复制或链接到上表中的发现路径。

### 1. 整理论文进清单（`add-paper-to-list`）

触发措辞：「添加 XXX 论文」「把 XXX 加到论文列表」，或直接给出论文简称/一批论文，可附带领域、代码仓库、会议等线索。

工作流概要：

1. 解析输入（简称、全称线索、领域、代码仓库、会议）
2. 检索论文信息（arXiv / Semantic Scholar / Google Scholar / HF Papers，≥2 源交叉验证）
3. 读取 `paper-with-code-list.md`，按 [`categories.md`](skills/add-paper-to-list/categories.md) 确定分类与插入位置
4. 写入表格行，并对该章节**按 arXiv 编号升序整表重排**
5. 逐项校验（全称、链接、会议、代码、框架、分类、顺序）
6. 确认无误后询问是否 `git` 提交

表格行格式：

```markdown
| {Title} | [{Full Title}]({paper_url}) | {Conf} | [{Framework}]({code_url})
```

### 2. 论文精读（`paper-logic-reading`）

触发措辞：「精读论文」「逻辑分析」「三栏批注 HTML」，并给出 arXiv/PDF 链接或清单中的某一行。

产出一个自包含 HTML，逐段呈现：

- **左栏**：论文原文，五类维度高亮（核心论点 / 关键概念 / 实证证据 / 让步反驳 / 方法论）
- **中栏**：忠实中文翻译，逐段对应
- **右栏**：段落功能、逻辑角色、论证技巧/漏洞；核心方法与实验章节加厚解析并配逻辑图

另含顶部**费曼速读**、底部**结构化十问**与**深挖追问**。最高优先级是「保真性铁律」：论文未给出的内容一律写「论文未说明」，关键论断与实验数字标注出处，**严禁编造**。

## 例子

### 整理：添加 DDPM

> 用户：添加 DDPM

检索后判定属于 `Diffusion Model`，写入：

```markdown
| DDPM | [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) | arXiv(2020) / NIPS(2020) | [PyTorch](https://github.com/lucidrains/denoising-diffusion-pytorch)
```

### 精读：DDPM

> 用户：精读 DDPM

把清单中 `| DDPM | [Denoising Diffusion...](https://arxiv.org/abs/2006.11239) | ...` 的 `abs` 链接转为 `pdf` 下载阅读，输出到 [`paper-reading/ddpm.html`](paper-reading/ddpm.html)（覆盖 Abstract、Introduction、Background、Method、Experiments、Conclusion）。

在浏览器中打开该 HTML 即可阅读三栏批注。

## 论文清单与自定义分类

Skill 本身**不绑定任何分类体系**。仓库内现有清单只是**作者自己的研究方向**，仅为示例——请把它当作模板，替换成你关心的任意领域（机器人、NLP、系统、生物信息……）。

三种方式让分类为你所用：

1. **直接改清单**——修改 [`paper-with-code-list.md`](paper-with-code-list.md) 的章节标题（`##` / `###`）与目录；想从零开始可直接清空。
2. **改映射表**——更新 [`categories.md`](skills/add-paper-to-list/categories.md)（用户措辞 → 清单章节 → 锚点的映射），让 `add-paper-to-list` 按你的预期归类。
3. **直接告诉 agent**——添加论文时指定目标分类，或要求新建分类；Skill 会自动建立章节并更新目录。

默认示例清单当前涵盖：

- **AIGC**：GAN / VAE / Diffusion / 应用（Face Editing、Face Swapping）
- **LLM · VLM**：Transformer / ViT / VLM
- **CV**：Backbone / Detection / Segmentation / Tracking / Few-Shot / 3D Face / SOD / Optimization / Survey
