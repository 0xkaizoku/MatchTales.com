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
  integrations: [
    tailwind({ applyBaseStyles: false }),
    sitemap(),
  ],
  server: {
    host: '0.0.0.0',
    port: DEV_PORT,
  },
  vite: {
    server: {
      allowedHosts: true,
      hmr: { clientPort: HTTPS_PORT },
    },
  },
});
