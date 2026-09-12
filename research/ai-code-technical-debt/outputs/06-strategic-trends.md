# Stream 6 — Strategic Trend and Direction: Where the Industry Is Heading

## Stream summary

The evidence broadly supports the hypothesis that the industry is moving toward AI agents owning
larger portions of the software lifecycle, with growing (if contested) acknowledgment that this
creates a new dependency and comprehension risk — but the framing differs sharply by source type.
Analyst firms (Gartner, Forrester, IDC) forecast very high adoption (75–90% of enterprise engineers
using AI code assistants by 2028) alongside explicit warnings that are directly on-hypothesis:
Gartner's "Predicts 2026" report forecasts a 2,500% increase in software defects by 2028 from
prompt-to-app/citizen-development approaches, driven by "a new class of defect... as AI generates
context-deficient code" that produces "complex architectural and logical bugs... significantly
harder to detect," and separately predicts over 40% of agentic AI projects will be cancelled by
end-2027 due to cost, governance and unclear ROI — a governance failure, not strictly a code-debt
one. Vendors are unambiguously racing toward agents owning more of the SDLC: GitHub's Agent HQ
(multi-vendor "mission control"), Anthropic's Claude Code/Agent SDK and Managed Agents, OpenAI's
Codex + AGENTS.md, AWS Kiro's "spec-driven development," and Google Antigravity/Jules all point the
same direction — from assistant to autonomous agent to fleets of agents. Karpathy's "Software 3.0"
thesis (English as source code, code as a disposable, regenerable intermediate output) is the most
articulate "code doesn't need to be human-legible" vision, while Thoughtworks explicitly names the
countervailing risk as "cognitive debt" — "the gap between humans and software systems" widening as
AI generates more code than teams can retain shared understanding of — and recommends governance
(Agent Skills, spec-driven development, mutation testing, Git AI provenance tracking) rather than
abandoning human comprehension. Labour data (Stanford's "Canaries in the Coal Mine," Challenger
Gray & Christmas layoff tracking) shows a real, measurable hollowing of junior-engineer hiring
correlated with AI exposure. Counter-evidence is real too: Stack Overflow's 2025 survey shows
adoption rising (80%+) while trust in AI accuracy is *falling* (40%→29%), and DORA 2025 finds AI is
an "amplifier" of existing organizational quality rather than a uniform net positive — teams with
weak practices ship "low-quality work, just faster." Coding-agent market concentration (Anthropic
~54%, OpenAI ~21% per Menlo Ventures) plus formal model-deprecation cycles (as short as 2 weeks for
preview models) is a documented, structural dependency/single-point-of-failure risk for code whose
maintenance already depends on a specific vendor's agent.

## Evidence table

