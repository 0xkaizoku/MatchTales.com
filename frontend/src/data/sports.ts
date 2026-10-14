export const SITE_TODAY = '2026-10-14';

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
    tagline: 'Shanghai Masters: Daniil Medvedev beats Stefanos Tsitsipas 6-4, 7-5. Quarterfinal field is set.',
    liveNow: 'Wednesday R16: Medvedev d. Tsitsipas 6-4, 7-5. Paul d. Bergs 7-6 (5), 6-4. Jodar d. van de Zandschulp in 3 sets. Ruud through. Sinner remains out.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'MEDVEDEV BEATS TSITSIPAS IN SHANGHAI',
    board: 'Open the court',
    span: 'hero',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'Week 6 kickoff: Denver Broncos visit Seattle Seahawks on Thursday Night Football at Lumen Field.',
    liveNow: 'Bills beat Rams 37-34 in OT. Vikings (5-0), 49ers (5-0), Chiefs (4-0) remain undefeated. Seahawks (4-1) host Broncos (2-3) Thursday 8:15 p.m. ET.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'BRONCOS AT SEAHAWKS ON THURSDAY',
    board: 'Open the field',
    span: 'side',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Premier League: Manchester City lead on 18 points. Matchweek 7 returns Saturday.',
    liveNow: 'Coventry beat Newcastle 4-1 on Monday. City 18 (16 for, 5 against). Arsenal 15, Brighton 13, Liverpool 9. Spurs 19th on 3 points.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'CITY LEAD TABLE INTO MATCHWEEK 7',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA Finals: Dream vs Valkyries Game 1 tipoff is Saturday at Chase Center on NBC.',
    liveNow: 'Game 1 is Saturday 17 October, 3:30 p.m. ET, NBC. Game 2 Monday 19 October, 8:00 p.m. ET. Expansion Valkyries host Atlanta after 3-0 sweep.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA FINALS: THREE DAYS TO GAME 1',
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'United States GP countdown: Antonelli leads by 102 points as Mercedes eye Constructors title in Austin.',
    liveNow: 'Austin COTA race is 25 October, 15:00 local. Antonelli 340, Russell 238, Hamilton 229, Verstappen 221. Mercedes lead constructors with 578 points.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'AUSTIN GP: MERCEDES EYE CONSTRUCTORS CROWN',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'The PGA Tour is off this week. Brennan\'s Baycurrent win stands as Bermuda qualifying begins.',
    liveNow: 'Next stop: Butterfield Bermuda Championship, 22-25 October at Port Royal, purse $6 million. Michael Brennan won Baycurrent at 16 under.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'PGA TOUR OFF: BERMUDA NEXT IN SIGHT',
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
