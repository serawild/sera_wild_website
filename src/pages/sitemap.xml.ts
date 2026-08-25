import type { APIRoute } from 'astro';

/**
 * Sitemap ohne Zusatzpaket.
 *
 * Neue Seite dazu? Hier eine Zeile ergaenzen.
 * Nicht aufnehmen: /bausteine (Werkstattseite) sowie Netzwerk, Sara und
 * Emanuela — die gehen bewusst nicht online.
 *
 * prioritaet ist ein Hinweis an Suchmaschinen, keine Garantie.
 */
const seiten: { pfad: string; prioritaet: string }[] = [
  { pfad: '/', prioritaet: '1.0' },
  { pfad: '/w-erlaebnis', prioritaet: '0.9' },
  { pfad: '/scheune', prioritaet: '0.8' },
  { pfad: '/geschichten', prioritaet: '0.8' },
  { pfad: '/geschichten/simona', prioritaet: '0.7' },
  { pfad: '/ueber', prioritaet: '0.7' },
  { pfad: '/kontakt', prioritaet: '0.9' },
  { pfad: '/impressum', prioritaet: '0.3' },
  { pfad: '/datenschutz', prioritaet: '0.3' },
  { pfad: '/agb', prioritaet: '0.3' },
];

const BASIS = 'https://serawild.com';

export const GET: APIRoute = () => {
  const heute = new Date().toISOString().split('T')[0];

  const eintraege = seiten
    .map(
      ({ pfad, prioritaet }) => `  <url>
    <loc>${BASIS}${pfad}</loc>
    <lastmod>${heute}</lastmod>
    <priority>${prioritaet}</priority>
  </url>`,
    )
    .join('\n');

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${eintraege}
</urlset>
`;

  return new Response(xml, {
    headers: { 'Content-Type': 'application/xml; charset=utf-8' },
  });
};
