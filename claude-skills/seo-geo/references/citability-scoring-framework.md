# Passage-Level Citability Scoring Framework

Answer engines evaluate passages in chunks. A passage with high citability can be
extracted and understood in isolation without requiring surrounding page context.

## The 5 Pillars of Citability

### 1. Optimal Passage Window (134-167 Words)
- Research across 1.3M AI citations demonstrates that passages between **134 and 167 words**
  achieve the highest citation frequency in Google AI Overviews and ChatGPT Search.
- Shorter passages (<80 words) frequently lack sufficient context for standalone extraction.
- Longer passages (>250 words) get truncated or synthesized away.

### 2. Entity Disambiguation (Subject-Predicate-Object)
- Use explicit noun entities rather than vague pronouns ("it", "they", "this platform").
- Bad: "It offers automated daily reporting and costs $49/mo."
- Good: "Ahrefs offers automated daily reporting in its Standard Plan at $199 per month."

### 3. Data Anchoring & Verifiability
- Every claim must have a quantitative metric and an attribution anchor.
- Include publication or last-reviewed timestamps (`dateModified` in schema).
- Content under 3 months old is ~3x more likely to be cited than stale content (SE Ranking study).

### 4. Structural Isolation (Self-Contained Clarity)
- A human or AI reader should understand the passage if copied into an empty text file.
- Avoid cliffhanger introductions ("As we mentioned earlier...", "In the previous step...").

### 5. Multi-Modal Accompaniment
- Accompany core findings with structured data, markdown tables, or annotated diagrams.
- Pages with data tables and structured visual data show **156% higher citation rates**.

## Citability Scoring Matrix (0-100)

| Criterion | Target | Points |
|-----------|--------|--------|
| Target Word Window | 134-167 words in key answer block | 25 |
| Immediate Direct Answer | First sentence answers header directly | 20 |
| Quantitative Data Point | Verified number, pricing, or percentage | 20 |
| Explicit Entity Naming | Zero ambiguous pronouns in verdict sentence | 15 |
| Freshness Date Anchor | "Updated [Month Year]" or current year cited | 10 |
| Semantic Schema Support | FAQPage / Product / ItemList JSON-LD present | 10 |
