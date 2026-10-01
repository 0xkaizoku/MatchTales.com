export const SITE_TODAY = '2026-10-03';

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
    tagline: 'Premier League MW7: Man City fight back to beat Brentford 2-1; Liverpool edge Palace 1-0 to stay locked in title race.',
    liveNow: 'Haaland strikes his 11th league goal and Foden hits the winner in West London. City reach 21 points with seven straight wins.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'MAN CITY 2-1 BRENTFORD',
    board: 'Open the pitch',
    span: 'hero',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Singapore GP: Lando Norris storms to sensational pole position at Marina Bay, edging Max Verstappen and Lewis Hamilton.',
    liveNow: 'Norris clocks 1:29.525 under the floodlights to secure pole. Verstappen starts P2 (+0.203s), Hamilton P3 (+0.316s).',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'NORRIS POLE IN SINGAPORE',
    board: 'Open the grid',
    span: 'side',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'China Open 2026: Alcaraz downs Medvedev in straight sets; Sinner joins him for dream Beijing final.',
    liveNow: 'Alcaraz wins 7-5, 6-3 to reach his first Beijing final; defending champion Sinner defeats Bu 6-3, 7-6(3).',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'ALCARAZ VS SINNER FINAL',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'NFL Week 4 Sunday Night Football: Undefeated Bills visit Lamar Jackson and the Ravens in Baltimore.',
    liveNow: 'Josh Allen leads 3-0 Buffalo into M&T Bank Stadium against Jackson and Derrick Henry following 49ers TNF win.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'BILLS AT RAVENS SNF EVE',
    board: 'Open the field',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Sanderson Farms: Keith Mitchell shoots 64 on moving day to take 54-hole lead at 20-under in Jackson.',
    liveNow: 'Mitchell leads Beau Hossler (-19) by one shot heading into Sunday. Defending champion Kevin Yu sits T3 at -15.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'MITCHELL -20 ROUND 3',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA Semifinals Eve: Final Four tactical breakdown as Lynx-Fever and Aces-Liberty prepare for Sunday Game 1.',
    liveNow: 'Caitlin Clark tests Minnesota defense at Target Center while A\'ja Wilson battles Breanna Stewart in finals rematch.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA SEMIFINALS EVE',
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
