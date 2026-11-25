# Apply 2026-11-26 desk updates for AGENTS.md, sports.ts, and desk.json
import os
import json
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# 1. Update AGENTS.md
agents_path = os.path.join(ROOT, "AGENTS.md")
with open(agents_path, "r", encoding="utf-8") as f:
    agents_content = f.read()

new_clock_line = (
    "*   **Site clock:** editorial today is `2026-11-26` in `frontend/src/data/sports.ts` (`SITE_TODAY`). "
    "Football: NFL Week 12 Thanksgiving Week (Wed 25 Nov Netflix: Packers 6-4 at Rams 6-4; Thu 26 Nov: Bears 8-2 at Lions 8-2 1:00 PM ET, Eagles 3-7 at Cowboys 5-6 4:30 PM ET, Chiefs 8-2 at Bills 9-1 8:20 PM ET; Week 11 Final: Texans 26-3 Colts, TEX 4-7, IND 3-8). "
    "Soccer: UEFA Champions League MD5 (Tue: Real Madrid 5-1 PSV, Arsenal 1-1 Dortmund, Man City 2-2 Napoli; Wed early HT: Sabah 0-1 Barcelona; Wed 20:00 UTC slate ahead); PL after MW11: Arsenal 28, Brighton 22, Man City 22, Liverpool 21 (Liverpool 4-0 Man Utd, Newcastle 2-2 Arsenal, Man City 1-1 Fulham). "
    "Formula 1: Round 21 Las Vegas GP complete (1. Verstappen, 2. Norris +0.639s, 3. Piastri from P17; Russell crashed Lap 48); standings: Champion Antonelli 402, Verstappen 304, Hamilton 267, Russell 264, Norris 264; Round 22 Qatar GP at Lusail 27-29 Nov. "
    "Tennis: Davis Cup Finals Bologna (Tue QF: Czechia 2-0 Canada; Wed QF: Italy 1-0 South Korea via Musetti d. Hong 6-0, 7-6(5), Cobolli vs Kwon underway; Thu QFs: GB vs Germany, Austria vs Spain); Turin Final (22 Nov): Alcaraz d. Zverev 6-2, 7-6(7) unbeaten 5-0. "
    "Golf: Marco Penge wins The RSM Classic in 4-way playoff at -16 (266) over Haotong Li, Michael Thorbjornsen, and Max Greyserman; Hero World Challenge 3-6 Dec next. "
    "Basketball: NBA Emirates Cup Tue (Mavericks 120-101 Nuggets, Celtics 131-116 Wizards, Pistons 104-86 Magic); Wed 9-game slate starts 5:00 PM ET; Thu Thanksgiving rest day."
)

agents_content = re.sub(
    r'\*   \*\*Site clock:\*\* editorial today is `\d{4}-\d{2}-\d{2}`.*',
    new_clock_line,
    agents_content
)

agents_check = agents_content.replace("(`—`)", "")
if "\u2014" in agents_check:
    raise ValueError("Unexpected em-dash in AGENTS.md!")

with open(agents_path, "w", encoding="utf-8") as f:
    f.write(agents_content)
print("Updated AGENTS.md")

# 2. Update frontend/src/data/sports.ts
sports_path = os.path.join(ROOT, "frontend", "src", "data", "sports.ts")

