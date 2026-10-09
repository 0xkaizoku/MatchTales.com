export const SITE_TODAY = '2026-10-10';

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
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Premier League Matchweek 6 kicks off Saturday. Arsenal host Leeds at 12:30 BST, Man United meet Spurs at 17:30 BST.',
    liveNow: 'Manchester City lead with 15 points (5-0-0), Arsenal 12, Brighton 10. Sunday blockbuster brings Liverpool vs City at Anfield.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'PREMIER LEAGUE MW6 SATURDAY',
    board: 'Open the pitch',
    span: 'hero',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'Saturday brings 122nd Red River Rivalry (Texas vs Oklahoma at Cotton Bowl). NFL Week 5 Sunday slate looms.',
    liveNow: 'Buccaneers beat Cowboys 24-16 on TNF. Sunday brings Ravens at Falcons on SNF; Chiefs, Vikings and 49ers stand 4-0.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'RED RIVER RIVALRY SATURDAY',
    board: 'Open the field',
    span: 'side',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Singapore GP Saturday: Max Verstappen and George Russell share front row for the 100km Sprint, followed by GP Qualifying.',
    liveNow: 'Verstappen took Sprint pole (1:31.156) ahead of Russell (+0.120). Leclerc third, Piastri fourth, championship leader Antonelli seventh.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'SINGAPORE SPRINT & QUALIFYING',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Baycurrent Classic Round 3: Mitchell (-11) and Bridgeman (-11) lead into Moving Day paired with Max Homa (-9).',
    liveNow: 'Yokohama Country Club par 71: leaders tee off at 10:36 AM JST. Bauchou, Kohles and Meissner also two shots back at -9.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'BAYCURRENT MOVING DAY (-11)',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Shanghai Masters Round of 32: draw blown wide open after Hubert Hurkacz shocked Novak Djokovic 6-4, 6-3.',
    liveNow: 'Hurkacz snapped 0-8 streak against Djokovic. Zverev, Shelton, Sakamoto and Mannarino in action as round of 32 continues at Qizhong.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'SHANGHAI ROUND OF 32',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA semifinals: Atlanta Dream and Golden State Valkyries hold 2-0 series advantages as elimination weekend unfolds.',
    liveNow: 'Game 2 saw Dream beat Liberty 101-98 in OT and Valkyries defeat Aces 83-81. Lower seeds control both best-of-five battles.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA ELIMINATION WEEKEND',
    board: 'Open the floor',
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
