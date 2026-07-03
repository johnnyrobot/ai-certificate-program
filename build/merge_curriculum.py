import json, pathlib
ORDER = ["100","101","102","200","201","202","300","301","302","303"]
SEM = {**{c:1 for c in ORDER[:3]}, **{c:2 for c in ORDER[3:6]}, **{c:3 for c in ORDER[6:]}}
SOCS = {  # from spec §8 — only the 8 verified SOCs
 "100":["15-1299","15-1252"], "101":["15-1252","15-1299"], "102":["15-1241","15-1244","15-1252"],
 "200":["15-1252","15-1299","11-3021"], "201":["15-1252","15-1299"], "202":["15-2051","15-1299"],
 "300":["15-1252","15-1299"], "301":["15-2051","15-1299"], "302":["15-1299","15-1252"],
 "303":["15-1252","15-2051","11-3021"]}
def prereq(code):
    return "none" if code == "100" else ORDER[ORDER.index(code)-1]
def nxt(code):
    i = ORDER.index(code); return ORDER[i+1] if i+1 < len(ORDER) else None
raw = {c: json.loads(pathlib.Path(f"site/data/_raw/{c}.json").read_text()) for c in ORDER}
courses = []
for c in ORDER:
    r = raw[c]
    courses.append({
        "code": c, "title": r["title"], "subtitle": r["subtitle"], "semester": SEM[c],
        "hours": 54, "unitEquivalent": 3, "prereq": prereq(c), "next": nxt(c),
        "description": r["description"], "objectives": r["objectives"], "slos": r["slos"],
        "weeks": r["weeks"],            # [{n,title,summary}] — summaries added in Step 3/here
        "midtermWeek": 8, "capstoneWeek": 16,
        "tools": r["tools"], "socs": SOCS[c],
    })
program = {
  "name":"AI Infrastructure and Architecture",
  "credential":"Certificate of Completion — non-credit (CDCP)",
  "stats":{"courses":10,"contactHours":540,"unitEquivalent":30,"semesters":3,"weeksPerCourse":16,"hoursPerCourse":54},
  "overview": (
    "The AI Infrastructure and Architecture certificate is a 10-course, 540-contact-hour "
    "noncredit sequence (a 30-unit credit equivalent) that takes learners from foundational "
    "computing concepts through production-grade AI systems. Students build the compute, "
    "container, cloud, and data skills that underlie modern AI workloads, then apply them to "
    "production inference serving, model adaptation, agentic systems, retrieval-augmented "
    "generation, and AI security and governance."
    " Each 16-week, 54-hour course pairs lecture with hands-on labs using free and open-source "
    "tools and cloud free tiers, so no paid software or hardware is required to complete the "
    "program. Every course ends in a midterm assessment in week 8 and a capstone project in "
    "week 16, culminating in a final, portfolio-ready capstone course that integrates serving, "
    "evaluation, and governance into one production-grade artifact."
  ),
  "pathway": (
    "The certificate is organized as three stackable semesters — Foundations, Core "
    "Infrastructure, and Applied Production Systems — so a learner can exit after any semester "
    "with a coherent, résumé-ready set of skills, or continue straight through to the full "
    "credential. As a noncredit Chancellor's-Office-recognized CDCP (Credit for Prior Learning-"
    "eligible, enhanced-funding) certificate, the program is designed to articulate toward "
    "credit coursework, giving graduates a stackable, non-credit-to-credit on-ramp into an "
    "associate degree or transfer pathway without repeating material they've already mastered."
  ),
  "careersNarrative": (
    "California labor-market data show the occupations this certificate targets among the "
    "fastest-growing in the state: Data Scientists (+37.1%) and Computer & Information "
    "Research Scientists (+26.1%) are projected to grow far faster than the statewide "
    "all-occupations baseline of 8.8%, and Software Developers — the largest target occupation "
    "at 290,800 workers — is projected to add over 200,000 openings through 2034. AI is "
    "simultaneously displacing routine technical roles (Network & Computer Systems "
    "Administrators is the one target occupation in decline) and creating new demand for "
    "workers who can build, deploy, and govern AI systems — precisely the retraining path this "
    "certificate provides."
  ),
  "semesters":[
    {"n":1,"theme":"Foundations","hours":162,"courses":ORDER[0:3]},
    {"n":2,"theme":"Core Infrastructure","hours":162,"courses":ORDER[3:6]},
    {"n":3,"theme":"Applied Production Systems","hours":216,"courses":ORDER[6:10]},
  ],
}
pathlib.Path("site/data/curriculum.json").write_text(
    json.dumps({"program":program,"courses":courses}, indent=2, ensure_ascii=False), encoding="utf-8")
print("wrote curriculum.json")
