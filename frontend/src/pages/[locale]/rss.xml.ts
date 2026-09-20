import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { SITE, absoluteUrl, seoDescription } from '../../lib/site';
import { OTHER_LOCALES, isLocale, dict, localePath } from '../../i18n';
import { localizeStory } from '../../i18n/content';

function escapeXml(s: string) {
  return s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');
}

export function getStaticPaths() {
  return OTHER_LOCALES.map((locale) => ({ params: { locale } }));
}

export const GET: APIRoute = async ({ params }) => {
  const locale = params.locale;
  if (!isLocale(locale) || locale === 'en') {
    return new Response('', { status: 404 });
  }
  const d = dict(locale);
  const stories = await getCollection('stories');
  const items = stories
    .map((s) => {
      const loc = localizeStory(s.data, locale, undefined, s.id);
      return { id: s.id, ...s.data, title: loc.title, excerpt: loc.excerpt };
    })
    .sort((a, b) => new Date(b.pubDate).getTime() - new Date(a.pubDate).getTime())
    .slice(0, 50);

  const self = `${SITE.url}${localePath(locale, '/rss.xml')}`;
  const storiesUrl = `${SITE.url}${localePath(locale, '/stories')}`;
  const lang = locale === 'zh' ? 'zh-cn' : locale;

  const body = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:content="http://purl.org/rss/1.0/modules/content/">
  <channel>
    <title>${escapeXml(d.storiesPage.schemaName)}</title>
    <link>${storiesUrl}</link>
    <description>${escapeXml(d.meta.description)}</description>
    <language>${lang}</language>
    <lastBuildDate>${new Date().toUTCString()}</lastBuildDate>
    <atom:link href="${self}" rel="self" type="application/rss+xml"/>
    ${items
      .map(
        (s) => `<item>
      <title>${escapeXml(s.title)}</title>
      <link>${absoluteUrl(localePath(locale, `/stories/${s.id}`))}</link>
      <guid isPermaLink="true">${absoluteUrl(localePath(locale, `/stories/${s.id}`))}</guid>
      <pubDate>${new Date(s.pubDate).toUTCString()}</pubDate>
      <category>${escapeXml(s.excerpt ? d.category[s.category as keyof typeof d.category] || s.category : s.category)}</category>
      <description>${escapeXml(seoDescription(s.excerpt, 300))}</description>
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
