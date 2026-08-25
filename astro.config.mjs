// @ts-check
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import mdx from '@astrojs/mdx';

// https://astro.build/config
export default defineConfig({
  // Eigene Domain (GitHub Pages via CNAME) — kein base-Pfad nötig.
  site: 'https://serawild.com',
  integrations: [tailwind(), mdx()],
  // Die Website ist deutsch. Eine einzelne englische Seite braucht keine
  // i18n-Einstellung — sie wird als normale Datei unter src/pages/en/ angelegt
  // und bekommt im Base-Layout sprache="en" plus den Pfad der deutschen Fassung.
});
