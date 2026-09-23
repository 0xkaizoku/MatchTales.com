export const SITE_TODAY = '2026-09-23';

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
    tagline: 'Falcons at Packers opens Week 3 on Thursday. Penix Jr. returns.',
    liveNow: 'Lambeau lights on Thursday night. Love leads Green Bay. Alumni weekend in Wisconsin.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'PACKERS TNF',
    board: 'Open the field',
    span: 'hero',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'Fever 96-77 Lynx. Clark 27 points. Playoff bracket locks for 27 Sep.',
    liveNow: 'FINAL: Fever 96, Lynx 77. Aces 89-79 Sparks. Lynx 32-10 No. 1 seed. Playoffs start Sunday.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'FEVER 96-77',
    board: 'Open the floor',
    span: 'side',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Bayern 2-2 Man City in UWCL. City 15 from five in Premier League.',
    liveNow: 'UWCL Matchday 1: Wamser 86th-minute equalizer. Real Madrid 1-1 PSG. City leads EPL on 15 pts.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'BAYERN 2-2 CITY',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Presidents Cup practice day 2 at Medinah. Foursomes begin Thursday.',
    liveNow: 'Snedeker and Ogilvy eve press conference. Course No. 3 ready for 24 world-class players.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'PRESIDENTS CUP',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Laver Cup begins Friday at The O2. Agassi and Noah lead the benches.',
    liveNow: 'Teams on court at The O2 for media day. Alcaraz and Zverev lead Europe. World with Fritz and Shelton.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'LAVER CUP 25 SEP',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Baku race is Saturday 26 September. FP1 begins Thursday.',
    liveNow: 'Antonelli leads by 81 points. Media day at Baku street circuit. Practice Thursday, race Saturday.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'BAKU RACE SAT',
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
