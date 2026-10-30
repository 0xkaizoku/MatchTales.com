export const SITE_TODAY = '2026-10-31';

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
    tagline: 'Premier League MW9: Arsenal and Liverpool battle to 2-2 draw at Emirates; Man City take sole top spot.',
    liveNow: 'Final at Emirates: Arsenal 2-2 Liverpool (Saka 9\', Merino 43\'; Van Dijk 18\', Salah 81\'). Man City edge Southampton 1-0 to lead on 23 pts.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'PREMIER LEAGUE MW9: ARSENAL AND LIVERPOOL SHARE SPOILS IN 2-2 EMIRATES EPIC',
    board: 'Open the pitch',
    span: 'hero',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Mexico City GP Qualifying: Kimi Antonelli captures dramatic pole position ahead of Leclerc and Verstappen.',
    liveNow: 'Qualifying at Hermanos Rodriguez: Antonelli (1:16.892) takes pole from Leclerc (+0.076s) and Verstappen (+0.142s). P9 on Sunday seals title.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'MEXICO CITY GP QUALIFYING: KIMI ANTONELLI STORMS TO POLE POSITION ON BRINK OF TITLE',
    board: 'Open the grid',
    span: 'side',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'NBA Saturday: Victor Wembanyama puts up 31 points and 6 blocks as Spurs tame Suns 118-106 in Phoenix.',
    liveNow: 'Final at Footprint Center: Spurs 118, Suns 106. Wembanyama 31 pts, 14 reb, 6 blk; Chris Paul 12 ast; Durant 28 pts. Spurs 3-1.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'NBA SATURDAY: VICTOR WEMBANYAMA POSTS 31 POINTS AND 6 BLOCKS IN PHOENIX',
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Erste Bank Open semi-finals: Carlos Alcaraz outduels Alexander Zverev 6-4, 7-6 to book ticket to Vienna final.',
    liveNow: 'Vienna ATP 500 SF: Alcaraz def. Zverev 6-4, 7-6 (5) with 34 winners. Alcaraz reaches 9th final of 2026 without dropping a set.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'ERSTE BANK OPEN: CARLOS ALCARAZ SUBDUES ALEXANDER ZVEREV TO REACH VIENNA FINAL',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'College Football Week 10: Georgia pulls away from Florida 34-20 in Jacksonville Cocktail Party to stay 8-0.',
    liveNow: 'Final in Jacksonville: Georgia 34, Florida 20. Beck 285 yds, 3 TD; Etienne 112 yds, 1 TD. Sunday: 6-0 Vikings face Colts.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'COLLEGE FOOTBALL: GEORGIA OVERPOWERS FLORIDA 34-20 TO PRESERVE 8-0 RECORD',
    board: 'Open the field',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'VidantaWorld Mexico Open round 3: Austin Smotherman clings to 54-hole lead at 13-under; Raul Pereda chases at 12-under.',
    liveNow: 'Moving day at VidantaVallarta: Smotherman -13 (66-65-69=200) holds 1-shot lead over Mexico\'s Raul Pereda (-12, 201) and Rai (-11).',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'PGA TOUR MEXICO OPEN: SMOTHERMAN HOLDS 54-HOLE LEAD AT -13; PEREDA CHARGES TO -12',
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
