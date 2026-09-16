import type { APIRoute } from 'astro';
import { OTHER_LOCALES, isLocale } from '../../i18n';
import { buildSearchIndex } from '../../lib/searchIndex';

export function getStaticPaths() {
  return OTHER_LOCALES.map((locale) => ({ params: { locale } }));
}

export const GET: APIRoute = async ({ params }) => {
  const locale = params.locale;
  if (!isLocale(locale) || locale === 'en') {
    return new Response('[]', { status: 404 });
  }
  const index = await buildSearchIndex(locale);
  return new Response(JSON.stringify(index), {
    headers: { 'Content-Type': 'application/json', 'Cache-Control': 'public, max-age=3600' },
  });
};
