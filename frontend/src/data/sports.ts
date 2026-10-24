export const SITE_TODAY = '2026-10-24';

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
    tagline: 'London derby Saturday: Chelsea host Tottenham at Stamford Bridge. Friday final: Ipswich 1, Forest 1.',
    liveNow: 'MW8 Saturday 17:30 UK: Chelsea v Tottenham at Stamford Bridge. Friday: Ipswich 1, Forest 1. City lead on 21 (7-0-0).',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'DERBY DAY: CHELSEA HOST TOTTENHAM AT THE BRIDGE',
    board: 'Open the pitch',
    span: 'hero',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Almaty Saturday: Basilashvili stuns Tsitsipas in three sets. Medvedev advances as Bublik retires.',
    liveNow: 'Almaty SF: Basilashvili d. Tsitsipas 6-4, 6-7(5), 6-3. Medvedev d. Bublik 6-3, ret. Sunday final: Medvedev v Basilashvili.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'ALMATY SF: BASILASHVILI AND MEDVEDEV REACH FINAL',
    board: 'Open the court',
    span: 'side',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA Finals Game 4 today: Dream lead series 2-1 and chase first championship in Atlanta.',
    liveNow: 'Game 4 at State Farm Arena: Dream lead 2-1 after 97-71 blowout. Reese historic 3rd Finals double-double. Valkyries fight for Game 5.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA FINALS GAME 4: DREAM CHASE HISTORIC CROWN',
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Austin Saturday qualifying: Leclerc paced Friday practice; Antonelli defends 102-point lead.',
    liveNow: 'COTA Saturday: FP3 and Qualifying at 16:00 local. Leclerc led FP1 and FP2; Antonelli +0.042s. Race Sunday 15:00.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'AUSTIN SATURDAY: QUALIFYING AT COTA',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Bermuda Round 3: Blanchet and Hirata share 36-hole lead at 13 under (129) at Port Royal.',
    liveNow: 'Butterfield Bermuda Round 3: Blanchet (62-67) and Hirata (65-64) tied at -13. Conners in chase. Port Royal, par 71.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'PORT ROYAL ROUND 3: BLANCHET AND HIRATA TIED AT -13',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'NFL Week 7 Sunday eve: Bears sit 5-2 after TNF win. Unbeaten Chiefs, 49ers and Vikings ready for Sunday.',
    liveNow: 'TNF Final: Bears 30, Patriots 24. Sunday slate: Chiefs at Seahawks (SNF), 49ers at Falcons, Colts at Vikings.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'NFL WEEK 7: SUNDAY SLATE AHEAD',
    board: 'Open the field',
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
