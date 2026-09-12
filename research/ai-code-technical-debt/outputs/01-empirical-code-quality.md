# Stream 1 — Empirical evidence on quality, maintainability and churn of AI-generated code

*Research date: 2026-09-12. All sources fetched and read unless marked UNVERIFIED.*

## Stream summary

The empirical record gives **moderate-to-strong support to the "AI code as technical debt" hypothesis on
maintainability and system-level stability, but does not support it on raw developer output**, which has
clearly risen. The two findings are not in conflict; they are the core tension of this stream.

The strongest structural evidence is longitudinal. GitClear's 2026 analysis of 623 million changed lines
(2023–2026) reports that *moved* code — the fingerprint of refactoring — fell from 21% of changed lines in
2022 to 3.8% in 2026, while copy/paste rose from 9.4% to 15.7%, and block duplication rose 81% since 2023
to its highest level on record. It also reports a 35% decline in cross-file method calls and a 74% drop in
maintenance of code older than 12 months. These are correlational, industry-produced metrics, and GitClear
sells a tool that measures them — but the direction is corroborated by independent academic work.

That academic corroboration is now substantial. A 304,362-commit study of verified AI-authored commits
across 6,275 repositories (Liu et al., arXiv 2603.28592) found 15–29% of AI commits introduce a detectable
static-analysis issue, with 24.2% of issues still alive at HEAD and security issues most persistent (41.1%).
CodeRabbit's 470-PR comparison found ~1.7x more issues in AI-co-authored PRs. Peer-reviewed CodeScene work
found AI assistants raise defect risk ≥30% in unhealthy code. DORA 2025 (n≈5,000) found AI adoption now
correlates *positively* with throughput but **still negatively with delivery stability**.

The review-oversight evidence is the most directly on-hypothesis. Duma et al. (EASE 2026) found most
AI-generated PRs receive **no human review at all**, and where review happens it is "largely dominated by AI
agents rather than humans." Faros AI telemetry (22,000 developers) reports 31% more PRs merged with no
review. Mujahid & Imran (TechDebt 2026) found developers' own AI-related TODO comments cluster on
*postponed testing, incomplete adaptation, and limited understanding of AI-generated code* — the hypothesis
stated in developers' own words.

The counter-evidence is real: Cui et al. (n=4,867, Management Science) found +26% tasks completed; GitHub's
own RCT (n=202) found small but significant *quality gains*; and METR retracted the practical force of its
own 19%-slowdown finding in February 2026.

## Evidence table

