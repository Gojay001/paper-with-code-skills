# Diffusion 与 Video Generation 研究综述

> 范围：以 `paper-with-code-list.md` 的 Diffusion Model、Video Generation 两节为主，结合 `paper-reading/` 中 15 篇精读文档，并补充截至 2026-07-15 的相邻工作检索。论文节点和原始摘要见 `papers/`，这里提供面向研究选题的综合视图。

## 1. 主干范式：从离散去噪到视频 Flow DiT

1. **DDPM / DDIM：生成过程可训练、但采样昂贵。** DDPM 用固定高斯前向链和噪声预测目标建立现代扩散模型基线；DDIM 说明同一训练目标可对应非马尔可夫、少步采样路径。核心遗留问题是步数、似然与感知质量不一致。
2. **Latent Diffusion：把“感知压缩”和“语义生成”解耦。** Stable Diffusion/LDM 将生成搬到连续 latent，显著降低高分辨率成本，同时让 cross-attention 成为文本、边缘、深度、布局等条件的统一接口。代价是 VAE 重建上限和细节损失。
3. **Flow Matching / Rectified Flow：直接学习连续速度场。** Flow Matching 用无需 ODE 仿真的向量场回归训练 CNF；SD3 将更直的路径、logit-normal 时间采样和 MM-DiT 组合到大规模图像生成。直线路径降低数值求解难度，但实际轨迹仍可能局部弯曲，且多项架构/数据变化常被一起报告。
4. **DiT：扩散骨干转向 Transformer。** DiT 让扩散模型获得更清晰的 scaling 路径；PixArt-α证明课程训练和 dense caption 能显著降低训练成本，PixArt-δ再用一致性蒸馏和 DiT-ControlNet 缩短采样、增加结构控制。
5. **Video DiT / Flow：时空压缩、长序列建模与数据工程共同决定结果。** CogVideoX 以 3D causal VAE、Expert Transformer、3D full attention 和 dense caption 构成系统；Wan2.1 使用更高压缩 causal VAE、14B DiT 和 Rectified Flow，并提供 1.3B 低门槛版本。两者都说明：视频质量不能归因于单一模块。

## 2. 控制范式：从结构残差到多路条件组合

### 2.1 结构控制与安全接入

ControlNet 的关键不是某一种条件，而是“冻结主干 + 可训练副本 + zero-init 残差”的安全接入协议。PixArt-δ把该协议迁移到 DiT，但复制多个完整 block 带来接近 50% 的额外参数与计算；RelaCtrl 用 ControlNet Relevance Score 找到前中层的非均匀重要性，并以稀疏层放置和轻量 mixer 把控制开销降到原方案约 15%。当前证据仍主要绑定 PixArt-α，尚不能直接外推到 Flux、SD3 或视频 DiT。

### 2.2 文本与运动

FancyVideo 的诊断是：逐帧重复同一个文本 embedding 会让动词的空间注意区域近乎不动。CTGM 通过帧特异文本条件、跨帧 affinity refinement 和输出时序增强改善动作与一致性。但其证据主要是注意力可视化、消融和结果相关性，尚未用“冻结、置乱、交换”等干预证明 verb attention 是动作的因果中介。

### 2.3 物理、布局与多主体

- **WISA** 把物理条件拆为文本、定性类别和定量参数，并只在 CogVideoX 末层加入物理模块，体现低开销专用适配；绝对物理一致性仍低，且 29 维 prior 的来源和机制使用方式未充分校准。
- **Lay2Story** 通过布局分支和 layout dropout 支持有/无布局故事生成，但对部分、噪声和错误布局的连续可靠性缺乏系统验证。
- **MoFu** 用尺度调制和 Fourier Fusion 处理多主体比例与参考顺序，贡献同时包含方法和压力测试 benchmark；其“高维特征近似正交”解释仍属启发式。
- **Wan-S2V、LTX-2、MOVA** 把条件扩展到音频或联合音视频；**Wan2.6**进一步走向原生多模态、多镜头叙事。控制问题因此从“能否注入条件”转为“多条件何时冲突、怎样分配容量”。

## 3. 效率地图：四个彼此正交的杠杆

| 层次 | 代表工作 | 主要收益 | 尚未解决 |
|---|---|---|---|
| 表示压缩 | LDM、CogVideoX VAE、Wan-VAE | 降低 token 数与显存 | 压缩率与运动边界、闪烁、文字细节的内容依赖关系 |
| 路径/步数 | DDIM、FM/RF、PixArt-δ、ChordEdit | 降 NFE、改善数值路径 | 图像少步方法如何保持视频时间一致性 |
| 主干注意力 | Qihoo-T2X、Sparse VideoGen、Sparse-vDiT | 稀疏长序列计算 | 结构稀疏与样本/时间步动态稀疏如何统一 |
| 条件分支 | RelaCtrl、WISA | 减少控制参数和 FLOPs | 控制预算是否应随样本、层、时间步和频带变化 |

近期相邻工作收紧了部分空白：Sparse VideoGen 和 Sparse-vDiT 已系统利用视频 attention 的时空/层头稀疏；USV 进一步联合 token、attention 与去噪步的动态稀疏；DSA 已按帧置信度动态分配自回归视频扩散步数。因此，“泛化的动态加速”不再足够新，研究应聚焦**控制分支的机制与条件遵循误差**，或聚焦**空间外观与时间变化子空间的可证伪差异**。

## 4. 跨论文共识与矛盾

### 共识

