# Common instructions included in every research subagent prompt

**What is happening:** The orchestrating session is researching the hypothesis that AI-generated
code (from Microsoft/GitHub, AWS, Anthropic, Cursor, OpenAI and similar tools) is becoming a new
form of technical debt: code that few humans, or only coding models, understand, creating a
dependency on the coding harness/model that produced it. The research is split into six parallel
streams. This file holds the instructions that are prepended to every stream prompt.

Today's date is 2026-09-12. Prefer sources from 2024-2026 but include foundational earlier work.

## Rules
1. Use WebSearch to find candidate sources and WebFetch to read them. Read the actual source
   before citing it. Do not cite from memory alone.
2. EVERY claim must carry a URL. If you cannot fetch/verify a URL, mark the claim `UNVERIFIED`.
   Never invent URLs, paper titles, statistics or quotes.
3. Distinguish evidence types: peer-reviewed paper / preprint (arXiv etc.) / industry study with
   methodology / analyst report / vendor blog or press release / survey / news article / opinion.
4. Record for every source: title, author or organisation, date, URL, evidence type, and a
   1-2 sentence note with the specific finding or number (quote briefly where useful).
5. Actively look for counter-evidence that weakens the hypothesis, not just support.
6. Be precise with numbers: report the exact figure, population, and time window as the source
   states it.
7. Aim for 12-25 high-quality sources for your stream. Quality over quantity.

## Output
Write your full findings as a markdown file to the exact path given in your stream prompt, with
these sections:
1. `## Stream summary` - 200-400 words: what the evidence says relative to the hypothesis.
2. `## Evidence table` - a markdown table with columns:
   `# | Claim (one sentence) | Source title | Author/Org | Date | Type | Strength (High/Med/Low) | URL | Note`
3. `## Detailed findings` - narrative grouped by theme, citing sources with inline URLs.
4. `## Counter-evidence and caveats`
5. `## Gaps and open questions`
Then reply with a 150-word summary of what you found and the path you wrote to.
