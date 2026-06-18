/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,ts,tsx,md,mdx}'],
  darkMode: ['selector', '[data-theme="dark"]'],
  theme: {
    extend: {
      colors: {
        bg: 'hsl(var(--bg) / <alpha-value>)',
        fg: 'hsl(var(--fg) / <alpha-value>)',
        surface: 'hsl(var(--surface) / <alpha-value>)',
        surface2: 'hsl(var(--surface-2) / <alpha-value>)',
        border: 'hsl(var(--border) / <alpha-value>)',
        muted: 'hsl(var(--muted) / <alpha-value>)',
        pitch: 'hsl(var(--pitch) / <alpha-value>)',
        pitch2: 'hsl(var(--pitch-2) / <alpha-value>)',
        sky: 'hsl(var(--accent-sky) / <alpha-value>)',
        coral: 'hsl(var(--accent-coral) / <alpha-value>)',
        lime: 'hsl(var(--accent-lime) / <alpha-value>)',
      },
      fontFamily: {
        head: ['"Space Grotesk"', 'ui-sans-serif', 'system-ui', 'sans-serif'],
        body: ['Spectral', 'Georgia', 'serif'],
        sans: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
        mono: ['"IBM Plex Mono"', 'ui-monospace', 'monospace'],
      },
      borderRadius: {
        card: '14px',
        btn: '12px',
      },
      boxShadow: {
        card: '0 1px 0 rgba(16,24,40,0.06), 0 10px 30px rgba(16,24,40,0.08)',
        cardhover: '0 1px 0 rgba(16,24,40,0.06), 0 18px 50px rgba(16,24,40,0.12)',
      },
      maxWidth: {
        container: '1120px',
      },
    },
  },
  plugins: [],
};
