# Paper-with-Code Skills

**English** | [中文](README.zh-CN.md)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Skills](https://img.shields.io/badge/Cursor-Skills-blue) ![Papers](https://img.shields.io/badge/Deep%20Learning-Papers-green) ![Reading](https://img.shields.io/badge/Paper-Reading-orange)

A repository that turns **paper curation** and **deep paper reading** into reusable Agent Skills for **Cursor**, **Claude Code**, and **Codex**. It maintains a categorized paper-with-code list and can turn any paper into a triple-column annotated reading HTML — closing the loop from collect → organize → read deeply.

The skills are **domain-agnostic**: they work for any research field. The categories shipped in [`paper-with-code-list.md`](paper-with-code-list.md) merely reflect the author's own directions and are only a starting point — **you define your own taxonomy** (see [Paper List & Custom Categories](#paper-list--custom-categories)).

## What This Repo Does

| Capability | Description | Output |
|------------|-------------|--------|
| **Paper curation** | Given a paper alias or hints, search for full title, arXiv link, venue/year, official code, and framework; write into the list by category and sort by arXiv ID | Table rows in [`paper-with-code-list.md`](paper-with-code-list.md) |
| **Deep reading** | Given a paper (link or list row), produce triple-column HTML (original · Chinese translation · analysis) with Feynman summary, structured Q&A, deep-dive, and logic diagrams | `paper-reading/{slug}.html` |

Both capabilities are implemented as [Agent Skills](https://agentskills.io/specification) under `skills/` (canonical source). Symlinks let each tool discover them from its own path:

| Tool | Discovery path |
|------|----------------|
| **Cursor** | `.cursor/skills/` → `skills/` |
| **Claude Code** | `.claude/skills/` → `skills/` |
| **Codex** | `.agents/skills/` → `skills/` |

Describe what you want in natural language; the matching skill is loaded automatically.

## Repository Structure

```
paper-with-code-skills/
├── README.md                       # This file (English)
├── README.zh-CN.md                 # Chinese README
├── paper-with-code-list.md         # Paper list (example taxonomy; Title|Paper|Conf|Code)
├── paper-reading/                  # Deep-reading HTML output
│   ├── ddpm.html                   # DDPM triple-column example
│   └── assets/{slug}/              # Images per reading
├── skills/                         # Canonical skill source (edit here)
│   ├── add-paper-to-list/          # Skill 1: add papers to the list
│   │   ├── SKILL.md                # Workflow, sources, table format, sorting rules
│   │   └── categories.md           # User phrases ↔ list sections ↔ anchors
│   └── paper-logic-reading/        # Skill 2: triple-column deep reading
│       ├── SKILL.md                # Workflow, fidelity rules, deep analysis
│       ├── template.html           # HTML skeleton (KaTeX, highlights, sticky nav)
│       └── examples.md             # DDPM example metadata and commands
├── .cursor/skills/                 # → skills/ (Cursor)
├── .claude/skills/                 # → skills/ (Claude Code)
└── .agents/skills/                 # → skills/ (Codex)
```

## Usage

No scripts to run manually — open this repo in Cursor, Claude Code, or Codex and describe what you want; the matching skill loads and runs.

> **Note:** After cloning, symlinks should work on macOS/Linux. If a tool does not see skills, restart the agent session. On Windows without symlink support, copy or link `skills/` manually to the tool’s discovery path above.

### 1. Add papers to the list (`add-paper-to-list`)

**Triggers:** “Add paper XXX”, “Add XXX to the paper list”, or a batch of aliases with optional domain, repo, or venue hints.

**Workflow:**

1. Parse input (alias, full-title hints, domain, repo, venue)
2. Search (arXiv / Semantic Scholar / Google Scholar / HF Papers; cross-check ≥2 sources)
3. Read `paper-with-code-list.md`; pick section via [`categories.md`](skills/add-paper-to-list/categories.md)
4. Insert table row and **re-sort the whole section by ascending arXiv ID**
5. Validate (title, links, venue, code, framework, category, order)
6. Ask whether to `git` commit after confirmation

**Table row format:**

```markdown
| {Title} | [{Full Title}]({paper_url}) | {Conf} | [{Framework}]({code_url})
```

### 2. Deep paper reading (`paper-logic-reading`)

**Triggers:** “Deep read this paper”, “logic analysis”, “triple-column HTML”, plus arXiv/PDF link or a list row.

Produces a self-contained HTML file, paragraph by paragraph:

- **Left:** Original text with five highlight dimensions (thesis / terms / evidence / concession / method)
- **Middle:** Faithful Chinese translation, aligned per paragraph
- **Right:** Paragraph role, logic position, rhetorical moves or gaps; thicker analysis + diagrams for method and experiments

Also includes **Feynman summary** at the top and **structured ten questions** + **deep dive** at the bottom. Top rule: **fidelity** — if the paper does not state something, write “not stated in paper”; cite sources for claims and numbers; **no fabrication**.

## Examples

### Curation: add DDPM

> User: Add DDPM

Classified under `Diffusion Model`, appended as:

```markdown
| DDPM | [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) | arXiv(2020) / NIPS(2020) | [PyTorch](https://github.com/lucidrains/denoising-diffusion-pytorch)
```

### Deep reading: DDPM

> User: Deep read DDPM

Convert the list row’s `abs` URL to `pdf`, read, and write [`paper-reading/ddpm.html`](paper-reading/ddpm.html) (Abstract, Introduction, Background, Method, Experiments, Conclusion).

Open the HTML in a browser to read the triple-column notes.

## Paper List & Custom Categories

The skills do not hard-code any taxonomy. The list shipped here reflects the **author's own research directions** and is only an example — treat it as a template and replace it with whatever fields you care about (robotics, NLP, systems, bioinformatics, …).

Three ways to make the categories your own:

1. **Edit the list directly** — change the section headings (`##` / `###`) and the table of contents in [`paper-with-code-list.md`](paper-with-code-list.md); start fresh by emptying it.
2. **Edit the mapping** — update [`categories.md`](skills/add-paper-to-list/categories.md), which maps user phrasing → list section → anchor, so the `add-paper-to-list` skill routes papers the way you expect.
3. **Just tell the agent** — specify the target category when adding a paper, or ask it to create a new category; the skill creates the section and updates the TOC for you.

The default example list currently covers:

- **AIGC:** GAN / VAE / Diffusion / applications (Face Editing, Face Swapping)
- **LLM · VLM:** Transformer / ViT / VLM
- **CV:** Backbone / Detection / Segmentation / Tracking / Few-Shot / 3D Face / SOD / Optimization / Survey
