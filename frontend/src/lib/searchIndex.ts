import { getCollection } from 'astro:content';
import { data, sportOf, isWorldCup } from './site';
import { dict, localePath, categoryLabel, sportCopy, fill, entityName } from '../i18n';
import { localizeMatch, stageLabelI18n } from '../i18n/content';
import type { Locale } from '../i18n';

export async function buildSearchIndex(locale: Locale) {
  const d = dict(locale);
  const matches = await getCollection('matches');
  const stories = await getCollection('stories');
  const index: any[] = [];
  const lp = (p: string) => localePath(locale, p);

  for (const t of data.teams) {
    index.push({
      t: entityName(t.name, locale),
      s: `${t.nick} ${t.group}`,
      k: fill(d.search.teamKind, { g: t.group }),
      e: '⚽',
      u: lp(`/team/${t.slug}`),
    });
  }
  for (const m of matches) {
    const locm = localizeMatch(m.data, locale);
    const sport = sportOf(m.data);
    const stage = stageLabelI18n(locale, m.data.group, m.data.roundLabel);
    const score =
      m.data.status === 'FINISHED' && m.data.homeScore != null ? ` ${m.data.homeScore}-${m.data.awayScore}` : '';
    index.push({
      t: `${locm.home} ${d.common.vs} ${locm.away}${score}`,
      s: `${locm.headline} ${(m.data.tags || []).join(' ')}`,
      k: `${sportCopy(locale, sport).label} · ${stage}`,
      e: '🏟️',
      u: lp(`/match/${m.data.slug}`),
    });
  }
  for (const s of stories) {
    index.push({
      t: s.data.title,
      s: s.data.excerpt,
      k: fill(d.search.storyKind, { k: categoryLabel(locale, s.data.sport || s.data.category) }),
      e: '📰',
      u: lp(`/stories/${s.id}`),
    });
  }
  index.push({ t: d.search.directory, s: d.search.directoryS, k: d.search.pageKind, e: '🗂️', u: lp('/sports') });
  for (const slug of ['tennis', 'football', 'f1', 'soccer', 'golf', 'basketball'] as const) {
    const c = sportCopy(locale, slug);
    index.push({ t: c.label, s: c.keywords, k: d.search.sportKind, e: '•', u: lp(`/sport/${slug}`) });
  }
  index.push({ t: d.search.wc, s: d.search.wcS, k: d.search.pageKind, e: '🏆', u: lp('/world-cup') });

  return index;
}
