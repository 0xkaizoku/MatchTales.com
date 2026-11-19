export const SITE_TODAY = '2026-11-17';

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
    tagline: "Germany crush Netherlands 5-0 in Nations League romp; England hold off Spain 3-2 in Madrid.",
    liveNow: "Mon: Germany 5-0 Netherlands (Wirtz 60, 77, Scherhant, Schlotterbeck, Gruda); Greece 1-0 Serbia. Sun: Spain 2-3 England. PL: Arsenal 27, Brighton 22, City 21.",
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: "NATIONS LEAGUE: GERMANY CRUSH NETHERLANDS 5-0 TO CLINCH GROUP A2; WIRTZ SCORES BRACE",
    board: 'Open the pitch',
    span: 'hero',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: "MNF Final: Chargers edge Ravens 23-20 in Harbaugh Bowl; Lions rout Patriots 35-10 in Munich.",
    liveNow: "MNF: Chargers 23, Ravens 20 (Herbert 22-yd TD run, Hampton 105 yds, Still forced fumble). Sun Munich: Lions 35-10 Patriots (Gibbs 252 yds, 2 TDs).",
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: "MNF FINAL: CHARGERS SURVIVE RAVENS 23-20 IN HARBAUGH BOWL AS JIM EDGES JOHN",
    board: 'Open the field',
    span: 'side',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: "Turin ATP Finals: Alcaraz storms past Tiafoe 6-2, 6-2; Zverev meets Shelton in Tuesday night clash.",
    liveNow: "Mon Lendl: Alcaraz d Tiafoe 6-2, 6-2; Medvedev d Cobolli 7-6 (4), 6-3. Tue McEnroe: Fils vs Jodar (14:00 CET), Zverev vs Shelton (20:30 CET).",
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: "TURIN ATP FINALS: ALCARAZ SWEEPS TIAFOE 6-2, 6-2; ZVEREV VS SHELTON TONIGHT IN MCENROE GROUP",
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: "Magic rally past Celtics 115-105 to snap Boston streak; Heat extend run to five behind Giannis.",
    liveNow: "Mon: Magic 115-105 Celtics (Bane 24); Heat 128-110 Rockets (Giannis 20/13/6, 5th straight win); 76ers 135-123 Nets (Embiid 37); Suns 117-105 Nuggets.",
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: "NBA MONDAY: MAGIC END CELTICS STREAK 115-105; HEAT EXTEND RUN TO FIVE BEHIND GIANNIS",
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: "RSM Classic practice underway at Sea Island with top-125 cards on the line; McIlroy savors 8th crown.",
    liveNow: "PGA Tour: RSM Classic tournament week begins at Sea Island (19-22 Nov). DP World Tour Complete: Hatton -15 (273); McIlroy -10 (278, 8th Race to Dubai).",
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: "PGA TOUR FALL FINALE: RSM CLASSIC PRACTICE UNDERWAY AT SEA ISLAND AS PLAYERS CHASE TOP-125 CARDS",
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: "Two days to Round 21 Las Vegas: Strip setup finishes as five-driver battle for P2 heats up.",
    liveNow: "Drivers P2 shootout: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). Vegas Strip: 19-21 Nov.",
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: "TWO DAYS TO VEGAS: VERSTAPPEN TO NORRIS SPLIT BY 33 POINTS AHEAD OF THURSDAY PRACTICE",
    board: 'Open the grid',
    span: 'half',
  },
];

export function sportBySlug(slug: string): SportMeta | undefined {
  return SPORTS.find((s) => s.slug === slug);
}

export function getSport(slug: string): SportMeta | undefined {
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
    .map((p) => p[0])
    .filter(Boolean)
    .slice(0, 2)
    .join('')
    .toUpperCase();
}
