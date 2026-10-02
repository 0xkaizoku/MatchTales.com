export const SITE_TODAY = '2026-10-06';

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
    tagline: 'WNBA Semifinals Game 2: Liberty host Aces at Barclays; Lynx battle Fever at Target Center in critical double-header.',
    liveNow: 'Aces and Fever face must-win road battles to avoid 0-2 holes as Stewart (34 pts) and Collier (28 pts) seek 2-0 leads.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA SEMIS GAME 2 SHOWDOWN',
    board: 'Open the floor',
    span: 'hero',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Rolex Shanghai Masters: Wawrinka and Nishikori advance in opening round as Alcaraz and Sinner prepare debuts.',
    liveNow: '39-year-old Wawrinka beats Safiullin 7-5, 7-6 to make Masters history; top seeds await second-round openers.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'WAWRINKA MAKES HISTORY',
    board: 'Open the court',
    span: 'side',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'NFL Week 5: Vikings and Chiefs stand as lone unbeatens; Lions vault into top three after Goff historic 18/18 display.',
    liveNow: 'Thursday Night Football looms as Falcons host Buccaneers; power rankings shift following Week 4 blowouts.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'CHIEFS & VIKINGS 4-0',
    board: 'Open the field',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'International Break: Nations League MD3 brings Italy vs Belgium blockbuster; City sit clear on 21 points at break.',
    liveNow: 'National squads gather across Europe and South America for World Cup qualifying and Nations League action.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'NATIONS LEAGUE MD3',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'F1 Americas Countdown: Liam Lawson begins intense RB audition as Red Bull readies Austin upgrade package.',
    liveNow: 'Lawson faces six-race shootout against Tsunoda with 2027 Red Bull seat on the line; McLaren defends 41-point lead.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'LAWSON AUDITION & RED BULL UPGRADE',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'PGA Tour: Black Desert Championship prepares for historic Utah debut among red rock canyons and black lava beds.',
    liveNow: 'Keith Mitchell and Beau Hossler seek Jackson redemption as Utah welcomes PGA Tour for first time since 1963.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'UTAH DEBUT & BLACK DESERT',
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
