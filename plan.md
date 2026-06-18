# MatchTales — Development Plan (Astro + FastAPI/Mongo)

## 1) Objectives
- Ship a **lightweight, SEO-dominant AstroJS site** for WC2026 storytelling: “why this match matters” narratives, hype scores, fun facts, team/group deep dives, shareable match/story cards.
- Prove the **core workflow** works end-to-end: (1) Football-Data.org fetch (supplemental live widget) + (2) Claude narrative generation (build-time, human-sounding) + (3) persistence for newsletter/hype notes via FastAPI+Mongo.
- Deliver a **Vercel-ready** static-first build with islands only where needed (live widgets, filters, search, second-screen mode).

**Status update (as of current iteration):**
- ✅ Phase 1 (POC) complete
- ✅ Phase 2 (V1 full build) complete
- ✅ Testing complete: backend **14/14**, frontend **all critical features**, **0 bugs**
- ✅ Production build: **108 pages** + **sitemap-index.xml** (Vercel-ready)

---

## 2) Implementation Steps

### Phase 1 — Core POC (isolation; do not proceed until passing)
**User stories**
1. As a user, I want to see a single match card with a believable “Why Care” story so I trust the site.
2. As a user, I want hype score + 3 fun facts to quickly decide what to watch.
3. As a user, I want the site to pull at least one real competition list from Football-Data so I believe it’s connected to live football.
4. As a user, I want newsletter signup to store my email so I can get updates.
5. As a user, I want to submit a hype note and see it appear in a list so the community feels alive.

**Steps**
1. Add backend env: `EMERGENT_LLM_KEY=...` (use provided universal key) and `FOOTBALL_DATA_API_KEY=...`.
2. Create `/app/backend/scripts/poc_core.py` that:
   - Calls Football-Data.org with `X-Auth-Token` and prints sample competition fields.
   - Calls Claude via `emergentintegrations` using model `anthropic/claude-sonnet-4-6` and generates **one** WC2026 match story JSON.
   - Prints result and validates schema (basic checks; fail loudly).
3. Create minimal FastAPI endpoints + Mongo persistence:
   - `POST /api/newsletter`
   - `POST /api/hype-notes`
   - `GET /api/hype-notes?limit=20`
4. Run POC script + hit endpoints with curl; iterate prompts until output feels human/non-AI.

**Exit criteria (must pass)**
- Football-Data request succeeds (200) and prints parsed fields.
- Claude generation returns valid JSON with believable prose.
- Newsletter + hype-note persists to Mongo and reads back.

**Status:** ✅ Completed
- Football-Data proxy validated with key.
- Claude storytelling validated (human, editorial tone).
- Backend persistence validated.

---

### Phase 2 — V1 App Development (Astro site + core pages)
**User stories**
1. As a user, I want a fast homepage showing today/upcoming matches with hype scores.
2. As a user, I want to open a match page and instantly understand context, stakes, and rivalry.
3. As a user, I want to browse fixtures by date/group/team with minimal friction.
4. As a user, I want to explore a team page with history, key players, and storyline.
5. As a user, I want to submit a hype note/newsletter from any page and get a clear success/error state.

**Steps**
1. Replace `/app/frontend` with Astro (Node 22 + Astro 6) + Tailwind integration; set `yarn start` to `astro dev --host 0.0.0.0 --port 3000`.
2. Add `PUBLIC_BACKEND_URL` to `frontend/.env` (keep existing `REACT_APP_BACKEND_URL` untouched).
3. Create **seed data**: 48 teams, 12 groups (A–L), fixtures/results (week 1 + marquee MD2 + one LIVE), rivalries, iconic moments, player arcs.
4. Set up Astro **Content Collections**:
   - `matches` (JSON generated)
   - `teams` (JSON generated dossiers)
   - `stories` (Markdown long-form)
5. Build `generate_content.py` (build-time) to enrich seed with Claude narratives and write into:
   - `src/content/matches/*.json`
   - `src/content/teams/*.json`
   - `src/content/stories/*.md`
