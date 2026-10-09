export const SITE_TODAY = '2026-10-09';

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
    tagline: 'Week 5 TNF final: Buccaneers beat Cowboys 24-16 for first win of 2026. Jalon Daniels stars. Dallas falls to 2-3.',
    liveNow: 'Daniels 19 of 25 for 189 yards and 1 TD. Bucky Irving adds two scores. Chiefs, Vikings and 49ers remain 4-0.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'TNF: BUCCANEERS 24, COWBOYS 16',
    board: 'Open the field',
    span: 'hero',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA semifinals: Dream and Valkyries take 2-0 leads. Game 3 double-header tonight in New York and Las Vegas.',
    liveNow: 'Dream won 101-98 in OT; Valkyries won 83-81. Liberty (7:30 p.m. ET) and Aces (9:30 p.m. ET) face elimination tonight.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA SEMIS: GAME 3 TONIGHT',
    board: 'Open the floor',
    span: 'side',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Shanghai Masters Round 2: Hubert Hurkacz stuns Novak Djokovic 6-4, 6-3. Zverev and Shelton advance.',
    liveNow: 'Hurkacz earns first win in nine tries against Djokovic. Zverev def. Wu 6-4, 7-6(4). Sakamoto upsets Rublev.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'HURKACZ STUNS DJOKOVIC',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Singapore GP: Max Verstappen takes Sprint pole with 1:31.156. George Russell joins him on the front row.',
    liveNow: 'Verstappen edges Russell by 0.120s. Leclerc third, Piastri fourth, Norris fifth, Antonelli seventh. Sprint race Saturday.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'VERSTAPPEN SPRINT POLE',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Baycurrent Classic Round 2: Keith Mitchell and Jacob Bridgeman share the 36-hole lead at 11 under in Yokohama.',
    liveNow: 'Mitchell and Bridgeman at -11. Homa, Bauchou, Kohles and Meissner sit two back at -9. Yokohama Country Club, par 71.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'MITCHELL & BRIDGEMAN LEAD (-11)',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Premier League returns Saturday with Matchweek 6. Manchester City lead on 15 points, Arsenal 12, Brighton 10.',
    liveNow: 'Saturday features Arsenal vs Leeds and Man United vs Spurs. Sunday brings Liverpool vs Manchester City at Anfield.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'PREMIER LEAGUE MW6 EVE',
    board: 'Open the pitch',
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
