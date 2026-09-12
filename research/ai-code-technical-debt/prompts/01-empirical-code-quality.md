# Stream 1 - Empirical evidence on quality, maintainability and churn of AI-generated code

**What is happening:** This stream gathers the quantitative/academic evidence for and against
the claim that AI-assisted coding increases technical debt (duplication, churn, complexity,
maintainability decline, defect rates, review burden).

## Research questions
- What do longitudinal repository studies show about code churn, duplication ("copy/paste" vs
  "moved" code), and refactoring rates since Copilot/ChatGPT adoption? (e.g. GitClear 2024 and
  2025 "AI Copilot Code Quality" reports; any 2026 follow-ups.)
- What do controlled studies say about developer productivity vs. quality? (METR 2025 RCT on
  experienced open-source developers; Uplevel study on bug rates; Google/Microsoft internal
  studies; GitHub's own RCTs; Cui et al. field experiments at Microsoft/Accenture; Faros AI or
  similar telemetry studies; DORA 2024/2025 reports on AI adoption vs delivery stability and
  throughput.)
- Academic work on maintainability, code smells, complexity and "comprehensibility" of LLM code
  (arXiv / ICSE / FSE / MSR / TOSEM papers 2023-2026; e.g. studies of Copilot-generated code
  smells, "self-admitted technical debt" in AI code, PR acceptance rates for AI agent PRs such
  as the AIDev dataset of agent-authored pull requests).
- Evidence about review load: are humans reviewing less as volume increases? Any data on PR
  size, review time, or "rubber-stamp" approval of AI PRs.
- Any data quantifying "technical debt" directly attributed to AI (e.g. SonarSource, CodeScene,
  Qodo, Sonar "State of Code" reports, Stack Overflow developer survey trust figures).

Include the sample sizes, effect sizes and methodology caveats. Highlight where vendor-funded
studies conflict with independent ones.

## Output path
Write to: /home/user/demodhruv/research/ai-code-technical-debt/outputs/01-empirical-code-quality.md
