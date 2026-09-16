import { defineMiddleware } from 'astro:middleware';
import { localeFromPath } from './i18n/locales';

export const onRequest = defineMiddleware((context, next) => {
  context.locals.locale = localeFromPath(context.url.pathname);
  return next();
});
