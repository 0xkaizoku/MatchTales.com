export const SITE_TODAY = '2026-10-08';

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
    tagline: 'Week 5 TNF is Buccaneers (0-4) at Cowboys (2-2), 8:15 p.m. ET. Chiefs, Vikings and 49ers are 4-0. No score yet.',
    liveNow: 'AT&T Stadium, Prime Video. Falcons are 2-2 and host the Ravens Sunday night. Chiefs are on a bye after a 30-27 win at the Raiders.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'TNF: BUCCANEERS AT COWBOYS',
    board: 'Open the field',
    span: 'hero',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Nations League window is closed. Spain and Portugal are through on 12 points. France 10, Italy 7, England 9.',
    liveNow: 'Monday: France 4-1 Belgium, Italy 3-1 Turkiye. Tuesday: England 3-0 Czechia, Croatia 1-2 Spain. Premier League still City 15 from five.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'SPAIN AND PORTUGAL THROUGH',
    board: 'Open the pitch',
    span: 'side',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA semis are 1-0, not 1-1. Dream beat Liberty 92-82. Valkyries beat Aces 71-60. Game 2 has no verified final.',
    liveNow: 'Game 2 is on the 7 October schedule: Liberty at Dream 7:30 p.m. ET, Aces at Valkyries 9:30. Allisha Gray is out. No box score is printed.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA SEMIS STILL 1-0',
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Shanghai first round is open, not round 2. Ten Wednesday results are in. Zverev, Alcaraz and Djokovic have not played.',
    liveNow: 'Djokovic beat de Minaur 7-6 (3), 0-1 ret in Beijing. Alcaraz beat Lehecka 7-6 (4), 6-4 in Tokyo. Both are on a Shanghai bye.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'SHANGHAI FIRST ROUND OPEN',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Baycurrent Classic first tee at Yokohama Country Club. Par 71, 7,322 yards, 8 million dollars. No round score posted.',
    liveNow: 'Spieth, Schauffele, Morikawa and Matsuyama have Thursday groups. The board is pairings, not a leader.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'BAYCURRENT FIRST TEE',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Singapore sprint weekend is next. Antonelli 320, Russell 236, an 84-point gap. No Austin result and no Singapore result.',
    liveNow: 'Hamilton 214, Leclerc 191, Norris 188, Verstappen 188. Verstappen won at Sepang on 4 October. Race in Singapore is Sunday 11 October.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'SINGAPORE NEXT, GAP 84',
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
