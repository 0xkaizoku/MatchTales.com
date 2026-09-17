---
name: seo-competitor-pages
description: >
  Generate and audit SEO- and AEO-optimized competitor comparison and alternatives pages.
  Covers "X vs Y" head-to-head layouts, "Best [Category] Tools" roundups, "Alternatives to X" pages,
  feature matrices, schema markup, conversion optimization, and Answer Engine extractability.
  Use when user says "comparison page", "vs page", "alternatives page", "competitor comparison",
  "X vs Y", "versus", "best tools", "top software", or "compare tools".
user-invocable: true
argument-hint: "[url or generate] [competitor or category]"
license: MIT
metadata:
  author: AgriciDaniel
  version: "2.3.1"
  category: seo
---

# Competitor Comparison, Alternatives & Best-Tools Pages

Create high-converting, authoritative comparison and roundup pages that rank in search engines
and get cited by Answer Engines (ChatGPT Search, Perplexity, Claude, Google AI Overviews).

## Reference Guides
- Read `references/tool-comparison-architecture.md` for 1v1 head-to-head blueprints.
- Read `references/best-tools-roundup-guide.md` for "Best Tools in 2026" roundup structures.
- Read `references/aeo-geo-comparison-optimization.md` for Answer Engine citation mechanics.
- Read `references/comparison-schema-templates.md` for JSON-LD schema templates.

---

## Core Page Formats

### 1. "X vs Y" Head-to-Head Comparisons
- Target keyword: `[Tool A] vs [Tool B]`
- **Above-Fold Verdict Capsule (50-70 words):** Unambiguous summary stating which tool to choose under what condition.
- **Quick Decision Box:** "Choose Tool A if [X]; Choose Tool B if [Y]."
- **Feature Matrix:** Side-by-side comparison table with quantitative limits (not just checkmarks).
- **Category Deep Dives:** Dedicated sections for Usability, Features, Integrations, Pricing, and Support.
- **Winner Badges:** Explicit category winner declarations.

### 2. "Best [Category] Tools" Roundups
- Target keyword: `best [category] tools [year]`, `top [category] software`
- **Methodology Disclosure:** Testing hours, criteria, account tiers, and team credentials.
- **Top Picks Summary Table:** Placed immediately below methodology for zero-click and AEO extraction.
- **Standardized Review Cards:** Consistent layout for each tool:
  - Heading: `## [Rank]. [Tool] -- Best For [Persona/Use Case]`
  - Quick Verdict (Answer Capsule)
  - Key Specs, Pros (with evidence), Cons (dealbreakers), and Hands-on Experience.
- **Buyer's Decision Guide:** Framework for assessing team requirements and budget.

### 3. "Alternatives to [Tool]" Pages
- Target keyword: `[Tool] alternatives`, `best alternatives to [Tool]`
- Categorized alternatives: Budget/Free, Enterprise, Simple/Modern, and Specialized.
- Direct migration guidance (export/import ease, switching downtime).

---

## AEO & Answer Engine Citability Rules

When users ask conversational AI engines *"What is the best [tool] for [use case]?"*:
1. **The "Best For" Hook:** Always append an explicit `Best For [Persona]` hook to each tool heading.
   AI models match user query constraints directly to these labels.
2. **Semantic HTML Tables:** Use `<table` or clean Markdown tables with `<th scope="col">` and `<th scope="row">`.
   Never embed tables inside images.
3. **Quantitative Metrics:** State exact limits (e.g. "500 MB storage", "Up to 5 seats", "$49/mo") rather than vague adjectives ("generous", "affordable").
4. **Freshness Date Anchors:** State "Pricing verified: [Month Year]" to retain recency citation score.

---

## Automated Audit Tool

Run the comparison auditor on any live URL or local draft:
```bash
"${CLAUDE_PLUGIN_ROOT}/scripts/claude-seo" run tool_comparison_check.py <url-or-file> --json
```

The script evaluates:
- Page intent detection (1v1, roundup, alternatives)
- Feature matrix quality and quantitative metric density
- AEO extractability and verdict capsule presence
- Balance and neutrality (pros/cons distribution)
- Pricing transparency and freshness date anchors
- Schema.org markup (`SoftwareApplication`, `ItemList`, `FAQPage`)

---

## Schema Markup Architecture

- **Roundups:** Use `ItemList` schema with nested `SoftwareApplication` or `Product` elements including `offers` and `aggregateRating`.
- **Head-to-Head Comparisons:** Use `FAQPage` answering direct comparison queries ("Is Tool A cheaper than Tool B?").
- Full templates: see `references/comparison-schema-templates.md`.
