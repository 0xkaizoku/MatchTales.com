export const SITE_TODAY = '2026-10-30';

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
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA Finals Game 6: Valkyries defeat Dream 76-71 to win historic maiden championship in inaugural season.',
    liveNow: 'Valkyries crowned 2026 WNBA Champions! Golden State clinches series 4-2 behind Paige Bueckers 24 pts and 8 ast in Atlanta.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA FINALS GAME 6: GOLDEN STATE VALKYRIES WIN HISTORIC EXPANSION CHAMPIONSHIP',
    board: 'Open the floor',
    span: 'hero',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'NFL Week 8 TNF: Packers beat Panthers 27-17 behind Jordan Love 2 TD passes to improve to 6-2 at Lambeau Field.',
    liveNow: 'Final at Lambeau: Packers 27, Panthers 17. Jordan Love 21/30, 248 yds, 2 TD; Josh Jacobs 94 yds, 1 TD; Rashan Gary 2 sacks.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'THURSDAY NIGHT FOOTBALL: PACKERS SURGE PAST PANTHERS 27-17 AT LAMBEAU',
    board: 'Open the field',
    span: 'side',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Carabao Cup quarter-final draw: Fourth-tier Fleetwood Town draw Newcastle United; Arsenal host Liverpool on Saturday.',
    liveNow: 'Carabao Cup draw: Fleetwood Town host Newcastle, Man City visit Tottenham, Liverpool face Brentford. Premier League MW9 kicks off Saturday.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'CARABAO CUP DRAW: FLEETWOOD TOWN GET NEWCASTLE; ARSENAL HOST LIVERPOOL SATURDAY',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Vienna quarter-finals: Carlos Alcaraz sweeps Jack Draper 6-4, 6-4 to set up blockbuster semi-final clash with Alexander Zverev.',
    liveNow: 'Erste Bank Open QF: Alcaraz def. Draper 6-4, 6-4 (29 winners). Zverev def. Rublev 7-6(4), 6-4. Alcaraz vs Zverev on Saturday.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'ERSTE BANK OPEN: ALCARAZ SWEEPS DRAPER TO SET UP VIENNA SEMI-FINAL WITH ZVEREV',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Mexico City GP FP2: Kimi Antonelli sets blistering 1:17.342 benchmark at altitude to top Friday practice over Leclerc and Verstappen.',
    liveNow: 'FP2 in Mexico City: Antonelli leads Ferrari Leclerc by 0.188s and Red Bull Verstappen by 0.245s. Antonelli needs P9 on Sunday for crown.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'MEXICO CITY GP FP2: KIMI ANTONELLI PACES FRIDAY PRACTICE AT ALTITUDE',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'VidantaWorld Mexico Open round 2: Austin Smotherman fires 65 to seize 36-hole lead at 11-under 131; Pereda and Rai chase at 9-under.',
    liveNow: 'Round 2 at VidantaVallarta: Smotherman (-11, 131) leads Raul Pereda (-9) and Aaron Rai (-9). Cut falls at 1-under 141 with 68 making weekend.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'PGA TOUR MEXICO OPEN: SMOTHERMAN FIRES 65 TO TAKE 36-HOLE LEAD AT 11-UNDER',
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
