export const SITE_TODAY = '2026-11-14';

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
    tagline: "TNF Final: Diggs 32-yard TD with 0:57 left lifts Commanders 24-21 over Giants. No Saturday NFL game.",
    liveNow: "FINAL Thu: Commanders 24, Giants 21 (Daniels 3 TD, Diggs winner, Douglas INT). WSH 3-5-1, NYG 5-3-1. Sunday Munich: Patriots vs Lions, 9:30 a.m. ET FOX.",
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: "NFL TNF FINAL: COMMANDERS 24-21 GIANTS ON DIGGS TD AT 0:57; SATURDAY DARK, SUNDAY MUNICH",
    board: 'Open the field',
    span: 'hero',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: "Kane penalty wins England 2-1 on cap 126; Arsenal hold Barcelona 1-1 at Camp Nou. Sunday: Spain vs England.",
    liveNow: "Thu Finals: England 2-1 Croatia (Rogers 24, Kane 64 pen); Italy 3-1 France; Czechia 0-2 Spain; Barcelona 1-1 Arsenal. Sunday 19:45 GMT: Spain vs England, Madrid.",
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: "ENGLAND 2-1 CROATIA AND BARCELONA 1-1 ARSENAL; SUNDAY SPAIN VS ENGLAND IN MADRID",
    board: 'Open the pitch',
    span: 'side',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: "Spurs 123-85 Warriors for an 11th straight win; Castle 32. Thursday: Cunningham 52 in 2OT.",
    liveNow: "Fri: Spurs 123, Warriors 85 (Castle 32, Wemby 12/12/6). Thu: Pistons 144-140 2OT Wizards (Cunningham 52). Tonight: 5 NBA games upcoming.",
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: "NBA: SPURS 11TH STRAIGHT 123-85, CASTLE 32; CUNNINGHAM 52 IN DOUBLE OT THURSDAY",
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: "Dubai R2 complete: McIlroy and Hatton share 139 (-5). Round 3 Saturday unpublished as final.",
    liveNow: "R2 AP: T1 McIlroy 69-70=139, Hatton 70-69=139; T3 Luiten 140, Reitan 140; Chacarra 143 (T11). R3 in progress, not posted as final.",
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: "DUBAI R2: MCILROY AND HATTON SHARE 139; LUITEN 140; R3 NOT PUBLISHED AS FINAL",
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: "Stockholm Final Today: Fritz vs Tirante after a 6-4, 6-2 SF. Turin opens Sunday with Zverev vs Jodar.",
    liveNow: "Today Final: Fritz vs Tirante (upcoming). Fri SF: Fritz d Musetti 6-4, 6-2; Tirante d Tabilo 7-5, 7-6 (1). QF: Fritz walkover Rune. Turin Sunday.",
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: "STOCKHOLM FINAL TODAY FRITZ VS TIRANTE; TURIN OPENS SUNDAY ZVEREV VS JODAR",
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: "Five days to Round 21 Las Vegas: 33 points still split Verstappen to Norris. No Strip race yet.",
    liveNow: "Drivers P2 race unchanged: Verstappen 279, Russell 262, Hamilton 261, Leclerc 249, Norris 246 (Antonelli 390; Mercedes 652). Round 21: 19-21 Nov.",
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: "FIVE DAYS TO VEGAS: VERSTAPPEN TO NORRIS STILL 33 PTS BEHIND CHAMPION ANTONELLI",
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