| # | Claim (one sentence) | Source title | Author/Org | Date | Type | Strength | URL | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | Moved (refactored) code fell from 21% of changed lines in 2022 to 3.8% in 2026 while copy/paste rose 9.4%→15.7%. | The Maintainability Gap: 2026 AI Code Quality Research | GitClear | 2026 | Industry study w/ methodology | Med-High | https://www.gitclear.com/the_ai_code_quality_maintainability_gap | 623M analyzed changes, 2023–2026. Block duplication +81% (40.3→73.0 dup lines per million changed). Cross-file method calls −35% (343→223 per 1k changed lines). Long-term (12mo+) code updates −74% (1.7%→0.46%). Two-week churn +15%. Correlational only. |
| 2 | 2024 was the first year on record where copy/paste exceeded "moved" code. | AI Copilot Code Quality: 2025 Data Suggests 4x Growth in Code Clones | GitClear | Feb 2025 | Industry study | Med | https://www.gitclear.com/ai_assistant_code_quality_2025_research | 211M changed lines, Jan 2020–Dec 2024, from Google/Microsoft/Meta and enterprise repos. Refactoring fell from 25% of changed lines (2021) to <10% (2024); cloned blocks 8.3%→12.3%. |
| 3 | 15–29% of AI-authored commits introduce at least one detectable quality issue, and 24.2% of those issues survive to HEAD. | Debt Behind the AI Boom: A Large-Scale Empirical Study of AI-Generated Code in the Wild | Liu, Widyasari, Zhao, Irsan, Lo | 30 Mar 2026 | Preprint (arXiv) | High | https://arxiv.org/html/2603.28592v1 | 304,362 verified AI-authored commits, 6,275 repos (100+ stars), Python/JS/TS. 484,606 issues: 89.1% code smells, 5.8% runtime bugs, 5.1% security. Survival: security 41.1%, bugs 30.3%, smells 22.7%. Issue rate by tool: Copilot 17.3% → Gemini 28.7%. AI commits fix slightly more smells than they add but introduce ~2x more security issues than they fix. |
| 4 | AI coding assistants increase defect risk by at least 30% when applied to unhealthy code. | Code for Machines, Not Just Humans: Quantifying AI-Friendliness with Code Health Metrics | Borg, Hagatulah, Tornhill, Söderberg (CodeScene / Lund Univ.) | 5 Jan 2026, FORGE 2026 | Peer-reviewed paper | Med-High | https://arxiv.org/abs/2601.02200 | 5,000 Python files; LLM refactoring experiments. Finds "meaningful association" between CodeHealth and semantic preservation after AI refactoring. Vendor-affiliated (CodeScene) but peer-reviewed. Press release: https://www.prnewswire.com/news-releases/ai-coding-assistants-increase-defect-risk-by-30-in-unhealthy-code-new-peer-reviewed-research-finds-302672355.html |
| 5 | Most AI-generated PRs receive no review, and where review occurs it is dominated by AI agents rather than humans. | These Aren't the Reviews You're Looking For: How Humans Review AI-Generated Pull Requests | Duma, Wróblewski, Bobińska, Winiarska, Przymus (Nicolaus Copernicus Univ.) | 5 May 2026, EASE 2026 | Peer-reviewed paper | High | https://arxiv.org/abs/2605.02273 | Uses AIDev dataset, compares AI vs human PRs *within the same repositories*. Human involvement "frequently expressed through agent steering rather than standalone evaluation." Authors warn review metrics can no longer be read as proxies for human oversight. Most directly on-hypothesis source in the stream. |
| 6 | Developers' own AI-related TODO comments cluster on postponed testing, incomplete adaptation, and limited understanding of AI-generated code. | "TODO: Fix the Mess Gemini Created": Towards Understanding GenAI-Induced Self-Admitted Technical Debt | Mujahid & Imran (Missouri S&T) | TechDebt 2026 (Apr 2026) | Peer-reviewed paper | Med-High | https://conf.researchr.org/details/TechDebt-2026/TechDebt-2026-main/2/-TODO-Fix-the-Mess-Gemini-Created-Towards-Understanding-GenAI-Induced-Self-Admitte | 6,540 LLM-referencing comments from public Python/JS repos, Nov 2022–Jul 2025; 81 self-admit technical debt. Proposes "GIST" framing. Shift away from *design* debt toward *requirement and testing* debt. Small n on the SATD subset. Preprint: https://arxiv.org/pdf/2601.07786 |
| 7 | 46.41% of agent-generated fix PRs are rejected. | Understanding the Rejection of Fixes Generated by Agentic Pull Requests — Insights from the AIDev Dataset | Abujadallah, Arabat, Sayagh (ÉTS Montréal) | 11 Jun 2026, MSR '26 | Peer-reviewed paper | High | https://arxiv.org/html/2606.13468 | 3,225 fix PRs from Copilot/Devin/Cursor/Claude; qualitative coding of 306 rejected PRs (Cohen's κ=0.605). Reasons: relevance 23.5% (inactivity alone 17.3%), implementation 9.6%, provider 8.5%, technical 7.2%; 49.3% unclassified. Caveat: much rejection is *abandonment/inactivity*, not defectiveness. |
| 8 | AI agent PR acceptance varies 55–84% by task type, with generative tasks lowest. | Comparing AI Coding Agents: A Task-Stratified Analysis of Pull Request Acceptance | Pinna, Gong, Williams, Sarro (UCL) | 7 May 2026, MSR '26 | Peer-reviewed paper | High | https://arxiv.org/html/2602.08915v2 | 7,156 PRs from AIDev. Chore 84.0%, docs 82.1%, style 78.1%, refactor 71.2%, features 66.1%, fixes 66.0%, tests 61.5%, performance 55.4%. By agent: Codex 77.9%, Cursor 74.5%, Claude Code 71.9%, Copilot 68.0%, Devin 61.6%. 29pp task gap exceeds inter-agent variance. |
| 9 | AI adoption correlates positively with delivery throughput but negatively with delivery stability. | Announcing the 2025 DORA Report / State of AI-assisted Software Development | Google Cloud / DORA | Sep 2025 | Industry survey (rigorous) | High | https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report | ~5,000 technology professionals + 100h qualitative. 90% use AI at work; >80% believe it raised productivity; **30% report little or no trust in AI-generated code**. Throughput relationship flipped positive vs 2024; stability relationship remains negative. "AI as amplifier" framing. |
| 10 | In 2024 a 25% increase in AI adoption was associated with a 7.2% decrease in delivery stability and a 1.5% decrease in throughput, despite a 3.4% code-quality gain. | Accelerate State of DevOps Report 2024 | DORA / Google Cloud | Oct 2024 | Industry survey | Med (figures via secondary) | https://dora.dev/research/2024/dora-report/ | Landing page summary confirms direction ("negatively impacts software delivery stability and throughput"); the exact 3.4%/7.2%/1.5%/7.5% figures are reported by secondary coverage (https://getdx.com/blog/2024-dora-report/) — **numbers UNVERIFIED against the full PDF**. Notable because it separates *micro* quality gain from *system* stability loss. |
| 11 | AI-co-authored PRs contain ~1.7x more issues than human-only PRs. | State of AI vs Human Code Generation Report | CodeRabbit | 17 Dec 2025 | Vendor study w/ methodology | Med | https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report | 470 open-source PRs (320 AI-co-authored, 150 human-only); Poisson rate ratios w/ 95% CIs. 10.83 findings/PR vs 6.45. Logic/correctness +75%, readability ~3x, security up to 2.74x, formatting 2.66x. Vendor sells AI code review — clear commercial interest. Independent coverage: https://www.theregister.com/2025/12/17/ai_code_bugs/ |
| 12 | Under high AI adoption PRs are 51% larger, bugs per PR up 54%, median time in review up 441%, and 31% more PRs merge with no review. | AI Engineering Report 2026 ("Acceleration Whiplash") | Faros AI | 2026 | Vendor telemetry study | Med | https://www.faros.ai/blog/ai-code-quality-senior-engineer-review-burden | 22,000 developers across 4,000 teams, two years of telemetry. Also: files edited/PR +59.7%, tasks completed +210%, time to first review +156.6%, time in progress +225.2%, 25% of PRs now reviewed by AI agents (up from 0% in 2025). Vendor-produced; "high vs low AI adoption" comparison is observational, not randomised. |
| 13 | 88% of developers report at least one negative technical-debt impact from AI; AI now accounts for 42% of committed code. | State of Code: Developer Survey | Sonar | 8 Jan 2026 | Vendor survey | Med | https://www.sonarsource.com/company/press-releases/sonar-data-reveals-critical-verification-gap-in-ai-coding/ | >1,100 developers globally. 96% do not fully trust AI code is functionally correct, but only 48% always check it before committing — the "verification gap." 38% say reviewing AI code takes more effort than reviewing a colleague's. 53% cite "code that looks correct but isn't reliable"; 40% cite unnecessary duplication. AI share projected to hit 65% by 2027. Vendor sells technical-debt tooling. |
| 14 | 66% of developers say AI solutions are "almost right, but not quite," and 45.2% say debugging AI code is more time-consuming. | 2025 Developer Survey — AI section | Stack Overflow | Jul 2025 (fielded 29 May–23 Jun 2025) | Large survey | High | https://survey.stackoverflow.co/2025/ai | 49,009 responses, 166 countries (33,662 answered AI usage items). Only 3.1% highly trust AI accuracy; trust split ~45.7% trust / 45.7% distrust. Positive sentiment fell from >70% (2023–24) to 60%. 20% report reduced confidence in their own problem-solving. Only 31% use AI agents regularly. |
| 15 | Experienced OSS developers were 19% *slower* with AI tools while believing they were 20% faster. | Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity | METR | 10 Jul 2025 | RCT (preprint) | Med (superseded — see #16) | https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ | 16 developers, 246 real issues, repos averaging 22k+ stars and 1M+ LOC; per-issue randomisation. Forecast +24% speedup, post-hoc estimate +20%, actual −19%. Authors explicitly disclaim generalisation. arXiv: https://arxiv.org/abs/2507.09089 |
| 16 | **METR revised its own design and now estimates AI speeds developers up, not down.** | We are Changing our Developer Productivity Experiment Design | METR | 24 Feb 2026 | Research update | High (counter-evidence) | https://metr.org/blog/2026-02-24-uplift-update/ | Late-2025 data: returning developers −18% completion time (CI −38% to +9%); new developers −4% (CI −15% to +9%). Severe selection bias identified: developers refuse to participate without AI, and *strategically withhold tasks where AI would help most* ("I avoid issues like AI can finish things in just 2 hours, but I have to spend 20 hours"). METR says developers are "likely more sped up from AI tools now — in early 2026." Wide CIs crossing zero. |
| 17 | A randomised trial across 4,867 developers found 26.08% more tasks completed with an AI assistant. | The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers | Cui, Demirer, Jaffe, Musolff, Peng, Salz | Jun 2025; *Management Science* 2026 | Peer-reviewed RCT | High (counter-evidence) | https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/ | Microsoft, Accenture, anonymous Fortune 100. SE 10.3%. Junior/recent hires +27–39%, senior +8%. **Crucially, the study measures task completion, not code quality** — no maintainability or defect outcome reported. Two of three sites are Copilot-vendor-adjacent. Also: https://pubsonline.informs.org/doi/10.1287/mnsc.2025.00535 |
| 18 | GitHub's own RCT found Copilot code scored modestly *higher* on readability, reliability, maintainability and conciseness. | Does GitHub Copilot improve code quality? Here's what the data says | GitHub | 22 Nov 2024 | Vendor RCT | Med (counter-evidence) | https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/ | 243 devs with ≥5y Python; 202 valid submissions (104 Copilot / 98 control); 25 blind reviewers, 1,293 reviews. Readability +3.62% (p=0.003), reliability +2.94% (p=0.01), maintainability +2.47% (p=0.041), conciseness +4.16% (p=0.002); 53.2% greater likelihood of passing all 10 unit tests; 5% more likely to be approved. **Single greenfield task (fictional restaurant-review web server), not a large existing codebase** — precisely the setting where duplication/refactoring debt cannot manifest. Vendor's own product research. |
| 19 | A Google enterprise RCT found AI shortened task time by ~21%, with a wide confidence interval. | How much does AI impact development speed? An enterprise-based randomized controlled trial | Paradis, Grey, Madison, Nam, Macvean, Meimand, Zhang, Ferrari-Church, Chandra (Google) | Oct–Nov 2024 | RCT (preprint) | Med (counter-evidence) | https://arxiv.org/abs/2410.12944 | 96 full-time Google engineers, one complex enterprise-grade task, three AI features. Authors state the CI is large and caution against generalising beyond Google's internal tooling in summer 2024. No quality outcome measured. |
| 20 | AI-generated files received ~50% *fewer* commits than human files in their first month, and 5% fewer bug-fix commits. | To What Extent Does Agent-generated Code Require Maintenance? An Empirical Study | Sawada, Shirai, Kashiwa, Yamaguchi, Iwata, Iida (NAIST) | 7 May 2026 | Peer-reviewed paper | High (mixed) | https://arxiv.org/html/2605.06464v1 | 508 AI + 508 human files, 100 repos (100+ stars), ≥6 months observation, 3,238 commits. AI files: features 21.78%, refactoring 14.19%, chore 13.35%, bug fixes 11.73%. Human files: bug fixes 16.76%, docs 16.22%, refactoring 15.10%. **Humans performed 83.21% of maintenance on AI-generated files; agents only 16.79%.** Ambiguous: lower churn could mean higher quality *or* abandonment/neglect. |
| 21 | Generative AI measurably degrades code-expertise and Truck-Factor models used to identify who knows a codebase. | The Impact of Generative AI on Code Expertise Models: An Exploratory Study | Cury & Avelino | 10 Jul 2025 | Preprint (arXiv) | Med | https://arxiv.org/abs/2507.08160 | Simulation-based: injects varying degrees of ChatGPT-generated code into GitHub projects and measures effect on knowledge/Truck-Factor models. "Most scenarios led to measurable impacts." Directly relevant to "code few humans understand" — but simulated, not observational. |
| 22 | Acceptance of a PR is highly predictable from submission-time signals, but review *effort* is not. | Predicting Acceptance and Review Effort in Human and Agent Pull Requests | Pansuriya, Ghorbani, Singh, AlOmar (Stevens Inst.) | 13 Jul 2026 | Preprint (arXiv) | Med | https://arxiv.org/abs/2607.12057 | AIDev dataset; leakage-aware pipeline, five classical ML models across pooled/human-only/agent-only/balanced views. Tree models >0.95 F1 for acceptance; review-effort prediction "substantially more challenging." Implies review cost is the unmodellable residual. |
| 23 | Evidence on AI code quality is genuinely contradictory across 24 primary studies. | Factors Influencing the Quality of AI-Generated Code: A Synthesis of Empirical Evidence | Geruslu, Aliyeva, Tüzün (Bilkent) | 26 Mar 2026 | Systematic literature review | High (caveat) | https://arxiv.org/abs/2603.25146 | Synthesises 24 primary studies. Reports "variability in quality outcomes such as correctness, security, maintainability, and complexity across studies, with both improvements and risks reported." Quality depends on prompt design, task specification and developer expertise — i.e. no single determinant. Best single citation for "the literature does not agree." |
| 24 | 29.5% of Python and 24.2% of JavaScript Copilot-generated snippets in real GitHub projects contained security weaknesses. | Security Weaknesses of Copilot-Generated Code in GitHub Projects: An Empirical Study | Yu et al. | 2023, rev. 2025 | Peer-reviewed paper | Med-High | https://arxiv.org/abs/2310.02059 | 733 snippets analysed; weaknesses span 43 CWE categories, 8 of which are in the 2023 CWE Top-25 (incl. CWE-330, CWE-94, CWE-79). Predates agentic coding; snippet-level not system-level. |
| 25 | Copilot users introduced 41% more bugs with no gain in PR throughput or cycle time. | Gen AI for Coding Research Report | Uplevel Data Labs | Sep 2024 | Vendor telemetry study | Low-Med | https://resources.uplevelteam.com/gen-ai-for-coding | ~800 developers, 3 months pre- vs 3 months post-Copilot access. Landing page confirms "significantly higher bug rate" and flat throughput; **the specific 41% figure is gated behind the full report and is UNVERIFIED against the primary document** (widely reported secondarily, e.g. https://www.cio.com/article/3540579/devs-gaining-little-if-anything-from-ai-coding-assistants.html). Also reported: burnout risk fell 28% without Copilot vs 17% with. |
| 26 | 75% of all new code at Google is AI-generated and approved by engineers, up from 50% in autumn 2025. | Sundar Pichai shares news from Google Cloud Next 2026 | Sundar Pichai / Google | 22 Apr 2026 | Vendor statement (primary) | High (for the claim itself) | https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/ | Exact quote: "Today, 75% of all new code at Google is now AI-generated and approved by engineers, up from 50% last fall." Establishes the *exposure* base rate that makes the debt question material. No quality figures given; "approved by engineers" is unaudited. |

## Detailed findings

### 1. Longitudinal repository evidence: refactoring is collapsing, duplication is rising

The single most-cited body of evidence is GitClear's. Its
[2026 "Maintainability Gap" report](https://www.gitclear.com/the_ai_code_quality_maintainability_gap) analyses
623 million changed lines from 2023–2026 across eight quality signals, and the trend lines are steep:

- **Moved code** (the signature of refactoring/extraction) fell from **21% of changed lines in 2022 to 3.8% in 2026**.
- **Copy/paste** rose from **9.4% (2022) to 15.7% (mid-2026)** — developers are now roughly **5x more likely to
  copy/paste than to refactor**.
- **Block duplication** rose **81% since 2023**, from 40.3 to 73.0 duplicated lines per million changed lines,
  "the highest level on record."
- **Cross-file method calls fell 35%** (343 → 223 per thousand changed lines) — new code increasingly does
  *not* call existing functions, i.e. it is isolated rather than integrated.
- **Long-term maintenance** (updates to code untouched for 12+ months) fell **74%**, 1.7% → 0.46%.
- Error-masking constructs +47%; two-week churn +15%; within-commit copy/paste +41%.

The [2025 edition](https://www.gitclear.com/ai_assistant_code_quality_2025_research) (211M lines, 2020–2024)
established the inflection: refactoring fell from 25% of changed lines in 2021 to under 10% in 2024, cloned
blocks rose 8.3% → 12.3%, and 2024 was the **first year on record in which copy/paste exceeded moved code**.

The cross-file-connectivity and legacy-maintenance declines are the two metrics that speak most directly to
the hypothesis. Code that does not call existing functions and is never revisited after 12 months is, almost
by definition, code that no one is maintaining a mental model of.

**Methodological caveat, stated plainly:** these are *correlational time series over the AI adoption period*,
not attribution. GitClear does not identify which lines an AI wrote. Confounders include the 2022–24 tech
layoffs (loss of senior maintainers), remote-work shifts, and changing repository mix in their sample.
GitClear also sells the diff-analysis product these metrics come from.

### 2. Commit-level attribution: the strongest independent corroboration

[Liu et al., "Debt Behind the AI Boom" (arXiv 2603.28592, March 2026)](https://arxiv.org/html/2603.28592v1)
addresses GitClear's attribution weakness directly. It identifies **304,362 verified AI-authored commits**
across **6,275 GitHub repositories** (≥100 stars, Python/JS/TS) using explicit Git metadata — actor logins,
author emails, commit trailers — then runs Pylint, Bandit, ESLint and njsscan *before and after each commit*
to attribute issues, and tracks whether they survive to HEAD.

- **484,606 distinct issues** introduced: 89.1% code smells, 5.8% runtime bugs, 5.1% security.
- **>15% of commits from every AI assistant** introduce at least one detectable problem; rates range from
  **Copilot 17.3% to Gemini 28.7%**.
- **24.2% of introduced issues are still alive at HEAD.** Security issues persist most (**41.1%**), then
  runtime bugs (30.3%), then smells (22.7%).
- Accumulation is accelerating: **22.20 surviving issues per 100 commits older than 9 months vs 39.92 per 100
  commits under 3 months.**
- Net: AI commits *fix* slightly more code smells (449,984) than they introduce (431,850) — but introduce
  **nearly twice as many security issues as they fix**.

The persistence and acceleration figures are the important ones for the debt thesis: it is not that AI
introduces issues (humans do too), it is that a quarter of them are never removed, and the recent cohort is
worse than the old one.

### 3. Defect risk is conditional on the code AI is dropped into

[Borg, Hagatulah, Tornhill & Söderberg (FORGE 2026, arXiv 2601.02200)](https://arxiv.org/abs/2601.02200) ran
LLM refactoring experiments over 5,000 Python files and found a meaningful association between CodeHealth
and *semantic preservation after AI refactoring*. CodeScene's
[accompanying announcement](https://www.prnewswire.com/news-releases/ai-coding-assistants-increase-defect-risk-by-30-in-unhealthy-code-new-peer-reviewed-research-finds-302672355.html)
puts the headline at **≥30% higher defect risk when AI assistants operate on unhealthy code**.

This is a feedback-loop finding and deserves emphasis: if AI degrades maintainability (§1–2), and degraded
maintainability raises AI's own defect rate, the mechanism is self-reinforcing. It is also the most direct
empirical support for "dependency on the harness" — the codebase becomes one that only tools can navigate,
and the tools get worse at navigating it.

Caveat: CodeScene is a code-health vendor and both senior authors are CodeScene principals, though the paper
is peer-reviewed and the dataset (competitive-programming Python) is synthetic relative to production code.

### 4. Review is thinning exactly where volume is rising — the core oversight finding

This is the most on-hypothesis theme in the stream, and it now has peer-reviewed backing.

[Duma et al., "These Aren't the Reviews You're Looking For" (EASE 2026)](https://arxiv.org/abs/2605.02273)
compares AI-generated and human PRs **within the same repositories** using the AIDev dataset and finds that
**most AI-generated PRs receive no review at all**; where review does occur it is "largely dominated by AI
agents rather than humans," with human involvement "frequently expressed through **agent steering** rather
than standalone evaluation." The authors' own conclusion is that these patterns "raise challenges for
interpreting review metrics as indicators of human oversight." That is a peer-reviewed statement that the
usual proxies for human understanding of code have stopped working.

[Faros AI's 2026 telemetry report](https://www.faros.ai/blog/ai-code-quality-senior-engineer-review-burden)
(22,000 developers, 4,000 teams, two years) quantifies the squeeze comparing high- to low-AI-adoption teams:

| Metric | Change |
|---|---|
| Average PR size | +51.3% |
| Files edited per PR | +59.7% |
| Tasks with code completed | +210% |
| Bugs per PR | +54% |
| Median time to first review | +156.6% |
| Median time in PR review | +441.5% |
| PRs merged with **no review** | +31% |
| PRs reviewed by AI agents | 25% (from 0% in 2025) |

[Sonar's State of Code survey](https://www.sonarsource.com/company/press-releases/sonar-data-reveals-critical-verification-gap-in-ai-coding/)
(>1,100 developers, Jan 2026) names the gap: **96% of developers do not fully trust that AI-generated code is
functionally correct, yet only 48% always check it before committing.** 38% say reviewing AI code takes more
effort than reviewing a human colleague's.

The AIDev acceptance studies give the outcome side. [Pinna et al. (MSR '26)](https://arxiv.org/html/2602.08915v2)
find acceptance ranges **84.0% for chores and 82.1% for documentation down to 66.1% for features, 61.5% for
tests and 55.4% for performance** across 7,156 PRs — a 29-point task gap that exceeds the variance between
agents (Codex 77.9%, Cursor 74.5%, Claude Code 71.9%, Copilot 68.0%, Devin 61.6%).
[Abujadallah et al. (MSR '26)](https://arxiv.org/html/2606.13468) find **46.41% of agent fix PRs are
rejected** out of 3,225 — though their qualitative coding of 306 rejections shows the largest single reason
is **inactivity (17.3%)**, i.e. abandonment rather than demonstrated defect, with genuine implementation
faults accounting for only 9.6%.

### 5. Developers say, in their own commit comments, that they don't understand the code

[Mujahid & Imran (TechDebt 2026)](https://conf.researchr.org/details/TechDebt-2026/TechDebt-2026-main/2/-TODO-Fix-the-Mess-Gemini-Created-Towards-Understanding-GenAI-Induced-Self-Admitte)
analysed **6,540 LLM-referencing code comments** from public Python and JavaScript repositories
(Nov 2022–Jul 2025), of which **81 also self-admit technical debt**. They propose **GIST** (GenAI-Induced
Self-admitted Technical debt) for cases where "developers explicitly express uncertainty about the behavior
or rationale of AI-generated code."

The three dominant categories are **postponed testing, incomplete adaptation, and limited understanding of
AI-generated code** — and the study finds a compositional shift: **design debt appears less often, while
requirement and testing debt appear more often**, reflecting deferred completion and validation. This is the
hypothesis restated by developers about their own work. The SATD subset (n=81) is small, which limits
generalisation, but the direction matches §4.

Complementing this, [Cury & Avelino (arXiv 2507.08160)](https://arxiv.org/abs/2507.08160) show that injecting
GenAI-authored code into projects **measurably degrades code-expertise and Truck-Factor models** — the
standard algorithms for identifying who understands a codebase. "Most scenarios led to measurable impacts."
If those models break, organisations lose the instrument that would tell them they have a comprehension
problem. This is simulation-based and exploratory, so it should be treated as a hypothesis-generating result.

### 6. Delivery outcomes: throughput up, stability still down

[DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)
(~5,000 professionals, 100+ hours qualitative) is the best-powered survey instrument here, and its finding is
deliberately two-sided. **90% of respondents use AI at work and >80% believe it raised their productivity;
30% report little or no trust in AI-generated code.** AI adoption's relationship with **throughput flipped
positive** in 2025 (it was negative in 2024) — but its relationship with **software delivery stability
remains negative**. DORA's framing is that AI is an **amplifier**: without strong automated testing, mature
version control and fast feedback loops, higher change volume converts directly into instability.

[DORA 2024](https://dora.dev/research/2024/dora-report/) reported the same stability penalty more sharply;
secondary coverage puts a 25% increase in AI adoption at **+3.4% code quality, +7.5% documentation quality,
−1.5% throughput and −7.2% delivery stability** (these precise figures are UNVERIFIED against the full PDF).
That combination — micro-quality up, system stability down — is the single most useful frame in this stream,
because it explains why vendor RCTs on isolated tasks and repository-level longitudinal studies can both be
right.

### 7. What the volume numbers mean

[Pichai, Google Cloud Next 2026 (22 Apr 2026)](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/):
"Today, **75% of all new code at Google is now AI-generated and approved by engineers, up from 50% last
fall**." [Sonar](https://www.sonarsource.com/company/press-releases/sonar-data-reveals-critical-verification-gap-in-ai-coding/)
puts the industry figure at **42% of committed code today, projected to 65% by 2027**.

These are the exposure base rates. Even a modest per-unit quality penalty compounds at these volumes, and
"approved by engineers" is precisely the claim that §4 calls into question.

## Counter-evidence and caveats

**1. METR walked back the headline finding — this matters a great deal.** The 19%-slowdown result
([METR, Jul 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/); 16 developers,
246 issues) is the single most-cited datapoint against AI coding. In
[February 2026 METR published an update](https://metr.org/blog/2026-02-24-uplift-update/) redesigning the
experiment and reporting late-2025 data showing **speedup**: returning developers −18% completion time
(CI −38% to +9%), new developers −4% (CI −15% to +9%). They identify severe selection bias — developers now
refuse to participate without AI, and **strategically avoid submitting tasks where AI would help most**
("I avoid issues like AI can finish things in just 2 hours, but I have to spend 20 hours"). METR's own
position is that developers are "likely more sped up from AI tools now — in early 2026." Both confidence
intervals cross zero, so this is weak evidence for *speedup* too — but anyone citing the 19% figure in 2026
without the update is misrepresenting the source.

**2. The strongest RCTs measure output, not quality.** Cui et al.
([Management Science, 2026](https://pubsonline.informs.org/doi/10.1287/mnsc.2025.00535); **n=4,867** across
Microsoft, Accenture and a Fortune 100 firm) found a **26.08% increase in completed tasks (SE 10.3%)**, with
junior developers gaining 27–39% and seniors only 8%. Google's internal RCT
([arXiv 2410.12944](https://arxiv.org/abs/2410.12944), n=96) found ~21% time reduction with a wide CI. Neither
reports a maintainability, defect or review outcome. They are strong evidence that AI raises throughput and
silent on whether it raises debt. Note also the juniority gradient: if gains concentrate among the developers
least equipped to evaluate what they merge, that is arguably *consistent with* the debt hypothesis rather
than against it.

**3. GitHub's own RCT found quality gains.**
[GitHub (Nov 2024)](https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/):
243 developers with ≥5 years Python, 202 valid submissions, 25 blind reviewers producing 1,293 reviews.
Readability +3.62% (p=0.003), reliability +2.94% (p=0.01), maintainability +2.47% (p=0.041), conciseness
+4.16% (p=0.002), 53.2% greater likelihood of passing all 10 unit tests, 5% more likely to be approved. All
statistically significant. **But**: the task was a single greenfield exercise — a web server for fictional
restaurant reviews — evaluated in isolation. Duplication, cross-file connectivity decay and legacy-code
neglect (the actual debt mechanisms in §1) cannot manifest in a fresh single-file task. It is also the
vendor's own research on its own product. It is good evidence that AI improves *local* code quality and no
evidence at all about *system* maintainability.

**4. AI-generated files receive *less* maintenance — and that cuts both ways.**
[Sawada et al. (NAIST, May 2026)](https://arxiv.org/html/2605.06464v1) matched 508 AI-generated against 508
human-generated files across 100 repositories over ≥6 months and found AI files received **~50% fewer commits
in their first month** and **5.03% fewer bug-fix commits** (11.73% vs 16.76%). A defender of AI code reads
this as higher quality. A defender of the debt hypothesis reads it as abandonment — nobody is tending this
code. The study cannot distinguish these. One figure does support the dependency thesis: **humans performed
83.21% of maintenance commits on AI-generated files; agents performed only 16.79%** — the agents do not come
back to maintain their own output, humans do.

**5. The literature genuinely does not agree.**
[Geruslu, Aliyeva & Tüzün (arXiv 2603.25146)](https://arxiv.org/abs/2603.25146), a systematic review of 24
primary studies, concludes there is "variability in quality outcomes such as correctness, security,
maintainability, and complexity across studies, **with both improvements and risks reported**," and that
quality is contingent on prompt design, task specification and developer expertise rather than on any
property of the tools. Anyone claiming the empirical question is settled is overstating.

**6. Vendor incentives run in both directions.** The pro-debt evidence leans on GitClear (sells diff
analytics), Sonar (sells technical-debt management), CodeScene (sells code health), CodeRabbit (sells AI code
review) and Faros (sells engineering telemetry) — every one of them monetises the problem it is measuring.
The anti-debt evidence leans on GitHub (sells Copilot) and Microsoft-affiliated authors. The cleanest
sources are the academic AIDev-based studies (§4) and DORA, and those are the ones I have weighted highest.

**7. Attribution remains the deepest methodological problem.** GitClear, DORA and Faros measure *the era*, not
*the code*. Only Liu et al. (§2) and the AIDev-based studies (§4) use explicit provenance metadata — and that
metadata captures agent-authored PRs and tagged commits while missing the far larger volume of IDE-autocomplete
assistance that leaves no trace. The AI-attributed corpus is therefore both small relative to true AI usage and
non-randomly selected (agentic PRs are a distinctive workflow), which cuts both ways for generalisation.

**8. Several widely circulated figures did not survive verification.** The Uplevel "41% more bugs" number is
behind a gate and I could confirm only the directional claim of "a significantly higher bug rate" on the
[landing page](https://resources.uplevelteam.com/gen-ai-for-coding). I also encountered a claim of "32.7% AI
vs 84.4% human PR acceptance across 8.1 million PRs" in secondary blog coverage and could not trace it to any
primary source — **it should not be used.** The DORA 2024 precise percentages are likewise secondary-sourced.

## Gaps and open questions

1. **No controlled study measures maintenance cost over time.** Every RCT measures a task of hours; every
   debt claim concerns months-to-years. The decisive experiment — randomise AI assistance across teams, then
   measure defect and change-cost outcomes on the same modules 12–24 months later — has not been run.

2. **Attribution at line level is unsolved.** Until provenance is recorded natively (a commit trailer that
   captures autocomplete, not just agent PRs), longitudinal claims stay correlational.

3. **Is lower churn on AI files quality or neglect?** Sawada et al. leaves the stream's most important
   ambiguity unresolved. Distinguishing them needs incident/outage data joined to file provenance — which no
   published study has.

4. **Comprehension is measured only indirectly.** SATD comments (n=81), Truck-Factor simulations, and review
   metrics are all proxies. No study directly tests whether developers can explain, debug or safely modify
   code an AI wrote for them versus code they wrote. This is the central claim of the hypothesis and it is
   the least directly evidenced.

5. **Harness lock-in is entirely unmeasured.** I found **no** empirical study testing whether codebases with
   high AI-generated content become harder for *humans* to modify without AI assistance, or whether teams
   become unable to maintain code when they switch models or tools. The CodeScene result (AI performs worse
   on unhealthy code) is the closest proxy and is one step removed. **This is the largest single gap relative
   to the hypothesis.**

6. **Survivorship in the AIDev corpus.** Acceptance and rejection rates are computed over PRs that agents were
   permitted to open in public repos with maintainer tolerance for bot PRs — a selected population.

7. **No data on juniors.** Cui et al. show gains concentrate in junior developers; nobody has measured whether
   those developers' *own* skill trajectory or code comprehension changes. Stack Overflow's finding that
   **20% report reduced confidence in their own problem-solving** is the only signal, and it is self-reported.

8. **2026 agentic-era data is thin.** Most quality evidence predates widespread autonomous agent use. GitClear
   2026 and the AIDev studies are the leading indicators; their 2027 successors will matter more.
