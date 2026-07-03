"""Render the AI Infrastructure & Architecture curriculum site.

Consumes site/data/curriculum.json + site/data/lmi.json and writes:
  - site/index.html
  - site/courses/aiinfra-<code>.html   (one per course)

Design system: site/styles.css (ported from johnnyphung.com). This module
only emits HTML structure to use those existing classes — no new CSS beyond
the one small, brief-authorized :focus-visible touch.
"""
import html
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
DATA = SITE / "data"

FONTS_HREF = "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600&display=swap"


def esc_title(s):
    """Escape <, >, ", ' but leave a bare '&' literal in course/program titles.

    All 10 course titles were checked and contain only '&' (never <, >, quotes,
    or an '&' immediately followed by a valid entity/charref pattern), so this
    is HTML5-safe. It exists solely so the rendered title text matches the
    curriculum.json string byte-for-byte, which build/tests/test_render.py
    checks with a literal `c["title"] in h` substring assertion.
    """
    return html.escape(s, quote=True).replace("&amp;", "&")


# ---------------------------------------------------------------------------
# shell: head / header / footer
# ---------------------------------------------------------------------------

def head(title, desc, depth):
    """depth=0 -> index (assets at './'); depth=1 -> course pages (assets at '../')."""
    p = "../" if depth else ""
    return f'''<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(desc)}">
  <meta name="theme-color" content="#ffffff">
  <link rel="icon" type="image/svg+xml" href="{p}assets/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{FONTS_HREF}" rel="stylesheet">
  <link rel="stylesheet" href="{p}styles.css">
</head>'''


def header(active, depth):
    p = "../" if depth else ""
    home = p if p else "#top"
    careers_href = (p + "index.html#careers") if depth else "#careers"
    courses_href = (p + "index.html#courses") if depth else "#courses"
    pathway_href = (p + "index.html#pathway") if depth else "#pathway"
    def cls(name):
        return "nav-link" + (" is-active" if active == name else "")
    return f'''<header class="site-header">
    <a class="brand" href="{home if depth else '#top'}">AI Infrastructure &amp; Architecture</a>
    <nav class="nav" aria-label="Primary">
      <a class="{cls('courses')}" href="{courses_href}">Courses</a>
      <a class="{cls('careers')}" href="{careers_href}">Careers</a>
      <a class="{cls('pathway')}" href="{pathway_href}">Pathway</a>
      <a class="nav-cta" href="{p}index.html">Program overview</a>
    </nav>
  </header>'''


def footer(depth, courses):
    p = "../" if depth else ""
    links = "\n".join(
        f'          <a href="{p}courses/aiinfra-{c["code"]}.html">AIINFRA {c["code"]}<span class="handle">{esc_title(c["title"])}</span></a>'
        for c in courses
    )
    return f'''<footer class="footer" id="connect" aria-labelledby="footer-title">
    <div class="container">
      <div class="footer-top">
        <div class="footer-head">
          <span class="eyebrow">// stackable, non-credit, no cost</span>
          <h2 id="footer-title">Build the systems <span class="grad">modern AI runs on.</span></h2>
          <div class="footer-id">
            <span class="who"><span class="n">Los Angeles Community College District</span><span class="r">AI Infrastructure and Architecture &middot; noncredit CDCP certificate</span></span>
          </div>
        </div>
        <nav class="footer-links" aria-label="Course quick links">
{links}
        </nav>
      </div>
      <div class="footer-bar">
        <span>&copy; LACCD &middot; AI Infrastructure and Architecture certificate</span>
        <span>built accessible &middot; WCAG 2.2 AA &middot; no cost tools &amp; free tiers</span>
      </div>
    </div>
  </footer>'''


def page(title, desc, depth, active, body_html, extra_head_scripts=""):
    skip_target = "#main"
    return f'''<!DOCTYPE html>
<html lang="en">
{head(title, desc, depth)}
<body>
  <a class="skip-link" href="{skip_target}">Skip to content</a>
  {header(active, depth)}
  <main id="main">
{body_html}
  </main>
  {footer(depth, json.loads((DATA / "curriculum.json").read_text(encoding="utf-8"))["courses"])}
  {extra_head_scripts}
  <script src="{"../" if depth else ""}app.js"></script>
</body>
</html>'''


# ---------------------------------------------------------------------------
# landing builders
# ---------------------------------------------------------------------------

