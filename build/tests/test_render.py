import pathlib, re, json
idx = pathlib.Path("site/index.html").read_text(encoding="utf-8")
for needle in ['id="lmi-table"','id="lmi-badge"','data-state="snapshot"','class="roadmap"',
               '540','30-unit','href="courses/aiinfra-100.html"','href="courses/aiinfra-303.html"',
               '<link rel="stylesheet" href="styles.css">','data-sort="growth"']:
    assert needle in idx, f"index.html missing {needle}"
assert idx.count('class="lmi-row"') == 8, "index must bake all 8 occupation rows"
cur = json.loads(pathlib.Path("site/data/curriculum.json").read_text())
for c in cur["courses"]:
    h = pathlib.Path(f"site/courses/aiinfra-{c['code']}.html").read_text(encoding="utf-8")
    assert c["title"] in h, f"{c['code']} title missing"
    assert h.count('class="sched-row') == 16, f"{c['code']} must have 16 schedule rows"
    assert 'class="is-midterm"' in h.replace('sched-row is-midterm','is-midterm') or 'is-midterm' in h, f"{c['code']} midterm flag"
    assert 'is-capstone' in h, f"{c['code']} capstone flag"
    assert 'class="careers-widget"' in h and 'data-socs' in h, f"{c['code']} careers widget"
    assert '../styles.css' in h and '../app.js' in h, f"{c['code']} asset links"
    for o in c["objectives"]: assert o.split("(")[0][:30] in h, f"{c['code']} objective missing"
print("test_render OK")
