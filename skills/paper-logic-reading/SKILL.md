---
name: paper-logic-reading
description: Generate three-column Paper Logic Reading HTML (original | translation | analysis) in this repo. Use when user invokes /paper-logic-reading, asks for 逻辑精读, 三栏批注, or to generate paper-reading HTML with figures, diagrams, and lightbox.
---

# Paper Logic Reading

Canonical location: `skills/paper-logic-reading/` in **paper-with-code-skills** (this repo).

Generate `{slug}.html` + `assets/{slug}/` under `paper-reading/`.

**Reference implementations:** `paper-reading/sd.html`, `paper-reading/ddpm.html` (lightbox + figures); **`paper-reading/controlnet.html`**, **`paper-reading/cogvideox.html`** (above + **`#code` 代码对照**).

After commit & push here → in blog repo **Gojay001.github.io** update submodule pointer → invoke `skills/hexo-paper-reading-deploy/SKILL.md`.

## Output contract

| Artifact | Path |
|----------|------|
| HTML | `paper-reading/{slug}.html` |
| Figures | `paper-reading/assets/{slug}/fig{N}.{jpg\|png}` |
| Cache (gitignored) | `.cache/{slug}/` |
| Title alias (optional) | `paper-reading/slug-aliases.json` — when list Title ≠ slug |

**Meta line** (segment 2 → Hexo subcategory):

```html
<div class="meta">DeepLearning-Paper-with-Code · Diffusion Model · arXiv(2021) / CVPR(2022)</div>
```

**Page title (`<title>` + `<h1><a>`)** — English paper title only:

| Element | Rule |
|---------|------|
| `<h1><a>` | `{ShortName} — {full English title as in arXiv/PDF}` — **canonical** for bridge post `title` |
| `<title>` | Same English string as `h1`, plus ` · 逻辑精读` suffix |
| Don't | Chinese subtitles, agent summaries, or abbreviated English in `h1`/`title` |

Example: `MoFu — Scale-Aware Modulation and Fourier Fusion for Multi-Subject Video Generation`

After deploy sync, verify `source/_posts/paper-reading/{slug}.md` **`title`** matches `h1` exactly (user may override `date` / `thumbnail` only).

## Workflow

