export const SITE_TODAY = '2026-10-28';

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
    tagline: 'Carabao Cup shock: League Two Fleetwood Town stun Arsenal 5-3 on penalties after 1-1 draw.',
    liveNow: 'Fourth Round drama: Fleetwood Town eliminate Arsenal 5-3 on penalties. Wednesday ties: Man City vs Brighton, Liverpool vs Chelsea.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'LEAGUE CUP SHOCK: FLEETWOOD TOWN STUN ARSENAL IN SHOOTOUT',
    board: 'Open the pitch',
    span: 'hero',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'Valkyries grab 3-2 Finals lead as NBA season explodes with Wembanyama 29-point show.',
    liveNow: 'WNBA Finals Game 5: Valkyries 64, Dream 55. NBA Opening: Spurs 130, Kings 103 (Wemby 9 dunks); Celtics 125, Nets 124 (Tatum 40 pts).',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'HOOPS EXPLOSION: VALKYRIES SEIZE 3-2 LEAD AS NBA TIPOFS',
    board: 'Open the floor',
    span: 'side',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'Cowboys crush Eagles 38-21 on MNF: Prescott throws 3 TDs; Packers host Panthers on Thursday night.',
    liveNow: 'MNF Final: Cowboys 38, Eagles 21 behind Prescott masterclass. Vikings (6-0) stand as lone unbeaten. TNF: Panthers at Packers.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'MNF STATEMENT: COWBOYS ROUT EAGLES 38-21 IN PHILADELPHIA',
    board: 'Open the field',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Vienna drama: Alcaraz downs Khachanov in straight sets while Zverev survives 13-11 tiebreak marathon.',
    liveNow: 'Vienna R1: Alcaraz def. Khachanov 6-4, 7-6 (5). Zverev outlasts Landaluce 7-5, 3-6, 7-6 (13-11) saving match points.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'ERSTE BANK OPEN: ALCARAZ AND ZVEREV SURVIVE VIENNA OPENERS',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'Mexico City GP countdown: Antonelli needs ninth place at Hermanos Rodriguez to seal maiden title.',
    liveNow: 'Championship equation: Antonelli (365 pts) leads Russell by 123. P9 on Sunday guarantees title. Antonelli confirms car #12 for 2027.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'MEXICO CITY GP: ANTONELLI ON BRINK OF HISTORIC WORLD TITLE',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'VidantaWorld Mexico Open tee-off: Smotherman brings Bermuda momentum to $6M FedExCup Fall test.',
    liveNow: 'Mexico Open Preview: Field gathers at VidantaVallarta. Smotherman seeks back-to-back wins after 3rd playoff hole triumph in Bermuda.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'FEDEXCUP FALL: VIDANTAWORLD MEXICO OPEN TEEING OFF',
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
