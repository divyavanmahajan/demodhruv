# Stream 5 - Mitigations taken at a corporate / engineering-organisation level

**What is happening:** This stream catalogues what companies, standards bodies and tool vendors
are actually doing to manage the technical-debt and dependency risk of AI-generated code.

## Research questions
- Published corporate policies and engineering practices: Google's internal AI coding
  guidelines and "AI-assisted code review" practices; Microsoft/GitHub guidance on reviewing
  Copilot output; Amazon's policies; Meta; Shopify (Tobi Lütke's 2025 "AI is a baseline
  expectation" memo); Anthropic's own practices for Claude Code development; Thoughtworks
  Technology Radar advice (e.g. "complacency with AI-generated code", "AI-accelerated shadow
  IT", "spec-driven development"); DORA 2025 "AI Capabilities Model" (7 capabilities); Gartner
  or Forrester recommendations; McKinsey "tech debt" and AI guidance.
- Concrete controls: mandatory human review / code ownership rules (CODEOWNERS), AI-authored
  commit labelling and provenance (git trailers like Co-Authored-By, GitHub's agent attribution,
  SLSA / in-toto attestations, AI-BOM proposals), test-coverage gates, static analysis and
  "AI code quality gates" (SonarQube AI Code Assurance, CodeRabbit, Qodo, Snyk for AI code),
  architecture fitness functions, "spec-driven development" (AWS Kiro specs, GitHub Spec Kit),
  context-engineering files (AGENTS.md, CLAUDE.md, cursor rules) as documented architecture,
  limiting agent autonomy (permission modes, sandboxing), red-teaming of agents.
- Portability / anti-lock-in measures: AGENTS.md standard under the Agentic AI Foundation
  (Linux Foundation, Dec 2025), Model Context Protocol, multi-model strategies, open-source
  harnesses (OpenHands, Aider, Cline, Goose), enterprise contracts with multiple model vendors.
- Skills and organisation: training programmes, "AI-native" engineering role definitions,
  pairing rules, junior-developer hiring changes (evidence from Stanford Digital Economy Lab
  2025 study on entry-level employment; any 2026 follow-ups), changes to code review culture.
- Measurement: how companies measure AI-code quality (DORA metrics, SPACE, DX Core 4, "AI
  measurement framework" by DX/Abi Noda, GitHub Copilot metrics API), and evidence on whether
  the mitigations work.
- Standards and regulation: ISO/IEC 42001, NIST AI RMF, EU AI Act obligations relevant to
  software produced with AI, financial-regulator guidance (e.g. FINOS AI governance framework
  for banks), UK NCSC guidance.

## Output path
Write to: /home/user/demodhruv/research/ai-code-technical-debt/outputs/05-corporate-mitigations.md
