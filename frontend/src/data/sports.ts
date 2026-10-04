export const SITE_TODAY = '2026-10-05';

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
    tagline: 'Dream beat Liberty 92-82 and lead 1-0. Valkyries beat Aces 71-60 and lead 1-0. Game 2 is not final.',
    liveNow: 'Canada scored 25 for Atlanta. Williams had 25 points, 11 rebounds and 5 assists for Golden State. Wilson scored 24. Game 2 is not in the book.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'DREAM 92, VALKYRIES 71',
    board: 'Open the floor',
    span: 'hero',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Djokovic beat Zverev 4-6, 6-4, 6-4 in Beijing. Alcaraz beat Shapovalov 7-6 (3), 2-1 retired in Tokyo. Semifinals are next.',
    liveNow: 'ATP quarterfinals are final. Medvedev, de Minaur and Hurkacz also won in Beijing. Sinner remains out of Shanghai. Monday is not in the book.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'DJOKOVIC AND ALCARAZ THROUGH',
    board: 'Open the court',
    span: 'side',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'Week 4 finals include Patriots 29, Bills 26, and Colts 30, Commanders 13 in London. The late window, Sunday night and Monday night are not final.',
    liveNow: 'ESPN finals also include Giants 36-24, Cowboys 34-30, Rams 24-20, Bears 23-12, Ravens 24-18, Packers 17-14 and Jaguars 22-17. No late-window score is printed.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'PATRIOTS 29, BILLS 26',
    board: 'Open the field',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Portugal beat Norway 2-1 in Porto without Ronaldo and reached the Nations League quarterfinals. England 7-0 and Spain 3-1 stay in the book. The Premier League returns 10 October.',
    liveNow: 'Ajer 36, Cancelo 38, Ramos 79. Conceição was sent off and did not score. City still lead a frozen table with 15 points from five. Monday is not final.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'PORTUGAL 2-1 NORWAY',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Verstappen won the Bahrain Grand Prix in Malaysia. Antonelli was second and leads by 84 points, 320 to Russell on 236.',
    liveNow: 'Hamilton finished third. Russell retired and scored 0. Mercedes 556, Ferrari 405. Singapore is not a result.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'VERSTAPPEN WINS AT SEPANG',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Smotherman led by one at 23 under after 54 holes (63-62-65). The final round is under way. No winner is printed.',
    liveNow: 'PGA and AP: 190, a 54-hole record. Ghim 191. Crowe, James and Streelman 195. Moving Sunday numbers are not a result.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'SMOTHERMAN -23 AFTER 54',
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
