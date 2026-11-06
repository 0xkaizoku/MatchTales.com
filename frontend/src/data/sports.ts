export const SITE_TODAY = '2026-11-06';

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
    tagline: 'NFL Week 9 TNF: Jaguars thrash depleted Ravens 33-10 behind Lawrence, four Little field goals.',
    liveNow: 'Final in Baltimore: Jaguars 33, Ravens 10. Lawrence 242 yds, 50-yd TD; Little 4 FGs; Fagnano 2 INT. Jaguars 6-2, Ravens 4-5.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'NFL WEEK 9 TNF: JACKSONVILLE JAGUARS THRASH RAVENS 33-10; JAGUARS 6-2, RAVENS 4-5',
    board: 'Open the field',
    span: 'hero',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'NBA: Wembanyama posts 52 points, 24 rebounds, 8 blocks as Spurs edge Mavericks 112-111.',
    liveNow: 'Final in San Antonio: Spurs 112, Mavericks 111. Wembanyama 52-24-8; winning FT 24.2s. Spurs 6-2. Cavs are 4-4.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'NBA: WEMBANYAMA 52-24-8 AS SPURS EDGE MAVERICKS 112-111 FOR SIXTH STRAIGHT',
    board: 'Open the floor',
    span: 'side',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'UCL MD4: Haaland winner as Manchester City edge RB Leipzig 3-2. Arsenal lead Premier League on 24 points.',
    liveNow: 'Final in Leipzig: RB Leipzig 2-3 Manchester City (Lukeba OG 37, Baku 49, Fernandez 58, Nusa 61, Haaland 78). City 3-1, 7th in UCL.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'UCL MD4: HAALAND 78TH-MINUTE WINNER LIFTS CITY PAST LEIPZIG 3-2; ARSENAL LEAD PL ON 24',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Rolex Paris Masters QF: Ben Shelton beats Tommy Paul 6-4, 4-6, 6-3 to reach first Bercy semi-final.',
    liveNow: 'Paris Masters QF: Shelton def. Paul 6-4, 4-6, 6-3 in 1h46m, 19 aces. Tiafoe qualifies for Turin; Paul is out.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'ROLEX PARIS MASTERS: BEN SHELTON BEATS TOMMY PAUL TO REACH FIRST BERCY SEMI-FINAL',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'São Paulo GP FP1: Lando Norris leads Kimi Antonelli and Max Verstappen at Interlagos.',
    liveNow: 'FP1: Norris 1:11.717, Antonelli +0.082s, Verstappen +0.236s. No Sprint. Mercedes 630, Ferrari 504 after Mexico.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'F1 INTERLAGOS FP1: NORRIS LEADS ANTONELLI; NO SPRINT; MERCEDES 630, FERRARI 504',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'WWT Championship Round 1: Chris Kirk fires bogey-free 63 to lead by one at El Cardonal.',
    liveNow: 'R1 complete: Kirk 63 leads Dunlap and Blair 64. Purse $6 million. Round 2 in progress, unpublished as final.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'PGA TOUR CABO R1: CHRIS KIRK 63 LEADS WWT CHAMPIONSHIP; FEDEXCUP FALL CARDS ON THE LINE',
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
