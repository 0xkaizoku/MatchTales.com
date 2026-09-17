import type { Locale } from './locales';
import { DEFAULT_LOCALE, fill, localeFromPath, localePath, LOCALE_META } from './locales';
import type { Messages } from './messages';
import { en, fr } from './messages';
import { es } from './messages-es';
import { de } from './messages-de';
import { it } from './messages-it';
import { pl } from './messages-pl';
import { zh } from './messages-zh';
import { ja } from './messages-ja';
import { ko } from './messages-ko';
import { ar } from './messages-ar';

export type { Locale, LocaleMeta } from './locales';
export type { Messages, FaqItem, SportCopy } from './messages';
export type { PlaygroundCopy } from './playground';
export { playgroundCopy, PLAYGROUND } from './playground';
export {
  LOCALES,
  DEFAULT_LOCALE,
  OTHER_LOCALES,
  LOCALE_META,
  isLocale,
  localeFromPath,
  stripLocalePrefix,
  localePath,
  withTrailingSlash,
  fill,
} from './locales';
export { entityName, competitionName } from './names';

export const MESSAGES: Record<Locale, Messages> = { en, fr, es, de, it, pl, zh, ja, ko, ar };

export function dict(locale: Locale | string | undefined): Messages {
  const loc = (locale && locale in MESSAGES ? locale : DEFAULT_LOCALE) as Locale;
  return MESSAGES[loc];
}

export function t(
  locale: Locale | string | undefined,
  pick: (m: Messages) => string,
  vars?: Record<string, string | number>
): string {
  return fill(pick(dict(locale)), vars);
}

export function categoryLabel(locale: Locale, category: string): string {
  const d = dict(locale);
  const map = d.category as Record<string, string>;
  return map[category] || category;
}

export function sportCopy(locale: Locale, slug: string) {
  const d = dict(locale);
  const key = slug as keyof typeof d.sports;
  return d.sports[key] || d.sports.soccer;
}

export function htmlLang(locale: Locale): string {
  return LOCALE_META[locale].htmlLang;
}

export function dirOf(locale: Locale): 'ltr' | 'rtl' {
  return LOCALE_META[locale].dir;
}

export function hreflangOf(locale: Locale): string {
  return LOCALE_META[locale].hreflang;
}

export function ogLocaleOf(locale: Locale): string {
  return LOCALE_META[locale].ogLocale;
}

export function dateLocaleOf(locale: Locale): string {
  return LOCALE_META[locale].dateLocale;
}

/** Locale-prefixed paths for a given English-root path. Includes x-default → English. */
export function hreflangAlternates(englishPath: string): { lang: string; path: string }[] {
  const rest = englishPath.startsWith('/') ? englishPath : `/${englishPath}`;
  const out = (['en', 'fr', 'es', 'de', 'it', 'pl', 'zh', 'ja', 'ko', 'ar'] as Locale[]).map((l) => ({
    lang: hreflangOf(l),
    path: localePath(l, rest),
  }));
  out.push({ lang: 'x-default', path: localePath('en', rest) });
  return out;
}

export { localeFromPath as localeOf };
