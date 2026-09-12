# Stream 3 — Comprehension Debt, Skill Atrophy, and Dependency on the Coding Model/Harness

## Stream summary

The core mechanism behind the "AI code as new technical debt" hypothesis — that generated code
becomes something few humans (or only a specific model/harness) understand — has moved from
informal essay-writing in 2024-2025 to a small but real empirical literature by late 2025/2026,
plus a wave of industry-vendor pricing/rate-limit events that illustrate dependency risk
directly. The term "comprehension debt" was popularized by Addy Osmani (Google, "Comprehension
Debt: The Hidden Cost of AI-Generated Code," O'Reilly Radar/his own blog, March 2026), building on
Simon Willison's earlier and more precise distinction between "vibe coding" (accepting code you
never review) and "cognitive debt" (losing track of how agent-written code works even when you
did review it, tested it, or it looks clean). Independently, Margaret-Anne Storey (University of
Victoria) has published a parallel "cognitive debt"/"intent debt" framework (ACM Queue, Feb 2026;
GetDX; her own blog) grounded in Peter Naur's 1985 "Programming as Theory Building." Both framings
are currently conceptual/essayistic rather than measured against a validated instrument, and both
authors explicitly say so.

The strongest empirical evidence supporting the hypothesis is Anthropic's own January 2026 RCT
(52 engineers learning an unfamiliar Python library), which found AI-assisted developers scored
50% vs. 67% on a comprehension quiz (Cohen's d = 0.74, p = 0.01) — with the gap concentrated in
debugging questions and in developers who delegated code generation vs. those who used AI
conversationally. This tracks with the CMU/Microsoft Research CHI 2025 survey (319 knowledge
workers) showing higher trust in GenAI correlates with less critical thinking, and with the MIT
Media Lab "Your Brain on ChatGPT" preprint (EEG evidence of "cognitive debt" and reduced essay
ownership) — though the latter is unpeer-reviewed, N=54 (18 in the critical fourth session), and
about writing, not code. GitClear's analysis of 211M lines of code (refactoring share of commits
falling from 25% to under 10% between 2021-2024, copy/paste overtaking "moved" code, code churn
roughly doubling) and Google's 2024 DORA report (a 25% rise in AI adoption predicting a 7.2% drop
in delivery stability even as individual-reported productivity rose) are the best large-sample
quantitative proxies for eroding maintainability, and METR's July 2025 RCT (experienced OSS devs
19% *slower* with AI tools despite believing themselves 20% faster) is strong counter-evidence to
naive productivity claims, if not directly about comprehension.

On lock-in: dependency on a specific vendor/harness is well evidenced but mostly as *economic and
operational* risk (Cursor's June-July 2025 pricing backlash; Anthropic's August 2025 Claude Code
weekly rate limits) rather than as demonstrated *technical* lock-in from model-specific code
styles — that claim is argued in industry blogs but not yet tested empirically. The AGENTS.md
standardization (OpenAI/Anthropic donating it to a new Linux-Foundation-hosted Agentic AI
Foundation, Dec 2025, 60,000+ adopting repos) is a real, verifiable portability countermeasure.
Authorship-based bus-factor metrics being invalidated by AI-authored merges is argued cogently in
one recent independent-researcher preprint but is conceptual, not measured. The strongest
counter-argument — that code is becoming cheap/disposable and shouldn't be "understood" so much
as regenerated — is most clearly and credibly made by Charity Majors (Honeycomb co-founder), who
also argues telemetry, not code review, should be the trust mechanism; Kent Beck's "augmented
coding" and Böckeler's Thoughtworks work on using AI *to understand* legacy code are the clearest
evidence that AI can reduce, not just create, comprehension debt.

## Evidence table

