# Prompt für Claude Code — Scheune als Türöffner

Alles ab der Linie kopieren.

---

Vier Textänderungen auf `src/pages/scheune.astro`. Die Scheune soll nicht mehr als eigenes Angebot mit eigener Haltung lesen, sondern als kleiner erster Schritt zum W-Erläbnis. Sonst widerspricht sie der Kernaussage der Website.

Alle Änderungen gelten für beide Fassungen — Rechner und Handy. Die meisten Texte stehen als Konstanten am Dateikopf und wirken dadurch in beiden.

## 1. Der Widerspruch — Konstante `raumP1`, Zeile 9

In diesem Absatz steht heute «Es geht um Bilder, um **Darstellung**, um Spass vor der Kamera». Das ist das Gegenteil dessen, was auf `w-erlaebnis.astro` steht («Reportage statt Posieren», «Bilder, die dich nicht abbilden, sondern zeigen»). Ersetze **nur diesen einen Satz**, der Rest der Konstante bleibt Wort für Wort:

```
const raumP1 = 'Hier darfst du dich austoben – mit deinen Lieblingsoutfits, deinen Ideen, deiner Energie. Es geht ums Ausprobieren: eine Viertelstunde, in der du herausfindest, wie es ist, vor einer Kamera zu stehen, ohne etwas darstellen zu müssen. Und wer weiss – vielleicht entdeckst du dabei den Wunsch nach mehr. Nach Bildern, die nicht nur zeigen wie du aussiehst, sondern wer du bist.';
```

## 2. Neuer Abschnitt «Ein kleiner Schritt, kein grosser Entscheid»

Setz ihn zwischen «01 Raum mit Geschichte» und den Zitat-Abschnitt. Hintergrund Creme wie der Abschnitt darüber, keine Bilder, keine Illustration.

- Kapitelmarke wie auf den anderen Abschnitten, Wort `FÜR WEN`
- Titel: «Ein kleiner Schritt, kein grosser Entscheid.»
- Darunter drei Zeilen untereinander, je durch eine feine Linie in Sand getrennt, gleiche Bauart wie die Leistungsliste auf anderen Seiten:

1. «Du willst wissen, wie sich das anfühlt – ohne dich gleich auf einen halben Tag einzulassen.»
2. «Du brauchst ein gutes Bild von dir. Für dein Profil, deine Website, deine Bewerbung.»
3. «Du liebäugelst mit dem W-Erläbnis und möchtest mich vorher kennenlernen.»

Kein Knopf in diesem Abschnitt. Er ordnet ein, er verkauft nicht.

Auf dem Handy dieselben Inhalte, Polsterung nach `spec/mobil.json`. Trag den Abschnitt dort ebenfalls in der Abschnittsliste von `M2.1_Scheune` nach.

## 3. Der Übergang — Abschnitt «Neugierig auf mehr?»

Der Absatz endet heute mit «Und genau dort beginnen wir beim W-Erläbnis!». Ausserdem steht sein Einstieg («Viele Menschen kommen zu mir und sagen: Ich bin nicht fotogen…») wortgleich auch auf `index.astro` und `geschichten.astro` — dreimal derselbe Text. Auf der Scheune wird er ersetzt.

Neuer Text, mit derselben Auszeichnung wie bisher — der hervorgehobene Teil in `font-display font-semibold italic`, der Rest in `font-body`:

> Manche merken nach fünfzehn Minuten, dass sie mehr Zeit wollen. *Nicht mehr Bilder – mehr Zeit.* Dafür gibt es das W-Erläbnis: zwei bis drei Stunden, draussen, an einem Ort, der dir etwas bedeutet.

Kursiv gesetzt wird nur «Nicht mehr Bilder – mehr Zeit.»

Die Überschrift «Neugierig auf mehr?» bleibt. Der Knopf «schreib mir!» bleibt und zeigt weiterhin auf `/kontakt` — den Weg zum W-Erläbnis übernimmt der Verweis-Abschnitt darunter.

Das gilt für beide Fassungen: Handy um Zeile 328, Rechner um Zeile 358.

## 4. Die Hero-Zeile

«rustikal & echt» wird zu **«Der erste Schritt»**. Zwei Stellen, und sie verhalten sich unterschiedlich:

- **Handy**, Zeile 59: kleine Überzeile in Grossbuchstaben → `DER ERSTE SCHRITT`
- **Rechner**, Zeile 79: das ist die grosse Zeile in `text-h1` über dem Titel → `Der erste Schritt`, in normaler Schreibweise

Der Rest des Heros bleibt: «Dein Fotoshooting: vier Kulissen, eine Stimmung, ganz du.»

## Was unverändert bleibt

- `raumP2`, der Absatz über die fehlende Heizung — Wort für Wort.
- `kulissenBold`, «Wir treffen uns direkt bei der Scheune…»
- Alle Preise und Pakete.
- Der Verweis-Abschnitt «Oder doch das grosse Ganze?» am Seitenende.
- Das Zitat.

## Zum Schluss

Bau, prüf die Seite auf dem Rechner und bei 390 px, und melde mir, was du geändert hast. Die Änderungen auch in `spec/seiten/scheune.json` nachtragen, damit Spec und Code übereinstimmen.
