# Saras Geschichte — Bildauswahl

22 Dateien für 21 Bildplätze. Der Hero braucht zwei Versionen (quer für den Rechner, hoch fürs Handy), alle anderen je eine.

**So läuft es:** Bild aussuchen → exakt so benennen wie unten → in den angegebenen Ordner legen. Dateiname und Ordner sind verbindlich, sonst findet die Seite das Bild nicht. Format `.jpg`, gross genug (mindestens die 1,5-fache Anzeigebreite), Astro rechnet danach selbst AVIF/WebP.

---

## Hero — ganz oben

Titel darüber: «Die Geschichte von Sara»
Untertitel: «Sera hat eine super Stimmung geschaffen, sodass es mir leicht fiel, natürlich in die Kamera zu schauen.»
Der Text liegt hell auf dem Bild, dahinter ein dunkler Schleier. Also ein Bild, das unten links Ruhe hat.

| Datei | Format | Anzeige | Ordner |
|---|---|---|---|
| `hero-sara.jpg` | quer, 1.55 : 1 | 1728 × 1117 | `src/assets/images/Hero_Bilder/` |
| `hero-sara-hoch.jpg` | hoch, 0.63 : 1 | fürs Handy | `src/assets/images/Hero_Bilder/` |

---

## 01 Geschichte oben — ein grosses Bild

Danebenstehender Text: «Sara berät Frauen zu ihrer Gesundheit. Ihre Kundinnen kennen sie als jemanden, der zuhört, erklärt und dabei lacht.»
Das Bild trägt den ganzen Abschnitt — am ehesten ein ruhiges Porträt.

| Datei | Format | Anzeige | Ordner |
|---|---|---|---|
| `sara-geschichte-oben.jpg` | hoch, 0.76 : 1 | 560 × 740 | `src/assets/images/Galerie_4-5/` |

---

## 02 Foto-Story — drei Bilder

Überschrift: «Alles begann mit der Frage: ‹Wie zeige ich auf Bildern, was meine Kundinnen längst an mir kennen?›»
Hier darf Bewegung rein: Küche, Wald, Handlung.

| Datei | Format | Anzeige | Ordner |
|---|---|---|---|
| `sara-fotostory-01.jpg` | hoch, 0.89 : 1 | 580 × 650 | `src/assets/images/Galerie_4-5/` |
| `sara-fotostory-02.jpg` | quer, 1.49 : 1 | 700 × 470 | `src/assets/images/Galerie_3-2/` |
| `sara-fotostory-03.jpg` | hoch, 0.92 : 1 | 580 × 630 | `src/assets/images/Galerie_4-5/` |

---

## 03 Was geblieben ist — zwei Bilder

Saras eigene Worte daneben: «Ich bin sehr happy mit den Fotos — sie zeigen mich genau so, wie mich meine besten Freunde jeweils erleben.»
Zwei Hochformate nebeneinander, eines grösser. Nähe, Lachen.

| Datei | Format | Anzeige | Ordner |
|---|---|---|---|
| `sara-geschichte-unten-01.jpg` | hoch, 0.70 : 1 | 380 × 540 | `src/assets/images/Galerie_2-3/` |
| `sara-geschichte-unten-02.jpg` | hoch, 13 : 19 | 260 × 380 | `src/assets/images/Galerie_2-3/` |

---

## 04 Collage — vierzehn Bilder

Kapitelmarke: «AUS SARAS W-ERLÄBNIS» · Überschrift: «Ein Ausschnitt aus Saras Bilderreise»
Fotospots: Saras eigene Küche · verschiedene Plätze im Wald bei Aarau

Am Rechner stehen sie in vier Reihen, am Handy als Wischleiste in derselben Reihenfolge. Die Reihenfolge zählt also — 01 wird zuerst gesehen.

**Reihe 1** — vier gleich breite Hochformate, alle 3 : 4, Anzeige 357 × 476, Ordner `src/assets/images/Galerie_4-5/`

- `sara-collage-01.jpg`
- `sara-collage-02.jpg`
- `sara-collage-03.jpg`
- `sara-collage-04.jpg`

**Reihe 2** — ein breites, zwei schmale

| Datei | Format | Anzeige | Ordner |
|---|---|---|---|
| `sara-collage-05.jpg` | quer, 1.79 : 1 | 788 × 440 | `src/assets/images/Galerie_3-2/` |
| `sara-collage-06.jpg` | hoch, 3 : 4 | 330 × 440 | `src/assets/images/Galerie_4-5/` |
| `sara-collage-07.jpg` | hoch, 3 : 4 | 330 × 440 | `src/assets/images/Galerie_4-5/` |

**Reihe 3** — ein breites, zwei hohe

| Datei | Format | Anzeige | Ordner |
|---|---|---|---|
| `sara-collage-08.jpg` | quer, 1.34 : 1 | 668 × 500 | `src/assets/images/Galerie_3-2/` |
| `sara-collage-09.jpg` | hoch, 0.78 : 1 | 390 × 500 | `src/assets/images/Galerie_4-5/` |
| `sara-collage-10.jpg` | hoch, 0.78 : 1 | 390 × 500 | `src/assets/images/Galerie_4-5/` |

**Reihe 4** — ein breites, drei schmale

| Datei | Format | Anzeige | Ordner |
|---|---|---|---|
| `sara-collage-11.jpg` | quer, 3 : 2 | 630 × 420 | `src/assets/images/Galerie_3-2/` |
| `sara-collage-12.jpg` | hoch, 0.63 : 1 | 266 × 420 | `src/assets/images/Galerie_2-3/` |
| `sara-collage-13.jpg` | hoch, 0.63 : 1 | 266 × 420 | `src/assets/images/Galerie_2-3/` |
| `sara-collage-14.jpg` | hoch, 0.63 : 1 | 266 × 420 | `src/assets/images/Galerie_2-3/` |

---

## Was danach noch offen ist

- **ALT-Texte.** Alle 21 Einträge in `spec/bilder.json` haben ein leeres `alt`. Sobald die Bilder da sind, kommen die dazu — sie beschreiben, was zu sehen ist, nicht was es bedeutet.
- **Der `hinweis`-Vermerk** «Platzhalter. Datei fehlt noch» in `spec/bilder.json` fällt dann weg.
- **Saras Freigabe** für die Textfassung, bevor die Seite jemandem gezeigt wird.
