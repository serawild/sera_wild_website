# Prompt für Claude Code — Illustrationen

Alles ab der Linie kopieren.

---

Die Illustrationen bekommen neue Werte. Alles steht in `spec/deko.json` — Regeln unter `einbau`, Positionen unter `seiten` für den Rechner und unter `mobil.seiten` für das Handy. Lies dort, erfinde nichts dazu.

## Am Rechner ändert sich nichts

Die 26 Positionen in `spec/deko.json` › `seiten` sind von Hand gesetzt und bleiben, wie sie sind. Wenn im Code etwas anders aussieht als dort beschrieben, ist die Umrechnung in `DekoIllustration.astro` falsch — nicht die Vorlage. Melde solche Stellen, statt sie zu verschieben.

## Am Handy wird neu verteilt

Unter `spec/deko.json` › `mobil.seiten` stehen für jede der sieben Seiten vier Illustrationen. Sie sind kleiner als am Rechner — 122 bis 186 px statt 130 bis 450 — und laufen zu knapp der Hälfte über den Seitenrand hinaus.

Zwei Felder verhalten sich anders als am Rechner:

**`obenAbAnkerAnteil`** ist kein Pixelwert, sondern ein Anteil der Abschnittshöhe. `0.42` heisst: die Oberkante der Illustration sitzt bei 42 Prozent der Höhe dieses Abschnitts. So bleibt die Angabe gültig, auch wenn ein Abschnitt durch andere Umbrüche höher oder tiefer wird als in Figma.

**`abstandVomRand`** ist negativ. Die Illustration läuft über den Seitenrand hinaus; der Überstand wird vom `overflow-hidden` des umgebenden Blocks beschnitten. Das ist gewollt — nicht auf 0 korrigieren.

Das Feld **`bildzoneImAbschnitt`** ist nur ein Hinweis für dich: Wo es `true` ist, enthält der Abschnitt Bilder. Die sitzen dort immer unten, deshalb steht die Illustration im oberen Drittel. Prüf beim Bauen, ob das im gerenderten Layout stimmt.

## Die Regeln

Sie stehen in `spec/deko.json` › `einbau.regeln`, die Abweichungen fürs Handy unter `mobil.regelnAbweichend`. Der wichtigste Unterschied:

- **Am Rechner** liegt die Illustration nie hinter Text und nie über einem Bild.
- **Am Handy** darf sie hinter Text liegen. Auf 390 px Breite mit 24 px Rand gibt es sonst keinen Platz. Über einer Bildfläche liegt sie auch dort nie.

In beiden Fällen: Deckkraft 0.6, hinterstes Element im Abschnitt, nie gespiegelt.

## Zu tun

1. Alle bestehenden `<DekoIllustration />`-Aufrufe entfernen, auf allen Seiten, beide Fassungen.
2. Neu setzen aus `spec/deko.json`: `seiten` für den Rechner, `mobil.seiten` fürs Handy.
3. `DekoIllustration.astro` um `obenAbAnkerAnteil` erweitern — der Anteil wird gegen die tatsächliche Höhe des Elternabschnitts gerechnet, nicht gegen einen festen Wert aus Figma.
4. Jeder Abschnitt mit einer Illustration braucht `overflow-visible` in der Senkrechten und `overflow-hidden` in der Waagrechten, damit der Überstand am Seitenrand beschnitten wird, ohne dass die Seite breiter wird. Der Schutz gegen Querscrollen auf `<body>` bleibt.
5. Melden: für jede Seite, wie viele gesetzt sind, und wo eine Illustration im Browser doch über einem Bild landet.

## Was du nicht tun sollst

Keine Positionen erfinden, keine verschieben, weil dir etwas komisch vorkommt. Wenn eine Illustration falsch liegt, melde sie mit Seite, Abschnitt und Motiv — ich korrigiere die Vorlage.

## Zum Schluss

Bau, geh alle Seiten durch, am Rechner und bei 390 px. Am Handy zuerst die Startseite zeigen, bevor du die anderen sechs machst.
