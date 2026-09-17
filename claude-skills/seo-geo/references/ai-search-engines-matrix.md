# AI Search Engines & Answer Engines Comparison Matrix

Generative and answer engines differ significantly in index sources, crawler rules,
extraction windows, and citation behavior.

## Platform Breakdown (2026)

| Platform | Crawlers | Underlying Index | Key Citation Triggers | Primary Authority Bias |
|----------|----------|------------------|-----------------------|------------------------|
| **ChatGPT Search** | `OAI-SearchBot` (Search), `GPTBot` (Training) | Bing Search + Direct OAI Crawl | Answer capsules, table data, review recency | Neutral/editorial, G2/Capterra, fresh news |
| **Perplexity AI** | `PerplexityBot` | Bing + Google + Perplexity Sonar Index | Exact stat matches, domain authority, Reddit | Wikipedia, Reddit, academic/primary sources |
| **Google AI Overviews / AI Mode** | `Googlebot` (Search), `Google-Extended` (Gemini Training) | Google Search Index | Multi-source corroboration, E-E-A-T, schema | Primary reporting ("Highly Cited"), Preferred Sources |
| **Claude Search** | `Claude-SearchBot` (Search), `ClaudeBot` (Training) | Brave Search + Web Fetch | High semantic density, logical coherence, balanced pros/cons | Documentation, technical authorities, neutral blogs |
| **Microsoft Copilot** | `Bingbot` | Bing Search Index | Schema.org markup, IndexNow freshness, Bing DA | Microsoft ecosystem, LinkedIn, MSN partners |

## Crawler Governance & Permissions

### Rule 1: Training Bots vs Search Bots
- Blocking `GPTBot` stops model training but **allows** ChatGPT Search via `OAI-SearchBot`.
- Blocking `ClaudeBot` stops training but **allows** Claude search via `Claude-SearchBot`.
- Blocking `Google-Extended` stops Gemini/Vertex training but **never** blocks Google AI Overviews or Search.

### Robots.txt Best Practice for AI Visibility
```
User-agent: OAI-SearchBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Googlebot
Allow: /
```

## Citation Mechanics by Platform

### Perplexity AI
- Uses dense semantic vector search across cached documents.
- Favors pages with self-contained passages (130-170 words).
- Frequently cites Reddit and forum threads for anecdotal validation.

### ChatGPT Search
- Leverages synthetic answer synthesis with inline numerical citation pills.
- Prioritizes structured comparison tables when comparing tools or services.
- Requires pricing and product specs to be explicitly anchored with update dates.

### Google AI Overviews
- Governed by standard Google Search directives (`nosnippet`, `data-nosnippet`, `max-snippet`).
- "Preferred Sources" feature enables user-level source prioritization.
- Surfaces "Highly Cited" tags for original primary reporting that others reference.