- dense caption、过滤和专用数据常与架构收益同等重要；PixArt、SD3、CogVideoX、WISA 都支持这一点。
- 新条件路径需要安全初始化和冻结主干，zero-init 残差是最稳定的通用接口。
- 稀疏全局表示不能独自保留局部细节；Qihoo-T2X 去掉局部 TCM 后显著退化，过度 latent 压缩也有同类问题。
- FID/CLIP/VBench 等单指标无法同时衡量动作、身份、物理、控制遵循与视觉质量，专用失败模式需要专用压力测试。

### 尚未解决的矛盾

- **动作幅度 vs 主体/纹理稳定：** 更强文本或运动引导可能带来更大动作，也可能破坏身份和局部细节。
- **压缩/稀疏 vs 时间边界：** 静态背景冗余很大，但运动边界恰好是最容易闪烁、又最不能被压缩的位置。
- **物理一致 vs 创作自由：** 强物理 prior 可能压制幻想、隐喻和故意违背常识的 prompt。
- **多条件可组合 vs 条件碰撞：** 残差求和、token 拼接或 Fourier 求和都提供了组合接口，却很少直接测量条件间的梯度、频谱或注意力冲突。

## 5. 适合继续研究的空白

对应稳定编号见 `gap_map.md`。优先级最高的是：

1. **G1：视频控制的层—去噪步—时间频率相关性。** RelaCtrl 只验证图像 DiT 的层相关性；视频条件可能在不同帧、步和频带承担不同功能。
2. **G2：帧特异文本引导的因果机制。** FancyVideo 证明“有用”，但没有证明 verb attention 的时间变化“导致”运动。
3. **G3：Flow 视频轨迹的子空间几何。** 现有曲率/自适应采样主要把 latent 视为整体，尚未比较空间外观子空间与时间差分子空间的曲率是否预测不同伪影。
4. **G4：按样本分配控制分支预算。** 动态主干/采样已有较强先例，但条件遵循误差驱动的控制容量调度仍缺少直接证据。
5. **G5：多条件碰撞的可测量诊断。** 多条件组合方法很多，统一、可干预的冲突量化仍少。

## 6. 来源边界

- 本地清单同时包含正式论文、技术报告和厂商博客；综述没有把列表归类直接等同于算法家族。
- SD 1.x/SD 2、Wan2.1/Wan2.2、LTX-2/LTX-2.3 等共享同一论文，知识库按 arXiv ID 去重。
- 截止日期后的工作未覆盖；2026 年条目的版本、代码和同行评审状态可能继续变化。

## 7. 电商视频生成专题

专题综述见 [`ECOMMERCE_VIDEO.md`](ECOMMERCE_VIDEO.md)。本轮新增 31 篇直接或相邻工作后，技术版图可概括为：

- **商品图直生视频**：E-CommerceVideo 定义多视图商品图到展示视频，ConsID-Gen/3DreamBooth 补充多视图和 3D 身份。
- **人—商品演示**：AnchorCrafter、DreamActor-H1、DreamRelation 处理人物、商品、动作与关系。
- **广告规划与剪辑**：Narrative Weaver 生成分镜；VC-LLM、Tree-of-AdEditor、AutoCut 编排真实素材。
- **卖点与品牌**：KD-CVG 注入广告知识，BrandFusion 做品牌植入，E-VAds/AD-MIR 从理解侧提供商业意图 critic。
- **生成—真实混合**：PLACID、InsertAnywhere、SimInsert、Point2Insert 支持商品插入和背景保持。

该领域的核心研究矛盾不是一般的“质量 vs 速度”，而是 **生成自由度 vs SKU 可核验真实性**。新增 G11–G20 聚焦视频级 SKU 评价、证据边界外视角、镜头风险预算、包装硬约束、跨镜头状态和低成本复现。优先 Idea 为 SKU-TraceBench 与 Evidence-Bounded Camera。

## 8. 近期相邻工作（用于新颖性边界）

- [Sparse VideoGen](https://arxiv.org/abs/2502.01776)：训练免费、在线识别时空稀疏 attention head。
- [Sparse-vDiT](https://arxiv.org/abs/2506.03065)：按层/头搜索稀疏 pattern 并做硬件感知加速。
- [USV](https://arxiv.org/abs/2512.05754)：联合 attention、token merge 与去噪步的动态稀疏。
- [Dynamic Diffusion Transformer](https://arxiv.org/abs/2410.03456)：图像 DiT 的时间步动态宽度和空间动态 token。
- [DSA](https://arxiv.org/abs/2606.04432)：按帧置信度动态分配自回归视频扩散步数。
- [Causality in Video Diffusers is Separable from Denoising](https://arxiv.org/abs/2602.10095)：探测层/步冗余并分离因果时序推理与逐帧渲染。
- [Curvature-Adaptive Consistency Flow Matching](https://arxiv.org/abs/2606.22394)：用曲率自适应优化图像一致性蒸馏轨迹，构成视频曲率方向的重要近邻。
- [Understanding Attention Mechanism in Video Diffusion Models](https://arxiv.org/abs/2504.12027)：对视频扩散的空间/时间 attention 做信息论扰动分析，并用于视频增强和编辑。
- [AttentionBender](https://arxiv.org/abs/2604.20936)：大规模操纵 Video DiT cross-attention，显示其表征高度纠缠。
- [Few-Step Diffusion Sampling Through Instance-Aware Discretizations](https://arxiv.org/abs/2603.17671)：学习按实例分配时间离散，并已在 video flow matching model 上验证。
- [PhysVideoGenerator](https://arxiv.org/abs/2601.03665)：从噪声 latent 预测 V-JEPA 物理 token 并注入 temporal attention，验证联合训练可行性。
