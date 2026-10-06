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
    tagline: 'Week 5 kickoff tonight: Falcons visit Buccaneers in NFC South showdown. Chiefs and Vikings stand 4-0.',
    liveNow: 'TNF at Raymond James Stadium (8:15 PM ET). Atlanta seek bounce-back on short rest; Tampa Bay defend home turf.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'TNF: FALCONS AT BUCCANEERS',
    board: 'Open the field',
    span: 'hero',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Nations League Matchday 3 tonight: Italy host Belgium in Rome; England face Greece at Wembley.',
    liveNow: 'Ten fixtures tonight. Azzurri seek Group A2 command; Carsley side back at Wembley. Portugal already through to QFs.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'NATIONS LEAGUE MD3 LIVE',
    board: 'Open the pitch',
    span: 'side',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA Semifinals all square at 1-1: Liberty edge Dream 86-80; Aces top Valkyries 83-74 in road responses.',
    liveNow: 'Ionescu (26 pts) and Wilson (28 pts, 13 reb) spark Game 2 road triumphs. Series head to New York and Las Vegas.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA SEMIS TIED 1-1',
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Shanghai Masters Round 2 ready: Alcaraz (10 straight wins) and Djokovic join top seed Zverev as main draw heats up.',
    liveNow: 'Round 1 in the books at Qizhong Arena. Top 32 seeds enter Round 2. Sinner out; Alcaraz and Djokovic chase Asian double.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'SHANGHAI MASTERS ROUND 2',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Baycurrent Classic Round 1 underway at Yokohama Country Club: Ghim and Yu pursue FedExCup Fall points in Japan.',
    liveNow: 'Inaugural PGA Tour event in Yokohama. 500 FedExCup points at stake. Smotherman 51st in standings after Utah record.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'BAYCURRENT CLASSIC ROUND 1',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Americas triple-header countdown: Antonelli holds 84-point lead over Russell. Red Bull fast-tracks Austin floor upgrades.',
    liveNow: 'Antonelli 320, Russell 236, Hamilton 214, Verstappen 188. Red Bull floor revision for COTA; Lawson 10-place penalty confirmed.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'COTA UPGRADES COUNTDOWN',
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
