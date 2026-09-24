export const SITE_TODAY = '2026-09-25';

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
    tagline: 'Laver Cup Day 1 live at The O2. Ruud vs Cerúndolo opens in London.',
    liveNow: 'Day 1 underway at The O2: Ruud vs Cerúndolo, Mensik vs Nakashima. Noah leads Europe, Agassi leads World.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'LAVER CUP LIVE',
    board: 'Open the court',
    span: 'hero',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Baku qualifying day is here. Antonelli and Russell fight for pole.',
    liveNow: 'Qualifying on Friday at Baku City Circuit. 51-lap grid decided today. Race Saturday.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'BAKU QUALIFYING',
    board: 'Open the grid',
    span: 'side',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Presidents Cup Day 2 underway on Medinah Course No. 3.',
    liveNow: 'Friday matches rolling at Medinah: Snedeker and USA face Ogilvy and Internationals.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'PRESIDENTS CUP D2',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'Week 3 TNF in the books. Sunday slate countdown begins.',
    liveNow: 'Falcons and Packers kicked off Week 3. Highmark and Arrowhead headline Sunday.',
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
    tagline: 'WNBA playoffs tip off Sunday 27 Sep. Fever visit Dream in Game 1.',
    liveNow: '48-hour playoff countdown: Lynx vs Mystics, Valkyries vs Liberty, Aces vs Wings, Dream vs Fever.',
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
    tagline: 'Premier League Matchweek 6 arrives Saturday. City hosts Newcastle.',
    liveNow: 'Man City leads on 15 pts. Arsenal and Brighton pursue. European leagues in action tonight.',
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
