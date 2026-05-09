# How to apply these changes to your repo

This bundle redesigns your Hugo Blox site into an editorial-minimalist UI/UX
portfolio that puts your published AR/VR + haptics work front and center, and
adds **three deep case-study pages** for your flagship 1st-author projects. It
keeps everything Hugo Blox can build natively — no custom Hugo layouts to
maintain, just new content, a new menu, and one CSS override file.

---

## 1. Files in this bundle

```
mywebsite-changes/
├── HOW-TO-APPLY.md                           ← you're reading this
├── assets/scss/custom.scss                   ← visual system (typography, cards, nav, buttons)
├── content/_index.md                         ← homepage rebuilt
├── content/authors/admin/_index.md           ← rewritten About / role / interests
├── content/publication/                      ← full case-study bodies for 3 flagship papers
│   ├── conference-paper-fiery-hands/index.md
│   ├── conference-paper-thermal-masking/index.md
│   └── journal-article-snow/index.md
├── config/_default/menus.yaml                ← new nav: Work · Publications · Approach · News · Contact
├── config/_default/params.yaml               ← light mode default, updated SEO + footer text
└── tools/polish-publications.py              ← one-shot: marks every paper featured + adds richer tags
```

A static preview of the new look lives one folder up at
`mywebsite-preview.html`. Open it in a browser before committing.

---

## 2. Apply (3 minutes)

```bash
# from the root of your DRAGONSTRIKE/mywebsite clone
git checkout -b portfolio-redesign

# 1. Drop the new/edited files in (the bundle mirrors the repo layout)
cp -r path/to/mywebsite-changes/assets       ./
cp -r path/to/mywebsite-changes/content      ./
cp -r path/to/mywebsite-changes/config       ./
cp -r path/to/mywebsite-changes/tools        ./

# 2. Polish every publication's metadata in one shot
python tools/polish-publications.py

# 3. Local preview
hugo server -D
# open http://localhost:1313

# 4. Commit & push
git add -A
git commit -m "Redesign: editorial UI/UX portfolio, add case studies"
git push origin portfolio-redesign
```

> The migration script is **idempotent** — running it twice is safe. It only
> touches `tags:` and `featured:` lines.

---

## 3. What changed and why

### Visual system (`assets/scss/custom.scss`)
- **Typography:** Fraunces (serif display) + Inter (UI). A tight, editorial
  pairing that signals craft to design hiring managers.
- **Color:** Off-white `#FAFAF7` with near-black ink and a single warm coral
  accent reserved for venue labels (CHI / UIST / etc.).
- **Cards:** Hairline border, no shadow, subtle hover lift. Featured images
  desaturate slightly at rest and re-saturate on hover.
- **Tags:** All-caps tracked pills.
- **Nav:** Frosted glass, name in serif, links at 70% opacity until hover.
- **Spacing:** Sections breathe at `clamp(4rem, 8vw, 8rem)` — the single
  biggest jump in perceived quality.

### Homepage (`content/_index.md`)
- Hero stays dark + image-backed (your `background.png`) with a darker
  brightness filter so text reads cleanly.
- New **Selected Work** section directly under the hero, pulling every
  publication where `featured: true`. The migration script flips every paper
  to featured, so all 8 surface here in a 3-column visual grid.
- Below that: **All Publications** (clean academic citation list),
  **Approach** (your end-to-end process), **News**, and **Contact** with an
  explicit "open to UI/UX, Product Design, UX Research roles" line.

### About (`content/authors/admin/_index.md`)
- Role reframed from "Research Assistant" → **"UX Researcher · AR/VR
  Interaction Designer."**
- Interests trimmed to 3 crisp pillars.
- Bio rewritten to lead with what you design and study, then where you
  publish, then your availability.

### Publications (`tools/polish-publications.py`)
- Every paper gets `featured: true`.
- Single generic `Haptic` / `Haptic devices` tag replaced with a
  designer-readable mix per project (e.g. `AR / VR · Wearable Haptics ·
  Hardware Prototyping · User Study`).
