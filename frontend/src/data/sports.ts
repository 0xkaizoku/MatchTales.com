export const SITE_TODAY = '2026-11-07';

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
    tagline: 'NFL Week 9 Madrid: Bengals visit Falcons at Bernabeu on Sunday, 9:30 a.m. ET. Saturday has no NFL game.',
    liveNow: 'UPCOMING Sunday in Madrid: Bengals (5-2) at Falcons (3-5), 9:30 a.m. ET, NFL Network. Last final: Jaguars 33, Ravens 10. No Saturday game.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'NFL WEEK 9 MADRID: BENGALS AT FALCONS SUNDAY 9:30 A.M. ET; LAST FINAL JAGUARS 33-10',
    board: 'Open the field',
    span: 'hero',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'NBA: Luka Doncic scores 53 as Lakers rally past Trail Blazers 124-118.',
    liveNow: 'Final in Los Angeles: Lakers 124, Trail Blazers 118. Doncic 53; Reaves 25. Spurs 7-2. Cavs are 5-4.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'NBA: DONCIC 53 AS LAKERS BEAT TRAIL BLAZERS 124-118; SPURS 7-2, CAVS 5-4',
    board: 'Open the floor',
    span: 'side',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Premier League MW10: Noah Okafor winner as Leeds beat Tottenham 1-0. Arsenal still 24 from 9.',
    liveNow: 'Final at Elland Road: Leeds 1-0 Tottenham (Okafor 79). Friday: Everton 3-1 Coventry. Arsenal vs Hull unpublished.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'PREMIER LEAGUE MW10: OKAFOR 79TH-MINUTE WINNER LIFTS LEEDS PAST TOTTENHAM 1-0',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Rolex Paris Masters SF: Ben Shelton beats Luca Van Assche 5-7, 6-3, 6-4 to reach the final.',
    liveNow: 'Paris Masters SF: Shelton def. Van Assche 5-7, 6-3, 6-4. First American finalist since Sock 2017. Alcaraz vs Ruud unpublished.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'ROLEX PARIS MASTERS: BEN SHELTON BEATS VAN ASSCHE TO REACH THE BERCY FINAL',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Sao Paulo GP FP3: Max Verstappen leads Kimi Antonelli by 0.025s at Interlagos.',
    liveNow: 'FP3: Verstappen 1:11.622, Antonelli +0.025s, Norris +0.131s. Qualifying unpublished. Mercedes 630, Ferrari 504.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'F1 INTERLAGOS FP3: VERSTAPPEN LEADS ANTONELLI BY 0.025S; QUALIFYING UNPUBLISHED',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'WWT Championship Round 2: Ben James shoots 64 to lead at 15 under at El Cardonal.',
    liveNow: 'R2 complete: James 129 (-15) leads Malnati 130. Kirk 135. Cut 139. Round 3 unpublished as final.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'PGA TOUR CABO R2: BEN JAMES 129 LEADS WWT CHAMPIONSHIP; ROUND 3 UNPUBLISHED',
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
