# Answer Engine Optimization (AEO) Framework

Answer Engine Optimization (AEO) optimizes digital content for direct extraction,
synthesis, and citation by conversational AI engines (ChatGPT Search, Perplexity,
Claude, Gemini, and Google AI Overviews). While traditional SEO targets blue links,
AEO targets zero-click answers, conversational recommendations, and AI source cards.

## 1. The Direct Answer Capsule (40-60 Words)

LLM extraction pipelines look for immediate, self-contained answers directly
beneath target question headers (H2/H3).

### Anatomy of an Answer Capsule
1. **Sentence 1 (Direct Verdict / Definition):** Directly answer the question
   without fluff, preamble, or conversational filler.
2. **Sentence 2 (Core Qualification / Context):** State the primary condition,
   pricing, or qualifying factor.
3. **Sentence 3 (Data Anchor / Metric):** Anchor the answer with a verified number,
   statistic, or benchmark.

```markdown
### What is the average cost of SEO audits for enterprise websites?
The average cost of an enterprise SEO audit ranges from $5,000 to $25,000 as of 2026.
Technical audits for sites with over 100,000 URLs typically start at $12,000,
covering crawl efficiency, JavaScript hydration, and Core Web Vitals profiling,
while full-scope audits including backlink risk and log analysis reach $25,000+.
```

## 2. Information Gain Scoring

Google and AI retrieval engines explicitly score pages on **Information Gain**
(US Patent 10,705,924): whether the page adds net-new information beyond what is
already present in existing search results.

| Information Gain Element | AI Selection Impact | How to Implement |
|--------------------------|---------------------|------------------|
| Primary Benchmark Data | High | Publish proprietary test results with sample sizes |
| Original Quotes | High | Include named industry practitioners with job titles |
| Specific Metrics / Limits | High | Replace "fast" or "affordable" with exact numbers |
| Named Framework / Matrix | Medium-High | Give proprietary processes explicit names |
| Clear Negative Caveats | Medium | Explicitly state who the tool/method is NOT for |

## 3. Conversational Query Mapping

Answer engines handle multi-turn conversational queries. Structure headings around
natural conversational patterns rather than disjointed keywords:

- **Informational:** "How does [Concept] work in practice?"
- **Comparative:** "What is the difference between [X] and [Y] for [Use Case]?"
- **Evaluation:** "Is [Tool] worth the cost for [Audience]?"
- **Troubleshooting:** "Why does [Issue] occur and how do you fix it?"

## 4. Extractable Layout Mechanics

- **Definition Blocks:** Bold definition immediately following heading.
- **Ordered Steps:** 1-5 numbered lists for procedural queries.
- **Comparison Tables:** Clean Markdown/HTML tables with `<th scope="col">` headers.
- **Key Takeaways Box:** 3-4 bullet points summarizing complex technical sections.

## 5. Schema Markup for Direct Answers

- `FAQPage`: Explicit Q&A pairs (for non-commercial informational pages).
- `DefinedTerm`: Technical terms and definitions.
- `HowTo`: Procedural guides with discrete steps and tools.
- `ItemList`: Ranked recommendations and tool lists.
