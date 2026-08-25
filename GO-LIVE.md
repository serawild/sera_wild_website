# Was noch fehlt bis zum Livegang

Stand 23. August 2026. Abgehakt wird hier, nicht im Kopf.

## 1. Inhalt und Code

- [ ] **Mobile Fassung bauen.** In Figma stehen alle elf Rahmen, im Code gibt es bisher fast nichts dafür — auf der Startseite drei `md:`-Breakpoints, sonst nichts. Vorlage ist `spec/mobil.json`, Bezugsbreite 390 px.
- [ ] **Drei Seiten gegen Figma nachziehen.** `geschichten.astro` (176 Zeilen), `geschichten/simona.astro` (161) und `scheune.astro` (241) sind gemessen an den Figma-Abschnitten noch dünn. Abschnitt für Abschnitt vergleichen.
- [ ] **`spec/seiten/geschichten.json` und `simona.json` füllen.** Beide sind noch Rümpfe. Erst schreiben, dann bauen.
- [x] ~~**`src/pages/bausteine.astro`** ist eine Werkstattseite.~~ Steht jetzt auf `noindex`.
- [ ] **`OFFEN.md` anlegen.** `CLAUDE.md` verweist darauf, die Datei fehlt.

## 2. Bilder

- [ ] Die vierzehn Hochformat-Ausschnitte sind abgelegt — prüfen, ob alle vierzehn wirklich da sind.
- [ ] **`hero-ueber-hoch`** fehlt noch. Entweder ein Standbild oder ein Hochformat-Schnitt aus dem Video.
- [ ] Nach dem ersten Build durchklicken: Welche Bilder hat Claude Code automatisch beschnitten? Steht in `OFFEN.md`.

## 3. Technik vor dem Schalten

- [x] ~~**`public/robots.txt`** fehlt.~~ Angelegt, `/bausteine` ist ausgeschlossen.
- [x] ~~**Sitemap** fehlt.~~ `src/pages/sitemap.xml.ts` erzeugt sie ohne Zusatzpaket. Neue Seiten dort als Zeile ergaenzen.
- [x] ~~**`public/og-default.jpg`** fehlt.~~ Angelegt: Bildmarke und Wortmarke hell auf Dunkelgrün, 1200 × 630 px.
- [x] ~~**Titel und Beschreibung je Seite.**~~ Geprüft: alle zehn Seiten haben bereits eigene.
- [x] ~~**i18n entscheiden.**~~ Entfernt. Die Website ist deutsch. Eine einzelne englische Seite später: Datei unter `src/pages/en/` anlegen und im Layout `sprache="en"` plus `uebersetzung="/pfad-der-deutschen-seite"` setzen — `hreflang` und `og:locale` stellen sich dann selber.
- [x] ~~**Rechtstexte prüfen lassen.**~~ Bleiben so, bewusst entschieden.

## 4. Schalten

- [ ] `develop` durchtesten: alle zehn Seiten, Handy und Rechner, alle Links, alle Knöpfe.
- [ ] `develop` → `main` zusammenführen.
- [ ] GitHub Actions (`.github/workflows/deploy.yml`) läuft durch.
- [ ] DNS auf serawild.com zeigt richtig, HTTPS greift.
- [ ] Nach dem Livegang: Startseite in der Google Search Console anmelden.

## Was schon steht

Alle zehn Seiten existieren als `.astro`. Der Deploy-Workflow ist eingerichtet, `CNAME` zeigt auf serawild.com. Schriften, Icons, Video und die Illustrationen liegen im Repo. Alle 72 ALT-Texte stehen in `spec/bilder.json`. Der Figma-Entwurf ist für Rechner und Handy vollständig.
