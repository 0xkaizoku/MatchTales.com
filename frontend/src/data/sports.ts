export const SITE_TODAY = '2026-10-17';

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
    tagline: 'Shanghai Masters: Semifinals Saturday as Jodar meets Medvedev and Zverev faces Davidovich Fokina.',
    liveNow: 'Friday QFs: Jodar d. Ruud 4-6, 6-4, 6-3. Medvedev d. Paul 6-3, 1-6, 6-3. Saturday Semifinals: Zverev vs Davidovich Fokina, Medvedev vs Jodar.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'SHANGHAI SEMIFINALS: JODAR, MEDVEDEV, ZVEREV',
    board: 'Open the court',
    span: 'hero',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA Finals Game 1 Gameday: Valkyries host Dream at Chase Center today at 3:30 p.m. ET.',
    liveNow: 'Game 1 is Saturday 17 October, 3:30 p.m. ET, Chase Center, NBC/Peacock. Series 0-0. Expansion Valkyries host Dream after both completed 3-0 semifinal sweeps.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA FINALS GAME 1 TODAY AT CHASE CENTER',
    board: 'Open the floor',
    span: 'side',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'Week 6 TNF Final: Broncos edge Seahawks 17-14 in overtime on Lutz 53-yard field goal.',
    liveNow: 'FINAL (OT): Broncos 17, Seahawks 14. Lutz 53-yd FG after McMillian INT. Broncos improve to 4-2, Seahawks 3-3. Vikings and 49ers stand 5-0. Chiefs 4-0.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'FINAL (OT): BRONCOS 17, SEAHAWKS 14',
    board: 'Open the field',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Premier League MW7: City host Ipswich at 15:00 BST after Everton meet Chelsea at 12:30.',
    liveNow: 'Matchweek 7 Saturday kickoff: Everton vs Chelsea 12:30 BST, City vs Ipswich 15:00 BST, Brentford vs Liverpool 15:00 BST. City lead table with 18 points (6-0-0), Arsenal 15.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'MW7 SATURDAY: CITY HOST IPSWICH AT ETIHAD',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'United States GP: One week to Austin sprint. Antonelli leads Russell by 102 points.',
    liveNow: 'Austin COTA Sprint weekend 23-25 October, race Sunday 25 October at 15:00 local. Antonelli 340, Russell 238. Mercedes lead constructors with 578 points.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'ONE WEEK TO AUSTIN: MERCEDES EYE TITLE AT COTA',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'PGA Tour fall hiatus: Brennan title stands as Butterfield Bermuda tees off next week.',
    liveNow: 'PGA Tour off this weekend. Butterfield Bermuda Championship begins 22-25 October at Port Royal, $6 million purse. Brennan won Baycurrent at 16 under.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'PGA TOUR OFF: BERMUDA TEES OFF NEXT WEEK',
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
