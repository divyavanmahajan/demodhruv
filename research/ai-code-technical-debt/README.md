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
| 4 | Every claim used in the paper was collected into `claims.json` (129 claims, graded), from which the paper's reference list, the markdown table and the published artifact are all generated. | `claims.json`, `claims-and-sources.md`, `claims-and-sources.html` |

## Layout

```
research/ai-code-technical-debt/
  README.md                               this file
  prompts/                                exact prompts given to each subagent
  outputs/                                raw subagent outputs (unedited)
  claims.json                             single source of truth: 129 graded claims with URLs
  build_docx.js, docx_helpers.js          docx-js script that generates the paper from claims.json
  build_claims_html.js                    generates the claims-table artifact from claims.json
  AI_Generated_Code_Technical_Debt.docx   the research paper (all links inline, references by theme)
  claims-and-sources.md                   claims table as markdown
  claims-and-sources.html                 claims table as the published artifact
```

## Rebuilding

```
npm install docx@9            # or set NODE_PATH to a directory that has it
node build_docx.js            # -> AI_Generated_Code_Technical_Debt.docx
node build_claims_html.js     # -> claims-and-sources.html
```

## Verification notes

- The docx passes the OOXML schema validator (364 paragraphs, all validations passed).
- LibreOffice in the build container could not load any file, so the rendered layout was not visually
  checked; structure was verified with python-docx (headings, tables, hyperlink count).
- Secondary-sourced figures that could not be confirmed against a primary are marked UNVERIFIED in
  `claims.json` and discussed in Section 8.3 of the paper.
