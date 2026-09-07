export const SITE_TODAY = '2026-09-08';

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
    tagline: 'Wimbledon is in the books. The US Open is still live in New York.',
    liveNow: 'Quarter-finals: Alcaraz vs Shelton, Sabalenka vs Noskova.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'LIVE IN NEW YORK',
    board: 'Open the court',
    span: 'hero',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'Super Bowl LX is the reason Wednesday night is a rematch.',
    liveNow: 'Kickoff: Patriots at Seahawks, Wednesday 9 September, 8:20 p.m. ET.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'KICKOFF TOMORROW',
    board: 'Open the field',
    span: 'side',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Antonelli from nineteenth at Monza. Madrid is next.',
    liveNow: 'Drivers: Antonelli 267, Russell 201, Hamilton 191. Madring, 11-13 September.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'MADRID NEXT',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'The World Cup is archive. The Premier League is three games old and already rude.',
    liveNow: 'After three games: City and Arsenal on 9, Hull on 7 without conceding.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'BETWEEN MATCHWEEKS',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Fox has the Claret Jug. Scheffler has the FedEx Cup. Presidents Cup is next.',
    liveNow: 'Presidents Cup, 25-28 September. No result yet.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'PRESIDENTS CUP SOON',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'The Knicks waited 53 years. September belongs to the WNBA.',
    liveNow: 'WNBA playoffs begin 27 September. Lynx are the one-seed at 31-9.',
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
