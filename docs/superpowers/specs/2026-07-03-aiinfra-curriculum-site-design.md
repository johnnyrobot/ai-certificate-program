# Phase 3 — AI Infrastructure Certificate Curriculum Site

**Design spec · 2026-07-03**
Project: LACCD non-credit CDCP *Certificate of Completion — "AI Infrastructure and Architecture"* (courses AIINFRA 100–303).
Phase 3 of the modernization project (Phase 1 = deep-research report ✓; Canvas build of all 10 courses ✓).

---

## 1. Goal

A public, static, multi-page **curriculum website** that presents the certificate in as much detail as possible — **the curriculum, not the Canvas course material** (no lectures, labs, quizzes). One landing/overview page plus one page per course (10), navigable as a site. Visually a sibling of **johnnyphung.com** (dev-tool aesthetic à la Firecrawl / Linear). **Light mode only.**

It also surfaces **live labor-market data (LMI/BLS)** tied to the curriculum: a curated, interactive dashboard of the certificate's target occupations, refreshed live from California's open-data portal, with per-course "careers this maps to" widgets.

## 2. Non-goals (YAGNI)

- No Canvas content (lecture text, labs, discussions, quizzes, rubrics) — that lives in Notion/Canvas.
- No dark mode.
- No build toolchain / framework / SPA — plain static HTML + one shared stylesheet.
- No backend, database, or server-side runtime.
- No open-ended BLS/LMI *search* over all ~800 SOC codes (see §7 — decided: curated + interactive, not a general explorer).
- No login, enrollment transactions, or personal-data collection.

## 3. Audience

Prospective adult learners (non-credit), counselors/advisors, and college/district administrators evaluating the program. Tone: clear, credible, encouraging; makes the labor-market case for enrolling.

## 4. Design system (extracted verbatim from johnnyphung.com)

Extract the reference site's inline design system into a shared `styles.css`. Tokens:

