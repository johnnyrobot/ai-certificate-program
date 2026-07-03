# Modernization Report — AIINFRA Non-Credit Certificate of Completion (AI Infrastructure & Architecture)

**Prepared for:** LACCD program-revision team
**Scope:** Regulatory/accreditation compliance, California labor-market justification, and curriculum modernization for the non-credit CDCP Certificate of Completion in AI Infrastructure & Architecture (162h + 162h + 216h = 540h; 10 × 54 contact hours).
**Evidence basis:** Research findings with adversarial verification verdicts. Claims marked *refuted* have been dropped or corrected; claims marked *uncertain* are hedged and collected in §7 for human verification.

> **Evidence note.** The initial automated CCCCO research pass returned unusable placeholder data (a search-tool auth failure), so **§2 was re-researched by hand against primary Chancellor's Office / Title 5 / Education Code sources on 2026-07-02** and is now verified — see references **[C1]–[C6]**. The ACCJC (§3), labor-market (§4), and industry/skills (§5–§6) sections rest on verified primary sources and are cited with confidence.

---

## 1. Executive Summary

The certificate has a sound skeleton — Python/Git dev environments, containers/Kubernetes, cloud ML platforms, self-hosting, provider APIs, Model Context Protocol (MCP), and vector-DB/RAG workflows — but it is built around a **2023–2024 "run models locally + basic RAG" worldview** and has not kept pace with the **2025–2026 production-agentic-systems stack**. The single biggest technical gap is that the program teaches prototyping tools (Ollama, LM Studio, AnythingLLM/Open WebUI, N8N/Langflow/Flowise) as if they were production infrastructure, while a course branded "AI Infrastructure and Architecture" is expected to cover high-throughput inference serving, GPU orchestration at scale, LLMOps observability, guardrails/security, and AI governance [10][12][15][19][20].

**What to change (headline recommendations):**

1. **Keep the non-credit CDCP structure for now, but formally decide the credential path.** Non-credit is the fastest, lowest-friction way to ship and update a fast-moving AI curriculum, and it is **expressly exempt from ACCJC substantive-change review** [5]. The recommendation (§2) is a **stackable non-credit → for-credit pathway**, mirroring the strongest CCC precedents (Grossmont, De Anza) [22][23].
2. **Reframe the "local model" and "low-code" content as dev-only**, and add production serving (vLLM/TGI/TensorRT-LLM), GPU orchestration (GPU Operator, DRA, KAI Scheduler), and disaggregated inference (NVIDIA Dynamo) [15][16][17].
3. **Add the missing production competencies**: agent frameworks (code-first), LLMOps observability/eval, fine-tuning/quantization, modern multi-stage RAG with rerankers and evals, guardrails/security (OWASP LLM Top 10 2025), AI governance (NIST AI RMF / ISO 42001 / EU AI Act), and GPU FinOps [10][12][14][19][20][26].
4. **Expand MCP coverage** — it is *current and correctly placed*; MCP is now under the Linux Foundation's Agentic AI Foundation and is an industry standard, so deepen it (server-building, tool security) rather than replace it [11].
5. **Anchor SLOs, program review, and disaggregated completion/job-placement tracking from day one** to satisfy ACCJC Standard 2 and Eligibility Requirement 11 even though no ACCJC filing is required for a non-credit offering [6][7].
6. **Ground the labor-market justification** in verified EDD data: Data Scientists (+37.1%) and Computer & Information Research Scientists (+26.1%) are the fastest-growing target occupations statewide, Software Developers is the largest-employment and a top-5 bachelor's-level opening occupation, and Network/Systems Administrators is the lone decliner (−4.5%) — reinforcing a *retrain-toward-cloud/MLOps* thesis [1][2][3][8][9].

---

## 2. Regulatory & Compliance Update (CCCCO)

> **Verified section (re-researched 2026-07-02).** The items below are sourced to primary Chancellor's Office / Title 5 / Education Code references **[C1]–[C6]** listed in §9.

### 2.1 Governing handbook — PCAH 8th Edition (November 2019)

- The controlling reference for CCCCO curriculum/program approval is the **Program and Course Approval Handbook (PCAH), 8th Edition (November 2019)** — still the current edition as of mid-2026 [C1]. It is organized into **credit** and **noncredit** components and governs course/program submission, approval, chaptering, and maintenance. Build the revised program narrative and Course Outlines of Record (CORs) to the PCAH 8th-edition **noncredit** specifications.
- Approval flows **college curriculum committee → district governing board → CCCCO Curriculum & Instruction Unit** (Curriculum Inventory submission) [C1][C2]. Noncredit certificates are approved through this CCCCO noncredit process; they are **outside ACCJC substantive-change jurisdiction** (§3.3) [5] but **not** outside Title 5 / CCCCO approval — a separate, required track.

### 2.2 Noncredit certificate types & CDCP enhanced funding

Statutory/regulatory basis: **Ed Code §84760.5** (defines CDCP categories), **Ed Code §84750.5** (uniform FTES apportionment; **§84750.5(d)(4)(A)(i)** codifies CDCP funding at **credit parity**, enacted by **SB 860 (2014)**, effective 2015–16), and **Title 5 §55151** (CDCP program approval) [C3][C4].

- **Enhanced (credit-parity) funding** is available only for noncredit courses in **four instructional domains** — ESL, Elementary & Secondary Basic Skills, **Short-Term Vocational**, and **Workforce Preparation** — **and only when the courses are sequenced (≥2) into an approved certificate** [C3].
- **Certificate of Completion** = a course sequence leading to **improved employment** (short-term vocational / workforce prep). **← Correct classification for the AI Infrastructure certificate.**
- **Certificate of Competency** = a sequence that prepares students to **transition into credit coursework** (credit certificate, associate degree, or transfer) [C3].
- **Bottom line:** the 540-hour AI Infrastructure certificate — classified **Short-Term Vocational → Certificate of Completion** — is CDCP-eligible for enhanced (credit-parity) funding **once CCCCO-approved and documented as leading to improved employment with a demonstrated labor-market need** (which §4 supplies). This confirms and now properly sources the original proposal's funding premise. Enhanced funding is **not automatic** — it follows CCCCO approval of the certificate and its course sequence [C3][C4].

### 2.3 Course Outline of Record (COR) & Distance Education

- Each noncredit COR must meet **Title 5 §55002(c)** standards (objectives, content, methods of instruction and evaluation, SLOs) and the PCAH 8th-edition noncredit COR fields [C1]. The program already includes a **COR template** — align it to these fields.
- **Distance Education:** each course offered online needs a **DE addendum** (Title 5 §55200 et seq.), and instruction must meet the federal **Regular and Substantive Interaction (RSI)** standard (34 CFR 600.2) [4]. Note the separate ACCJC **50%-of-courses DE** substantive-change trigger in §3.3 [4][5].

### 2.4 Compliance checklist mapped to existing program sections

