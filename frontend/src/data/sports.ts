export const SITE_TODAY = '2026-10-20';

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
    tagline: 'Tuesday tennis: Moutet beat Humbert in Lyon. Almaty is through the first round.',
    liveNow: 'Lyon: Moutet d. Humbert 6-2, 6-7(5), 7-6(4). Almaty Tuesday: Diaz Acosta, Basilashvili, Duckworth, Kukushkin and Mannarino through. Shanghai: Davidovich Fokina d. Jodar.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'LYON: MOUTET BEATS HUMBERT IN THREE SETS',
    board: 'Open the court',
    span: 'hero',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: '49ers beat the Commanders 23-17 and move to 6-0. Thursday: Patriots at Bears.',
    liveNow: 'Monday final: 49ers 23, Commanders 17. San Francisco 6-0, Washington 1-4-1. No game Tuesday. Thursday 8:15 p.m. ET: Patriots at Bears, Soldier Field, Prime Video.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: '49ERS 23-17: SAN FRANCISCO IS 6-0',
    board: 'Open the field',
    span: 'side',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'Dream beat the Valkyries 79-65. The WNBA Finals are tied 1-1.',
    liveNow: 'Game 2 final: Dream 79, Valkyries 65. Reese 30 points, 16 rebounds. Series tied 1-1. Game 3 Wednesday 8:00 p.m. ET, State Farm Arena. No score.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'DREAM 79-65: WNBA FINALS TIED 1-1',
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Spurs beat Coventry 3-1 for a first league win. City still lead on 21.',
    liveNow: 'Monday final: Tottenham 3, Coventry 1. Spurs 16th on 6, Coventry 17th on 6. City 21, Arsenal 18, Brighton 16. No match Tuesday.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'SPURS 3-1 COVENTRY: FIRST WIN OF THE SEASON',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'United States GP: no session on Tuesday. Antonelli leads Russell by 102 points.',
    liveNow: 'No running on 20 October. COTA weekend 23-25 October, race Sunday 25 October at 15:00 local. Antonelli 340, Russell 238. Mercedes 578, 134 ahead of Ferrari.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'AUSTIN IN THREE DAYS: ANTONELLI LEADS BY 102',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'No round on Tuesday. Butterfield Bermuda opens Thursday at Port Royal.',
    liveNow: 'Field of 120, purse $6 million. Adam Schenk defends. Port Royal is 6,828 yards, par 71. Golf Channel Thursday to Sunday, 1-4 p.m. ET. Brennan\'s 16-under Baycurrent win stands.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'BERMUDA OPENS THURSDAY: NO ROUND ON TUESDAY',
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
