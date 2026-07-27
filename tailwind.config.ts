import type { Config } from 'tailwindcss';

/**
 * Design-Tokens aus dem Figma-Styleguide (Datei „SeraWild | Website").
 * Farben = Markenpalette (Primary/Secondary/Akzent).
 * fontSize/spacing = responsiv (mobile → desktop) via clamp().
 * Siehe CLAUDE.md §4.
 */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,ts,tsx}'],
  theme: {
    extend: {
      colors: {
        dark: '#2F322D', // 1 Dunkelgrün — Text / dunkler Grund
        olive: '#5B5C4F', // 2 Hellgrün — Sekundärfläche
        rust: '#983515', // 3 Rostorange — Hauptakzent
        orange: '#BC541F', // 4 Hellorange — Hover / heller Akzent
        beige: '#A0886D', // 5 Beage — warmes Beige/Taupe
        cream: '#F5F3ED', // 6 Hell — heller Grund / Off-White
      },
      fontFamily: {
        display: ['Vollkorn', 'ui-serif', 'Georgia', 'serif'],
        body: ['Roboto', 'ui-sans-serif', 'system-ui', 'sans-serif'],
      },
      fontSize: {
        // [size, { lineHeight, letterSpacing }] — Werte mobile → desktop
        h1: ['clamp(2.75rem, 1.96rem + 3.38vw, 5rem)', { lineHeight: '1' }], // 44 → 80 (H1 mobile korrigiert)
        h2: ['clamp(2.5rem, 2.15rem + 1.5vw, 3.5rem)', { lineHeight: '1' }], // 40 → 56
        h3: ['clamp(1.75rem, 1.49rem + 1.13vw, 2.5rem)', { lineHeight: '1' }], // 28 → 40
        h4: ['clamp(1rem, 0.74rem + 1.13vw, 1.75rem)', { lineHeight: '1' }], // 16 → 28
        cta: ['clamp(1.5rem, 1.41rem + 0.38vw, 1.75rem)', { lineHeight: '1', letterSpacing: '0.06em' }], // 24 → 28, LS 6
        body: ['clamp(1.25rem, 1.01rem + 1.05vw, 2rem)', { lineHeight: '2' }], // 20 → 32
        small: ['1.5rem', { lineHeight: '1.3' }], // 24 (inkl. Navigation)
      },
      spacing: {
        xs: '0.5rem', // 8 / 6
        sm: '1.25rem', // 20 / 16
        md: '2.5rem', // 40
        lg: 'clamp(3.5rem, 2.6rem + 3.85vw, 5rem)', // 56 → 80
        xl: 'clamp(6.25rem, 2.05rem + 17.9vw, 12.5rem)', // 100 → 200
      },
      maxWidth: {
        content: '1728px', // Design-Breite aus Figma
      },
    },
  },
  plugins: [],
} satisfies Config;
