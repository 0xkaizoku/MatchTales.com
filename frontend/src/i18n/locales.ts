export const LOCALES = ['en', 'fr', 'es', 'de', 'it', 'pl', 'zh', 'ja', 'ko', 'ar'] as const;
export type Locale = (typeof LOCALES)[number];
export const DEFAULT_LOCALE: Locale = 'en';
export const OTHER_LOCALES = LOCALES.filter((l) => l !== DEFAULT_LOCALE);

export type LocaleMeta = {
  /** URL prefix (`zh` for Simplified Chinese). Empty for default locale. */
  path: string;
  /** BCP-47 / HTML lang. Use zh-Hans, never bare zh. */
  htmlLang: string;
  /** hreflang value. zh-Hans not zh. ja not jp. */
  hreflang: string;
  ogLocale: string;
  dateLocale: string;
  dir: 'ltr' | 'rtl';
  nativeName: string;
  englishName: string;
  /** Google Fonts family extra for CJK / Arabic. */
  fontHref?: string;
};

export const LOCALE_META: Record<Locale, LocaleMeta> = {
  en: {
    path: '',
    htmlLang: 'en',
    hreflang: 'en',
    ogLocale: 'en_US',
    dateLocale: 'en-US',
    dir: 'ltr',
    nativeName: 'English',
    englishName: 'English',
  },
  fr: {
    path: 'fr',
    htmlLang: 'fr',
    hreflang: 'fr',
    ogLocale: 'fr_FR',
    dateLocale: 'fr-FR',
    dir: 'ltr',
    nativeName: 'Français',
    englishName: 'French',
  },
  es: {
    path: 'es',
    htmlLang: 'es',
    hreflang: 'es',
    ogLocale: 'es_ES',
    dateLocale: 'es-ES',
    dir: 'ltr',
    nativeName: 'Español',
    englishName: 'Spanish',
  },
  de: {
    path: 'de',
    htmlLang: 'de',
    hreflang: 'de',
    ogLocale: 'de_DE',
    dateLocale: 'de-DE',
    dir: 'ltr',
    nativeName: 'Deutsch',
    englishName: 'German',
  },
  it: {
    path: 'it',
    htmlLang: 'it',
    hreflang: 'it',
    ogLocale: 'it_IT',
    dateLocale: 'it-IT',
    dir: 'ltr',
    nativeName: 'Italiano',
    englishName: 'Italian',
  },
  pl: {
    path: 'pl',
    htmlLang: 'pl',
    hreflang: 'pl',
    ogLocale: 'pl_PL',
    dateLocale: 'pl-PL',
    dir: 'ltr',
    nativeName: 'Polski',
    englishName: 'Polish',
  },
  zh: {
    path: 'zh',
    htmlLang: 'zh-Hans',
    hreflang: 'zh-Hans',
    ogLocale: 'zh_CN',
    dateLocale: 'zh-CN',
    dir: 'ltr',
    nativeName: '简体中文',
    englishName: 'Chinese',
    fontHref:
      'https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@500;600;700&family=Noto+Serif+SC:wght@400;600&display=swap',
  },
  ja: {
    path: 'ja',
    htmlLang: 'ja',
    hreflang: 'ja',
    ogLocale: 'ja_JP',
    dateLocale: 'ja-JP',
    dir: 'ltr',
    nativeName: '日本語',
    englishName: 'Japanese',
    fontHref:
      'https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@500;600;700&family=Noto+Serif+JP:wght@400;600&display=swap',
  },
  ko: {
    path: 'ko',
    htmlLang: 'ko',
    hreflang: 'ko',
    ogLocale: 'ko_KR',
    dateLocale: 'ko-KR',
    dir: 'ltr',
    nativeName: '한국어',
    englishName: 'Korean',
    fontHref:
      'https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@500;600;700&family=Noto+Serif+KR:wght@400;600&display=swap',
  },
  ar: {
    path: 'ar',
    htmlLang: 'ar',
    hreflang: 'ar',
    ogLocale: 'ar_SA',
    dateLocale: 'ar',
    dir: 'rtl',
    nativeName: 'العربية',
    englishName: 'Arabic',
    fontHref:
      'https://fonts.googleapis.com/css2?family=Noto+Sans+Arabic:wght@500;600;700&family=Noto+Naskh+Arabic:wght@400;600&display=swap',
  },
};

export function isLocale(value: string | undefined | null): value is Locale {
  return !!value && (LOCALES as readonly string[]).includes(value);
}

/** First path segment if it is a non-default locale. */
export function localeFromPath(pathname: string): Locale {
  const first = (pathname || '/').split('/').filter(Boolean)[0];
  if (first && isLocale(first) && first !== DEFAULT_LOCALE) return first;
  return DEFAULT_LOCALE;
}

/** English path (`/match/foo`) from any locale URL. */
export function stripLocalePrefix(pathname: string): string {
  const locale = localeFromPath(pathname);
  if (locale === DEFAULT_LOCALE) {
    const p = pathname || '/';
    return p.length > 1 && p.endsWith('/') ? p.slice(0, -1) : p || '/';
  }
  const rest = pathname.replace(new RegExp(`^/${locale}(?=/|$)`), '') || '/';
  return rest.length > 1 && rest.endsWith('/') ? rest.slice(0, -1) : rest;
}

/** Prefix an English-root path for a locale. English stays unprefixed. */
export function localePath(locale: Locale, path: string): string {
  let p = path || '/';
  if (!p.startsWith('/')) p = `/${p}`;
  const stripped = stripLocalePrefix(p);
  if (locale === DEFAULT_LOCALE) return stripped === '' ? '/' : stripped;
  if (stripped === '/') return `/${locale}`;
  return `/${locale}${stripped}`;
}

/** Static HTML pages use a trailing slash. Keep files (rss.xml, json) bare. */
export function withTrailingSlash(path: string): string {
  if (!path || path === '/') return '/';
  if (/\.[a-z0-9]+$/i.test(path.split('/').pop() || '')) return path;
  return path.endsWith('/') ? path : `${path}/`;
}

export function fill(template: string, vars?: Record<string, string | number>): string {
  if (!vars) return template;
  return template.replace(/\{(\w+)\}/g, (_, k) => (vars[k] == null ? '' : String(vars[k])));
}
