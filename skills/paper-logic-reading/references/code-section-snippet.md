# Code section snippet（论文 ↔ 仓库对照）

列表 `Code` 列有官方仓库时，在 Method 与 Experiments 之间插入 `<section class="code-section" id="code">`。  
Canonical 范例：`paper-reading/controlnet.html`（单核心机制）、`paper-reading/cogvideox.html`（多模块 + 训练流程）。

## 何时写

| 条件 | 写 `#code` |
|------|------------|
| `paper-with-code-list.md` 有 `[PyTorch](github…)` 等可访问官方 repo | **默认写** |
| 论文核心贡献 = 可定位的模块/训练技巧（非纯 benchmark） | 至少 2 个小节 |
| 仅闭源 / `[code]` 无仓库 | 跳过；在三栏解析里文字说明即可 |

## 研究 repo（写之前做）

1. 从 list 取 GitHub URL；`raw.githubusercontent.com` 或本地 clone 读核心文件
2. 列出 2–5 个「论文符号/步骤 → 文件:类/函数」映射
3. 标出论文与实现的粒度差异（如论文单 block vs 代码整段 U-Net）

## CSS（并入 `<style>`，与 `controlnet.html` 一致）

```css
.code-section { background:#fff; border:1px solid var(--border); border-radius:8px; padding:1.5rem 1.75rem; margin:2rem 0; }
.code-section h3 { color:var(--navy); font-size:1.05rem; margin:1.5rem 0 0.75rem; }
.code-section h3:first-of-type { margin-top:0; }
.code-section p, .code-section li { font-size:0.9rem; line-height:1.75; margin-bottom:0.5rem; }
.code-section ul { margin:0.5rem 0 0.75rem 1.25rem; }
.code-block { font-family:'IBM Plex Mono','IBM Plex Sans',monospace; font-size:0.78rem; line-height:1.65; background:#1e293b; color:#e2e8f0; padding:1rem 1.15rem; border-radius:6px; overflow-x:auto; margin:0.75rem 0; white-space:pre; tab-size:2; }
.code-block .cm { color:#94a3b8; font-style:italic; }
.code-block .kw { color:#7dd3fc; }
.code-block .fn { color:#fde68a; }
.code-block .str { color:#86efac; }
.code-note { font-size:0.82rem; color:var(--muted); margin:0.35rem 0 1rem; padding-left:0.75rem; border-left:3px solid #0d9488; }
.code-map { width:100%; border-collapse:collapse; margin:0.75rem 0; font-size:0.82rem; }
.code-map th, .code-map td { border:1px solid var(--border); padding:0.4rem 0.55rem; text-align:left; vertical-align:top; }
.code-map th { background:var(--paper); color:var(--navy); font-weight:600; }
.code-map code { font-size:0.78rem; background:var(--paper); padding:0.1rem 0.3rem; border-radius:3px; }
```

`chapter-nav` 增加：`<a href="#code">代码</a>`（放在 Method 与 Experiments 之间）。

## HTML 骨架

```html
<section class="code-section" id="code">
  <h2 class="section-title" style="margin-top:0;border:none;padding:0;">💻 代码对照 — {一句话核心}</h2>
  <p>官方实现：<a href="…">github…</a> · 核心在 <code>path/to.py</code>。论文 … 在工程里拆成 …</p>

  <table class="code-map">…论文符号 → 代码位置…</table>

  <h3>① {子主题}</h3>
  <p>…</p>
  <div class="code-block"><span class="cm"># 伪代码或 repo 摘录</span>
…</div>
  <p class="code-note">对应论文式 / 与论文差异 …</p>

  <!-- 可选：训练一步数据流 -->
  <div class="diagram"><pre class="mermaid">flowchart TB …</pre></div>
</section>
```

## 每个 `h3` 小节结构（固定节奏）

1. **一句话**：论文主张或设计意图  
2. **伪代码**：与公式/图对齐的简化逻辑（`def` + 注释，不必可运行）  
3. **仓库摘录**（可选）：真实 `forward` / 10–30 行，注明 `path:line`  
4. **`.code-note`**：step-0 行为、shape、冻结/梯度、与论文不同点  

## 范例对照

### ControlNet（单机制纵深）

| 小节 | 内容 |
|------|------|
| 映射表 | $\mathcal{F}$ locked → `ControlledUnetModel`；$Z$ → `zero_module` |
| ① | `zero_module` 最小实现 |
| ② | 论文式 (3.1) 伪代码 + `ControlNet.forward` |
| ③ | `no_grad` + `hs.pop()+control.pop()` |
| ④ | `ControlLDM.apply_model` 训练 glue |
| ⑤ | Mermaid 训练一步 |

### CogVideoX（多模块 + 训练）

| 小节 | 内容 |
|------|------|
| ① | 3D VAE 8×8×4、因果卷积、单帧 encode |
| ② | 图像/视频 shape 与 4k+1 帧约束 |
| ③ | 3D full attention 伪代码 + Expert AdaLN |
| ④ | Frame Pack：`pad_last_frame` len&lt;max / len&gt;max |
| ⑤ | VAE 与 DiT **两阶段**训练伪代码 + 阶段表 |

## 三栏正文联动

- Method 三栏写**论文语言**；`#code` 写**工程语言**  
- 训练/数据技巧（pad、两阶段、uniform sampling）在三栏用 1 句概括 + 链到 `#code` §N  
- 避免整段复制仓库进三栏解析列

## KaTeX 注意

- 用 `$z_{\text{vision}}$`，勿在 `{` 与 `\text` 之间插入 Tab（会破坏 KaTeX）  
- HTML 实体：`&lt;` `&gt;` 用于比较符（尤其在 code-block 内）

## 检查

- [ ] 每个 `h3` 至少一段伪代码或真实摘录  
- [ ] `code-map` 覆盖论文核心符号/模块  
- [ ] 写明「联合训练 vs 分阶段」若有 VAE+DiT  
- [ ] 链到官方 repo 路径可点击  
- [ ] `#code` 在 `chapter-nav` 可跳转
