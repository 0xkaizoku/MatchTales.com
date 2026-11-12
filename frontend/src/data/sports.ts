export const SITE_TODAY = '2026-11-12';

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
    tagline: "UWCL & Nations League Tonight: Barcelona host Arsenal at Camp Nou; England face Croatia at Wembley after OL Lyonnes crushed Juventus 6-0.",
    liveNow: "Tonight: Barcelona vs Arsenal (18:45 CET Camp Nou); England vs Croatia (19:45 UK), Italy vs France, Czechia vs Spain (20:45 CET). Wed UWCL: Juventus 0-6 OL Lyonnes.",
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: "TONIGHT: BARCELONA VS ARSENAL AT CAMP NOU & ENGLAND VS CROATIA AFTER LYON 6-0 AT JUVENTUS",
    board: 'Open the pitch',
    span: 'hero',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: "TNF Tonight (8:15 p.m. ET, Prime Video): Both Jayden Daniels & J.J. McCarthy cleared for Giants White Out vs Commanders.",
    liveNow: "Tonight 8:15 p.m. ET: Commanders (2-5-1, C Patrick & TE Yankoff OUT, Daniels cleared) at Giants (5-2-1, McCarthy/Nabers/Skattebo active). MNF Final: Bills 23, Vikings 6.",
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: "NFL TNF TONIGHT: JAYDEN DANIELS & J.J. MCCARTHY CLEARED FOR METLIFE WHITE OUT REMATCH",
    board: 'Open the field',
    span: 'side',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: "NBA: Harden's 32 leads Cavaliers past Knicks 115-107; Rockets beat Warriors 115-108 as Curry exits Q1 injured.",
    liveNow: "Wed Finals: Cavaliers 115, Knicks 107 (Harden 32, Brunson 27); Rockets 115, Warriors 108 (Curry Q1 inj., Sengun 19); Celtics 98, Raptors 93 (-22 rally). Tonight: 4 NBA games.",
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: "NBA: HARDEN DROPS 32 AT MSG, WARRIORS LOSE CURRY EARLY AT HOUSTON & CELTICS RALLY FROM 22",
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: "Dubai R1 Complete: Joost Luiten fires 67 (-5) to lead Jacob Skov Olesen (68) & Rory McIlroy (69, T3).",
    liveNow: "Dubai R1: 1. Joost Luiten -5 (67); 2. Jacob Skov Olesen -4 (68); T3. Rory McIlroy -3 (69), Perez, De Leo, Schott, Laporta; T28. Eugenio Chacarra E (72).",
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: "DUBAI R1: LUITEN LEADS ON 67 (-5) WHILE MCILROY OPENS 69 TO GAIN THREE ON CHACARRA",
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: "Turin Draw Set: Zverev anchors McEnroe Group & Alcaraz leads Lendl Group; Fritz faces Rune today in Stockholm QF.",
    liveNow: "Turin: McEnroe = Zverev (1), Shelton (3), Fils (6), Jodar (8); Lendl = Alcaraz (2), Medvedev (4), Cobolli (5), Tiafoe (7). Stockholm Today: Fritz vs Rune QF.",
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: "NITTO ATP FINALS DRAW SET: ALCARAZ & ZVEREV SPLIT IN TURIN AS FRITZ MEETS RUNE IN STOCKHOLM",
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: "One Week to Round 21 in Las Vegas: Five F1 drivers packed inside 33 points behind Champion Antonelli.",
    liveNow: "Drivers P2 Race: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli Champion 390; Mercedes 652). Round 21: Las Vegas (19-21 Nov).",
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: "ROUND 21 VEGAS COUNTDOWN: VERSTAPPEN TO NORRIS SEPARATED BY 33 PTS BEHIND ANTONELLI",
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
