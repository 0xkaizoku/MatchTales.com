export const SITE_TODAY = '2026-10-05';

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
    tagline: 'NFL Week 4 MNF: Jared Goff achieves historic 18-for-18 perfect passing game as Lions outduel Seahawks 42-29.',
    liveNow: 'Goff sets NFL record for most completions without an incompletion (292 yds, 2 passing TDs, 1 receiving TD).',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'GOFF HISTORIC 18/18 MNF',
    board: 'Open the field',
    span: 'hero',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Rolex Shanghai Masters: ATP 1000 main draw kicks off at Qizhong Arena with Alcaraz, Sinner, and Djokovic arriving.',
    liveNow: 'Opening round underway in Shanghai while Beijing champions Alcaraz and Gauff travel south after China Open crowns.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'SHANGHAI MASTERS KICKS OFF',
    board: 'Open the court',
    span: 'side',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'F1 Americas Countdown: Norris Singapore masterclass trims Verstappen gap to 52 points; Lawson replaces Ricciardo.',
    liveNow: 'McLaren leads Constructors by 41 points heading into Austin triple-header as paddock analyzes RB20 balance.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'NORRIS MASTERCLASS & LAWSON',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Premier League MW7 Washup: Tottenham reel from Brighton collapse; Man City sit clear on 21 points at break.',
    liveNow: 'Postecoglou under mounting scrutiny after Spurs drop 10th point from leading position; international window begins.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'SPURS FALLOUT & CITY 21 PTS',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA Semifinals Game 2 Eve: Aces and Fever plot tactical counterpunches after Liberty and Lynx strike first.',
    liveNow: 'Hammon demands defensive overhaul against Stewart (34 pts); Clark and Fever prepare perimeter response at Lynx.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA SEMIS GAME 2 EVE',
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'PGA Tour: Kevin Yu vaults into top 65 after maiden playoff win; tour shifts to Utah for Black Desert Championship.',
    liveNow: 'Yu joins elite company with Jackson victory as inaugural Black Desert Championship tees off among red sandstone.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'YU SURGE & UTAH PREVIEW',
    board: 'Open the course',
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
