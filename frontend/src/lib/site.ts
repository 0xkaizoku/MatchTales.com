import seed from '../data/seed.json';

export const SITE = {
  name: 'MatchTales',
  title: 'MatchTales — Why This Match Matters | World Cup 2026',
  description:
    'MatchTales is the story layer on top of the 2026 FIFA World Cup. Why-Care scores, rivalries, player legacies, iconic moments and human-written stories for every match.',
  url: 'https://www.matchtales.com',
  ogImage: '/og-default.svg',
  twitter: '@matchtales',
};

export const BACKEND_URL =
  (import.meta.env.PUBLIC_BACKEND_URL as string) || 'https://www.matchtales.com';

export const data = seed as any;

export function slugify(s: string) {
  return s.toLowerCase().replace(/\s+/g, '-');
}

export function teamBySlug(slug: string) {
  return data.teams.find((t: any) => t.slug === slug);
}

export function teamByName(name: string) {
  return data.teams.find((t: any) => t.name === name);
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

// Build a quick lookup of generated match story slugs -> for matching fixtures
export function matchHref(slug: string) {
  return `/match/${slug}`;
}
