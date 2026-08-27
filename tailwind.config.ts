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
        dark: '#2F322D',       // 1 Dunkelgrün — Text / dunkler Grund
        olive: '#5B5C4F',      // 2 Hellgrün — Sekundärfläche
        rust: '#983515',       // 3 Rostorange — Hauptakzent
        orange: '#BC541F',     // 4 Hellorange — Hover / heller Akzent
        beige: '#A0886D',      // 5 Beage — warmes Beige/Taupe
        cream: '#F5F3ED',      // 6 Hell — heller Grund / Off-White
        'cream-warm': '#F5F2ED', // 6b Hell-Warm — minimale Abweichung, beide kommen vor
      },
      fontFamily: {
        display: ['Vollkorn', 'ui-serif', 'Georgia', 'serif'],
        body: ['Roboto', 'ui-sans-serif', 'system-ui', 'sans-serif'],
      },
      fontSize: {
        // [size, { lineHeight, letterSpacing }] — Werte mobile → desktop
        h1: ['clamp(2.75rem, 1.96rem + 3.38vw, 5rem)', { lineHeight: '1.2' }],   // 44 → 80
        h2: ['clamp(2.5rem, 2.1rem + 0.83vw, 3rem)', { lineHeight: '1.2' }],    // 40 → 48
        h3: ['clamp(1.75rem, 1.55rem + 0.42vw, 2rem)', { lineHeight: '1.2' }], // 28 → 32
        h4: ['clamp(1rem, 0.74rem + 1.13vw, 1.75rem)', { lineHeight: '1.2' }],   // 16 → 28
        cta: ['clamp(1.5rem, 1.41rem + 0.38vw, 1.75rem)', { lineHeight: '1', letterSpacing: '0.06em' }], // 24 → 28
        body: ['clamp(1.125rem, 1.056rem + 0.3vw, 1.375rem)', { lineHeight: '1.65' }], // 18 (mobil) → 22 (desktop)
        'body-klein': ['1.125rem', { lineHeight: '1.6' }],                         // 18 px fix
        highlight: ['clamp(1.75rem, 1.49rem + 1.13vw, 2.5rem)', { lineHeight: '1.4' }], // 28 → 40
        small: ['1.125rem', { lineHeight: '1.3' }],                                // 18
        label: ['1rem', { lineHeight: '1.5', letterSpacing: '0.08em' }],          // 16, UC, 8 % LS
        'label-gross': ['2rem', { lineHeight: '1.5', letterSpacing: '0.08em' }],  // 32, UC, 8 % LS
      },
      spacing: {
        xs: '0.5rem', // 8 / 6
        sm: '1.25rem', // 20 / 16
        md: '2.5rem', // 40
        lg: 'clamp(3.5rem, 2.6rem + 3.85vw, 5rem)', // 56 → 80
        xl: '5rem', // 80 px bei 16 px Basis — Standard-Abschnittsabstand
      },
      maxWidth: {
        content: '108rem', // 1728px bei 16px Basis (Entwurfsbreite)
        inhalt: '93rem',   // 1488px bei 16px Basis (Inhaltsbreite, Seitenrand 120 px)
      },
    },
  },
  plugins: [],
} satisfies Config;
