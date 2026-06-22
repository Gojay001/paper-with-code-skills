#!/usr/bin/env python3
"""Extract paper figures from arXiv LaTeX source or PDF page renders.

Cache: .cache/{slug}/
Output: paper-reading/assets/{slug}/

Examples (from paper-with-code-skills repo root):
  skills/paper-logic-reading/scripts/extract-figures.py fetch --arxiv 2112.10752 --slug sd
  skills/paper-logic-reading/scripts/extract-figures.py list --slug sd
  skills/paper-logic-reading/scripts/extract-figures.py copy --slug sd --src img/foo.jpg --out fig2.jpg --install
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import tarfile
import urllib.request
from pathlib import Path


def paper_repo_root() -> Path:
    """Root of paper-with-code-skills (this submodule)."""
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "paper-with-code-list.md").is_file():
            return parent
    for parent in here.parents:
        sub = parent / "submodule" / "paper-with-code-skills"
        if (sub / "paper-with-code-list.md").is_file():
            return sub
    raise SystemExit(
        "Cannot locate paper-with-code-skills repo root "
        "(run from repo root or via blog submodule path)"
    )


def cache_dir(slug: str) -> Path:
    return paper_repo_root() / ".cache" / slug


def src_dir(slug: str) -> Path:
    return cache_dir(slug) / "src"


def assets_dir(slug: str) -> Path:
    return paper_repo_root() / "paper-reading" / "assets" / slug


def require_pillow():
    try:
        from PIL import Image  # noqa: F401
    except ImportError as e:
        venv = paper_repo_root() / ".cache" / ".venv"
        raise SystemExit(
            f"Pillow required: {e}\n"
            f"  python3 -m venv {venv}\n"
            f"  {venv}/bin/pip install Pillow\n"
            f"  Then run with: {venv}/bin/python {Path(__file__).name} ..."
        ) from e


def parse_box(s: str) -> tuple[int, int, int, int]:
    parts = [int(x.strip()) for x in s.split(",")]
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("box must be x0,y0,x1,y1")
    return tuple(parts)  # type: ignore


def scale_box(box: tuple[int, int, int, int], ref_dpi: int | None, target_dpi: int) -> tuple[int, int, int, int]:
    if not ref_dpi or ref_dpi == target_dpi:
        return box
    scale = target_dpi / ref_dpi
    return tuple(round(v * scale) for v in box)  # type: ignore


def resolve_src_path(slug: str, rel: str) -> Path:
    p = Path(rel)
    if p.is_file():
        return p
    base = src_dir(slug)
    for candidate in (base / rel, base / rel.lstrip("/")):
        if candidate.is_file():
            return candidate
        for ext in (".jpg", ".jpeg", ".png", ".pdf"):
            if candidate.with_suffix(ext).is_file():
                return candidate.with_suffix(ext)
    raise SystemExit(f"Source not found: {rel} (looked under {base})")


def output_path(slug: str, out: str, install: bool) -> Path:
    name = Path(out).name
    if install:
        dest = assets_dir(slug) / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        return dest
    dest = cache_dir(slug) / "out" / name
    dest.parent.mkdir(parents=True, exist_ok=True)
    return dest


def save_image(im, dest: Path, jpeg: bool = False, quality: int = 88):
    require_pillow()
    from PIL import Image

    if not isinstance(im, Image.Image):
        im = Image.open(im)
    if jpeg or dest.suffix.lower() in (".jpg", ".jpeg"):
        im.convert("RGB").save(dest, format="JPEG", quality=quality, optimize=True)
    else:
        im.save(dest)


def cmd_fetch(args):
    cache = cache_dir(args.slug)
    cache.mkdir(parents=True, exist_ok=True)
    src = src_dir(args.slug)
    src.mkdir(parents=True, exist_ok=True)
    tarball = cache / "source.tar.gz"
    url = f"https://arxiv.org/e-print/{args.arxiv}"
    print(f"→ {url}")
    urllib.request.urlretrieve(url, tarball)
    with tarfile.open(tarball) as tf:
        tf.extractall(src)
    print(f"Extracted to {src}")
    cmd_list(argparse.Namespace(slug=args.slug, limit=args.limit))


def find_figures_tex(slug: str) -> Path | None:
    base = src_dir(slug)
    if not base.is_dir():
        return None
    for name in ("ms_figures.tex",):
        p = base / name
        if p.is_file():
            return p
    matches = sorted(base.glob("*_figures.tex"))
    return matches[0] if matches else None


def cmd_list(args):
    fig_tex = find_figures_tex(args.slug)
    base = src_dir(args.slug)
    if not base.is_dir():
        raise SystemExit(f"No cache src for slug={args.slug}. Run: fetch --arxiv ID --slug {args.slug}")
    if fig_tex:
        print(f"Figure map ({fig_tex.relative_to(base.parent)}):")
        lines = fig_tex.read_text(errors="replace").splitlines()
        pat = re.compile(r"includegraphics|\\label\{fig:")
        shown = 0
        for i, line in enumerate(lines, 1):
            if pat.search(line):
                print(f"  {i}: {line.strip()}")
                shown += 1
                if args.limit and shown >= args.limit:
                    break
    else:
        print("No *_figures.tex — grep .tex manually")
    img_dir = base / "img"
    img_files = [p for p in img_dir.rglob("*") if p.is_file()] if img_dir.is_dir() else []
    print(f"\nimg/ files: {len(img_files)}")


def cmd_copy(args):
    src = resolve_src_path(args.slug, args.src)
    dest = output_path(args.slug, args.out, args.install)
    shutil.copy2(src, dest)
    print(f"{src} → {dest} ({dest.stat().st_size // 1024} KB)")


def cmd_render_pdf(args):
    require_pillow()
    from PIL import Image

    pdf = resolve_src_path(args.slug, args.pdf)
    cache = cache_dir(args.slug)
    prefix = cache / "_render"
    prefix.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["pdftoppm", "-png", "-r", str(args.dpi), str(pdf), str(prefix)],
        check=True,
    )
    rendered = sorted(cache.glob(f"{prefix.name}-*.png"))
    if not rendered:
        raise SystemExit(f"pdftoppm produced no output for {pdf}")
    im = Image.open(rendered[0])
    if args.crop:
        x0, y0, x1, y1 = args.crop
        if x1 < 0:
            x1 = im.width
        if y1 < 0:
            y1 = im.height
        im = im.crop((x0, y0, x1, y1))
    dest = output_path(args.slug, args.out, args.install)
    save_image(im, dest, jpeg=args.jpeg, quality=args.quality)
    print(f"{pdf} @ {args.dpi}dpi → {dest} ({im.width}×{im.height})")


def cmd_stitch(args):
    require_pillow()
    from PIL import Image

    paths = [resolve_src_path(args.slug, p.strip()) for p in args.images.split(",")]
    imgs = [Image.open(p) for p in paths]
    gap = args.gap
    if args.vertical:
        w = max(i.width for i in imgs)
        h = sum(i.height for i in imgs) + gap * (len(imgs) - 1)
        out = Image.new("RGB", (w, h), args.bg)
        y = 0
        for im in imgs:
            out.paste(im, ((w - im.width) // 2, y))
            y += im.height + gap
    else:
        h = max(i.height for i in imgs)
        w = sum(i.width for i in imgs) + gap * (len(imgs) - 1)
        out = Image.new("RGB", (w, h), args.bg)
        x = 0
        for im in imgs:
            out.paste(im, (x, (h - im.height) // 2))
            x += im.width + gap
    dest = output_path(args.slug, args.out, args.install)
    save_image(out, dest, jpeg=args.jpeg, quality=args.quality)
    print(f"stitched {len(paths)} → {dest} ({out.width}×{out.height})")


def cmd_crop_page(args):
    require_pillow()
    from PIL import Image

    cache = cache_dir(args.slug)
    pdf = Path(args.pdf) if args.pdf else cache / "paper.pdf"
    if not pdf.is_file():
        raise SystemExit(f"PDF not found: {pdf} (pass --pdf or place paper.pdf in {cache})")
    prefix = cache / f"_page{args.page}"
    subprocess.run(
        [
            "pdftoppm", "-png", "-r", str(args.dpi),
            "-f", str(args.page), "-l", str(args.page),
            str(pdf), str(prefix),
        ],
        check=True,
    )
    rendered = sorted(cache.glob(f"{prefix.name}-*.png"))
    if not rendered:
        raise SystemExit("pdftoppm failed")
    im = Image.open(rendered[0])
    box = scale_box(args.box, args.ref_dpi, args.dpi)
    im = im.crop(box)
    dest = output_path(args.slug, args.out, args.install)
    save_image(im, dest, jpeg=args.jpeg, quality=args.quality)
    print(f"{pdf} p.{args.page} @ {args.dpi}dpi crop {box} → {dest} ({im.width}×{im.height})")


def cmd_crop(args):
    require_pillow()
    from PIL import Image

    src = Path(args.input)
    if not src.is_file():
        src = cache_dir(args.slug) / args.input
    if not src.is_file():
        raise SystemExit(f"Input not found: {args.input}")
    im = Image.open(src)
    box = args.box
    if args.ref_dpi and args.dpi and args.ref_dpi != args.dpi:
        box = scale_box(box, args.ref_dpi, args.dpi)
    im = im.crop(box)
    dest = output_path(args.slug, args.out, args.install)
    save_image(im, dest, jpeg=args.jpeg, quality=args.quality)
    print(f"{src} crop {box} → {dest} ({im.width}×{im.height})")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Extract figures for paper-logic-reading HTML")
    sub = p.add_subparsers(dest="cmd", required=True)

    f = sub.add_parser("fetch", help="Download arXiv LaTeX source")
    f.add_argument("--arxiv", required=True)
    f.add_argument("--slug", required=True)
    f.add_argument("--limit", type=int, default=40)
    f.set_defaults(func=cmd_fetch)

    l = sub.add_parser("list", help="List includegraphics / fig labels in cache")
    l.add_argument("--slug", required=True)
    l.add_argument("--limit", type=int, default=40)
    l.set_defaults(func=cmd_list)

    c = sub.add_parser("copy", help="Copy single file from tex source to output")
    c.add_argument("--slug", required=True)
    c.add_argument("--src", required=True, help="Path relative to .cache/{slug}/src/")
    c.add_argument("--out", required=True, help="Output filename e.g. fig2.jpg")
    c.add_argument("--install", action="store_true", help="Write to paper-reading/assets/{slug}/")
    c.set_defaults(func=cmd_copy)

    r = sub.add_parser("render-pdf", help="Render vector PDF with pdftoppm + optional crop")
    r.add_argument("--slug", required=True)
    r.add_argument("--pdf", required=True)
    r.add_argument("--out", required=True)
    r.add_argument("--dpi", type=int, default=300)
    r.add_argument("--crop", type=parse_box, help="x0,y0,x1,y1 (-1 = image edge)")
    r.add_argument("--jpeg", action="store_true")
    r.add_argument("--quality", type=int, default=88)
    r.add_argument("--install", action="store_true")
    r.set_defaults(func=cmd_render_pdf)

    s = sub.add_parser("stitch", help="Stitch multiple images horizontally or vertically")
    s.add_argument("--slug", required=True)
    s.add_argument("--images", required=True, help="Comma-separated paths (under src/ or absolute)")
    s.add_argument("--out", required=True)
    s.add_argument("--gap", type=int, default=20)
    s.add_argument("--bg", default="white")
    s.add_argument("--vertical", action="store_true")
    s.add_argument("--jpeg", action="store_true")
    s.add_argument("--quality", type=int, default=88)
    s.add_argument("--install", action="store_true")
    s.set_defaults(func=cmd_stitch)

    cp = sub.add_parser("crop-page", help="Render PDF page at DPI and crop bbox")
    cp.add_argument("--slug", required=True)
    cp.add_argument("--page", type=int, required=True)
    cp.add_argument("--box", type=parse_box, required=True, help="x0,y0,x1,y1 (use with --ref-dpi to scale)")
    cp.add_argument("--pdf", help="Defaults to .cache/{slug}/paper.pdf")
    cp.add_argument("--dpi", type=int, default=400)
    cp.add_argument("--ref-dpi", type=int, help="If box was measured at another DPI, scale to --dpi")
    cp.add_argument("--out", required=True)
    cp.add_argument("--jpeg", action="store_true")
    cp.add_argument("--quality", type=int, default=88)
    cp.add_argument("--install", action="store_true")
    cp.set_defaults(func=cmd_crop_page)

    cr = sub.add_parser("crop", help="Crop an existing PNG/JPG (e.g. pdftoppm output)")
    cr.add_argument("--slug", required=True)
    cr.add_argument("--input", required=True)
    cr.add_argument("--box", type=parse_box, required=True)
    cr.add_argument("--dpi", type=int, help="Target DPI context for ref scaling")
    cr.add_argument("--ref-dpi", type=int, help="DPI at which box was measured")
    cr.add_argument("--out", required=True)
    cr.add_argument("--jpeg", action="store_true")
    cr.add_argument("--quality", type=int, default=88)
    cr.add_argument("--install", action="store_true")
    cr.set_defaults(func=cmd_crop)

    return p


def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
