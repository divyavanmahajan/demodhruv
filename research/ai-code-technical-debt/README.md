# AI-Generated Code as the New Technical Debt - research package

Research date: 2026-09-12. Produced in a Claude Code session using six parallel research subagents
plus an orchestrating synthesis pass.

## Hypothesis under test

> Microsoft, AWS, Anthropic, Cursor, OpenAI and others now generate code with near-autonomous AI that
> is loosely managed by people. As adoption grows, the generated code becomes a new form of technical
> debt: code that is too complex, or that too few people (or only coding models) understand. This
> creates a dependency on the coding harness / coding model that produced it.

Three questions follow from it:
1. What does the research evidence say about this perceived increase in technical debt?
2. What is the strategic trend and direction?
3. What mitigations are being taken at a corporate level?

## Process (what happened, in order)

| Step | What happened | Where |
|---|---|---|
| 1 | The hypothesis was decomposed into six research streams. A common instruction block (citation rules, evidence typing, output format) was written once and prepended to each stream prompt. | `prompts/00-common-instructions.md`, `prompts/01..06-*.md` |
| 2 | Six subagents ran in parallel with web search/fetch. Stream 1 (empirical studies, where sample sizes and effect sizes matter) ran on Claude Opus; streams 2-6 (broader sweeps) ran on Claude Sonnet. Each wrote its findings, evidence table, counter-evidence and gaps to its own file. | `outputs/01..06-*.md` |
| 3 | The orchestrator read all six outputs, cross-checked overlapping claims, and wrote the synthesis as a research paper. | `AI_Generated_Code_Technical_Debt.docx` (built by `build_docx.js`) |
| 4 | Every claim used in the paper was collected into a claims-and-sources table and published as a separate artifact. | `claims-and-sources.md` (source of the artifact), `claims-and-sources.html` |

## Layout

```
research/ai-code-technical-debt/
  README.md                         this file
  prompts/                          exact prompts given to each subagent
  outputs/                          raw subagent outputs (unedited)
  build_docx.js                     docx-js script that generates the paper
  AI_Generated_Code_Technical_Debt.docx   the research paper (all links inline)
  claims-and-sources.md             claims table, one row per claim, with URL and evidence grade
  claims-and-sources.html           the same table as the published artifact
```
