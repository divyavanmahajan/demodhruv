# Stream 4 - Security, reliability and incident evidence for AI-generated code

**What is happening:** This stream collects the security and reliability dimension of AI-generated
technical debt: vulnerability rates, supply-chain risks (hallucinated packages / slopsquatting),
and real incidents caused by loosely supervised agents.

## Research questions
- Vulnerability rates in AI-generated code: Veracode 2025 GenAI Code Security Report (share of
  AI code with OWASP top-10 flaws); Stanford "Do Users Write More Insecure Code with AI
  Assistants?" (Perry et al.); Snyk, GitGuardian (secrets leakage in Copilot-enabled repos),
  Apiiro 2025 study on AI-assisted developers producing more vulnerabilities; Sonar/SonarSource
  studies on LLM code; NYU Copilot security study (Pearce et al. 2021/2022) as baseline; any
  2026 updates.
- Supply chain: "slopsquatting" and package hallucination studies (Spracklen et al. 2025 USENIX),
  dependency bloat in AI code.
- Agent incidents: Replit agent deleting production DB (July 2025), Amazon Q Developer VS Code
  extension malicious prompt (July 2025), Google Gemini CLI deleting files, Claude Code / Cursor
  incidents reported publicly, "prompt injection" into coding agents (e.g. GitHub MCP, Copilot
  "CamoLeak"), CVEs in agent harnesses.
- Vendor and regulator responses: OWASP Top 10 for LLM applications and Agentic AI; NIST AI RMF
  generative AI profile; CISA/NSA guidance on AI-generated code (if any); EU Cyber Resilience
  Act implications; ENISA.
- Evidence on remediation cost: is AI-found/AI-written vulnerability volume outpacing remediation
  capacity ("security debt")? Veracode State of Software Security 2025/2026.

## Output path
Write to: /home/user/demodhruv/research/ai-code-technical-debt/outputs/04-security-and-incidents.md
