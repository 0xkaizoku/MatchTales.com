export const SITE_TODAY = '2026-10-12';

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
    tagline: 'Premier League Matchweek 6 fallout: Manchester City crush Liverpool 3-0 at Anfield to pull three points clear.',
    liveNow: 'Haaland (65\'), Doku (68\'), and Cherki (78\') strike after Gravenberch red card. City reach 18 points (6-0-0), Arsenal 15, Brighton 13.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'CITY CRUSH LIVERPOOL AT ANFIELD (18 PTS)',
    board: 'Open the pitch',
    span: 'hero',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'Monday Night Football: Bills visit Rams at SoFi Stadium after Ravens edge Falcons 30-23 in overtime SNF thriller.',
    liveNow: 'Vikings (5-0) and 49ers (5-0) stay perfect; Chiefs 4-0 on bye. Week 5 wraps tonight in Los Angeles with Allen vs Stafford (8:15 p.m. ET, ESPN).',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'MONDAY NIGHT FOOTBALL: BILLS AT RAMS',
    board: 'Open the field',
    span: 'side',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Singapore GP: Max Verstappen commands 62-lap night race for first Marina Bay win as Kimi Antonelli extends title lead from third.',
    liveNow: 'Verstappen won from pole ahead of Leclerc (+4.2s) and Antonelli (+8.5s). Russell placed ninth. Antonelli (339 pts) leads Russell by 94 points.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'VERSTAPPEN WINS SINGAPORE GP',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Baycurrent Classic: Michael Brennan fires final-round 67 to claim inaugural Japan title at 16 under par.',
    liveNow: 'Brennan (-16) edged Keith Mitchell (-15) and Jacob Bridgeman (-15) by one stroke at Yokohama Country Club; Homa finished T11 (-10).',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'BRENNAN WINS BAYCURRENT CLASSIC (-16)',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Shanghai Masters: Alexander Zverev battles past Halys in three sets as Center Court action continues at Qizhong Arena.',
    liveNow: 'Zverev fought back 6-4, 6-7(8), 6-3; Hurkacz ousted Zhou 6-2, 3-6, 6-3; De Minaur stopped Sakamoto 7-6, 6-4. Sinner and Alcaraz headline Monday.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'SHANGHAI MASTERS CRUCIBLE',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA Finals locked: Atlanta Dream and Cinderella expansion Golden State Valkyries complete 3-1 semifinal upsets.',
    liveNow: 'Dream eliminated Liberty 85-83; Valkyries edged Aces 87-83 in overtime. Historic Finals matchup pits Atlanta against expansion Valkyries.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA FINALS: DREAM VS VALKYRIES',
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
