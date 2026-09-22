export const SITE_TODAY = '2026-09-22';

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
    tagline: 'Week 2 is closed. Chiefs 33-30 in OT. Rams 28-6 on Monday night.',
    liveNow: 'FINAL: Rams 28, Giants 6. Chiefs beat Colts 33-30 in OT. Falcons at Packers on Thursday.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'RAMS 28-6',
    board: 'Open the field',
    span: 'hero',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'City 15 from five. Arsenal 12. Matchweek 6 arrives 26 September.',
    liveNow: 'Matchweek 5 is closed. City 5-0-0 on 15 points. Arsenal 12, Brighton 10.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'CITY 15 PTS',
    board: 'Open the pitch',
    span: 'side',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Baku race is Saturday 26 September. FP1 begins Thursday.',
    liveNow: 'Antonelli leads by 81 points. Baku street circuit: practice Thursday, race Saturday.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'BAKU RACE SAT',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Presidents Cup arrives at Medinah. Spaun won Wentworth at 17 under.',
    liveNow: 'U.S. vs International at Medinah No. 3. Competition begins Thursday 24 September.',
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
    liveNow: 'Davis Cup Final 8 is locked for Bologna. Laver Cup in London: 25-27 September.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'LAVER CUP 25 SEP',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA playoffs tip off 27 September. Lynx 31-10 on top.',
    liveNow: 'Dream 95-84 Liberty. Mercury 87-86 Wings. Eight-team playoff bracket begins Sunday.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'PLAYOFFS 27 SEP',
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
