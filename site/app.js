(() => {
  "use strict";
  const CKAN = "https://data.ca.gov/api/3/action/datastore_search_sql";
  const PROJ = "274e273c-d18c-4d84-b8df-49b4d13c14ce";
  const table = document.getElementById("lmi-table");
  const usd = n => "$" + Math.round(n).toLocaleString("en-US");
  const pct = n => (n >= 0 ? "+" : "") + Number(n).toFixed(1) + "%";
  if (!table) return;
  const tbody = table.tBodies[0];
  const pairs = () => [...tbody.querySelectorAll("tr.lmi-row")].map(r => [r, r.nextElementSibling]);

  // ---- expand/collapse wage band ----
  tbody.addEventListener("click", e => {
    const row = e.target.closest("tr.lmi-row"); if (!row) return;
    row.nextElementSibling.classList.toggle("open");
  });

  // ---- sort ----
  let sortKey = null, sortDir = 1;
  table.querySelectorAll(".th-sort[data-sort]").forEach(th => th.addEventListener("click", () => {
    const k = th.dataset.sort;
    sortDir = sortKey === k ? -sortDir : 1; sortKey = k;
    const val = r => k === "occ" ? r.querySelector(".occ").textContent.toLowerCase()
                                 : parseFloat(r.dataset[k === "median" ? "median" : k]);
    pairs().sort((a, b) => (val(a[0]) > val(b[0]) ? 1 : -1) * sortDir)
           .forEach(([r, band]) => { tbody.appendChild(r); tbody.appendChild(band); });
  }));

  // ---- filter by semester / course (options injected from window.__COURSES if present) ----
  const selSem = document.getElementById("lmi-filter-sem");
  const selCourse = document.getElementById("lmi-filter-course");
  function applyFilter() {
    const socsFor = selCourse && selCourse.value ? selCourse.value.split(",") : null;
    pairs().forEach(([r, band]) => {
      const show = !socsFor || socsFor.includes(r.dataset.soc);
      r.style.display = show ? "" : "none";
      band.style.display = show ? "" : "none";
      if (!show) band.classList.remove("open");
    });
  }
  selSem && selSem.addEventListener("change", applyFilter);
  selCourse && selCourse.addEventListener("change", applyFilter);

  // ---- live refresh from data.ca.gov (progressive enhancement) ----
  function setBadge(state, label) {
    const b = document.getElementById("lmi-badge");
    if (!b) return; b.dataset.state = state; b.textContent = label;
  }
  async function liveRefresh() {
    const rows = [...tbody.querySelectorAll("tr.lmi-row")];
    const socs = rows.map(r => r.dataset.soc);
    const inList = socs.map(s => `'${s}'`).join(",");
    const sql = `SELECT "Standard Occupational Classification (SOC)" soc,"Percentage Change" growth,` +
      `"Total Job Openings" openings,"Median Annual Wage" median FROM "${PROJ}" ` +
      `WHERE "Area Name"='California' AND "Period"='2024-2034' AND ` +
      `"Standard Occupational Classification (SOC)" IN (${inList})`;
    const ctrl = new AbortController(); const to = setTimeout(() => ctrl.abort(), 8000);
    const res = await fetch(CKAN + "?sql=" + encodeURIComponent(sql), { signal: ctrl.signal, headers: { Accept: "application/json" } });
    clearTimeout(to);
    const j = await res.json(); if (!j.success) throw new Error("ckan");
    const by = {}; j.result.records.forEach(r => by[r.soc] = r);
    let n = 0, period = "";
    rows.forEach(r => {
      const rec = by[r.dataset.soc]; if (!rec) return;
      const med = parseFloat(String(rec.median).replace(/[,$]/g, ""));
      const gr = parseFloat(rec.growth), op = parseInt(String(rec.openings).replace(/,/g, ""), 10);
      if (med) { r.dataset.median = med; r.querySelector(".median").textContent = usd(med); }
      if (!isNaN(gr)) { r.dataset.growth = gr; const g = r.querySelector(".growth"); g.textContent = pct(gr); g.className = "num growth " + (gr >= 0 ? "up" : "down"); }
      if (!isNaN(op)) { r.dataset.openings = op; r.querySelector(".openings").textContent = op.toLocaleString("en-US"); }
      n++;
    });
    if (n) setBadge("live", `● live · updated ${new Date().toLocaleDateString("en-US")} · data.ca.gov`);
  }

  // ---- init ----
  document.addEventListener("DOMContentLoaded", () => {
    // populate course filter from a global the page may define
    if (selCourse && window.__COURSES) window.__COURSES.forEach(c => {
      const o = document.createElement("option"); o.value = c.socs.join(","); o.textContent = `${c.code} — ${c.title}`; selCourse.appendChild(o);
    });
    liveRefresh().catch(() => setBadge("snapshot", document.getElementById("lmi-badge").textContent));
  });
})();
