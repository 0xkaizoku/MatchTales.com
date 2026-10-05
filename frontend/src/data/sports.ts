export const SITE_TODAY = '2026-10-06';

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
    tagline: 'WNBA Semifinals Game 2 eve: Dream lead Liberty 1-0 and Valkyries lead Aces 1-0. Game 2 double-header is Wednesday.',
    liveNow: 'Jordin Canada (25 pts) and Gabby Williams (25-11-5) led opening wins. Defending finalists seek road adjustments on 7 October.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA SEMIS GAME 2 EVE',
    board: 'Open the floor',
    span: 'hero',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Beijing and Tokyo finals are set: Djokovic faces De Minaur; Alcaraz battles Lehecka. Sinner remains out of Shanghai.',
    liveNow: 'Djokovic led 7-5, 5-3 when Medvedev defaulted. De Minaur advanced over Hurkacz (ret). Alcaraz beat Munar 5-7, 6-3, 6-1. Finals Tuesday.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'DJOKOVIC AND ALCARAZ IN FINALS',
    board: 'Open the court',
    span: 'side',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'Week 4 is in the book: Chiefs (30-27) and Vikings (15-10) stand as lone 4-0 unbeatens. Panthers beat Lions 32-26 on Sunday night.',
    liveNow: 'Late window finals: 49ers 24-14, Seahawks 30-23. Week 5 opens Thursday with Buccaneers at Falcons in an NFC South clash.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'CHIEFS AND VIKINGS 4-0',
    board: 'Open the field',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Nations League: Portugal reach quarterfinals with 2-1 over Norway. Germany held 0-0 by Greece. Premier League returns 10 October.',
    liveNow: 'Cancelo and Ramos send Portugal through (4-0-0, 12 pts). Germany sit third in Group A2. City lead frozen Premier League with 15 pts.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'PORTUGAL THROUGH, GERMANY 0-0',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Aftermath of Sepang: Verstappen breakthrough win, Antonelli leads by 84 points. Paddock readies Austin floor upgrades.',
    liveNow: 'Verstappen on 188 pts, level with Norris. Antonelli 320, Russell 236, Hamilton 214. Mercedes 556, Ferrari 405. COTA sprint next.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'ANTONELLI +84, AUSTIN UPGRADES',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Austin Smotherman shot 26 under (258) to win maiden PGA Tour title at Bank of Utah Championship. Doug Ghim runner-up at 24 under.',
    liveNow: 'Smotherman (63-62-65-68) sets 72-hole scoring record in 100th start, leaping to 51st in FedExCup Fall. Ghim finishes two back at 260.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'SMOTHERMAN WINS IN UTAH (-26)',
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
