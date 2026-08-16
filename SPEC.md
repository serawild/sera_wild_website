# Spezifikation Website Sera Wild

Verbindliche Grundlage für den Neubau. Bei Widersprüchen gilt: **Layout, Text und Masse aus Figma, alles andere aus dieser Datei.**

Das Figma-File wurde vollständig auf Auto Layout umgebaut. Der bestehende Code im Repo stammt aus der Zeit davor und ist überholt.

---

## 0. Grundregeln

1. **Keine Bilder aus Figma exportieren.** In Figma liegen nur Platzhalter und Vorschauen. Die echten Bilder liegen als AVIF in `assets/images/`. Zuordnung in `spec/bilder.json`. Jedes `<img>` verweist auf einen Pfad aus dieser Datei.
2. **Die bestehende Website wird vollständig ersetzt.** Alte HTML- und CSS-Dateien überschreiben oder löschen. `assets/images/` bleibt unangetastet.
3. **Die technische Grundlage bleibt wie bisher.** Erst das Repo analysieren, dann im vorhandenen Stack weiterbauen.
4. **Drei Seiten gehen nicht online:** Netzwerk, Sara, Emanuela. Nicht bauen, nicht verlinken, nicht in die Sitemap.
5. **Keine Schriften-CDNs.** Vollkorn und Roboto selbst hosten. Google Fonts würde IP-Adressen übertragen und der Datenschutzerklärung widersprechen.

---

## 1. Umfang

Figma-File-Key `L1sORBHNF7ohDq9DXjruRm`, Seite **Desktop | Designs**.

| Figma-Frame | Node-ID | Zieldatei | im Menü |
|---|---|---|---|
| 1_Startseite | `13:285` | `index.html` | — |
| 2_Erläbnis | `45:932` | `w-erlaebnis.html` | Angebot |
| 2.1_Scheune | `2018:1202` | `scheune.html` | — |
| 3_Geschichten | `85:1428` | `geschichten.html` | Geschichten |
| 4_Simona | `85:1705` | `geschichten/simona.html` | — |
| 5_Über | `2013:854` | `ueber.html` | Sera Wild |
| 6_Kontakt | `2021:367` | `kontakt.html` | Kontakt |
| 7_Impressum | `2206:226` | `impressum.html` | — |
| 8_Datenschutz | `2206:251` | `datenschutz.html` | — |
| 9_AGB | `2206:276` | `agb.html` | — |

**Nicht bauen:** 10_Netzwerk, 4.1_Sara, 4.2_Emanuela. Alle Verweise darauf entfernen, auch den Button „Nächste Geschichte" am Ende von `geschichten/simona.html`.

### Abschnittsfolge

Exakt die Ebenenreihenfolge im jeweiligen Figma-Frame, von oben nach unten.

- **index** — Hero Startseite · Über mich · Erläbnis · Authentizität · Angebot · Galerie/Geschichten · Geschichten (gespiegelt) · Referenzen · Kontakt-Teaser · Footer
- **w-erlaebnis** — Hero · Begegnung · Das W · Wonach wir suchen · Angebot · Timeline · Zitat · Orte · Verweis Simona · richtig · CTA Banner · FAQ · Footer
- **scheune** — Hero · Raum mit Geschichte · Zitat · Kulissen · Pakete · neugier · Verweis zurück · Footer
- **geschichten** — Hero · Foto-Story 2 · Authentizität · Angebot · Kundenstory Collage · Zitat · Kontakt-Teaser · Footer
- **geschichten/simona** — Hero · Geschichte Oben · Foto-Story · Geschichte Unten · Collage · Zitat · Footer *(Weiter-Button entfällt)*
- **ueber** — Hero · Fakten · Geschichte Seraina · Geschichte Seraina unten · Zitat · Echtes Portrait · Kontakt-Teaser · Footer
- **kontakt** — Hero · Kontaktdaten · Footer
- **impressum / datenschutz / agb** — Titelleiste · Inhalt · Footer

---

## 2. Layout

Entwurfsbreite 1728, Inhalt 1488 zentriert, Seitenrand 120. Abschnitte laufen in voller Fensterbreite, der Inhalt darin ist begrenzt.

```css
:root { --inhalt: 1488px; --rand: 120px; }
.abschnitt > .inhalt { max-width: var(--inhalt); margin-inline: auto; }
```

---

## 3. Farben

