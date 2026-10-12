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
    tagline: 'Premier League Matchweek 6: Manchester City beat Liverpool 3-0 at Anfield and lead by three points.',
    liveNow: 'Haaland 65, Doku 68, Cherki 78 after Gravenberch was sent off. City 18 points (6-0-0, 16 for and 5 against). Arsenal 15, Brighton 13. Liverpool ninth on 9.',
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
    tagline: 'Monday Night Football: Bills (3-1) visit Rams (2-2) at SoFi after the Ravens won 30-23 in overtime.',
    liveNow: 'Kickoff is 8:15 p.m. ET on ESPN and ABC. No score yet. Vikings and 49ers are 5-0. Chiefs (4-0) are on a bye.',
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
    tagline: 'Singapore GP: Max Verstappen wins from pole. Kimi Antonelli finishes third and leads by 102 points.',
    liveNow: 'Official gaps: Leclerc +7.335s, Antonelli +24.573s. Russell ninth from 19th. Antonelli 340, Russell 238.',
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
    tagline: 'Baycurrent Classic: Michael Brennan wins at 16 under with a final-round 68.',
    liveNow: 'Brennan (-16, $1.44 million) finished one shot ahead of Mitchell and Bridgeman (-15). Homa tied for 13th at 11 under.',
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
    tagline: 'Shanghai Masters: Zizou Bergs beats Carlos Alcaraz, and Alexander Zverev is year-end No. 1.',
    liveNow: 'Bergs won 7-5, 7-6 (4). Sinner is out for the season. Sunday: Zverev beat Halys 6-4, 6-7 (8), 6-3.',
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
    tagline: 'WNBA Finals: the Dream and the Valkyries both swept their semifinals. Game 1 is Saturday at Chase Center.',
    liveNow: 'Dream beat Liberty 85-83. Valkyries beat the Aces 87-77 in overtime. Both series ended 3-0. Game 1 is 17 October, 3:30 p.m. ET, NBC.',
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
