"""Update site clock, sports.ts, AGENTS.md, and desk.json to 2026-11-16."""
import os
import re
import json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
FRONTEND = os.path.join(ROOT, "frontend")

# 1. Update AGENTS.md
agents_path = os.path.join(ROOT, "AGENTS.md")
agents_txt = open(agents_path, "r", encoding="utf-8").read()
# Replace Site clock line
agents_txt = re.sub(
    r'\*   \*\*Site clock:\*\* editorial today is `\d{4}-\d{2}-\d{2}`.*',
    "*   **Site clock:** editorial today is `2026-11-16` in `frontend/src/data/sports.ts` (`SITE_TODAY`). Soccer: Sunday Spain 2-3 England at Metropolitano (Kane, Konsa, White snap Spain 43-game unbeaten run); Denmark 4-1 Portugal; PL Arsenal 27, Brighton 22, Man City 21. Football: Monday Night Football Chargers at Ravens (Harbaugh Bowl); Sunday Munich Lions 35, Patriots 10 (Gibbs 252 scrimmage yds, 2 TDs). Basketball: Sunday Spurs 110-102 Jazz (Wembanyama 26/11/6/5, Harper 31, 12th straight win); Lakers 131-123 Suns; Celtics 131-94 Mavs. Tennis: Turin ATP Finals McEnroe Group complete (Zverev d Jodar 6-4, 6-4; Shelton d Fils 6-2, 3-6, 6-3); Monday Lendl Group opens (Alcaraz vs Tiafoe, Medvedev vs Cobolli). Golf: DP World Tour season complete: Hatton wins Dubai on -15 (273); McIlroy (67, -10, 278) seals 8th Race to Dubai title by 125 pts; PGA Tour heads to Sea Island for RSM Classic. Formula 1: Three days to Round 21 Las Vegas (19-21 Nov, 6.201 km Strip), 33 pts cover Verstappen (279) through Norris (246) behind Champion Antonelli (390); Mercedes 652, Ferrari 510, Red Bull 415, McLaren 398. No Vegas track session yet.",
    agents_txt
)
open(agents_path, "w", encoding="utf-8").write(agents_txt)
print("AGENTS.md updated.")

# 2. Update sports.ts
sports_path = os.path.join(FRONTEND, "src", "data", "sports.ts")
sports_content = """export const SITE_TODAY = '2026-11-16';

export const SPORT_SLUGS = ['soccer', 'tennis', 'golf', 'football', 'basketball', 'f1'] as const;
export type SportSlug = (typeof SPORT_SLUGS)[number];

export type SportSpan = 'hero' | 'side' | 'half';

export type SportMeta = {
  slug: SportSlug;
  label: string;
  short: string;
  href: string;
  tagline: string;
  liveNow: string;
  accent: string;
  hue: string;
  pulse: string;
  board: string;
  span: SportSpan;
};

/** Order is "what is on right now", not soccer first. */
export const SPORTS: SportMeta[] = [
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: "MNF Tonight: Chargers at Ravens in Harbaugh Bowl; Lions rout Patriots 35-10 in Munich.",
    liveNow: "Tonight: Chargers at Ravens (8:15 PM ET, M&T Bank Stadium, Harbaugh Bowl). Sun Munich: Lions 35-10 Patriots (Gibbs 252 yds, 2 TDs).",
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: "MNF TONIGHT: CHARGERS AT RAVENS IN HARBAUGH BOWL; LIONS ROUT PATRIOTS 35-10 IN MUNICH",
    board: 'Open the field',
    span: 'hero',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: "England shock Spain 3-2 in Madrid thriller to claim Group A3 top spot; Denmark crush Portugal 4-1.",
    liveNow: "Sun: Spain 2-3 England (Kane 45 pen, Konsa 53, White 58; Oyarzabal 65 pen, Williams 75). PL: Arsenal 27, Brighton 22, City 21.",
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: "NATIONS LEAGUE: ENGLAND STUN SPAIN 3-2 IN MADRID; THREE LIONS CLAIM GROUP A3 TOP SEED",
    board: 'Open the pitch',
    span: 'side',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: "Spurs extend streak to 12 behind Wembanyama and Harper; Lakers outlast Suns 131-123.",
    liveNow: "Sun: Spurs 110-102 Jazz (Wembanyama 26/11/6/5, Harper 31, 12 in a row); Lakers 131-123 Suns; Celtics 131-94 Mavs; Knicks 112-108 Raptors (OT).",
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: "NBA SUNDAY: SPURS WIN 12TH STRAIGHT, DOWN JAZZ 110-102; LAKERS BEAT SUNS 131-123",
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: "Turin ATP Finals: Shelton edges Fils in three; Alcaraz meets Tiafoe as Lendl Group opens Monday.",
    liveNow: "Turin Sun: Shelton d Fils 6-2, 3-6, 6-3; Zverev d Jodar 6-4, 6-4. Mon Lendl Group: Alcaraz vs Tiafoe (14:00 CET), Medvedev vs Cobolli (20:30 CET).",
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: "TURIN ATP FINALS: SHELTON EDGES FILS 6-2, 3-6, 6-3; ALCARAZ MEETS TIAFOE ON MONDAY",
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: "McIlroy celebrates record-equalling 8th Race to Dubai title; RSM Classic tournament week begins.",
    liveNow: "Dubai Complete: 1. Hatton -15 (273); 2. McIlroy -10 (278, seals 8th season crown by 125 pts). Next: RSM Classic at Sea Island (19-22 Nov).",
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: "MCILROY SEALS RECORD-EQUALING 8TH RACE TO DUBAI; PGA TOUR HEADS TO SEA ISLAND FOR RSM CLASSIC",
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: "Three days to Round 21 Las Vegas: 33 points cover five drivers in furious shootout for P2.",
    liveNow: "Drivers P2 battle: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). Vegas Strip: 19-21 Nov.",
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: "THREE DAYS TO VEGAS: 33 POINTS SPLIT VERSTAPPEN TO NORRIS FOR RUNNER-UP HONORS",
    board: 'Open the grid',
    span: 'half',
  },
];

export function sportBySlug(slug: string): SportMeta | undefined {
  return SPORTS.find((s) => s.slug === slug);
}

export function getSport(slug: string): SportMeta | undefined {
  return SPORTS.find((s) => s.slug === slug);
}

export function sportOf(entry: { sport?: string | null }): SportSlug {
  const s = (entry.sport || 'soccer').toLowerCase();
  return (SPORT_SLUGS as readonly string[]).includes(s) ? (s as SportSlug) : 'soccer';
}

export function isWorldCup(entry: { competition?: string | null }): boolean {
  const c = entry.competition || 'world-cup-2026';
  return c === 'world-cup-2026';
}

export function initials(name: string) {
  return name
    .split(/\\s+/)
    .map((p) => p[0])
    .filter(Boolean)
    .slice(0, 2)
    .join('')
    .toUpperCase();
}
"""
open(sports_path, "w", encoding="utf-8").write(sports_content)
print("sports.ts updated.")

# 3. Update desk.json
desk_path = os.path.join(FRONTEND, "src", "data", "desk.json")
desk_json = json.load(open(desk_path, "r", encoding="utf-8"))
desk_json["asOf"] = "2026-11-16"
open(desk_path, "w", encoding="utf-8").write(json.dumps(desk_json, indent=2, ensure_ascii=False) + "\n")
print("desk.json updated.")