```css
:root {
  --dunkelgruen: #2F322D;
  --hellgruen:   #5B5C4F;
  --rostorange:  #983515;
  --hellorange:  #BC541F;
  --beige:       #A0886D;
  --hell:        #F5F3ED;
  --hell-warm:   #F5F2ED;
}
```

`--hell` und `--hell-warm` unterscheiden sich minim, beide kommen vor. Den Wert des jeweiligen Abschnitts aus Figma übernehmen, nicht vereinheitlichen.

Text auf hellem Grund `--dunkelgruen`, auf dunklem und rostorangem Grund `--hell`.

---

## 4. Typografie

**Vollkorn SemiBold** für Überschriften, **Roboto Regular** für alles andere.

| Stil | Familie | px | Besonderheit |
|---|---|---|---|
| H1 | Vollkorn SemiBold | 80 | Hero-Titel |
| H2 | Vollkorn SemiBold | 56 | Abschnittstitel |
| H2 Klein | Vollkorn SemiBold | 44 | |
| H3 | Vollkorn SemiBold | 40 | |
| H3 Klein | Vollkorn SemiBold | 32 | |
| H4 | Roboto Regular | 28 | |
| Body | Roboto Regular | 32 | Fliesstext |
| Body Klein | Roboto Regular | 22 | |
| CTA | Roboto Regular | 28 | Grossbuchstaben, 6 % Laufweite |
| Navigation | Roboto Regular | 24 | |
| Small | Roboto Regular | 24 | |
| Label | Roboto Regular | 16 | Grossbuchstaben, 8 % Laufweite |
| Label Gross | Roboto Regular | 32 | Grossbuchstaben, 8 % Laufweite |
| H1 Mobile | Vollkorn SemiBold | 36 | unter 640 px |
| H2 Mobile | Vollkorn SemiBold | 40 | unter 640 px |
| Body Mobile | Roboto Regular | 20 | unter 640 px |

Schriften als `.woff2` in `assets/fonts/`, eingebunden mit `font-display: swap`.

---

## 5. Bilder

### Bestand

```
assets/images/Hero_Bilder/     8 Dateien, lange Kante 3358
assets/images/Galerie_2-3/    25 Dateien, 1200 × 1800
assets/images/Galerie_3-2/    19 Dateien, 1800 × 1200
assets/images/Galerie_4-5/    16 Dateien, 1280 × 1600
assets/images/Quadrat/         3 Dateien, 640 × 640
```

Die Ordner sind nach Seitenverhältnis benannt, nicht nach Seite.

### Zuordnung

`spec/bilder.json`, ein Eintrag je Bildplatz:

```json
{
  "id": "orte-aare",
  "figmaEbene": "orte-aare.jpg",
  "baustein": "Orte",
  "seite": "Erläbnis",
  "anzeige": { "breite": 469, "hoehe": 300 },
  "verhaeltnis": "1.56 : 1",
  "ausrichtung": "quer",
  "alt": "",
  "aktiv": true,
  "datei": "assets/images/Galerie_3-2/orte-aare.avif",
  "dateiMasse": { "breite": 1800, "hoehe": 1200 },
  "deckungsfaktor": 3.84
}
```

Die Figma-Ebene heisst genau wie `figmaEbene`. Trifft der Code auf eine Ebene `orte-aare.jpg`, wird `datei` eingesetzt. Einträge mit `"aktiv": false` überspringen.

### Einbindung

Die Dateien sind grösser als der Anzeigeplatz, damit sie auf Retina-Bildschirmen scharf bleiben.

```css
.bild { aspect-ratio: 469 / 300; object-fit: cover; width: 100%; height: auto; }
```

Das Verhältnis der Datei stimmt nicht immer exakt mit dem Platz überein. `object-fit: cover` schneidet mittig. Das ist gewollt — deshalb wurde nicht jedes Bild einzeln zugeschnitten.

### AVIF und Rückfallebene

Alle Bilder sind AVIF. Safari unterstützt das erst ab 16.4, deshalb pro Bild ein `<picture>`:

```html
<picture>
  <source srcset="assets/images/Galerie_3-2/orte-aare.avif" type="image/avif">
  <img src="assets/images/webp/orte-aare.webp" alt="" width="469" height="300" loading="lazy">
</picture>
```

WebP-Dateien aus den AVIF erzeugen, nach `assets/images/webp/`. Zusätzlich kleinere Varianten mit 640 und 1024 px langer Kante und über `srcset` mit `sizes` anbieten — sonst lädt ein Handy ein 1800-Pixel-Bild für einen 350 Pixel breiten Platz.