| Requirement | Governing source | Maps to program section | Status / action |
|---|---|---|---|
| PCAH-conformant non-credit program narrative | PCAH (edition TBD) | Overview, Requirements | Verify edition; confirm non-credit fields |
| CDCP category mapping (short-term vocational / workforce prep) | Ed Code / Title 5 (verify) | Overview, Career Pathways | **Add explicit category justification** |
| Labor-market need documentation | CCCCO non-credit approval | Career Pathways, References | Use §4 EDD data |
| COR fields per PCAH non-credit template | PCAH | COR template | Verify field completeness |
| DE addendum + RSI per course | 34 CFR 600.2 (RSI) [4] | Implementation | Add DE addenda if online |
| SLOs + program review + disaggregated data | ACCJC Std 2 / ER 11 [6][7] | Evaluation (SLO/program review) | **Strengthen — §3** |
| Program discontinuance / teach-out | ACCJC Std 2, item 2viii [8-refs below] | Implementation | Add teach-out plan |
| Advisory committee / industry alignment | ACCJC 2.2 [6] | Implementation (advisory) | Confirm active advisory board |

### 2.5 Credential-structure analysis and recommendation

Three options were weighed:

| Option | Unit/hour implication | Approval path | Funding | Assessment |
|---|---|---|---|---|
| **A. Keep non-credit CDCP Certificate of Completion** (status quo) | 540 contact hours (162h + 162h + 216h = 10×54h), no units | CCCCO non-credit approval; **no ACCJC substantive-change** [5] | Enhanced CDCP FTES *if* category-eligible (verify) | Fastest to launch/update; lowest student barrier; best for rapidly-changing AI content |
| **B. Add a for-credit Certificate of Achievement** | Would require conversion to units (~16+ units triggers ACCJC review for credit) [refs below] | CCCCO credit approval **plus** ACCJC administrative approval if ≥16 units and significant resources [refs below] | Standard credit apportionment; transferability | Slower; heavier COR/curriculum-committee load; but confers transcripted, transferable credit |
| **C. Stackable non-credit → credit pathway** (recommended) | Keep 540h non-credit foundation; layer credit certificates on top | Non-credit now; phase in credit later | CDCP enhanced funding on the non-credit tier; credit apportionment on upper tiers | Matches Grossmont/De Anza precedents [22][23]; lowest-barrier entry with an achievement ceiling |

**Recommendation: Option C (stackable non-credit → credit).** Launch/maintain the current non-credit CDCP Certificate of Completion as the accessible entry tier (preserving the ACCJC non-credit exemption and enhanced CDCP funding, pending category verification), and **design the courses so they can later articulate into a for-credit Certificate of Achievement / AS**. This mirrors the two strongest verified CCC precedents:

- **Grossmont College** (Fall 2025) — first CCC Applied AI AS with a **noncredit → degree stack** (AI Fundamentals and AI Developer non-credit Certificates of Completion → Certificate of Achievement/AS, 32 units), including a dedicated *Applied AI in Cloud Computing* course [22].
- **De Anza College** (Fall 2026) — stackable no-cost non-credit foundational certificate → technical certificates (ML, deep learning, NLP, prompt engineering, AI agents) → AS in Applied AI; reported ~222-hour Applied AI Certificate of Completion [23] *(medium confidence — see §7)*.

**Credit-conversion thresholds to plan around (Title 5 §55070, as amended 2025)** [C5][C5a]: a credit **grouping of ≥16 semester units** of degree-applicable coursework **must** be Chancellor-approved and can **only** be titled **"Certificate of Achievement"** (transcriptable); only ≥16-unit certificates are **federal Title IV financial-aid eligible**. A district **may optionally** submit **8 to <16 semester units** for Certificate-of-Achievement approval. Sequences **<8 units** (or not submitted) are locally-approved certificates that **cannot** use the "Certificate of Achievement / Completion / Competency" titles or appear on the transcript, and a certificate **cannot** consist solely of basic-skills courses. *(The April 2025 §55070 revision refined wording — "grouping" vs "sequence," the intersegmental-GE definition — but kept these unit thresholds.)* Separately, **ACCJC** treats a new ≥16-unit credit certificate requiring significant institutional resources as an **Administrative Approval** substantive change; **non-credit tiers remain exempt throughout** [5].

---

## 3. Accreditation (ACCJC)

### 3.1 The 2024 Standards touchpoints

The 2024 ACCJC Accreditation Standards (adopted June 2023; June 2025 edition) are organized into four standards: **Standard 1 (Institutional Mission and Effectiveness), Standard 2 (Student Success), Standard 3 (Infrastructure and Resources), Standard 4 (Governance and Decision-Making)** [6]. **Standard 2** governs instructional program design for this certificate:

- **2.1** — academic programs must be in fields of study consistent with the institution's mission, with appropriate breadth, depth, and expected learning outcomes (ER 3, ER 9, ER 12) [6].
- **2.2** — the institution, relying on faculty and other stakeholders, designs and delivers programs reflecting **relevant discipline and industry standards** (ER 3, 9, 11, 14) — directly supports justifying the AI curriculum against current industry practice (which §5–§6 supply) [6].
- **2.5** — scheduling must ensure certificate programs can be completed in the expected period of time (ER 9) [6].
- **2.9** — the institution conducts **systematic review and assessment** of program quality (ER 11, 14) — the program-review/SLO engine [6].
- **1.3** and required documentation **item 1v** — institution-set standards for **certificate completion** specifically, alongside course completion, degree/transfer, job placement, and licensure pass rates, reviewed via **meaningfully-disaggregated data** [6].

### 3.2 SLO / assessment obligations (ER 9 and ER 11)

**Eligibility Requirement 11** is the program-level SLO/assessment anchor: publish each program's expected SLOs and any program-specific achievement outcomes, and demonstrate through **regular, systematic assessment** that completers achieve them — including **review of meaningfully-disaggregated data to identify and close achievement gaps** [7]. **ER 9** requires programs of **sufficient content and length**, at appropriate rigor, culminating in identified outcomes [7].

**Action:** Even though a non-credit certificate triggers no ACCJC filing, the college must still (a) publish program SLOs, (b) run a program-review cycle, and (c) track completion and job-placement data disaggregated by student group, in the program's **Evaluation** section [6][7]. *(Caveat: ER 9/ER 11 documentation is framed around degree programs; applying it to a non-credit certificate is a reasonable inference but not named explicitly in the ERs — see §7.)*

### 3.3 Substantive-change implications

- **Non-credit programs are exempt from ACCJC's substantive-change process** — no notification, administrative approval, or committee review. This is confirmed verbatim in the Substantive Change Manual (May 2026), which lists "Non-credit courses and/or programs" as an exempt category [5]. *(Correction per verdict: the manual lists **five** exempt categories, not four; the load-bearing conclusion — non-credit triggers no substantive-change filing — holds [5].)*
- **Distance Education exception applies regardless:** if **50% or more of the courses** are delivered via distance/correspondence education, advance notice through the substantive-change process is still expected, and the **first course in a DE modality** requires Administrative Approval; federal **RSI** requirements apply [4][5]. This matters if the certificate is delivered substantially online.
- **Teach-out / program discontinuance:** ACCJC required-documentation **item 2viii** requires policies ensuring enrolled students can complete in a timely way if a program is eliminated [6]. Given how fast AI tooling changes, build a **teach-out plan** into the Implementation section for any future course sunset.
- The specific substantive-change *process timelines* (ALO inquiry form; 15-day notification acknowledgment; 30/90/180-day administrative-approval windows) are largely confirmed, **but the committee-approval payment deadline is internally inconsistent in ACCJC's own manual** (Section 2 prose says "within 2 weeks," the flowchart says "at least 30 days") — flagged in §7 [5].

---

## 4. Labor Market Justification (California)

