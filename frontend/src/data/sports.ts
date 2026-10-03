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
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA semifinals open today: Liberty at Dream, 2:00 p.m. ET on ABC. Aces at Valkyries, 4:00 p.m. ET on NBC. Both series are 0-0.',
    liveNow: 'New York swept Minnesota 91-75 and 87-71. Atlanta swept Washington 92-77 and 93-75. No Game 1 score is final on this desk.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'SEMIS GAME 1, SERIES 0-0',
    board: 'Open the floor',
    span: 'hero',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Asia swing: Alcaraz beat Arnaldi 7-6 (6), 6-1 in Tokyo. Zverev beat Shang 6-0, 6-3 in Beijing. Sinner is out of Shanghai.',
    liveNow: 'ATP: quarter-finals in Beijing and Tokyo are next. Field Level Media: Sinner misses Shanghai with a knee injury.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'ALCARAZ AND ZVEREV THROUGH',
    board: 'Open the court',
    span: 'side',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'Week 4: Browns 27, Steelers 24 is the only final. Sunday, including London, is still on the board.',
    liveNow: 'CBS and ESPN list Colts at Commanders, Patriots at Bills (3-0), and Vikings (3-0). No Sunday score is printed here.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'BROWNS 27, STEELERS 24',
    board: 'Open the field',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Nations League: England beat Croatia 7-0 in Rijeka. Spain beat Czechia 3-1 in Oviedo. The Premier League returns 10 October.',
    liveNow: 'Kane and Saka scored twice each. Yamal, Rodri and Merino scored for Spain. City still lead a frozen table with 15 points from five.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'ENGLAND 7-0, SPAIN 3-1',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Bahrain Grand Prix in Malaysia: Verstappen on pole at Sepang, 1:35.130. Hamilton is alongside, 0.298s back. The race is Sunday.',
    liveNow: 'Antonelli leads on 302 points, 66 ahead of Russell. Hadjar qualified third and has a five-place grid penalty. No race winner is printed.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'VERSTAPPEN POLE AT SEPANG',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Bank of Utah Championship: Smotherman led by one at 17 under after 36 holes. Sunday round 3 is under way. No winner is printed.',
    liveNow: 'AP and PGA Tour: 63-62, 125. Kevin Roy 126. Ghim and Streelman 127. The live board is not a final.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'SMOTHERMAN -17 AFTER 36',
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
