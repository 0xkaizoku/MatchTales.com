export const SITE_TODAY = '2026-10-19';

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
    tagline: 'Shanghai Masters: Davidovich Fokina beat Jodar 1-6, 7-6(5), 6-4 for the title.',
    liveNow: 'Final: Alejandro Davidovich Fokina d. Rafael Jodar 1-6, 7-6(5), 6-4. Semis: Fokina d. Zverev 5-7, 6-4, 6-3. Jodar d. Medvedev 6-3, 6-4. Zverev remains year-end No. 1.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'SHANGHAI: DAVIDOVICH FOKINA BEATS JODAR IN THE FINAL',
    board: 'Open the court',
    span: 'hero',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'NFL Week 6 Monday: Commanders visit the unbeaten 49ers. Chiefs are 5-0 after 22-6.',
    liveNow: 'Monday 8:15 p.m. ET: Commanders (1-3-1) at 49ers (5-0), Levi\'s Stadium, ESPN/ABC. No score. Sunday: Chiefs 22, Chargers 6. Bills 33, Raiders 30. Vikings 5-0 on a bye.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'WEEK 6 MONDAY: COMMANDERS AT UNBEATEN 49ERS',
    board: 'Open the field',
    span: 'side',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA Finals Game 2: Dream at Valkyries, 8:00 p.m. ET. Golden State lead 1-0.',
    liveNow: 'Game 1 final: Valkyries 68, Dream 64. Game 2 is Monday 19 October, 8:00 p.m. ET at Chase Center on USA, Peacock and CNBC. No score. Series 1-0.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA FINALS GAME 2: DREAM AT VALKYRIES, SERIES 1-0',
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Premier League Monday: Tottenham host Coventry. City lead on 21, Arsenal have 18.',
    liveNow: 'Monday 20:00 UK: Tottenham (3 pts) v Coventry (6 pts). No score. Sunday: Forest 0-1 Arsenal, Brighton 5-0 Palace. City 21 (7-0-0), Arsenal 18, Brighton 16.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'MW7 MONDAY: SPURS HOST COVENTRY OFF THE BOTTOM',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'United States GP: no session on Monday. Antonelli leads Russell by 102 points.',
    liveNow: 'No running on 19 October. COTA weekend 23-25 October, race Sunday 25 October at 15:00 local. Antonelli 340, Russell 238. Mercedes 578, 134 ahead of Ferrari.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'AUSTIN IN FOUR DAYS: ANTONELLI LEADS BY 102',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Butterfield Bermuda field is set. Port Royal tees off Thursday. No round today.',
    liveNow: '120-player field, $6 million, 500 FedExCup points. Defending champion Adam Schenk. First round Thursday 22 October. Brennan\'s Baycurrent win at 16 under stands.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'BERMUDA FIELD SET: PORT ROYAL OPENS THURSDAY',
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