| # | Claim (one sentence) | Source title | Author/Org | Date | Type | Strength | URL | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | Coins/popularizes "comprehension debt": the growing gap between code that exists and code any human genuinely understands | Comprehension Debt: The Hidden Cost of AI-Generated Code | Addy Osmani / O'Reilly Radar | 2026-03-14 | Opinion/essay (practitioner) | Med | https://addyosmani.com/blog/comprehension-debt/ ; https://www.oreilly.com/radar/comprehension-debt-the-hidden-cost-of-ai-generated-code/ | Cites Anthropic's 52-engineer study (50% vs 67% quiz scores) and industry trust-decline stats; largely a synthesis/argument piece |
| 2 | Distinguishes "vibe coding" (unreviewed AI code) from "cognitive debt" (losing track of how reviewed agent code works) | Simon Willison's blog / tags: technical-debt, cognitive debt commentary | Simon Willison | 2025-2026 (ongoing) | Opinion/essay | Med | https://simonwillison.net/tags/technical-debt/ | "If an LLM wrote every line of your code, but you've reviewed, tested, and understood it all, that's not vibe coding" |
| 3 | Proposes a "cognitive debt"/"intent debt" framework replacing technical debt as the primary risk under AI-accelerated dev, grounded in Naur's "programs are theories" | From Technical Debt to Cognitive and Intent Debt: Rethinking Software Health in the Age of AI | Margaret-Anne Storey (Univ. of Victoria) | 2026 (ACM Queue; arXiv 2603.22106) | Perspective/position piece (peer-venue, non-empirical) | Med | https://arxiv.org/pdf/2603.22106 ; https://queue.acm.org/detail.cfm?id=3807966 | No quantitative data; conceptual framework only, per Storey's own follow-up posts |
| 4 | Same author's plainer-language version of the cognitive-debt argument, with practical mitigations (require human verification, document "why", knowledge-sharing) | Cognitive debt: The hidden risk in AI-driven software development / margaretstorey.com blog | Margaret-Anne Storey / GetDX | 2026-02-09 | Opinion/essay | Low-Med | https://getdx.com/blog/cognitive-debt-the-hidden-risk-in-ai-driven-software-development/ ; https://margaretstorey.com/blog/2026/02/09/cognitive-debt/ | Explicitly no empirical data; one classroom anecdote |
| 5 | AI-assisted developers score significantly lower on code comprehension quizzes than those coding by hand; gap concentrated in debugging and in "delegate to AI" usage patterns | How AI assistance impacts the formation of coding skills | Anthropic | 2026-01-29 | Industry RCT with methodology | High | https://www.anthropic.com/research/AI-assistance-coding-skills | N=52 mostly-junior engineers, unfamiliar Python library (Trio); AI group 50% vs. hand-coding 67% (Cohen's d=0.738, p=0.01); AI-for-conceptual-questions scored ≥65%, AI-for-code-generation <40% |
| 6 | Higher self-reported trust/confidence in GenAI correlates with less critical thinking among knowledge workers | The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers | Lee et al., Microsoft Research + Carnegie Mellon (CHI 2025) | 2025-02 | Peer-reviewed conference paper | High | https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/ | N=319 knowledge workers, 936 real AI-task examples; shift from "task execution" to "task stewardship" (verification) |
| 7 | LLM-assisted essay writers show weaker EEG neural connectivity and severely impaired ability to recall/own their own writing ("cognitive debt") vs. brain-only writers | Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task | MIT Media Lab (multiple authors) | Submitted 2025-06-10, revised through Dec 2025 | Preprint, not peer-reviewed | Med (caveat: unreviewed, small/attrited N) | https://arxiv.org/abs/2506.08872 | N=54 across 3 sessions, 18 in session 4; 83%/78% of LLM users couldn't quote their own essay; about writing not code, explicitly preliminary |
| 8 | Refactoring share of code changes fell from 25% (2021) to <10% (2024); copy/pasted code overtook "moved" (refactored) code for the first time in 2024; code churn roughly doubled (3.3%→7.1%) | Coding on Copilot (2023 data) / AI Copilot Code Quality 2025 research | GitClear | 2025-02 (with 2025 follow-up) | Industry study with stated methodology | High | https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality ; https://www.gitclear.com/ai_assistant_code_quality_2025_research | Analysis of 211M changed lines across private + 25 major open-source repos, 2020-2024/2025 |
| 9 | A 25% increase in AI adoption predicts a 7.2% decrease in software delivery stability, even as individual developer-reported flow/productivity rose | 2024 DORA State of DevOps Report | Google Cloud DORA team | 2024 (late 2024) | Industry survey/analyst report with methodology | High | https://getdx.com/blog/2024-dora-report/ ; https://thenewstack.io/dora-2024-ai-and-platform-engineering-fall-short/ | Org-level stability down while individual satisfaction/flow up ~2% — a dissociation between felt and measured impact |
| 10 | Experienced open-source developers were 19% *slower* completing real tasks with AI tools despite forecasting a 24% speedup and self-reporting a 20% speedup afterward | Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity | METR | 2025-07-10 | RCT with stated methodology | High | https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ ; https://arxiv.org/abs/2507.09089 | N=16 experienced devs, 246 real issues on large repos (avg 22k+ stars, 1M+ LOC), randomized AI-allowed vs. disallowed |
| 11 | A separate paper argues AI-assisted programming decreases experienced-developer productivity specifically via increased technical debt/maintenance burden | AI-Assisted Programming Decreases the Productivity of Experienced Developers by Increasing the Technical Debt and Maintenance Burden | Xu, Medappa, Tunc, Vroegindeweij, Fransoo | 2025-10 | Preprint (arXiv) | Med (full methodology not independently verified beyond title/abstract) | https://arxiv.org/pdf/2510.10165 | Title/thesis confirmed; detailed methodology not extractable from PDF via automated fetch |
| 12 | Authorship-based "bus/truck factor" metrics no longer predict comprehension or incident-resolution risk once AI generates merged code, because "authored implies understands" breaks down | The Substrate Collapse: AI Code Generation Invalidates Authorship-Based Knowledge Metrics | Brett Wheeler (independent researcher) | 2026-06 | Preprint/conceptual, with corroborating secondary evidence | Low-Med | https://arxiv.org/html/2606.20882 | Cites METR study and a "Liu et al. 2026" lifecycle study (AI commits: fewer surface bugs, 2x logic-bug repair rate) as corroboration, not proof |
| 13 | AGENTS.md — a vendor-neutral instructions file for coding agents — was donated by OpenAI and Anthropic to a new Linux-Foundation-hosted Agentic AI Foundation to prevent agent-ecosystem fragmentation | Linux Foundation Announces the Formation of the Agentic AI Foundation (AAIF) | Linux Foundation / OpenAI | 2025-12-09 | Press release / vendor announcement | High (as fact of the event) | https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation ; https://openai.com/index/agentic-ai-foundation/ | AGENTS.md adopted by 60,000+ repos/frameworks since Aug 2025 (Codex, Cursor, Copilot, Gemini CLI, VS Code, etc.) per secondary sources |
| 14 | Coding-agent context files (CLAUDE.md, AGENTS.md, .cursorrules) can silently be dropped from context as sessions grow, causing unauthorized edits despite explicit written rules | Practitioner reports (Reddit; Spacelift blog) on Claude Code ignoring CLAUDE.md rules under context pressure | Spacelift / community reports | 2025-2026 | Practitioner reports/vendor blog (anecdotal) | Low | https://spacelift.io/blog/claude-code-for-infrastructure-as-code | Anecdotal but consistent with known context-compaction failure modes; not a controlled study |
| 15 | Cursor's June 2025 shift from request-based to credit-based pricing (marketed as "unlimited") caused unexpected bills and a public apology/refunds | Cursor's Pricing Disaster: The Full Timeline | We Are Founders | 2025 (events June-July 2025) | News/analyst article | Med-High | https://www.wearefounders.uk/cursors-pricing-disaster-the-full-timeline-of-how-an-ai-coding-darling-burned-its-most-loyal-users/ | Direct evidence of vendor/economic lock-in risk: users tied workflows to a tool whose pricing model changed abruptly |
| 16 | Anthropic imposed new weekly usage caps on Claude/Claude Code from Aug 28, 2025, after quietly tightening limits in July, triggering developer backlash | Anthropic throttles Claude rate limits, devs call foul | VentureBeat | 2025-08 | News article | Med-High | https://venturebeat.com/ai/anthropic-throttles-claude-rate-limits-devs-call-foul | Anthropic said <5% of subscribers affected; Pro got 40-80 hrs/week Sonnet 4, Max($100) 140-280 hrs + 15-35 hrs Opus |
| 17 | Anthropic experienced clustered multi-service outages (Claude API, Console, Claude Code, Office add-ins) across Aug-Sep 2026, illustrating single-vendor dependency risk | Reports on Anthropic outages Aug-Sep 2026 | TechCrunch / StatusGator / secondary sources | 2025-09 through 2026 (ongoing incident history) | News/status-page aggregation | Med | https://techcrunch.com/2025/09/10/anthropic-reports-outages-claude-and-console-impacted/ ; https://statusgator.com/services/anthropic/outage-history | 21 incidents logged 12 Aug-2 Sep 2026 per secondary aggregator; illustrates concentration risk for teams hard-coded to one vendor |
| 18 | Kent Beck distinguishes "augmented coding" (AI as accelerant, human still owns quality/design/comprehension) from "vibe coding" (accepting whatever AI generates) | Augmented Coding: Beyond the Vibes | Kent Beck (newsletter.kentbeck.com) | 2025 | Opinion/essay (practitioner, high-credibility author) | Med | https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes | Counter to pure comprehension-debt narrative: argues understanding is preservable with the right practice, not technology-determined |
| 19 | Generative AI can be more useful for *understanding* existing/legacy code than for generating new code — demonstrated via a real open-source hospital-management-system issue | Onboarding to a "legacy" codebase with the help of AI | Birgitta Böckeler, Thoughtworks (martinfowler.com) | 2024-08-15 | Practitioner case study | Med | https://martinfowler.com/articles/exploring-gen-ai.html | Counter-evidence: AI reducing rather than creating comprehension debt in a documented walkthrough |
| 20 | Argues software is bifurcating into "disposable code" (prototypes, regenerate rather than maintain) and "durable code" (banking, medical, infra — still needs traditional engineering/trust built over time) | Disposable Code Is Here to Stay, but Durable Code Is What Runs the World | Charity Majors, Honeycomb | 2025-07-29 | Opinion/essay (practitioner, high-credibility author/co-founder) | Med | https://www.honeycomb.io/blog/disposable-code-is-here-to-stay | "There is no test suite on earth that could make me trust a new chunk of code more than...code that's been running in production for two years" |
| 21 | Argues code review is not the right trust mechanism for AI-era code; production telemetry/observability, not human reading, should validate AI-generated code | Charity Majors on AI-generated code and code review (Pragmatic Engineer interview; charity.wtf) | Charity Majors / Gergely Orosz | 2025-2026 | Opinion/interview (practitioner) | Med | https://newsletter.pragmaticengineer.com/p/stop-being-skeptical-about-ai-for | "No PR should ever be accepted unless the engineer can answer: how will I know if this breaks?" — reframes comprehension debt as an observability problem, not a reading problem |
| 22 | Steve Yegge argues developers should stop reading/reviewing AI-generated code line by line ("code is a liquid... you don't look at it"), trusting agent output and validating outcomes instead | Steve Yegge Wants You to Stop Looking at Your Code | Tim O'Reilly, O'Reilly Radar | 2026-03-12 | Opinion/interview (practitioner, high-profile) | Med | https://www.oreilly.com/radar/steve-yegge-wants-you-to-stop-looking-at-your-code/ | Directly on-point for the hypothesis: an influential voice explicitly endorsing giving up code comprehension as the trade for velocity |
| 23 | Lisanne Bainbridge's 1983 "Ironies of Automation" (deskilling; operators left with only the hardest, least-practiced tasks) is being explicitly reapplied to AI coding tools | Ironies of Automation (1983); "AI and the ironies of automation" | Lisanne Bainbridge (Automatica, 1983); Uwe Friedrichsen (2025 application) | 1983 / 2025 | Foundational peer-reviewed paper + contemporary application essay | High (foundational) / Med (application) | https://www.sciencedirect.com/science/article/abs/pii/0005109883900468 ; https://www.ufried.com/blog/ironies_of_ai_1/ | ~1800+ citations by 2016; contemporary essay explicitly draws the AI-coding parallel (deskilling, humans left to debug what they can't follow) |
| 24 | 88% of surveyed developers report at least one negative impact of AI on technical debt (unreliable-looking-correct code, duplicated/unnecessary code); 93% also report at least one positive impact (e.g., documentation) | State of Software Delivery 2025 / secondary survey reporting (via LeadDev, Stack Overflow Blog coverage) | Industry survey (aggregated via LeadDev / Stack Overflow) | 2025-2026 | Survey (secondary reporting; primary survey not independently fetched) | Low-Med | https://leaddev.com/technical-direction/how-ai-generated-code-accelerates-technical-debt | Numbers reported second-hand from an industry survey; original survey instrument/N not verified directly |
| 25 | AGENTS.md-style standardization and portable prompt/instruction practices are explicitly framed by practitioners as mitigations against single-vendor coding-agent lock-in | Practitioner comparisons of Claude Code/Codex/Cursor/OpenCode on lock-in and model flexibility | Multiple vendor-comparison blogs (ComputingForGeeks, Morphllm, etc.) | 2026 | Vendor/analyst blogs | Low | https://www.morphllm.com/comparisons/claude-code-alternatives | Consistent secondary framing rather than primary data; useful for the "portability mitigation" narrative but not rigorous |
| 26 | The gap between "understanding-oriented" and "delegation-oriented" AI use is the single best predictor of skill retention in the empirical literature so far | Cross-cutting synthesis of #5, #6 above | Anthropic; Lee et al./Microsoft-CMU | 2025-2026 | Synthesis of two high-quality primary studies | High | https://www.anthropic.com/research/AI-assistance-coding-skills ; https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/ | Both studies converge independently on "how you use AI" mattering more than "whether you use AI" |

