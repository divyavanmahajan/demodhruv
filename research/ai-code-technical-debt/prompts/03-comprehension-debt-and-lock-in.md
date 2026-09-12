# Stream 3 - Comprehension debt, skill atrophy, and dependency on the coding model/harness

**What is happening:** This stream examines the core mechanism of the hypothesis: code that
humans no longer understand ("comprehension debt"), erosion of developer skills, and the
resulting dependency on the specific coding model or harness (Claude Code, Codex, Cursor,
Copilot) that produced or can maintain the code.

## Research questions
- Concepts and framing: "comprehension debt", "cognitive debt", "vibe coding debt",
  "understanding debt", "AI-generated technical debt" - who coined them and what evidence do
  they cite? (e.g. essays by Simon Willison, Martin Fowler/Thoughtworks, Birgitta Böckeler,
  Kent Beck, Gergely Orosz/Pragmatic Engineer, Addy Osmani, Steve Yegge, Charity Majors,
  academic papers on "program comprehension" with LLMs.)
- Empirical evidence on skill erosion / deskilling: Microsoft Research + CMU 2025 study on
  critical thinking with GenAI (Lee et al.), MIT Media Lab "Your Brain on ChatGPT" (cognitive
  debt), studies of students learning with Copilot, Anthropic's 2026 study on AI assistance and
  skill formation among developers (if it exists - verify), "automation bias" and "ironies of
  automation" (Bainbridge 1983) applied to software.
- Evidence on ownership and bus-factor: does AI-generated code have identifiable owners? Any
  research on "orphaned" code, knowledge loss, or onboarding difficulty in AI-heavy codebases.
- Dependency/lock-in on the harness or model: does code produced by one model become harder for
  another model or for humans to maintain? Evidence of "model-specific" code styles, of
  companies standardising on one vendor's agent, of context files (CLAUDE.md, AGENTS.md,
  .cursorrules, copilot-instructions.md) becoming critical infrastructure; the AGENTS.md
  standardisation effort (OpenAI/Agentic AI Foundation) as a portability mitigation; pricing
  and rate-limit changes (Cursor pricing changes 2025, Anthropic Claude Code limits) as evidence
  of dependency risk; vendor outages affecting developer productivity.
- Counter-argument: "code is now cheap and disposable; regenerate rather than maintain" - who
  argues this and with what evidence? Also evidence that models are good at explaining and
  refactoring legacy code, which would reduce comprehension debt.

## Output path
Write to: /home/user/demodhruv/research/ai-code-technical-debt/outputs/03-comprehension-debt-and-lock-in.md
