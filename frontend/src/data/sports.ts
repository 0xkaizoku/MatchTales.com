export const SITE_TODAY = '2026-10-29';

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
    tagline: 'WNBA Finals Game 6 tonight: Valkyries (3-2) seek historic maiden title as Thunder open NBA defense with win.',
    liveNow: 'WNBA Finals Game 6 tonight in Atlanta: Valkyries lead 3-2. NBA: Thunder 122, Nuggets 108 (SGA 34 pts); Spurs 130, Kings 103 (Wemby 29 pts).',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA FINALS GAME 6: VALKYRIES ON BRINK OF CHAMPIONSHIP DESTINY',
    board: 'Open the floor',
    span: 'hero',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'NFL Week 8 kickoff tonight: Packers host Panthers at Lambeau Field as NFC North race intensifies.',
    liveNow: 'TNF tonight: Panthers (3-4) at Packers (5-2) on Prime Video. Minnesota Vikings (6-0) stand as lone unbeaten team.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'THURSDAY NIGHT FOOTBALL: PACKERS HOST PANTHERS UNDER LAMBEAU LIGHTS',
    board: 'Open the field',
    span: 'side',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Carabao Cup round 4: Man City edge Brighton 2-1 and Liverpool down Chelsea 2-0 to book quarter-final spots.',
    liveNow: 'Quarter-final draw today: Man City and Liverpool advance alongside Fleetwood Town. Premier League returns Saturday.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'CARABAO CUP QUARTER-FINAL DRAW: GIANTS JOIN FLEETWOOD TOWN IN HAT',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Vienna Round of 16: Alcaraz sweeps Berrettini 6-3, 6-4 while Zverev downs Giron to reach quarter-finals.',
    liveNow: 'Erste Bank Open R16: Alcaraz def. Berrettini 6-3, 6-4 (28 winners, 0 break points faced). Zverev def. Giron 6-2, 7-5 into Friday quarters.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'ERSTE BANK OPEN: ALCARAZ AND ZVEREV CRUISE INTO VIENNA QUARTER-FINALS',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Mexico City GP media day: Antonelli confirms car #12 for 2027 needing only P9 on Sunday to seal title.',
    liveNow: 'Press day at Hermanos Rodriguez: Antonelli (365 pts) confirms car #12. Ninth-place finish in Mexico guarantees 2026 World Championship.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'MEXICO CITY GP: ANTONELLI CONFIRMS NUMBER 12 ON BRINK OF CROWN',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'VidantaWorld Mexico Open round 1: Raul Pereda leads with 65 as Bermuda winner Smotherman opens with 66.',
    liveNow: 'VidantaVallarta Round 1: Raul Pereda (-6, 65) leads by one over Austin Smotherman (-5, 66) and Aaron Rai (-5, 66). Grillo at -4.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'PGA TOUR MEXICO OPEN: PEREDA LEADS AS SMOTHERMAN FIRES 66',
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
