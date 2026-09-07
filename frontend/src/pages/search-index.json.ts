import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { data, sportOf, isWorldCup } from '../lib/site';

export const GET: APIRoute = async () => {
  const matches = await getCollection('matches');
  const stories = await getCollection('stories');
  const index: any[] = [];

  for (const t of data.teams) {
    index.push({ t: t.name, s: `${t.nick} ${t.group}`, k: `Team · Group ${t.group}`, e: '⚽', u: `/team/${t.slug}` });
  }
  for (const m of matches) {
    const d = m.data;
    const sport = sportOf(d);
    const stage = d.roundLabel
      ? d.roundLabel
      : ['R32', 'R16', 'QF', 'SF', '3RD', 'FINAL'].includes((d.group || '').toUpperCase())
      ? d.group
      : isWorldCup(d)
        ? `Group ${d.group}`
        : sport;
    const score =
      d.status === 'FINISHED' && d.homeScore != null ? ` ${d.homeScore}-${d.awayScore}` : '';
    index.push({
      t: `${d.home} vs ${d.away}${score}`,
      s: `${d.headline} ${(d.tags || []).join(' ')}`,
      k: `${sport} · ${stage}`,
      e: '🏟️',
      u: `/match/${d.slug}`,
    });
  }
  for (const s of stories) {
    index.push({ t: s.data.title, s: s.data.excerpt, k: `Story · ${s.data.sport || s.data.category}`, e: '📰', u: `/stories/${s.id}` });
  }
  index.push({ t: 'Sports directory', s: 'Tennis football F1 soccer golf basketball desks', k: 'Page', e: '🗂️', u: '/sports' });
  index.push({ t: 'Tennis', s: 'Wimbledon US Open Alcaraz Sabalenka Noskova', k: 'Sport', e: '🎾', u: '/sport/tennis' });
  index.push({ t: 'Football', s: 'NFL Seahawks Patriots Super Bowl LX kickoff', k: 'Sport', e: '🏈', u: '/sport/football' });
  index.push({ t: 'Formula 1', s: 'Antonelli Monza Mercedes championship', k: 'Sport', e: '🏎️', u: '/sport/f1' });
  index.push({ t: 'Soccer', s: 'Premier League Hull Arsenal', k: 'Sport', e: '⚽', u: '/sport/soccer' });
  index.push({ t: 'Golf', s: 'Ryan Fox Open Scheffler FedEx Cup', k: 'Sport', e: '⛳', u: '/sport/golf' });
  index.push({ t: 'Basketball', s: 'Knicks NBA Finals WNBA Lynx', k: 'Sport', e: '🏀', u: '/sport/basketball' });
  index.push({ t: 'World Cup archive', s: 'Spain champions fixtures groups teams', k: 'Page', e: '🏆', u: '/world-cup' });

  return new Response(JSON.stringify(index), {
    headers: { 'Content-Type': 'application/json', 'Cache-Control': 'public, max-age=3600' },
  });
};
