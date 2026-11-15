export const SITE_TODAY = '2026-11-15';

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
    tagline: "NFL Munich Live: Lions lead Patriots 21-3 at half; Drake Maye exits with ankle injury.",
    liveNow: "LIVE Munich: Lions 21, Patriots 3 (St. Brown 56-yd TD, Gibbs TD, Borregales 33-yd FG). Maye hurt ankle. 2nd half in progress.",
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: "NFL MUNICH LIVE: LIONS LEAD PATRIOTS 21-3 AT HALF; DRAKE MAYE RULED OUT WITH ANKLE INJURY",
    board: 'Open the field',
    span: 'hero',
  },
  {
        slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: "Spain host England tonight in Madrid (19:45 GMT) for Group A3; Denmark stun Portugal 4-1.",
    liveNow: "Tonight: Spain vs England, 19:45 GMT Metropolitano. Sat: Denmark 4-1 Portugal; Sweden 3-2 Bosnia. PL: Arsenal 27, Brighton 22, City 21.",
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: "SPAIN VS ENGLAND TONIGHT IN MADRID; DENMARK STUN PORTUGAL 4-1 IN NATIONS LEAGUE",
    board: 'Open the pitch',
    span: 'side',
  },
  {
        slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: "Giannis 34 leads Heat 137-117 over Pistons; Proctor triple-double powers short-handed Cavs 127-117.",
    liveNow: "Sat: Heat 137-117 Pistons (Giannis 34, Klay 26, Cade 33); Cavs 127-117 Mavs (Proctor 24/11/10). Fri: Spurs 123-85 Warriors (11 straight).",
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: "NBA SATURDAY: HEAT 137-117 PISTONS, GIANNIS 34; PROCTOR TRIPLE-DOUBLE LEADS CAVS OVER MAVS",
    board: 'Open the floor',
    span: 'half',
  },
  {
        slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: "Dubai Finale Complete: Tyrrell Hatton fires 66 to win by 5 at -15; Rory McIlroy seals 8th Race to Dubai title.",
    liveNow: "Dubai Final: 1. Tyrrell Hatton -15 (273, 66); 2. Rory McIlroy -10 (278, 67, Race to Dubai champion); T3. Chacarra -9 (279), Lindell -9. Final.",
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: "DUBAI FINALE: HATTON WINS ON 273 (-15); MCILROY (278, -10) SEALS EIGHTH RACE TO DUBAI CROWN",
    board: 'Open the course',
    span: 'half',
  },
  {
        slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: "Turin ATP Finals: Zverev sweeps Jodar 6-4, 6-4; Fritz outlasts Tirante in Stockholm final.",
    liveNow: "Turin Sun: Zverev d Jodar 6-4, 6-4; Shelton vs Fils tonight (20:30 CET). Stockholm Sat Final: Fritz d Tirante 6-2, 4-6, 7-6 (3).",
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: "TURIN ATP FINALS OPEN: ZVEREV SWEEPS JODAR 6-4, 6-4; FRITZ WINS STOCKHOLM IN DECIDING TIEBREAK",
    board: 'Open the court',
    span: 'half',
  },
  {
        slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: "Four days to Round 21 Las Vegas: 33 points still split Verstappen to Norris. No Strip race yet.",
    liveNow: "Drivers P2 race unchanged: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). Round 21: 19-21 Nov.",
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: "FOUR DAYS TO VEGAS: VERSTAPPEN TO NORRIS STILL 33 PTS BEHIND CHAMPION ANTONELLI",
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
    .map((p) => p[0])
    .filter(Boolean)
    .slice(0, 2)
    .join('')
    .toUpperCase();
}
