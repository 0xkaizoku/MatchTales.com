export const SITE_TODAY = '2026-10-23';

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
    tagline: 'Thursday Night Football final: Bears edge Patriots 30-24 at Soldier Field. Chicago moves to 5-2.',
    liveNow: 'TNF Final: Bears 30, Patriots 24. Williams 308 pass yds, 2 TD; Santos 58-yd FG. Bears 5-2, Patriots 4-3. 49ers 6-0.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'TNF FINAL: BEARS 30, PATRIOTS 24',
    board: 'Open the field',
    span: 'hero',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Almaty Friday: Tsitsipas beats Duckworth in straight sets to reach semifinals.',
    liveNow: 'Almaty QF: Tsitsipas d. Duckworth 6-3, 6-4. Bublik d. Khachanov 4-6, 7-6, 7-6. Medvedev d. Atmane 6-4, 6-4. Basilashvili d. Mannarino 6-3, 6-1.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'ALMATY: TSITSIPAS AND BUBLIK REACH SEMIFINALS',
    board: 'Open the court',
    span: 'side',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA Finals Game 4: Dream chase first franchise crown with 2-1 series lead in Atlanta.',
    liveNow: 'Game 4 at State Farm Arena: Dream lead 2-1 after 97-71 blowout. Reese historic 3rd Finals double-double. Valkyries face elimination.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA FINALS: DREAM CHASE TITLE IN GAME 4',
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Round 2 at Port Royal: Blanchet holds lead after opening 9-under 62 with two eagles.',
    liveNow: 'Butterfield Bermuda Round 2: Chandler Blanchet leads after 62 (-9). Conners, Kohles, Walker at 63 (-7). Port Royal Golf Course, par 71.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'PORT ROYAL ROUND 2: BLANCHET PACES FIELD',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Matchweek 8 opens tonight with Ipswich v Forest. City lead table by three on 21.',
    liveNow: 'MW8 Friday 20:00 UK: Ipswich v Forest at Portman Road. City 21 (7-0-0), Arsenal 18, Brighton 16. Chelsea v Spurs Saturday.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'PREMIER LEAGUE: MW8 OPENS TONIGHT AT IPSWICH',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Friday practice underway at COTA: Antonelli and Russell begin US Grand Prix running.',
    liveNow: 'Austin Friday: Practice 1 and 2 at COTA. Race Sunday 25 October at 15:00 local. Antonelli 340, Russell 238 (gap 102). Mercedes 578.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'AUSTIN PRACTICE UNDERWAY: ANTONELLI LEADS BY 102',
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
