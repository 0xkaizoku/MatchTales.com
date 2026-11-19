export const SITE_TODAY = '2026-11-19';

export const SPORT_SLUGS = ['tennis', 'football', 'f1', 'golf', 'basketball', 'soccer'] as const;
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
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: "Turin Day 5: Zverev faces Fils while Shelton meets Jodar for final McEnroe semifinal spot.",
    liveNow: "Thu McEnroe: Shelton vs Jodar (14:00 CET), Zverev vs Fils (20:30 CET). Wed Lendl: Alcaraz d Medvedev 6-2, 6-4 to clinch SF; Tiafoe d Cobolli.",
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: "TURIN ATP FINALS: DECISIVE MCENROE BATTLES TODAY AS SHELTON AND FILS FIGHT TO JOIN ZVEREV IN SEMIS",
    board: 'Open the court',
    span: 'hero',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: "TNF Week 11: Colts clash with Texans in Houston; Chargers fresh off 23-20 Harbaugh Bowl victory.",
    liveNow: "Tonight: Colts at Texans (8:15 PM ET, Prime Video, NRG Stadium). Week 10 MNF: Chargers 23, Ravens 20 (Herbert 22-yd TD run, Hampton 105 yds).",
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: "THURSDAY NIGHT FOOTBALL: COLTS AND TEXANS CLASH IN CRUCIAL AFC SOUTH WEEK 11 SHOWDOWN",
    board: 'Open the field',
    span: 'side',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: "Las Vegas GP arrives: Engines fire on the Strip tonight for opening practice sessions under neon lights.",
    liveNow: "Tonight: Practice 1 (21:30 ET) & Practice 2 (01:00 ET). Drivers P2: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390).",
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: "LAS VEGAS GP: ENGINES ROAR TONIGHT ON THE STRIP AS THURSDAY PRACTICE GETS UNDERWAY",
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: "The RSM Classic Round 1 underway at Sea Island with 2027 PGA Tour cards and top-125 cutoff on the line.",
    liveNow: "PGA Tour: Round 1 in progress at Sea Island (Seaside & Plantation). Top-125 bubble: Thompson, Hughes, Smotherman, Dahmen chasing status.",
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: "PGA TOUR FALL FINALE: ROUND 1 UNDERWAY AT SEA ISLAND AS BUBBLE CONTENDERS FIGHT FOR 2027 CARDS",
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: "Heat top Bucks 137-130 behind Giannis revenge game; Nuggets rally from 17 down to stun Celtics.",
    liveNow: "Wed: Heat 137-130 Bucks (Giannis 27/14/9, 6th straight win); Nuggets 105-101 Celtics (Jokic 24/9/8); Wizards 103-99 Raptors (Davis 25/14).",
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: "NBA WEDNESDAY: GIANNIS POSTS 27/14/9 TO BEAT FORMER TEAM FOR HEAT SIXTH STRAIGHT WIN",
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: "Nations League phase wraps with Haaland heroics; Premier League title race resumes this Saturday.",
    liveNow: "Tue: Norway 3-2 Denmark (Haaland late winner); Wales 2-3 Portugal. Mon: Germany 5-0 Netherlands. PL resumes Sat: Arsenal 27, Brighton 22, City 21.",
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: "SOCCER: NATIONS LEAGUE GROUPS CONCLUDE AS HAALAND FIRES NORWAY; PREMIER LEAGUE RETURNS SATURDAY",
    board: 'Open the pitch',
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
    .split(/\s+/)
    .map((p) => p[0])
    .filter(Boolean)
    .slice(0, 2)
    .join('')
    .toUpperCase();
}
