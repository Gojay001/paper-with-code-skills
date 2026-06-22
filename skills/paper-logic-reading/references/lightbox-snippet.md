# Lightbox snippet (click-to-zoom)

Copy into every new `paper-reading/{slug}.html`. Canonical working version: `sd.html`.

## CSS (inside `<style>`)

```css
/* 可点击放大 */
.diagram img, .diagram svg, .figure-row img, .figure-row svg { cursor: zoom-in; transition: box-shadow .15s; }
.diagram img:hover, .diagram svg:hover, .figure-row img:hover, .figure-row svg:hover { box-shadow: 0 0 0 2px #0d9488; }
#lightbox { position: fixed; inset: 0; background: rgba(10,12,20,0.92); display: none; align-items: center; justify-content: center; z-index: 1000; cursor: zoom-out; padding: 3vh 3vw; }
#lightbox.open { display: flex; }
#lightbox .lb-content { display: flex; align-items: center; justify-content: center; }
#lightbox .lb-content img, #lightbox .lb-content svg { display: block; background: #fff; border-radius: 6px; box-shadow: 0 8px 40px rgba(0,0,0,0.5); }
#lightbox .lb-close { position: fixed; top: 1rem; right: 1.5rem; color: #fff; font-size: 2rem; line-height: 1; opacity: 0.8; }
#lightbox .lb-cap { position: fixed; bottom: 1.2rem; left: 0; right: 0; text-align: center; color: #e8e4df; font-size: 0.8rem; padding: 0 2rem; }
```

**Do not** set `max-width/max-height` + `width:auto` on `.lb-content img/svg` — it fights JS sizing.

## HTML (before `</body>`)

```html
<div id="lightbox" role="dialog" aria-modal="true" aria-label="放大查看">
  <span class="lb-close" aria-hidden="true">&times;</span>
  <div class="lb-content"></div>
  <div class="lb-cap"></div>
</div>
```

## JavaScript (before `</body>`)

```javascript
(function () {
  var lb = document.getElementById('lightbox');
  var content = lb.querySelector('.lb-content');
  var cap = lb.querySelector('.lb-cap');

  function findZoomTarget(node) {
    var el = node.closest ? node.closest('img, svg') : null;
    if (!el) return null;
    if (!el.closest('.diagram, .figure-row, .mermaid')) return null;
    return el;
  }
  function nearestCaption(el) {
    var fig = el.closest('figure') || el.closest('.diagram') || el.closest('.figure-row');
    var c = fig && fig.querySelector('figcaption');
    return c ? c.textContent.trim() : '';
  }
  function openLightbox(node, caption) {
    content.innerHTML = '';
    var clone = node.cloneNode(true);
    clone.style.cursor = 'default';
    clone.style.boxShadow = 'none';
    // Required for SVG: cloned nodes lose layout size → 0 height, caption-only overlay
    var r = node.getBoundingClientRect();
    var vw = window.innerWidth * 0.96, vh = window.innerHeight * 0.92;
    var w = r.width || node.clientWidth || 600;
    var h = r.height || node.clientHeight || 400;
    var scale = Math.min(vw / w, vh / h);
    if (!isFinite(scale) || scale <= 0) scale = 1;
    clone.style.width = Math.round(w * scale) + 'px';
    clone.style.height = Math.round(h * scale) + 'px';
    clone.style.maxWidth = 'none';
    clone.style.maxHeight = 'none';
    content.appendChild(clone);
    cap.textContent = caption || '';
    lb.classList.add('open');
    document.body.style.overflow = 'hidden';
  }
  function closeLightbox() {
    lb.classList.remove('open');
    content.innerHTML = '';
    document.body.style.overflow = '';
  }
  document.addEventListener('click', function (e) {
    if (lb.classList.contains('open')) { closeLightbox(); return; }
    var el = findZoomTarget(e.target);
    if (el) { e.preventDefault(); e.stopPropagation(); openLightbox(el, nearestCaption(el)); }
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && lb.classList.contains('open')) closeLightbox();
  });
})();
```

## Why event delegation

Mermaid replaces `<pre class="mermaid">` with `<svg>` after load. Per-element `onclick` or `querySelectorAll` at parse time misses those nodes.

## Verification

1. Click inline SVG in `.diagram` → image fills overlay
2. Click `assets/...` raster in `.figure-row` → sharp enlarged image
3. Click overlay or press Escape → closes
4. Optional: headless Chrome screenshot (see main SKILL.md)

## Backfill older pages

All `paper-reading/*.html` should include this snippet. Reference: `sd.html`, `ddpm.html`.