new_sports_ts = """export const SITE_TODAY = '2026-11-26';

export const SPORT_SLUGS = ['football', 'soccer', 'f1', 'tennis', 'golf', 'basketball'] as const;
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
    tagline: "Thanksgiving Football: 8-2 Bears at 8-2 Lions open Thursday tripleheader after Wed Packers-Rams on Netflix.",
    liveNow: "Thanksgiving Eve (Wed 8:15 PM ET Netflix): Packers (6-4) at Rams (6-4). Thu Nov 26: Bears (8-2) at Lions (8-2) 1 PM ET, Eagles (3-7) at Cowboys (5-6) 4:30 PM ET, Chiefs (8-2) at Bills (9-1) 8:20 PM ET.",
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: "NFL WEEK 12 THANKSGIVING: IDENTICAL 8-2 LIONS AND BEARS CLASH FOR NFC NORTH LEAD; CHIEFS VISIT BILLS NIGHTCAP",
    board: 'Open the field',
    span: 'hero',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: "Champions League MD5: Real Madrid storm past PSV 5-1; Sabah 0-1 Barcelona HT as Wednesday night slate opens.",
    liveNow: "UCL Tue: Real Madrid 5-1 PSV (Mbappe 2), Arsenal 1-1 Dortmund (Gyokeres 10; Beier 55), Man City 2-2 Napoli. Wed HT: Sabah 0-1 Barcelona (Gordon). PL: Arsenal 28, Brighton 22, City 22, Liverpool 21.",
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: "CHAMPIONS LEAGUE MD5: REAL MADRID HIT 15 POINTS AT SUMMIT; LIVERPOOL ROUT MAN UTD 4-0 IN POCHETTINO BOW",
    board: 'Open the pitch',
    span: 'side',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: "Qatar GP next (27-29 Nov): Verstappen carries chaotic Las Vegas victory into Lusail standard weekend.",
    liveNow: "Vegas GP Final: 1. Verstappen, 2. Norris (+0.639s), 3. Piastri (from P17); Russell crashed Lap 48. Standings: Antonelli 402 (Champ), Verstappen 304, Hamilton 267, Russell 264, Norris 264. Qatar Fri FP1.",
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: "FORMULA 1: VERSTAPPEN TAKES LAS VEGAS THROUGH 35 LEAD CHANGES AS MCLAREN SLASH RED BULL GAP TO 9 POINTS",
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: "Davis Cup Final 8 in Bologna: Defending champions Italy lead South Korea 1-0; Alcaraz crowned Turin champion.",
    liveNow: "Davis Cup Bologna: Czechia d. Canada 2-0; Italy 1-0 South Korea (Musetti d. Hong 6-0, 7-6(5), Cobolli vs Kwon). Thu QFs: GB vs Germany, Austria vs Spain. Turin Final: Alcaraz d. Zverev 6-2, 7-6(7).",
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: "DAVIS CUP FINALS: ITALY LEAD SOUTH KOREA IN BOLOGNA QUARTERFINALS; ALCARAZ COMPLETES 5-0 TURIN TITLE RUN",
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: "Marco Penge captures maiden PGA Tour victory in dramatic four-man Sea Island playoff at The RSM Classic.",
    liveNow: "RSM Classic Final (23 Nov): Marco Penge (-16, 266) wins 1st playoff hole over Haotong Li, Michael Thorbjornsen, and Max Greyserman to earn PGA Tour card through 2028. Next: Hero World Challenge (3-6 Dec).",
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: "PGA TOUR: MARCO PENGE CAPS FOUR-WAY PLAYOFF AT SEA ISLAND FOR MAIDEN WIN AND 2027 MASTERS TICKET",
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: "Emirates NBA Cup heats up before Thanksgiving break: Mavericks stun Nuggets 120-101; Celtics drop 131 on Wizards.",
    liveNow: "Tue Cup Finals: Mavericks 120-101 Nuggets (Flagg 24/6/12); Celtics 131-116 Wizards (Tatum 41, George 28; Davis 33/13); Pistons 104-86 Magic (Joe 21 without Cunningham). Wed 9 games; Thu off.",
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: "EMIRATES NBA CUP: MAVS CRUISE BEHIND COOPER FLAGG AND TATUM EXPLODES FOR 41 AS LEAGUE NEARS THANKSGIVING PAUSE",
    board: 'Open the floor',
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

if "\u2014" in new_sports_ts or "--" in new_sports_ts:
    raise ValueError("Em-dash or double-hyphen detected in sports.ts string payload!")

with open(sports_path, "w", encoding="utf-8") as f:
    f.write(new_sports_ts)
print("Updated frontend/src/data/sports.ts")

# 3. Update frontend/src/data/desk.json
desk_path = os.path.join(ROOT, "frontend", "src", "data", "desk.json")
with open(desk_path, "r", encoding="utf-8") as f:
    desk_data = json.load(f)

desk_data["asOf"] = "2026-11-26"

# Update Premier League table to post-Matchweek 11 (verified Nov 24, 2026)
desk_data["premierLeagueTable"] = [
    {"pos": 1, "team": "Arsenal", "p": 11, "w": 9, "d": 1, "l": 1, "gf": 17, "ga": 7, "gd": 10, "pts": 28},
    {"pos": 2, "team": "Brighton", "p": 11, "w": 7, "d": 1, "l": 3, "gf": 26, "ga": 9, "gd": 17, "pts": 22},
    {"pos": 3, "team": "Manchester City", "p": 11, "w": 7, "d": 1, "l": 3, "gf": 22, "ga": 14, "gd": 8, "pts": 22},
    {"pos": 4, "team": "Liverpool", "p": 11, "w": 6, "d": 3, "l": 2, "gf": 18, "ga": 10, "gd": 8, "pts": 21},
    {"pos": 5, "team": "Bournemouth", "p": 11, "w": 5, "d": 3, "l": 3, "gf": 18, "ga": 14, "gd": 4, "pts": 18},
    {"pos": 6, "team": "Brentford", "p": 11, "w": 4, "d": 5, "l": 2, "gf": 20, "ga": 11, "gd": 9, "pts": 17},
    {"pos": 7, "team": "Leeds", "p": 11, "w": 4, "d": 5, "l": 2, "gf": 14, "ga": 9, "gd": 5, "pts": 17},
    {"pos": 8, "team": "Chelsea", "p": 11, "w": 5, "d": 1, "l": 5, "gf": 20, "ga": 20, "gd": 0, "pts": 16},
    {"pos": 9, "team": "Everton", "p": 11, "w": 4, "d": 4, "l": 3, "gf": 12, "ga": 14, "gd": -2, "pts": 16},
    {"pos": 10, "team": "Tottenham", "p": 11, "w": 4, "d": 3, "l": 4, "gf": 12, "ga": 11, "gd": 1, "pts": 15}
]

# Update F1 Drivers standings post-Las Vegas GP (Round 21 of 23)
desk_data["f1Drivers"] = [
    {"pos": 1, "name": "Kimi Antonelli (Champion)", "team": "Mercedes", "pts": 402},
    {"pos": 2, "name": "Max Verstappen", "team": "Red Bull", "pts": 304},
    {"pos": 3, "name": "Lewis Hamilton", "team": "Ferrari", "pts": 267},
    {"pos": 4, "name": "George Russell", "team": "Mercedes", "pts": 264},
    {"pos": 5, "name": "Lando Norris", "team": "McLaren", "pts": 264},
    {"pos": 6, "name": "Charles Leclerc", "team": "Ferrari", "pts": 250}
]

# Update F1 Constructors post-Las Vegas GP
desk_data["f1Constructors"] = [
    {"pos": 1, "name": "Mercedes (Champions)", "pts": 666},
    {"pos": 2, "name": "Ferrari", "pts": 517},
    {"pos": 3, "name": "Red Bull", "pts": 440},
    {"pos": 4, "name": "McLaren", "pts": 431}
]

# Append Week 11 + Week 12 Thanksgiving entries to nflWeek1 cleanly
week11_12_notes = [
    {"date": "2026-11-19", "time": "8:15 p.m. ET", "home": "Houston Texans", "away": "Indianapolis Colts", "note": "FINAL: Texans 26, Colts 3. Stroud 21/27, 194 yds, 3 TDs; Montgomery 107 rush yds; Anderson safety. Texans 4-7, Colts 3-8."},
    {"date": "2026-11-22", "time": "1:00 p.m. ET", "home": "Buffalo Bills", "away": "Miami Dolphins", "note": "FINAL: Bills 26, Dolphins 9. Buffalo leads AFC East at 9-1."},
    {"date": "2026-11-22", "time": "4:25 p.m. ET", "home": "San Francisco 49ers", "away": "Minnesota Vikings", "note": "FINAL: 49ers 35, Vikings 10 in Mexico City. 49ers sit atop NFC at 9-1."},
    {"date": "2026-11-25", "time": "8:15 p.m. ET", "home": "Los Angeles Rams", "away": "Green Bay Packers", "note": "UPCOMING Thanksgiving Eve (Netflix): Both teams 6-4 at SoFi Stadium."},
    {"date": "2026-11-26", "time": "1:00 p.m. ET", "home": "Detroit Lions", "away": "Chicago Bears", "note": "UPCOMING Thanksgiving Day (CBS): Both rivals 8-2 at Ford Field for NFC North lead."},
    {"date": "2026-11-26", "time": "4:30 p.m. ET", "home": "Dallas Cowboys", "away": "Philadelphia Eagles", "note": "UPCOMING Thanksgiving Day (FOX): Cowboys (5-6) host Eagles (3-7) at AT&T Stadium."},
    {"date": "2026-11-26", "time": "8:20 p.m. ET", "home": "Buffalo Bills", "away": "Kansas City Chiefs", "note": "UPCOMING Thanksgiving Night (NBC): Chiefs (8-2) at Bills (9-1) in AFC heavyweight clash."},
    {"date": "2026-11-27", "time": "3:00 p.m. ET", "home": "Pittsburgh Steelers", "away": "Denver Broncos", "note": "UPCOMING Black Friday (Prime Video): Broncos (8-2) visit Steelers (6-4)."}
]
existing_notes = {item.get("note", "") for item in desk_data.get("nflWeek1", [])}
for item in week11_12_notes:
    if item["note"] not in existing_notes:
        desk_data["nflWeek1"].append(item)

# Append Turin Final + Davis Cup Final 8 notes to usOpenQF
tennis_notes = [
    {"draw": "Turin Final", "p1": "Carlos Alcaraz", "p2": "Alexander Zverev", "status": "Alcaraz 6-2, 7-6 (7) on 22 Nov; undefeated 5-0 maiden champion"},
    {"draw": "Davis Cup QF", "p1": "Czechia", "p2": "Canada", "status": "Czechia won 2-0 on 24 Nov (Machac d. Draxl 6-2, 3-6, 6-2)"},
    {"draw": "Davis Cup QF", "p1": "Italy", "p2": "South Korea", "status": "25 Nov: Italy lead 1-0 (Musetti d. Hong 6-0, 7-6 (5)); Cobolli vs Kwon underway"},
    {"draw": "Davis Cup QF", "p1": "Great Britain", "p2": "Germany", "status": "Thu 26 Nov (10:00 CET) in Bologna; Austria vs Spain (17:00 CET) follows"}
]
existing_tennis = {f"{item.get('draw')}-{item.get('p1')}-{item.get('p2')}" for item in desk_data.get("usOpenQF", [])}
for item in tennis_notes:
    key = f"{item['draw']}-{item['p1']}-{item['p2']}"
    if key not in existing_tennis:
        desk_data["usOpenQF"].append(item)

raw_desk_str = json.dumps(desk_data, ensure_ascii=False, indent=2)
if "\u2014" in raw_desk_str or "--" in raw_desk_str:
    raise ValueError("Em-dash or double-hyphen detected in desk.json!")

with open(desk_path, "w", encoding="utf-8") as f:
    f.write(raw_desk_str + "\n")
print("Updated frontend/src/data/desk.json")