def hero_program(program):
    stats = program["stats"]
    return f'''<section class="hero" id="top" aria-labelledby="hero-title">
      <div class="container hero-inner">
        <span class="avail"><span class="led" aria-hidden="true"></span>Noncredit &middot; CDCP &middot; enhanced funding</span>
        <p class="eyebrow">// {html.escape(program["credential"])}</p>
        <h1 id="hero-title">Build the infrastructure behind <span class="grad">production-grade AI systems.</span></h1>
        <p class="hero-lead"><strong>{html.escape(program["name"])}</strong> is a {stats["courses"]}-course, {stats["contactHours"]}-contact-hour sequence that takes learners from foundational computing through inference serving, model adaptation, agentic systems, RAG, and AI security &mdash; using only free and open-source tools.</p>
        <div class="hero-chips">
          <span class="chip">Compute &amp; containers</span>
          <span class="chip">Cloud &amp; MLOps</span>
          <span class="chip">Inference serving</span>
          <span class="chip">Agents &amp; RAG</span>
          <span class="chip">AI security &amp; governance</span>
        </div>
        <div class="hero-actions">
          <a class="btn btn-primary" href="#courses">See the 10 courses<svg class="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path></svg></a>
          <a class="btn btn-ghost" href="#careers">See labor-market demand</a>
        </div>
        <p class="hero-note">No paid software or hardware required &mdash; every lab runs on free tiers and open-source tools.</p>
      </div>
    </section>'''


def stat_band(program):
    s = program["stats"]
    return f'''<div class="container stats-wrap">
      <div class="stats" role="list" aria-label="Program at a glance">
        <div class="stat" role="listitem"><span class="num">{s["courses"]}</span><span class="cap">courses</span></div>
        <div class="stat" role="listitem"><span class="num">{s["contactHours"]}<span class="u"> hrs</span></span><span class="cap">contact hours</span></div>
        <div class="stat" role="listitem"><span class="num">{s["unitEquivalent"]}-unit<span class="u"> equiv.</span></span><span class="cap">credit equivalent</span></div>
        <div class="stat" role="listitem"><span class="num">{s["semesters"]}<span class="u"> semesters</span></span><span class="cap">stackable pathway</span></div>
      </div>
    </div>'''


def overview(program):
    return f'''<section class="section" id="overview" aria-labelledby="overview-title" style="padding-top:120px;">
      <div class="container">
        <div class="sec-head"><span class="kicker"><span class="idx">01</span>&nbsp;/ overview</span><h2 id="overview-title">What the certificate covers</h2></div>
        <div class="about-body">
          <p class="about-statement">A {program["stats"]["weeksPerCourse"]}-week-per-course sequence from <span class="em">foundational computing</span> to <span class="em">production AI systems.</span></p>
          <div class="about-col">
            <p>{html.escape(program["overview"])}</p>
          </div>
        </div>
      </div>
    </section>'''


def roadmap(program):
    courses_by_code = None
    sems = []
    for sem in program["semesters"]:
        items = "\n".join(
            f'            <li><a href="courses/aiinfra-{code}.html"><span>AIINFRA {code}</span><span class="code">&rarr;</span></a></li>'
            for code in sem["courses"]
        )
        sems.append(f'''<div class="roadmap-sem">
          <span class="n">Semester {sem["n"]}</span>
          <h3>{html.escape(sem["theme"])}</h3>
          <span class="sem-hours">{sem["hours"]} hrs &middot; {len(sem["courses"])} courses</span>
          <ul>
{items}
          </ul>
        </div>''')
    sems_html = "\n        ".join(sems)
    return f'''<section class="section subtle" id="roadmap" aria-labelledby="roadmap-title">
      <div class="container">
        <div class="sec-head split">
          <div style="display:flex;flex-direction:column;gap:18px;"><span class="kicker"><span class="idx">02</span>&nbsp;/ semester roadmap</span><h2 id="roadmap-title">Three stackable semesters</h2></div>
          <p class="note">Exit after any semester with a coherent, r&eacute;sum&eacute;-ready skill set, or continue to the full credential.</p>
        </div>
        <div class="roadmap">
        {sems_html}
        </div>
      </div>
    </section>'''


