# Prompt für Claude Code — mobile Fassung bauen

Alles ab der Linie in Claude Code kopieren.

---

Bau die mobile Fassung der Website. Sie ist kein neuer Inhalt, sondern dasselbe in schmal.

## Wo du stehst

`src/pages/index.astro` ist bereits mobil gebaut, dazu `MobileNavLeiste.astro`, `FaqListe.astro` und `DekoIllustration.astro`. Bau die Startseite nicht neu.

Zwei Dinge dort noch korrigieren, bevor du weitermachst:

- Die Hero-Überschrift steht auf `text-[1.6875rem]` (27 px). Der Wert ist inzwischen **31 px** — also `text-[1.9375rem]`. Nur die Hero-Überschrift, die Abschnitts-Überschriften bleiben bei 27 px.
- Hero-Untertitel sind neu **18 px** bei 160 % Zeilenabstand. Auf der Startseite gibt es keinen, auf den anderen Seiten schon.

Danach der Reihe nach: `w-erlaebnis`, `scheune`, `geschichten`, `geschichten/simona`, `ueber`, `kontakt`, zuletzt `impressum`, `datenschutz`, `agb`. Bei `ueber` und `kontakt` gibt es schon ein paar `md:`-Stellen aus der Zeit davor — die gehören nicht zu dieser Fassung, prüf sie gegen `spec/mobil.json` und zieh sie nach.

## Woher du was nimmst

**Das Layout** steht in `spec/mobil.json`. Dort findest du für jede der elf Seiten: Raster, Farben, Schriftskala, die wiederkehrenden Bausteine, und unter `abschnitte` die Abschnitte in ihrer Reihenfolge mit Hintergrundfarbe, Bildplätzen und Massen. Bezugsbreite ist 390 px.

**Die Texte** nimmst du aus der bestehenden Seite am Rechner. Zu jedem mobilen Abschnitt steht in `spec/mobil.json` das Feld `quelleDesktop` — das ist der Name der Sektion in der zugehörigen `.astro`-Datei, die unter `desktopDatei` genannt ist. Beispiel: `M2_W-Erläbnis` › `01 Begegnung` hat `quelleDesktop: "Sektion – Begegnung"` und `desktopDatei: "src/pages/w-erlaebnis.astro"`. Nimm den Text von dort, Wort für Wort. Nichts umformulieren, nichts kürzen, nichts erfinden.

**Die Bilder** stehen in `spec/bilder.json`. Das Feld `datei` ist die normale Datei, `dateiMobil` die Hochformat-Variante mit dem Zusatz `-hoch`. Der ALT-Text kommt immer aus dem Feld `alt`, auch für die `-hoch`-Fassung.

**Was mobil fehlt, fehlt mit Absicht.** Wo `spec/mobil.json` unter `weggelassen` etwas aufzählt, wird dieser Abschnitt am Handy nicht gezeigt. Nicht ergänzen.

## Wie du baust

Kein neues Seitengerüst. Dieselbe `.astro`-Datei bekommt beide Fassungen, über Tailwind-Breakpoints: schmal ist der Standard, ab `md:` gilt das bestehende Layout am Rechner. Wo sich die Anordnung zu stark unterscheidet — Wischleisten statt Reihen, gestapelte Karten statt Spalten — darfst du zwei Blöcke nebeneinander stellen und mit `md:hidden` beziehungsweise `hidden md:block` umschalten. Der Text darf dabei nur einmal im Quelltext stehen; wenn nötig, zieh ihn in eine Konstante am Dateikopf.

## Bilder — hier bleibst du nie stehen

1. Gibt es die `-hoch`-Datei: auf schmalen Bildschirmen diese ausliefern, sonst die normale. Über `<picture>` mit einem `media`-Wechsel bei 768 px.
2. Fehlt die `-hoch`-Datei: nimm die normale und beschneide sie per `object-fit: cover` auf das Verhältnis, das der mobile Platz verlangt.
3. Fehlt auch die: setz ein Rechteck in Beige `#a0886d` in der richtigen Grösse, mit dem ALT-Text aus `bilder.json`.
4. Jeden Fall aus 2 und 3 in `OFFEN.md` eintragen: Seite, Bild-ID, was du gemacht hast, welches Verhältnis nötig wäre. Eine Zeile pro Bild.

Nicht nachfragen, nicht abbrechen, nicht auslassen.

## Seitenverhältnisse der mobilen Plätze

Heros 0.63 : 1 über die volle Breite. Bildgruppen 3 : 4 — grosses Bild 214 × 286 bei 0/0, kleines 178 × 238 bei 164/84, Unterkanten bewusst versetzt. Wischleisten-Karten 260 × 340. Simonas Collage 220 × 290. Einzelbilder in Textabschnitten 342 × 456. Referenz-Portraits rund, 50 × 50.

## Illustrationen

Erst zum Schluss, wenn alle Seiten stehen. Positionen stehen in `spec/deko.json` unter `mobil`. Die Illustration ist immer das hinterste Element ihres Abschnitts, Deckkraft 0.6. Sie darf hinter Text liegen, nie über einer Bildfläche.

## Arbeitsweise

Eine Seite pro Schritt, innerhalb der Seite ein Abschnitt nach dem anderen. Nach jeder Seite kurz melden: was gebaut wurde und was in `OFFEN.md` gelandet ist.

Fang mit den zwei Korrekturen auf der Startseite an, dann `w-erlaebnis`. Zeig mir das Ergebnis, bevor du weitergehst.