- Fixes the `featured: fasle` typo in `conference-paper-fiery-hands`.

### Menu and params
- Old nav was Bio · Papers · News. New nav: **Work · Publications · Approach · News · Contact**.
- Light mode default; logo `WHKIRL` → `Haokun Wang`; SEO description updated.

---

## 4. Case studies — the most important section

This bundle ships **three full UI/UX case-study pages** as the body of the
publication index files:

```
content/publication/conference-paper-fiery-hands/index.md     ← Fiery Hands (UIST 24)
content/publication/conference-paper-thermal-masking/index.md ← Thermal Masking (CHI 24)
content/publication/journal-article-snow/index.md             ← Let It Snow (IMWUT 24)
```

### Structure (same for all three)
1. **TL;DR** — one paragraph + role/team/timeline/tools/methods table
2. **Context** — what was broken in the world before this project
3. **Approach / Research** — how you framed it
4. **Prototyping** — iteration story, with successes and useful failures
5. **User study** — protocol + headline numbers
6. **Outcome** — venue, video, follow-on impact
7. **Reflection** — what you'd do differently, what you're still figuring out

### ⚠️ Fact-check pass needed before publishing

Each case study has a banner at the top calling this out. Items in
`[brackets]` (e.g. `[N=XX]`, `[XX%]`, `[M=X.X]`) are **placeholders** — I
extracted everything safe to claim from the abstracts, but I left the
specific sample sizes, accuracy %, comfort means, and any other headline
statistics as bracketed placeholders for you to fill in from your own
papers. The **narrative, framings, prototyping iteration story, and
reflection sections are mine** — feel free to rewrite those too if a
different beat fits your real journey better.

### Image placeholders

Inside each case study you'll see HTML comments like:

```markdown
<!-- IMAGE: hero shot of the glove on a hand reaching toward a virtual flame in VR -->
<!-- ![Fiery Hands glove worn during a VR fire interaction](fig-hero.jpg) -->
```

These are **invisible until you activate them**. To drop in a real image:

1. Save the photo into the same folder as `index.md` (e.g.
   `content/publication/conference-paper-fiery-hands/fig-hero.jpg`).
2. In `index.md`, **uncomment the second line** by removing the surrounding
   `<!--` and `-->` so the markdown image renders.

The filenames I suggested for each case study are listed at the top of each
`index.md` in a comment block, so you have a checklist to fill out. Use any
filename you like — just keep the markdown line in sync.

### What images to grab from your papers

Concrete shopping list per case study:
- **Hero** — apparatus + person + visible task. Crop tight, desaturate slightly.
- **Context / landscape** — competitor matrix or "before vs. our approach."
- **Principle diagram** — the perceptual or technical mechanism (paper Fig. 1 or 2).
- **Prototypes V1 / V2 / V3** — iteration story, even if V1 is a breadboard mess. Recruiters love the failures.
- **Study setup** — a participant in context (face blurred or angle-cropped if IRB requires).
- **Results chart** — clean Figure from the paper showing the key numbers.
- **Candid / human moment** — someone laughing during the demo. The difference between a paper and a portfolio.

---

## 5. Things you should still do yourself

1. **Replace `static/uploads/resume.pdf`** with your latest CV — the hero CTA points to it.
2. **Better hero background:** the current `assets/media/background.png` is the theme default. Consider replacing it with a desaturated lab/AR-VR shot of your own.
3. **Featured images:** you already have `featured.png` for every publication. For maximum portfolio impact, swap any that look like flat diagrams for process photos.
4. **Author headshot:** `content/authors/admin/avatar.jpg` — confirm it's a recent, well-cropped portrait at ~600×600.
5. **(Optional) Apply the case-study template to the other 5 papers** if you want full coverage. The template is reusable verbatim.

---

## 6. Roll back

Everything is in one branch. To revert:

```bash
git checkout main
git branch -D portfolio-redesign
```

The `tools/polish-publications.py` script changes content files in place; if
you need to undo, `git checkout -- content/publication/`.
