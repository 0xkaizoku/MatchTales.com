export const SITE_TODAY = '2026-10-16';

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
    tagline: 'Shanghai Masters: Zverev beats de Minaur 6-4, 6-4; Friday quarterfinals are Jodar-Ruud and Medvedev-Paul.',
    liveNow: 'Thursday: Zverev d. de Minaur 6-4, 6-4. Davidovich Fokina d. Gea 4-1, ret. Friday QFs have no posted score. Sinner remains out.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'ZVEREV INTO SHANGHAI SEMIS, 6-4 6-4',
    board: 'Open the court',
    span: 'hero',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'Week 6: ESPN has no final for Seahawks at Broncos. Both enter 3-2.',
    liveNow: 'No final on the ESPN game page. Seahawks (3-2) at Broncos (3-2), Empower Field, 8:15 p.m. ET, Prime Video. Vikings and 49ers are 5-0. Chiefs are 4-0.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'NO ESPN FINAL: SEAHAWKS AT BRONCOS',
    board: 'Open the field',
    span: 'side',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Premier League: City still lead on 18 as Matchweek 7 starts Saturday.',
    liveNow: 'No Friday league match. City 18, Arsenal 15, Brighton 13. Saturday: Everton-Chelsea 12:30 BST, City-Ipswich 15:00, Brentford-Liverpool 15:00.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'CITY STILL 18 POINTS BEFORE SATURDAY',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA Finals: one day out, series 0-0, Game 1 Saturday at Chase Center.',
    liveNow: 'No game Friday. Game 1 is Saturday 17 October, 3:30 p.m. ET, Chase Center, NBC. Valkyries host Dream after 3-0 sweeps.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA FINALS GAME 1 IS SATURDAY',
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'United States GP: Austin is a week away. Antonelli leads Russell by 102.',
    liveNow: 'No session Friday. COTA sprint weekend 23-25 October, race Sunday 25 October at 15:00 local. Antonelli 340, Russell 238. Mercedes 578.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'AUSTIN IN A WEEK: ANTONELLI LEADS BY 102',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'PGA Tour is off. Brennan\'s Baycurrent title stands. Bermuda is next.',
    liveNow: 'No PGA Tour round Friday. Butterfield Bermuda is 22-25 October at Port Royal, $6 million. Previous winner Adam Schenk. Brennan won Baycurrent at 16 under.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'PGA TOUR OFF: BERMUDA IS NEXT WEEK',
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
