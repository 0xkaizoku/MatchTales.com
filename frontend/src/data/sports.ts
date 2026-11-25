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
    tagline: "Thanksgiving Football: 8-2 Bears at 8-2 Lions open Thursday tripleheader after Wed Packers-Rams on Netflix.",
    liveNow: "Thu Nov 26: Bears (8-2) at Lions (8-2) 1 PM ET CBS, Eagles (3-7) at Cowboys (5-6) 4:30 PM FOX, Chiefs (8-2) at Bills (9-1) 8:20 PM NBC. Wed Netflix Packers-Rams unpublished. Week 11: Texans 26-3 Colts (HOU 4-6).",
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: "NFL WEEK 12 THANKSGIVING: IDENTICAL 8-2 LIONS AND BEARS CLASH FOR NFC NORTH LEAD; CHIEFS VISIT 9-1 BILLS",
    board: 'Open the field',
    span: 'hero',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: "Champions League MD5: Real Madrid storm past PSV 5-1 to sit alone on 15 points; Wednesday slate unpublished.",
    liveNow: "UCL Tue: Real Madrid 5-1 PSV (Mbappe 64, 84), Arsenal 1-1 Dortmund (Gyokeres 10; Beier 55), Man City 2-2 Napoli. PL: Arsenal 28, Brighton 22, City 22, Liverpool 21. City 1-1 Fulham (Anderson 57; Muniz 16).",
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: "CHAMPIONS LEAGUE MD5: REAL MADRID HIT 15 POINTS AT SUMMIT AFTER 5-1 PSV; ARSENAL LEAD PL ON 28",
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
    tagline: "Davis Cup Final 8 in Bologna: Czechia through 2-0; Italy vs Korea still open; Alcaraz crowned in Turin.",
    liveNow: "Davis Cup Bologna: Czechia d Canada 2-0; Italy vs Korea open after Musetti d Hong 6-0, 7-6(5). Thu QFs: GB vs Germany 10:00 CET, Austria vs Spain 17:00 CET. Turin Final: Alcaraz d Zverev 6-2, 7-6(7).",
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: "DAVIS CUP FINALS: CZECHIA INTO THE LAST FOUR; GREAT BRITAIN VS GERMANY OPENS THURSDAY IN BOLOGNA",
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
    tagline: "Emirates NBA Cup before Thanksgiving rest: Mavericks beat Nuggets 120-101; Celtics drop 131 on Wizards.",
    liveNow: "Tue Cup: Mavericks 120-101 Nuggets (Flagg 24/6/12); Celtics 131-116 Wizards (Tatum 41, George 28; Davis 33/13); Pistons 104-86 Magic (Joe 21). Wed unpublished. Thu rest.",
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: "EMIRATES NBA CUP: MAVS CRUISE BEHIND COOPER FLAGG AND TATUM SCORES 41 AS THE LEAGUE TAKES THANKSGIVING OFF",
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
