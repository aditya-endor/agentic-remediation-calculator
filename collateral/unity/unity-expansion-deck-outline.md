# Unity 2027 AppSec Consolidation — Deck Outline

**Deal:** Unity expansion (Cycode displacement + GHAS-secrets head-off) | **AE:** Steve Selby | **Owner:** Aditya Patil (PMM)
**Status:** Working outline v1 — for iteration, then rendering via the `endor-decks` skill
**Last updated:** Sep 3, 2026

---

## How to use this outline

- **Audience: dual-use.** Written so it works both ways: the champion (Chris/Andie) presenting the 2027 business case internally to finance and the VP of Engineering, or Endor Labs presenting to Unity stakeholders (including the new CISO, who has zero account history). Voice is neutral third-person: "Unity's 2027 AppSec decision," never "we at Unity," never hard sales voice. Competitive content is framed as evaluation facts, safe as a leave-behind.
- **Each slide block** gives: the `[archetype]` (matches the endor-decks catalog, so this pipes straight into `build_deck.py`), proposed headline copy, the one idea, body content, evidence with source, and the speaker-note angle.
- **Every number** traces to the claims registry, the deal record, or Unity's own supplied figures. Anything else is in the **Verify before use** table at the bottom. Nothing ships until its row is cleared.
- **Sensitivity:** incident details (7,500 repos, TruffleHog comparison) are Unity-confidential. This deck is for Unity-internal audiences only, in either presenting mode. Do not reuse outside this account.

## The narrative arc (three structural bets)

1. **The spine is Unity's own five success metrics, run as a scorecard.** Slides 5 through 11 walk one metric per slide and score each option. Criteria first, evidence second, so the deck is legible to the new CISO and lands Steve's directive: map clearly to the success metrics.
2. **Secrets gets a two-slide deep-dive** (detection, then blocking). It is metric #5, the emotional core of the incident, and the entire reason GHAS is in the room.
3. **The deck closes on "the $250K question."** A dedicated AI SAST slide (Code Pro is 2,000 of the 3,000 seats and the capability neither incumbent has) followed by the explicit economics slide. The deck never dodges the premium; it prices it at under $10 per developer per month and shows it is the only option that meets all five criteria.

Story in one sentence: *Unity already wrote the definition of success; only one option on the table meets it, it is already proven on Unity's hardest codebase, and the premium over the fragmented alternative is single-digit dollars per developer per month.*

---

## The scorecard (reference table, used on slides 5–11)

Unity's five success metrics, in Unity's own priority order, scored against the two options actually on the table: consolidate on Endor Labs, or renew Cycode and add GHAS Secret Protection.