1. Resolve arXiv ID / PDF URL from `paper-with-code-list.md`
2. **Extract figures** — follow [references/figure-extraction.md](references/figure-extraction.md) (tex source first, not PDF crop)
3. Draft content: Feynman → sections (**三栏**：左=论文英文原文、中=翻译、右=解析) → **`#code` 代码对照（有官方 repo 时）** → deep cards → notation / FAQ / deepdive
4. Embed **lightbox** — copy from [references/lightbox-snippet.md](references/lightbox-snippet.md)
5. Put paper figures in `<section class="figure-row">`; **self-drawn diagrams** → follow [Self-drawn diagrams](#self-drawn-diagrams-fireworks-tech-graph) (`fireworks-tech-graph`), embed in `.diagram`
6. **Code section** — if list has official repo: follow [references/code-section-snippet.md](references/code-section-snippet.md); place after Method, before Experiments
7. Validate: KaTeX, div balance, asset paths, lightbox screenshot (see below)
8. **List links:** if list `Title` ≠ `{slug}` (e.g. `SD 1.x` vs `sd.html`), add `paper-reading/slug-aliases.json` entry, then in blog repo run `skills/sync-overview-from-list/scripts/sync-overview-from-list.py`
9. **List row order:** when adding or moving a row in `paper-with-code-list.md`, insert it in **arxiv_id ascending** order within that `##` section (see below)

## `paper-with-code-list.md` row order

Within each `##` / `###` section table, sort rows by **arxiv_id** when the Paper column links to arXiv.

| Rule | Detail |
|------|--------|
| Sort key | `YYYY.NNNNN` from `https://arxiv.org/abs/{id}` (or `/pdf/{id}`) in the **Paper** column |
| Order | Ascending (older → newer): e.g. HunyuanVideo `2412.03603` **before** WISA `2503.08153` |
| Same arxiv_id | Keep variants together in stable order (e.g. Wan2.1 → Wan2.2) |
| No arXiv link | Rows without `arxiv.org/abs/` stay **after** all arxiv-linked rows; preserve relative order among them |
| New paper | Do not append blindly — find the correct slot by arxiv_id and re-sort the section if needed |

Example (Video Generation): CogVideoX `2408.06072` → FancyVideo `2408.08189` → HunyuanVideo `2412.03603` → WISA `2503.08153` → Open-Sora `2503.09642` → …

## Reusable lessons (SD 2026-06)

### 1. Figure quality — tex source beats PDF crop

| Situation | Do | Avoid |
|-----------|-----|-------|
| Single `includegraphics{img/foo}` | Copy `foo.jpg` from arXiv source as-is | Cropping from `pdftoppm` page PNG |
| Vector `foo.pdf` (architecture) | `pdftoppm -png -r 300`; crop with Pillow if `trim=` in tex | Low-DPI page screenshot |
| Two plots side-by-side in tex | Stitch source JPGs with Pillow | Re-crop from PDF |
| LaTeX mosaic (10+ subfigures, no `pdflatex`) | Re-render PDF page at **400 DPI**, crop bbox | 150 DPI crop (blurry) |
| Photo galleries | Save as **JPG q≈88** | Huge PNG |

Map figures via `grep includegraphics ms_figures.tex` (or `*_figures.tex`) and `\label{fig:...}`.

Helper: `skills/paper-logic-reading/scripts/extract-figures.py` or `scripts/fetch-arxiv-source.sh {arxiv_id} {slug}`

### 2. Lightbox — SVG clone collapses without explicit size

**Symptom:** overlay opens, caption visible, image/SVG invisible.

**Cause:** `cloneNode(true)` on SVG loses layout box; flex child height → 0.

**Fix:** In `openLightbox`, read `getBoundingClientRect()` from the **live** node, scale to viewport, set `clone.style.width/height` in px; clear `max-width/max-height`. Use **event delegation** on `document` (Mermaid renders SVG after load).

**Zoom targets:** `img, svg` inside `.diagram`, `.figure-row`, or `.mermaid`.

**Verify:**

```bash
# From paper-reading/ — auto-click first .diagram svg, screenshot
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu --virtual-time-budget=4000 \
  --screenshot=/tmp/lb-test.png "file://$PWD/{slug}.html"
```

Repeat for a `.figure-row img` (paper raster figure).

### 3. HTML conventions

#### Three-column semantics（三栏分工）

Each `.row` under a section **must** have exactly three columns. Labels: `原文 | 翻译 | 解析`.

| Column | Class | Language | Content |
|--------|-------|----------|---------|
| **Left — 原文** | `.col-original` | **Paper language (usually English)** | Wording **traceable to the paper**: abstract sentences, section paragraphs, list items, table numbers, equations as in PDF. May **condense** (merge sentences, drop redundancy) but **must not** paraphrase into Chinese, add interpretation, or replace with bullet summaries written by the agent. |
| **Middle — 翻译** | `.col-translation` | **Chinese** | **Faithful translation of the left column only** — same paragraph / list / table structure, sentence-by-sentence. Terminology may be clarified (e.g. permutation → 排列不变性) but **no extra compression, no arrow pipelines, no reader interpretation**. |
| **Right — 解析** | `.col-analysis` | **Chinese** | `.analysis-card` only: **理解、压缩、归纳**、对比、局限、消融、表格解读、与 Fig/附录联动 — anything not a straight translation of the left column. |

**Do / Don't**

| Do | Don't |
|----|-------|
| Left: quote or tight excerpt from paper § / abstract / appendix | Left: Chinese prose |
| Left: English table headers matching paper (Method, Metric, …) | Left: agent-written 「动机 / 局限 / 流水线总结」 |
| Middle: **逐段/逐句**翻译左栏；列表项一一对应；表格行一一对应 | Middle: 速记（「A → B → C」）、合并段落、分析性评价、左栏未出现的信息 |
| Right: 理解压缩、与 Phantom 对比、消融、可复现性 | Right: repeat translation |
| `math-block` / `.notation` between rows: bilingual notes OK | Put `math-block` dimension notes inside `.col-original` as if they were paper text |

**Non–three-column blocks** (no column split): `#feynman`, `.figure-row`, `.math-block`, `.diagram`, `#code`, `#notation`, `#faq`, `#deepdive`. Agent commentary there is allowed.

**Reference rows:** `paper-reading/lay2story.html` (Abstract), `paper-reading/controlnet.html` (Method).

- Paper originals: `<section class="figure-row"><figure><img src="assets/{slug}/figN.jpg"><figcaption>…点击放大。</figcaption></figure></section>`
- Self-drawn: see [Self-drawn diagrams](#self-drawn-diagrams-fireworks-tech-graph) — prefer `fireworks-tech-graph` SVG in `.diagram` (Mermaid only for trivial one-step flows)
- Cursor/hover: CSS on `.diagram img, .diagram svg, .figure-row img, .figure-row svg` (no per-element JS class)
- **结构化十问**（`#faq`）：Q1–Q10 全部 `<details open>`，默认展开；读者仍可点击折叠。勿只给 Q1 加 `open`

```html
<section class="summary faq" id="faq">
  <h2>🧩 结构化十问（AI 解构）</h2>
  <details open><summary>Q1 · …</summary><div class="answer">…</div></details>
  <details open><summary>Q2 · …</summary><div class="answer">…</div></details>
  <!-- Q3–Q10 同样 details open -->
</section>
```

### 4. Pillow / venv

System Python may block `pip install Pillow`. Use:

```bash
python3 -m venv .cache/.venv
.cache/.venv/bin/pip install Pillow
```

### 5. Code section — 论文核心步骤 ↔ 官方仓库（2026-06，ControlNet / CogVideoX）

**目的：** 三栏讲论文；`#code` 讲**工程落地**——读者能对照 repo 复现关键路径。

**何时写：** `paper-with-code-list.md` 的 Code 列有官方 GitHub → **默认增加** `#code`。无仓库则跳过。

**放置：** Method 三栏之后、Experiments 之前；`chapter-nav` 加 `<a href="#code">代码</a>`。

**写法（每篇 2–5 个 `h3` 小节）：**

| 步骤 | 动作 |
|------|------|
| 1. 扫 repo | 定位核心文件（如 `cldm/cldm.py`、`sat/dit_video_concat.py`） |
| 2. 映射表 | `code-map`：论文符号/模块 → 类/函数 |
| 3. 伪代码 | 与公式/Fig 对齐的简化 `def`（注释写清 shape、冻结、梯度） |
| 4. 摘录 | 可选 10–30 行真实 `forward` / 数据预处理 |
| 5. 差异 | `.code-note`：论文粒度 vs 代码粒度、联合/分阶段训练 |
| 6. 联动 | 三栏 Method 保留论文表述；pad/采样/两阶段等细节链到 `#code` §N |

**单机制 vs 多模块：**

- **单核心**（ControlNet）：纵深拆 locked copy、zero conv、训练 glue、一步 Mermaid  
- **多模块**（CogVideoX）：VAE 压缩率 + 单帧 encode、attention 伪代码、数据 pad/truncate、VAE/DiT 两阶段表

**CSS / HTML：** 复制 [references/code-section-snippet.md](references/code-section-snippet.md)（与 `controlnet.html` 同源）。

**研究来源：** GitHub `raw`、论文附录训练表、官方 issue（如 Frame Pack 末帧 pad）。

### 6. Self-drawn diagrams (`fireworks-tech-graph`)

When **drawing** training/inference pipelines, architecture summaries, argument chains, or other agent-authored diagrams (not paper-extracted figures):

1. **Read and follow** [`skills/fireworks-tech-graph/SKILL.md`](../fireworks-tech-graph/SKILL.md) (submodule: [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)).
2. Set `SKILL_ROOT` to that skill directory; use its `scripts/` + `references/` as documented there.
3. **Default style for paper-reading HTML:** Style **1** (Flat Icon) or **4** (Notion Clean) — light backgrounds match the triple-column page. Use dark styles only if the user asks.
4. **Output paths:** write under `paper-reading/assets/{slug}/` (or `paper-reading-local/assets/{slug}/` while drafting), e.g. `diagram-train.svg` / `diagram-sample.svg` (+ PNG export optional).
5. **Embed:** put SVG in `.diagram` via `<img src="assets/{slug}/….svg">` or inline `<svg>`; add a one-line `figcaption` stating which logic the diagram supports. Keep lightbox targets (`img, svg` in `.diagram`).
6. **Fidelity:** nodes/edges/labels must match the paper (symbols, module names). No invented components — if unsure, omit or mark 「论文未说明」 in caption/analysis.
7. **Mermaid fallback:** only for a single trivial LR flow (≤5 nodes). Prefer fireworks SVG for anything with layers, swimlanes, or multi-stage pipelines.

## Checklist before commit

- [ ] All `assets/{slug}/fig*` paths match HTML `src`
- [ ] Extension matches file (`.jpg` vs `.png`) after format choice
- [ ] Lightbox works for at least one SVG and one raster figure
- [ ] Self-drawn diagrams (if any) produced via `fireworks-tech-graph`; assets under `assets/{slug}/`
- [ ] `#feynman` section present (bridge post excerpt)
- [ ] `#faq` 十问全部 `<details open>`（默认展开）
- [ ] `<title>` and `<h1><a>` = English paper title (`ShortName — Full Title`); bridge md `title` matches `h1`
- [ ] If official repo: `#code` with `code-map` + ≥2 伪代码/摘录小节；`chapter-nav` 含「代码」
- [ ] Three-column rows: `.col-original` = paper English; `.col-translation` = **忠实翻译左栏**（禁压缩/速记/理解）；`.col-analysis` = 理解/压缩/解析
- [ ] If Title ≠ slug: `slug-aliases.json` + Overview sync (blog repo)
- [ ] New/updated list row placed in **arxiv_id ascending** order within its section

## References

- [references/figure-extraction.md](references/figure-extraction.md) — full extraction decision tree + SD example
- [references/lightbox-snippet.md](references/lightbox-snippet.md) — copy-paste CSS, HTML, JS
- [references/code-section-snippet.md](references/code-section-snippet.md) — `#code` CSS, skeleton, ControlNet/CogVideoX patterns
- [scripts/extract-figures.py](scripts/extract-figures.py) — `fetch | list | copy | render-pdf | stitch | crop-page | crop`
- [`../fireworks-tech-graph/SKILL.md`](../fireworks-tech-graph/SKILL.md) — self-drawn technical SVG+PNG diagrams
