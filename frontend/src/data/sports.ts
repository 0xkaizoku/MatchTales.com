export const SITE_TODAY = '2026-10-18';

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
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Shanghai Masters Final: Zverev faces Medvedev for the Masters 1000 crown at Qizhong.',
    liveNow: 'Saturday Semifinals: Zverev d. Davidovich Fokina 6-4, 6-3. Medvedev d. Jodar 7-6(4), 6-3. Sunday Final: Alexander Zverev vs Daniil Medvedev on Stadium Court.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'SHANGHAI MASTERS FINAL: ZVEREV VS MEDVEDEV',
    board: 'Open the court',
    span: 'hero',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'NFL Week 6 Sunday: Chiefs hold off Chargers 27-20 to stay unbeaten; Bills roll past Raiders.',
    liveNow: 'Sunday: Chiefs 27, Chargers 20. Bills 31, Raiders 13. TNF (OT): Broncos 17, Seahawks 14. Chiefs 5-0, Bills 5-1, Broncos 4-2. Vikings and 49ers stand 5-0.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'WEEK 6 SUNDAY: CHIEFS 27, CHARGERS 20',
    board: 'Open the field',
    span: 'side',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA Finals Game 1 Final: Valkyries defeat Dream 82-76 at Chase Center to lead series 1-0.',
    liveNow: 'FINAL: Valkyries 82, Dream 76. Golden State takes 1-0 series lead. Game 2 is Monday 19 October, 8:00 p.m. ET at Chase Center on ESPN.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'VALKYRIES TAKE GAME 1 OVER DREAM 82-76',
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Premier League MW7: Arsenal blank Forest 2-0 to chase City (21 pts) after 3-1 win over Ipswich.',
    liveNow: 'Sunday: Forest 0-2 Arsenal, Brighton 2-1 Palace. Saturday: City 3-1 Ipswich, Everton 1-1 Chelsea, Brentford 2-1 Liverpool. City 21 pts (7-0-0), Arsenal 18 (6-0-1), Brighton 16.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'MW7 SUNDAY: ARSENAL ANSWER CITY WITH FOREST WIN',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'United States GP: Race week arrives in Austin. Antonelli leads Russell by 102 points.',
    liveNow: 'Race week in Austin: COTA sprint weekend 23-25 October, race Sunday 25 October at 15:00 local. Antonelli 340, Russell 238. Mercedes lead constructors with 578 points.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'RACE WEEK AT COTA: AUSTIN SPRINT FIVE DAYS AWAY',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'PGA Tour Bermuda countdown: Port Royal prepares as fall series resumes in four days.',
    liveNow: 'Fall hiatus ends. Butterfield Bermuda Championship begins 22-25 October at Port Royal, Southampton, $6M purse. Brennan won Baycurrent at 16 under.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'BERMUDA COUNTDOWN: PORT ROYAL TEES OFF THURSDAY',
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
