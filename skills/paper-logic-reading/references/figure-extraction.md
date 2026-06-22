# Figure extraction from arXiv papers

Cache everything under `.cache/{slug}/` (gitignored). Ship only `paper-reading/assets/{slug}/`.

Run commands from **repo root** (paper-with-code-skills).

## Step 1 — Download LaTeX source

```bash
skills/paper-logic-reading/scripts/extract-figures.py fetch --arxiv 2112.10752 --slug sd
# or: skills/paper-logic-reading/scripts/fetch-arxiv-source.sh 2112.10752 sd
```

Fallback if no tex bundle: keep `paper.pdf` + `pdftoppm` only for mosaics.

## Step 2 — Map figures to files

```bash
skills/paper-logic-reading/scripts/extract-figures.py list --slug sd
```

Record per figure:

| Fig | `\label` | Source file(s) | Notes |
|-----|----------|----------------|-------|
| 2 | `fig:perceptualcompression` | `img/generativevscompressive4.jpg` | single file |
| 3 | `fig:conditioning` | `img/final_figure.pdf` | vector; `trim=` in tex → crop after render |
| 6 | `fig:cin_traincourse` | `img/compression_analysis/fid_*.jpg` + `is_*.jpg` | stitch 2 JPGs |
| 7 | `fig:speedplot` | `img/speed_vs_fid/*-complete_new2.jpg` ×2 | stitch |
| 1,4,5 | sample grids | many sub-JPGs in `img/` | mosaic → see §4 |

## Step 3 — Single-file figures

```bash
skills/paper-logic-reading/scripts/extract-figures.py copy \
  --slug sd --src img/generativevscompressive4.jpg --out fig2.jpg --install
```

Prefer original extension when quality is already good (JPG from authors).

## Step 4 — Vector PDF figures

```bash
skills/paper-logic-reading/scripts/extract-figures.py render-pdf \
  --slug sd --pdf img/final_figure.pdf --out fig3.png --dpi 300 \
  --crop 0,0,-1,600 --install
```

`--crop x0,y0,x1,y1` — use `-1` for image width/height edge.

Match `trim= L B R T` in `\includegraphics[trim=...]` when present (values are in tex units; tune by visual inspection).

## Step 5 — Stitch multiple source JPGs

```bash
skills/paper-logic-reading/scripts/extract-figures.py stitch \
  --slug sd \
  --images img/compression_analysis/fid_vs_trainstep_cin_new2.jpg,img/compression_analysis/is_vs_trainstep_cin_new2.jpg \
  --out fig6.png --install
```

## Step 6 — LaTeX mosaics (no pdflatex)

When a figure is a `tabular` of dozens of `\includegraphics` and `pdflatex` is unavailable:

1. Place `paper.pdf` in `.cache/{slug}/` (or pass `--pdf`)
2. Crop with DPI scaling from a reference bbox:

```bash
skills/paper-logic-reading/scripts/extract-figures.py crop-page \
  --slug sd --page 5 --box 70,82,1196,440 --dpi 400 --ref-dpi 150 \
  --out fig4.jpg --jpeg --install
```

3. Photo-heavy → `--jpeg`; line charts / architecture → omit `--jpeg` (PNG)

## Step 7 — Install to assets

Use `--install` on any subcommand to write directly to `paper-reading/assets/{slug}/`. Without it, outputs go to `.cache/{slug}/out/`.

Update HTML `src` to match extensions (`fig2.jpg` not `fig2.png`).

### CLI summary

| Subcommand | Purpose |
|------------|---------|
| `fetch` | Download arXiv e-print |
| `list` | Print `includegraphics` / `fig:` lines |
| `copy` | Copy single source file |
| `render-pdf` | `pdftoppm` + crop |
| `stitch` | Horizontal/vertical join |
| `crop-page` | PDF page render + bbox |
| `crop` | Crop existing raster |

## SD (2112.10752) reference outcome

| Asset | Source | Method |
|-------|--------|--------|
| fig1.jpg | PDF p.1 gallery | 400 DPI crop, JPG q88 |
| fig2.jpg | `generativevscompressive4.jpg` | direct |
| fig3.png | `final_figure.pdf` | 300 DPI render + top crop |
| fig4.jpg | PDF p.5 gallery | 400 DPI crop, JPG q88 |
| fig5.jpg | PDF p.6 gallery | 400 DPI crop, JPG q88 |
| fig6.png | fid + is JPGs | stitch |
| fig7.png | celeba + cin JPGs | stitch |

Total assets ≈ 1.8 MB (vs multi-MB PNG galleries).

## Tools

| Tool | Use |
|------|-----|
| `curl` | arXiv e-print |
| `tar` | extract source |
| `pdftoppm` | PDF → PNG (poppler) |
| `Pillow` | crop, stitch, JPEG encode |
| `file`, `sips -g pixelWidth` | inspect dimensions |

## Anti-patterns

- **Default 150 DPI PDF crop** for final assets — always too soft for sample grids
- **PNG for photo mosaics** — bloated, no quality gain
- **pdfimages** on arXiv PDFs — often embedded low-res or wrong objects
- **Forgetting to sync HTML extension** after converting PNG → JPG
