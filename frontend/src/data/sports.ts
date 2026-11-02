export const SITE_TODAY = '2026-11-02';

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
    tagline: 'NFL Week 8 MNF: Steelers overpower Giants 26-18 behind Calvin Austin\'s two touchdowns and ferocious pass rush.',
    liveNow: 'Final in Pittsburgh: Steelers 26, Giants 18. Austin 2 TD (73-yd punt ret, 29-yd rec); Wilson 278 yds; Watt 2 sacks. Steelers improve to 6-2.',
    accent: 'coral',
    hue: '14 86% 60%',
    pulse: 'NFL WEEK 8 MNF: PITTSBURGH STEELERS TOP GIANTS 26-18 TO LEAD AFC NORTH AT 6-2',
    board: 'Open the field',
    span: 'hero',
  },
  {
    slug: 'basketball',
    label: 'Basketball',
    short: 'Hoops',
    href: '/sport/basketball',
    tagline: 'NBA Thriller: Donovan Mitchell sinks baseline jumper with 0.3 seconds left as Cavaliers edge Bucks 114-113.',
    liveNow: 'Final in Milwaukee: Cavaliers 114, Bucks 113. Mitchell 30 pts (game-winner 0.3s) answers Lillard\'s 41 pts (10 threes). Cleveland moves to 7-0.',
    accent: 'coral',
    hue: '24 90% 48%',
    pulse: 'NBA THRILLER: DONOVAN MITCHELL HITS GAME-WINNER AS CAVALIERS STAY UNBEATEN (7-0)',
    board: 'Open the floor',
    span: 'side',
  },
  {
    slug: 'soccer',
    label: 'Soccer',
    short: 'Soccer',
    href: '/sport/soccer',
    tagline: 'Premier League MW9: Harry Wilson scores sensational stoppage-time brace as Fulham stun Brentford 2-1.',
    liveNow: 'Final at Craven Cottage: Fulham 2-1 Brentford (Wilson 90+2\', 90+7\'; Janelt 24\'). Fulham climb to 8 points after dramatic derby comeback.',
    accent: 'pitch',
    hue: '158 42% 22%',
    pulse: 'PREMIER LEAGUE MW9: HARRY WILSON 97TH-MINUTE HEADER CAPS MIRACLE FULHAM COMEBACK',
    board: 'Open the pitch',
    span: 'half',
  },
  {
    slug: 'tennis',
    label: 'Tennis',
    short: 'Tennis',
    href: '/sport/tennis',
    tagline: 'Rolex Paris Masters: Stefanos Tsitsipas rallies past Roberto Carballes Baena 4-6, 6-3, 6-3 in Bercy opener.',
    liveNow: 'Paris Masters R64: Tsitsipas def. Carballes Baena 4-6, 6-3, 6-3 in 2h07m. Tsitsipas fires 37 winners and 11 aces to keep ATP Finals bid alive.',
    accent: 'sky',
    hue: '198 88% 45%',
    pulse: 'ROLEX PARIS MASTERS: STEFANOS TSITSIPAS BATTLES BACK TO WIN THREE-SET BERCY OPENER',
    board: 'Open the court',
    span: 'half',
  },
  {
    slug: 'f1',
    label: 'Formula 1',
    short: 'F1',
    href: '/sport/f1',
    tagline: 'São Paulo GP Preview: Fresh off Antonelli\'s coronation, F1 heads to Interlagos for high-stakes Constructors\' showdown.',
    liveNow: 'Next up: Grande Prêmio de São Paulo (6-8 Nov). Mercedes (607 pts) lead Ferrari (474 pts) by 133 points heading into Interlagos Sprint weekend.',
    accent: 'sky',
    hue: '210 90% 48%',
    pulse: 'F1 INTERLAGOS PREVIEW: MERCEDES AND FERRARI CLASH IN SAO PAULO SPRINT SHOWDOWN',
    board: 'Open the grid',
    span: 'half',
  },
  {
    slug: 'golf',
    label: 'Golf',
    short: 'Golf',
    href: '/sport/golf',
    tagline: 'WWT Championship Preview: Following Pereda\'s historic triumph, PGA Tour arrives in Cabo with FedExCup cards on the line.',
    liveNow: 'Next up at El Cardonal at Diamante (5-8 Nov). Raul Pereda vaults into world top 50; Smotherman and Rai chase redemption in Los Cabos.',
    accent: 'lime',
    hue: '84 55% 38%',
    pulse: 'PGA TOUR CABO PREVIEW: PLAYERS CHASE TOP 125 STATUS AT TIGER WOODS-DESIGNED DIAMANTE',
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
