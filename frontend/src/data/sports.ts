export const SITE_TODAY = '2026-09-14';

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
    tagline: 'Arsenal and City are both 4-0-0. Hull are unbeaten. Leeds are 2-0 live at Elland Road.',
    liveNow: "LIVE 36': Leeds 2-0 Newcastle. Miley own goal 32', Calvert-Lewin 34'. Not finished.",
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'LIVE 2-0',
    board: 'Open the pitch',
    span: 'hero',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'Sunday is locked. Giants 28-20. Monday night is still open.',
    liveNow: 'Broncos at Chiefs, Monday 14 September, 8:15 p.m. ET, ESPN/ABC. Not kicked.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'KICKOFF TONIGHT',
    board: 'Open the field',
    span: 'side',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'The US Open has names. Zverev and Rybakina. Wimbledon already did.',
    liveNow: 'Zverev 6-3, 7-6 (2), 5-7, 6-2 Shelton. Rybakina 6-4, 5-7, 6-2 Sabalenka.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'OPEN CLOSED',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Antonelli won the first Madrid Grand Prix. Baku is next.',
    liveNow: 'Drivers: Antonelli 292, Russell 211, Hamilton 191. Azerbaijan, 24-26 September.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'BAKU NEXT',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Fox has the Claret Jug. Scheffler has the FedEx Cup. Presidents Cup is next.',
    liveNow: 'Presidents Cup, Medinah, 24-27 September. No result yet.',
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
