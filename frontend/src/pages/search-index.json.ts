import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { data } from '../lib/site';

export const GET: APIRoute = async () => {
  const matches = await getCollection('matches');
  const stories = await getCollection('stories');
  const index: any[] = [];

  for (const t of data.teams) {
    index.push({ t: t.name, s: t.nick, k: `Team · Group ${t.group}`, e: t.flag, u: `/team/${t.slug}` });
  }
  for (const m of matches) {
    const d = m.data;
    index.push({ t: `${d.home} vs ${d.away}`, s: d.headline + ' ' + d.tags.join(' '), k: `Match · Group ${d.group}`, e: `${d.homeFlag}${d.awayFlag}`, u: `/match/${d.slug}` });
  }
  for (const s of stories) {
    index.push({ t: s.data.title, s: s.data.excerpt, k: `Story · ${s.data.category}`, e: '📖', u: `/stories/${s.id}` });
  }

  return new Response(JSON.stringify(index), {
    headers: { 'Content-Type': 'application/json', 'Cache-Control': 'public, max-age=3600' },
  });
};
