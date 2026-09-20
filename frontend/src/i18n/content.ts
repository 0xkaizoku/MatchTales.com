import type { Locale } from './locales';
import { fill, LOCALE_META } from './locales';
import { competitionName, entityName } from './names';
import { dict } from './index';
import { STORY_I18N } from './stories';

function scoreLine(m: {
  homeScore?: number | string | null;
  awayScore?: number | string | null;
  decidedBy?: string | null;
}, locale: Locale): string {
  if (m.homeScore == null || m.awayScore == null) return '';
  const d = dict(locale);
  const sep = locale === 'de' || locale === 'pl' ? ':' : '-';
  let s = `${m.homeScore}${sep}${m.awayScore}`;
  if (m.decidedBy === 'aet') s += ` ${d.status.aet}`;
  if (m.decidedBy === 'pens') s += ` ${d.status.pens}`;
  return s;
}

export function stageLabelI18n(locale: Locale, group: string, roundLabel?: string): string {
  const d = dict(locale);
  if (roundLabel) {
    const rl = roundLabel.toLowerCase();
    if (rl.includes('round of 32')) return d.stage.r32;
    if (rl.includes('round of 16')) return d.stage.r16;
    if (rl.includes('quarter')) return d.stage.qf;
    if (rl.includes('semi')) return d.stage.sf;
    if (rl.includes('third')) return d.stage.third;
    if (rl.includes('final') && !rl.includes('week')) return d.stage.final;
    if (rl.includes('premier')) return d.stage.pl;
    if (rl.includes('matchweek') || rl.includes('matchday')) {
      const n = roundLabel.match(/\d+/)?.[0];
      return n ? fill(d.stage.matchdayLong, { n }) : d.stage.pl;
    }
  }
  const g = (group || '').toUpperCase();
  if (g === 'R32') return d.stage.r32;
  if (g === 'R16') return d.stage.r16;
  if (g === 'QF') return d.stage.qf;
  if (g === 'SF') return d.stage.sf;
  if (g === '3RD' || g === 'THIRD') return d.stage.third;
  if (g === 'FINAL') return d.stage.final;
  if (g === 'PL') return d.stage.pl;
  if (g === 'NFL') return d.stage.nfl;
  if (g === 'NBA') return d.stage.nba;
  if (g === 'WNBA') return d.stage.wnba;
  if (g === 'ATP' || g === 'WTA' || g === 'GS') return d.stage.gs;
  if (g === 'PGA' || g === 'OPEN') return d.stage.golf;
  if (g === 'F1') return d.stage.f1;
  if (g.length === 1) return fill(d.stage.group, { g });
  return group;
}

export function statusLabelI18n(locale: Locale, status: string): string {
  const d = dict(locale);
  if (status === 'LIVE') return d.status.LIVE;
  if (status === 'FINISHED') return d.status.FINISHED;
  return d.status.UPCOMING;
}

export function scoreDisplayI18n(
  locale: Locale,
  m: {
    homeScore?: number | string | null;
    awayScore?: number | string | null;
    decidedBy?: string | null;
    homePen?: number | string | null;
    awayPen?: number | string | null;
  }
) {
  if (m.homeScore === null || m.homeScore === undefined) return null;
  const d = dict(locale);
  const sep = locale === 'de' || locale === 'pl' ? ':' : '–';
  const base = `${m.homeScore}${sep}${m.awayScore}`;
  if (m.decidedBy === 'pens' && m.homePen != null && m.awayPen != null) {
    return { main: base, note: `${m.homePen}${sep}${m.awayPen} ${d.status.pens}` };
  }
  if (m.decidedBy === 'aet') return { main: base, note: d.status.aet };
  return { main: base, note: null as string | null };
}

export function fmtDateI18n(locale: Locale, d: string): string {
  try {
    return new Date(d + 'T00:00:00').toLocaleDateString(LOCALE_META[locale].dateLocale, {
      weekday: 'short',
      month: 'short',
      day: 'numeric',
    });
  } catch {
    return d;
  }
}