**Data sources & vintage.** Figures below come from **EDD's OEWS wage file** (California-Statewide; **May 2024 employment estimates with wages escalated to Q1 2025 dollars**) and **EDD's Long-Term Occupational Employment Projections 2024–2034**, cross-referenced with the **2025 California Jobs Market Report** [1][2][3]. All eight occupation figures were verified exactly against source [verdicts: *confirmed*].

**BLS-API / OEWS data caveat.** (1) The bulk EDD OEWS CSV used here is **one release cycle behind** the live EDD OEWS page, which now shows May 2025 employment / Q1 2026 wages — so employment counts differ slightly between the OEWS survey file and the projections file (different release vintages); both are legitimate official EDD numbers and are cited separately [9]. (2) There is **no standalone SOC code** for "MLOps Engineer" or "AI Engineer"; those roles are absorbed into 15-1252, 15-2051, and 15-1299, and any role-specific demand figures come from **private vendors (Lightcast), not government statistics** — treat as directional only [13]. (3) The statewide **8.8% baseline** is on the 2023–2033 cycle while occupation growth rates are 2024–2034 — a minor cross-cycle comparison [8].

### 4.1 Per-occupation table (California statewide)

| SOC | Occupation | Base employment (2024, projections file) | Median annual wage | Mean annual wage (OEWS) | Projected growth 2024–34 | Total openings 2024–34 |
|---|---|---|---|---|---|---|
| 15-2051 | **Data Scientists** | 40,400 | $145,554 (proj) / $140,518 (OEWS) | $159,675 | **+37.1%** (fastest) → 55,400 | 40,180 [1] |
| 15-1221 | **Computer & Information Research Scientists** | 8,800 | $163,554 (proj) / $160,538 (OEWS) | $168,344 | **+26.1%** (2nd fastest) → 11,100 | 7,690 [1] |
| 15-1252 | **Software Developers** | 290,800 | $179,292 (proj) / $175,555 (OEWS) | $190,798 | **+18.4%** → 344,400 | 207,260 [1][2] |
| 11-3021 | **Computer & Information Systems Managers** | 96,800 | $221,952 (proj) / $215,259 (OEWS) | $237,025 | **+16.5%** → 112,800 | 82,270 [1] |
| 15-1241 | **Computer Network Architects** | 15,300 | $163,317 (proj) / $142,110 (OEWS) | $154,087 | **+11.8%** → 17,100 | 9,510 [1] |
| 15-1299 | **Computer Occupations, All Other** (catch-all for many AI/ML/MLOps roles) | 84,700 | $138,203 (proj) / $132,249 (OEWS) | $140,015 | **+11.1%** → 94,100 | 59,320 [1] |
| 15-1211 | **Computer Systems Analysts** | 62,000 | $131,295 (proj) / $131,129 (OEWS) | $136,553 | **+9.7%** → 68,000 | 41,500 [1] |
| 15-1244 | **Network & Computer Systems Administrators** | 26,900 | $109,420 (proj) / $109,518 (OEWS) | $117,612 | **−4.5%** (only decliner) → 25,700 | 11,510 [1] |

### 4.2 Demand narrative

- **The AI/ML-adjacent occupations are the fastest-growing.** Data Scientists (+37.1%) and Computer & Information Research Scientists (+26.1%) far outpace the statewide **8.8% all-occupations baseline** (2023–2033, >21 million jobs) [8]. Seven of the eight target occupations exceed that baseline [8].
- **Software Developers is both the largest and a flagged high-demand occupation.** At 290,800 base employment and +18.4% growth, it is one of EDD's named high-demand careers and ranks **#2 among all bachelor's-level occupations** by projected openings (222,110, 2023–2033 cycle; $175,555 median; 9,838 online job ads June 12–Aug 10 2025 via Lightcast/CalJOBS) [2][3].
- **The one decliner reinforces the retraining thesis.** Network & Computer Systems Administrators is the only shrinking target occupation (−4.5%), consistent with cloud automation and managed services absorbing traditional on-prem sysadmin work — a direct argument for **retraining toward cloud/MLOps-adjacent skills** rather than legacy administration [1].
- **AI is simultaneously displacing and creating tech roles.** EDD's 2025 report attributes part of recent high-tech job losses (Professional & Business Services −179,100; Information −105,100) to "the rapid increase in the integration of artificial intelligence-related cost-saving measures," citing AI-driven layoffs shrinking entry-level jobs [3]. This supports training workers toward **higher-value AI-building/AI-operating roles** rather than commoditized ones.
- **Emerging roles corroborate direction (low confidence).** Vendor data (Lightcast) shows generative-AI unique job postings rising from ~55 (Jan 2021) to nearly 10,000 (May 2025), with California/Bay Area a top concentration — directional support for an AI-infrastructure credential, not a primary justification figure [13].

---

## 5. Curriculum Modernization

### 5.1 Course-by-course disposition

**Semester 1 — Foundations**

| Course | Verdict | Add / cut | Modern tools & techniques |
|---|---|---|---|
| **AIINFRA 100 — Intro to AI Systems & Infrastructure** | **KEEP + UPDATE** | Add a "prototype vs. production" framing that recurs across the program; add an AI-governance/ethics primer | Introduce the inference-serving landscape and the OWASP LLM Top 10 2025 [19] and NIST AI RMF [20] at survey level |
| **AIINFRA 101 — Dev Environments & Tools** (Python, Git, Conda/venv, Jupyter) | **KEEP** | Minor: add `uv`/modern packaging awareness; keep Git/Jupyter | Add experiment-tracking preview (MLflow) to foreshadow LLMOps [12] |
| **AIINFRA 102 — Containerization & Orchestration** (Docker, Compose, K8s, IaC) | **KEEP + UPDATE** | Add **GPU-aware** Kubernetes: NVIDIA GPU Operator, Dynamic Resource Allocation (GA in k8s 1.34), MIG partitioning | Terraform/IaC stays; add GPU scheduling concepts to bridge to the new GPU-orchestration module [17] |

**Semester 2 — Deployment**

| Course | Verdict | Add / cut | Modern tools & techniques |
|---|---|---|---|
| **AIINFRA 200 — Cloud Platforms for AI** (SageMaker, Azure ML, Vertex) | **KEEP + UPDATE** | Add cloud ML certification alignment (AWS ML Engineer-Associate, Google Cloud PMLE, Azure AI Engineer) [21]; add CI/CD-for-ML | Managed inference endpoints; cost/quota awareness feeding FinOps [26] |
| **AIINFRA 201 — Self-Hosting & Local Model Servers** (Linux, Hetzner, DO, Ollama, LM Studio) | **UPDATE — reframe as dev-only** | **Explicitly frame Ollama/LM Studio as prototyping**; add production serving engines | **vLLM** (PagedAttention, continuous batching), **TGI v3**, **TensorRT-LLM**; introduce disaggregated prefill/decode (NVIDIA **Dynamo**) [15][16] |
| **AIINFRA 202 — All-in-One AI Apps** (AnythingLLM, Open WebUI, RAG) | **UPDATE** | Keep as an intro to app assembly, but move real RAG rigor into the new RAG course | Frame these as reference UIs, not production RAG [10] |

**Semester 3 — Advanced**

