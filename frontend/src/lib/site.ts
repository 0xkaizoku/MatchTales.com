import seed from '../data/seed.json';
import { SITE_TODAY, sportOf, isWorldCup, initials, SPORTS, sportBySlug } from '../data/sports';
export { SITE_TODAY, sportOf, isWorldCup, initials, SPORTS, sportBySlug };

export const SITE = {
  name: 'MatchTales',
  title: 'MatchTales | Why This Match Matters',
  description:
    'MatchTales is the story layer on top of the score. Rivalries and human-written reports across tennis, football, Formula 1, soccer, golf and basketball.',
  url: 'https://www.matchtales.com',
  // Social crawlers prefer raster OG images over SVG
  ogImage:
    'https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=1200&h=630&q=80',
  twitter: '@matchtales',
  locale: 'en_US',
  keywords:
    'why this match matters, US Open tennis, NFL kickoff, Formula 1, Premier League, The Open, WNBA, World Cup 2026 archive, MatchTales',
};

export const BACKEND_URL =
  (import.meta.env.PUBLIC_BACKEND_URL as string) || 'https://www.matchtales.com';

export const data = seed as any;

export function slugify(s: string) {
  return s
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/(^-|-$)/g, '');
}

export function teamBySlug(slug: string) {
  return data.teams.find((t: any) => t.slug === slug);
}

export function teamByName(name: string) {
  return data.teams.find((t: any) => t.name === name);
}

/** Prefer canonical team.slug from seed; never invent broken links. */
export function teamSlugByName(name: string) {
  return teamByName(name)?.slug || slugify(name);
}

export function fixturesByGroup(group: string) {
  return data.fixtures.filter((f: any) => f.group === group);
}

// Why-Care score -> semantic color token + label
export function scoreMeta(score: number) {
  if (score >= 8) return { color: 'coral', label: 'Must-watch', cls: 'bg-coral' };
  if (score >= 6) return { color: 'pitch2', label: 'Big one', cls: 'bg-pitch2' };
  if (score >= 3) return { color: 'sky', label: 'Worth it', cls: 'bg-sky' };
  return { color: 'muted', label: 'Low stakes', cls: 'bg-muted' };
}

export function fmtDate(d: string) {
  try {
    return new Date(d + 'T00:00:00').toLocaleDateString('en-US', {
      weekday: 'short',
      month: 'short',
      day: 'numeric',
    });
  } catch {
    return d;
  }
}

export function statusLabel(status: string) {
  if (status === 'LIVE') return 'LIVE';
  if (status === 'FINISHED') return 'Full time';
  return 'Upcoming';
}

/** Stage label for group letter or knockout code. */
export function stageLabel(group: string, roundLabel?: string) {
  if (roundLabel) return roundLabel;
  const g = (group || '').toUpperCase();
  if (g === 'R32') return 'Round of 32';
  if (g === 'R16') return 'Round of 16';
  if (g === 'QF') return 'Quarter-final';
  if (g === 'SF') return 'Semi-final';
  if (g === '3RD' || g === 'THIRD') return 'Third place';
  if (g === 'FINAL') return 'Final';
  if (g === 'PL') return 'Premier League';
  if (g === 'NFL') return 'NFL';
  if (g === 'NBA') return 'NBA';
  if (g === 'WNBA') return 'WNBA';
  if (g === 'ATP' || g === 'WTA' || g === 'GS') return 'Grand Slam';
  if (g === 'PGA' || g === 'OPEN') return 'Golf';
  if (g === 'F1') return 'Formula 1';
  if (g.length === 1) return `Group ${g}`;
  return group;
}