- **Color:** `--bg:#FFFFFF`, `--bg-subtle:#FAFAFB`, `--bg-sunken:#F5F6F8`, `--text:#15161A`, `--text-muted:#585C64`, `--text-faint:#767B85`, `--border:#ECECF1`, `--border-strong:#E0E1E8`, `--accent:#4F46E5`, `--accent-hover:#4038C9`, `--accent-bright:#6366F1`, `--accent-soft:#EEEDFD`. Gradient phrase = `linear-gradient(100deg,#4F46E5,#6366F1 55%,#8B5CF6)`.
- **Type:** Inter (400–800) + JetBrains Mono (500–600) via Google Fonts. Headings 800, `letter-spacing:-0.025em…-0.04em`, `clamp()` fluid sizing. Body 17px/1.6.
- **Shape:** radii `14 / 10 / 22 / pill`; four-tier subtle shadows; `--maxw:1180px`, `--gutter:40px`.
- **Components (reused):** skip-link + a11y focus rings; sticky blurred header; mono **kicker** (`01 / outcomes`, square dot); **eyebrow** (`// text`); **chip**/**tag** (mono, pill/rounded); pill **buttons** (primary + ghost, arrow icon, lift on hover); **hero** (dot-grid `radial-gradient` + radial glow + gradient-text phrase); overlapping **stat band**; **section** (96px pad, `.subtle` alternator); **sec-head** (with split variant); lift-on-hover bordered **cards**; **cta-card** (accent-soft); gradient **footer**.
- Responsive breakpoints 1024 / 820 / 540 as in reference. `prefers-reduced-motion` respected. WCAG 2.2 AA target (contrast, focus, semantics, `aria`).

## 5. Architecture & file structure

Static, no build step. Deployable by copying `site/` to any static host (Cloudflare Pages, Hostinger, Netlify). New `site/` folder in project root; repo `git init`'d at project root.

```
site/
  index.html                     ← landing / program overview
  styles.css                     ← shared design system
  app.js                         ← shared: live-LMI fetch + dashboard interactivity (progressive enhancement)
  data/
    curriculum.json              ← all program + course content (generated, §6)
    lmi.json                     ← verified LMI/BLS snapshot + metadata (generated, §7)
  courses/
    aiinfra-100.html … aiinfra-303.html   (10 pages)
  assets/                        ← favicon (inline SVG), og image
build/
  merge_curriculum.py            ← merge agent-extracted Notion data → curriculum.json
  refresh_lmi.py                 ← source CSVs + BLS API → lmi.json (uses BLS key server-side)
  render_site.py                 ← curriculum.json + templates → course HTML pages
```

All `build/` scripts are **Python** (matches existing project tooling: `gen_prompts.py`, `compile.py`). Client-side `site/app.js` is browser JavaScript (no build step). The Extract step is an agent fan-out (Notion MCP) whose structured output `merge_curriculum.py` assembles.

Pages are **deterministically templated** by `render_site` from `curriculum.json` (not authored by LLM agents) so all 10 course pages are structurally identical. Landing page hand-authored against `curriculum.json` + `lmi.json`.

## 6. Content model — `curriculum.json`

**Source of truth = the 10 Notion course home pages** (authoritative built titles/descriptions/objectives + the 16 week-page child titles) + the modernized Notion curriculum page (SLOs, program framing). Local scratchpad JSON (`new_courses.json`, `briefs*.json`, `weeks*.json`) is a cross-check and the source for synthesized week one-liners. Phase-1 report supplies program-level career/pathway prose.

```jsonc
{
  "program": {
    "name": "AI Infrastructure and Architecture",
    "credential": "Certificate of Completion (non-credit, CDCP)",
    "stats": { "courses": 10, "contactHours": 540, "unitEquivalent": 30, "semesters": 3, "weeksPerCourse": 16 },
    "overview": "…", "pathway": "…", "semesters": [ {"n":1,"theme":"Foundations","courses":["100","101","102"],"hours":162}, … ]
  },
  "courses": [
    {
      "code": "100", "title": "…", "subtitle": "…", "semester": 1,
      "description": "…", "hours": 54, "unitEquivalent": 3,
      "prereq": "none|AIINFRA 0xx", "next": "101",
      "objectives": ["…×5"], "slos": ["…×5"],
      "weeks": [ {"n":1,"title":"…","summary":"one sentence, synthesized"}, … {"n":16 …} ],
      "midtermWeek": 8, "capstoneWeek": 16,
      "tools": ["…grouped tags…"],
      "socs": ["15-1252","15-1299"]        // target occupations, from §8 map
    }, …
  ]
}
```

Authoritative titles per Notion (modernized): 201 = *Production Inference Serving & GPU Orchestration*, 202 = *Model Adaptation — Fine-Tuning & Quantization*, 300 = *Agentic AI & the Model Context Protocol (MCP)*, 301 = *Production RAG & LLMOps*, 302 = *AI Security, Guardrails & Governance*. 100/101/102/200/303 confirmed against Notion during Extract (report matrix titles may be stale). Course home IDs are recorded in project memory (`canvas-course-build`).

## 7. Live LMI / BLS dashboard

**Decision: curated occupation set, presented as a live *interactive* dashboard — not an open BLS/LMI search.** Rationale: the site's job is to justify *this* certificate; only Phase-1-verified SOC figures ship; an open search returns unvetted, off-message occupations and is a separate product.

### Data sources (verified reachable 2026-07-03)
- **Occupational (curriculum-related) — LIVE in-browser.** California open-data portal `data.ca.gov` CKAN datastore. OEWS wage resource `aef4c53a-7e17-418c-acc1-d189e39b6caa` and Long-Term Projections 2024–2034 resource `274e273c-d18c-4d84-b8df-49b4d13c14ce`. `datastore_search` / `datastore_search_sql` return JSON and send **`access-control-allow-origin: *`** → callable directly from a static page, no key, no backend.
- **National context — BLS API v2.** Works for national series (e.g. CES Computer Systems Design employment). **Does NOT serve occupational OEWS wages** (confirmed) — so BLS is national context only. **BLS key stays server-side** in `refresh_lmi.py`; national figures are baked into `lmi.json` (BLS national series update monthly, so a refreshable snapshot is effectively current). Key is never emitted to the browser.

### Progressive-enhancement pattern (never breaks)
1. `lmi.json` ships the **Phase-1-verified 8-occupation snapshot** (CA EDD OEWS median/mean/percentile wages + 2024–34 growth + openings, `asOf` labels) + baked BLS national context. This always renders and always matches the verified report.
2. On load, `app.js` queries `data.ca.gov` for the same 8 SOCs' latest wages + projections. On success: update numbers in place, show green badge `● live · updated <date> · data.ca.gov`. On any failure (offline/CORS edge/timeout): silently keep the snapshot with its `asOf` label. Results cached briefly in `localStorage`.

### The 8 verified occupations (baked snapshot)
| SOC | Occupation | CA median wage | Growth 2024–34 | Openings |
|---|---|--:|--:|--:|
| 15-2051 | Data Scientists | $145,554 | **+37.1%** (fastest) | 40,180 |
| 15-1221 | Computer & Info Research Scientists | $163,554 | +26.1% | 7,690 |
| 15-1252 | Software Developers | $179,292 | +18.4% | 207,260 |
| 11-3021 | Computer & Info Systems Managers | $221,952 | +16.5% | 82,270 |
| 15-1241 | Computer Network Architects | $163,317 | +11.8% | 9,510 |
| 15-1299 | Computer Occupations, All Other (AI/ML/MLOps catch-all) | $138,203 | +11.1% | 59,320 |
| 15-1211 | Computer Systems Analysts | $131,295 | +9.7% | 41,500 |
| 15-1244 | Network & Computer Systems Administrators | $109,420 | −4.5% (only decliner) | 11,510 |

### Interactivity (the "explorable" feel, on the curated set)
- Sort by wage / growth / openings; filter by **semester** or **by course**.
- Click a row → expand **10th→90th percentile wage band** (entry vs. senior pay).
- "Fastest-growing statewide" highlight + the report's AI-displaces-and-creates narrative.
- Live-refresh badge + `asOf` provenance line.
- **Door open (not built now):** a bounded "related roles" toggle adding 4–6 curated adjacent tech SOCs (DBAs, InfoSec Analysts, etc.). Deferred.

### Per-course "careers this maps to" widget
Each course page renders a compact card of its 1–3 mapped SOCs (from the course's `socs`), pulling the **same live data** — so LMI is tied to the curriculum course-by-course, not just program-wide.

### `refresh_lmi.py`
Re-freezes `lmi.json` from local source CSVs (`oews_2009_2025.csv`, `ca_projections_2024_2034.csv`) + a BLS national pull (key from env/local, not committed). Idempotent; run to update the baked fallback. Emits `asOf` metadata.

## 8. Course → target-occupation (SOC) map

Uses only the 8 verified SOCs.

| Course | Focus | SOCs |
|---|---|---|
| 100 Intro to AI Systems & Infrastructure | broad on-ramp | 15-1299, 15-1252 |
| 101 Development Environments & Tools | Python/Git/Jupyter | 15-1252, 15-1299 |
| 102 Containerization & Orchestration | Docker/K8s/IaC | 15-1241, 15-1244, 15-1252 |
| 200 Cloud Platforms for AI | SageMaker/Vertex/Azure ML | 15-1252, 15-1299, 11-3021 |
| 201 Production Inference & GPU Orchestration | vLLM/Triton/K8s GPU | 15-1252, 15-1299 |
| 202 Model Adaptation (Fine-Tuning & Quantization) | PEFT/quant | 15-2051, 15-1299 |
| 300 Agentic AI & MCP | agents/MCP | 15-1252, 15-1299 |
| 301 Production RAG & LLMOps | RAG/eval/observability | 15-2051, 15-1299 |
| 302 AI Security, Guardrails & Governance | security/FinOps | 15-1299, 15-1252 |
| 303 Capstone | integrative | 15-1252, 15-2051, 11-3021 |

## 9. Page specs

### 9.1 Landing (`index.html`)
Header (brand = certificate; nav: Overview · Courses · Careers · Pathway) → **Hero** (kicker `// certificate of completion · non-credit`, gradient-phrase H1, lead, chips `10 courses`·`540 contact hours`·`30-unit equivalent`·`free / non-credit`, CTAs → Courses/Careers) → **Stat band** (overlaps hero) → **01 / Overview** (what it is, who it's for, the arc, CDCP framing) → **02 / Semester roadmap** (3 semesters, courses each) → **03 / The ten courses** (2-col card grid → course pages; primary nav) → **04 / Careers** (the live LMI dashboard, §7) → **05 / Credential & pathway** (non-credit → stackable credit, 30-unit equivalent) → **Footer** (gradient headline, LACCD/program identity, jump links).

### 9.2 Course page template (×10)
Header (brand → home; "← All courses" + anchors Outcomes · Schedule · Tools) → **Compact hero** (kicker `// semester N · AIINFRA NNN`, gradient-keyword title, subtitle, lead = description, meta chips `54 contact hours`·`3-unit equivalent`·`prerequisite: …`·`16 weeks`) → **01 / Outcomes** (5 objectives + 5 SLOs) → **02 / 16-week schedule** (numbered rows: week title + synthesized one-line summary; **Wk 8 midterm** & **Wk 16 capstone** flagged) → **03 / Tools & technologies** (grouped mono tags) → **Careers this maps to** (per-course LMI widget, §7) → **Prev / Next course** nav + back to program → Footer.

## 10. Content pipeline (build)

1. **Extract** — fan out one agent per course (10, parallel) to fetch its Notion home page → `{title, subtitle, description, objectives, weekTitles[16]}`; fetch curriculum page → SLOs; synthesize each week's one-line `summary` from title + local briefs (no 160-page fetch). Merge → `data/curriculum.json`. Cross-check against local `new_courses.json`.
2. **LMI** — `refresh_lmi.py` builds `data/lmi.json` from local CSVs + BLS national pull.
3. **Generate** — hand-author `styles.css`, `app.js`, landing, and the course template; `render_site` templates the 10 course pages from `curriculum.json`.
4. **Verify** — local preview server; screenshot landing + 2–3 course pages; check responsive (mobile/desktop), live-badge success + fallback, links, a11y (focus, contrast, headings). Confirm baked figures equal the verified report table.

## 11. Deployment

Build only, in `site/`. User reviews locally (preview server / open in browser), decides hosting later. Static bundle is host-agnostic.

## 12. Risks / open items

- data.ca.gov datastore vintage may lag the live EDD page by a release cycle — snapshot carries explicit `asOf`; live badge shows the portal's own latest year/quarter.
- Notion titles for 100/101/102/200/303 confirmed during Extract (report matrix may be stale).
- Week one-liners are synthesized (title + briefs), not verbatim Notion module overviews — accuracy check in Verify.
- Google Fonts via CDN (matches reference); acceptable for a hosted site.

## 13. Build sequence (detail deferred to writing-plans)

Scaffold `site/` + `git init` → `styles.css` (design system) → Extract `curriculum.json` → `refresh_lmi.py` → `lmi.json` → landing page → `app.js` (dashboard + live fetch) → course template + `render_site` → generate 10 course pages → Verify (preview + screenshots) → hand off for local review.
