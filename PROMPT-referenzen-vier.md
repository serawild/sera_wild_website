# Prompt für Claude Code — vierte Kundenstimme und 2×2-Raster

Alles ab der Linie kopieren.

---

Auf `src/pages/index.astro` kommt eine vierte Kundenstimme dazu. Auf dem Rechner wird das Dreier-Nebeneinander zu einem 2×2-Raster, auf dem Handy bleibt die Wischleiste und bekommt eine vierte Karte.

Kein Karussell auf dem Rechner. Kundenstimmen sollen auf einen Blick sichtbar sein.

## 1. Die neue Stimme

In der Konstante `referenzen` am Dateikopf (ab Zeile 23) einen vierten Eintrag ergänzen. **Reihenfolge beachten** — die Kacheln werden nach Textlänge gepaart, damit die beiden Reihen je für sich ausgewogen wirken:

```js
const referenzen = [
  {
    id: 'referenz-patricia',
    name: 'PATRICIA',
    zitat:
      'Ich bin wirklich begeistert was für tolle Fotos Seraina gezaubert hat! Sie ist voll auf meine Ideen eingegangen und hat sie noch mit ihrer inspirierenden Art «auf der Jagd nach dem schönsten Bild» optimiert! Seraina hat mich mit ihrer Art und ihrer Begeisterung sehr inspiriert. Ich konnte davon Einiges für mein Leben und meinen Weg mitnehmen.',
  },
  { /* IVOR — bestehender Eintrag, unverändert */ },
  { /* SIMONA — bestehender Eintrag, unverändert */ },
  { /* BEATRICE — bestehender Eintrag, unverändert */ },
];
```

Also: Patricia und Ivor in der oberen Reihe, Simona und Beatrice in der unteren. Die bestehenden drei Texte bleiben Wort für Wort.

## 2. Rechner — vom Dreier zum 2×2

Abschnitt «8b. DESKTOP: Referenzen», um Zeile 540. Heute:

```
<div class="flex gap-[2rem]" style="width:75rem">
```

Neu ein Raster mit zwei Spalten und gleich hohen Zeilen:

```
<div class="grid grid-cols-2 gap-[2rem]" style="width:75rem">
```

An der Kachel selbst ändert sich fast nichts — sie behält Hintergrund, Radius, Polsterung und das runde Portrait. Nur zwei Dinge:

- `flex-1` entfällt, das Raster übernimmt die Breite. `min-w-0` bleibt.
- Die Kachel füllt die Zeilenhöhe: `h-full` ergänzen, damit beide Kacheln einer Reihe gleich hoch sind.

Die Kacheln werden dadurch rund 580 px breit statt 380. Prüf, ob die Zitate darin gut umbrechen — bei Bedarf die Zeilenlänge über die seitliche Polsterung steuern, nicht über die Schriftgrösse.

## 3. Handy — vierte Karte

Abschnitt «8a. MOBILE: 04 Stimmen», um Zeile 474. Beides läuft über `referenzen.map(...)`, die vierte Karte und der vierte Wischpunkt entstehen also von selbst. Prüf trotzdem:

- Die Wischleiste rechnet nirgends mit einer festen Anzahl von drei.
- Das Skript, das den aktiven Punkt setzt, kommt mit vier Karten zurecht.

## 4. Das Bild

Neuer Eintrag `referenz-patricia` in `spec/bilder.json`, quadratisch, wird rund beschnitten dargestellt — gleiche Angaben wie bei `referenz-simona`.

Solange die Datei fehlt: statt eines leeren Kreises einen Kreis in Sand `#A0886D` mit dem Anfangsbuchstaben in Creme, Vollkorn, mittig. Das sieht besser aus als ein grauer Platzhalter und funktioniert notfalls auch dauerhaft. In `OFFEN.md` eintragen.

## 5. Die Überschrift

`referenzenH2` heisst «Was meine Kunden über mich sagen». Bei drei Frauen und einem Mann in der Liste passt «Kundinnen und Kunden» besser — oder «Was meine Kundschaft über mich sagt». Schlag mir eine Fassung vor, ändere sie aber nicht eigenmächtig.

## Zum Schluss

Bau, prüf auf dem Rechner und bei 390 px, und melde, was du geändert hast. `spec/seiten/index.json` nachtragen.
