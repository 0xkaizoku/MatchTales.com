export const SITE_TODAY = '2026-10-21';

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
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA Finals Game 3 tonight: Valkyries at Dream. The series is tied 1-1.',
    liveNow: 'Game 3 Wednesday 8:00 p.m. ET, State Farm Arena, USA/Peacock/CNBC. No score. Game 2: Dream 79, Valkyries 65. Series 1-1.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA FINALS GAME 3 TONIGHT: SERIES TIED 1-1',
    board: 'Open the floor',
    span: 'hero',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Almaty Wednesday: Tsitsipas edges Kovacevic in three. Khachanov cruises past Sakamoto.',
    liveNow: 'Almaty: Tsitsipas d. Kovacevic 7-6(9), 3-6, 6-3. Khachanov d. Sakamoto 6-2, 6-4. Duckworth d. Darderi 7-5, 7-6(7). Lyon: Moutet d. Humbert.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'ALMATY: TSITSIPAS AND KHACHANOV REACH ROUND TWO',
    board: 'Open the court',
    span: 'side',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'Thursday kickoff: Patriots visit the Bears at Soldier Field. 49ers remain 6-0.',
    liveNow: 'TNF Thursday 8:15 p.m. ET: Patriots (4-2) at Bears (4-2), Prime Video, Chicago -3. Monday final: 49ers 23, Commanders 17 (49ers 6-0).',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'TNF TOMORROW: PATRIOTS AT BEARS (4-2)',
    board: 'Open the field',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Spurs digest 3-1 win ahead of Chelsea trip. City lead table by three on 21.',
    liveNow: 'Standings: City 21, Arsenal 18, Brighton 16. Spurs 16th on 6, Coventry 17th on 6. MW8 opens Friday; Chelsea v Spurs Saturday.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'PREMIER LEAGUE: CITY LEAD AS DERBY WEEKEND NEARS',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'United States GP: two days to Friday practice. Antonelli leads Russell by 102.',
    liveNow: 'No running on 21 October. COTA weekend 23-25 October, race Sunday 25 October at 15:00 local. Antonelli 340, Russell 238. Mercedes 578.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'AUSTIN IN TWO DAYS: ANTONELLI LEADS BY 102',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Wednesday Pro-Am wraps in Bermuda. Port Royal opens Thursday for Round 1.',
    liveNow: 'Pro-Am completed Wednesday. Field of 120, purse $6 million, par 71. Adam Schenk defends. Round 1 Thursday, Golf Channel 1-4 p.m. ET.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'PORT ROYAL OPENS THURSDAY: PRO-AM COMPLETE',
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
