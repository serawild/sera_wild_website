# Prompt für Claude Code — Schriftskala am Rechner aufräumen

Alles ab der Linie kopieren.

---

Die Typografie am Rechner wird vereinheitlicht und eine Stufe ruhiger gestellt. **Am Handy ändert sich nichts.**

## Was heute nicht stimmt

Im Code stehen für dieselbe Rolle mehrere Grössen nebeneinander:

- Fliesstext in drei Grössen: `text-body` (32), `text-small` (24), `text-body-klein` (22)
- Titel in fünf Grössen: `text-h1` (80), `text-h2` (56), `text-[3rem]` (48), `text-[2.5rem]` (40), `text-[2rem]` (32)

Dazu steht der Zeilenabstand des Fliesstexts auf `2`. Bei 32 px Schrift sind das 64 px von Zeile zu Zeile — das ist der Hauptgrund, warum die Seite überdimensioniert wirkt.

## Die neue Skala

Fünf Werte statt zehn, gemessen bei 1728 px Fensterbreite:

| Rolle | Neu | Bisher |
|---|---|---|
| Hero-Titel | **80** | 80 — unverändert |
| Abschnittstitel | **48** | 56, 48 und 40 gemischt |
| Zwischentitel | **32** | 40 und 32 gemischt |
| Fliesstext | **32, Zeilenabstand 1.65** | 32, Zeilenabstand 2 |
| Kleingedrucktes | **22** | 24 und 22 gemischt |

## 1. Die Token in `tailwind.config.ts`

- `h1` bleibt unverändert.
- `h2`: oberes Ende der clamp von `3.5rem` auf **`3rem`**. Unteres Ende bleibt `2.5rem`. Das mittlere Glied so nachrechnen, dass der Übergang zwischen 768 und 1728 px linear bleibt — nach derselben Methode wie bei den bestehenden Werten.
- `h3`: oberes Ende von `2.5rem` auf **`2rem`**, unteres Ende bleibt.
- `body`: Grösse **unverändert**, nur `lineHeight` von `2` auf **`1.65`**.
- `small`: von `1.5rem` auf **`1.375rem`** — damit deckungsgleich mit `body-klein`.
- `h2klein`, `h3klein`: entfernen, sobald sie nirgends mehr verwendet werden.

**Die Grösse des Fliesstexts bleibt bei 32.** Bei einer Textspalte von 848 px ergibt das rund 53 Zeichen pro Zeile — eine gute Zeilenlänge. Kleiner würde die Zeilen zu lang machen. Nicht verkleinern.

## 2. Die Sonderfälle im Markup ersetzen

Such im Markup für den Rechner nach `text-[3rem]`, `text-[2.5rem]`, `text-[2rem]`, `text-h2klein`, `text-h3klein` und ersetze sie:

- Alles, was ein Abschnittstitel ist → `text-h2`
- Alles, was ein Zwischentitel innerhalb eines Abschnitts ist → `text-h3`

Wo `text-h1` ausserhalb eines Heros steht — laut Suche sieben Mal — prüf jede Stelle einzeln und melde sie mir, bevor du sie änderst. Manche davon sind bewusst gross, zum Beispiel die Zeile über dem Titel im Hero der Scheune.

## 3. Am Handy darf sich nichts ändern

Das ist die wichtigste Bedingung dieses Auftrags.

Die mobilen Blöcke setzen ihre Grössen mit eigenen Werten wie `text-[1.0625rem] leading-[1.68]` und überschreiben die Token damit ohnehin. Aber: **Prüf jedes Element, das ein Token ohne `md:`-Präfix verwendet und auf dem Handy sichtbar ist.** Dort schlägt die Änderung durch. Wenn du solche Stellen findest, gib ihnen einen ausdrücklichen mobilen Wert, damit das Handy so bleibt, wie es ist.

Mach vorher und nachher je einen Durchgang bei 390 px und vergleiche. Es darf sich nichts verschieben.

## 4. Die Skala festschreiben

Trag die fünf Werte in `spec/SPEC.md` ein, mit dem Hinweis, dass es keine weiteren Grössen gibt und Sonderwerte im Markup nicht erlaubt sind. Sonst wächst die Skala beim nächsten Abschnitt wieder.

## Was danach kommt

Durch die kleineren Titel werden die Abschnitte niedriger. Die Illustrationen sitzen dadurch nicht mehr exakt richtig. **Das ist bekannt und wird separat behandelt** — versuch nicht, sie nachzujustieren. Melde mir nur, welche Abschnitte spürbar niedriger geworden sind.

## Zum Schluss

Bau und prüf bei **1440 px** — das ist die häufigste Bildschirmbreite und wichtiger als 1728. Dann bei 1728, dann bei 390. Melde mir, was du geändert hast und welche `text-h1`-Stellen du zur Entscheidung zurückstellst.