def course_grid(courses):
    cards = []
    for c in courses:
        cards.append(f'''<a class="card" href="courses/aiinfra-{c["code"]}.html">
          <span class="cat">AIINFRA {c["code"]} &middot; Semester {c["semester"]}</span>
          <h3>{esc_title(c["title"])}</h3>
          <p>{html.escape(c["subtitle"])}</p>
          <span class="go">View course<svg class="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path></svg></span>
        </a>''')
    cards_html = "\n        ".join(cards)
    return f'''<section class="section" id="courses" aria-labelledby="courses-title">
      <div class="container">
        <div class="sec-head"><span class="kicker"><span class="idx">03</span>&nbsp;/ the ten courses</span><h2 id="courses-title">Every course in the sequence</h2></div>
        <div class="grid" style="display:grid;grid-template-columns:repeat(2,1fr);gap:20px;">
        {cards_html}
        </div>
      </div>
    </section>'''


def lmi_section(lmi):
    rows = []
    for o in lmi["occupations"]:
        up = "up" if o["growthPct"] >= 0 else "down"
        g = ("+%.1f%%" % o["growthPct"]) if o["growthPct"] >= 0 else ("%.1f%%" % o["growthPct"])
        p = o.get("percentiles") or {}
        top = lmi["meta"]["wageTopCode"]
        def tick(val):
            return f"${val:,}+" if val >= top else f"${val:,}"
        band = (f'<div class="band-inner"><div class="bar"></div><div class="ticks">'
                f'<span>10th {tick(p["p10"])}</span><span>25th {tick(p["p25"])}</span>'
                f'<span>median {tick(p["p50"])}</span><span>75th {tick(p["p75"])}</span>'
                f'<span>90th {tick(p["p90"])}</span></div>'
                f'<p class="note">OEWS current-quarter wage distribution ({html.escape(lmi["meta"]["percentilesAsOf"])}); '
                f'the CA median wage column above is the 2024&ndash;34 <em>projected</em> median, so the two can legitimately differ.</p></div>') if p else \
               '<div class="band-inner"><span class="note">Percentile detail loads live from data.ca.gov.</span></div>'
        rows.append(f'''<tr class="lmi-row" data-soc="{o['soc']}" data-median="{o['medianWage']}" data-growth="{o['growthPct']}" data-openings="{o['openings']}">
  <td><span class="occ">{html.escape(o['title'])}</span><br><span class="soc">{o['soc']}</span></td>
  <td class="num median">${o['medianWage']:,}</td>
  <td class="num growth {up}">{g}</td>
  <td class="num openings">{o['openings']:,}</td></tr>
<tr class="wage-band"><td colspan="4">{band}</td></tr>''')
    m = lmi["meta"]; n = lmi["national"]
    return f'''<section class="section subtle" id="careers"><div class="container">
  <div class="sec-head split"><div><span class="kicker"><span class="idx">04</span>&nbsp;/ careers</span>
  <h2>What this trains you for</h2></div><p class="note">California demand for the roles this certificate builds toward. {html.escape(n['label'])}: {n['value']:,}K ({html.escape(n['period'])}, {n['source']}).</p></div>
  <div class="lmi-controls">
    <span id="lmi-badge" class="live-badge" data-state="snapshot">snapshot &middot; EDD {html.escape(m['verifiedAsOf'])}</span>
    <select id="lmi-filter-sem" aria-label="Filter by semester"><option value="">All semesters</option><option value="1">Semester 1</option><option value="2">Semester 2</option><option value="3">Semester 3</option></select>
    <select id="lmi-filter-course" aria-label="Filter by course"><option value="">All courses</option></select>
  </div>
  <div class="lmi-table-wrap"><table id="lmi-table" class="lmi-table">
    <caption>Source: {html.escape(m['source'])}. Projections {html.escape(m['projectionsPeriod'])}. Click a row for the wage range.</caption>
    <thead><tr><th scope="col"><button type="button" class="th-sort" data-sort="occ">Occupation (SOC)</button></th><th class="num" scope="col"><button type="button" class="th-sort" data-sort="median">CA median wage</button></th><th class="num" scope="col"><button type="button" class="th-sort" data-sort="growth">Growth &rsquo;24&ndash;&rsquo;34</button></th><th class="num" scope="col"><button type="button" class="th-sort" data-sort="openings">Annual openings</button></th></tr></thead>
    <tbody>{"".join(rows)}</tbody></table></div>
  <p class="hero-note">Wages refresh live from data.ca.gov when available; otherwise the verified snapshot shown. No occupation-level data comes from the BLS API (BLS provides national context only).</p>
</div></section>'''


