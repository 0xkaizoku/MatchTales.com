export const SITE_TODAY = '2026-10-01';

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
    tagline: 'NFL Week 4 kicks off tonight: 49ers host Rams at Levi\'s Stadium on Thursday Night Football.',
    liveNow: 'NFC West rivals clash on short rest in Santa Clara (8:15 p.m. ET). Purdy and Stafford battle for divisional leverage.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'TNF 49ERS VS RAMS TONIGHT',
    board: 'Open the field',
    span: 'hero',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Champions League: Arsenal down PSG 2-0 with Havertz and Saka strikes; City cruise 4-0 in Europe.',
    liveNow: 'Arteta masterclass downs French champions at Emirates. Clean sheet keeps Gunners soaring ahead of Premier League MW7.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'ARSENAL 2-0 PSG',
    board: 'Open the pitch',
    span: 'side',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA Semifinals locked: Aces and Liberty finish sweeps to set up Lynx-Fever and Aces-Liberty.',
    liveNow: 'Historic first round features clean 2-0 sweeps across all four series. Semifinal battles tip off Sunday.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA FINAL FOUR LOCKED',
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Sanderson Farms Championship: Round 1 underway as Hadley and Hossler set early pace at 6-under.',
    liveNow: 'Defending champion Kevin Yu opens with a 4-under 68 in Jackson; FedExCup Fall points battle is live.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'ROUND 1 LIVE JACKSON',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'China Open 2026: Alcaraz defuses Mpetshi Perricard 6-4, 6-4; Medvedev and Gauff advance in Beijing.',
    liveNow: 'World No. 2 Alcaraz and Medvedev reach round of 16. Gauff cruises 6-1, 6-2 on Diamond Court.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'ALCARAZ ROLLS BEIJING',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Singapore GP: Marina Bay lights ignite as Antonelli leads grid into Thursday track walk.',
    liveNow: '1,600 floodlights illuminate 19 corners. Antonelli defends 88-point lead as teams prep for Friday practice.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'MARINA BAY TRACK WALK',
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
