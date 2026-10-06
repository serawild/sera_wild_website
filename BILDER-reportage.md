# Bilder für die Reportage-Seite — Bildablage

Zwölf Dateien, alle als **JPG**. Der Dateiname entscheidet alles — er muss
**exakt** so lauten wie hier, **durchgehend klein geschrieben**, ohne
Leerzeichen und ohne Zusätze wie `_final` oder `Kopie`.

> Grossbuchstaben sind die häufigste Falle: Dein Mac unterscheidet sie nicht,
> der Server unterscheidet sie schon. `Reportage-Galerie-01.jpg` landet dann
> live als fehlendes Bild.

## 1. Hero — das grosse Bild ganz oben

| Datei | Format | Mindestens |
|---|---|---|
| `hero-reportage.jpg` | quer, ca. 3 : 2 | 2400 × 1550 |
| `hero-reportage-hoch.jpg` | hoch, 3 : 4 | 1200 × 1600 |

Das Bild läuft über den ganzen Bildschirm, mit einem dunklen Schleier darüber
und dem Titel unten links. Die zweite Datei ist derselbe Moment als
Hochformat-Ausschnitt fürs Handy — ohne sie wird das Querbild beschnitten und
es geht links und rechts einiges verloren.

**Wichtig:** Unten links liegt Text auf dem Bild. Dort sollte nichts
Entscheidendes sein — kein Gesicht, kein Logo.

## 2. Collage — neun Bilder, Abschnitt «Was ich fotografiere»

Drei Reihen zu drei Bildern. In jeder Reihe ein Querbild, daneben zwei
Hochformate. Das Querbild wandert von Reihe zu Reihe:

| Reihe | links | Mitte | rechts |
|---|---|---|---|
| 1 | **`reportage-galerie-01.jpg`** quer | `reportage-galerie-02.jpg` hoch | `reportage-galerie-03.jpg` hoch |
| 2 | `reportage-galerie-04.jpg` hoch | `reportage-galerie-05.jpg` hoch | **`reportage-galerie-06.jpg`** quer |
| 3 | `reportage-galerie-07.jpg` hoch | **`reportage-galerie-08.jpg`** quer | `reportage-galerie-09.jpg` hoch |

| Format | Dateien | Verhältnis | Mindestens | Besser |
|---|---|---|---|---|
| quer | `-01`, `-06`, `-08` | 3 : 2 | 1320 × 880 | 1800 × 1200 |
| hoch | alle übrigen sechs | 2 : 3 | 600 × 900 | 1200 × 1800 |

**Die Nummer bestimmt den Platz, nicht die Reihenfolge deiner Auswahl.** Wenn
dein stärkstes Bild quer ist, gehört es auf `-01` — das ist der erste Platz,
oben links.

Beschnitten wird nichts: Jedes Bild bekommt genau den Platz, der zu seinem
Verhältnis passt. Liegt eines in 4 : 5 statt 2 : 3 vor, stimmt die Reihe
trotzdem — sie wird nur etwas flacher. Nur quer und hoch dürfen nicht
vertauscht werden, sonst kippt der Rhythmus.

## 3. Kontakt — das Bild im letzten Abschnitt

| Datei | Format | Mindestens |
|---|---|---|
| `reportage-kontakt.jpg` | hoch, 4 : 5 | 960 × 1200 |

## Wohin damit

Am einfachsten: alle zwölf in **einen** Ordner legen — Schreibtisch genügt —
und mir sagen, wo er liegt. Ich sortiere sie in die richtigen Ordner im
Projekt, trage sie in `spec/bilder.json` ein und schalte sie scharf.

Wer selber einsortieren will:

    hero-reportage.jpg, hero-reportage-hoch.jpg  →  src/assets/images/Hero_Bilder/
    die drei Querbilder (-01, -06, -08)          →  src/assets/images/Galerie_3-2/
    die sechs Hochformate                        →  src/assets/images/Galerie_2-3/
    reportage-kontakt.jpg                        →  src/assets/images/Galerie_4-5/

## ALT-Texte

Die schreibe ich, sobald ich die Bilder sehe — ein Satz pro Bild, der
beschreibt, was darauf zu sehen ist. Du liest sie gegen. Bis dahin steht in
`bilder.json` überall «ALT-Text fehlt noch».

## Solange Bilder fehlen

Es bleibt eine beige Fläche mit dem Dateinamen darin stehen. Die Seite
funktioniert, man sieht nur, was noch aussteht. Es müssen also nicht alle
zwölf aufs Mal kommen.
