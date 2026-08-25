# Prompt für Claude Code — Wortmarke W Momänt in den Hero

Alles ab der Linie kopieren.

---

Die Seite `w-momaent.astro` bekommt im Hero die Wortmarke statt einer Titelzeile — genau wie `w-erlaebnis.astro`.

## Was schon da ist

Die Wortmarke wird **nicht** als Bild eingesetzt. Sie besteht aus der W-Bildmarke als Inline-SVG plus dem Wort als echtem Text, absolut darübergelegt. So ist sie scharf, skalierbar und lesbar. Auf `w-erlaebnis.astro` steht das bereits — mobil um Zeile 167, für den Rechner um Zeile 191.

Die Masse für beide Wortmarken stehen in `spec/deko.json` unter `marken`: `wortmarke` für Erläbnis, `wortmarkeMomaent` für Momänt.

## 1. Zuerst eine gemeinsame Komponente bauen

Die Konstruktion steht heute dreimal im Code — zweimal auf `w-erlaebnis.astro`, einmal auf `index.astro` — jedes Mal mit von Hand ausgerechneten rem-Werten. Mit der vierten und fünften Stelle wird das unhaltbar. Bau `src/components/Wortmarke.astro`:

```ts
interface Props {
  wort: 'Erläbnis' | 'Momänt';
  breite: number;    // Breite des ganzen Blocks in rem
  klasse?: string;   // z. B. 'text-cream'
}
```

Alle Masse leiten sich aus einem Bezugsrahmen ab. Er ist für beide Wortmarken gleich, ausser in der Gesamtbreite:

| Grösse | Erläbnis | Momänt |
|---|---|---|
| Bezugsbreite | 532 | 539 |
| Höhe | 222 | 222 |
| Breite des W | 308 | 308 |
| Text von links | 160 | 160 |
| Text von oben | 56 | 56 |
| Schriftgrösse | 96 | 96 |
| Zeilenhöhe | 1.396 | 1.396 |

Der Massstab ist `breite * 16 / Bezugsbreite`. Alle sieben Werte werden damit multipliziert und in rem ausgegeben. Rechne sie im Frontmatter aus, schreib keine Zahlen von Hand in die Klassen.

Wichtig: **Text von oben ist bei beiden 56.** Gleiche Schrift, gleiche Grösse, gleiche Zeilenhöhe heisst gleiche Grundlinie — die beiden Wortmarken stehen damit auf derselben Linie. Nicht nachjustieren.

Die Komponente gibt aus:

- ein `<span class="relative block">` mit der berechneten Breite und Höhe
- darin das W als Inline-SVG, `viewBox="0 0 1765.27 1262.84"`, `fill="currentColor"`, `aria-hidden="true"`, absolut oben links
- darin das Wort als `<span>` in `font-display font-semibold`, absolut positioniert, `aria-hidden="true"`

Die Farbe kommt über `klasse` und `currentColor` — nicht über `fill` fest verdrahten.

Für Barrierefreiheit: Die Komponente selbst trägt kein `aria-label`. Das setzt die aufrufende Seite an ihr `<h1>`, so wie heute schon.

## 2. Auf `w-momaent.astro` einsetzen

Im Hero die Titelzeile «W-Momänt» durch die Wortmarke ersetzen. Aufbau wie auf `w-erlaebnis.astro`:

- **Rechner:** `<h1 aria-label="W-Momänt">` mit `<Wortmarke wort="Momänt" breite={27.875} klasse="text-cream" />`, darunter der Untertitel «Vier Kulissen, eine Stimmung, ganz du.» in `text-h2`
- **Handy:** `<h1 aria-label="W-Momänt">` mit `<Wortmarke wort="Momänt" breite={15.1875} klasse="text-cream" />`, darunter der Untertitel in 18 px

Die Überzeile «Der erste Schritt» bleibt und steht **über** der Wortmarke.

Die Breiten 27.875 und 15.1875 rem entsprechen genau den Werten von W-Erläbnis, umgerechnet auf den 7 px breiteren Bezugsrahmen. Damit wirken beide Heros gleich gross.

## 3. Die drei bestehenden Stellen umstellen

Erst wenn W-Momänt steht und stimmt:

- `w-erlaebnis.astro`, Hero mobil und Rechner → `<Wortmarke wort="Erläbnis" breite={15} … />` und `breite={27.5}`
- `index.astro`, Abschnitt Erläbnis, um Zeile 221 → dieselbe Komponente mit der dort verwendeten Breite

**Vergleich vorher/nachher machen.** Diese drei Stellen sind heute richtig und freigegeben. Wenn die Komponente sie auch nur um ein Pixel verschiebt, stimmt die Umrechnung nicht — dann liegt der Fehler bei der Komponente, nicht bei der Vorlage. Melde mir das Ergebnis, bevor du weitergehst.

## Was nicht gemacht wird

`spec/marken/w-momaent.svg` ist die Fassung mit den Buchstaben in Kurven. Sie ist für den Druck gedacht — Flyer, Visitenkarte — und wird auf der Website **nicht** verwendet.

## Zum Schluss

Bau, prüf beide Heros auf dem Rechner und bei 390 px, und leg die Seiten W-Erläbnis und W-Momänt nebeneinander: Die Wortmarken müssen gleich gross wirken und auf derselben Höhe sitzen.
