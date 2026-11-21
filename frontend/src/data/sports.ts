export const SITE_TODAY = '2026-11-21';

export const SPORT_SLUGS = ['tennis', 'f1', 'soccer', 'golf', 'football', 'basketball'] as const;
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
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: "Turin Semifinals Saturday: Alcaraz battles Shelton in afternoon clash before Zverev meets Medvedev tonight.",
    liveNow: "Sat Semifinals: Alcaraz vs Shelton (14:00 CET), Zverev vs Medvedev (20:30 CET). Groups Complete: Alcaraz 3-0, Zverev 3-0, Shelton 2-1, Medvedev 2-1.",
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: "NITTO ATP FINALS: BLOCKBUSTER TURIN SEMIFINALS TODAY AS ALCARAZ MEETS SHELTON AND ZVEREV PLAYS MEDVEDEV",
    board: 'Open the court',
    span: 'hero',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: "Las Vegas GP Race Night: Verstappen starts on pole alongside Russell as the 50-lap desert showdown begins.",
    liveNow: "Tonight 22:00 local (01:00 ET Sun): Las Vegas GP Main Race. Grid: Verstappen P1, Russell P2, Leclerc P3, Norris P4, Antonelli P6 (penalty).",
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: "LAS VEGAS GP: 50-LAP MAIN RACE TONIGHT ON THE STRIP AS VERSTAPPEN LEADS THE FIELD FROM POLE POSITION",
    board: 'Open the grid',
    span: 'side',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: "Premier League returns: Fulham lead Man City 1-0 in early thriller; Newcastle host leaders Arsenal at 17:30 GMT.",
    liveNow: "Live: Man City 0-1 Fulham (Muniz 16). Today: Newcastle vs Arsenal (17:30 GMT), Chelsea vs Leeds (15:00 GMT). Table: Arsenal 27, Brighton 22, City 21.",
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: "PREMIER LEAGUE: TITLE RACE RESUMES AS MAN CITY TRAIL FULHAM AND ARSENAL VISIT ST JAMES PARK TONIGHT",
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: "The RSM Classic Moving Day: Thorbjornsen, Penge, and Neergaard-Petersen share lead at -9 as 36-hole cut falls at -2.",
    liveNow: "Round 3 underway at Sea Island (Seaside Course). Leaders at -9: Thorbjornsen, Penge, Neergaard-Petersen. Top-125 bubble: Dahmen (-3), Thompson (-5).",
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: "PGA TOUR FALL FINALE: ROUND 3 MOVING DAY LIVE AT SEA ISLAND AS TOP-125 CARDS REACH THE CLIMAX",
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: "Texans dismantle Colts 26-3 on Thursday Night Football; Week 11 Sunday showdowns take center stage.",
    liveNow: "TNF Final: Texans 26, Colts 3 (Stroud 2 TDs, defense forces 3 turnovers). Next: Chiefs at Panthers, 49ers at Packers on Sunday.",
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: "NFL WEEK 11: TEXANS ROUT COLTS 26-3 TO SEIZE AFC SOUTH DRIVER SEAT AHEAD OF SUNDAY ACTION",
    board: 'Open the field',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: "Lakers edge Kings 106-104 on Friday stop; Jokic drops 32-point triple-double to lead Nuggets past Rockets.",
    liveNow: "Fri: Lakers 106-104 Kings; Nuggets 133-124 Rockets (Jokic 32/12/10); Cavs 128-119 Pacers; Magic 113-111 Nets. Thu: Spurs 118-106 Warriors (13 straight).",
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: "NBA FRIDAY: LAKERS SURVIVE KINGS 106-104 ON FINAL BUZZER; JOKIC POSTS 32-POINT TRIPLE-DOUBLE",
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
