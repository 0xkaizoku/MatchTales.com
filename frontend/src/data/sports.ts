export const SITE_TODAY = '2026-10-07';

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
    tagline: 'WNBA Semifinals: Liberty hold off Aces 88-84 to seize 2-0 lead; Lynx top Fever 84-78 behind Collier 26 pts.',
    liveNow: 'Sabrina Ionescu drops 24 points in Game 2 thriller; defending champion Aces face must-win Game 3 in Las Vegas.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'LIBERTY & LYNX LEAD 2-0',
    board: 'Open the floor',
    span: 'hero',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Rolex Shanghai Masters: Alcaraz cruises to 10th consecutive win; Sinner claims 60th victory of the season in R2.',
    liveNow: 'Alcaraz defeats Shang 6-2, 6-2 in 76 minutes; Sinner tops Daniel 6-1, 6-4 as Djokovic prepares tournament return.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'ALCARAZ 10TH STRAIGHT WIN',
    board: 'Open the court',
    span: 'side',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'NFL Week 5 TNF Eve: Buccaneers and Falcons clash for NFC South supremacy; Chiefs and Vikings stay 4-0 unbeatens.',
    liveNow: 'Baker Mayfield (8 TDs, 106.9 rating) leads Bucs into Atlanta; Kirk Cousins seeks first place on prime time.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'TNF: BUCS AT FALCONS',
    board: 'Open the field',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'International Window: Nations League MD3 brings Italy vs Belgium blockbuster; Brazil under pressure in Chile.',
    liveNow: 'Spalletti Azzurri chase third straight win in Rome; Messi returns for Argentina while club football takes a breath.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'NATIONS LEAGUE & CONMEBOL',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'F1 Americas Triple-Header: Red Bull finalizes crucial Austin floor upgrade; Liam Lawson faces grid penalty on debut.',
    liveNow: 'Norris trails Verstappen by 52 points with six rounds left; McLaren defends 41-point constructors lead heading to Texas.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'RED BULL UPGRADE & LAWSON',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'PGA Tour: Black Desert Championship Round 1 tee times locked as tour returns to Utah for first time since 1963.',
    liveNow: 'Sanderson Farms champion Kevin Yu grouped with Keith Mitchell and Beau Hossler amid red rocks and black basalt lava.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'BLACK DESERT ROUND 1 EVE',
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
