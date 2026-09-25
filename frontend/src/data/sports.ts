export const SITE_TODAY = '2026-09-26';

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
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Baku Grand Prix race day is here. Antonelli leads Mercedes front row into 51-lap fight.',
    liveNow: 'Saturday race at Baku City Circuit. Antonelli on pole, Russell P2, Leclerc P3. Lights out 15:00 local (12:00 BST).',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'BAKU RACE DAY',
    board: 'Open the grid',
    span: 'hero',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Laver Cup Day 2 live at The O2. Points count double in London.',
    liveNow: 'Saturday ties underway: Alcaraz vs Fritz, Zverev vs De Minaur. 2 points per win. First to 13 points.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'LAVER CUP DAY 2',
    board: 'Open the court',
    span: 'side',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Presidents Cup Day 3 underway on Medinah Course No. 3.',
    liveNow: 'Moving Day double session: 8 points at stake across morning four-balls and afternoon foursomes.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'PRESIDENTS CUP D3',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Premier League Matchweek 6 arrives Saturday. City hosts Newcastle at Etihad.',
    liveNow: 'Man City defends 100% record on 15 pts. Arsenal, Liverpool, and Chelsea in Saturday action.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'EPL MATCHWEEK 6',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'Week 3 Sunday countdown underway. Packers hold off Falcons 24-20 on TNF.',
    liveNow: 'Love tallies 3 TDs at Lambeau. Bills-Dolphins and Chiefs-Chargers headline Sunday slate.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'NFL WEEK 3',
    board: 'Open the field',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA playoffs tip off Sunday 27 Sep. 24-hour countdown begins.',
    liveNow: 'Round 1 locked: Lynx vs Mystics, Valkyries vs Liberty, Aces vs Wings, Dream vs Fever.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA ROUND 1',
    board: 'Open the floor',
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
