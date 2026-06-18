# MatchTales ⚽ — Why This Match Matters

The **story layer** on top of the 2026 FIFA World Cup. While other apps show scores and lineups, MatchTales tells you *why you should care*: rivalries, player legacies, iconic moments, fun facts, and a **Why-Care score (0–10)** for every match — all written to feel human, not robotic.

Built with **AstroJS** (static-first, lightning fast, SEO-dominant) + **Tailwind CSS**, with a small **FastAPI + MongoDB** backend for newsletter, fan hype notes, live-score proxy and polls. AI narratives are pre-generated with **Claude** and committed as static content.

## Tech Stack
- **Frontend:** Astro 6 + Tailwind 3 (content collections, view transitions, zero-JS by default with tiny vanilla islands for interactivity)
- **Backend:** FastAPI + MongoDB (`/api` prefix)
- **Data:** Football-Data.org (live competitions widget) + curated WC2026 seed dataset
- **AI:** Claude (`claude-sonnet-4-6`) via Emergent LLM key — build-time story generation
- **Deploy:** Vercel-ready (`vercel.json`, clean URLs, caching + security headers, dynamic sitemap, robots.txt)

## Project Structure
```
frontend/
  astro.config.mjs        # Astro + Tailwind + Sitemap (site URL, dev on :3000)
  tailwind.config.mjs     # design tokens -> CSS variables (dark/light)
  vercel.json             # headers, cleanUrls, redirects
  src/
    data/seed.json        # canonical dataset (48 teams, 12 groups, fixtures, rivalries, moments)
    content/
      matches/*.json      # AI-generated match story packages
      stories/*.md        # AI-generated long-form articles
      teams/*.json        # AI-generated team dossiers
    content.config.ts     # content collection schemas (glob loaders)
    lib/site.ts           # helpers (Why-Care colors, dates, lookups)
    layouts/BaseLayout.astro
    components/            # Nav, Hero, MatchStoryCard, WhyCareMeter, GroupStandingsWidget, HypeNotes, LiveScores ...
    pages/                # index, fixtures, match/[slug], teams, team/[slug], groups, group/[group], stories, stories/[slug], live, about, privacy, 404, search-index.json
    styles/global.css
backend/
  server.py               # FastAPI: newsletter, hype-notes, live-scores, poll
  scripts/
    build_seed.py         # builds src/data/seed.json
    generate_content.py   # Claude -> content collections (idempotent)
    poc_core.py           # core integration POC
```

## Local Development
Services run under supervisor:
- Frontend: `yarn start` → `astro dev --host 0.0.0.0 --port 3000`
- Backend: `uvicorn server:app --port 8001`

```bash
# frontend
cd frontend && yarn install && yarn start
# backend
cd backend && pip install -r requirements.txt   # served by supervisor on :8001
```

### Environment
- `frontend/.env` → `PUBLIC_BACKEND_URL` (backend base for client calls)
- `backend/.env` → `MONGO_URL`, `DB_NAME`, `EMERGENT_LLM_KEY`, `FOOTBALL_DATA_API_KEY`

## Regenerating Content (AI)
```bash
cd backend
python3 scripts/build_seed.py                 # rebuild dataset
python3 scripts/generate_content.py            # generate all (skips existing)
python3 scripts/generate_content.py --only matches --force   # force re-gen matches
```
Prompt templates live in `generate_content.py` — edit the `VOICE` system prompt and per-type prompts to tune tone or add new fixtures.

## Deploying to Vercel
1. Push to GitHub.
2. Import the `frontend/` directory as an Astro project on Vercel (framework auto-detected).
3. Set env var `PUBLIC_BACKEND_URL` to your deployed backend URL.
4. `vercel.json` handles headers, clean URLs and redirects. `astro build` emits `sitemap-index.xml`.
5. Deploy the FastAPI backend separately (Render/Railway/Fly) with the same env vars.

## SEO
Per-page meta + Open Graph + Twitter cards, canonical URLs, JSON-LD schema (`SportsEvent` for matches, `Article` for stories, `WebSite` + `SearchAction` on home), build-time `sitemap-index.xml`, `robots.txt`, PWA manifest, custom football-themed 404.

---
*MatchTales is an independent fan project and is not affiliated with or endorsed by FIFA.*
