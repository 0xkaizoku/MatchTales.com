export const SITE_TODAY = '2026-11-26';

export const SPORT_SLUGS = ['football', 'soccer', 'f1', 'tennis', 'golf', 'basketball'] as const;
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
    tagline: "Thanksgiving Football: Rams 26-13 Packers on Netflix; 8-2 Bears at 8-2 Lions still to kick at 1 PM ET.",
    liveNow: "FINAL Wed: Rams 26, Packers 13 (Corum 32-184-1; LAR 7-4, GB 6-5). Thu unpublished: Bears (8-2) at Lions (8-2) 1 PM ET CBS, Eagles (3-7) at Cowboys (5-6) 4:30 FOX, Chiefs (8-2) at Bills (9-1) 8:20 NBC.",
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: "NFL WEEK 12: RAMS 26-13 PACKERS; 8-2 BEARS AT 8-2 LIONS OPEN THANKSGIVING TRIPLEHEADER",
    board: 'Open the field',
    span: 'hero',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: "Champions League MD5: Barcelona 4-1 at Sabah and Liverpool 3-0 at Brugge; Real Madrid still first on 15.",
    liveNow: "UCL Wed: Sabah 1-4 Barcelona (Gordon 31, 51; Adeyemi 55; Jesus 60); Club Brugge 0-3 Liverpool (Isak 13, Wirtz 79). Tue: Real Madrid 5-1 PSV (Bellingham 59). Table: Madrid 15, PSG 13, Barca 12, Liverpool 12. PL: Arsenal 28, Brighton 22, City 22, Liverpool 21.",
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: "CHAMPIONS LEAGUE MD5: BARCELONA 4-1 SABAH AND LIVERPOOL 3-0 BRUGGE; MADRID STILL FIRST ON 15",
    board: 'Open the pitch',
    span: 'side',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: "Qatar GP next (27-29 Nov): Verstappen carries Las Vegas victory into a standard Lusail weekend with no sprint.",
    liveNow: "Vegas GP Final: 1. Verstappen 1:27:39.624, 2. Norris +0.639s, 3. Piastri from P17; Russell P9 +13.192s. Standings: Antonelli 402 (Champ), Verstappen 304, Hamilton 267, Russell 264, Norris 264. Qatar Fri FP1.",
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: "FORMULA 1: VERSTAPPEN WINS LAS VEGAS AS MCLAREN CUT RED BULL CONSTRUCTORS GAP TO 9 POINTS",
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: "Davis Cup Bologna: Italy 2-1 Korea and Great Britain 2-1 Germany; Austria vs Spain 17:00 CET unpublished.",
    liveNow: "QF complete: Czechia 2-0 Canada; Italy 2-1 Korea; GB 2-1 Germany (Patten/Skupski d Krawietz/Puetz 6-2, 7-6(6)). Austria vs Spain 17:00 CET unpublished. Fri: Italy vs Czechia 16:00 CET. Turin: Alcaraz d Zverev 6-2, 7-6(7).",
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: "DAVIS CUP: GREAT BRITAIN AND ITALY JOIN CZECHIA IN THE LAST FOUR; AUSTRIA-SPAIN STILL TO PLAY",
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: "Marco Penge captures maiden PGA Tour victory in a four-man Sea Island playoff at The RSM Classic.",
    liveNow: "RSM Classic Final (23 Nov): Marco Penge (-16, 266) wins 1st playoff hole over Haotong Li, Michael Thorbjornsen, and Max Greyserman. Next: Hero World Challenge (3-6 Dec).",
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: "PGA TOUR: MARCO PENGE CAPS FOUR-WAY PLAYOFF AT SEA ISLAND FOR MAIDEN WIN AND 2027 MASTERS TICKET",
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: "NBA Cup: Sixers 111-104 Heat as LeBron posts 25/10/12; league rests on Thanksgiving.",
    liveNow: "Wed Cup: 76ers 111-104 Heat (LeBron 25/10/12, Maxey 30; Giannis 32/14); Blazers 116-111 Spurs (Wemby 44/16). Tue: Mavs 120-101 Nuggets, Celtics 131-116 Wizards, Pistons 104-86 Magic. Thu rest.",
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: "NBA CUP: LEBRON FIRST SIXERS TRIPLE-DOUBLE BEATS HEAT 111-104 BEFORE THANKSGIVING REST",
    board: 'Open the floor',
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
