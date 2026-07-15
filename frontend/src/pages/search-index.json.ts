import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { data } from '../lib/site';

export const GET: APIRoute = async () => {
  const matches = await getCollection('matches');
  const stories = await getCollection('stories');
  const index: any[] = [];

  for (const t of data.teams) {
    index.push({ t: t.name, s: `${t.nick} ${t.group}`, k: `Team · Group ${t.group}`, e: '⚽', u: `/team/${t.slug}` });
  }
  for (const m of matches) {
    const d = m.data;
    const stage = ['R32', 'R16', 'QF', 'SF', '3RD', 'FINAL'].includes((d.group || '').toUpperCase())
      ? d.group
      : `Group ${d.group}`;
    const score =
      d.status === 'FINISHED' && d.homeScore != null ? ` ${d.homeScore}-${d.awayScore}` : '';
    index.push({
      t: `${d.home} vs ${d.away}${score}`,
      s: `${d.headline} ${(d.tags || []).join(' ')}`,
      k: `Match · ${stage}`,
      e: '🏟️',
      u: `/match/${d.slug}`,
    });
  }
  for (const s of stories) {
    index.push({ t: s.data.title, s: s.data.excerpt, k: `Story · ${s.data.category}`, e: '📰', u: `/stories/${s.id}` });
  }
  index.push({ t: 'Leaderboards', s: 'Group tables goals knockout progress', k: 'Page', e: '📊', u: '/leaderboard' });
  index.push({ t: 'Fixtures & Schedule', s: 'All World Cup 2026 matches', k: 'Page', e: '📅', u: '/fixtures' });

  return new Response(JSON.stringify(index), {
    headers: { 'Content-Type': 'application/json', 'Cache-Control': 'public, max-age=3600' },
  });
};
