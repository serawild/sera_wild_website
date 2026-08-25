# Prompt für Claude Code — W im mobilen Footer nach rechts

Alles ab der Linie kopieren.

---

Im mobilen Footer in `src/components/Footer.astro` (Block `md:hidden`, ab Zeile 121) sitzt die W-Bildmarke heute hinter dem Text: `left:12px; top:56px; width:370px; height:265px; opacity:0.1`.

Sie soll neu **rechts neben dem Text** stehen, gross, unten angesetzt, und rechts über den Seitenrand hinauslaufen — so führt der Schwung des W aus dem Bild heraus. Die Position ist in Figma auf allen zehn mobilen Rahmen gesetzt, die Werte unten sind von dort abgemessen.

## Die Bildmarke

Der Wrapper um `wSvg` bekommt:

- `right: -4.125rem` (−66 px) statt `left: 12px` — die Marke läuft rechts aus dem Baustein hinaus
- `bottom: 0.5625rem` (9 px) statt `top: 56px` — unten angesetzt, nicht mittig
- `width: 17.875rem` (286 px), `height: auto` statt der festen 265 px
- `opacity: 0.12` statt `0.1` — sie steht jetzt frei und darf etwas kräftiger sein
- `aria-hidden="true"` und `pointer-events: none` bleiben
- Farbe bleibt `#F5F3ED`

Der äussere Block hat bereits `overflow-hidden` — das bleibt so und ist hier wichtig: Es beschneidet den Überstand am rechten Rand, statt die Seite breiter zu machen.

## Der Textblock

Die Spalte mit Logo, Telefon, E-Mail und Rechtszeile wird auf die linke Hälfte begrenzt:

- feste Breite `15.25rem` (244 px) statt der vollen Breite
- linke Polsterung bleibt `1.5rem` (24 px), die **rechte fällt weg**
- die Rechtszeile «Datenschutz · Impressum · AGB» muss auf einer Zeile bleiben. Bei 220 px Innenbreite passt sie. Wenn sie in deiner Umsetzung trotzdem umbricht, verkleinere sie nicht — prüf zuerst die Polsterung.

Der Textblock behält seine Reihenfolge und bleibt vor der Bildmarke, also weiterhin `relative`.

Der linke Ausläufer der Bildmarke reicht bis unter das Ende der E-Mail-Adresse und der Rechtszeile. Das ist gewollt — dort ist der Strich dünn und blass, die Lesbarkeit bleibt. Nicht «korrigieren», indem du die Marke kleiner machst oder weiter nach rechts schiebst.

## Zum Schluss

Prüf bei 390 px und bei 320 px Breite. Bei 320 px darf die Bildmarke mitwandern, der Überstand rechts bleibt aber erhalten und der Text darf nicht unleserlich werden. Die Fassung für den Rechner im Block darüber bleibt unangetastet.
