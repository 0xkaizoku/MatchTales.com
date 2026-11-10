export const SITE_TODAY = '2026-11-10';

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
    tagline: 'Rolex Paris Masters Final: Carlos Alcaraz battles past Ben Shelton 7-6(5), 7-5 to capture maiden Bercy crown.',
    liveNow: 'Paris Masters Final: Alcaraz def. Shelton 7-6(5), 7-5. Alcaraz saves key break points and captures his 9th ATP Masters 1000 title.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'ROLEX PARIS MASTERS FINAL: CARLOS ALCARAZ DOWNS BEN SHELTON IN STRAIGHT SETS FOR 9TH MASTERS CROWN',
    board: 'Open the court',
    span: 'hero',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'São Paulo GP: Lando Norris wins chaotic Interlagos race as Mercedes officially clinches 2026 Constructors title.',
    liveNow: 'Interlagos Race Final: Norris P1 (McLaren), Verstappen P2 (from 21st), Hadjar P3. Russell P4 and Antonelli P5 seal title for Mercedes.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'F1 SAO PAULO GP: LANDO NORRIS WINS DRAMATIC WET RACE AS MERCEDES CLINCHES CONSTRUCTORS TITLE',
    board: 'Open the grid',
    span: 'side',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'NFL Week 9 MNF: James Cook rushes for 107 yards as Bills stifle Vikings 23-6 in Minneapolis.',
    liveNow: 'Final at U.S. Bank Stadium: Bills 23, Vikings 6. Cook 107 yds, 1 TD; Allen 235 yds, 1 TD. Buffalo hands Minnesota (7-1) its first defeat.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'NFL WEEK 9 MNF: BUFFALO BILLS STIFLE VIKINGS 23-6 TO HAND MINNESOTA FIRST DEFEAT',
    board: 'Open the field',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'WWT Championship: 19-year-old Blades Brown edges Ben James in playoff for historic maiden PGA Tour victory.',
    liveNow: 'Final Round at Diamante: Blades Brown (-24) def. Ben James (-24) on 2nd playoff hole to become youngest PGA Tour winner in 95 years.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'PGA TOUR CABO: BLADES BROWN EDGES BEN JAMES IN PLAYOFF TO WIN HISTORIC WWT CHAMPIONSHIP',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Premier League MW10: Martin Ødegaard winner against Hull sends Arsenal six points clear atop the table.',
    liveNow: 'Final at Emirates: Arsenal 1-0 Hull City (Odegaard 72\'). Arsenal move to 27 points from 10 matches after City fall 3-1 at Forest.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'PREMIER LEAGUE MW10: MARTIN ODEGAARD 72ND-MINUTE STRIKE FIRES ARSENAL SIX POINTS CLEAR',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'NBA: Stephen Curry scores 25 points and passes DeRozan for 16th all-time as Warriors demolish Pelicans 138-87.',
    liveNow: 'Final at Chase Center: Warriors 138, Pelicans 87. Curry 25 pts (passes DeRozan); Podziemski 25 pts; Lendeborg 23 pts. Golden State wins 8th straight.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'NBA: STEPHEN CURRY HITS ALL-TIME MILESTONE AS WARRIORS DEMOLISH PELICANS 138-87',
    board: 'Open the floor',
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
