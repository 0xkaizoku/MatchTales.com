import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { SITE, absoluteUrl, seoDescription } from '../lib/site';

function escapeXml(s: string) {
  return s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');
}

export const GET: APIRoute = async () => {
  const stories = await getCollection('stories');
  const items = stories
    .map((s) => ({ id: s.id, ...s.data }))
    .sort((a, b) => new Date(b.pubDate).getTime() - new Date(a.pubDate).getTime())
    .slice(0, 50);

  const body = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:content="http://purl.org/rss/1.0/modules/content/">
  <channel>
    <title>${escapeXml(SITE.name)} Stories</title>
    <link>${SITE.url}/stories</link>
    <description>${escapeXml(SITE.description)}</description>
    <language>en-us</language>
    <lastBuildDate>${new Date().toUTCString()}</lastBuildDate>
    <atom:link href="${SITE.url}/rss.xml" rel="self" type="application/rss+xml"/>
    ${items
      .map(
        (s) => `<item>
      <title>${escapeXml(s.title)}</title>
      <link>${absoluteUrl(`/stories/${s.id}`)}</link>
      <guid isPermaLink="true">${absoluteUrl(`/stories/${s.id}`)}</guid>
      <pubDate>${new Date(s.pubDate).toUTCString()}</pubDate>
      <category>${escapeXml(s.category)}</category>
      <description>${escapeXml(seoDescription(s.excerpt, 300))}</description>
      ${s.image ? `<enclosure url="${escapeXml(s.image)}" type="image/jpeg"/>` : ''}
    </item>`
      )
      .join('\n    ')}
  </channel>
</rss>`;

  return new Response(body, {
    headers: {
      'Content-Type': 'application/rss+xml; charset=utf-8',
      'Cache-Control': 'public, max-age=3600',
    },
  });
};
