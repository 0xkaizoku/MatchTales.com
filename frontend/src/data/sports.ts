export const SITE_TODAY = '2026-10-11';

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
    tagline: 'Premier League Sunday blockbuster: undefeated Liverpool host perfect Manchester City at Anfield (16:30 BST).',
    liveNow: 'Arsenal beat Leeds 2-1 to reach 15 points (5-0-1), pulling level with City. United beat Spurs 2-0; Brighton sit third with 13.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'LIVERPOOL VS MANCHESTER CITY',
    board: 'Open the pitch',
    span: 'hero',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Singapore GP Sunday: Max Verstappen and George Russell share front row for 62 laps under Marina Bay floodlights.',
    liveNow: 'Verstappen swept Saturday Sprint win and GP pole (1:29.525). Antonelli (324 pts) starts fourth defending an 81-point lead over Russell (243).',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'SINGAPORE GP NIGHT RACE',
    board: 'Open the grid',
    span: 'side',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'NFL Week 5 Sunday: Ravens visit Falcons on SNF. Undefeated Vikings and 49ers aim to reach 5-0; Chiefs (4-0) on bye.',
    liveNow: 'Texas won 122nd Red River Rivalry 34-20 over Oklahoma. Sunday brings full NFL slate capped by Ravens at Falcons at 8:20 p.m. ET.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'NFL SUNDAY SLATE & SNF',
    board: 'Open the field',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Baycurrent Classic Championship Sunday: Max Homa (-14) holds one-shot lead over Jacob Bridgeman (-13) in Yokohama.',
    liveNow: 'Homa carded Moving Day 66 for 54-hole lead (199). Keith Mitchell (-12) in final group; Hideki Matsuyama surged to -10.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'BAYCURRENT CHAMPIONSHIP SUNDAY (-14)',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Shanghai Masters Round of 16: Alexander Zverev faces Ben Shelton on Center Court; Hubert Hurkacz meets Rei Sakamoto.',
    liveNow: 'Hurkacz followed Djokovic upset by beating Mannarino 6-3, 6-4. Zverev and Shelton advanced in straight sets for Sunday clash.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'SHANGHAI ROUND OF 16',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA Semifinals Game 4 double-header: Liberty and Aces fight to force deciding Game 5 clashes against Dream and Valkyries.',
    liveNow: 'Stewart (28 pts) led Liberty past Dream 88-82; Wilson (31 pts, 14 reb) lifted Aces over Valkyries 86-79. Both series stand 2-1.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA GAME 4 DOUBLE-HEADER',
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
