export const SITE_TODAY = '2026-10-22';

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
    tagline: 'Thursday kickoff: Patriots visit the Bears at Soldier Field. 49ers remain 6-0.',
    liveNow: 'TNF Thursday 8:15 p.m. ET: Patriots (4-2) at Bears (4-2), Prime Video, Chicago -3. Monday: 49ers 23, Commanders 17 (49ers 6-0).',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'TNF TONIGHT: PATRIOTS AT BEARS (4-2)',
    board: 'Open the field',
    span: 'hero',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA Finals Game 3: Dream crush Valkyries 97-71 to take 2-1 series lead.',
    liveNow: 'Final Wednesday: Dream 97, Valkyries 71. Angel Reese 21 pts, 12 reb, 3 stl. Game 4 Friday 8:00 p.m. ET, State Farm Arena.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA FINALS: DREAM LEAD 2-1 AFTER 97-71 ROUT',
    board: 'Open the floor',
    span: 'side',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Almaty Thursday: Tsitsipas closes Kukushkin farewell. Mannarino upsets Rublev.',
    liveNow: 'Almaty R16: Tsitsipas d. Kukushkin 6-1, 6-2. Mannarino d. Rublev 6-4, 3-6, 6-3. Duckworth d. Darderi 7-5, 7-6(9).',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'ALMATY: TSITSIPAS AND MANNARINO ADVANCE TO QF',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Round 1 begins at Port Royal. Butterfield Bermuda field of 120 tees off.',
    liveNow: 'Round 1 Thursday: Port Royal Golf Course, Southampton. Field of 120, purse $6M, par 71. Defending champion Adam Schenk.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'PORT ROYAL ROUND 1 UNDERWAY: 120 IN FIELD',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Matchweek 8 opens Friday with Ipswich v Forest. City lead table by three on 21.',
    liveNow: 'Standings: City 21, Arsenal 18, Brighton 16. Spurs 16th on 6, Coventry 17th on 6. MW8 opens Friday; Chelsea v Spurs Saturday.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'PREMIER LEAGUE: MW8 OPENS FRIDAY AT IPSWICH',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Austin Thursday media day: one day to Friday practice. Antonelli leads Russell by 102.',
    liveNow: 'Paddock media day at COTA. Weekend 23-25 October, race Sunday 25 October at 15:00 local. Antonelli 340, Russell 238. Mercedes 578.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'AUSTIN MEDIA DAY: ONE DAY TO PRACTICE',
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
