# Gap Map

_Field gaps with stable IDs. Status reflects the literature scan at 2026-07-15, not experimental validation._

| ID | Gap | Evidence anchor | Falsifiable next question | Status |
|---|---|---|---|---|
| G1 | 视频控制缺少层—去噪步—时间频率的联合相关性图谱 | RelaCtrl only profiles image-DiT layers; FancyVideo/WISA inject temporal or physics signals without joint profiling | 单层、单时间段和单频带控制消融，是否能稳定预测控制遵循度与时序质量？ | open |
| G2 | 帧特异文本注意与动作之间主要是相关证据，缺少因果干预 | FancyVideo attention visualization and module ablations | 保持边际分布的 verb-attention 冻结/置乱/交换，是否定向改变运动而不等价破坏画质？ | open |
| G3 | Flow/RF 视频路径尚未分解为空间外观与时间差分子空间 | FM/SD3 optimize global paths; CACFM and instance-aware discretization already adapt schedules | 归一化后的时间差分子空间曲率是否比全局曲率、local truncation error 和帧置信度更能预测 flicker/动作断裂？ | open diagnostic; adaptive-schedule claim crowded |
| G4 | 控制分支容量多为全局固定，缺少按样本/条件难度分配 | RelaCtrl uses a fixed top-11 layout; DynamicControl selects condition types, not control depth | 早期条件遵循误差能否预测后续所需控制层数并改善 quality-control Pareto？ | open; crowded efficiency neighborhood |
| G5 | 多条件组合缺少统一的碰撞度量 | ControlNet residual sums, U-StyDiT token composition, MoFu Fourier sum | 频谱重叠、相位冲突或梯度夹角能否预测哪一条件会被覆盖？ | open |
| G6 | 视频 VAE 的压缩—闪烁边界缺少内容条件化分析 | CogVideoX and Wan use different temporal compression ratios/protocols | 同一 token 预算下，运动边界保留更多 temporal tokens 是否优于均匀压缩？ | open; high implementation cost |
| G7 | 物理专家可能学习类别/词汇捷径，而非可迁移机制 | WISA uses 29 priors and 17 categories; absolute PC remains low | 连续改变质量、摩擦、重力等数值，路由和轨迹是否方向正确且平滑？ | open |
| G8 | 多主体视频尚未统一尺度、顺序、身份、遮挡和物理交互 | MoFu focuses scale/order; WISA physics; FancyVideo motion | 一个模型能否在受控压力测试中同时保持全部约束？ | open; scope too broad for first pilot |
| G9 | 专用自动评判器存在闭源 API 漂移和自评偏差 | MoFu ScaleScore uses GPT-4o; WISA evaluator has domain gap; Wan-Bench is self-built | 开源、版本固定、与盲人评校准的评测能否重现排名？ | open |
| G10 | 图像少步/一步编辑尚未稳健扩展到视频 | ChordEdit has low-energy one-step image transport; FancyVideo exposes temporal conditioning needs | 在控制编辑场能量的同时加入时间子空间约束，能否避免 flicker？ | open; high novelty and engineering risk |
| G11 | 缺少视频级 SKU 真实性分解评价 | E-CommerceVideo mainly uses generic metrics; OpenS2V-Nexus is subject-level; ProductConsistency is image-only | 几何、颜色、材质、Logo、OCR、规格和版本的逐帧/跨帧指标能否预测盲人评可发布率？ | open; high priority |
| G12 | 大视角生成没有显式证据边界 | VideoBooth is view-limited; ConsID-Gen/3DreamBooth add multi-view cues | 对参考未覆盖表面，限制镜头或 abstain 是否比自由补全更可信？ | open |
| G13 | 相机运动与商品真实性的风险冲突未量化 | CameraCtrl/MotionCtrl and product-identity methods are evaluated separately | 参考覆盖度和属性风险能否预测每种镜头轨迹的最大安全幅度？ | open; method opportunity |
| G14 | 人物—商品接触、功能和身份尚未统一 | AnchorCrafter/DreamActor-H1 use trajectories, meshes and boxes; DreamRelation models relations | 能否同时满足接触、遮挡恢复、功能状态与商品不形变？ | open; high engineering cost |
| G15 | 最终视频缺少跨镜头 SKU 状态连续性 | Narrative Weaver focuses on long-range visual/storyboard consistency | 商品方向、开合、数量和已发生动作能否在 shot 切换后保持因果一致？ | open |
| G16 | 品牌与包装多为软相似度而非硬约束 | BrandFusion optimizes recognizability; ProductConsistency adds image-level OCR rewards | 禁改区域、Logo、型号和法定文案能否成为可审计硬约束并触发拒绝？ | open |
| G17 | 生成—真实混合缺少风险驱动的区域决策 | AutoCut edits real footage; InsertAnywhere/SimInsert synthesize local insertions | 按区域事实风险选择保留、warp、插入或生成，能否优于全生成和全剪辑？ | open; systems risk |
| G18 | 商业意图 critic 对生成的因果有效性未知 | E-VAds/AD-MIR understand intent; KD-CVG injects ad knowledge | critic 分数提升是否带来人类信任/卖点理解提升，而非关键词或露出捷径？ | open |
| G19 | 长尾 SKU 与复杂材质覆盖不足 | Existing datasets emphasize common products/subjects | 透明、镜面、柔性包装、家具、多商品和相似 SKU 上的排名是否稳定？ | open |
| G20 | 缺少低成本、公开可复现的电商视频研究路径 | Strong systems rely on proprietary ads, 10B models, multi-GPU or multi-agent APIs | 公开 I2V 基座上的 benchmark、诊断和轻量 adapter 能否复现实质增益？ | open; feasibility gate |