/** Score display with optional pens note. */
export function scoreDisplay(m: {
  homeScore?: number | string | null;
  awayScore?: number | string | null;
  decidedBy?: string | null;
  homePen?: number | string | null;
  awayPen?: number | string | null;
}) {
  if (m.homeScore === null || m.homeScore === undefined) return null;
  const base = `${m.homeScore}–${m.awayScore}`;
  if (m.decidedBy === 'pens' && m.homePen != null && m.awayPen != null) {
    return { main: base, note: `${m.homePen}–${m.awayPen} pens` };
  }
  if (m.decidedBy === 'aet') return { main: base, note: 'AET' };
  return { main: base, note: null as string | null };
}

export function matchHref(slug: string) {
  return `/match/${slug}`;
}

/** Clamp meta description length for SERP display (~150-160). */
export function seoDescription(text: string, max = 158) {
  const t = (text || '').replace(/\s+/g, ' ').trim();
  if (t.length <= max) return t;
  return t.slice(0, max - 1).replace(/\s+\S*$/, '') + '…';
}

/**
 * Resize Unsplash (and similar) URLs for bandwidth.
 * Keeps non-Unsplash URLs untouched.
 */
export function optimizeImage(url: string | null | undefined, width = 800, quality = 75) {
  if (!url) return '';
  if (!url.includes('images.unsplash.com')) return url;
  try {
    const u = new URL(url);
    u.searchParams.set('auto', 'format');
    u.searchParams.set('fit', 'crop');
    u.searchParams.set('w', String(width));
    u.searchParams.set('q', String(quality));
    // Drop overly large legacy params noise
    u.searchParams.delete('crop');
    u.searchParams.delete('cs');
    u.searchParams.delete('fm');
    return u.toString();
  } catch {
    return url;
  }
}

/** Absolute URL helper for canonical / schema. */
export function absoluteUrl(path: string) {
  if (!path) return SITE.url;
  if (path.startsWith('http')) return path;
  return new URL(path.startsWith('/') ? path : `/${path}`, SITE.url).href;
}

/** Top group-stage table for leaderboard pages. */
export function groupStageLeaders(limit = 24) {
  const rows: any[] = [];
  for (const g of Object.keys(data.groups)) {
    data.groups[g].forEach((r: any, i: number) => {
      rows.push({ ...r, group: g, groupPos: i + 1 });
    });
  }
  rows.sort((a, b) => b.Pts - a.Pts || b.GD - a.GD || b.GF - a.GF);
  return rows.slice(0, limit);
}

const flagCodeMap: Record<string, string> = {
  MEX: 'mx',
  KOR: 'kr',
  RSA: 'za',
  CZE: 'cz',
  CAN: 'ca',
  SUI: 'ch',
  QAT: 'qa',
  BIH: 'ba',
  BRA: 'br',
  MAR: 'ma',
  HAI: 'ht',
  SCO: 'gb-sct',
  USA: 'us',
  PAR: 'py',
  AUS: 'au',
  TUR: 'tr',
  GER: 'de',
  CUW: 'cw',
  CIV: 'ci',
  ECU: 'ec',
  NED: 'nl',
  JPN: 'jp',
  TUN: 'tn',
  SWE: 'se',
  BEL: 'be',
  EGY: 'eg',
  IRN: 'ir',
  NZL: 'nz',
  ESP: 'es',
  CPV: 'cv',
  KSA: 'sa',
  URU: 'uy',
  FRA: 'fr',
  SEN: 'sn',
  NOR: 'no',
  IRQ: 'iq',
  ARG: 'ar',
  ALG: 'dz',
  AUT: 'at',
  JOR: 'jo',
  POR: 'pt',
  UZB: 'uz',
  COL: 'co',
  COD: 'cd',
  ENG: 'gb-eng',
  CRO: 'hr',
  GHA: 'gh',
  PAN: 'pa',
};

/** FlagCDN URL. Use w20 for lists, w40 for cards, w80 for headers. */
export function getFlagUrl(code: string, size: 20 | 40 | 80 = 40) {
  const c = flagCodeMap[(code || '').toUpperCase()] || 'un';
  return `https://flagcdn.com/w${size}/${c}.png`;
}