function vsWord(locale: Locale): string {
  return dict(locale).common.vs;
}

export function localizeMatch(m: any, locale: Locale): any {
  if (!m) return m;
  if (locale === 'en') return m;
  const d = dict(locale);
  const n = d.narrative;
  const home = entityName(m.home, locale);
  const away = entityName(m.away, locale);
  const city = entityName(m.city, locale);
  const venue = m.venue;
  const date = fmtDateI18n(locale, m.date);
  const stage = stageLabelI18n(locale, m.group, m.roundLabel);
  const score = scoreLine(m, locale);
  const played = m.status === 'FINISHED' || m.status === 'LIVE';
  const whyTpl = m.whyCareScore >= 8 ? n.whyHigh : m.whyCareScore >= 5 ? n.whyMid : n.whyLow;
  const why = fill(whyTpl, { home, away, stage });
  const comp = competitionName(m.competition, locale) || stage;
  const stakes = fill(m.competition === 'world-cup-2026' ? n.stakesWc : n.stakesOther, { stage, comp });
  let headline: string;
  if (m.status === 'LIVE') headline = fill(n.live, { home, away });
  else if (played && score) {
    if (m.decidedBy === 'aet') headline = fill(n.finishedAet, { home, away, score });
    else if (m.decidedBy === 'pens') headline = fill(n.finishedPens, { home, away, score });
    else headline = fill(n.finishedScore, { home, away, score });
  } else headline = fill(n.preview, { home, away });

  const result = !played
    ? fill(n.resultUpcoming, { time: m.time, date })
    : m.decidedBy === 'aet'
      ? fill(n.resultAet, { score })
      : m.decidedBy === 'pens'
        ? fill(n.resultPens, { score })
        : fill(n.resultFt, { score });

  const teaser = [headline, stage, fill(n.atVenue, { venue, city }), date].filter(Boolean).join('. ') + '.';
  const story = [
    fill(n.body1, { home, away, date, venue, city, stage, result }),
    fill(n.body2, { why }),
    fill(n.body3, { stakes }),
  ].join('\n\n');

  const funFacts = [
    score ? fill(n.factScore, { score }) : '',
    fill(n.factVenue, { venue, city }),
    ...(Array.isArray(m.keyPlayers)
      ? m.keyPlayers.slice(0, 2).map((p: any) => fill(n.factPlayer, { name: p.name, team: entityName(p.team, locale) }))
      : []),
  ].filter(Boolean);

  const keyPlayers = (m.keyPlayers || []).map((p: any) => ({
    ...p,
    team: entityName(p.team, locale),
    hook: fill(n.playerHook, { name: p.name, team: entityName(p.team, locale) }),
  }));

  const scoreQs: Record<Locale, string> = {
    en: `What is the ${home} vs ${away} score?`,
    fr: `Quel est le score de ${home} contre ${away} ?`,
    es: `¿Cuál es el marcador de ${home} vs ${away}?`,
    de: `Wie steht es zwischen ${home} und ${away}?`,
    it: `Qual è il risultato di ${home} contro ${away}?`,
    pl: `Jaki jest wynik ${home} kontra ${away}?`,
    zh: `${home}对${away}的结果是什么？`,
    ja: `${home}対${away}の結果は？`,
    ko: `${home} 대 ${away} 결과는?`,
    ar: `ما نتيجة ${home} ضد ${away}؟`,
  };
  const faqs = [
    {
      q: scoreQs[locale],
      a: played && score ? `${headline}. ${stage}. ${fill(n.atVenue, { venue, city })}.` : fill(n.resultUpcoming, { time: m.time, date }),
    },
    {
      q:
        locale === 'fr'
          ? 'Pourquoi ce match compte-t-il ?'
          : locale === 'es'
            ? '¿Por qué importa este partido?'
            : locale === 'de'
              ? 'Warum zählt dieses Spiel?'
              : locale === 'it'
                ? 'Perché questa partita conta?'
                : locale === 'pl'
                  ? 'Dlaczego ten mecz jest ważny?'
                  : locale === 'zh'
                    ? '这场比赛为什么重要？'
                    : locale === 'ja'
                      ? 'この試合が重要な理由は？'
                      : locale === 'ko'
                        ? '이 경기가 왜 중요한가요?'
                        : locale === 'ar'
                          ? 'لماذا تهم هذه المباراة؟'
                          : 'Why does this match matter?',
      a: why,
    },
  ];

  return {
    ...m,
    home,
    away,
    city,
    headline,
    teaser,
    story,
    whyCareReason: why,
    stakes,
    rivalryAngle: n.rivalryDefault,
    resultSummary: result,
    roundLabel: stage,
    funFacts,
    keyPlayers,
    headToHead: n.rivalryDefault,
    _faqs: faqs,
    _vs: vsWord(locale),
    _stage: stage,
  };
}

