# Research Wiki Query Pack

_Auto-generated. Do not edit._

## Open Gaps
# Gap Map

_Field gaps with stable IDs. Status reflects the literature scan at 2026-07-15, not experimental validation._

| ID | Gap | Evidence anchor | Falsifiable next question | Status |
|---|---|---|---|---|
| G1 | 视频控制缺少层—去噪步—时间频率的联合相关性图谱 | RelaCtrl only profiles image-DiT layers; FancyVideo/WISA inject temporal or physics signals without joint profiling | 单层、单时间段和单频带控制消融，是否能稳定预测控制遵循度与时序质量？ | open |
| G2 | 帧特异文本注意与动作之间主要是相关证据，缺少因果干预 | FancyVideo attention visualization and module ablations | 保持边际分布的 verb-attention 冻结/置乱/交换，是否定向改变运动而不等价破坏画质？ | open |
| G3 | Flow/RF 视频路径尚未分解为空间外观与时间差分子空间 | FM/SD3 optimize global paths; CACFM and instance-aware discretization already adapt schedules | 归一化后的时间差分子空间曲率是否比全局曲率、local truncation error 和帧置信度更能预测 flicker/动作断裂？ | open diagnostic; adaptive-schedule claim crowded |
| G4 | 控制分支容量多为全局固定，缺少按样本/条件难度分配 | RelaCtrl uses a fixed top-11 layout; DynamicControl selects condition types, not control depth | 早期条件遵循误差能否预测后续所需控制层数并改善 quality-control Pareto？ | open; crowded efficiency neighborhood |
| G5 | 多条件组合缺少统一的碰撞度量 | ControlNet residual sums, U-StyDiT token composition, MoFu Fourier sum | 频谱重叠、相位冲突或梯度夹角能否预测哪一条件会被覆盖？ | open |
| G6 | 视频 VAE 的压缩—闪烁边界缺少内容
## Failed Ideas (avoid repeating)
- **Product-Frequency Router：商品属性分频条件路由**: 
## Key Papers (76 total)
- [paper:bai2026_causality_video_diffusers] Causality in Video Diffusers is Separable from Denoising
- [paper:cao2025_relactrl_relevanceguided_efficient] RelaCtrl: Relevance-Guided Efficient Control for Diffusion Transformers
- [paper:chen2023_pixart_fast_training] PixArt-$α$: Fast Training of Diffusion Transformer for Photorealistic Text-to-Image Synthesis
- [paper:chen2024_pixart_fast_controllable] PIXART-δ: Fast and Controllable Image Generation with Latent Consistency Models
- [paper:chen2025_sparsevdit_unleashing_power] Sparse-vDiT: Unleashing the Power of Sparse Attention to Accelerate Video Diffusion Transformers
- [paper:chen2026_siminsert_seamless_video] SimInsert: Seamless Video Object Insertion via Regional Sparse Attention Fusion
- [paper:cheng2026_recommendation_generation_unifying] Recommendation as Generation: Unifying Personalized Video Generation and Recommendation at Industrial Scale
- [paper:cole2026_attentionbender_manipulating_crossattention] AttentionBender: Manipulating Cross-Attention in Video Diffusion Transformers as a Creative Probe
- [paper:deng2025_ecommercevideo_benchmark_approach] E-CommerceVideo: A Benchmark and Approach for E-Commerce Video Generation from Product Images
- [paper:esser2024_scaling_rectified_flow] Scaling Rectified Flow Transformers for High-Resolution Image Synthesis
- [paper:feng2024_fancyvideo_towards_dynamic] FancyVideo: Towards Dynamic and Consistent Video Generation via Cross-frame Textual Guidance
- [paper:gao2025_wans2v_audiodriven_cinematic] Wan-S2V: Audio-Driven Cinematic Video Generation
## Recent Relationships (60 total)
  idea:evidence-bounded-camera --inspired_by--> paper:wu2026_considgen_viewconsistent_identitypreserving
  idea:evidence-bounded-camera --inspired_by--> paper:ko2026_3dreambooth_highfidelity_subjectdriven
  idea:evidence-bounded-camera --inspired_by--> paper:he2024_cameractrl_enabling_camera
  idea:evidence-bounded-camera --inspired_by--> paper:wang2023_motionctrl_unified_flexible
  idea:evidence-bounded-camera --addresses_gap--> gap:G12
  idea:evidence-bounded-camera --addresses_gap--> gap:G13
  idea:evidence-bounded-camera --addresses_gap--> gap:G16
  idea:evidence-bounded-camera --addresses_gap--> gap:G20
  idea:risk-routed-product-lock --inspired_by--> paper:jin2025_insertanywhere_geometrically_grounded
  idea:risk-routed-product-lock --inspired_by--> paper:tarrs2026_placid_identitypreserving_multiobject
  idea:risk-routed-product-lock --inspired_by--> paper:chen2026_siminsert_seamle
