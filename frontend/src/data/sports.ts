export const SITE_TODAY = '2026-09-28';

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
    tagline: 'Monday Night Football: Cowboys battle Eagles at Lincoln Financial Field in Week 3 finale.',
    liveNow: 'NFC East rivalry live in prime time: Hurts and Eagles host Prescott and Cowboys in high-stakes divisional duel.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'MNF RIVALRY LIVE',
    board: 'Open the field',
    span: 'hero',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Team Europe wins 2026 Laver Cup! Alcaraz clinches 13-11 thriller at The O2.',
    liveNow: 'Alcaraz defeats Fritz in decisive final match. Europe reclaims trophy in front of 18,000 London fans.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'EUROPE CHAMPIONS',
    board: 'Open the court',
    span: 'side',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'United States wins 16th Presidents Cup at Medinah. Scheffler and Cantlay lead 18.5-11.5 triumph.',
    liveNow: 'American squad takes 10th consecutive cup as Snedeker team dominates Sunday singles.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'USA WINS CUP',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA Playoffs: Caitlin Clark powers Fever past Dream in Game 1; Lynx and Aces roll.',
    liveNow: 'Fever lead 1-0 after 86-80 road win in Atlanta. Game 2 elimination stakes await.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'PLAYOFFS GAME 1',
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Manchester City sit alone at Premier League summit on 18 points after MW6.',
    liveNow: 'City 6-0-0 with Haaland on 10 goals. Champions League Matchday 2 approaches midweek.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'CITY ON 18 PTS',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Formula 1 heads to Marina Bay: Antonelli holds 45-point cushion ahead of Singapore GP night race.',
    liveNow: 'Mercedes 1-2 in Baku puts Antonelli at 317 pts. Street circuit under the floodlights up next.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'SINGAPORE BOUND',
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
    .filter(Boolean)
    .slice(0, 2)
    .map((w) => w[0]?.toUpperCase() || '')
    .join('');
}