6. Core pages (static-first, JS only where needed):
   - `/` Home: hero (featured match), upcoming carousel, trending stories, group standings widget, live-scores widget, hype wall, newsletter
   - `/fixtures`: filters (group/team/status) + spoiler-free toggle
   - `/match/[slug]`: rich narrative, stakes, rivalry angle, key players, fun facts, head-to-head, share button, match-specific hype notes
   - `/teams` + `/team/[slug]`
   - `/groups` + `/group/[group]`
   - `/stories` hub + `/stories/[slug]`
   - `/live`: second-screen mode (hype meter, simulated commentary feed, poll)
   - `/about`, `/privacy`, custom `/404`
7. UI system: Tailwind token-based theme, dark/light toggle, accessible nav + mobile bottom nav, card components; minimal JS.
8. SEO infra:
   - canonical URLs, meta tags, OG/Twitter
   - JSON-LD schema.org (WebSite/SearchAction, SportsEvent, Article)
   - `@astrojs/sitemap` (`sitemap-index.xml` at build)
   - `robots.txt`, PWA manifest, favicon, default OG image
9. Vercel readiness:
   - `vercel.json` (security + caching headers, redirects, clean URLs)
   - Production build verification (`astro build`) and route health checks
10. End-to-end tests for all core flows.

**Exit criteria**
- All pages render with seeded WC2026 content; fast static-first architecture.
- Forms work against backend and show robust error handling.
- Live scores widget pulls server-side proxied data.

**Status:** ✅ Completed
- Astro 6 + Tailwind running on :3000 via `yarn start`.
- Seed dataset built: 48 teams, 12 groups, 35 fixtures, 4 rivalries, 6 moments, 4 story metas.
- Claude-generated content committed: 35 match packages, 48 team dossiers, 4 long-form articles.
- Backend endpoints shipped: newsletter, hype-notes (+filter +like), live-scores proxy, poll.
- SEO shipped: meta/OG/Twitter, schema, canonicals, robots, manifest, sitemap at build.
- Vercel-ready: `vercel.json`, clean URLs, production build success (108 pages).
- Testing: ✅ 100% pass (backend 14/14, frontend all features).

---

### Phase 3 — Expansion (quality + virality + polish) *(optional; do only if requested)*
**User stories**
1. As a user, I want shareable match/story cards that look great in WhatsApp/Twitter previews.
2. As a user, I want an even richer on-site search across matches/teams/stories.
3. As a user, I want standings and “tournament state” summaries to update easily as MD2/MD3 completes.
4. As a user, I want second-screen mode to feel even more like a companion (more polls, better live data, more interaction).
5. As a user, I want stronger trust signals and moderation workflows for user content.

**Steps (backlog / polish)**
1. **Per-match/per-story OG images** (build-time generation; 1200×630 templates) and wire to each page.
2. Expand search:
   - highlight matched terms
   - add keyboard selection (↑/↓ + Enter)
   - add filters (Teams/Matches/Stories)
3. Expand seeded tournament coverage:
   - add MD3 fixtures/results
   - add knockout bracket placeholders + story scaffolding
4. PWA enhancement:
   - optional service worker caching strategy (keep lightweight)
   - install prompt + offline-friendly essentials
5. Community safety:
   - moderation queue (approved=false by default)
   - basic rate limiting / IP-based throttling for hype notes
6. Content polish:
   - prompt refinement + editorial guardrails
   - add more rivalries, legends, underdog arcs

**Exit criteria**
- Share previews are unique per match/story.
- Search feels instant and keyboard-friendly.
- Content can scale through the rest of the tournament with minimal manual effort.
- Community features remain safe and spam-resistant.

---

## 3) Next Actions (immediate)
- ✅ None required for V1 delivery — Phase 1 and Phase 2 are complete and tested.
- If you want Phase 3 polish, choose priorities:
  1) per-match OG images, 2) MD3 + knockout expansion, 3) PWA/service worker, 4) moderation/rate limiting, 5) richer live mode.

---

## 4) Success Criteria
- ✅ **POC:** Football-Data fetch works; Claude story JSON is human-sounding; newsletter/hype notes persist.
- ✅ **V1:** Astro site has homepage/fixtures/match/team/group/story/live pages with seeded WC2026 content; forms work; fast + accessible.
- ✅ **SEO:** Correct meta/OG/schema/canonicals + robots + sitemap at build; share previews have default OG.
- ✅ **Performance:** Static-first pages, minimal hydration, optimized assets, strong CWV.
- (Optional) **Phase 3:** per-page OG images, expanded tournament content, PWA caching, moderation safeguards.
