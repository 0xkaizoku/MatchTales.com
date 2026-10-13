export const SITE_TODAY = '2026-10-13';

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
    tagline: 'Premier League: Coventry beat Newcastle 4-1. City still lead on 18 points after the 3-0 at Anfield.',
    liveNow: 'Rudoni 6 (pen), Cherif 48, Botman 70, Simms 81, Mfuni 86. Coventry are 14th on 6 points. Newcastle stay 11th on 8. City 18 (16 for, 5 against).',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'COVENTRY BEAT NEWCASTLE 4-1',
    board: 'Open the pitch',
    span: 'hero',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'Monday Night Football: Bills beat Rams 37-34 in overtime at SoFi. Buffalo are 4-1.',
    liveNow: 'Bass hit a 45-yard field goal with 1:55 left in overtime. Bills 4-1, Rams 2-3. Vikings and 49ers are 5-0. Chiefs (4-0) are on a bye.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'BILLS BEAT RAMS 37-34 IN OT',
    board: 'Open the field',
    span: 'side',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'No race on Tuesday. Antonelli still leads by 102 points. Austin is next, 23-25 October.',
    liveNow: 'Singapore stands: Verstappen won from pole. Leclerc +7.335s, Antonelli +24.573s. Antonelli 340, Russell 238. Race day in Austin is 25 October, 15:00 local.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'AUSTIN NEXT: ANTONELLI LEADS BY 102',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'The PGA Tour is off this week. Brennan\'s Baycurrent win at 16 under still stands.',
    liveNow: 'No tournament is scheduled. Next: Butterfield Bermuda, 22-25 October, Port Royal, purse $6 million. Previous winner Adam Schenk.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'PGA TOUR OFF UNTIL BERMUDA',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Shanghai Masters: Alexander Zverev beats Alexander Bublik 7-6 (6), 4-6, 7-6 (1).',
    liveNow: 'Also through: de Minaur d. Khachanov 6-3, 6-4. Gea d. Mensik 7-6 (4), 6-4. Davidovich Fokina d. Hurkacz 1-6, 6-3, 7-6 (6). Sinner is still out.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'ZVEREV BEATS BUBLIK IN SHANGHAI',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA Finals: no game on Tuesday. Game 1 is Saturday at Chase Center, Valkyries hosting the Dream.',
    liveNow: 'Game 1 is 17 October, 3:30 p.m. ET, NBC. Game 2 is Monday 19 October, 8:00 p.m. ET. Both semis ended 3-0. No score yet.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA FINALS OPEN SATURDAY',
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
