# AGENTS.md

Welcome, AI Coding Agent! This file outlines the architecture, tech stack, rules, and guidelines for **MatchTales** to help you understand the codebase and make consistent, high-quality contributions.

---

## 1. Project Overview

**MatchTales** is a story-centric web platform. It began as the narrative layer on the **2026 FIFA World Cup** and now covers soccer, tennis, golf, American football, basketball and Formula 1 with the same question: why does this one matter?
*   **"Why Care" Scores & Reasons:** Editorial assessments of match, round and race stakes.
*   **Narrative Stories:** Previews and write-ups locked to named sources. No invented scorers.
*   **World Cup Archive:** 48 teams, 12 groups, completed 19 July 2026. Spain are champions.
*   **Sport desks:** mosaic at `/sports`. Unique boards at `/sport/tennis`, `/sport/football`, `/sport/f1`, `/sport/soccer`, `/sport/golf`, `/sport/basketball`. Soccer is one desk, not the default.
*   **Site clock:** editorial today is `2026-11-14` in `frontend/src/data/sports.ts` (`SITE_TODAY`). Soccer: Thu UWCL Barcelona 1-1 Arsenal (Maanum 22, Graham Hansen 59); Nations League England 2-1 Croatia (Rogers 24, Kane 64 pen on cap 126), Italy 3-1 France (Pio Esposito 2), Czechia 0-2 Spain; Sunday Spain vs England 19:45 GMT Metropolitano; PL Arsenal 27, Brighton 22, Man City 21. Football: TNF Thu Commanders 24, Giants 21 (Daniels 3 TD, Diggs 32-yd at 0:57, Douglas INT; WSH 3-5-1, NYG 5-3-1); Saturday 14 Nov has no NFL game; Sunday Munich Patriots vs Lions 9:30 a.m. ET FOX unpublished. Basketball: Fri Spurs 123-85 Warriors (Castle 32, Wemby 12/12/6, 11th straight, 11-2; Curry out oblique); Thu Pistons 144-140 2OT Wizards (Cunningham 52); Saturday 5 NBA games upcoming. Golf: Dubai R2 complete AP: McIlroy and Hatton -5 (139), Luiten and Reitan -4 (140), Chacarra -1 (143 T11); R3 Saturday unpublished as final. Tennis: Stockholm Fritz walkover Rune, then 6-4, 6-2 Musetti; Tirante 7-5, 7-6 (1) Tabilo; today final Fritz vs Tirante unpublished; Turin starts Sunday Zverev vs Jodar. Formula 1: Five days to Round 21 Las Vegas (19-21 Nov, 6.201 km Strip), 33 pts separate Verstappen (279) through Norris (246) behind Champion Antonelli (390); Mercedes 652, Ferrari 510, Red Bull 415, McLaren 398. No Vegas race result.

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