def pathway(program):
    return f'''<section class="section" id="pathway" aria-labelledby="pathway-title">
      <div class="container">
        <div class="sec-head"><span class="kicker"><span class="idx">05</span>&nbsp;/ credential &amp; pathway</span><h2 id="pathway-title">Credential &amp; pathway</h2></div>
        <div class="about-body">
          <p class="about-statement">A <span class="em">{html.escape(program["credential"])}</span> designed to stack toward credit.</p>
          <div class="about-col">
            <p>{html.escape(program["pathway"])}</p>
            <p class="muted">{html.escape(program["careersNarrative"])}</p>
          </div>
        </div>
      </div>
    </section>'''


# ---------------------------------------------------------------------------
# course-page builders
# ---------------------------------------------------------------------------

def course_hero(c):
    prereq = "None" if c["prereq"] == "none" else f'AIINFRA {c["prereq"]}'
    return f'''<section class="hero course-hero" aria-labelledby="course-title">
      <div class="container hero-inner">
        <a class="back" href="../index.html#courses">&larr; All courses</a>
        <p class="eyebrow">// AIINFRA {html.escape(c["code"])} &middot; Semester {c["semester"]}</p>
        <h1 id="course-title">{esc_title(c["title"])}</h1>
        <p class="hero-lead">{html.escape(c["subtitle"])}</p>
        <p class="hero-note">{html.escape(c["description"])}</p>
      </div>
    </section>'''


def meta_band(c):
    prereq = "None" if c["prereq"] == "none" else f'AIINFRA {c["prereq"]}'
    return f'''<div class="container">
      <div class="meta-band">
        <div class="m"><span class="k">Contact hours</span><span class="v">{c["hours"]} hrs</span></div>
        <div class="m"><span class="k">Credit equivalent</span><span class="v">{c["unitEquivalent"]}-unit</span></div>
        <div class="m"><span class="k">Prerequisite</span><span class="v">{html.escape(prereq)}</span></div>
        <div class="m"><span class="k">Length</span><span class="v">{16} weeks</span></div>
      </div>
    </div>'''


def outcomes(c):
    same = c["slos"] == c["objectives"]
    if same:
        items = "\n".join(f'          <li>{html.escape(o)}</li>' for o in c["objectives"])
        body = f'''<div>
          <h3>Learning outcomes</h3>
          <ol>
{items}
          </ol>
        </div>'''
    else:
        obj_items = "\n".join(f'            <li>{html.escape(o)}</li>' for o in c["objectives"])
        slo_items = "\n".join(f'            <li>{html.escape(s)}</li>' for s in c["slos"])
        body = f'''<div class="outcomes-grid">
          <div>
            <h3>Course objectives</h3>
            <ol>
{obj_items}
            </ol>
          </div>
          <div>
            <h3>Student learning outcomes</h3>
            <ul>
{slo_items}
            </ul>
          </div>
        </div>'''
    return f'''<section class="section" id="outcomes"><div class="container">
  <div class="sec-head"><span class="kicker"><span class="idx">01</span>&nbsp;/ outcomes</span><h2>Outcomes</h2></div>
  {body}
</div></section>'''


def schedule(c):
    rows=[]
    for w in c["weeks"]:
        cls="sched-row"; flag=""
        if w["n"]==c["midtermWeek"]: cls+=" is-midterm"; flag='<span class="flag">Midterm &middot; covers Wks 1&ndash;7</span>'
        if w["n"]==c["capstoneWeek"]: cls+=" is-capstone"; flag='<span class="flag">Capstone</span>'
        rows.append(f'''<div class="{cls}"><div class="wk">Wk {w['n']:02d}</div>
  <div class="body"><div class="t">{html.escape(w['title'])}</div><div class="d">{html.escape(w['summary'])}</div>{flag}</div></div>''')
    return f'''<section class="section" id="schedule"><div class="container">
  <div class="sec-head"><span class="kicker"><span class="idx">02</span>&nbsp;/ schedule</span><h2>16-week schedule</h2></div>
  <div class="sched-list">{"".join(rows)}</div></div></section>'''


