# Kulissen beim W-Momänt — Bildablage

Die Kulissen auf `/w-momaent` lassen sich jetzt durchklicken: links ein
grosses Bild, rechts die Namen. Pro Kulisse sind **beliebig viele Bilder**
möglich — hat eine mehr als eines, erscheinen unter dem Bild kleine Punkte
zum Weiterklicken.

## So legst du Bilder ab

Alle Bilder in **einen** Ordner:

    src/assets/images/Kulissen/

Der Dateiname entscheidet die Zuordnung — ein Kürzel, ein Bindestrich,
eine laufende Nummer:

| Kulisse | Kürzel | Dateinamen |
|---|---|---|
| Vintage mit Charme | `vintage` | `vintage-01.jpg`, `vintage-02.jpg`, … |
| Licht trifft Tiefe | `licht` | `licht-01.jpg`, `licht-02.jpg`, … |
| Zeitlos wie du | `stein` | `stein-01.jpg`, `stein-02.jpg`, … |
| Leinen & Licht | `leinen` | `leinen-01.jpg`, `leinen-02.jpg`, … |

Mehr musst du nicht tun. Kein Eintrag in `bilder.json`, keine Änderung am
Code — die Seite liest den Ordner beim Bauen aus und nimmt alles mit, was
sie findet. Die Reihenfolge ergibt sich aus der Nummer.

## Format und Grösse

Pro Kulisse werden **drei Bilder** gezeigt, jedes in einem anderen Format.
Die Nummer im Dateinamen bestimmt den Platz:

| Datei | Format | Platz | Export mindestens |
|---|---|---|---|
| `<kuerzel>-01.jpg` | **quer 3:2** | unten, liegt zuoberst | **528 × 352**, besser 704 × 470 |
| `<kuerzel>-02.jpg` | **hoch 2:3** | oben links | **312 × 468**, besser 416 × 624 |
| `<kuerzel>-03.jpg` | **hoch 4:5** | oben rechts | **360 × 450**, besser 480 × 600 |

Die drei überlappen sich; daneben steht eine Illustration in Dunkelgrün.

Weitere Dateien (`-04` und folgende) erscheinen nur in der wischbaren
Leiste auf dem Handy, nicht auf dem Rechner.

## Stand (06.10.2026)

| Kulisse | vorhanden | fehlt |
|---|---|---|
| Vintage mit Charme | `-01` quer, `-02` hoch, `-03` hoch | — vollständig |
| Zeitlos wie du | `-01` quer, `-02` hoch, `-03` hoch | — vollständig |
| Licht trifft Tiefe | `-01` hoch | `licht-02` (quer 3:2), `licht-03` (hoch 4:5) |
| Leinen & Licht | `-01` hoch, `-02` hoch | `leinen-03` (hoch 4:5) |

Hat eine Kulisse weniger als drei Bilder, ordnet die Seite die vorhandenen
automatisch an, ohne etwas zu beschneiden — ein Bild gross, zwei überlappend.
Erst ab drei Bildern entsteht die Collage aus der Tabelle oben.

**Achtung bei `licht`:** `licht-01.jpg` ist Hochformat. Sobald zwei weitere
dazukommen, rutscht es in den Querformat-Platz und wird stark beschnitten.
Dann besser ein echtes Querbild als `-01` ablegen und das heutige nach `-03`
umbenennen.

Die alten Dateien `Galerie_2-3/kulissen-01…03.jpg` werden nicht mehr
gebraucht und können weg, sobald alles steht.
