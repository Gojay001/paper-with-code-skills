# DDPM 示例

本仓库 `paper-reading/ddpm.html` 为 paper-with-code-list.md Diffusion Model 章节 DDPM 的精读输出。

## 论文元数据

| 字段 | 值 |
|------|-----|
| Title（简称） | DDPM |
| 全称 | Denoising Diffusion Probabilistic Models |
| 作者 | Jonathan Ho, Ajay Jain, Pieter Abbeel |
| 列表 abs | `https://arxiv.org/abs/2006.11239` |
| **精读 PDF** | `https://arxiv.org/pdf/2006.11239.pdf` |
| Conf | arXiv(2020) / NeurIPS(2020) |
| Code | [PyTorch](https://github.com/lucidrains/denoising-diffusion-pytorch)（社区实现；原文官方为 [hojonathanho/diffusion](https://github.com/hojonathanho/diffusion)） |

## 获取全文命令

```bash
# PDF（精读用）
curl -L "https://arxiv.org/pdf/2006.11239.pdf" -o .cache/ddpm/paper.pdf

# LaTeX 源码（可选，便于提取段落）
curl -L "https://arxiv.org/e-print/2006.11239" -o .cache/ddpm/source.tar.gz
tar -xzf .cache/ddpm/source.tar.gz -C .cache/ddpm/
```

## 输出

- 路径：`paper-reading/ddpm.html`
- 布局：三栏 `[原文 | 翻译 | 解析]`，逐段对应
- 覆盖章节：Abstract、Introduction、Background、Method、Experiments、Conclusion

## 逻辑骨架（预填）

```
问题：扩散模型能否生成与 GAN 等媲美的图像？
论点：扩散模型 + ε 参数化 + 简化目标 L_simple 可达 SOTA 样本质量
证据：CIFAR10 IS=9.46 / FID=3.17；消融实验；与 score matching 的等价性
反驳：承认 NLL 不如自回归模型；主动讨论 rate-distortion 与「无损码长浪费在不可感知细节」
结论：扩散模型是通用生成工具，归纳偏置适合图像
```

## 带 `#code` 的范例

| 论文 | HTML | 模式 |
|------|------|------|
| ControlNet | `paper-reading/controlnet.html` | 单核心：locked copy、zero conv、训练 glue |
| CogVideoX | `paper-reading/cogvideox.html` | 多模块：3D VAE、full attention、Frame Pack、两阶段训练 |

写法见 `skills/paper-logic-reading/references/code-section-snippet.md`。
