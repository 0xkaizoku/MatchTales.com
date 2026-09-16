import type { APIRoute } from 'astro';
import { buildSearchIndex } from '../lib/searchIndex';

export const GET: APIRoute = async () => {
  const index = await buildSearchIndex('en');
  return new Response(JSON.stringify(index), {
    headers: { 'Content-Type': 'application/json', 'Cache-Control': 'public, max-age=3600' },
  });
};
