export const SITE_TODAY = '2026-11-11';

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
    tagline: 'NBA: Paul George pours in 36 points in Philly return as Celtics rout 76ers 123-101 to seize East No. 1.',
    liveNow: 'Final in Philly: Celtics 123, 76ers 101 (George 36 pts, 6-11 3PT; Tatum 21; Maxey 24, Brown 13). Tonight ESPN: CLE at NYK (7 p.m. ET), GSW at HOU (9:30 p.m. ET).',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'NBA: PAUL GEORGE DROPS 36 IN PHILLY RETURN AS CELTICS TAKE EAST NO. 1 BEFORE TONIGHT ON ESPN',
    board: 'Open the floor',
    span: 'hero',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'UWCL MD4: Bayern win 2-1 at PSG and Real Madrid crush Paris FC 3-0 before Juventus host OL Lyonnes tonight.',
    liveNow: "Tuesday Finals: PSG 1-2 Bayern (Buhl 40'); Real Madrid 3-0 Paris FC; Hacken 0-0 Chelsea. Tonight: Juventus vs OL Lyonnes (20:00 UTC). Thu: Barcelona vs Arsenal.",
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'UWCL MD4: BAYERN EDGE PSG 2-1, JUVENTUS HOST LYON TONIGHT BEFORE BARCELONA VS ARSENAL',
    board: 'Open the pitch',
    span: 'side',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'NFL Week 10 TNF Tomorrow: Giants (5-2-1) and J.J. McCarthy host Commanders after Week 5 27-27 tie.',
    liveNow: 'Thursday 8:15 p.m. ET (MetLife White Out): Commanders (2-5-1) at Giants (5-2-1). MNF Final: Bills (7-1) 23, Vikings (6-2) 6 (Cook 107 yds, 1 TD).',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'NFL WEEK 10 TNF: GIANTS (5-2-1) HOST COMMANDERS TOMORROW AFTER WEEK 5 27-27 DEADLOCK',
    board: 'Open the field',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'DP World Tour Championship: Rory McIlroy and Race leader Eugenio Chacarra pair up Thursday in Dubai.',
    liveNow: 'Dubai R1 Tomorrow (12:40 GST): Chacarra (4,243.79 pts) leads McIlroy (3,709.86) by 533.93 pts for $3M prize. Cabo Final: Blades Brown (-23) wins playoff at 19.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'DUBAI FINALE: LEADER EUGENIO CHACARRA AND RORY MCILROY TEE OFF TOGETHER THURSDAY',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Stockholm Open: Musetti 6-1, 6-4 & Rune advance smoothly on eve of Thursday Nitto ATP Finals draw.',
    liveNow: 'Stockholm R16/R32: Musetti def. Samuel 6-1, 6-4; Rune def. Bergs 6-3, 6-4; Humbert def. Vallejo 6-4, 6-3. Turin 8-man draw: Thu 12:00 CET.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'ATP STOCKHOLM & TURIN DRAW: MUSETTI AND RUNE ADVANCE BEFORE THURSDAY NITTO ATP FINALS DRAW',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'F1 Standings Entering Las Vegas: 33 points cover Verstappen (279) through Norris (246) behind Antonelli.',
    liveNow: 'Drivers P2 Race: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli Champion 390; Mercedes 652). Next: Las Vegas (19-21 Nov).',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'F1 ENTERING LAS VEGAS: FIVE STARS SEPARATED BY 33 POINTS IN BATTLE BEHIND ANTONELLI',
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
    .map((p) => p[0])
    .filter(Boolean)
    .slice(0, 2)
    .join('')
    .toUpperCase();
}