| # | Claim (one sentence) | Source title | Author/Org | Date | Type | Strength | URL | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | Gartner forecasts 90% of enterprise software engineers will use AI code assistants by 2028, up from <14% in early 2024 | Gartner Says 90% of Enterprise Software Engineers Will Use AI Code Assistants by 2028 (analyst Joachim Herschmann) | Gartner (via DevOpsDigest mirror) | 2025-07-01 | Analyst report / press release | High | https://www.devopsdigest.com/gartner-75-of-enterprise-software-engineers-will-use-ai-code-assistants-by-2028 | Revises Gartner's earlier (Apr 2024) 75%-by-2028 figure upward; also predicts 55% of eng. teams building LLM features by 2027 |
| 2 | Gartner's original (2024) forecast: 75% of enterprise engineers will use AI code assistants by 2028, up from <10% in 2023 | Gartner Says 75% of Enterprise Software Engineers Will Use AI Code Assistants by 2028 | Gartner (press release, via search summary) | 2024-04-11 | Analyst report / press release | High | https://www.gartner.com/en/newsroom/press-releases/2024-04-11-gartner-says-75-percent-of-enterprise-software-engineers-will-use-ai-code-assistants-by-2028 | Earlier, lower baseline figure superseded by #1 — shows forecasts being revised upward year over year |
| 3 | Gartner predicts prompt-to-app/citizen-developer approaches will increase software defects by 2,500% by 2028, driven by a "new class of defect" from context-deficient AI-generated code | Predicts 2026: AI Potential and Risks Emerge in Software Engineering Technologies (summarized) | Gartner, via ArmorCode blog | 2025-12-03 | Analyst report (secondary summary of paywalled report) | High | https://www.armorcode.com/blog/your-genai-code-debt-is-coming-due-heres-what-gartner-predicts | Directly on-hypothesis: names AI-generated code debt and harder-to-detect architectural/logical bugs explicitly |
| 4 | Gartner predicts 40% of enterprises using consumption-priced AI coding tools will face unplanned costs 2x expected budgets by 2027 | Predicts 2026: AI Potential and Risks Emerge in Software Engineering Technologies (summarized) | Gartner, via ArmorCode blog | 2025-12-03 | Analyst report (secondary summary) | Med | https://www.armorcode.com/blog/your-genai-code-debt-is-coming-due-heres-what-gartner-predicts | Same report as #3; recommends FinOps-style governance for AI coding tools |
| 5 | Gartner predicts over 40% of agentic AI projects will be cancelled by end of 2027 due to escalating costs, unclear business value, or inadequate risk controls | Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027 | Gartner (press release, via secondary confirmation) | 2025-06-25 | Analyst report / press release | High | https://trullion.com/blog/why-over-40-of-agentic-ai-projects-will-fail/ | Reasons cited are governance/ROI, not code comprehension per se — nuance for the paper |
| 6 | GitHub's Gartner-cited whitepaper states "by 2028, more than 70% of enterprise software engineers will rely on AI coding agents for both synchronous and asynchronous development tasks" | GitHub recognized as a Leader by 2026 Gartner Magic Quadrant for Enterprise AI Coding Agents | GitHub/Gartner | 2026 | Vendor whitepaper citing analyst report | Med | https://github.com/resources/whitepapers/gartner-magic-quadrant-and-critical-capabilities-for-ai-code-assistants | Third distinct Gartner figure (70/75/90%) circulating — figures are inconsistent across vendor citations, a caveat for the paper |
| 7 | Forrester predicts software development will be the #1 AI use case in 2026, evolving from "vibe coding" to "vibe engineering" covering the full SDLC | Predictions 2026: Software Development Goes From Jamming To A Full Orchestra | Forrester | 2025-12-04 | Analyst report | Med | https://www.forrester.com/blogs/predictions-2026-software-development-goes-from-jamming-to-full-orchestra | Also predicts 20% fewer CS enrollments and 2x longer time-to-fill for developer roles |
| 8 | IDC predicts agentic AI will handle 40% of "G2000" jobs by end of 2026 and enable 70% of CEOs to pursue growth without headcount expansion | 2026 AI Predictions roundup (IDC) | IDC (via secondary summary) | 2025/2026 | Analyst report (secondary summary) | Low-Med | https://medium.com/@Lisamedrouk/2026-ai-predictions-what-gartner-forrester-and-idc-reveal-for-tech-leaders-96cbe36b7985 | Not fetched from IDC primary; broader than coding specifically — UNVERIFIED against primary IDC document |
| 9 | Anthropic Economic Index: coding/technical work is ~1/6 of all Claude Chat/Cowork output; Claude Code sessions show far higher autonomy (+0.37 on a 1–5 scale) and far fewer human turns (median 1 prompt vs. 13) than chat | Anthropic Economic Index report: Cadences | Anthropic | 2026-06 | Industry study (first-party usage data) | High | https://www.anthropic.com/research/economic-index-june-2026-report | Building apps uses >3x the median tokens — complexity/compute proxy for how much of the app the model is producing autonomously |
| 10 | Anthropic Economic Index: coding (Computer & Mathematical occupations) = ~35% of Claude.ai conversations and ~44% of API traffic (Jan 2026); coding work is migrating from Claude.ai chat to API/agentic use (Claude Code) | Anthropic Economic Index report (Jan/Mar 2026 editions) | Anthropic | 2026-01 to 2026-03 | Industry study (first-party usage data) | High | https://www.anthropic.com/research/anthropic-economic-index-january-2026-report | Shows the shift from "assistant used interactively" to "agent used programmatically/autonomously" in the actual usage data, supporting the agent-fleet trend |
| 11 | Claude Code annualized revenue run-rate grew from $1B (Nov 2025) to $2.5B (Feb 2026) to $8B (May 2026) | Claude Code Is Doing $2.5B in Annualized Revenue... / growth trajectory reporting | MindStudio (secondary, citing Anthropic disclosures) | 2026 | News article (secondary, aggregating company disclosures) | Med | https://www.mindstudio.ai/blog/claude-code-2-5-billion-annualized-revenue-saas-comparison | Not independently verified against an Anthropic financial filing (private company) — treat magnitude as directionally reliable, exact figures as company-sourced claims |
| 12 | Anthropic holds an estimated 54% share of the enterprise coding LLM market vs. 21% for OpenAI, up from 42% six months earlier; enterprise LLM share overall grew from 24% to 40% | 2025: The State of Generative AI in the Enterprise | Menlo Ventures | 2025 (H2) | Analyst/VC market report (survey + spend data) | High | https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/ | Coding is described as the largest departmental AI spending category (~$4B / 55% of departmental AI spend in 2025); 76% of coding solutions now bought vs. built (up from lower) |
| 13 | Cursor/Anysphere reached ~$1B ARR by late 2025, ~$2–3B by early-to-mid 2026, and a $60B valuation tied to a SpaceX deal announced June 16, 2026 (up from $29.3B Series D, Nov 2025) | Cursor by Anysphere Revenue 2026 / valuation trackers | Getlatka, TheNextWeb, Tech-Insider (secondary aggregation) | 2026 | News article (secondary, private-company estimates) | Med | https://thenextweb.com/news/cursor-anysphere-2-billion-funding-50-billion-valuation-ai-coding | Private company; figures are estimates/press reports, not audited financials — UNVERIFIED precision, directionally consistent across multiple outlets |
| 14 | OpenAI's ~$3B bid to acquire Windsurf collapsed (2025) over Microsoft IP-rights complications and Anthropic's withdrawal of Claude access from Windsurf; Windsurf was split — Google licensed the tech/hired the CEO for $2.4B, Cognition acquired the remaining company/IP | Google, Cognition Carve Up Windsurf After OpenAI's Failed $3B Acquisition Bid | DeepLearning.AI / TechCrunch | 2025-07-14 | News article | High | https://www.techcrunch.com/2025/07/14/cognition-maker-of-the-ai-coding-agent-devin-acquires-windsurf/ | Illustrates M&A volatility/consolidation and cross-vendor dependency risk (a vendor pulling model access broke a competitor's product) |
| 15 | GitHub announced "Agent HQ," a "mission control" letting Copilot subscribers run/manage coding agents from Anthropic, OpenAI, Google, Cognition, xAI and others inside one platform | Introducing Agent HQ: Any agent, any way you work | GitHub (official blog) | 2025-10 (GitHub Universe) | Vendor announcement | High | https://github.blog/news-insights/company-news/welcome-home-agents/ | Explicit strategic bet on multi-agent orchestration as the next platform layer, addressing "too many agents, no central control" |
| 16 | Satya Nadella describes a strategic shift "from building operating systems, devices for apps, to agents," framing agentic computing as expanding Microsoft's TAM; Microsoft's AI business run-rate crossed $37B (+123%) | Microsoft CEO: We're moving from OS and apps to agents instead | 9to5Mac (reporting Nadella remarks) | 2026-06-02 | News article (reporting exec statement) | Med | https://9to5mac.com/2026/06/02/microsoft-ceo-were-moving-from-os-and-apps-to-agents-instead/ | Frames "agentic DevOps" as part of a broader platform-level bet, not coding-specific alone |
| 17 | AWS Kiro launched as a ground-up agentic IDE (not a Q Developer feature update) built around "spec-driven development" — structured requirements/specs must exist before code generation | Kiro: Move beyond AI coding to agentic engineering / developer coverage | AWS / Developers Digest | 2025 GA, intl. launch 2026-05-07 | Vendor announcement + trade press | High | https://kiro.dev/ | Represents the "hybrid" competing vision: spec becomes the durable artifact, code is generated/regenerated from it |
| 18 | Google's Antigravity (agentic IDE, multi-model, "Manager view" for orchestrating parallel agents) and Jules (async agent that clones a repo, edits, tests, and opens a PR) both launched/matured in 2025–2026 alongside Gemini 3 | Google Antigravity vs. Jules comparison coverage | ainoya.dev / multiple trade outlets | 2025-11 (Antigravity), Jules GA 2025-08 | News article / trade coverage | Med | https://ainoya.dev/posts/antigravity-and-jules/ | Confirms the "agent fleet" pattern is now a multi-vendor norm (Microsoft, Google, Anthropic, OpenAI, AWS all shipping analogous products) |
| 19 | Karpathy's "Software 3.0" framing: Software 1.0 = human-written code, 2.0 = trained neural net weights, 3.0 = software programmed via prompts/context/agents/tools, with English described as "the hottest new programming language" | Andrej Karpathy: Software Is Changing (Again) [AI Startup School keynote, transcript] | Andrej Karpathy, via SingjuPost transcript | 2025-06-18 | Conference talk (primary transcript) | High | https://singjupost.com/andrej-karpathys-software-is-changing-again/ | The clearest articulation of the "code as disposable/regenerable intermediate output" competing vision named in the research questions |
| 20 | Thoughtworks' Technology Radar (Vol. 34) names "cognitive debt" — AI generating more code than teams' shared understanding can keep pace with — and recommends spec-driven development, mutation testing, Agent Skills guardrails, and Git AI provenance tracking as countermeasures | As AI Accelerates Software Complexity, Thoughtworks Technology Radar Urges a Return to Engineering Fundamentals to Combat Cognitive Debt | Thoughtworks | 2026 | Industry report (practitioner analyst) | High | https://www.thoughtworks.com/about-us/news/2026/combat-ai-cognitive-debt-radar-v34 | Closest direct evidence for the paper's core hypothesis, naming the phenomenon and proposing governance rather than acceptance |
| 21 | Thoughtworks Radar recommends "Git AI," an open-source Git extension that links every AI-written line of code to the specific agent, model, and prompt that generated it, for long-term accountability | Git AI — Technology Radar | Thoughtworks | 2026 | Industry report / tool listing | Med | https://www.thoughtworks.com/radar/tools/git-ai | A concrete tooling response to the "who understands/owns this code" dependency problem |
| 22 | Stanford Digital Economy Lab: employment of 22–25-year-olds in the most AI-exposed occupations (incl. software development) is ~19% below where it would be absent AI, driven by reduced hiring of juniors, not increased firing; experienced workers show no comparable gap | Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence (Aug 2026 update) | Brynjolfsson, Chandar, Chen — Stanford Digital Economy Lab | 2026-08 (updated; orig. Nov 2025) | Working paper (empirical, ADP payroll data, 3.5–5M workers/month) | High | https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/ | Directly supports the "junior engineers who would learn to read/maintain code are being hired less" mechanism underlying long-run dependency risk |
| 23 | 84% of developers use or plan to use AI tools (up from 76% in 2024) in the 2025 Stack Overflow survey of 49,000+ developers, yet trust in AI accuracy fell from 40% to 29%; top complaint (45%) is "almost right, but not quite" AI output, and 66% report spending more time fixing "almost-right" AI code | Developers remain willing but reluctant to use AI: The 2025 Developer Survey results are here | Stack Overflow | 2025-12-29 | Industry survey (~49,000 respondents) | High | https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/ | Key counter-evidence: rising adoption is not accompanied by rising trust — cuts against a narrative of smooth, trusted agent takeover |
| 24 | DORA's 2025 State of AI-assisted Software Development report (90% AI adoption, +14pp YoY) frames AI as an "amplifier" of existing org strengths/weaknesses; teams with weak practices "ship low-quality work... only faster," and there is no uniform improvement in delivery outcomes | 2025 DORA State of AI-assisted Software Development Report | DORA / Google Cloud | 2025 | Industry survey with methodology (large-N developer survey) | High | https://dora.dev/dora-report-2025/ | Important counter-evidence/nuance: undermines a simple "AI agents unlock consistent productivity" story and supports "debt accumulates faster where governance is weak" |
| 25 | GitHub Octoverse 2025: 1.13M+ public repos import an LLM SDK (+178% YoY); Copilot's coding agent authored 1M+ pull requests between May–Sept 2025, concentrated in older/higher-star repos; 72.6% of Copilot code-review users report improved effectiveness; ~80% of new GitHub developers use Copilot in their first week | Octoverse: A new developer joins GitHub every second as AI leads TypeScript to #1 | GitHub (official blog) | 2025-10 | Industry report (first-party platform data) | High | https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/ | Report notably does NOT disclose overall % of code AI-written or human-review/acceptance rates — a data gap flagged as a caveat |
| 26 | Model deprecation is a routine, vendor-controlled lifecycle: OpenAI gives ≥6 months' notice for GA models, ≥3 months for specialized/codex variants, but as little as 2 weeks for preview models before retirement (404s on use) | Deprecations — OpenAI API docs | OpenAI | 2026 (live docs) | Primary vendor documentation | High | https://developers.openai.com/api/docs/deprecations | Structural dependency risk: code/agents built against a specific model version can break on a vendor-set retirement schedule outside the customer's control |
| 27 | Anthropic uses a four-stage model lifecycle (Active → Legacy → Deprecated → Retired), where Retired models return errors on API calls | Model deprecations — Claude Platform Docs | Anthropic | 2026 (live docs) | Primary vendor documentation | High | https://platform.claude.com/docs/en/about-claude/model-deprecations | Same dependency dynamic as #26, confirming this is an industry-wide (not single-vendor) structural risk for agent-maintained code |
| 28 | 81% of enterprise leaders are concerned about AI vendor dependency, but only 6% believe they could switch primary AI provider without material operational disruption; 67% are actively working to avoid single-provider lock-in | AI Coding Assistants in 2026 / vendor lock-in coverage (secondary aggregation of survey data) | Kusari / multiple secondary sources | 2026 | Industry report (secondary aggregation — original survey not independently located) | Low-Med | https://www.kusari.dev/blog/ai-coding-assistants-in-2026-4x-faster-10x-riskier-the-hidden-security-cost | UNVERIFIED against a named primary survey; treat as indicative rather than precise — flagged for the paper as needing a primary-source check |
| 29 | Through June 2026, AI was cited in 101,743 US job-cut announcements (vs. 54,836 for all of 2025); AI has led all layoff reasons for 4+ straight months in 2026; tech sector job cuts up 67% YoY through July 2026, with AI "still the reason companies give" (Andy Challenger) | Challenger Report: Layoffs Fall, Hiring Picks Up; AI Leads For Fifth Straight Month (and related monthly reports) | Challenger, Gray & Christmas, Inc. | 2026 (monthly reports through July/Aug) | Industry report (labour-market tracking firm, primary data) | High | https://www.challengergray.com/blog/challenger-report-layoffs-fall-hiring-picks-up-ai-leads-for-fifth-straight-month/ | Firm itself cautions "AI is shifting the labor market, it is not dismantling it" — hiring also up 25% YoY, a needed caveat |
| 30 | Named company statements tying layoffs to AI: Meta (~8,000 roles, Apr 2026, citing AI automation in content moderation/testing/engineering), Salesforce CEO Benioff ("I need less heads," re: Agentforce), Microsoft (9,000 roles, 2025, cites AI absorbing workload), Oracle's 10-K disclosing AI-driven "reductions to our workforce" | AI Layoffs by Company: A Tracker (secondary aggregation of company statements/filings) | Founder Reports / press coverage | 2025–2026 | News article (secondary, aggregating primary company statements/SEC filings) | Med | https://founderreports.com/ai-layoffs-tracker/ | Oracle's 10-K language is a primary regulatory disclosure; other examples are company statements reported in press — worth independently pulling the Oracle 10-K text for the final paper |