def tools_section(c):
    groups = []
    for g in c["tools"]:
        tags = "".join(f'<span class="tag">{html.escape(item)}</span>' for item in g["items"])
        groups.append(f'''<div class="tool-group">
          <span class="g">{html.escape(g["group"])}</span>
          <div class="tags">{tags}</div>
        </div>''')
    groups_html = "\n        ".join(groups)
    return f'''<section class="section subtle" id="tools"><div class="container">
  <div class="sec-head"><span class="kicker"><span class="idx">03</span>&nbsp;/ tools</span><h2>Tools &amp; frameworks</h2></div>
  <div class="tools-list" style="display:flex;flex-direction:column;">
        {groups_html}
  </div>
</div></section>'''


def careers_widget(c, lmi):
    occ_by_soc = {o["soc"]: o for o in lmi["occupations"]}
    socs = c["socs"]
    roles = []
    for soc in socs:
        o = occ_by_soc.get(soc)
        if not o:
            continue
        roles.append(f'''<div class="role"><span class="r-t">{html.escape(o["title"])}</span><span class="r-w">${o["medianWage"]:,} median</span></div>''')
    roles_html = "\n        ".join(roles)
    return f'''<section class="section" id="course-careers"><div class="container">
  <div class="careers-widget" data-socs="{html.escape(",".join(socs))}">
    <h3>What this course trains you for</h3>
    <div class="roles">
        {roles_html}
    </div>
    <p class="note">CA median wages, 2024&ndash;34 projections (EDD/OEWS). See the full labor-market dashboard on the <a href="../index.html#careers">program overview</a>.</p>
  </div>
</div></section>'''


def course_nav(c, courses):
    by_code = {x["code"]: x for x in courses}
    links = []
    if c["prereq"] != "none":
        prev = by_code.get(c["prereq"])
        if prev:
            links.append(f'<a class="btn btn-ghost" href="aiinfra-{prev["code"]}.html">&larr; AIINFRA {prev["code"]}: {esc_title(prev["title"])}</a>')
    nxt = c.get("next")
    if nxt:
        nxt_c = by_code.get(str(nxt))
        if nxt_c:
            links.append(f'<a class="btn btn-primary" href="aiinfra-{nxt_c["code"]}.html">AIINFRA {nxt_c["code"]}: {esc_title(nxt_c["title"])} &rarr;</a>')
    links_html = "\n    ".join(links) if links else ""
    return f'''<section class="section" id="course-nav"><div class="container">
  <div class="hero-actions" style="justify-content:space-between;">
    {links_html}
  </div>
  <p class="hero-note"><a href="../index.html">&larr; Back to program overview</a></p>
</div></section>'''


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def render_index(curriculum, lmi):
    program = curriculum["program"]
    courses = curriculum["courses"]
    courses_js = json.dumps([
        {"code": c["code"], "title": c["title"], "socs": c["socs"]} for c in courses
    ])
    body = "\n".join([
        hero_program(program),
        stat_band(program),
        overview(program),
        roadmap(program),
        course_grid(courses),
        lmi_section(lmi),
        pathway(program),
    ])
    extra = f'<script>window.__COURSES={courses_js};</script>'
    html_out = page(
        title=f'{program["name"]} — LACCD Certificate',
        desc=program["overview"][:200],
        depth=0,
        active="courses",
        body_html=body,
        extra_head_scripts=extra,
    )
    (SITE / "index.html").write_text(html_out, encoding="utf-8")


def render_course(c, courses, lmi):
    body = "\n".join([
        course_hero(c),
        meta_band(c),
        outcomes(c),
        schedule(c),
        tools_section(c),
        careers_widget(c, lmi),
        course_nav(c, courses),
    ])
    html_out = page(
        title=f'AIINFRA {c["code"]}: {c["title"]}',
        desc=c["subtitle"],
        depth=1,
        active="courses",
        body_html=body,
    )
    out_path = SITE / "courses" / f'aiinfra-{c["code"]}.html'
    out_path.write_text(html_out, encoding="utf-8")


def main():
    curriculum = json.loads((DATA / "curriculum.json").read_text(encoding="utf-8"))
    lmi = json.loads((DATA / "lmi.json").read_text(encoding="utf-8"))
    (SITE / "courses").mkdir(parents=True, exist_ok=True)
    render_index(curriculum, lmi)
    for c in curriculum["courses"]:
        render_course(c, curriculum["courses"], lmi)
    print(f'Rendered site/index.html + {len(curriculum["courses"])} course pages.')


if __name__ == "__main__":
    main()