## Detailed findings

### 1. Concepts and framing: who coined "comprehension debt" / "cognitive debt" and what they cite

The clearest, most widely circulated coinage is **Addy Osmani's "Comprehension Debt"**
(published simultaneously on his own blog and O'Reilly Radar, March 2026):
https://addyosmani.com/blog/comprehension-debt/ and
https://www.oreilly.com/radar/comprehension-debt-the-hidden-cost-of-ai-generated-code/. Osmani
defines it as "the growing gap between how much code exists in your system and how much of it any
human being genuinely understands," explicitly distinguishing it from classic technical debt
(which announces itself through friction) because comprehension debt "breeds false confidence"
and accumulates invisibly across code reviews that "looked fine." Osmani cites Anthropic's own
52-engineer study (see below) and a cited-but-unlinked claim that "developer trust in AI-generated
code accuracy fell from 40% (2024) to 29% (2025)" alongside "production incidents per pull request"
rising 23.5% — these secondary statistics could not be traced to a primary source in this pass and
should be treated as **unverified** pending a primary citation.

**Simon Willison** used "cognitive debt" earlier and more precisely
(https://simonwillison.net/tags/technical-debt/), defining it as what accumulates "when we lose
track of how code written by our agents works" — explicitly *not* about code quality (code can be
clean, tested, and documented and still carry cognitive debt) but about whether the *maintainer*
understands it. His practical proposed mitigation is "linear walkthroughs" — forcing a human to
trace agent-written logic line by line before accepting it.

**Margaret-Anne Storey** (University of Victoria) independently developed a "cognitive debt" /
"intent debt" framework, published as an ACM Queue perspective piece and preprint
(https://arxiv.org/pdf/2603.22106, https://queue.acm.org/detail.cfm?id=3807966) and in more
accessible form via GetDX (https://getdx.com/blog/cognitive-debt-the-hidden-risk-in-ai-driven-software-development/).
Storey's framing rests on Peter Naur's 1985 idea that "a program is a theory" living in developers'
heads, and Fred Brooks' *Mythical Man-Month*; she argues that AI-accelerated development lets teams
outrun that shared theory even while the code itself stays "clean." This is explicitly conceptual —
Storey's own posts state there is no quantitative data behind the framework, only a classroom
anecdote and synthesis of practitioner discussion.

Neither Osmani's nor Storey's framing has yet been operationalized into a measurable construct
(e.g., a validated comprehension-debt score); both remain essayistic as of this research.

**Thoughtworks/Martin Fowler**'s contribution is more oblique but directly relevant: Birgitta
Böckeler's August 2024 piece "Onboarding to a 'legacy' codebase with the help of AI"
(https://martinfowler.com/articles/exploring-gen-ai.html) documents using GenAI *to reduce*
comprehension debt — using it to understand an unfamiliar, real hospital-management open-source
codebase rather than to generate new code — which is one of the clearer pieces of counter-evidence
in this stream (see Counter-evidence section).

**Kent Beck**'s "Augmented Coding: Beyond the Vibes" (https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes)
explicitly separates "vibe coding" (accepting whatever the AI generates) from "augmented coding"
(AI as accelerant while the human retains responsibility for quality, complexity, test coverage,
and design) — implying comprehension debt is a *practice choice*, not an inevitable consequence of
using AI tools.

**Steve Yegge** takes the opposite, more radical position: in a March 2026 O'Reilly Radar interview
(https://www.oreilly.com/radar/steve-yegge-wants-you-to-stop-looking-at-your-code/) he argues
developers should explicitly stop reading code line by line ("code is a liquid... you don't
freaking look at it"), reframing the goal as validating *outcomes* rather than maintaining
*comprehension* — effectively endorsing comprehension debt as an acceptable, even necessary,
trade for velocity. **Charity Majors** makes a structurally similar but more rigorous argument: in
her Honeycomb post (https://www.honeycomb.io/blog/disposable-code-is-here-to-stay) and a Pragmatic
Engineer interview (https://newsletter.pragmaticengineer.com/p/stop-being-skeptical-about-ai-for),
she argues code review/human reading is "the least valuable part of what humans add," and that
production telemetry — not comprehension — should be the trust mechanism ("no PR should be
accepted unless the engineer can answer: how will I know if this breaks?").

The stream prompt also asked about **"AI-generated technical debt"** as a distinct term: this
appears widely in industry commentary (GitClear, LeadDev, Stack Overflow Blog) but functions more
as a catch-all than a coined term with a single author; researchers studying self-admitted
technical debt have proposed "GIST debt" — debt arising from uncertainty about AI-generated code's
behavior/suitability rather than from deliberate shortcuts — per secondary reporting
(https://leaddev.com/technical-direction/how-ai-generated-code-accelerates-technical-debt), though
the primary paper coining "GIST debt" was not independently located/verified in this pass and
should be treated with caution.

### 2. Empirical evidence on skill erosion / deskilling

The single strongest primary source here is **Anthropic's own January 2026 study**
(https://www.anthropic.com/research/AI-assistance-coding-skills), a randomized controlled trial
with 52 mostly-junior engineers learning Trio (an async Python library unfamiliar to all
participants). AI-assisted developers scored 50% vs. 67% for hand-coders on a post-task
comprehension quiz (Cohen's d = 0.738, p = 0.01) — roughly two letter grades — with the largest
gap on debugging questions. Critically, the study found usage pattern mattered more than usage
itself: participants who used AI for conceptual questions/explanations scored ≥65%, while those
who delegated code generation to AI scored <40%. Speed gains from AI were not statistically
significant. Anthropic's own authors caveat that N was small and the quiz measured immediate, not
long-term, retention.

This dovetails with the **Microsoft Research + CMU CHI 2025 study** (Lee et al.,
https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/),
which surveyed 319 knowledge workers and analyzed 936 real AI-assisted task examples, finding
higher self-reported *trust* in GenAI is associated with *less* critical thinking, while higher
self-confidence is associated with more. This is not code-specific but is the paper most often
invoked as foundational for the broader deskilling argument (it is a peer-reviewed CHI 2025 paper,
not a preprint).

The **MIT Media Lab "Your Brain on ChatGPT"** preprint
(https://arxiv.org/abs/2506.08872) is the most attention-getting but weakest-evidenced source in
this cluster: N=54 across three sessions with only 18 completing a fourth "switch" session, EEG
data showing weakest neural connectivity in LLM users, and 83%/78% of LLM users unable to quote
their own essays. It is explicitly a writing-task study (not code), unpeer-reviewed as of the
last-checked revision (Dec 2025), and the authors themselves flag it as preliminary. It is
frequently cited by surrounding commentary (Osmani, Storey) as supporting evidence for
code-comprehension claims, which is a generalization beyond what the study itself supports.

No source located in this pass constitutes a rigorous, code-specific, longitudinal deskilling
study beyond Anthropic's — this is a clear gap (see Gaps section).

**Bainbridge's 1983 "Ironies of Automation"** (https://www.sciencedirect.com/science/article/abs/pii/0005109883900468)
is the canonical foundational reference the prompt asked about: it argues that automating the
"easy" parts of a task leaves human operators responsible for exactly the hardest, least-practiced
residual tasks, and that reliance on automation actively erodes the skill needed to intervene when
automation fails. A 2025 essay (https://www.ufried.com/blog/ironies_of_ai_1/) explicitly reapplies
this to AI coding tools, arguing that developers are increasingly left to debug/maintain code they
no longer have the practiced skill to follow — directly analogous to the "operator deskilled by the
system they must still supervise" irony.

### 3. Ownership, bus factor, and orphaned code

The most direct — if speculative — treatment is Brett Wheeler's 2026 preprint "The Substrate
Collapse" (https://arxiv.org/html/2606.20882), arguing that authorship-based bus/truck-factor
metrics assumed "authored implies understands," a link severed once AI generates code that a
human merges without deep comprehension. Wheeler's paper is conceptual but cites two corroborating
data points: the METR productivity study (see below) and an unverified "Liu et al. (2026)"
claim that AI-generated commits remove surface-level defects while introducing logic-dependent
bugs at roughly twice the repair rate of human-authored bugs — this secondary citation could not
be independently traced to a primary paper in this pass and should be flagged **UNVERIFIED**.

Beyond this, evidence is anecdotal: practitioner blogs (Medium, dev.to) describe onboarding
successors taking months when knowledge lived only in one departed engineer's head, and argue AI
"mentors" with full code-history access could shorten this — but no controlled study measuring
onboarding time in AI-heavy vs. AI-light codebases was found. This is a clear evidence gap.

### 4. Dependency/lock-in on the harness or model

This is the best-evidenced sub-question in the stream, though largely as **economic/operational**
rather than **technical** lock-in:

- **Pricing shocks**: Cursor's June 2025 shift from request-based to "unlimited"-but-actually-
  credit-based pricing caused a well-documented backlash, surprise bills, and a public apology
  with refunds in July 2025 (https://www.wearefounders.uk/cursors-pricing-disaster-the-full-timeline-of-how-an-ai-coding-darling-burned-its-most-loyal-users/).
- **Rate-limit shocks**: Anthropic imposed new weekly usage caps on Claude/Claude Code starting
  August 28, 2025 (Pro: 40-80 hrs/week Sonnet 4; Max $100: 140-280 hrs plus 15-35 hrs Opus),
  following an earlier unannounced tightening in July 2025, generating GitHub-issue and social-
  media backlash from developers whose workflows were built around continuous agent use
  (https://venturebeat.com/ai/anthropic-throttles-claude-rate-limits-devs-call-foul).
- **Outages**: secondary aggregation suggests a cluster of ~21 Anthropic incidents between
  12 August and 2 September 2026 spanning Claude API, Console, Claude Code, and Office add-ins
  (https://techcrunch.com/2025/09/10/anthropic-reports-outages-claude-and-console-impacted/,
  https://statusgator.com/services/anthropic/outage-history) — illustrating that teams whose
  workflows are hard-wired to one vendor's agent inherit that vendor's availability risk.
- **Context-file lock-in / criticality**: CLAUDE.md, AGENTS.md, and .cursorrules files are widely
  described in practitioner sources as becoming de facto critical infrastructure that encodes
  architecture, conventions, and guardrails for the agent — but also as unreliable under context
  pressure: practitioner reports describe Claude Code silently dropping CLAUDE.md rules as a
  session's context window fills, leading to unauthorized edits (https://spacelift.io/blog/claude-code-for-infrastructure-as-code).
  This is anecdotal, not a controlled study, but is a consistent and plausible failure mode given
  known context-compaction mechanics.
- **Portability countermeasure**: the most concrete positive development is the **AGENTS.md
  standard**, created within OpenAI's Codex ecosystem, adopted by 60,000+ repositories/frameworks
  by late 2025 (Codex, Cursor, Copilot, Gemini CLI, VS Code, Devin, Amp, Factory, Jules, etc. per
  secondary reporting), and then donated by OpenAI and Anthropic to a newly formed
  **Agentic AI Foundation** hosted by the Linux Foundation on December 9, 2025
  (https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation,
  https://openai.com/index/agentic-ai-foundation/), backed by Google, Microsoft, AWS, Bloomberg,
  and Cloudflare, explicitly to prevent agent-ecosystem fragmentation. This is a direct, verifiable
  mitigation against the hypothesis's "lock-in via proprietary context files" concern.
- **Model-specific code style / cross-model maintainability**: this specific claim — that code
  produced by one model is harder for a *different* model or human to maintain — is asserted
  repeatedly in vendor-comparison blogs (e.g., https://www.morphllm.com/comparisons/claude-code-alternatives)
  but was **not found substantiated by any controlled study** in this pass. This is a genuine gap;
  the claim should be treated as plausible-but-unverified pending empirical work.

### 5. Counter-argument: code is cheap/disposable, and AI is good at explaining/refactoring

**Charity Majors** gives the clearest articulation of the "disposable code" counter-argument
(https://www.honeycomb.io/blog/disposable-code-is-here-to-stay, July 2025): software is
bifurcating into disposable code (prototypes, scripts — "you generate some code to do a thing, you
do the thing, you throw it away") and durable code (banking, medical devices, infrastructure —
still requiring traditional engineering discipline, testing, and — crucially — *trust built over
years in production*, which she argues no test suite or AI review can substitute for). This is a
partial counter to the hypothesis: it concedes comprehension debt is real and acceptable for
disposable code, but explicitly rejects the idea that durable/critical code becomes disposable.

**Kent Beck**'s "augmented coding" and **Birgitta Böckeler**'s Thoughtworks case study on using
GenAI to understand (not generate) legacy code are the two clearest pieces of evidence that AI can
*reduce* comprehension debt when used deliberately for explanation rather than delegation — a
finding that is also independently supported by the Anthropic RCT's finding that AI-for-
conceptual-questions usage scored far higher (≥65%) than AI-for-code-generation usage (<40%) on
the same comprehension quiz. Industry claims that "AI-driven refactoring achieves 60-80% reduction
in technical debt accumulation" and "4x better ROI" for prioritized legacy modernization
(surfaced via aggregator/vendor content such as gocodeo.com, createq.com) could not be traced to
verifiable primary studies in this pass and should be treated as **largely unverified,
vendor-sourced marketing claims** rather than independent evidence.

## Counter-evidence and caveats

- **METR's July 2025 RCT** (https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/,
  https://arxiv.org/abs/2507.09089) found experienced open-source developers were **19% slower**
  with AI tools on real tasks in their own large repositories, despite forecasting a 24% speedup
  and self-reporting a 20% speedup afterward. This complicates (though does not directly refute)
  the comprehension-debt hypothesis: if AI isn't even delivering the claimed speed benefit for
  experienced developers on familiar codebases, the debt/dependency trade may be even less
  favorable than proponents assume — but it is also evidence that heavy AI *reliance* is not yet
  universal even among developers who have access to it.
- Both of the two most-cited conceptual "debt" frameworks (Osmani's comprehension debt; Storey's
  cognitive/intent debt) explicitly state they are **not backed by an original empirical study** —
  they synthesize other people's data and personal/anecdotal observation. Citing them as if they
  were empirical findings would overstate the evidence.
- The MIT Media Lab "Your Brain on ChatGPT" study, frequently invoked in this space, is an
  **unpeer-reviewed preprint** about essay-writing (not code), with a small and heavily attrited
  sample (54 → 18 by session 4). It should not be treated as direct evidence about programmers or
  code comprehension.
- Kent Beck, Böckeler/Thoughtworks, and (in a more radical form) Charity Majors and Steve Yegge all
  represent **credible, senior practitioner voices arguing against treating comprehension loss as
  either inevitable or necessarily harmful** — this is a genuine, non-fringe counter-position, not
  a strawman, and should be weighted accordingly in any synthesis.
- The DORA 2024 finding is a **dissociation, not a clean refutation or confirmation**: AI adoption
  correlated with *individual*-reported productivity/satisfaction gains at the same time as
  *organizational* delivery-stability losses — suggesting the harm (if any) may be a coordination/
  batch-size effect rather than a comprehension effect per se.
- Several statistics circulating in this space (Osmani's "trust fell 40%→29%," "incidents per PR
  up 23.5%"; the "88%/93% of developers report negative/positive AI technical-debt impacts" survey
  figures) were traceable only to secondary blog citations, not to an identifiable, fetchable
  primary source, in this research pass. They are flagged in the evidence table as Low-strength /
  secondary-sourced and should be re-verified before being used as headline statistics.
- The claim that AI-generated code is harder for a *different* model or harness to maintain
  (model-specific lock-in at the code level, as opposed to workflow/pricing lock-in) is asserted
  frequently but was not found substantiated by any study — it remains a plausible hypothesis, not
  an evidenced finding.

## Gaps and open questions

1. **No longitudinal, code-specific deskilling study exists yet.** Anthropic's RCT is a single
   session/task; MIT Media Lab's study is about essays; there is no multi-month or multi-year study
   tracking professional developers' comprehension/debugging skill over time as AI-assistance
   intensity varies.
2. **No controlled study measures onboarding time or "orphaned code" incidence in AI-heavy vs.
   AI-light codebases.** The bus-factor/truck-factor argument (Wheeler 2026) is conceptually
   compelling but entirely unmeasured.
3. **Model-specific code style and cross-model maintainability costs are unmeasured.** No study
   was found quantifying whether code produced by Model A is measurably harder for Model B (or a
   human unfamiliar with Model A's idioms) to maintain than same-language human-written code.
4. **The "GIST debt" concept and several widely-cited survey statistics (88%/93%, trust decline
   40%→29%, incidents +23.5%) need primary-source verification** — they currently trace only to
   secondary blog/press coverage in this research pass.
5. **No direct empirical test of the "comprehension debt" or "cognitive/intent debt" constructs
   exists** — both remain qualitative frameworks awaiting an operational definition and measurement
   instrument (e.g., a validated comprehension-debt score correlated with incident rates, review
   time, or onboarding time).
6. **The economic lock-in evidence (Cursor pricing, Claude Code rate limits) is well documented,
   but no study connects these events to measured switching costs** — e.g., how many teams
   actually migrated tools, how long it took, or what it cost them technically versus just
  financially.
7. Given the very fast pace of change in this space (this stream cites several sources dated as
   late as mid-2026), any synthesis should note that findings from H1 2026 (Anthropic RCT, Storey's
   ACM Queue piece, GitClear's 2026 "Maintainability Gap" follow-up) supersede earlier 2024-2025
   framing and should be weighted more heavily.
