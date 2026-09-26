export const SITE_TODAY = '2026-09-27';

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
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Laver Cup Day 3 live at The O2. Triple points on Championship Sunday.',
    liveNow: 'Championship Sunday: 3 points per win. Alcaraz, Zverev, Fritz, and De Minaur fight for 13-point crown.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'LAVER CUP FINALE',
    board: 'Open the court',
    span: 'hero',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Presidents Cup Day 4 Sunday Singles underway at Medinah No. 3.',
    liveNow: '12 singles matches deciding the cup. Scheffler, Scott, Cantlay, and Matsuyama on the tee.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'PRESIDENTS CUP D4',
    board: 'Open the course',
    span: 'side',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'NFL Week 3 Sunday slate is live. Bills host Dolphins, Chiefs battle Chargers.',
    liveNow: 'Allen and 2-0 Bills host Miami at Highmark. Mahomes and 2-0 Chiefs face Chargers at Arrowhead.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'NFL WEEK 3 LIVE',
    board: 'Open the field',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA Playoffs Round 1 tips off today. Caitlin Clark and Fever visit Dream in Game 1.',
    liveNow: 'Opening-round quadruple-header: Lynx vs Mystics, Dream vs Fever, Valkyries vs Liberty, Aces vs Wings.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA PLAYOFFS R1',
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'City holds 100% record after 2-1 win over Newcastle. Premier League Matchweek 6 concludes.',
    liveNow: 'Haaland scores in 6th straight match as City reaches 18 pts. Arsenal in 2nd on 15 pts.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'EPL MATCHWEEK 6',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Antonelli wins Azerbaijan Grand Prix from pole in Mercedes 1-2 street triumph.',
    liveNow: 'Antonelli 1st, Russell 2nd, Leclerc 3rd. Mercedes extends constructors lead to 546 points.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'BAKU GP VICTORY',
    board: 'Open the grid',
    span: 'half',
  },
];

export function sportBySlug(slug: string): SportMeta | undefined {
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
    .filter(Boolean)
    .slice(0, 2)
    .map((w) => w[0]?.toUpperCase() || '')
    .join('');
}