| Course | Verdict | Add / cut | Modern tools & techniques |
|---|---|---|---|
| **AIINFRA 300 — Enterprise AI Services** (OpenAI, Claude, Bedrock, Vertex, OpenRouter APIs) | **KEEP** | Add cost/latency/observability instrumentation of provider calls | Tie provider usage to LLMOps tracing and FinOps [12][26] |
| **AIINFRA 301 — Model Context Protocol Implementation** | **KEEP + EXPAND** | MCP is **current and correctly placed** — deepen it | Add MCP **server-building**, **tool security**, and broader agentic standards (AGENTS.md, A2A); note MCP is now under the Linux Foundation's Agentic AI Foundation with 10,000+ public servers [11] |
| **AIINFRA 302 — Vector Databases & AI Workflows** (Pinecone, Chroma, pgvector/Supabase, N8N, Langflow, Flowise) | **REPLACE/SPLIT** | **Split:** (a) modernize vector-DB selection; (b) move workflow/agents to a new code-first agents course; low-code tools become an on-ramp, not the destination | Add **Qdrant/Milvus/Weaviate/pgvector** selection by scale, **HNSW vs IVF**, **hybrid (dense+sparse) search**, metadata filtering; link to OWASP **LLM08 (vector/embedding weaknesses)** [19][25] |
| **AIINFRA 303 — Capstone** (one version) | **KEEP** | Require a production-grade artifact instrumented with observability + evals + a guardrail | Capstone becomes the integration point for serving, RAG evals, and governance (see Phase 2, §8) |

### 5.2 New courses / modules to fill gaps

1. **Agentic AI & Agent Frameworks (code-first)** — LangGraph (graph-based), CrewAI (role-based), OpenAI Agents SDK (handoff-based, released March 2025), Pydantic AI (2025 breakout); agent state/graph control flow, tool-calling, handoffs, human-in-the-loop interrupts/approvals, multi-agent orchestration. Teach the cost/efficiency lesson (LangGraph fastest on latency; CrewAI ~3× token footprint on simple flows). Fills the gap left by N8N/Langflow/Flowise, which are visual workflow tools, not production agent frameworks [10].
2. **LLMOps: Observability, Tracing & Evaluation** — Langfuse (MIT, self-hostable), Arize Phoenix (50+ faithfulness/relevance/toxicity/hallucination metrics), LangSmith, OpenTelemetry/OpenLLMetry, MLflow tracing; the CLEAR evaluation framework (Cost, Latency, Efficacy, Assurance, Reliability). Currently entirely missing [12].
3. **High-Performance Inference Serving & GPU Orchestration** — vLLM/SGLang/TensorRT-LLM/TGI; Ray Serve, Triton, KServe; continuous batching, PagedAttention/KV-cache, tensor/pipeline parallelism; GPU Operator, DRA, **KAI Scheduler** (gang/topology-aware scheduling), MIG, Slurm-on-K8s (Slinky), SkyPilot; NVIDIA Dynamo disaggregated serving. The **biggest technical gap** for a course branded "Infrastructure and Architecture" [15][16][17].
4. **Model Adaptation: Fine-Tuning & Quantization** — LoRA/QLoRA/PEFT, DPO (has displaced classic RLHF), emerging GRPO; quantization formats **GGUF/AWQ/GPTQ/FP8**, KV-cache quantization; the heuristic "a larger model at lower precision usually beats a smaller model at higher precision." Single-GPU adaptation is accessible to this exact community-college audience [14][18].
5. **Production RAG: Rerankers, GraphRAG & Evals** — hybrid search (dense+BM25), query rewriting, **cross-encoder rerankers**, GraphRAG, agentic RAG; mandatory evaluation with **RAGAS** and **DeepEval** (CI/CD quality gates). Replaces naive embed-and-retrieve [10].
6. **AI Security & Guardrails** — OWASP **LLM Top 10 (2025)**; NeMo Guardrails, **Llama Guard 4** (12B multimodal, released Apr 30 2025), LLM Guard/Rebuff/Prompt Guard, Presidio (PII); direct vs. indirect prompt injection. Currently missing; essential given the agentic focus [19].
7. **AI Governance & Compliance** — **NIST AI RMF** (methodology), **ISO/IEC 42001** (auditable AMS), **EU AI Act** (binding law; prohibited practices + AI literacy applied Feb 2 2025, GPAI obligations Aug 2 2025, most high-risk requirements Aug 2 2026). Increasingly an employer/hiring requirement [20].
8. **GPU FinOps** — cost per 1,000 requests (not per GPU-hour); spot/preemptible for batch; quantization + KV-cache savings; right-sizing; fractional GPUs/MIG. Ties together serving, quantization, and orchestration [26] *(some FinOps case-study figures are vendor-sourced — see §7)*.

### 5.3 Revised program map (162h + 162h + 216h = 540h)

