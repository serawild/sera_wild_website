# Prompt für Claude Code — mobiles Menü neu gestalten

Alles ab der Linie kopieren.

---

Gestalte das mobile Menü in `src/components/Navigation.astro` neu — den Vollbild-Dialog `#mobile-nav`, der sich beim Tippen auf den Hamburger öffnet. Es geht nur um Aussehen und Aufbau. Die Mechanik bleibt: `<dialog>`, `showModal()`, Schliessen per Knopf, per Escape und per Tippen daneben, Scroll-Sperre auf `<body>`, `aria-expanded` am Hamburger.

## Warum

Die Menüpunkte stehen heute in Vollkorn auf `text-h2`. Das liest sich wie Kapitelüberschriften. Das Menü soll sich wie ein Menü anfühlen: Zeilen mit Icon, in Roboto, mit feinen Trennlinien.

## Aufbau von oben nach unten

**Kopfzeile.** Links das helle Logo, wie bisher. Rechts der Schliessen-Knopf, 40 × 40, das bestehende X-Icon. Polsterung 20 px oben und unten, 24 px seitlich.

**Menüzeilen.** Eine Zeile je Hauptpunkt, in dieser Reihenfolge: Angebot, Geschichten, Sera Wild. Jede Zeile:

- Höhe durch Polsterung 16 px oben und unten, 24 px seitlich
- links ein Icon, 20 px, in Sand `#A0886D`
- der Name in Roboto, `1.0625rem` (17 px), Sperrung `0.02em`, Farbe Creme `#F5F3ED`
- rechts ein Chevron nach unten, 18 px, in Sand — nur bei Punkten mit Untermenü, also Angebot und Geschichten
- darüber eine Trennlinie: `1px solid rgba(160,136,109,0.28)`. Die letzte Zeile bekommt zusätzlich eine untere Linie.

**Untermenüs.** Direkt unter der zugehörigen Zeile, eingerückt auf 58 px von links, Abstand 12 px zwischen den Einträgen, unten 14 px Luft. Roboto `0.9375rem` (15 px). Die aktuell geöffnete Seite in Rostorange `#BC541F`, die übrigen in `rgba(245,243,237,0.65)`. Untermenüs bleiben sichtbar wie bisher — nicht zum Aufklappen machen, das Menü ist kurz genug.

**Icons.** Für Angebot und Geschichten dieselben Motive wie in `MobileNavLeiste.astro` verwenden, damit beide Navigationen als eine Familie lesbar sind — zieh sie in eine gemeinsame Stelle, statt sie zu kopieren. Für Sera Wild fehlt eines: nimm eine schlichte Personen-Silhouette im gleichen Stil, `stroke="currentColor"`, `stroke-width="1.5"`, viewBox `0 0 24 24`, nur Umriss.

**Knopf.** Darunter mit 28 px Abstand: «Schreib mir», Hintergrund Terracotta `#983515`, Text Creme, Radius **8 px** — nicht der bisherige grössere Radius. Roboto `0.875rem` (14 px), Grossbuchstaben, Sperrung `0.1em`, Polsterung 15 px oben und unten, 28 px seitlich. Rechts im Knopf ein Pfeil nach rechts, 16 px. Verlinkt auf `/kontakt`.

**Fusszeile im Menü.** Darunter, Abstand 8 px zwischen den Zeilen, unten 32 px Luft:

- Telefon `+41 79 790 57 01` als `tel:`-Link
- `info@serawild.com` als `mailto:`-Link
- beide Roboto `0.9375rem`, Farbe `rgba(245,243,237,0.75)`
- darunter mit 6 px Abstand `Datenschutz · Impressum · AGB`, Roboto `0.75rem`, Farbe Sand, als drei einzelne Links

**Hintergrund.** Die Bildmarke W aus `spec/marken/w.svg` inline einsetzen, `fill="currentColor"`, Farbe Creme, Deckkraft `0.07`. Absolut positioniert, unten rechts, rund 420 px breit, teilweise über den Rand hinaus — der Dialog bekommt dafür `overflow: hidden`. `aria-hidden="true"` und `pointer-events: none`. Sie liegt hinter allem anderen.

## Was gleich bleibt

- Der Dialog füllt weiterhin den ganzen Bildschirm, Hintergrund Dunkel `#2F322D`.
- Keine abgerundeten Ecken ausser am Knopf.
- Die aktive Seite bekommt weiterhin `aria-current="page"`.
- Der Mohn als Marker beim aktiven Hauptpunkt entfällt — die aktive Seite wird nur noch über die Farbe im Untermenü gezeigt.

## Zum Schluss

Prüf das Menü bei 390 px Breite und bei 320 px. Bei 320 px darf keine Zeile umbrechen und nichts überlaufen. Melde mir, was du geändert hast.
