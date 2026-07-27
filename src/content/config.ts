import { defineCollection, z } from 'astro:content';

/**
 * Content Collection „geschichten" — Kunden-Stories / Case-Studies.
 * Struktur aus der Figma-Sitemap (node 55:1467): Storytelling, Ausgangslage,
 * Herausforderung, Lösung, Verlinkung Kunde. Siehe CLAUDE.md §6.
 */
const geschichten = defineCollection({
  type: 'content',
  schema: ({ image }) =>
    z.object({
      titel: z.string(),
      kunde: z.string(),
      datum: z.date(),
      sprache: z.enum(['de', 'en']).default('de'),
      cover: image(),
      coverAlt: z.string(),
      ausgangslage: z.string().optional(),
      herausforderung: z.string().optional(),
      loesung: z.string().optional(),
      kundenLink: z.string().url().optional(),
      published: z.boolean().default(true),
    }),
});

export const collections = { geschichten };
