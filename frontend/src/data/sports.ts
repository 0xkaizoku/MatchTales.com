export const SITE_TODAY = '2026-10-04';

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
    tagline: 'Premier League MW7: Brighton stun Tottenham 3-2 with three-goal second-half blitz; Chelsea held 1-1 by Forest.',
    liveNow: 'Minteh, Rutter, and Welbeck strike in 18 minutes to complete an epic Amex comeback. Brighton rise to fourth on 14 points.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'BRIGHTON 3-2 TOTTENHAM',
    board: 'Open the pitch',
    span: 'hero',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Singapore GP: Lando Norris converts pole into dominant 20-second victory over Max Verstappen at Marina Bay.',
    liveNow: 'Norris commands all 62 laps under the floodlights. Oscar Piastri finishes P3 for a McLaren double podium.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'NORRIS WINS IN SINGAPORE',
    board: 'Open the grid',
    span: 'side',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'China Open 2026: Carlos Alcaraz outlasts Jannik Sinner in 3h21m epic to capture Beijing championship.',
    liveNow: 'Alcaraz rallies from 0-3 in the final tiebreak to win 6-7(6), 6-4, 7-6(3). Coco Gauff sweeps WTA title 6-1, 6-3.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'ALCARAZ WINS BEIJING EPIC',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'NFL Week 4 Sunday Night Football: Derrick Henry runs wild as Ravens dismantle undefeated Bills 35-10.',
    liveNow: 'Henry explodes for 199 yards and two scores, including an 87-yard opening touchdown. Jackson totals three touchdowns.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'RAVENS 35-10 BILLS SNF',
    board: 'Open the field',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Sanderson Farms: Kevin Yu birdies 18th in sudden-death playoff against Beau Hossler for maiden PGA Tour title.',
    liveNow: 'Yu birdies the 72nd hole to shoot 67 and force extra holes at 23-under, then drains a five-foot birdie putt for the win.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'YU WINS PLAYOFF AT -23',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA Semifinals: Breanna Stewart powers Liberty past Aces 87-77; Napheesa Collier leads Lynx over Fever 88-82.',
    liveNow: 'Stewart drops 34 points at Barclays Center while Collier tallies 28 points at Target Center to claim 1-0 series leads.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'LIBERTY & LYNX TAKE G1',
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
    .filter(Boolean)
    .slice(0, 2)
    .map((w) => w[0]?.toUpperCase() || '')
    .join('');
}
