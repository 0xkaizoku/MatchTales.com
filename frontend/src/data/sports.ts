export const SITE_TODAY = '2026-10-15';

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
    tagline: 'Shanghai Masters: Davidovich Fokina reaches semifinals as Gea retires; Zverev meets de Minaur tonight.',
    liveNow: 'Thursday QF: Davidovich Fokina d. Gea 4-1, ret. Zverev vs de Minaur tonight on Stadium Court. Sinner remains out.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'DAVIDOVICH FOKINA FIRST SHANGHAI SEMIFINALIST',
    board: 'Open the court',
    span: 'hero',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'Week 6 TNF gameday: Denver Broncos visit Seattle Seahawks tonight at Lumen Field.',
    liveNow: 'Thursday Night Football: Broncos (2-3) at Seahawks (4-1) kicks off tonight 8:15 p.m. ET on Prime Video. Vikings and 49ers stand 5-0.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'BRONCOS AT SEAHAWKS TONIGHT ON TNF',
    board: 'Open the field',
    span: 'side',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Premier League: City lead table by three points as Matchweek 7 press conferences begin.',
    liveNow: 'Pre-match conferences Thursday ahead of MW7 kickoff Saturday. City 18 pts (6-0-0), Arsenal 15, Brighton 13, Coventry 6. Spurs 19th on 3 points.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'CITY THREE POINTS CLEAR BEFORE MW7',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA Finals: Media Day at Chase Center as Valkyries and Dream prepare for Game 1.',
    liveNow: 'Media Day Thursday in San Francisco. Game 1 is Saturday 17 October, 3:30 p.m. ET, NBC. Expansion Valkyries host Atlanta after 3-0 sweep.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA FINALS MEDIA DAY AT CHASE CENTER',
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'United States GP: One week to Austin as Mercedes eye Constructors crown at COTA.',
    liveNow: 'Austin COTA Sprint weekend 23-25 October. Antonelli 340, Russell 238, gap 102. Mercedes lead constructors with 578 points.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'ONE WEEK TO UNITED STATES GP AT COTA',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'PGA Tour Fall hiatus: Preliminary Bermuda commitments take shape as Brennan holds Baycurrent title.',
    liveNow: 'PGA Tour off this week. Butterfield Bermuda Championship next (22-25 Oct, Port Royal, $6M purse). Brennan won at 16 under.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'PGA TOUR OFF: BERMUDA FIELD TAKES SHAPE',
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
