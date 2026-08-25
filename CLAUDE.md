# Sera Wild — Website

Diese Datei wird bei jedem Start gelesen. Sie gilt immer, auch nach `/clear`.

## Was hier gebaut wird

Die Website von Sera Wild, prozessorientierte Fotografie. Astro mit Tailwind, Ziel ist GitHub Pages.

Der Entwurf liegt in Figma, File-Key `L1sORBHNF7ohDq9DXjruRm`, Seite **Desktop | Designs**. Das Figma-File wurde vollständig auf Auto Layout umgebaut — Abschnitte sind vertikale Auto-Layout-Rahmen, ihre Innereien horizontale oder vertikale Rahmen mit Abständen. Das lässt sich fast eins zu eins in Flexbox übersetzen.

## Die sechs Regeln

1. **Bilder nie aus Figma exportieren.** In Figma liegen nur Platzhalter. Die echten Dateien liegen im Repo. Die Zuordnung steht in `spec/bilder.json`: Das Feld `figmaEbene` nennt den Ebenennamen in Figma, das Feld `datei` den Pfad. Trifft der Code auf eine Ebene `orte-aare.jpg`, wird die Datei aus `datei` eingesetzt.

2. **Texte wörtlich aus Figma.** Nichts umformulieren, nichts ergänzen, nichts erfinden. Keine Platzhaltertexte, keine Blindtexte.

3. **Nicht raten.** Wenn etwas unklar ist: in `OFFEN.md` notieren mit Seite, Abschnitt, Node-ID und Frage — und mit der naheliegenden Lösung weiterbauen. Nicht stehenbleiben, aber auch nicht so tun, als wäre es geklärt.

4. **Ein Abschnitt pro Arbeitsschritt.** Nicht eine ganze Seite auf einmal. Nach jedem Abschnitt kurz melden, was gebaut wurde.

5. **`src/pages/kontakt.astro` ist der Massstab.** Diese Seite ist freigegeben. Abstände, Containerbreiten, Typo-Klassen und die Art, wie Bilder eingebunden sind, kommen von dort.

6. **Drei Seiten gehen nicht online:** Netzwerk, Sara, Emanuela. Nicht bauen, nicht verlinken, nicht in die Sitemap. Auch der Button „Nächste Geschichte" am Ende von `geschichten/simona` entfällt.

## Wo was steht

| Datei | Inhalt |
|---|---|
| `spec/SPEC.md` | Farben, Schriftskala, Raster, Umbruchregeln, Barrierefreiheit |
| `spec/bilder.json` | Zuordnung Figma-Ebene → Bilddatei, mit Anzeigegrösse, Seitenverhältnis und ALT-Text |
| `spec/deko.json` | Positionen aller Illustrationen, relativ zu ihrem Abschnitt, plus Bild- und Wortmarke |
| `spec/seiten/*.json` | Aufbau je Seite: Abschnitte, Layout, Texte, Bildplätze |
| `spec/mobil.json` | Aufbau der mobilen Seiten: Raster, Bausteine, Abschnitte je Seite, Deko |
| `spec/illustrationen/` | Die vier Motive als SVG, `fill="currentColor"` |
| `spec/icons/` | Die fünf Icons für den Fakten-Abschnitt, `stroke="currentColor"` |
| `spec/marken/` | Die Bildmarke W als SVG |
| `public/video/` | Hero-Video für die Über-Seite, MP4 und WebM plus Poster |
| `OFFEN.md` | Offene Fragen und bewusst Weggelassenes |

## Was seit dem letzten Stand dazugekommen ist

**ALT-Texte** stehen für alle 72 aktiven Bilder in `bilder.json`. Nicht selber erfinden, immer von dort nehmen.

**Der Hero auf Über ist ein Video**, kein Bild. Angaben im Eintrag `hero-ueber` unter `video`. Einbinden mit `autoplay muted loop playsinline` und `poster`; bei `prefers-reduced-motion` nur das Poster zeigen.

**Das Angebot heisst nicht mehr „30–40 Bilder"**, sondern Bilderreise mit mindestens 40 Bildern, ohne Wasserzeichen, leicht bearbeitet in Licht, Farbe und Ausschnitt, mit leichter Hautretusche. Steht so in Figma — von dort übernehmen, nicht aus dem Gedächtnis.

**Die Wortmarke „W Erläbnis"** ersetzt zwei Überschriften: den Titel im Hero von W-Erläbnis und die Überschrift der Sektion Erläbnis auf der Startseite. Aufbau und Masse stehen in `deko.json` unter `marken`. Sie wird aus der Bildmarke plus echtem Text gebaut, nicht als Bild eingesetzt.