| # | Unity's success metric | Endor Labs | Cycode (renew) | GHAS (secrets add-on) |
|---|---|---|---|---|
| 1 | Engineer experience is the #1 metric | ✅ Proven on Engine: 10–30 min scans, PR comments, 92% average false positive reduction | ❌ Unity's words: "disruptive and annoying"; search so slow it "never gets used" | ✅ Push protection is genuinely near-invisible (acknowledge honestly) |
| 2 | Security team keeps visibility and oversight | ✅ One policy engine, central exceptions, full audit trail, security stays in the loop | ⚠️ Dashboards exist but severity is "wonky," fails silently, floods engineers | ❌ The known GHAS trade: AppSec is out of the loop; no cross-tool policy, no centralized exceptions |
| 3 | Risk-based filtering and thresholds, natively | ✅ "Fix these, see the rest" via reachability + policy gates; no custom layer needed | ❌ Unity had to build its own CVSS re-scoring → Jira layer to survive the noise | ❌ No risk thresholds; Dependabot has no reachability |
| 4 | Tool consolidation | ✅ One platform: SCA (incl. manifest-less C/C++/C#), AI SAST, secrets; retires Cycode, GHAS proposal, Black Duck, Coverity, and the homegrown filter | ❌ Can never cover the Engine (no manifest-less C/C++/C# SCA), so Unity runs two stacks forever | ❌ Covers one slice (secrets); adds a vendor rather than removing one |
| 5 | Hard secrets blocking | ✅ Pre-commit blocking, plus validation (live vs. revoked) and full-history coverage | ❌ Missed the secrets in the 7,500-repo incident; open-source TruffleHog outperformed it | ✅ Push protection blocks at push (best-in-class at that point) but no validation, no oversight |

Bottom line the deck keeps returning to: **Endor Labs 5/5. Cycode 0/5 by Unity's own experience. GHAS 1.5/5, and the 1.5 comes at the cost of metric 2.**

---

# Main deck (16 slides)

### Slide 1 — Title `[title]`

- **Headline:** One AppSec Platform for Unity
- **Subhead:** The 2027 consolidation decision
- **The one idea:** This is a decision deck, not a vendor pitch. Date it, name the decision window (budget finalized November, Cycode renewal December).
- **Design note:** Endor Labs dark design; no logo soup.

### Slide 2 — Executive summary `[statement]` or `[bullets]`

- **Headline:** Consolidate AppSec on Endor Labs in 2027
- **The one idea:** Recommendation and ask up front, for the finance skimmer who reads two slides.
- **Body (the ask + three numbers):**
  - Recommendation: replace Cycode and the proposed GHAS secrets purchase with the Endor Labs platform: SCA, AI SAST (Code Pro), and secrets, for 2,000 Code Pro + 1,000 additional SCA seats.
  - Number 1: **one platform retires five line items** (Cycode, the GHAS proposal, Black Duck, Coverity, and the internal CVSS-to-Jira filter Unity maintains).
  - Number 2: **92% average false positive reduction**, the noise floor that made Cycode unusable is the headline fix. *(registry-approved)*
  - Number 3: the premium over the fragmented stack is **under $10 per developer per month** (see slide 14 math).
  - The ask: approve the 2027 consolidation budget ($950K–$1.05M/yr, 3-year term) ahead of the December Cycode renewal.
- **Speaker notes angle:** If the room only remembers one thing: Unity defined five success metrics for its 2027 stack; this is the only option that meets all five, and it is already running on the Engine.

### Slide 3 — Where Unity is today `[split]` or `[comparison]`

- **Headline:** Five tools, one problem, and a filter Unity had to build itself
- **The one idea:** The current stack is fragments of one problem (Sep 2 brief framing), and it is costing more than the invoices show.
- **Body (stack map):**
  - Cycode: $472K, all engineers. Flagship search unused due to latency; findings flood forced Unity to build its own CVSS re-scoring layer into Jira.
  - GHAS Secret Protection: ~$250K proposed, secrets only. Solves one slice, adds a vendor.
  - Endor Labs: OSS Core on the Engine monorepo, 1,000 devs, status "Adopt — green." The one tool Unity's engineers actually run in PRs today.
  - Still on the books: Black Duck (SBOM) and Coverity (SAST) maintained by the Engine team.
  - Homegrown: the CVSS-to-Jira noise filter, internal engineering time spent compensating for tooling.
- **Evidence/source:** Deal record + Unity-supplied figures (Sep 1 review).
- **Speaker notes angle:** Every box on this slide except one exists because another box doesn't work. The question isn't "which scanner," it's "how many layers of compensation is Unity willing to keep funding?"

### Slide 4 — Why now `[pillars]`

- **Headline:** Three clocks are running
- **The one idea:** 2027 is not an arbitrary refresh; three forcing functions converge in the next 90 days.
- **Body (three pillars):**
  1. **The incident set the bar.** The Engine compromise began with a malicious package; ~7,500 repos were exfiltrated with secrets in code that the incumbent scanner never flagged. The 2027 stack must be judged against that event, not against a demo.
  2. **The renewal window.** Cycode renews ~December 2026; budgets finalize in November; Andie presents the 2027 ask September 8. Deciding late means renewing by default.
  3. **The engineering mandate.** Security now reports into engineering. Tooling that engineers refuse to use is a failed control, and agentic development (Copilot, Cursor, AI-written code) is multiplying code volume faster than legacy scanners can triage.
- **Evidence/source:** Deal record; incident details from Sep 2 exec brief (Unity-confidential).
- **Speaker notes angle:** For the new CISO: this slide is the whole history lesson. Incident → distrust of incumbent → engineering-led rebuild → this decision.

### Slide 5 — The scorecard `[comparison]`

- **Headline:** Unity already defined success. Score the options against it.
- **The one idea:** The thesis slide. The five metrics are Unity's own (this is how Andie will measure it); the scorecard shows only one option meets all five.
- **Body:** The scorecard table above, rendered as the summary view (✅/⚠️/❌ only; detail comes one metric per slide next).
- **Speaker notes angle:** These criteria weren't written by a vendor. They came out of Unity's own incident review and engineering priorities. The next six slides walk them one at a time.
- **Design note:** This table is the deck's anchor visual; repeat a mini version as a progress marker on slides 6–11.

### Slide 6 — Metric 1: Engineer experience `[split]`

- **Headline:** Security that lives where engineers already work
- **The one idea:** The #1 metric is already proven at Unity, in production, on the hardest codebase they own.
- **Body:**
  - Endor Labs runs inside the PR and CI loop on the Engine monorepo today: scans in 10–30 minutes on a 25GB, 20-year-old codebase; PR comments rolled out; interactive in-PR triage on the near-term roadmap (CR-391).
  - 92% average false positive reduction; customers report 91 to 99% of findings eliminated as noise. *(registry-approved)*
  - Rollout philosophy matches Unity's own bar: "noisy findings are worse than under-reporting."
  - Honest contrast: Cycode is "disruptive and annoying" in Unity engineers' words, with an ASPM too slow to use. GHAS genuinely is low-friction for the secrets slice; that credit is real, and it's addressed on slides 7 and 11.
- **Evidence/source:** Engine deployment status (CSE record, Jun–Aug 2026); registry claims; Unity's own Cycode feedback (Sep 2025 discovery + Jul 2026 notes).
- **Speaker notes angle:** For Andie's audience: the risk of any new tool is developer revolt. That risk is already retired here; Unity engineers have been living with Endor Labs PR scans since June.

### Slide 7 — Metric 2: Security stays in the loop `[split]`

- **Headline:** Invisible to engineers should not mean invisible to security
- **The one idea:** The GHAS counterweight slide (Chris's metric, the new CISO's first question): frictionless-for-devs is only acceptable if AppSec keeps policy, exceptions, and evidence.
- **Body:**
  - The GHAS trade-off, stated plainly: push protection is near-invisible to engineers, and it takes AppSec out of the loop. No cross-tool policy, no risk thresholds, no centralized exception handling, no unified view of how findings are handled.
  - Endor Labs gives both halves: engineers see findings only in their PR; security gets one policy engine, central exception workflows, and a complete audit trail across SCA, SAST, and secrets.
  - Policy is code (customizable, auditable rules), so "how is this finding handled" always has an answer an auditor and a board can see.
- **Evidence/source:** GHAS competitive brief (Jul 2026): oversight gap is the documented category limitation; platform policy engine from FY27 messaging.
- **Speaker notes angle:** This metric exists because Chris insisted on it, and it's the one GHAS structurally cannot meet. Frame it as governance, not turf: after the incident, "we don't know how findings were handled" is not an acceptable answer to the board.

### Slide 8 — Metric 3: Risk-based control, natively `[split]`

- **Headline:** Fix these. See the rest. No custom layer required.
- **The one idea:** Unity's homegrown CVSS re-scoring layer is the strongest evidence in this deck: Unity already paid engineers to build what the platform should have done natively.
- **Body:**
  - Function-level reachability separates "a CVE exists in a dependency" from "the vulnerable function is actually callable in Unity's code," with a verifiable call path as evidence.
  - Policy gates fire only on reachable, high-confidence findings; thresholds are configurable per team, per severity, per risk factor. "Fix these, see the rest" is the product's native grammar.
  - Retires the internal CVSS-to-Jira filter: no more maintaining a compensating layer, no more arguing about "wonky" severity.
  - Function-level CVE annotations across the vulnerability database power this (19,118 CVEs annotated at function level as cited in the Sep 2 brief — *verify before external use*).
- **Evidence/source:** SCA reachability messaging (FY27 message house); Unity's own filter-layer history (deal record).
- **Speaker notes angle:** Ask the room: what does Unity currently spend maintaining the internal filter, and who owns it when its author leaves? That cost never appears on a renewal quote.

### Slide 9 — Metric 4: Tool consolidation `[comparison]`

- **Headline:** Endor Labs is already mandatory for the Engine. Every second tool is duplicate spend.
- **The one idea:** The consolidation logic is asymmetric: Cycode can never cover the Engine (no manifest-less C/C++/C# SCA), but Endor Labs can cover everything Cycode does.
- **Body (table: capability → today → 2027 consolidated):**
  - SCA incl. C/C++/C# without manifests → today: Endor Labs (Engine only) + Cycode (rest, no C/C++) + Black Duck (SBOM leftover) → 2027: Endor Labs, company-wide.
  - SAST → today: Cycode (acquired Bearer engine) + Coverity (Engine leftover) → 2027: Endor Labs AI SAST (Code Pro).
  - Secrets → today: Cycode (failed in the incident) + GHAS proposal → 2027: Endor Labs.
  - Policy/triage → today: homegrown CVSS filter + per-tool configs → 2027: one policy engine.
  - Roadmap upside, clearly marked not in this quote: Package Firewall (blocks malicious packages at install time, the incident's entry vector, integrates with Artifactory or direct) and AI agent governance for the Copilot/Cursor wave. One platform to grow into, no new vendor per problem.
- **Evidence/source:** Cycode competitive brief (SCA language table: no C/C++, no monorepo support); deal record; PFW/agent-governance messaging (FY27).
- **Speaker notes angle:** One vendor, one policy engine, one number for finance. And the number covers the codebase that generates Unity's revenue, which the $722K alternative never touches.

### Slide 10 — Metric 5, part A: Secrets detection at the incident standard `[split]` + `[stats]`

- **Headline:** The incident question: which secrets in 20,000 repos are live right now?
- **The one idea:** Detection quality is measured against the actual incident, not a feature list. Unity's shape (20K repos, 17+ acquisitions, decades of history) is exactly what full-history scanning with validation is for.
- **Body:**
  - Full Git history scanning: every branch, every commit, across every repo — not just default branches where leaks rarely live.
  - **Validation** is the differentiator: each finding is checked against the underlying service and marked Valid, Invalid, or Unvalidated. Triage only what is actually live. No other option on the table does this.
  - Deduplication: the same secret in 50 files is one finding with every location attached, not 50 tickets.
  - Custom rules for Unity-specific token formats on top of out-of-the-box coverage (AWS, GitHub, GitLab, and more).
  - The stakes, stated once: a leaked secret averages **$1.2M in damage** *(FY27 messaging, approved)*; in Unity's incident, secrets across ~7,500 exfiltrated repos went undetected by the incumbent, and open-source TruffleHog outperformed it.
- **Evidence/source:** Secrets Detection message house (FY27); incident facts from Sep 2 brief (Unity-confidential).
- **Speaker notes angle:** Don't relitigate the incident; use its question. "Do we know which secrets in our history are live?" is answerable with validation and unanswerable with pattern matching. That is the difference between an alert pile and an IR asset.

### Slide 11 — Metric 5, part B: Hard blocking without losing oversight `[split]`

- **Headline:** Block secrets before they exist in history, and keep AppSec in the loop
- **The one idea:** The GHAS head-to-head on Unity's terms. GHAS answers "stop the next push." The incident asks "which secrets already in 20,000 repos are live, and who is watching?" Unity needs both; only one option provides both.
- **Body (two columns):**
  - **Blocking (the GHAS draw, matched):** pre-commit hooks stop a secret before it ever enters Git history anywhere (earlier than push protection, which fires after the secret is already committed locally); PR and CI gates as the backstop; the same hooks cover AI coding agents writing code at machine speed.
  - **What blocking alone doesn't give (the Endor Labs case):** validation (live vs. revoked, so response is triage, not archaeology), full-history coverage of the M&A backlog, deduplication, and security-owned policy, exceptions, and audit trail (metric 2).
  - Give GHAS its due, on the slide: push protection is excellent at the push boundary. The gap is everything before and after that boundary, and the oversight cost is metric 2.
- **Evidence/source:** Secrets Detection message house; GHAS brief (acknowledge-then-differentiate is the sanctioned play; GHAS secrets strength is real).
- **Speaker notes angle:** If asked "why not GHAS just for secrets": it's ~$250K for one slice, it adds a vendor instead of removing one (metric 4), and it moves secrets governance outside AppSec (metric 2). The workflow engineers love is matched; the incident-grade detection and oversight are not available there at any price.
- **⚠️ Before this slide ships:** SE validation (Matthew/Shruti) on exact blocking mechanics and rollout at Unity scale: hook distribution via MDM/endorctl on ~3,000 workstations, GHES-behind-VPN specifics, and agent-hook coverage. Do not present enforcement mechanics beyond what SEs confirm.

### Slide 12 — Proof at Unity scale `[stats]` + `[quote]`

- **Headline:** Not a proposal. A production system on Unity's hardest codebase.
- **The one idea:** De-risk the decision: the vendor already cleared Unity's highest bar (the Engine) and delivered its roadmap promises.
- **Body (stat row + receipts):**
  - Only vendor with C/C++ and C# SCA without manifests — the gap that disqualified every other scanner from the Engine.
  - C# segment matching: promised on the land-deal roadmap (April target), shipped April. Roadmap credibility, on the record.
  - Evaluation results: 10–20% better findings than Black Duck (Unity's own Oct 2025 assessment); 89.5% dependency resolution and 93.3% reachability on the test repo; scan times cut from 10h to 2h to 10–30 min.
  - Unity's assessment, Oct 2025: "Endor can best meet their requirements for shifting left and doing dependency scans on the engine code base of C, C++, and C#." *(champion sign-off before use in slides)*
  - Peer scale proof *(all registry-approved, public case studies)*: Zebra Technologies 97% reduction in non-actionable alerts and 60% less remediation effort; Five9 ~50,000 findings down to 30–40 (96.5%) with one security engineer supporting 250+ developers; Egnyte 70% MTTR reduction.
- **Speaker notes angle:** The 2025 objection was "can they handle the Engine?" That question is closed. The 2026 question is only "why keep paying for tools that can't?"

### Slide 13 — AI SAST: the capability neither incumbent has `[stats]` + `[split]`

- **Headline:** SAST that reasons about code, benchmarked, not promised
- **The one idea:** Opens the $250K-question block. Code Pro is 2,000 of the 3,000 seats — most of what Unity is actually buying — and it is a generational upgrade neither Cycode nor GHAS matches.
- **Body:**
  - What it is: multiple specialized AI agents (detection, triage, remediation) tracing user-controlled data source-to-sink across files, classifying every finding true/false/unknown, and proposing a context-aware fix. Built on a semantic code graph, not codebase-dumped-into-an-LLM, which is what keeps it viable at Unity scale.
  - **Vs. CodeQL (GHAS):** head-to-head, Endor Labs AI SAST found **3.6× more true positives, with 2.8× more CWE coverage and 2.7× more file coverage**. *(approved, PMM brief)*
  - **Vs. Cycode:** SAST engine acquired (Bearer, 2024), strongest in Java, ~10 languages, closed rules. Endor Labs: 41 languages with auditable, configurable rules, plus the AI layer.
  - **GA benchmark (June 2026, hand-verified ground truth):** 192 real vulnerabilities across 8 projects; ~3× the frontier models; **63 findings no other tool caught**; 4× more high-severity findings than the best traditional tool; found a zero-day (CVE-2026-55407) in a Rust library, a source-to-sink flaw with no pattern to grep for.
  - Catches the OWASP classes rule-based SAST can't express: broken access control, business logic, insecure design.
  - Why it matters now at Unity: Copilot and Cursor are already in use, and AI-written code multiplies change volume; SAST has to reason at that pace. Also retires Coverity on the Engine.
- **Evidence/source:** AI SAST message house + GA benchmark (FY27, approved); GHAS brief; Cycode brief.
- **Speaker notes angle:** This is the slide for "what does the premium buy that we don't have today?" Answer: the only benchmarked AI-native SAST in the evaluation, replacing two SAST tools (Cycode's and Coverity) with one that finds what both miss.

### Slide 14 — The $250K question `[comparison]` + `[big_stat]`

- **Headline:** $250K more than the fragments. Under $10 per developer per month.
- **The one idea:** Meet the objection head-on. The real comparison is not Endor Labs vs. $722K; it's Endor Labs vs. $722K plus the hidden tax plus the risk those fragments already missed once.
- **Body (two-column value stack):**
  - **The fragmented stack (~$722K/yr):** Cycode renewal $472K + GHAS Secret Protection ~$250K *(Unity-supplied figures, Sep 1)*. Plus the invisible line items: engineering time on the homegrown CVSS filter; Black Duck + Coverity maintenance on the Engine; triage hours at Cycode noise levels; a secrets incident already realized, against a $1.2M-per-leak average. And it still runs two stacks, because none of it covers the Engine.
  - **The consolidated platform ($950K–$1.05M/yr, 3-yr term)** *(Endor Labs range, Sep 1)*: everything the fragments do, on one policy engine, plus what no combination of them offers at any price: benchmarked AI SAST, function-level reachability (mandatory for the Engine anyway), validated secrets with full-history coverage and AppSec oversight.
  - **The delta, normalized:** ~$228–328K/yr across 3,000 covered engineers ≈ **$6–9 per developer per month**. *(compute final figure from the closing quote)*
  - **Cost per success metric met:** the fragmented stack funds 1.5 of Unity's 5 metrics; the platform funds 5 of 5.
- **Speaker notes angle:** Finance framing: this is not a bigger security budget, it's the same problem bought once instead of five times, at a premium of one coffee per developer per month, judged against a $1.2M-average incident class Unity has already experienced.
- **Design note:** big_stat treatment on the per-dev/month figure; the value stack as the comparison visual.

### Slide 15 — Rollout and timeline `[timeline]`

- **Headline:** De-risked by design: the hardest codebase is already done
- **The one idea:** This is an expansion of a working deployment, not a migration gamble; the path lands before the Cycode renewal lapses.
- **Body (timeline):**
  - **Sep 8:** 2027 ask presented to finance (Andie).
  - **Oct–Nov 2026:** contract (Azure Marketplace path available; 3-year term basis for pricing).
  - **Dec 2026:** secrets baseline: full-history audit across the repo estate begins; validated findings triaged by liveness. *(operational sequencing to be confirmed with CSE)*
  - **Jan 2027:** Cycode off. Code Pro (AI SAST) rollout in waves by org, PR-first, same dev-trust gating that worked on the Engine.
  - **H1 2027:** checkpoints reported against the five metrics: false positive rate, PR dwell time, secrets blocked pre-commit, % findings under central policy, tools retired.
- **Speaker notes angle:** The rollout metric set IS the success-metric set: the deck's scorecard becomes the QBR scorecard. That's the accountability story for the new CISO.
- **⚠️ Confirm sequencing and wave plan with Thomas (CSE) before presenting.**

### Slide 16 — The ask `[closing]`

- **Headline:** Approve the 2027 consolidation before the December renewal
- **Body:**
  - Approve: Endor Labs platform, 2,000 Code Pro + 1,000 additional SCA seats, $950K–$1.05M/yr, 3-year term.
  - Note on term: 3-year is the pricing basis; Unity's 2025 two-year exception is the precedent for procurement, and multi-year matches security's stated preference.
  - Do not renew: Cycode ($472K). Do not initiate: GHAS Secret Protection (~$250K).
  - Next steps, named owners: finance presentation (Andie, Sep 8) → contract (Oct–Nov) → Cycode off (Jan 2027).
- **Speaker notes angle:** End on the scorecard: five metrics, one option at 5/5, already proven on the Engine.

---

# Appendix slides

### A1 — Capability and language matrix `[comparison]`

Full side-by-side: Endor Labs vs. Cycode vs. GHAS across SCA (ecosystems + reachability), SAST (languages, rule auditability), secrets (history depth, validation, blocking point, dedup), policy (thresholds, exceptions, audit), and deployment (SCM-agnostic, API-first, CI-based local scanning). Lead rows: **C/C++ and C# SCA without manifests (Endor Labs only — the Engine requirement)**; SCA reachability across transitive dependencies; secrets validation. Source: Cycode brief language tables (Feb 2026 battlecard data; re-verify current), GHAS brief.

### A2 — Alternatives considered `[comparison]`

Mirrors the Sep 2 exec brief's three scenarios, supporting the single recommendation:
1. Endor Labs full suite on Engine only + GHAS company-wide — solves the Engine, keeps two vendors and split visibility.
2. Endor Labs company-wide except secrets + GHAS for secrets — one scanner, but secrets governance sits outside AppSec (fails metric 2).
3. **Endor Labs for everything (recommended)** — one vendor, one policy engine, one number for finance, 5/5 on the scorecard.

### A3 — Objection prep (speaker back-pocket, not presented)

- **"It's $250K more."** → Slide 14. The alternative isn't $722K; it's $722K + the hidden tax + two stacks forever + 1.5/5 metrics. Delta is $6–9/dev/month.
- **"GHAS is nearly free / already in our GitHub bill."** → Unity's own quote is ~$250K for secrets alone. Extending GHAS toward full coverage means GitHub Code Security at ~$30/committer/month list (*verify current pricing*), roughly $720K+/yr at 2,000 committers, and still no reachability, no C/C++ SCA, no cross-tool policy. Partner tone: Endor Labs and GitHub are partners (SCA integrates into GHAS/Dependabot; Agent HQ plugin); Unity keeps GitHub, Unity doesn't need to buy GHAS to keep it.
- **"Cycode will discount at renewal."** → The problems are architectural, not commercial: no manifest-less C/C++/C# (can never cover the Engine), ASPM latency, noise model that forced a homegrown filter, and the incident performance. A discount buys the same gaps for less; Unity still runs Endor Labs for the Engine either way, so a Cycode renewal is the two-stack outcome at any price.
- **"Endor was called '10X Black Duck' at land. Now this."** → The land deal's scrutiny was answered with delivery: C# shipped on the promised date, 10–20% better results, production adoption rated green. The record is the rebuttal.
- **"Why a 3-year term when Unity avoids them?"** → Pricing basis for the range; 2025's two-year exception is precedent that terms flex; security's stated preference is multi-year. Escalate structure questions to Steve/Zack, not the room.
- **"PR blocking isn't even on yet."** → Deliberate: Unity asked that blocking wait until developers can triage findings in-PR (CR-391 in progress). Shipping trust before enforcement is the entire DevEx thesis of this deck; that is the feature.

### A4 — Contractual and compliance facts `[bullets]`

- AI-training opt-out on Unity data: in place since the land deal.
- Local CI-based scanning: how the deployment runs today (and a standing discount condition).
- Azure Marketplace: available procurement path.
- GitHub Enterprise behind VPN: current CI-based model already accommodates it. *(Do not promise GHES-app mechanics at 20K-repo scale; open feature ask.)*

---

# Verify before use

Every number/claim below must be cleared by its owner before the deck renders. Registry-approved and message-house claims are listed for completeness; deal-specific figures need Steve's confirmation.

| Claim | Slide(s) | Source | Status / owner |
|---|---|---|---|
| Cycode $472K; GHAS ~$250K; combined ~$722K | 3, 14, 16 | Unity-supplied (Sep 1 review) | Rep-supplied — confirm with Steve before any external showing |
| Endor Labs $950K–$1.05M/yr, 3-yr, 2,000 Code Pro + 1,000 SCA | 2, 14, 16 | Zack's range (Sep 1) | Internal — confirm current before presenting |
| $6–9 per developer per month delta (across 3,000 seats) | 2, 14 | Computed from the two rows above | Recompute from final quote |
| 92% average false positive reduction | 2, 6 | Claims registry (platform) | Approved |
| 91–99% customer noise-reduction range | 6 | Claims registry (derived) | Approved |
| Zebra 97% / 60%; Five9 96.5%, ~50k→30–40, 250:1; Egnyte 70% MTTR | 12 | Claims registry (public case studies) | Approved — keep exact framings |
| AI SAST vs CodeQL: 3.6× TP / 2.8× CWE / 2.7× file coverage | 5 (implied), 13 | GHAS competitive brief (Jul 2026) | Approved |
| AI SAST GA benchmark: 192 vulns, 63 unique, 4× high-sev, CVE-2026-55407 | 13 | FY27 AI SAST message house | Approved |
| $1.2M average damage per leaked secret | 10, 14 | FY27 Secrets message house | Approved |
| 19,118 CVEs annotated at function level | 8 | Sep 2 exec brief | Verify with PMM/product before reuse |
| 89.5% dependency resolution / 93.3% reachability | 12 | Unity PoV (Oct 2025) | Account-verified; confirm framing with Steve |
| 10–20% better than Black Duck | 12 | Unity's own assessment (Chris, Oct 2025) | Attribute as Unity's evaluation; champion sign-off |
| Chris quote (Oct 2025, "best meet their requirements…") | 12 | Internal call notes | Champion sign-off required |
| Scan times 10–30 min; PR comments live; "Adopt — green" | 3, 6, 12 | CSE record (Jun–Aug 2026) | Confirm current with Thomas |
| Incident: malicious package entry; ~7,500 repos; secrets missed; TruffleHog comparison | 4, 5, 10 | Sep 2 brief | Unity-confidential; champion sign-off for any room with new attendees |
| ~3,500 devs; 20K repos; 17+ acquisitions | 4, 10 | Deal record | Account facts; confirm |
| GHAS list pricing ($19 / $30 per committer/mo) | A3 | GHAS brief | Verify current GitHub pricing before quoting |
| Cycode language/SCA gap tables | 9, A1 | Cycode brief (Feb 2026 battlecard data) | Re-verify currency if challenged |
| Secrets pre-commit blocking mechanics + rollout at Unity scale (MDM/endorctl, GHES-behind-VPN, agent hooks) | 11 | Secrets messaging + deal record | **SE validation required (Matthew/Shruti) before slide 11 ships** |
| Rollout sequencing (Dec baseline scan, Jan waves) | 15 | Proposed | Confirm with Thomas (CSE) |

---

# Open items / next steps

1. Iterate on this outline with Steve (does the scorecard framing match how Chris/Andie talk?) and lock slide-level copy.
2. Clear the Verify-before-use table (owners named per row).
3. Render via the `endor-decks` skill (`build_deck.py`); archetypes are already assigned per slide. Green highlight ring budget (max 2): suggest slide 13 ("3.6×") and slide 14 (per-dev/month figure).
4. Companion piece: the champion still needs the finance two-pager (deal record ask) — derive it from slides 2, 5, 13, 14 via the `deal-one-pagers` skill once this outline is locked.