## Detailed findings

### Analyst forecasts: adoption keeps being revised upward, and technical-debt language enters the frame

Gartner's public forecasts on AI code-assistant adoption have moved upward across successive press
releases: from "<10% in 2023 → 75% by 2028" in April 2024
(https://www.gartner.com/en/newsroom/press-releases/2024-04-11-gartner-says-75-percent-of-enterprise-software-engineers-will-use-ai-code-assistants-by-2028)
to "<14% in early 2024 → 90% by 2028" attributed to analyst Joachim Herschmann in a July 2025 release
(https://www.devopsdigest.com/gartner-75-of-enterprise-software-engineers-will-use-ai-code-assistants-by-2028),
while a 2026 GitHub whitepaper citing the Gartner Magic Quadrant instead quotes "more than 70% ...
by 2028" (https://github.com/resources/whitepapers/gartner-magic-quadrant-and-critical-capabilities-for-ai-code-assistants).
These three figures (70/75/90%) could not all be reconciled from the sources available; the paper
should treat "Gartner forecasts adoption in the 70–90% range by 2028" as the safe claim and flag the
inconsistency as a citation-hygiene issue common in secondary AI-market reporting.

More importantly for the hypothesis, Gartner's "Predicts 2026: AI Potential and Risks Emerge in
Software Engineering Technologies" (Dec 3, 2025) is the single most on-point analyst artifact found:
it forecasts a **2,500% increase in software defects by 2028** from prompt-to-app/citizen-developer
approaches, explicitly naming "a new class of defect... as AI generates context-deficient code,"
producing "complex architectural and logical bugs that are more damaging and significantly harder to
detect with traditional testing methods" (https://www.armorcode.com/blog/your-genai-code-debt-is-coming-due-heres-what-gartner-predicts).
The same report predicts 40% of enterprises using consumption-priced AI coding tools will see
unplanned costs exceed 2x budget by 2027, and that GenAI will cut modernization costs 30% by 2028
"but will require robust governance to mitigate risk" — Gartner's throughline is adoption-with-debt,
not adoption-without-cost. Separately, Gartner's June 2025 prediction that over 40% of agentic AI
projects will be cancelled by end-2027 attributes this to cost, unclear ROI and governance failures
(https://trullion.com/blog/why-over-40-of-agentic-ai-projects-will-fail/) — a management/governance
framing rather than a code-comprehension framing, an important nuance for the paper not to conflate.

Forrester's "Predictions 2026" sees software development as the #1 AI use case in 2026 and coins
"vibe engineering" as the successor to "vibe coding" — AI moving from snippet generation to
full-SDLC engineering-grade output including analysis, planning, testing and optimization
(https://www.forrester.com/blogs/predictions-2026-software-development-goes-from-jamming-to-full-orchestra).
It also predicts 20% fewer CS enrollments and a doubling of time-to-fill for developer roles,
tying skills-pipeline effects directly to AI coding adoption. IDC's headline claim that agentic AI
will handle 40% of "G2000" jobs by end of 2026 was found only in secondary aggregation
(https://medium.com/@Lisamedrouk/2026-ai-predictions-what-gartner-forrester-and-idc-reveal-for-tech-leaders-96cbe36b7985)
and should be treated as UNVERIFIED pending a primary IDC citation.

### Market and adoption: concentration among a small number of vendors, extraordinary revenue growth

Anthropic's Economic Index shows coding is Claude's largest single usage category (~35% of Claude.ai
conversations, ~44% of API traffic as of Jan 2026) and, critically, shows coding work migrating from
interactive chat use to autonomous/agentic API use via Claude Code
(https://www.anthropic.com/research/anthropic-economic-index-january-2026-report). Claude Code's own
revenue trajectory — reported at $1B (Nov 2025), $2.5B (Feb 2026), and $8B (May 2026) annualized run
rate (https://www.mindstudio.ai/blog/claude-code-2-5-billion-annualized-revenue-saas-comparison) —
is one of the fastest product ramps reported in software history, though as a private company's
self-disclosed metrics these figures are directionally reliable but not independently audited.

Menlo Ventures' enterprise LLM market report finds Anthropic holds an estimated 54% share of the
coding LLM market versus 21% for OpenAI (up from 42% six months prior), and that coding is the
single largest departmental AI spending category (~$4B, 55% of departmental AI spend in 2025), with
a decisive shift from building to buying AI coding tools (76% bought vs. built)
(https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/). Cursor/Anysphere
shows comparably explosive but separately-estimated growth, reportedly reaching a $60B valuation tied
to a SpaceX transaction in June 2026 after a $29.3B Series D just months earlier
(https://thenextweb.com/news/cursor-anysphere-2-billion-funding-50-billion-valuation-ai-coding) — again,
private-company estimates rather than audited figures. M&A activity shows real volatility and
cross-vendor fragility: OpenAI's ~$3B bid for Windsurf collapsed over Microsoft IP entanglements and
Anthropic's own withdrawal of Claude model access from a competitor's product, after which Windsurf
was split between Google (technology license + talent, $2.4B) and Cognition (the remaining company)
(https://www.techcrunch.com/2025/07/14/cognition-maker-of-the-ai-coding-agent-devin-acquires-windsurf/)
— a concrete, real-world instance of the dependency risk the hypothesis anticipates: a vendor
decision (Anthropic pulling model access) directly disrupted a downstream coding product's viability.

### Vendor strategic direction: from assistant to agent to agent fleets, with a converging "who owns the SDLC" ambition

Every major vendor examined is moving in the same direction. GitHub's "Agent HQ," announced at
GitHub Universe (Oct 2025), is explicitly a "mission control" for running agents from Anthropic,
OpenAI, Google, Cognition, xAI and others inside one platform, addressing what VentureBeat's coverage
called "too many agents, no central control" (https://github.blog/news-insights/company-news/welcome-home-agents/).
Microsoft's Satya Nadella has framed this in platform-shift terms — "we're moving from building
operating systems, devices for apps, to agents" — with Microsoft's overall AI business run-rate
reportedly crossing $37B (https://9to5mac.com/2026/06/02/microsoft-ceo-were-moving-from-os-and-apps-to-agents-instead/).
AWS's Kiro represents a distinct strategic bet: rather than agents freely generating code, Kiro
enforces "spec-driven development," requiring structured requirements/specs before any code
generation begins (https://kiro.dev/) — this is the clearest embodiment of the "hybrid" competing
vision named in the research questions, where the spec (not the code) becomes the durable,
human-owned artifact. Google's Antigravity (a full agentic IDE with a "Manager view" for orchestrating
multiple parallel agents) and Jules (an async agent that clones a repo, edits, tests and opens a PR
autonomously) both matured through 2025–2026 alongside Gemini 3
(https://ainoya.dev/posts/antigravity-and-jules/), and Anthropic's own Agent SDK — which exposes the
internal harness behind Claude Code as a general-purpose library, now sitting under "Managed Agents"
with a scheduler and "rubric-based outcome grading" — shows the same assistant-to-agent-fleet
trajectory. OpenAI's Codex evolved similarly through 2025, adding AGENTS.md repo-configuration support,
MCP integration, and an open-source, provider-agnostic Agents SDK for building custom coding agents.
Collectively, the vendor roadmap evidence strongly supports the paper's premise that the industry
default is shifting toward code that is planned, written, reviewed and even deployed primarily by
agents, with humans in an increasingly supervisory/orchestration role.

### Competing visions about code itself

Karpathy's "Software 3.0" framing — Software 1.0 (human-written code), 2.0 (trained neural-network
weights), 3.0 (software specified via prompts/context/agents/tools, with "English as the hottest new
programming language") — is the primary articulation of the vision that code becomes a disposable,
regenerable intermediate representation rather than a durable, human-owned artifact
(https://singjupost.com/andrej-karpathys-software-is-changing-again/, June 2025 talk transcript). This
is in direct tension with Thoughtworks' Technology Radar Volume 34 (2026), which names the opposing
risk explicitly as **"cognitive debt"**: "accumulating cognitive debt as AI generates increasingly
larger amounts of code and, in so doing, introduces a wider gap between humans and software systems"
(https://www.thoughtworks.com/about-us/news/2026/combat-ai-cognitive-debt-radar-v34). Thoughtworks'
prescribed response is not to abandon human comprehension but to reinforce it — through "feedforward
controls like Agent Skills and spec-driven development" and "feedback controls like mutation
testing," plus a concrete accountability tool, "Git AI," which links every AI-written line of code
to the specific agent, model and prompt that produced it (https://www.thoughtworks.com/radar/tools/git-ai).
AWS's Kiro occupies the middle, hybrid position the research questions anticipated: specs and tests,
not code, become the durable artifact that humans own and review, with code treated as a compiled
output of that spec. Google's own Software Engineering at Google text is frequently invoked
(secondary sources) for the older, foundational position that "code is a liability" — a maintenance
burden regardless of who/what wrote it — which several practitioner sources use to argue AI-generated
code intensifies rather than removes the debt.

### Labour and skills direction

The Stanford Digital Economy Lab's "Canaries in the Coal Mine?" working paper (most recent public
update August 2026, using ADP payroll data covering 3.5–5 million workers/month through 2025) finds
employment for 22–25-year-olds in the most AI-exposed occupations — explicitly including software
development — running about 19% below where it would be absent AI, driven by reduced hiring of
juniors rather than increased layoffs of incumbents; workers aged 35–49 in the same occupations show
no comparable gap and even some growth
(https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/).
This is a mechanistically important data point for the paper's dependency thesis: if the pipeline of
junior engineers who would traditionally learn to read and maintain code is structurally shrinking,
the pool of humans capable of independently understanding AI-generated code also shrinks over time.
Challenger, Gray & Christmas's monthly job-cut reports corroborate a broader labour-market shift: AI
was cited in 101,743 US job-cut announcements through June 2026 (versus 54,836 for all of 2025) and
has led all layoff reasons for four-plus consecutive months in 2026
(https://www.challengergray.com/blog/challenger-report-layoffs-fall-hiring-picks-up-ai-leads-for-fifth-straight-month/),
with named company statements — Meta (~8,000 roles, citing AI automation including in engineering and
software testing), Salesforce's Benioff ("I need less heads," citing Agentforce), Microsoft (9,000
roles, AI absorbing workload), and Oracle's 10-K disclosure that "the adoption and deployment of AI
technologies across our operations have resulted... in reductions to our workforce" — providing
concrete, if heterogeneous, evidence that AI coding/agentic capability is already being cited as a
driver of headcount reduction (https://founderreports.com/ai-layoffs-tracker/). Challenger's own
caveat is important: "AI is shifting the labor market, it is not dismantling it," with hiring also up
25% year over year.

### Dependency/concentration risk as a strategic theme

Coding-agent market share is concentrated among a handful of vendors (Anthropic ~54%, OpenAI ~21% per
Menlo Ventures), and every major vendor publishes a model-deprecation lifecycle that customers do not
control: OpenAI commits to ≥6 months' notice for GA models, ≥3 months for specialized/codex variants,
but as little as 2 weeks for preview models (https://developers.openai.com/api/docs/deprecations);
Anthropic uses an analogous four-stage lifecycle (Active → Legacy → Deprecated → Retired) after which
API calls to a retired model fail outright (https://platform.claude.com/docs/en/about-claude/model-deprecations).
This is a structural, vendor-controlled dependency risk directly relevant to the paper's thesis: code
whose maintenance, extension, or even comprehension depends on invoking a specific model/agent is
exposed to that model's retirement schedule, pricing changes, or the vendor's own strategic pivots (as
the Windsurf case demonstrates for a downstream product). Secondary survey data (not independently
verified against a named primary survey; treat as indicative) suggests 81% of enterprise leaders are
concerned about AI vendor dependency but only 6% believe they could switch providers without material
disruption, with migration costs averaging an estimated $315,000 per project
(https://www.kusari.dev/blog/ai-coding-assistants-in-2026-4x-faster-10x-riskier-the-hidden-security-cost).

## Counter-evidence and caveats

- **Rising adoption, falling trust.** Stack Overflow's 2025 survey (49,000+ developers) found AI tool
  adoption climbing to 84% while trust in AI accuracy *fell* from 40% to 29%, with 45% citing
  "almost right, but not quite" output as their top frustration and 66% reporting more time spent
  fixing AI-introduced errors (https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/).
  This directly complicates any narrative of smooth, trust-based agent takeover — usage and
  confidence are decoupling, which if anything strengthens the "dependency without full
  understanding/trust" reading of the hypothesis, but weakens any strong-form "agents fully own the
  SDLC by consensus" claim.
- **AI as amplifier, not a uniform quality lever.** DORA's 2025 report (90% AI adoption, +14pp YoY)
  frames AI's primary effect as amplifying existing organizational strengths *and* dysfunctions —
  weak-process teams "ship low-quality work... only faster" — meaning the technical-debt/dependency
  risk described in the hypothesis is contingent on organizational maturity, not a universal outcome
  of AI coding adoption (https://dora.dev/dora-report-2025/).
  We could not extract DORA's numeric findings on trust/code-review burden directly (the primary
  report page is a navigation hub, not the full text); the more granular claims should be re-verified
  against the full PDF for the final paper.
  
- **Gartner's project-cancellation forecast is a governance story, not a code-comprehension story.**
  The stated reasons for the 40%-cancellation prediction are cost, unclear ROI and inadequate risk
  controls — not that the resulting code is unreadable or unmaintainable. The paper should not
  over-read this figure as direct evidence for the "code few humans understand" hypothesis.
- **Octoverse's data gap.** GitHub's own Octoverse 2025 report, despite extensive AI-adoption
  metrics, does not disclose what percentage of code merged on the platform is AI-written or what
  fraction receives full human review before merge — a first-party source that could have settled
  part of the hypothesis directly declines to report the most relevant number.
- **Inconsistent adoption percentages across Gartner citations (70/75/90% by 2028)** were found
  across different secondary sources citing Gartner, without a single authoritative primary figure
  confirmed — flagged rather than resolved.
- **Private-company revenue and valuation figures** (Claude Code's $8B run-rate, Cursor's $60B
  valuation, Cursor's ARR trajectory) come from press aggregation of company statements, not audited
  filings, and should be treated as directionally indicative rather than precise.
- **The 81%-vendor-dependency-concern and $315K-migration-cost figures** could not be traced to a
  named primary survey and are marked UNVERIFIED.
- **The IDC "40% of G2000 jobs" and "70% of CEOs" figures** were found only in secondary aggregation
  and could not be verified against a primary IDC publication; marked UNVERIFIED.

## Gaps and open questions

- No primary-source figure was found that directly quantifies "how much production code currently in
  active enterprise use was originally AI-generated and has never been read end-to-end by a human" —
  this is the crux of the paper's hypothesis and remains an inferred, not directly measured, gap
  across every source examined (including Octoverse, which is the most likely place to find it and
  does not report it).
- The Gartner "Predicts 2026" report (source of the 2,500%-defect-increase and cost-overrun figures)
  is paywalled; all figures here come from a single secondary summary (ArmorCode) and should be
  cross-checked against at least one more secondary citation or a purchased/library copy of the
  original report before being treated as final.
- DORA 2025's full report (not just its landing page) likely contains more granular data on
  code-review burden, defect rates, and stability trade-offs tied to AI adoption; worth a follow-up
  fetch of the full PDF.
- IDC's specific 2026 predictions on agentic AI job displacement need a primary citation.
- No source quantified the *rate* at which coding-agent models are actually deprecated in practice
  (as opposed to the policy notice periods) — i.e., how often has a customer's agent-authored/agent-
  dependent codebase actually broken due to a model retirement event. This would be strong direct
  evidence for the dependency-risk theme and was not found in the time available.
- The "10x team"/team-size-reduction narrative is well-represented in practitioner blogs and
  commentary but thin on rigorous, methodologically transparent data; the one study-like figure found
  (PR throughput up 7.76% against a 65% rise in AI usage across 400 companies) was reported only in
  secondary aggregation without a traceable primary study and should be independently verified or
  dropped.
- Given the six-stream split, this stream did not independently verify the underlying empirical
  claims behind Gartner's defect/cost forecasts (methodology, sample, survey population) — those
  would sit more naturally in Stream(s) covering direct code-quality/defect measurement; flagging for
  cross-stream reconciliation.