**Die mobile Fassung steht in Figma**, auf der Seite **Mobile | Designs**. Alle elf Rahmen sind gebaut: M0_Ladebild, M1_Startseite, M2_W-Erläbnis, M2.1_Scheune, M3_Geschichten, M3.1_Simona, M4_Über, M5_Kontakt, M6_Impressum, M7_Datenschutz, M8_AGB. Bezugsbreite 390 px. Raster, Bausteine und Abschnitte stehen in `spec/mobil.json` — von dort bauen, nicht aus Figma neu nachschlagen. Die sieben Hero-Bilder brauchen einen eigenen Hochformat-Ausschnitt, die Platzhalter heissen bereits `hero-*-hoch`.

**Mobile Bilder — nie stehenbleiben.** Zu vielen Bildern gibt es eine zweite Datei mit dem Zusatz `-hoch`, im selben Ordner. Auf schmalen Bildschirmen wird diese genommen, sonst die normale. Fehlt die `-hoch`-Datei: die vorhandene per `object-fit: cover` auf das mobile Seitenverhältnis beschneiden und weiterbauen. Nicht nachfragen, nicht auslassen. Jedes so behandelte Bild in `OFFEN.md` eintragen mit Seite, Bild-ID und Soll-Verhältnis, damit Seraina es anschauen kann.

**Illustrationen liegen nie über Text oder Bild.** Das ist in Figma gegen die Buchstabenumrisse geprüft, mit 10 px Mindestabstand. Wenn im Code etwas überlappt, stimmt die Umrechnung nicht — nicht die Vorlage.

## Seiten und Node-IDs

| Seite | Datei | Figma-Node |
|---|---|---|
| Startseite | `index.astro` | `13:285` |
| W-Erläbnis | `w-erlaebnis.astro` | `45:932` |
| W-Momänt | `w-momaent.astro` | `2018:1202` |
| Geschichten | `geschichten.astro` | `85:1428` |
| Simona | `geschichten/simona.astro` | `85:1705` |
| Über | `ueber.astro` | `2013:854` |
| Kontakt | `kontakt.astro` | `2021:367` — fertig, Referenz |
| Impressum | `impressum.astro` | `2206:226` |
| Datenschutz | `datenschutz.astro` | `2206:251` |
| AGB | `agb.astro` | `2206:276` |

## Abschnitte je Seite

**ueber** `2013:854`
Hero `2236:260` · Fakten `2286:775` · Geschichte Seraina `2246:273` · Geschichte Seraina unten `2246:278` · Zitat `2246:294` · Echtes Portrait `2246:287` · Kontakt-Teaser `2264:3433` · Footer `2013:924`

**geschichten** `85:1428`
Hero `2259:653` · Foto-Story 2 `2166:129` · Authentizität `2264:3270` · Angebot `2264:3245` · Kundenstory Collage `2259:638` · Zitat `2348:977` · Kontakt-Teaser `2264:3425` · Footer `85:1498`

**geschichten/simona** `85:1705`
Hero `2260:679` · Geschichte Oben `2260:661` · Foto-Story `2212:3235` · Geschichte Unten `2260:666` · Collage `2394:958` · Zitat `2260:673` · Weiter-Button `2397:932` (entfällt) · Footer `85:1987`

**w-momaent** `2018:1202` *(Figma-Rahmen: M2.1_Scheune)*
Hero `2257:624` · Raum mit Geschichte `2257:547` · Zitat `2442:1310` · Kulissen `2257:554` · Pakete `2257:579` · neugier `2257:606` · Verweis zurück `2339:919` · Footer `2018:1272`

**index** `13:285`
Hero `2251:342` · Über mich `2251:370` · Erläbnis `2251:390` · Authentizität `2251:410` · Angebot `2251:435` · Galerie/Geschichten `2251:451` · Geschichten gespiegelt `2310:971` · Referenzen `2247:319` · Kontakt-Teaser `2251:495` · Footer `13:760`

**w-erlaebnis** `45:932`
Hero `2253:604` · Begegnung `2253:422` · Das W `2283:775` · Wonach wir suchen `2348:955` · Angebot `2253:444` · Timeline `2255:515` · Zitat `2253:568` · Orte `2285:770` · Verweis Simona `2338:914` · richtig `2253:430` · CTA Banner `2253:406` · FAQ `2253:570` · Footer `2021:247`

## Arbeitsweise

**Zuerst lesen, dann bauen.** Für jede Seite existiert eine Datei `spec/seiten/<slug>.json` mit dem vollständigen Aufbau. Wenn sie fehlt, wird sie zuerst erzeugt: pro Abschnitt ein Figma-Aufruf, Ergebnis in die Datei schreiben. Erst danach bauen — und dann aus der Datei, nicht aus Figma.

Der Grund: Was in Figma nachgeschlagen und nicht aufgeschrieben wird, ist nach dem nächsten `/clear` weg.

**Illustrationen zuletzt**, über `spec/deko.json`, wenn alle Seiten stehen.