**Hero-Bilder:** kein `loading="lazy"`, stattdessen `fetchpriority="high"`.

### ALT-Texte

Das Feld `alt` ist noch leer und wird nachgeliefert. Bis dahin `alt=""` setzen — **nie** den Dateinamen einsetzen.

---

## 6. Illustrationen

Vier Motive als SVG in `spec/illustrationen/`: `mohn.svg`, `tulpe.svg`, `blattzweig.svg`, `eukalyptus.svg`. Einfarbig, Farbe über `fill`.

| Untergrund | Farbe |
|---|---|
| Dunkelgrün | `--hellgruen` |
| Rostorange | `--hellorange` |
| Hell / Hell-warm | `--hellgruen`, teils `--hellorange` |
| Hellgrün | `--beige` |

Position, Grösse, Drehung und Farbe stehen in Figma. Jede Illustration ist ein absolut positioniertes Element direkt im Seitenrahmen, benannt `Deko – …`.

- Sie liegen **über** den Abschnitten, nicht darin. Viele überlappen eine Abschnittskante — das ist der Zweck.
- Dekoration: `aria-hidden="true"`, `pointer-events: none`.
- Sie dürfen aus dem Bild laufen. Seitencontainer braucht `overflow-x: hidden`.
- Sie liegen **nie** über Text oder Bild. Passiert das beim Nachbauen, ist die Position falsch.
- **Unter 768 px Fensterbreite alle ausblenden.** Auf dem Handy fehlt der Rand.

---

## 7. Responsives Verhalten

Figma zeigt nur Desktop. Für kleinere Fenster gilt:

| Breite | Verhalten |
|---|---|
| über 1728 | Inhalt bleibt 1488 zentriert, Hintergründe laufen durch |
| 1024 – 1728 | Inhalt schrumpft mit, Seitenrand 120 → 48 |
| 640 – 1024 | Zweispaltiges wird einspaltig: Bild oben, Text darunter. Rand 32 |
| unter 640 | Mobile-Schriftskala, Rand 24, Illustrationen aus |

Je Bausteintyp:

- **Hero** — Bild als Hintergrund, Text darüber. Auf dem Handy Mindesthöhe 70 vh statt fester 1117 px.
- **Bild-Text-Abschnitte** (Über mich, Begegnung, Kulissen, Geschichte Oben/Unten, richtig) — die versetzt überlappenden Bildgruppen werden unter 1024 zu einer Reihe nebeneinander, unter 640 untereinander.
- **Galerie / Karussell** — Desktop nebeneinander mit Überlauf, Handy waagrecht scrollbar mit `scroll-snap`.
- **Collage** (Simona) — vier Reihen, unter 1024 zwei Spalten, unter 640 eine.
- **Orte** — drei Spalten, unter 1024 zwei, unter 640 eine.
- **Timeline** — Nummern auf dem Handy kleiner, über den Text gerückt.
- **FAQ** — Akkordeon mit `<details>` und `<summary>`, ohne JavaScript.
- **Fakten** — fünf Kacheln, unter 1024 zwei Reihen.

---

## 8. Barrierefreiheit

- Jedes Bild mit `alt`, dekorative mit `alt=""`.
- Eine `<h1>` pro Seite, das ist der Hero-Titel.
- `:focus-visible` mit deutlich sichtbarem Rahmen.
- Navigation mit Tastatur bedienbar, Mobilmenü mit Escape schliessbar.
- Beige `#A0886D` auf Hell `#F5F3ED` erreicht den Mindestkontrast nicht — nur für Flächen und Illustrationen, nie für Fliesstext.
- `prefers-reduced-motion` beachten.

---

## 9. Technik und Deploy

- GitHub Pages, Domain über Hostpoint.
- `.nojekyll` im Wurzelverzeichnis.
- `sitemap.xml` und `robots.txt` nur mit den zehn Seiten, die online gehen.
- Pro Seite `<title>`, `<meta name="description">`, Open-Graph-Bild.
- `lang="de-CH"`.

---

## 10. Offen vor dem Livegang

1. **ALT-Texte** fehlen für alle Bilder.
2. **`authentizitaet-01`** fehlt als Datei, Platz ist hoch 406 × 489.
3. **`hero-ueber.mp4`** wiegt 47 MB. Auf 3 bis 5 MB bringen, plus Standbild als Poster. Bis dahin auf Über das Standbild statt des Videos.
4. **Referenzen** laufen unter echten Namen. Einverständnis der drei einholen.
