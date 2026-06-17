# paper-with-code-list 分类映射

写入前先读取 `paper-with-code-list.md` 确认最新结构；本文件为快速参考。

## TOC 顶层

| 领域 | TOC 标签 | 说明 |
|------|----------|------|
| AIGC | **AIGC** (AI Generated Content) | 生成式内容 |
| LLM/VLM | **LLM / VLM** | 语言/视觉语言模型 |
| CV | **CV** (Computer Vision) | 计算机视觉 |

## AIGC 子分类

| 用户可能说的 | 列表章节 | 锚点 |
|-------------|-------------|------|
| GAN | Generative Adversarial Network | `#generative-adversarial-network` |
| VAE | Variational Auto-Encoder | `#variational-auto-encoder` |
| Diffusion / 扩散 | Diffusion Model | `#diffusion-model` |
| AIGC 应用 | AIGC-Applications | `#aigc-applications` |
| 人脸编辑 / Face Editing | AIGC-Applications → Face Editing | `#face-editing` |
| 换脸 / Face Swapping | AIGC-Applications → Face Swapping | `#face-swapping` |

## LLM / VLM 子分类

| 用户可能说的 | 列表章节 | 锚点 |
|-------------|-------------|------|
| Transformer / Attention | Attention or Transformer | `#attention-or-transformer` |
| PLM / 预训练语言模型 / BERT / T5 / GPT-2 / GLM | Pre-trained Language Model | `#pre-trained-language-model` |
| LLM / 大语言模型 / GPT / OpenAI / Claude / Google / Gemini / PaLM / Gemma / Qwen / DeepSeek / ByteDance / Seed / LLaMA / GLM-4 / ChatGLM | Large Language Model | `#large-language-model` |
| ViT / Vision Transformer | Vision Transformer | `#vision-transformer` |
| VLM / 视觉语言模型 / CLIP | Vision Language Model | `#vision-language-model` |

## CV 子分类

| 用户可能说的 | 列表章节 | 锚点 |
|-------------|-------------|------|
| Backbone / 分类网络 | Backbone | `#backbone` |
| Detection / 检测 | Object Detection | `#object-detection` |
| Segmentation / 分割 | Object Segmentation | `#object-segmentation` |
| Tracking / 跟踪 | Object Tracking | `#object-tracking` |
| MOT / 多目标跟踪 | Object Tracking → Multiple Object Tracking | `#multiple-object-tracking` |
| VOT / 单目标跟踪 | Object Tracking → Visual Object Tracking | `#visual-object-tracking` |
| FSS / 少样本分割 | Few-Shot Segmentation | `#few-shot-segmentation` |
| FSL / 少样本学习 | Few-Shot Learning | `#few-shot-learning` |
| 3D Face / 三维人脸 | 3D Face Reconstruction and Facial Animation | `#3d-face-reconstruction-and-facial-animation` |
| SOD / 显著性检测 | Salient Object Detection | `#salient-object-detection` |
| 3D Detection | 3D Object Detection | `#3d-object-detection` |
| Optimization / 优化 | Optimization | `#optimization` |
| Survey / 综述 | Survey | `#survey` |

## 分类选择原则

1. 优先匹配**最具体**的子分类（如 Face Editing 而非 AIGC-Applications）
2. 用户给出分类线索时优先采用，但仍需与论文内容一致
3. 无法确定时列出 2–3 个候选分类，请用户选择
4. 新建分类需用户明确指令，并同步更新 TOC 与 `##` 标题
