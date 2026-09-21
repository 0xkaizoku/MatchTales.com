export const SITE_TODAY = '2026-09-20';

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
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'City 15 from five. Arsenal 12. Brighton third on 10.',
    liveNow: 'City 5-3 Sunderland. Brobbey hat-trick in a loss. Matchweek 5 is closed.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'CITY 5-3',
    board: 'Open the pitch',
    span: 'hero',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'Bills 41-31. Sunday early window is LIVE. No Sunday final.',
    liveNow: 'FINAL: Bills 41, Lions 31. ESPN: Sunday first quarter is in progress. Do not print a Sunday final.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'BILLS 41-31',
    board: 'Open the field',
    span: 'side',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Davis Cup Final 8 is set. Germany 3-1 Croatia. Britain 4-0 Ecuador.',
    liveNow: 'Zverev sent Germany through in 77 minutes. Final 8, Bologna, 24-29 November.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'DAVIS CUP FINAL 8',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Antonelli won Madrid. Baku is 24-26 September, Saturday race.',
    liveNow: 'Drivers: Antonelli 292, Russell 211, Hamilton 191. FP1 Thursday 24 September in Baku.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'BAKU 24-26 SEP',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Spaun wins the BMW PGA at 17 under. Elvira, McIlroy, Rai, Scott T2.',
    liveNow: 'FINAL: JJ Spaun 271, 17 under. AP and DP World Tour. Presidents Cup 24-27 September.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'SPAUN -17',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'Lynx 31-10 still the one-seed. Liberty 93-81 in Minneapolis. Playoffs 27 September.',
    liveNow: 'Liberty 93-81 Lynx. Stewart 24 and 10. Playoffs begin 27 September. Sunday WNBA games are listed, not printed as finals.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'LIBERTY 93-81',
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
