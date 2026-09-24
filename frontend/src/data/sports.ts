export const SITE_TODAY = '2026-09-24';

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
    tagline: 'Falcons at Packers opens Week 3 tonight. Penix Jr. returns at Lambeau.',
    liveNow: 'Thursday Night Football kickoff 8:15 p.m. ET. Love leads 1-1 Packers; Penix starts for Atlanta on Prime Video.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'PACKERS TNF TONIGHT',
    board: 'Open the field',
    span: 'hero',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Presidents Cup Day 1 foursomes underway at Medinah No. 3.',
    liveNow: 'Course No. 3 opens: Snedeker and Ogilvy set Day 1 matches. Scheffler and Scott in action.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'MEDINAH FOURSOMES',
    board: 'Open the course',
    span: 'side',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Baku Thursday practice running. Antonelli and Russell test street circuit.',
    liveNow: 'FP1 and FP2 underway at Baku City Circuit. Mercedes leads constructors with 503 points. Race Saturday.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'BAKU FP1 & FP2',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Laver Cup eve in London: Noah and Agassi name Friday opening matches.',
    liveNow: 'The O2 is ready. Alcaraz and Zverev anchor Europe; Fritz and De Minaur lead World. Play begins Friday.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'LAVER CUP EVE',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA playoffs set for Sunday 27 Sep. Fever visit Dream in Game 1.',
    liveNow: 'Round 1 locked: Lynx vs Mystics, Valkyries vs Liberty, Aces vs Wings, Dream vs Fever.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA ROUND 1',
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Carabao Cup round 3 wrap and UWCL in the books. EPL Matchweek 6 ahead.',
    liveNow: 'City leads EPL on 15 pts. Arsenal and Brighton in pursuit. European Matchday 1 concluded.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'EPL MATCHWEEK 6',
    board: 'Open the pitch',
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