At **54 contact hours per course** (the Chancellor's-Office-recommended 18×3 standard) the full **10-course** sequence totals **540 contact hours** — a **30-unit** credit-equivalent (Semesters 1–2 = three courses/162h each; Semester 3 = four courses/216h, including the AIINFRA 303 capstone). Content is modernized and redistributed within this envelope (an accelerated 6-month/Kubernetes-fundamentals variant remains a valid alternate format).

- **Semester 1 — Foundations (162h):** 100 Intro to AI Systems & Infrastructure *(updated)* · 101 Dev Environments & Tools *(kept)* · 102 Containerization & **GPU-Aware** Orchestration *(updated)*
- **Semester 2 — Serving & Deployment (162h):** 200 Cloud Platforms for AI + CI/CD-for-ML *(updated)* · **201 Production Inference Serving & GPU Orchestration** *(replaces "Self-Hosting"; Ollama/LM Studio reframed dev-only)* · **202 Model Adaptation: Fine-Tuning & Quantization** *(new; replaces "All-in-One AI Apps")*
- **Semester 3 — Applied Production Systems (216h):** **300 Agentic AI & MCP** *(merges enterprise APIs + expanded MCP + code-first agents)* · **301 Production RAG + LLMOps Observability/Evals** *(replaces vector-DB/low-code course)* · **302 AI Security, Guardrails & Governance (+ GPU FinOps)** *(new)* · **303 Capstone** *(kept; production-grade, instrumented artifact)*

---

## 6. In-Demand Skills & Certifications Alignment

Employer demand for **AI Infrastructure Engineer / MLOps / ML Platform / AI/ML Engineer** roles in California converges on a consistent stack. Two live California postings verify the direction: **Scale AI** (Model Serving Platform) requires Python/Go/Rust/C++, Docker/Kubernetes, AWS/GCP + Terraform, and LLM-serving know-how with vLLM/SGLang/TensorRT-LLM as nice-to-haves [24] *(salary/URL specifics flagged in §7)*; **Hashlist** requires production GenAI experience, **MCP servers and agentic AI architectures**, and CI/CD-integrated AI tooling [24].

| Ranked employer-demanded skill/cert [21][24] | Where it lives in the revised curriculum |
|---|---|
| 1. Python (+ Go/Rust/C++ for infra) | 101 (kept) |
| 2. Docker + Kubernetes | 102 (GPU-aware K8s) |
| 3. Cloud platforms (AWS/GCP/Azure) | 200 |
| 4. Infrastructure-as-code (Terraform) | 102, 200 |
| 5. CI/CD (Jenkins, GitHub Actions, GitLab CI) | 200 (CI/CD-for-ML) |
| 6. PyTorch / TensorFlow | 202 (fine-tuning) |
| 7. MLOps/data platform (Databricks, MLflow, Delta Lake, PySpark) | 301 (LLMOps/observability) |
| 8. LLM/GenAI (LangChain, RAG, prompt/agentic, vLLM/SGLang/TensorRT-LLM, MCP) | 201, 300, 301 |
| 9. Monitoring/observability (Prometheus, Grafana) | 301 |
| 10. Certifications (CKA/CKAD; AWS ML Engineer-Associate; Google Cloud PMLE; Azure AI Engineer; Databricks Data/ML Associate) | Align 102 → CKA/CKAD; 200 → cloud ML certs [21] |

**Certification strategy.** Following the **Coastline College** model (AI-for-Cybersecurity AS with NSA CAE-C validation and CompTIA alignment) [22-analog], the certificate can map explicitly to **vendor-neutral Kubernetes certs (CKA/CKAD)** and **cloud ML certs** as preferred qualifications. Reported salary premiums are directional (industry compensation analysis, not government wage data): **CKA ~18–25%, CKS ~25–35%** [24] *(see §7 for the specific ML-postings-share figure)*.

**Statewide positioning.** The CCC **Vision 2030 AI Workplan (July 2025)** funds shared infrastructure (a **$10M initial + $12M scaling** Common Cloud Data Platform) and workforce MOUs with **Nvidia, Google, OpenAI, Microsoft, IBM, Intel and others**, but **does not prescribe a technical AI-infrastructure curriculum** — so a college proposing a specific AI-infrastructure/MLOps non-credit certificate is **filling a real gap the system has not centrally defined**, while aligning with the state's named priorities [27].

---

## 7. Risks & Human-Verification List

**A. CCCCO items — now verified (2026-07-02), with residual procedural confirmations**

1. **§2 was re-researched against primary sources** after the automated pass failed, and is no longer an open gap: PCAH **8th Edition (Nov 2019)** [C1]; CDCP basis Ed Code §84760.5 / §84750.5 + Title 5 §55151, credit-parity funding per SB 860 [C3][C4]; Certificate-of-Achievement thresholds Title 5 §55070 as amended 2025 [C5][C5a]; Vision 2030 stackable/CPL support [C6]. *[resolved]*
2. **CDCP eligibility classification is correct but approval is procedural.** The Short-Term Vocational → Certificate of Completion mapping is right, but enhanced funding still requires **CCCCO approval of the certificate + its course sequence**; confirm the local submission path with your college Curriculum Committee / Articulation Officer before asserting funding in the proposal. *[procedural]*

**B. ACCJC nuances to verify**

3. **Committee-approval payment deadline is internally inconsistent in ACCJC's own manual** ("2 weeks" in prose vs. "30 days" in the flowchart). Do not cite a single figure without checking the current manual [5]. *[uncertain]*
4. **"Category F" label** for the substantive-change category was not verifiable from the retrieved primary source; the manual does not use lettered categories. Do not cite "category F." *[uncertain]*
5. **ER 9 / ER 11 are degree-framed;** applying them to a non-credit certificate is a reasonable inference, not explicit text. Present as best practice, not a naming citation [7]. *[uncertain]*
6. **RSI citation set** (34 CFR 600.2; Standards 1.4/2.1/2.2/2.6/2.9/3.9) comes from a DE-policy PDF not independently re-retrieved; the RSI requirement itself is well-established [4]. *[uncertain]*

**C. Labor-market / skills figures to hedge**

7. **MLOps/AI-Engineer demand numbers are vendor-sourced (Lightcast), not government data** — directional only [13]. *[confirmed as low-confidence]*
8. **Scale AI posting:** technical requirements confirmed, but the cited salary band ($180K–$225K) matches a non-senior listing while a near-duplicate "Senior" listing shows $216,200–$270,250, and the LinkedIn URL digit may be mistyped. Verify exact posting/title/URL before quoting [24]. *[refuted as cited — corrected]*
9. **California ML-postings share:** cited as ~29% but at least one source shows 32%. Verify against the actual CompTIA report table before quoting precisely [24]. *[uncertain]*
10. **Certification salary premiums** are industry compensation analysis, not government wage data — label directional [24]. *[uncertain]*

**D. Curriculum-claim figures to soften**

11. **"~80% of RAG failures are retrieval, not generation"** — **corrected to ~73%**; the 80% figure applies to overall RAG *project* failure rate, a different metric. Use 73% [10]. *[refuted — corrected]*
12. **"60% of new 2026 RAG deployments include eval from day one (up from <30%)"** — single aggregator source; treat as unverified [10]. *[uncertain]*
13. **GPU FinOps case study ($39K→$16K/month) and "55–80% of AI GPU spend is inference"** — single vendor/marketing source; present as illustrative [26]. *[uncertain]*
14. **"Token consumption grows ~20x by 2030"** — closest verified figure is Goldman Sachs' 24× (2026→2030); adjust base year/figure before citing precisely [14/26-adjacent]. *[confirmed-with-adjustment]*
15. **"LoRA/QLoRA cover ~95% of production fine-tuning"** and **vector-DB scale thresholds** (e.g., "Qdrant 500K–50M vectors") are soft rules-of-thumb, not hard statistics [14][25]. *[confirmed-as-illustrative]*
16. **KAI Scheduler "de facto reference"** is promotional framing (CNCF Sandbox project); accurate underlying facts, soften the superlative [17]. *[confirmed-with-nuance]*

**E. Comparative/precedent claims to re-confirm**

17. **De Anza** (222h figure), **Coastline** (NSA CAE-C through 2030), **Chaffey/Bakersfield**, **MiraCosta/Saddleback** precedents were medium/low confidence or not independently re-fetched [22][23]. Confirm before citing specific hours/structures. *[uncertain]*
18. **CCC AI Consortium (cccaic.org)** was unreachable; member list/curriculum templates unverified — confirm via ASCCC/BACCC [22-analog]. *[low confidence]*

---

## 8. Phase 2 & Phase 3 Groundwork

**Phase 2 — Capstone project research (to tee up).** The revised **303 Capstone** should require a *production-grade, instrumented* artifact rather than a prototype: an agentic or RAG system that (a) serves a quantized model via vLLM/TGI, (b) is instrumented with LLMOps tracing (Langfuse/Phoenix) and an automated eval harness (RAGAS/DeepEval), (c) enforces at least one guardrail (NeMo Guardrails / Llama Guard) mapped to an OWASP LLM Top 10 risk, and (d) reports a FinOps metric (cost per 1,000 requests) [12][15][19][26]. Phase 2 research should draft the capstone rubric, define SLO-linked assessment tied to ER 11 [7], and specify facility/GPU-access needs (the CCC Common Cloud Data Platform and NVIDIA/cloud MOUs are potential resources [27]).

**Phase 3 — Interactive web conversion (to tee up).** The final program-revision proposal (Overview, Requirements, Core Curriculum, COR template, Implementation, Evaluation, Career Pathways, References) is a strong candidate for conversion to an **interactive web artifact**: a stackable-pathway visualizer (non-credit → credit), a labor-market dashboard driven by the §4 EDD table, a course-modernization matrix (KEEP/UPDATE/REPLACE), and a skills-to-curriculum crosswalk. Phase 3 groundwork: confirm the canonical section list, freeze the verified data tables, and resolve the §7 verification items so the interactive version ships only confirmed claims.

---

## 9. References

1. California Long-Term Occupational Employment Projections 2024–2034 (EDD CSV, `lt-occ-emp-2024-2034.csv`). https://data.ca.gov/dataset/715d1324-ac02-4b11-b922-86bafa6eb80f/resource/274e273c-d18c-4d84-b8df-49b4d13c14ce/download/lt-occ-emp-2024-2034.csv
2. California OEWS Wage Data (EDD, `oews-2009-2025_original.csv`). https://data.ca.gov/dataset/6411456b-594b-4b73-af57-ce8dd401f2e2/resource/aef4c53a-7e17-418c-acc1-d189e39b6caa/download/oews-2009-2025_original.csv
3. 2025 California Jobs Market Report (EDD, DE 864 Rev. 3 8-25). https://edd.ca.gov/siteassets/files/pdf_pub_ctr/2025_california_jobs_market_report.pdf
4. ACCJC Policy on Distance Education and on Correspondence Education, June 2025. https://accjc.org/wp-content/uploads/Policy-on-Distance-and-on-Correspondence-Education.pdf
5. ACCJC Substantive Change Manual, May 2026 Edition. https://accjc.org/wp-content/uploads/Substantive-Change-Manual.pdf
6. ACCJC 2024 Accreditation Standards (June 2025 edition). https://accjc.org/wp-content/uploads/ACCJC-2024-Accreditation-Standards.pdf
7. ACCJC Eligibility Requirements for Accreditation, January 2024. https://accjc.org/wp-content/uploads/Eligibility-Requirements-for-Accreditation.pdf
8. EDD Employment Projections page (confirms 2024–2034 vintage). https://labormarketinfo.edd.ca.gov/data/employment-projections.html
9. EDD OEWS Employment and Wage Statistics page. https://labormarketinfo.edd.ca.gov/data/oes-employment-and-wages.html
10. RAG in Production 2026: GraphRAG, Hybrid Retrieval, and Evals. https://ailearningguides.com/rag-production-patterns-2026/ · Top 5 Reranking Models (MachineLearningMastery). https://machinelearningmastery.com/top-5-reranking-models-to-improve-rag-results/
11. Donating the Model Context Protocol and establishing the Agentic AI Foundation (Anthropic). https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation · Linux Foundation press release. https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation
12. Best LLM Observability Tools (Firecrawl). https://www.firecrawl.dev/blog/best-llm-observability-tools · Top 5 LLM and Agent Observability Tools (MLflow). https://mlflow.org/top-5-agent-observability-tools/
13. Lightcast: The Generative AI Job Market: 2025 Data Insights. https://lightcast.io/resources/blog/the-generative-ai-job-market-2025-data-insights
14. LLM Fine-Tuning Guide: LoRA, QLoRA, DPO, GRPO, RLHF (Future AGI). https://futureagi.com/blog/llm-fine-tuning-guide-2025/
15. Comparing the Top 6 Inference Runtimes for LLM Serving in 2025 (MarkTechPost). https://www.marktechpost.com/2025/11/07/comparing-the-top-6-inference-runtimes-for-llm-serving-in-2025/
16. Introducing NVIDIA Dynamo (NVIDIA). https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/
17. Kubernetes GPU Scheduling: DRA, KAI, MIG (TechPlained). https://www.techplained.com/kubernetes-gpu-scheduling · Slurm-on-Kubernetes (NVIDIA). https://developer.nvidia.com/blog/running-large-scale-gpu-workloads-on-kubernetes-with-slurm/
18. Quantization Techniques for AI Inference 2026: GGUF, AWQ, GPTQ, FP8 (Sesame Disk). https://sesamedisk.com/quantization-techniques-ai-inference-2026/
19. OWASP Top 10 for LLM Applications 2025 (official). https://genai.owasp.org/llm-top-10/
20. EU AI Act Implementation Timeline (official). https://artificialintelligenceact.eu/implementation-timeline/ · EU AI Act vs NIST AI RMF vs ISO/IEC 42001 (EC-Council). https://www.eccouncil.org/cybersecurity-exchange/responsible-ai-governance/eu-ai-act-nist-ai-rmf-and-iso-iec-42001-a-plain-english-comparison/
21. AWS Certified ML Engineer – Associate. https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/ · Google Cloud Professional ML Engineer. https://cloud.google.com/learn/certification/machine-learning-engineer · Databricks ML Associate. https://www.databricks.com/learn/certification/machine-learning-associate
22. Grossmont College Applied AI AS/Certificate (catalog). https://catalog.gcccd.edu/grossmont/associate-degree-programs-certificates/stem/artificial-intelligence-as-cert-achievement/ · Grossmont launch news. https://www.gcccd.edu/news/articles/2025/2025-11-06-applied-ai-at-grossmont.php · Foothill College AI Certificate. https://catalog.foothill.edu/degrees-certificates/artificial-intelligence/ · Coastline AI for Cybersecurity AS. https://catalog.cccd.edu/coastline/pathways/computer-cyber-sciences/cybersecurity/ai-cybersecurity-as/
23. De Anza College Applied AI degree. https://www.deanza.edu/news/2026/applied-artificial-intelligence-degree-fall-2026.html · GovTech coverage. https://www.govtech.com/education/higher-ed/de-anza-college-launches-associate-degree-in-applied-ai
24. AI Infrastructure Engineer, Model Serving Platform (Scale AI). https://www.linkedin.com/jobs/view/ai-infrastructure-engineer-model-serving-platform-at-scale-ai-4196120822 *(URL/salary to verify — §7)* · AI Infrastructure Engineer (Hashlist). https://www.linkedin.com/jobs/view/ai-infrastructure-engineer-at-hashlist-4422814745 · CompTIA State of the Tech Workforce 2026. https://www.comptia.org/en-us/resources/research/state-of-the-tech-workforce-2026/ · LinkedIn Jobs on the Rise 2026. https://www.linkedin.com/pulse/linkedin-jobs-rise-2026-25-fastest-growing-roles-us-linkedin-news-dlb1c
25. Best Vector Databases 2026 (Firecrawl). https://www.firecrawl.dev/blog/best-vector-databases · pgvector vs Pinecone vs Qdrant vs Weaviate (Kalvium). https://www.kalviumlabs.ai/blog/vector-databases-compared-pgvector-pinecone-qdrant-weaviate/
26. AI Inference Cost Economics in 2026: GPU FinOps Playbook (Spheron). https://www.spheron.network/blog/ai-inference-cost-economics-2026/ *(vendor source — treat figures as illustrative, §7)* · FinOps for AI (Flexera). https://www.flexera.com/blog/finops/finops-for-ai-governing-the-unique-economics-of-intelligent-workloads/
27. California Community Colleges Vision 2030 Artificial Intelligence Workplan, July 2025. https://www.cccco.edu/-/media/CCCCO-Website/docs/vision2030/artificial-intelligence-workplan.pdf · CCCCO AI initiative. https://ai.cccco.edu/

### CCCCO Primary Sources — §2 (hand-verified 2026-07-02)

- **[C1]** Program and Course Approval Handbook (PCAH), **8th Edition (Nov 2019)** — current edition; credit + noncredit components. https://www.cccco.edu/-/media/CCCCO-Website/docs/curriculum/program-course-approval-handbook-8th-edition.pdf
- **[C2]** CCCCO Curriculum & Instruction Unit (approval authority for 116 colleges). https://www.cccco.edu/About-Us/Chancellors-Office/Divisions/Educational-Services-and-Support/What-we-do/Curriculum-and-Instruction-Unit
- **[C3]** CCCCO Noncredit Curriculum & Instructional Programs — CDCP categories; Certificate of Completion vs Certificate of Competency; enhanced-funding rules. https://www.cccco.edu/About-Us/Chancellors-Office/Divisions/Educational-Services-and-Support/What-we-do/Curriculum-and-Instruction-Unit/Curriculum/Noncredit-Curriculum-and-Instructional-Programs
- **[C4]** ASCCC Noncredit Instruction / Adult Education Basics — Ed Code §84750.5 / §84760.5, Title 5 §55151, SB 860 (2014) credit-parity funding. https://www.asccc.org/sites/default/files/Noncredit_Instruction_Adult_Education_Basics.pdf
- **[C5]** Title 5 §55070 Credit Certificates (Cornell LII). https://www.law.cornell.edu/regulations/california/5-CCR-55070
- **[C5a]** CCCCO Final Revisions to Title 5 §55070 re Credit Certificates of Achievement (adopted 2025). https://www.cccco.edu/-/media/CCCCO-Website/docs/regulatory-action/final-reg-text-certificate-of-achievement-final-v2-4-25-a11y-002.pdf
- **[C6]** CCCCO Vision 2030: A Roadmap for California Community Colleges — mirrored credit/noncredit pathways; Credit for Prior Learning via the MAP (Mapping Articulated Pathways) Initiative. https://www.cccco.edu/About-Us/Vision-2030 · https://vision2030.cccco.edu/

---

# Appendix: Compiled References

# Reference List

## A. CCCCO / Title 5 / Ed Code

1. [CCCCO Artificial Intelligence Workplan, July 2025](https://www.cccco.edu/-/media/CCCCO-Website/docs/vision2030/artificial-intelligence-workplan.pdf)
2. [CCCCO AI initiative overview](https://ai.cccco.edu/)
3. [California Community Colleges AI Consortium](http://cccaic.org/)

## B. ACCJC

4. [ACCJC 2024 Accreditation Standards (June 2025 edition, PDF)](https://accjc.org/wp-content/uploads/ACCJC-2024-Accreditation-Standards.pdf)
5. [ACCJC Adopts 2024 Accreditation Standards](https://accjc.org/announcement/accjc-adopts-2024-accreditation-standards/)
6. [ACCJC Substantive Change Manual, May 2026 Edition (PDF)](https://accjc.org/wp-content/uploads/Substantive-Change-Manual.pdf)
7. [ACCJC Policy on Substantive Change, January 2026 (PDF)](https://accjc.org/wp-content/uploads/Policy-on-Substantive-Change.pdf)
8. [ACCJC Policy on Distance Education and on Correspondence Education, June 2025 (PDF)](https://accjc.org/wp-content/uploads/Policy-on-Distance-and-on-Correspondence-Education.pdf)
9. [ACCJC Eligibility Requirements for Accreditation, January 2024 (PDF)](https://accjc.org/wp-content/uploads/Eligibility-Requirements-for-Accreditation.pdf)

## C. EDD / LMI / BLS / Projections / COE

10. [California OEWS wage data CSV (EDD)](https://data.ca.gov/dataset/6411456b-594b-4b73-af57-ce8dd401f2e2/resource/aef4c53a-7e17-418c-acc1-d189e39b6caa/download/oews-2009-2025_original.csv)
11. [California Long-Term Occupational Employment Projections 2024-2034 (EDD CSV)](https://data.ca.gov/dataset/715d1324-ac02-4b11-b922-86bafa6eb80f/resource/274e273c-d18c-4d84-b8df-49b4d13c14ce/download/lt-occ-emp-2024-2034.csv)
12. [2025 California Jobs Market Report (EDD, DE 864 Rev. 3 8-25)](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/2025_california_jobs_market_report.pdf)
13. [EDD Employment Projections page](https://labormarketinfo.edd.ca.gov/data/employment-projections.html)
14. [EDD OEWS Employment and Wage Statistics page](https://labormarketinfo.edd.ca.gov/data/oes-employment-and-wages.html)
15. [Employment Projections - Labor Market Information - CA.gov](https://labormarketinfo.edd.ca.gov/data/employment-projections.html)
16. [EDD Labor Market Information Division - Home Page](https://labormarketinfo.edd.ca.gov/)
17. [Centers of Excellence for Labor Market Research -- Collections](https://coeccc.net/collections/)

## D. Industry Tools & Techniques

18. [Lightcast: The Generative AI Job Market: 2025 Data Insights](https://lightcast.io/resources/blog/the-generative-ai-job-market-2025-data-insights)
19. [Lightcast: Beyond the Buzz -- AI Skills Command 28% Salary Premium](https://lightcast.io/resources/blog/beyond-the-buzz-press-release-2025-07-23)
20. [The best AI agent frameworks (LangChain)](https://www.langchain.com/resources/ai-agent-frameworks)
21. [Best AI Agent Frameworks 2025: LangGraph, CrewAI, OpenAI, LlamaIndex, AutoGen (Maxim AI)](https://www.getmaxim.ai/articles/top-5-ai-agent-frameworks-in-2025-a-practical-guide-for-ai-builders/)
22. [Best Multi-Agent Frameworks 2026: LangGraph, CrewAI, OpenAI SDK](https://uvik.net/blog/agentic-ai-frameworks/)
23. [Donating the Model Context Protocol and establishing the Agentic AI Foundation (Anthropic)](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)
24. [Linux Foundation Announces the Formation of the Agentic AI Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation)
25. [Best LLM Observability Tools (Firecrawl)](https://www.firecrawl.dev/blog/best-llm-observability-tools)
26. [Top 5 LLM and Agent Observability Tools (MLflow)](https://mlflow.org/top-5-agent-observability-tools/)
27. [Best AI Agent Observability Tools 2026 (Latitude)](https://latitude.so/blog/best-ai-agent-observability-tools-2026-comparison)
28. [Comparing the Top 6 Inference Runtimes for LLM Serving in 2025 (MarkTechPost)](https://www.marktechpost.com/2025/11/07/comparing-the-top-6-inference-runtimes-for-llm-serving-in-2025/)
29. [vLLM vs TensorRT-LLM vs HF TGI vs LMDeploy — Technical Comparison (MarkTechPost)](https://www.marktechpost.com/2025/11/19/vllm-vs-tensorrt-llm-vs-hf-tgi-vs-lmdeploy-a-deep-technical-comparison-for-production-llm-inference/)
30. [Introducing NVIDIA Dynamo, a Low-Latency Distributed Inference Framework (NVIDIA)](https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/)
31. [Kubernetes GPU Scheduling: DRA, KAI, MIG (TechPlained)](https://www.techplained.com/kubernetes-gpu-scheduling)
32. [Running Large-Scale GPU Workloads on Kubernetes with Slurm (NVIDIA)](https://developer.nvidia.com/blog/running-large-scale-gpu-workloads-on-kubernetes-with-slurm/)
33. [SkyPilot (GitHub)](https://github.com/skypilot-org/skypilot)
34. [LLM Fine-Tuning Guide: LoRA, QLoRA, DPO, GRPO, RLHF (Future AGI)](https://futureagi.com/blog/llm-fine-tuning-guide-2025/)
35. [The ML Practitioner's Guide to Fine-Tuning Language Models (MachineLearningMastery)](https://machinelearningmastery.com/the-machine-learning-practitioners-guide-to-fine-tuning-language-models/)
36. [Quantization Techniques for AI Inference 2026: GGUF, AWQ, GPTQ, FP8 (Sesame Disk)](https://sesamedisk.com/quantization-techniques-ai-inference-2026/)
37. [LLM Quantization: GPTQ, AWQ, and GGUF for Efficient Deployment (Calmops)](https://calmops.com/algorithms/llm-quantization-gptq-awq-gguf/)
38. [RAG in Production 2026: GraphRAG, Hybrid Retrieval, and Evals](https://ailearningguides.com/rag-production-patterns-2026/)
39. [Top 5 Reranking Models to Improve RAG Results (MachineLearningMastery)](https://machinelearningmastery.com/top-5-reranking-models-to-improve-rag-results/)
40. [RAG Techniques Compared: Best Practices Guide (Starmorph)](https://blog.starmorph.com/blog/rag-techniques-compared-best-practices-guide)
41. [OWASP Top 10 for LLM Applications 2025 (official)](https://genai.owasp.org/llm-top-10/)
42. [LLM Guardrails: Production Safety Layers Reference 2026 (Digital Applied)](https://www.digitalapplied.com/blog/llm-guardrails-production-safety-layers-reference-2026)
43. [LLM Guardrails: Best Practices (Datadog)](https://www.datadoghq.com/blog/llm-guardrails-best-practices/)
44. [EU AI Act Implementation Timeline (official EU AI Act portal)](https://artificialintelligenceact.eu/implementation-timeline/)
45. [EU AI Act vs NIST AI RMF vs ISO/IEC 42001: A Plain English Comparison (EC-Council)](https://www.eccouncil.org/cybersecurity-exchange/responsible-ai-governance/eu-ai-act-nist-ai-rmf-and-iso-iec-42001-a-plain-english-comparison/)
46. [ISO/IEC 42001 and EU AI Act: A Practical Pairing (ISACA)](https://www.isaca.org/resources/news-and-trends/industry-news/2025/isoiec-42001-and-eu-ai-act-a-practical-pairing-for-ai-governance)
47. [Best Vector Databases 2026: A Complete Comparison Guide (Firecrawl)](https://www.firecrawl.dev/blog/best-vector-databases)
48. [pgvector vs Pinecone vs Qdrant vs Weaviate (2026): Which We Use in Production (Kalvium)](https://www.kalviumlabs.ai/blog/vector-databases-compared-pgvector-pinecone-qdrant-weaviate/)
49. [AI Inference Cost Economics in 2026: GPU FinOps Playbook (Spheron)](https://www.spheron.network/blog/ai-inference-cost-economics-2026/)
50. [FinOps for AI: Governing the Unique Economics of Intelligent Workloads (Flexera)](https://www.flexera.com/blog/finops/finops-for-ai-governing-the-unique-economics-of-intelligent-workloads/)

## E. Peer Programs & Job Market

51. [De Anza College Launches Silicon Valley's First Associate Degree in Applied Artificial Intelligence](https://www.deanza.edu/news/2026/applied-artificial-intelligence-degree-fall-2026.html)
52. [Silicon Valley to get its first two-year degree focused on AI – The Press Democrat](https://www.pressdemocrat.com/2026/05/22/silicon-valley-to-get-its-first-two-year-degree-focused-on-ai/)
53. [De Anza College Launches Associate Degree in Applied AI](https://www.govtech.com/education/higher-ed/de-anza-college-launches-associate-degree-in-applied-ai)
54. [Applied Artificial Intelligence Associate in Science and Certificate of Achievement | Grossmont-Cuyamaca CCD Catalog](https://catalog.gcccd.edu/grossmont/associate-degree-programs-certificates/stem/artificial-intelligence-as-cert-achievement/)
55. [Grossmont College launches first of its kind, Applied Artificial Intelligence Associate Science degree](https://www.gcccd.edu/news/articles/2025/2025-11-06-applied-ai-at-grossmont.php)
56. [Artificial Intelligence - Academic Catalog - Foothill College](https://catalog.foothill.edu/degrees-certificates/artificial-intelligence/)
57. [AI for Cybersecurity, Associate of Science Degree < Coastline College](https://catalog.cccd.edu/coastline/pathways/computer-cyber-sciences/cybersecurity/ai-cybersecurity-as/)
58. [Press Release: Coastline College's AI for Cybersecurity Program Earns NSA Validation Through 2030](https://blog.coastline.edu/2025/09/nsa-validates-cyber-ai-program.html)
59. [Chaffey College to Launch Four New Computer Technology Programs](https://www.prnewswire.com/news-releases/chaffey-college-to-launch-four-new-computer-technology-programs-302745244.html)
60. [BC Offering Free Media Literacy Certificate Program](https://www.kccd.edu/news/2024/0814-bc-offering-free-media-literacy-certificate-program.html)
61. [Associate in Science in Artificial Intelligence - Academic Map | MiraCosta](https://surf.miracosta.edu/psc/ps/EMPLOYEE/SA/c/MCC_CUSTOM.MZ_ACAD_MAP_SS.GBL?MAP_ID=1216)
62. [Artificial Intelligence and Machine Learning Suite | MiraCosta College in partnership with ed2go](https://www.ed2go.com/miracosta/online-courses/artificial-intelligence-machine-learning-suite/)
63. [Introduction to Artificial Intelligence | Saddleback College](https://www.ed2go.com/saddleback/online-courses/introduction-to-artificial-intelligence/)
64. [AI - Bay Area Community College Consortium](https://baccc.net/ai/)
65. [AIDA - Bay Area Community College Consortium](https://baccc.net/aida/)
66. [AI Infrastructure Engineer, Model Serving Platform | Scale AI](https://www.linkedin.com/jobs/view/ai-infrastructure-engineer-model-serving-platform-at-scale-ai-4196120822)
67. [AI Infrastructure Engineer at Hashlist (San Francisco, CA)](https://www.linkedin.com/jobs/view/ai-infrastructure-engineer-at-hashlist-4422814745)
68. [State of the Tech Workforce 2026 | CompTIA Research](https://www.comptia.org/en-us/resources/research/state-of-the-tech-workforce-2026/)
69. [Key employment metrics, market insights and the impact of AI revealed in CompTIA State of Tech Workforce 2026 report](https://www.comptia.org/en-us/about-us/news/press-releases/key-employment-metrics-market-insights-and-the-impact-of-ai-revealed-in-comptia-state-of-tech-workforce-2026-report/)
70. [LinkedIn Jobs on the Rise 2026: The 25 fastest-growing roles in the U.S.](https://www.linkedin.com/pulse/linkedin-jobs-rise-2026-25-fastest-growing-roles-us-linkedin-news-dlb1c)
71. [AWS Certified Machine Learning Engineer – Associate](https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/)
72. [Professional ML Engineer Certification | Google Cloud](https://cloud.google.com/learn/certification/machine-learning-engineer)
73. [Databricks Certified Machine Learning Associate](https://www.databricks.com/learn/certification/machine-learning-associate)