export function localizeStory(
  s: { title: string; subtitle?: string; excerpt: string; category: string; relatedSlug?: string; sport?: string },
  locale: Locale,
  related?: any,
  slug?: string
): { title: string; subtitle: string; excerpt: string; category: string; body: string[] } {
  const d = dict(locale);
  const cat = (d.category as Record<string, string>)[s.category] || s.category;
  if (locale === 'en') {
    return {
      title: s.title,
      subtitle: s.subtitle || '',
      excerpt: s.excerpt,
      category: cat,
      body: [],
    };
  }
  const hit = slug && locale !== 'en' ? STORY_I18N[slug]?.[locale] : undefined;
  if (hit) {
    return {
      title: hit.title,
      subtitle: hit.subtitle,
      excerpt: hit.excerpt,
      category: cat,
      body: hit.body,
    };
  }
  const n = d.narrative;
  if (related) {
    const lm = localizeMatch(related, locale);
    return {
      title: lm.headline,
      subtitle: lm.teaser,
      excerpt: lm.teaser,
      category: cat,
      body: (lm.story as string).split(/\n\n+/),
    };
  }
  const sportKey = (s.sport || 'soccer') as keyof typeof d.sports;
  const sportLabel = d.sports[sportKey]?.label || d.sports.soccer.label;
  const title = `${sportLabel} · ${cat}`;
  const excerpt = fill(n.storyLede, { excerpt: `${sportLabel}. ${cat}. ${n.storyMore}` });
  return {
    title,
    subtitle: '',
    excerpt,
    category: cat,
    body: [excerpt, n.storyMore],
  };
}

export function localizeTeamFields(
  team: { name: string; nick: string; group: string; story: string; rank: number | string; conf: string; titles: number; best: string },
  dossier: { dossier?: string; whatToWatch?: string; xFactor?: string; verdict?: string; funFacts?: string[] } | undefined,
  locale: Locale
) {
  const name = entityName(team.name, locale);
  if (locale === 'en') {
    return {
      name,
      nick: team.nick,
      paras: dossier ? (dossier.dossier || '').split(/\n\n+/).filter(Boolean) : [team.story],
      whatToWatch: dossier?.whatToWatch || '',
      xFactor: dossier?.xFactor || '',
      verdict: dossier?.verdict || '',
      funFacts: dossier?.funFacts || [],
    };
  }
  const d = dict(locale);
  const n = d.narrative;
  const dossierText = fill(n.teamDossier, {
    name,
    g: team.group,
    rank: String(team.rank),
    conf: team.conf,
    titles: String(team.titles),
    best: team.best,
  });
  return {
    name,
    nick: team.nick,
    paras: [dossierText],
    whatToWatch: fill(n.teamWatch, { g: team.group }),
    xFactor: n.teamX,
    verdict: fill(n.teamVerdict, { name, g: team.group }),
    funFacts: [],
  };
}

export function matchFaqs(locale: Locale, m: any): { q: string; a: string }[] {
  const loc = localizeMatch(m, locale);
  return loc._faqs || [];
}
