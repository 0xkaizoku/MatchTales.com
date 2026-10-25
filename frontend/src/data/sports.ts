export const SITE_TODAY = '2026-10-25';

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
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'United States GP race day at COTA: Antonelli starts on pole as Ferrari and Verstappen chase.',
    liveNow: 'Austin Sunday 15:00 local: 56 laps at COTA. Antonelli on pole (1:34.035) ahead of Verstappen (+0.179s). Antonelli leads championship by 102.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'RACE DAY: ANTONELLI LEADS FROM POLE IN TEXAS',
    board: 'Open the grid',
    span: 'hero',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Almaty final: Medvedev rallies past Basilashvili 6-7, 6-1, 6-3 to defend his title.',
    liveNow: 'Almaty Final: Medvedev d. Basilashvili 6-7(6), 6-1, 6-3 in 1h 53m. 25th career title and first career title defense for Medvedev.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'ALMATY FINAL: MEDVEDEV DEFENDS TITLE IN THREE SETS',
    board: 'Open the court',
    span: 'side',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'NFL Week 7 Sunday: Unbeaten Chiefs, 49ers and Vikings put perfect marks on the line.',
    liveNow: 'Sunday Week 7: 49ers (6-0) at Falcons, Colts at Vikings (5-0), Chiefs (5-0) at Seahawks (SNF). Bears sit 5-2 after TNF win.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'NFL WEEK 7: UNBEATEN TRIO TESTED SUNDAY',
    board: 'Open the field',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Premier League shocks: Spurs stun Chelsea 2-0; Villa topple City 2-1 as Arsenal go level top.',
    liveNow: 'MW8: Spurs 2, Chelsea 0; Villa 2, City 1; Arsenal 2, Everton 0. City and Arsenal tied on 21 pts (7-0-1). Sunday: Liverpool 2, Brighton 0.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'PREMIER LEAGUE: SPURS AND VILLA DELIVER SATURDAY SHOCKS',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA Finals Game 4: Valkyries stifle Dream 67-62 to level series 2-2 and force Game 5.',
    liveNow: 'Game 4 Final: Valkyries 67, Dream 62. Williams 17 pts, Stokes defense halts Reese streak. Series tied 2-2 heading to San Francisco.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA FINALS: VALKYRIES FORCE GAME 5 IN SAN FRANCISCO',
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Bermuda final round: Power and Smotherman share 54-hole lead; Blanchet and Hirata in chase.',
    liveNow: 'Butterfield Bermuda Final Round: Power and Smotherman co-lead after 54 holes. Blanchet and Hirata chase at Port Royal, par 71.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'PORT ROYAL FINAL ROUND: POWER AND SMOTHERMAN CO-LEAD',
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
