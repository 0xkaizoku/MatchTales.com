# AGENTS.md

Welcome, AI Coding Agent! This file outlines the architecture, tech stack, rules, and guidelines for **MatchTales** to help you understand the codebase and make consistent, high-quality contributions.

---

## 1. Project Overview

**MatchTales** is a story-centric web platform. It began as the narrative layer on the **2026 FIFA World Cup** and now covers soccer, tennis, golf, American football, basketball and Formula 1 with the same question: why does this one matter?
*   **"Why Care" Scores & Reasons:** Editorial assessments of match, round and race stakes.
*   **Narrative Stories:** Previews and write-ups locked to named sources. No invented scorers.
*   **World Cup Archive:** 48 teams, 12 groups, completed 19 July 2026. Spain are champions.
*   **Sport desks:** mosaic at `/sports`. Unique boards at `/sport/tennis`, `/sport/football`, `/sport/f1`, `/sport/soccer`, `/sport/golf`, `/sport/basketball`. Soccer is one desk, not the default.
*   **Interactive Features:** Community hype walls, live second-screen companionship, newsletter subscriptions.
*   **Site clock:** editorial today is `2026-10-08` in `frontend/src/data/sports.ts` (`SITE_TODAY`). Football: TNF is Buccaneers (0-4) at Cowboys (2-2), 8:15 p.m. ET, AT&T Stadium, no score. Chiefs, Vikings and 49ers are 4-0. Chiefs are on a bye after 30-27 at the Raiders. Falcons (2-2) host the Ravens Sunday, not TNF. Soccer: Nations League window is closed. Spain and Portugal are through on 12. France 4-1 Belgium, Italy 3-1 Turkiye, England 3-0 Czechia, Croatia 1-2 Spain. Premier League still City 15 from five. Basketball: semis are 1-0. Dream 92-82 Liberty, Valkyries 71-60 Aces. Game 2 on 7 October has no verified final. Tennis: Shanghai first round is open. Ten Wednesday results are in. Djokovic beat de Minaur in Beijing. Alcaraz beat Lehecka in Tokyo. Seeds have not played in Shanghai. Golf: Baycurrent Classic first tee at Yokohama, par 71, no round score. F1: Singapore sprint weekend 9-11 October is next. Antonelli 320, Russell 236. Verstappen won at Sepang on 4 October. Do not print a Singapore result or an Austin grid penalty.

---

## 2. Architecture & Tech Stack

The project is split into two main directories:

### Frontend (`/frontend`)
*   **Framework:** Astro 6.x (Static-first build with islands where interactive components are needed).
*   **Styling:** Tailwind CSS (Vanilla CSS & Tailwind config).
*   **Data Layer:** Seed data loaded from `src/data/seed.json`.
*   **Astro Content Collections:**
    *   `matches` (`src/content/matches/*.json`): Event JSON (World Cup plus other sports). Optional `sport`, `competition`, `format`, `sources`, `leaderboard`, `tennisSets`.
    *   `teams` (`src/content/teams/*.json`): Dossiers for the 48 World Cup countries.
    *   `stories` (`src/content/stories/*.md`): Markdown blogs. Optional `sport`, `sources`, `relatedSlug`. No em-dashes. No invented stats.
*   **Flag Rendering Utility:** `getFlagUrl(code)` in [site.ts](file:///frontend/src/lib/site.ts) maps FIFA country codes to FlagCDN images (e.g., `gb-eng` for England, `gb-sct` for Scotland). Do **NOT** use raw system emojis for flags, as they fail to render on many platforms (e.g., Windows).

### Backend (`/backend`)
*   **Framework:** FastAPI (Python 3.10+).
*   **Database:** MongoDB (persists newsletter signups, hype notes, and votes).
*   **Data Scripts:** 
    *   `backend/scripts/build_seed.py`: Builds the core database of 48 teams, 12 groups, and 72 matches.
    *   `backend/scripts/generate_real_world_content.py`: Content compiler that builds the JSON dossiers, match metadata, and long-form markdown stories.

---

## 3. Directory Layout

```
.
├── backend/
│   ├── app/                # FastAPI application endpoints
│   ├── scripts/            # Seed data and content generation python scripts
│   └── tests/              # Python test suite
└── frontend/
    ├── public/             # Static public assets
    └── src/
        ├── components/     # Astro / React UI components
        ├── content/        # Markdown/JSON collection sources (generated)
        ├── data/           # seed.json (generated from python backend scripts)
        ├── layouts/        # Layout templates
        ├── lib/            # Utilities, API clients, and site config (site.ts)
        └── pages/          # Astro pages/routing (static & dynamic [slug] pages)
```

---

## 4. Coding Standards & Guidelines

When modifying or expanding the codebase, you **must** adhere to the following rules:

### ⚠️ Content Rules
*   **No Em-dashes (`—`) or Double-hyphens (`--`):** In any generated match story or markdown file, avoid em-dashes or double-hyphens to comply with strict style linting rules. Use a standard dash (`-`) or colons instead.
*   **World Cup Accuracy:** Group allocations and qualified teams must strictly mirror the official 2026 FIFA World Cup draw (completed on December 5, 2025). This comprises 48 teams across 12 groups (A through L).

### 🎨 Visual & Styling Standards
*   **Use Rich Aesthetics:** Apply premium color palettes, smooth hover effects, micro-animations, and harmonized dark modes.
*   **No Default Emojis for Flags:** Always render flags using the `getFlagUrl` utility imported from `src/lib/site.ts`:
    ```astro
    import { getFlagUrl } from '../lib/site';
    <img src={getFlagUrl(team.code)} alt={team.name} class="w-6 h-4" loading="lazy" />
    ```
*   **Responsive Layouts:** Ensure all page headers, grid systems, and list views render correctly on both desktop viewports and mobile screens.

### ⚙️ Development Workflows
1.  **Regenerating Content:**
    If you modify team data or fixture algorithms, run the Python build pipeline:
    ```bash
    python backend/scripts/generate_real_world_content.py
    ```
2.  **Building the Frontend:**
    Always verify that the static Astro pages build correctly:
    ```bash
    cd frontend
    npm run build
    ```
3.  **Local Dev Server:**
    To run the Astro dev environment locally:
    ```bash
    cd frontend
    npm run dev
    ```
