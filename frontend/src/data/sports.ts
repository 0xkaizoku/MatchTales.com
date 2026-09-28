export const SITE_TODAY = '2026-09-29';

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
    tagline: 'WNBA Playoffs Game 2: Caitlin Clark and Fever aim to sweep Dream; Lynx host Mystics.',
    liveNow: 'Elimination night in Atlanta and Minneapolis: Fever lead 1-0; Dream face win-or-go-home pressure.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'PLAYOFFS GAME 2',
    board: 'Open the floor',
    span: 'hero',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'Eagles hold off Cowboys 24-20 on Monday Night Football as NFL Week 3 concludes.',
    liveNow: 'Hurts and Barkley power Philadelphia to 2-1 start. Week 4 begins Thursday with 49ers hosting Rams.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'EAGLES 24-20 MNF',
    board: 'Open the field',
    span: 'side',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Manchester City command Premier League summit on 18 points ahead of Matchweek 7.',
    liveNow: 'Haaland on 10 goals in 6 matches. City visit Brentford Saturday seeking seventh straight win.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'CITY ON 18 PTS',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'China Open 2026: Sinner and Alcaraz touch down in Beijing as main draw gets underway.',
    liveNow: 'National Tennis Center welcomes world top stars. Rybakina and Sabalenka headline WTA 1000 field.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'CHINA OPEN LIVE',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Formula 1 heads to Marina Bay: Antonelli holds 88-point cushion ahead of Singapore GP night race.',
    liveNow: 'Mercedes 1-2 in Baku puts Antonelli at 317 pts. Marina Bay floodlights and 19 corners up next.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'SINGAPORE BOUND',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'FedExCup Fall begins: Sanderson Farms Championship tees off at Country Club of Jackson.',
    liveNow: 'United States celebrate 18.5-11.5 Presidents Cup victory as tour moves to Mississippi.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'FALL SWING TEES OFF',
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
