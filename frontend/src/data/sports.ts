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
    tagline: 'City 12 from four games. Arsenal 12 from five. Brighton third on 10.',
    liveNow: 'Brighton 3-0 Arsenal. Champions first league defeat. Sunday: City, Leeds, Liverpool, United still to play.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'BRIGHTON 3-0',
    board: 'Open the pitch',
    span: 'hero',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'Bills 41-31. Allen five TDs. Sunday Week 2 is today and has not kicked.',
    liveNow: 'FINAL: Bills 41, Lions 31. Fourteen Sunday games plus Monday Night have not been played.',
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
    tagline: 'US Open: Zverev and Rybakina. Laver Cup is 25-27 September at The O2.',
    liveNow: 'Zverev and Rybakina closed Flushing. Laver Cup, London, 25-27 September. No result yet.',
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
    tagline: 'Celli and Elvira share 13 under after 54 holes at Wentworth. No winner.',
    liveNow: 'BMW PGA, Wentworth. Celli 203, Elvira 203, both -13. Round 4 is Sunday. No champion.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'CELLI ELVIRA -13',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'Lynx 31-10 still the one-seed. Liberty 93-81 in Minneapolis. Playoffs 27 September.',
    liveNow: 'Liberty 93-81 Lynx. Stewart 24 and 10. Playoffs begin 27 September. Sunday games have not tipped.',
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
