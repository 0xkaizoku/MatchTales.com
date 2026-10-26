export const SITE_TODAY = '2026-10-26';

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
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'World Champion Antonelli: Italian teenager wins United States GP from pole to seal 2026 title.',
    liveNow: 'Austin GP Final: Antonelli wins ahead of Leclerc and Verstappen. Russell P8 clinches title for Antonelli with 123-point lead.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'WORLD CHAMPION: ANTONELLI SEALS 2026 TITLE AT COTA',
    board: 'Open the grid',
    span: 'hero',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'WNBA Finals Game 5 tonight: Valkyries and Dream clash at Chase Center in winner-take-all decider.',
    liveNow: 'Tonight 20:00 ET / 17:00 PT: Game 5 in San Francisco. Series tied 2-2 after Valkyries 67-62 road stunner in Game 4.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'WNBA FINALS DECIDER: GAME 5 TONIGHT IN SAN FRANCISCO',
    board: 'Open the floor',
    span: 'side',
  },
  {
    slug: 'football',
    label: 'Football',
    short: 'NFL',
    href: '/sport/football',
    tagline: 'NFL Week 7 Sunday shocks: Seahawks topple Chiefs 20-3, Falcons beat 49ers 29-20; Vikings stand alone at 6-0.',
    liveNow: 'Sunday finals: Seahawks 20, Chiefs 3; Falcons 29, 49ers 20; Vikings 16, Colts 10. Tonight: Cowboys (2-4) at Eagles (2-4) on MNF.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'UPSET SUNDAY: VIKINGS LONE UNBEATEN AS CHIEFS AND 49ERS FALL',
    board: 'Open the field',
    span: 'half',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Premier League MW8 wrap: Bournemouth stun Man United 3-0 at Old Trafford; Liverpool top Brighton 2-0.',
    liveNow: 'MW8 Sunday: Bournemouth 3, Man United 0; Liverpool 2, Brighton 0; Newcastle 2, Palace 0. Man City and Arsenal top table on 21 pts.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'PREMIER LEAGUE: BOURNEMOUTH ROUT MAN UNITED AT OLD TRAFFORD',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'Bermuda playoff thriller: Austin Smotherman outlasts Seamus Power on third extra hole for second victory in a month.',
    liveNow: 'Bermuda Final: Smotherman pars 16th on 3rd playoff hole to defeat Power after 54-hole tie at 16 under. Conners T3 at -14.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'PORT ROYAL PLAYOFF: SMOTHERMAN CLAIMS BERMUDA TITLE',
    board: 'Open the course',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'ATP 500 swing opens in Vienna and Basel: Alcaraz meets Khachanov while Almaty champion Medvedev enters draw.',
    liveNow: 'Monday Round 1: Erste Bank Open in Vienna and Swiss Indoors in Basel underway. Alcaraz, Zverev and Medvedev headline.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'INDOOR SWING: VIENNA AND BASEL LAUNCH ATP 500 WEEK',
    board: 'Open the court',
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
