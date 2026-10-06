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
    tagline: 'WNBA Semifinals Game 2 tonight: Dream guard 1-0 lead against Liberty; Valkyries host Aces in San Francisco.',
    liveNow: 'Atlanta host New York at 7:30 PM ET; Golden State host Las Vegas at 9:30 PM ET. Underdogs look to build 2-0 series advantages.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA SEMIS GAME 2 TONIGHT',
    board: 'Open the floor',
    span: 'hero',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Djokovic and Alcaraz claim Beijing and Tokyo crowns. Shanghai Masters ATP 1000 main draw begins in China.',
    liveNow: 'Djokovic wins 102nd title as De Minaur retires (7-6, 0-1). Alcaraz beats Lehecka 7-6, 6-4 for 10th straight win. Shanghai R1 underway.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'DJOKOVIC & ALCARAZ WIN TITLES',
    board: 'Open the court',
    span: 'side',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'Week 5 kicks off Thursday night: Chiefs (4-0) and Vikings (4-0) pace the league. Falcons visit Buccaneers in NFC South battle.',
    liveNow: 'Only Kansas City and Minnesota stay perfect. Week 5 opens Thursday at Raymond James Stadium. Power rankings locked.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'CHIEFS & VIKINGS 4-0, TNF EVE',
    board: 'Open the field',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Nations League Matchday 3 eve: Italy host Belgium in Rome; England face Greece at Wembley. Portugal already through to QFs.',
    liveNow: 'Thursday brings 10 Nations League fixtures. City lead frozen Premier League with 15 pts until Saturday 10 October restart.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'NATIONS LEAGUE MD3 EVE',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Austin countdown begins: Antonelli leads Russell by 84 points. Red Bull brings major floor upgrade for Verstappen at COTA.',
    liveNow: 'Antonelli 320, Russell 236, Hamilton 214, Verstappen 188. Lawson confirmed for 10-place grid penalty in Texas.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'AUSTIN RED BULL UPGRADES',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'PGA Tour heads to Japan for Baycurrent Classic at Yokohama Country Club following Austin Smotherman Utah triumph.',
    liveNow: 'Smotherman (-26, 258 record) moves to 51st in FedExCup Fall. Field gathers in Yokohama for Wednesday pro-am and R1 tee times.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'BAYCURRENT CLASSIC JAPAN EVE',
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
