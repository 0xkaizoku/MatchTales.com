export const SITE_TODAY = '2026-10-02';

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
    tagline: 'Champions League: Aston Villa stun Bayern Munich 1-0 with Jhon Duran wonder strike; Lille shock Real Madrid.',
    liveNow: 'Duran 79th-minute lob over Neuer repeats 1982 European Cup triumph at Villa Park. Premier League MW7 kicks off Saturday.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'ASTON VILLA 1-0 BAYERN',
    board: 'Open the pitch',
    span: 'hero',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'Thursday Night Football: 49ers hold off Rams 24-20 as goal-line stand seals NFC West thriller.',
    liveNow: 'FINAL: 49ers 24, Rams 20. Brock Purdy two TDs; McCaffrey 4th-quarter score withstands Stafford rally.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: '49ERS 24-20 RAMS FINAL',
    board: 'Open the field',
    span: 'side',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA Semifinals locked: Lynx-Fever and Aces-Liberty set for Sunday Game 1 tip-off.',
    liveNow: 'Historic first round sweeps complete. Caitlin Clark takes on Napheesa Collier while Stewart battles A\'ja Wilson.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA FINAL FOUR LOCKED',
    board: 'Open the floor',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Sanderson Farms: Beau Hossler shoots 64 to take 36-hole lead at 15-under in Jackson.',
    liveNow: 'Hossler sits one clear of Daniel Berger (-14). Defending champion Kevin Yu fires 66 to stay in the hunt at -10.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'HOSSLER -15 ROUND 2',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'China Open 2026: Alcaraz powers past Khachanov 7-5, 6-2; Sinner battles into Beijing semifinals.',
    liveNow: 'World No. 1 Sinner defeats Lehecka 6-2, 7-6(6). Aryna Sabalenka and Coco Gauff roll into WTA quarterfinals.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'ALCARAZ & SINNER IN SEMIS',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Singapore GP: Lando Norris edges Charles Leclerc by 0.058s in Friday night practice at Marina Bay.',
    liveNow: 'FP2 under 1,600 floodlights: Norris 1:30.727, Leclerc 1:30.785. Championship leader Antonelli within three tenths.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'NORRIS TOPS FP2 IN SINGAPORE',
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
    .filter(Boolean)
    .slice(0, 2)
    .map((w) => w[0]?.toUpperCase() || '')
    .join('');
}
