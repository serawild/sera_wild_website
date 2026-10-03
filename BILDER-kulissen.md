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

Der Platz ist **560 × 700** Pixel, also Hochformat **4 : 5**.

- mindestens **840 × 1050**
- besser **1120 × 1400**

Exportier im Verhältnis 4:5, dann wird nichts beschnitten. Andere
Hochformate funktionieren auch, die Seite schneidet dann oben und unten
etwas weg.

Die drei bestehenden Bilder sind 1198 × 1800, also 2:3. Sie werden
dadurch oben und unten leicht angeschnitten — bei Gelegenheit in 4:5
nachliefern, dann sitzt es genau.

## Stand

- `vintage-01.jpg` ✓
- `licht-01.jpg` ✓
- `stein-01.jpg` ✓
- `leinen-*` — fehlt noch, zeigt solange eine Platzhalterfläche

Die alten Dateien `Galerie_2-3/kulissen-01…03.jpg` werden nicht mehr
gebraucht und können weg, sobald alles steht.
