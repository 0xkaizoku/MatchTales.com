export const SITE_TODAY = '2026-09-30';

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
    tagline: 'WNBA Playoffs: Caitlin Clark leads Fever to sweep Dream 2-0; Lynx sweep Mystics into semifinals.',
    liveNow: 'Indiana and Minnesota advance to final four. Elimination night continues Wednesday: Wings at Aces, Liberty at Valkyries.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'FEVER & LYNX SWEEP',
    board: 'Open the floor',
    span: 'hero',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Champions League Matchday 2: Arsenal host PSG at Emirates as European heavyweights collide.',
    liveNow: 'Arteta and Enrique clash in North London. Manchester City visit Slovan Bratislava; Premier League MW7 awaits.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'UCL ARSENAL VS PSG',
    board: 'Open the pitch',
    span: 'side',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'NFL Week 4 begins Thursday: 49ers host Rams at Levi\'s Stadium in NFC West rivalry clash.',
    liveNow: 'Eagles 24-20 MNF win puts Week 3 in books. Purdy and Stafford square off on short rest.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'TNF 49ERS VS RAMS',
    board: 'Open the field',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'China Open 2026: Sinner launches title defense with straight-sets win; Sabalenka and Zheng roll.',
    liveNow: 'World No. 1 Sinner downs Safiullin 6-3, 6-4 at National Tennis Center. Alcaraz and Rybakina up next.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'SINNER ROLLS BEIJING',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Formula 1 arrives in Singapore: Antonelli commands 88-point cushion as Marina Bay paddock opens.',
    liveNow: 'Paddock setups complete under 30C tropical heat. 1,600 floodlights and 19 corners await Friday practice.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'MARINA BAY PADDOCK',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Sanderson Farms Championship: Pro-Am wraps at Country Club of Jackson ahead of Round 1.',
    liveNow: 'Defending champion Kevin Yu groups with Mackenzie Hughes for Thursday morning tee-off in Mississippi.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'ROUND 1 EVE JACKSON',
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
