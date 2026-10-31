export const SITE_TODAY = '2026-11-01';

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
    tagline: 'Mexico City GP: Kimi Antonelli finishes P2 behind Leclerc to become youngest F1 World Champion in history.',
    liveNow: 'Final at Hermanos Rodriguez: Charles Leclerc wins Mexico GP; Kimi Antonelli (Mercedes) finishes P2 to mathematically clinch the 2026 World Championship.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: '2026 F1 WORLD CHAMPION: KIMI ANTONELLI MAKES MOTORSPORT HISTORY IN MEXICO',
    board: 'Open the grid',
    span: 'hero',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'VidantaWorld Mexico Open: Raul Pereda shoots 66 to become first Mexican PGA Tour winner on home soil.',
    liveNow: 'Final at VidantaVallarta: Raul Pereda (-17, 267) birdies 15 and 17 to edge Austin Smotherman (-15, 269) by two shots for historic maiden victory.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'PGA TOUR MEXICO OPEN: RAUL PEREDA CLAIMS HISTORIC HOME TRIUMPH AT -17',
    board: 'Open the course',
    span: 'side',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'NFL Week 8: Undefeated Vikings stifle Colts 24-17 to advance to 7-0 behind Sam Darnold and Justin Jefferson.',
    liveNow: 'Final in Minneapolis: Vikings 24, Colts 17. Darnold 274 yds, 2 TD to Jefferson (128 rec yds). Minnesota stands as NFL\'s only 7-0 team.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'NFL WEEK 8: MINNESOTA VIKINGS REMAIN PERFECT AT 7-0 AFTER HOLDING OFF COLTS',
    board: 'Open the field',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Erste Bank Open Final: Carlos Alcaraz sweeps Lorenzo Musetti 6-3, 6-4 to lift Vienna ATP 500 crown.',
    liveNow: 'Vienna Championship: Alcaraz def. Musetti 6-3, 6-4 in 84 minutes. Alcaraz wins 6th title of 2026 without dropping a single set all week.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'ERSTE BANK OPEN: CARLOS ALCARAZ SWEEPS LORENZO MUSETTI TO CAPTURE VIENNA TITLE',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'NBA Sunday: Shai Gilgeous-Alexander pours in 36 points as defending champion Thunder edge Clippers 116-109.',
    liveNow: 'Final in Inglewood: Thunder 116, Clippers 109. Gilgeous-Alexander 36 pts, 9 ast; Holmgren 18 pts, 4 blk. Oklahoma City improves to 4-0.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'NBA SUNDAY: SHAI GILGEOUS-ALEXANDER LEADS UNBEATEN THUNDER PAST CLIPPERS',
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Premier League MW9: Cole Palmer strikes winner as Chelsea edge Newcastle 2-1; City lead table on 24 points.',
    liveNow: 'Premier League Sunday: Chelsea 2-1 Newcastle (Jackson 18\', Palmer 47\'; Isak 32\'). Chelsea climb to 16 pts. Man City lead league with 24 pts.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'PREMIER LEAGUE MW9: COLE PALMER STRIKES AS CHELSEA DOWN NEWCASTLE 2-1',
    board: 'Open the pitch',
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
