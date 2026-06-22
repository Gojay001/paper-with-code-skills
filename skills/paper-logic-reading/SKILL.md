---
name: paper-logic-reading
description: Generate three-column Paper Logic Reading HTML (original | translation | analysis) in this repo. Use when user invokes /paper-logic-reading, asks for 逻辑精读, 三栏批注, or to generate paper-reading HTML with figures, diagrams, and lightbox.
---

# Paper Logic Reading

Canonical location: `skills/paper-logic-reading/` in **paper-with-code-skills** (this repo).

Generate `{slug}.html` + `assets/{slug}/` under `paper-reading/`.

**Reference implementations:** `paper-reading/sd.html`, `paper-reading/ddpm.html` (both include lightbox + figures).

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

## Workflow

1. Resolve arXiv ID / PDF URL from `paper-with-code-list.md`
2. **Extract figures** — follow [references/figure-extraction.md](references/figure-extraction.md) (tex source first, not PDF crop)
3. Draft content: Feynman → sections (三栏) → deep cards → notation / FAQ / deepdive
4. Embed **lightbox** — copy from [references/lightbox-snippet.md](references/lightbox-snippet.md)
5. Put paper figures in `<section class="figure-row">`; self-drawn SVG/Mermaid in `.diagram`
6. Validate: KaTeX, div balance, asset paths, lightbox screenshot (see below)
7. **List links:** if list `Title` ≠ `{slug}` (e.g. `SD 1.x` vs `sd.html`), add `paper-reading/slug-aliases.json` entry, then in blog repo run `skills/sync-overview-from-list/scripts/sync-overview-from-list.py`

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

- Paper originals: `<section class="figure-row"><figure><img src="assets/{slug}/figN.jpg"><figcaption>…点击放大。</figcaption></figure></section>`
- Self-drawn: `.diagram` with inline SVG or `<pre class="mermaid">`
- Cursor/hover: CSS on `.diagram img, .diagram svg, .figure-row img, .figure-row svg` (no per-element JS class)

### 4. Pillow / venv

System Python may block `pip install Pillow`. Use:

```bash
python3 -m venv .cache/.venv
.cache/.venv/bin/pip install Pillow
```

## Checklist before commit

- [ ] All `assets/{slug}/fig*` paths match HTML `src`
- [ ] Extension matches file (`.jpg` vs `.png`) after format choice
- [ ] Lightbox works for at least one SVG and one raster figure
- [ ] `#feynman` section present (bridge post excerpt)
- [ ] `<title>` and `.meta` aligned with `paper-with-code-list.md`
- [ ] If Title ≠ slug: `slug-aliases.json` + Overview sync (blog repo)

## References

- [references/figure-extraction.md](references/figure-extraction.md) — full extraction decision tree + SD example
- [references/lightbox-snippet.md](references/lightbox-snippet.md) — copy-paste CSS, HTML, JS
- [scripts/extract-figures.py](scripts/extract-figures.py) — `fetch | list | copy | render-pdf | stitch | crop-page | crop`
