# AGENTS.md

Welcome, AI Coding Agent! This file outlines the architecture, tech stack, rules, and guidelines for **MatchTales** to help you understand the codebase and make consistent, high-quality contributions.

---

## 1. Project Overview

**MatchTales** is a story-centric web platform. It began as the narrative layer on the **2026 FIFA World Cup** and now covers soccer, tennis, golf, American football, basketball and Formula 1 with the same question: why does this one matter?
*   **"Why Care" Scores & Reasons:** Editorial assessments of match, round and race stakes.
*   **Narrative Stories:** Previews and write-ups locked to named sources. No invented scorers.
*   **World Cup Archive:** 48 teams, 12 groups, completed 19 July 2026. Spain are champions.
*   **Sport desks:** mosaic at `/sports`. Unique boards at `/sport/tennis`, `/sport/football`, `/sport/f1`, `/sport/soccer`, `/sport/golf`, `/sport/basketball`. Soccer is one desk, not the default.
*   **Site clock:** editorial today is `2026-11-26` in `frontend/src/data/sports.ts` (`SITE_TODAY`). Football: NFL Week 12 Thanksgiving Week (Wed 25 Nov Netflix: Packers 6-4 at Rams 6-4; Thu 26 Nov: Bears 8-2 at Lions 8-2 1:00 PM ET, Eagles 3-7 at Cowboys 5-6 4:30 PM ET, Chiefs 8-2 at Bills 9-1 8:20 PM ET; Week 11 Final: Texans 26-3 Colts, TEX 4-7, IND 3-8). Soccer: UEFA Champions League MD5 (Tue: Real Madrid 5-1 PSV, Arsenal 1-1 Dortmund, Man City 2-2 Napoli; Wed early HT: Sabah 0-1 Barcelona; Wed 20:00 UTC slate ahead); PL after MW11: Arsenal 28, Brighton 22, Man City 22, Liverpool 21 (Liverpool 4-0 Man Utd, Newcastle 2-2 Arsenal, Man City 1-1 Fulham). Formula 1: Round 21 Las Vegas GP complete (1. Verstappen, 2. Norris +0.639s, 3. Piastri from P17; Russell crashed Lap 48); standings: Champion Antonelli 402, Verstappen 304, Hamilton 267, Russell 264, Norris 264; Round 22 Qatar GP at Lusail 27-29 Nov. Tennis: Davis Cup Finals Bologna (Tue QF: Czechia 2-0 Canada; Wed QF: Italy 1-0 South Korea via Musetti d. Hong 6-0, 7-6(5), Cobolli vs Kwon underway; Thu QFs: GB vs Germany, Austria vs Spain); Turin Final (22 Nov): Alcaraz d. Zverev 6-2, 7-6(7) unbeaten 5-0. Golf: Marco Penge wins The RSM Classic in 4-way playoff at -16 (266) over Haotong Li, Michael Thorbjornsen, and Max Greyserman; Hero World Challenge 3-6 Dec next. Basketball: NBA Emirates Cup Tue (Mavericks 120-101 Nuggets, Celtics 131-116 Wizards, Pistons 104-86 Magic); Wed 9-game slate starts 5:00 PM ET; Thu Thanksgiving rest day.

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
