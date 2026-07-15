import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';

// The preview/production environment terminates TLS on the standard HTTPS port,
// so the Vite HMR websocket must be told to connect back over that port.
const HTTPS_PORT = 443;
const DEV_PORT = 3000;

// https://astro.build
export default defineConfig({
  site: 'https://www.matchtales.com',
  compressHTML: true,
  prefetch: {
    prefetchAll: false,
    defaultStrategy: 'hover',
  },
  build: {
    inlineStylesheets: 'auto',
    assets: '_astro',
  },
  integrations: [
    tailwind({ applyBaseStyles: false }),
    sitemap({
      filter: (page) =>
        !page.includes('/404') &&
        !page.includes('/api/') &&
        !page.endsWith('/search-index.json'),
      changefreq: 'daily',
      priority: 0.7,
      lastmod: new Date(),
      serialize(item) {
        const url = item.url;
        // Homepage + fixtures + leaderboard: highest priority
        if (url.endsWith('matchtales.com/') || url.endsWith('matchtales.com')) {
          item.priority = 1.0;
          item.changefreq = 'hourly';
        } else if (url.includes('/match/') || url.includes('/fixtures') || url.includes('/leaderboard')) {
          item.priority = 0.9;
          item.changefreq = 'daily';
        } else if (url.includes('/stories/') || url.includes('/team/')) {
          item.priority = 0.8;
          item.changefreq = 'weekly';
        } else if (url.includes('/group/')) {
          item.priority = 0.75;
          item.changefreq = 'daily';
        } else if (url.includes('/privacy') || url.includes('/about')) {
          item.priority = 0.3;
          item.changefreq = 'monthly';
        }
        return item;
      },
    }),
  ],
  server: {
    host: '0.0.0.0',
    port: DEV_PORT,
  },
  vite: {
    build: {
      cssMinify: true,
      minify: 'esbuild',
      rollupOptions: {
        output: {
          manualChunks: undefined,
        },
      },
    },
    server: {
      allowedHosts: true,
      hmr: { clientPort: HTTPS_PORT },
    },
  },
});
