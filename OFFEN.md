# Offene Punkte

## Texte «Nur du. In echt.» (2026-10-06) im Code, Figma noch nachführen

Die Texte stammen aus `PROMPT-texte-nur-du-in-echt.md`, von Seraina am
06.10.2026 freigegeben — **nicht** aus Figma. Für diese Stellen ist Figma
veraltet; Regel 2 in `CLAUDE.md` ist hier bewusst ausgesetzt. Figma später
nachziehen, sonst überschreibt der nächste Abgleich die neuen Texte.

Betroffene Abschnitte:

| Seite | Abschnitt | Node-ID |
|---|---|---|
| w-erlaebnis | Hero, Untertitel unter der Wortmarke | `2253:604` |
| w-erlaebnis | Begegnung — H2 und drei Absätze | `2253:422` |
| w-erlaebnis | **neu** «Das Ziel», zwischen «Das W» und «Wonach wir suchen» | — |
| w-erlaebnis | Angebot — **neuer** Kasten «Was ist dir ein Wochenende wert?» | `2253:444` |
| w-erlaebnis | «Du bist hier richtig wenn,» — Abschlusssatz | `2253:430` |
| index | Hero — **neue** Unterzeile unter der Headline | `2251:342` |
| index | Haltung — Satz am Ende von `haltungText` | — |
| index | Geschichten gespiegelt — H2 und Absatz | `2310:971` |
| index | Meta-Beschreibung | — |
| ueber | Mein Weg — **neuer** Absatz `meinWegP2` | `2246:273` |
| index · ueber · w-netzwerk · bausteine | Kontakt-Teaser: «zu sich zurückfinden» | — |

**Hero W-Erläbnis: alte Zeilen behalten (Entscheid Seraina, 06.10.2026).** Der
neue Untertitel «Nur du. In echt. / Kein Studio, keine Posen. Du an einem Ort,
den du liebst, bei dem, was dich ausmacht.» war mit 85 Zeichen zu lang für die
56-px-Schrift — drei Zeilen über fast die ganze Bildbreite. Im Hero stehen
darum weiter «Wenn du weisst, wer du bist, / kannst du sein, wer du willst.»
Die Haltung «Nur du. In echt.» trägt die Startseite im Hero und der Abschnitt
Begegnung auf W-Erläbnis. Beim Nachführen in Figma diese Zeile **nicht**
ändern.

**«Das Ziel» ohne Illustration:** Der neue Abschnitt verwendet den Baustein des
Zitat-Abschnitts, aber ohne Deko. Die Positionen der Illustrationen stehen in
`deko.json` und sind für diesen Abschnitt noch nicht erfasst — die Regel lautet,
nicht zu raten.

## Geschichten-Seite: Umbau am 06.10.2026

Drei Blöcke gestrichen, weil sie fast wortgleich auf der Startseite stehen:
«Du musst nicht jemand anderes sein» (Authentizität), «Veränderung beginnt dort»
(Angebot) und der Kontakt-Teaser. Telefon und Mail stehen im Footer, die Seite
verliert also keinen Kontaktweg.

Neu stehen die drei Geschichten als Karten mit Porträt, Name und einem Satz —
direkt nach der Foto-Story, vor der Kundenstory. Bild ist jeweils
`*-geschichte-oben` (alle 0.76 : 1), zugeschnitten auf 3 : 4.

**Von Seraina gegenlesen — die drei Sätze sind abgeleitet, nicht aus Figma:**
Grundlage ist jeweils `geschichteObenP1` der eigenen Unterseite.

- Tina: «Sie begegnet dem Wandel des Lebens mit Mut und ihrem inneren Kompass.»
  (aus ihrem Zitat, aus der Ich- in die Sie-Form gebracht)
- Sara: «Ihr Geschäft wächst. Sie wollte Bilder, die nach ihr aussehen statt nach Katalog.»
- Simona: «Sie baut ihr eigenes Business auf — und wollte sich zeigen, wie sie wirklich ist.»

## Schreibweise des Namens — entschieden am 06.10.2026

**Marke: `sera Wild`** — klein geschriebenes «sera», grosses «Wild», genau wie im
Logo. Auch am Satzanfang. In Versalien-Knöpfen wird daraus durch CSS automatisch
«ÜBER SERA WILD»; im Quelltext steht trotzdem `Über sera Wild`.

**Person: `Seraina Wild`** — nie «Seraina Stettler».

Beides ist überall nachgezogen: 199 Stellen `sera Wild`, 20 Stellen
`Seraina Wild`, kein `Sera Wild`, kein `SERAWILD`, kein `Stettler` mehr im
gebauten Stand. Bei neuen Texten immer so schreiben.

## Reportage-Seite (/reportage)

Seite: reportage.astro — vor dem Livegang zu erledigen:

**Umbau am 06.10.2026:** Bildstrecke und Anlässe sind zu einem Abschnitt
«04 — Was ich fotografiere» verschmolzen, mit einer Collage aus neun Bildern
statt fünf. Die Collage steht neu hinter dem Angebot: 03 ist das Angebot, 04 die
Collage, danach 05 Ablauf und 06 Kontakt. Der Hinweissatz «Die Auswahl folgt, sobald die Bilder
freigegeben sind.» ist damit weg und muss nicht mehr ersetzt werden.

- **hero-reportage** – Bild fehlt. Platzhalter Beige. Datei und ALT-Text in bilder.json eintragen, aktiv auf true setzen.
- **reportage-galerie-01 bis -09** – Alle neun Bilder fehlen (Collage in Sektion 04).
  Drei davon quer, sechs hoch — die Zuordnung steht im Feld `hinweis` je Eintrag:

  | Reihe | links | Mitte | rechts |
  |---|---|---|---|
  | 1 | **-01 quer** | -02 hoch | -03 hoch |
  | 2 | -04 hoch | -05 hoch | **-06 quer** |
  | 3 | -07 hoch | **-08 quer** | -09 hoch |

  Querbilder 3:2, mindestens 1320 × 880. Hochbilder 2:3, mindestens 600 × 900.
  Beschnitten wird nichts — jedes Bild bekommt den Platz, der seinem Verhältnis
  entspricht. Liegt ein Bild in einem anderen Verhältnis vor, stimmt die Reihe
  trotzdem, nur wird sie etwas höher oder flacher.
- **reportage-kontakt** – Bild fehlt (Sektion 06, rechts). Verhältnis 4:5. Datei und ALT-Text in bilder.json eintragen, aktiv auf true setzen.
- **Logo Secondary** – Hero und Seite sollen die Fassung ohne Untertitel («Secondary White.svg» / «Secondary Dark.svg») verwenden. Derzeit zeigt Navigation das Primärlogo. Entweder Navigation einen optionalen Logo-Prop geben oder für diese Seite eine eigene Kopfzeile ohne Navigation.astro bauen.

## Werbung für Kundinnen auf den Geschichten-Seiten

Der Abschnitt ganz unten mit dem Textverweis auf die Website der Kundin
(«Sara berät Frauen zu ihrer Gesundheit — baravital.ch») wurde am 2026-10-03
aus allen Geschichten-Seiten entfernt — sara.astro, tina.astro, _emanuela.astro.

Seraina will das anders lösen: **mit Logo oder mit einem eigenen Bild**,
nicht als Textzeile. Gestaltung noch offen.

Betroffen waren:
- Sara → baravital.ch
- Emanuela → instagram.com/alagna.art
- Tina → https://www.youtube.com/@tinamariameier (YouTube-Kanal, kein klassischer Webauftritt)


## Veraltete Handy-Fassungen der Heros (Stand 2026-10-03)

Die Querformate wurden am 3.10. erneuert, die zugehörigen `-hoch`-Dateien nicht.
Am Rechner erscheint das neue Motiv, auf dem Handy noch das alte.

- **hero-sara-hoch.jpg** – Stand 10:10, das Querformat wurde um 11:14 gewechselt.
- **hero-simona-hoch.jpg** – Stand 25.08., ausserdem mit 989 × 1572 zu klein
  (nötig wären mindestens ~1700 Pixel Breite).

Zielformat jeweils 0.63 : 1, also z. B. **2268 × 3600**. Praktisch passt alles
zwischen 0.55 und 0.65. Ablage: `src/assets/images/Hero_Bilder/`.

hero-startseite-hoch.jpg ist erledigt (2700 × 3600, bewusst so belassen).


## Fehlende -hoch-Dateien (Mobile Bilder)

Seite: index.astro — Abschnitt: 01 Haltung
- **ueber-mich-01** – kein dateiMobil vorhanden. Normale Datei (3:4, bereits Hochformat) mit object-fit cover verwendet. Soll-Verhältnis mobil: 3:4 (224×298).
- **ueber-mich-02** – kein dateiMobil vorhanden. Normale Datei (3:4, bereits Hochformat) mit object-fit cover verwendet. Soll-Verhältnis mobil: 3:4 (160×214).

Seite: index.astro — Abschnitt: 03 Arbeiten (Galerie)
- **galerie-geschichten-01** – kein dateiMobil vorhanden. Normale Datei (4:5) mit object-fit cover auf 260×340 (≈3:4) beschnitten.
- **galerie-geschichten-02** – kein dateiMobil vorhanden. Wie oben.
- **galerie-geschichten-03** – kein dateiMobil vorhanden. Wie oben.
- **galerie-geschichten-04** – kein dateiMobil vorhanden. Wie oben.
- **galerie-geschichten-05** – kein dateiMobil vorhanden. Wie oben.

Seite: index.astro — Abschnitt: 04 Stimmen (Referenzen)
- **referenz-simona** – kein dateiMobil vorhanden. Quadratbild mit object-fit cover auf 50×50 rund beschnitten. Kein Informationsverlust.
- **referenz-ivor** – kein dateiMobil vorhanden. Wie oben.
- **referenz-beatrice** – kein dateiMobil vorhanden. Wie oben.
- **referenz-patricia** – kein dateiMobil vorhanden. Wie oben. ALT-Text in bilder.json fehlt noch.

Seite: w-erlaebnis.astro — Abschnitt: 01 Begegnung
- **begegnung-01** – kein dateiMobil vorhanden. Normale Datei (4:5 Portrait) mit object-fit cover auf 214×286 (3:4) beschnitten.
- **begegnung-02** – kein dateiMobil vorhanden. Normale Datei (4:5 Portrait) mit object-fit cover auf 178×238 (3:4) beschnitten.

Seite: w-erlaebnis.astro — Abschnitt: 06 Orte (Wischleiste)
- **orte-aare** – kein dateiMobil vorhanden. Normale Datei (3:2 Querformat) mit object-fit cover auf 260×180 (13:9 Querformat) beschnitten. Minimaler Ausschnittsverlust.
- **orte-wald** – kein dateiMobil vorhanden. Wie orte-aare.
- **orte-stadt** – kein dateiMobil vorhanden. Wie orte-aare.
- **orte-atelier** – kein dateiMobil vorhanden. Wie orte-aare.
- **orte-scheune** – kein dateiMobil vorhanden. Wie orte-aare.

Seite: w-erlaebnis.astro — Abschnitt: 07 Richtig
- **richtig-01** – kein dateiMobil vorhanden. Normale Datei (3:4 Portrait) mit object-fit cover auf 214×286 (3:4) beschnitten. Verhältnis identisch, kein Informationsverlust.
- **richtig-02** – kein dateiMobil vorhanden. Normale Datei (3:4 Portrait) mit object-fit cover auf 178×238 (3:4) beschnitten. Wie richtig-01.

Seite: scheune.astro — Abschnitt: 02 Kulissen (Wischleiste)
- **kulissen-01** – kein dateiMobil vorhanden. Normale Datei (3:4 Portrait, 300×400) mit object-fit cover auf 260×340 (3:4) beschnitten. Verhältnis identisch, kein Informationsverlust.
- **kulissen-02** – kein dateiMobil vorhanden. Normale Datei (3:4 Portrait, 240×320) mit object-fit cover auf 260×340 (3:4) beschnitten. Wie kulissen-01.
- **kulissen-03** – kein dateiMobil vorhanden. Normale Datei (13:17 Portrait, 260×340) mit object-fit cover auf 260×340 beschnitten. Verhältnis identisch, kein Informationsverlust.

Seite: geschichten.astro — Abschnitt: 01 Foto-Story (Wischleiste)
- **geschichten-fotostory-01** – kein dateiMobil vorhanden. Normale Datei (4:5, 0.89:1) mit object-fit cover auf 260×340 (3:4) beschnitten.
- **geschichten-fotostory-03** – kein dateiMobil vorhanden. Normale Datei (0.92:1, nahezu quadratisch) mit object-fit cover auf 260×340 (3:4) beschnitten. Merklicher Verlust oben/unten.

Seite: geschichten.astro — Abschnitt: 02 Authentizität (Bildgruppe)
- **authentizitaet-01** – kein dateiMobil vorhanden. Normale Datei (4:5, 0.83:1) mit object-fit cover auf 214×286 (3:4) beschnitten.
- **authentizitaet-02** – kein dateiMobil vorhanden. Normale Datei (0.76:1 ≈ 3:4) mit object-fit cover auf 178×238 beschnitten. Minimaler Verlust.

Seite: geschichten.astro — Abschnitt: 04 Kundenstory (Wischleiste)
- **kundenstory-01** – kein dateiMobil vorhanden. Normale Datei (0.75:1 ≈ 3:4) mit object-fit cover auf 260×340 (3:4) beschnitten. Minimaler Verlust.

Seite: geschichten/simona.astro — Abschnitt: 02 Foto-Story (Wischleiste)
- **simona-fotostory-01** – kein dateiMobil vorhanden. Normale Datei (4:5, 0.89:1) mit object-fit cover auf 260×340 (3:4) beschnitten.
- **simona-fotostory-03** – kein dateiMobil vorhanden. Normale Datei (0.92:1) mit object-fit cover auf 260×340 beschnitten.

Seite: geschichten/simona.astro — Abschnitt: 03 Was geblieben ist (Bildgruppe)
- **simona-geschichte-unten-01** – kein dateiMobil vorhanden. Normale Datei (0.70:1) mit object-fit cover auf 214×286 (3:4) beschnitten. Seitenränder abgeschnitten.
- **simona-geschichte-unten-02** – kein dateiMobil vorhanden. Normale Datei (13:19, 0.68:1) mit object-fit cover auf 178×238 (3:4) beschnitten.

Seite: geschichten/simona.astro — Abschnitt: 04 Collage (Wischleiste)
- **simona-collage-01…14** – kein dateiMobil vorhanden. Normale Dateien (3:4) mit object-fit cover auf 220×290 beschnitten. Verhältnis identisch, kein Informationsverlust.

Seite: ueber.astro — Abschnitt: 02 Mein Weg
- **ueber-geschichte** – kein dateiMobil vorhanden. Normale Datei (0.76:1 ≈ 3:4) mit object-fit cover auf 342×456 (3:4) beschnitten. Minimaler Verlust.

Seite: ueber.astro — Abschnitt: 03 Meine Aufgabe (Bildgruppe)
- **ueber-geschichte-unten-01** – kein dateiMobil vorhanden. Normale Datei (0.70:1) mit object-fit cover auf 214×286 (3:4) beschnitten. Seitenränder abgeschnitten.
- **ueber-geschichte-unten-02** – kein dateiMobil vorhanden. Normale Datei (13:19, 0.68:1) mit object-fit cover auf 178×238 (3:4) beschnitten.

Seite: scheune.astro — Abschnitt: 04 Neugier (Bildgruppe)
- **neugier-01** – kein dateiMobil vorhanden. Normale Datei (4:5 Portrait, 406×508) mit object-fit cover auf 214×286 (3:4) beschnitten. Seitenränder leicht abgeschnitten.
- **neugier-02** – kein dateiMobil vorhanden. Normale Datei (0.76:1 Portrait, 320×420) mit object-fit cover auf 178×238 (3:4) beschnitten. Minimaler Verlust.

## Illustrationen: bewusste Abweichungen von Figma / deko.json

Von Seraina am 07.09.2026 direkt so gewünscht. `spec/deko.json` gibt weiterhin den
Figma-Stand wieder — bei einem Abgleich mit Figma diese drei nicht zurücksetzen.

Seite: w-erlaebnis.astro — Abschnitt: Zitat (`deko[3]`)
- **tulpe** – war Hellgrün, rechts, cssRotate −22.1. Jetzt **Hellorange**, **links**,
  cssRotate **+22.1** (Drehung im Uhrzeigersinn). Position gespiegelt, abstand unverändert −62.

Seite: w-erlaebnis.astro — Abschnitt: CTA Banner (`deko[6]`)
- **mohn** – war Hellgrün. Jetzt **Hellorange**. Position und Drehung unverändert.

Seite: geschichten/simona.astro — Abschnitt: Geschichte Oben (`deko[0]`)
- **tulpe** – war Hellgrün, `top` +80 (ganz im Abschnitt). Jetzt **Beige bei 50 % Deckkraft**
  («Hellbeige» — die Palette kennt keinen eigenen Wert dafür, 0.5 ist die Deckkraft aller
  mobilen Illustrationen) und `top` **−80**, ragt also in den Hero darüber. Bewusst gegen
  die Regel «Illustrationen liegen nie über Text oder Bild» — sie liegt über dem Hero-Bild,
  nicht über Text.

## Netzwerk-Seite: Partner-Logos (Stand 07.09.2026)

Erste Logos liegen in `public/logo-partner/`. Freigestellte Fassungen mit Alpha in
`public/logo-partner/aufbereitet/`. Die Originale bleiben unangetastet.

Von Seraina am 07.09.2026 entschieden:
- **AHA ist die Betreiberin der Aeschbachhalle** — also derselbe Eintrag, kein
  sechster Partner. `AHA-Logo_claim_schwarz-neu.png` gehört zu
  `netzwerk-aeschbachhalle`. Damit sind alle fünf Partner mit Logo versorgt:
  Studio Benanti, Baravital, Esmeralda Cosmetics, Aeschbachhalle (AHA), Fotostudio Fokus.
- **Die Seite wird gebaut, aber noch nicht verlinkt.** Nicht in die Navigation,
  nicht in `sitemap.xml.ts`. Regel 6 in CLAUDE.md und `spec/SPEC.md` bleibt vorerst
  unverändert stehen — diese Notiz hier ist die dokumentierte Ausnahme. Erst wenn
  Seraina die Seite freigibt, wird Regel 6 angepasst und die Seite verlinkt.

Offene Punkte:
- **Fotostudio Fokus: Wortmarke am 07.09.2026 nachgeliefert**
  (`fotostudio-fokus-wortmarke.png`). Sie ist mit 357×50 px sehr klein — auf
  Retina reicht das nur bis rund 178 px Anzeigebreite. Wenn die Vorlage das Logo
  breiter zeigt, braucht es eine grössere Fassung oder ein SVG. Die alte reine
  Bildmarke (Auge, 393×393) liegt weiterhin als `fotostudio-fokus-bildmarke.png`.
- **Studio Benanti: gewählt wurde `studio-benanti-logo-3.jpeg`** (Wortmarke
  «STUDIO BENANTI»), weil sie als einzige den Namen zeigt und hell genug ist.
  Die Dateien 1 und 2 sind schwarz auf schwarzem JPEG-Grund — praktisch unbrauchbar.
  Datei 4 ist die reine Bildmarke «B», als Alternative ebenfalls freigestellt.
  Alle vier haben keinen Alphakanal; der schwarze Grund wurde über die Helligkeit
  herausgerechnet.
- **Die Seite selbst gibt es nicht.** Kein `spec/seiten/netzwerk.json`, keine
  Figma-Node-ID in CLAUDE.md. Regel 6 sagt bislang: Netzwerk geht nicht online.
  Bevor gebaut wird, muss der Figma-Rahmen 10_Netzwerk ausgelesen werden.

## Netzwerk-Seite: Figma ausgelesen (07.09.2026)

Rahmen `10_Netzwerk` = Node **2289:770** auf *Desktop | Designs*. Baustein-Vorlage:
`Sektion – Netzwerk-Eintrag` = **2287:150** auf *03 Sections*. Vollständig ausgelesen
nach `spec/seiten/netzwerk.json`.

**Die Vorlage ist gestalterisch fertig, inhaltlich aber nicht.** Was fehlt:

- **Fünf «Beschrieb»-Texte.** In Figma steht bei allen fünf Partnern derselbe
  Blindtext: «Kurzer Beschrieb – was dieses Unternehmen macht und wofür es steht.
  Zwei bis drei Sätze reichen.»
- **Fünf «Geschichte»-Texte.** Ebenfalls überall derselbe Blindtext: «Hier steht,
  wie ihr euch begegnet seid. Genau das macht diese Seite aus – nicht die Liste,
  sondern die Geschichte dahinter.»
- **Fünf Partnerfotos à 700×500.** In Figma leere Rahmen in Beige #A0886D. Das sind
  die Einträge `netzwerk-*` in `bilder.json` (aktiv: false). Achtung: Das ist
  **nicht** der Logo-Platz — jeder Eintrag hat zusätzlich einen eigenen Logo-Rahmen
  von 200×76. Die Logos sind da, die Fotos fehlen.
- **ALT-Texte** für die fünf Fotos und die fünf Logos.
- **Keine mobile Vorlage.** Auf *Mobile | Designs* gibt es keinen Netzwerk-Rahmen.

Echt und übernehmbar sind: Titel und Intro, die fünf Partnernamen, die fünf Links,
das Label «WIE WIR UNS KENNENGELERNT HABEN», der Einladungs-Abschnitt und der
Kontakt-Teaser.

Die Fokus-Wortmarke (357×50) ist für den Logo-Rahmen von 200×76 **ausreichend** —
rund 1,8-fache Auflösung. Die Sorge von vorhin hat sich damit weitgehend erledigt.

## Netzwerk-Seite gebaut (07.09.2026) — bewusste Ableitungen

Datei `src/pages/w-netzwerk.astro`, Baustein
`src/components/blocks/NetzwerkEintrag.astro`. Baut fehlerfrei, 13 Seiten.

**Die Seite ist bewusst nicht erreichbar:** nicht in der Navigation, nicht in
`sitemap.xml.ts`, `noindex={true}` im Base-Layout. Im Build geprüft.

Wo die Vorlage keine Antwort gab und ich abgeleitet habe:

- **Logo-Rahmen.** Figma zeigt pro Eintrag einen weissen Kasten 200×76 als
  Platzhalter. Da die echten Logos freigestellt sind, entfällt der weisse Kasten;
  das Logo wird linksbündig in dieselben Maximalmasse eingepasst (`object-contain`,
  `object-left`). Wenn der weisse Kasten Absicht war, muss das zurückgebaut werden.
- **ALT-Texte der Logos** stehen auf `alt=""`. Begründung: Der Firmenname steht als
  Überschrift direkt daneben — dieselbe Logik, nach der in `bilder.json` die
  Referenzbilder behandelt werden. Wenn du eigene ALT-Texte willst, sag Bescheid.
- **Illustrationen hängen am Abschnitt darunter**, mit negativem `top`. In Figma
  stehen sie mit absoluter y-Position im 6593 px hohen Rahmen und laufen über
  Abschnittsgrenzen. Umgerechnet: Mohn an Studio Benanti (`top -251`), Tulpe an die
  Einladung (`top -183`). Eukalyptus (`top 65`) und Blattzweig (`top 636`) liegen
  ganz im Kontakt-Teaser. Das ist dasselbe Muster wie in `ueber.astro` und
  `geschichten.astro` — sonst überdeckt der spätere Abschnitt die Illustration.
- **Der Blattzweig ragt in Figma 86 px in den Footer.** Der Kontakt-Teaser steht auf
  `overflow-visible`, der Footer liegt aber später im DOM und deckt ihn dort ab.
  Praktisch wird der Zweig also an der Footer-Kante abgeschnitten.
- **Mobile Fassung komplett abgeleitet**, es gibt keine Figma-Vorlage. Gebaut nach
  den Mustern aus `spec/mobil.json`: 390 px Bezugsbreite, Seitenrand 24, helle
  Abschnitte `py-12`, dunkle `py-[52px]`, Zähler-Chip «01 — NETZWERK» wie auf den
  anderen Seiten. Partnerbild volle Breite im Verhältnis 7:5, Text darunter.
- **Hero.** Figma zeigt 1117 px feste Höhe. Gebaut wie alle anderen Unterseiten mit
  `h-[100svh] min-h-[600px]`, Titel rechtsbündig 160 px über der Unterkante. Die
  Bildmarke W sitzt mit 477×341 bei 18 % Deckkraft hinter dem Titel, von unten
  verankert, damit sie bei jeder Fensterhöhe gleich zum Titel steht.
- **`hero-netzwerk` in `bilder.json` aktiviert**: `aktiv: true`, `dateiMobil` auf
  `hero-netzwerk-hoch.jpg` gesetzt (die Datei war da, nur nicht eingetragen),
  ALT-Text ergänzt.
- **Logo-Dateien umgeräumt.** Die aufbereiteten Fassungen liegen flach in
  `public/logo-partner/` und werden ausgeliefert. Die Originale liegen jetzt in
  `logos-original/` ausserhalb von `public/` und gehen nicht mit ins Web.

## Netzwerk-Seite: Korrekturen nach Sichtung durch Seraina (07.09.2026)

**1. Keine Platzhalterflächen mehr.** Die Partnerfotos gibt es noch nicht. Statt der
beigen Rechtecke aus Figma rücken jetzt Logo und Name in die Bildspalte, der Text
bleibt daneben — die Reihen wirken damit fertig statt leer. Die Bildseite wechselt
weiterhin ab. Sobald ein Foto in `spec/seiten/netzwerk.json` unter `foto` eingetragen
ist, greift automatisch wieder das Figma-Layout mit Bild 700×500 daneben. Der Code
dafür steht unverändert in `NetzwerkEintrag.astro`, es muss nichts zurückgebaut werden.
Die Seite ist dadurch von 6349 px auf 5118 px Höhe geschrumpft.

**2. Illustrationsbreiten waren falsch umgerechnet.** Ich hatte Figmas *gedrehten*
Begrenzungsrahmen als Elementbreite übergeben. `DekoIllustration` und `deko.json`
erwarten aber die Breite **vor** der Drehung — deshalb lag der Mohn viel zu gross
über dem Intro-Text. Richtige Umrechnung:

    breite = BBoxBreite / (cos θ + a · sin θ),   a = SVG-Höhe / SVG-Breite

    Mohn        409 → 248     Tulpe       466 → 252
    Eukalyptus  350 → 211     Blattzweig  306 → 170

Gegenprobe über die Höhe stimmt bei allen vier auf unter 1 px mit Figma überein.
Wer künftig Deko aus der Figma-API übernimmt, muss dieselbe Umrechnung machen —
`absoluteBoundingBox` ist nie direkt als `breite` verwendbar.

**3. Zwei Illustrationen zusätzlich verschoben** (bewusste Abweichung von Figma):
- **Mohn** `abstand` −178 → **−278**. Auch nach der Breitenkorrektur streifte er die
  erste Zeile des Intro-Textes. Jetzt rund 30 px Abstand zur Textkante, die Regel
  «nie hinter Text, mindestens 16 px» ist damit eingehalten.
- **Blattzweig** `top` 636 → **300**, `abstand` −63 → **−210**. Der Kontakt-Teaser ist
  im Code rund 690 px hoch, in Figma 910. Bei `top 636` wurde der Zweig mitten im
  Abschnitt abgeschnitten und sah aus wie ein Fehler. Jetzt liegt er ganz im
  Abschnitt und läuft sauber über den rechten Seitenrand hinaus.

## Netzwerk-Seite: auf vier Partner reduziert (08.09.2026)

Vorgabe von Seraina: vorerst nur **Baravital, Studio Benanti, Esmeralda Cosmetics
und AHA**. Fotostudio Fokus fällt raus.

**1. Fotostudio Fokus zurückgestellt, nicht gelöscht.** Der Eintrag steht weiterhin
in `spec/seiten/netzwerk.json`, jetzt mit `aktiv: false`. `w-netzwerk.astro` filtert
auf `aktiv !== false`. Wieder aufnehmen heisst: ein Feld umstellen. Auch das Logo
bleibt unter `public/logo-partner/`.

**2. Reihenfolge neu**, von Seraina festgelegt: Baravital, Studio Benanti,
Esmeralda Cosmetics, Aeschbachhalle Aarau. Die Bildseite wechselt weiterhin ab und
wird jetzt aus der Position berechnet, nicht mehr fest in der JSON gepflegt.

**3. Einladungs-Banner in die Mitte.** In Figma stand es zwischen Eintrag 3 und 4 —
bei fünf Partnern sinnvoll, bei vier nicht. Jetzt nach Eintrag 2, also 2 + 2. Der
Wert steht als `einladungNachEintrag` in der JSON, damit er nicht im Code vergraben ist.

**4. Der Mohn hängt neu am ersten Eintrag** (vorher fest an Studio Benanti). Er soll
ins Intro hinaufragen — das hängt an der Position, nicht am Partner.

**5. Partnerfotos vorbereitet.** Seraina will pro Partner ein Bild. Die vier Einträge
`netzwerk-*` in `bilder.json` haben jetzt Pfad und Masse: `Galerie_3-2/<id>.jpg`,
700 × 500, Verhältnis 7 : 5.

Wichtig: `foto` wird in `w-netzwerk.astro` nur durchgereicht, **wenn die Datei
wirklich im Ordner liegt** (Prüfung über `import.meta.glob`). Solange sie fehlt,
greift weiter das Logo-Layout aus der Sichtung vom 07.09. — keine beigen Kästen.
Sobald ein Foto abgelegt wird, erscheint es von selbst. Es ist nichts umzustellen.

**Noch offen:** die acht Texte. `beschrieb` und `geschichte` sind bei allen vier
Partnern weiterhin Blindtexte aus Figma. Solange sie drinstehen, geht die Seite
nicht online — `noindex` bleibt, keine Verlinkung, nicht in der Sitemap.

## Netzwerk-Seite: Texte da (08.09.2026)

Alle acht Blindtexte der vier aktiven Partner sind ersetzt. Grundlage: Angaben von
Seraina im Gespräch, ergänzt um die Selbstdarstellung der jeweiligen Website
(baravital.ch, esmeraldacosmetics.com, aha.ag). Von Seraina Satz für Satz freigegeben.

Nur noch Blindtext hat der zurückgestellte Eintrag Fotostudio Fokus — er wird nicht
gerendert, also unkritisch. Bevor er je wieder aktiviert wird, braucht er eigene Texte.

**Offen bleibt:**

- **Die vier Partnerfotos.** `netzwerk-<id>.jpg` in `src/assets/images/Galerie_3-2/`,
  quer 7 : 5 (700 × 500). Fehlen sie, greift das Logo-Layout — die Seite ist auch
  ohne sie vorzeigbar.
- **Esmeralda hat als einzige keine Ansprechperson im Text.** Bei den anderen drei
  steht eine Person, hier «das Team». Falls ein Name dazukommt, wird der Eintrag
  runder.
- **Das Label «WIE WIR UNS KENNENGELERNT HABEN» passt beim AHA-Eintrag nicht** — dort
  steht keine Begegnung, sondern Serainas eigene Rolle im Team. Der Text löst das
  im ersten Satz auf («Hier ist es anders als bei den anderen»). Ein eigenes Label
  pro Eintrag wäre die sauberere Lösung, ist aber noch nicht gebaut.
- **Aufschalten** ist noch nicht entschieden: `noindex` steht, die Seite ist nicht
  in `Navigation.astro`, nicht in `sitemap.xml.ts`.

## Saras Geschichte: Bilder und ALT-Texte da (03.10.2026)

Alle 22 Dateien liegen in den vorgesehenen Ordnern, Namen stimmen. Die 21 Einträge
`hero-sara`, `sara-geschichte-oben`, `sara-fotostory-01` bis `-03`,
`sara-geschichte-unten-01`/`-02` und `sara-collage-01` bis `-14` in `spec/bilder.json`
sind aktiv, haben einen ALT-Text und keinen Platzhalter-Hinweis mehr.

Die ALT-Texte sind nach Sichtung jedes einzelnen Bildes geschrieben, im selben Muster
wie bei Simona: Vorname, was zu sehen ist, keine Deutung.

**Zu prüfen:** Bei `sara-collage-12` hält Sara ein kleines orangefarbenes Objekt, das
ich nicht sicher benennen kann. Der ALT-Text sagt deshalb nur «ein kleines
orangefarbenes Modell». Wenn Seraina weiss, was es ist, gehört der richtige Name hinein.

**Noch offen:** Build und Sichtung durch Seraina, Saras Freigabe für die Textfassung,
danach die Entscheidung über das Aufschalten (`noindex`, Navigation, Sitemap).

## Saras Geschichte: nach Serainas Bildtausch (03.10.2026)

Drei Bilder ausgetauscht: `hero-sara` (neues Motiv, Sara zwischen zwei Stämmen,
Blick nach oben), `sara-geschichte-unten-01` (Waldweg mit Tennisball) und
`sara-collage-02` (das frühere Hero-Querbild). ALT-Texte der ersten beiden
nachgezogen, beim dritten passte der bestehende.

Die erste Collage-Reihe ist neu schmal–breit–schmal–schmal. `verhaeltnis` und
`ausrichtung` von `sara-collage-01` bis `-04` in `bilder.json` entsprechend
korrigiert — sie standen noch auf 3 : 4 aus dem alten Raster.

**Von Seraina bewusst so belassen, nicht vergessen:**

- `sara-geschichte-unten-01` und `-02` zeigen dasselbe Motiv (grüne Jacke,
  Tennisball, Waldweg) und stehen im Layout nebeneinander.
- Beim neuen Hero steht Sara mittig. Der Titel liegt mobil unten links und könnte
  auf ihr liegen — bei 390 px prüfen. Falls nötig: Text verschieben oder den
  Schleier an der Stelle vertiefen.

## Kulissen auf W-Momänt: fehlende Bilder (06.10.2026)

Die Kulissenbilder lagen seit dem 3. Oktober nur lokal und waren nie
committet — live war darum pro Kulisse nur das jeweils erste Bild sichtbar.
Jetzt alle vorhandenen Dateien im Repo. Es fehlen noch:

Seite: w-momaent.astro — Abschnitt: 02 Kulissen (Durchklicken)
- **licht** – nur `licht-01.jpg` (hoch 2:3). Es fehlen `licht-02.jpg`
  (**quer 3:2**, mind. 704 × 470) und `licht-03.jpg` (**hoch 4:5**, mind.
  480 × 600). Solange zeigt die Kulisse ein einzelnes grosses Bild statt der
  Dreier-Collage. Hinweis: `licht-01.jpg` ist Hochformat — sobald zwei weitere
  dazukommen, landet es im Querformat-Platz und wird stark beschnitten. Dann
  besser ein echtes Querbild als `-01` nehmen und das heutige nach `-03` rücken.
- **leinen** – `leinen-01.jpg` und `-02.jpg` vorhanden (beide hoch). Es fehlt
  `leinen-03.jpg`; bis dahin die Zweier-Anordnung ohne Beschnitt.
- **vintage** und **stein** sind vollständig (01 quer, 02 + 03 hoch). Bei
  `vintage-03` und `stein-03` liegt 2:3 statt 4:5 im 4:5-Platz — leichter
  Beschnitt oben/unten, bewusst so.

Die Datei `Scheune-16.jpg` (identisches Motiv wie `licht-01.jpg`, nur anderer
Export) lag im Kulissenordner und wurde nach
`~/sera-bilder-originale/kulissen-unbenutzt/` verschoben. `licht-03.jpg` liegt
ebenfalls dort — Hochformat 2:3, passt nicht in den 4:5-Platz, darum nicht
eingesetzt.

## Kontakt-Teaser: neues Motiv, mobile Fassung fehlt (06.10.2026)

`kontakt-teaser-01.jpg` und `-02.jpg` zeigen seit dem 3. Oktober ein neues
Motiv (olivgrünes Spitzenkleid am Fluss, Abendsonne). ALT-Texte, `dateiMasse`
und `deckungsfaktor` in `bilder.json` nachgezogen.

Die passenden Hochformat-Ausschnitte lagen unter anderem Namen und im falschen
Ordner: `Galerie_2-3/kontakt-teaser-hoch-01.jpg` und `-02.jpg` statt
`Galerie_3-2/kontakt-teaser-01-hoch.jpg` und `-02-hoch.jpg`. Sie sind jetzt
umbenannt und einsortiert, beide 2:3 (665 × 1000 bzw. 667 × 1000). Die alten
`-hoch`-Dateien vom 25. August zeigten noch das frühere Motiv (Jeansjacke am
Hafen) und liegen zur Sicherheit in
`~/sera-bilder-originale/kontakt-teaser-altes-motiv/`.

**Von Seraina prüfen lassen — Zuordnung nach Motiv, nicht nach Nummer:**
Ihre Nummerierung und die Motive passten nicht zusammen. Zugeordnet wurde nach
Bildinhalt, damit die ALT-Texte stimmen:

- `kontakt-teaser-01` (lachende Nahaufnahme) ← ihre Datei `kontakt-teaser-hoch-02.jpg`
- `kontakt-teaser-02` (am Ufer, abgewandt) ← ihre Datei `kontakt-teaser-hoch-01.jpg`

Soll es doch nach ihrer Nummerierung gehen, sind es zwei vertauschte Dateinamen.

Die Bilder sind 2:3, der mobile Platz ist 3:4 — beschnitten wird oben und unten,
seitlich geht nichts verloren. Betrifft Startseite, Geschichten und Über.

## Netzwerk-Seite: Fotostudio Fokus wieder drin (06.10.2026)

Von Seraina entschieden: Fokus kommt wieder auf die Seite. Damit fünf Partner, Fokus an
Position 5, Bild links. Einladungs-Banner bleibt nach Eintrag 2.

- `aktiv: true` in `spec/seiten/netzwerk.json`, Foto-Eintrag in `bilder.json` aktiviert
  mit Pfad `Galerie_3-2/netzwerk-fotostudio-fokus.jpg`.
- Die zwei Texte (`beschrieb`, `geschichte`) sind inzwischen da, ebenso Logo und Foto.
  Der Figma-Blindtext steht nur noch als Rückfalltext in `netzwerk.json` und wird von
  keinem der fünf Einträge verwendet.
- Hinweis: Laut fotostudio-fokus.ch ist Seraina selbst im Team. Wie bei AHA passt das
  Label «WIE WIR UNS KENNENGELERNT HABEN» dann nur bedingt.

## Netzwerk-Seite: Partnerfotos da (06.10.2026)

Vier von fünf Fotos liegen in `Galerie_3-2/`: Studio Benanti, Baravital, Esmeralda,
Fotostudio Fokus. Je 2400 × 1600 (3 : 2). Der Rahmen ist 7 : 5 — `object-fit: cover`
schneidet links und rechts je rund 3 % weg. ALT-Texte in `bilder.json` eingetragen,
Platzhalter-Hinweise entfernt.

- `netzwerk-aeschbachhalle.jpg` am 06.10.2026 nachgeliefert, ALT-Text eingetragen. Alle fünf Fotos da.
- ALT-Texte Benanti und Baravital: Von Seraina bestätigt, dass Simona bzw. Sara
  abgebildet sind — Namen ergänzt. Bildformat 3 : 2 mit leichtem Beschnitt freigegeben.

## Netzwerk-Seite: Texte gekürzt (06.10.2026)

Vorgabe von Seraina: möglichst wenig Text, je zwei Sätze. Alle fünf Partner neu in
`spec/seiten/netzwerk.json` — Beschrieb und Geschichte je zwei Sätze. Fokus hat damit
eigene Texte, kein Blindtext mehr auf der Seite. Von Seraina freigegeben.

**Noch offen:** nur noch der Entscheid Aufschalten (noindex, Navigation, Sitemap).
- 06.10.2026: Label erledigt. `NetzwerkEintrag` nimmt optional `label`; AHA und Fokus
  zeigen «WAS MICH MIT DIESEM ORT VERBINDET».

## Netzwerk-Seite online (06.10.2026)

Von Seraina freigegeben. `noindex` entfernt, `/w-netzwerk` in `sitemap.xml.ts`, in der
Navigation als Unterpunkt von «Sera Wild» (neben «Über mich» → `/ueber`). Regel 6 in
CLAUDE.md angepasst — gesperrt bleibt nur noch Emanuela.

**Zu prüfen beim nächsten Build:** «Sera Wild» hatte bisher kein Untermenü, jetzt schon —
Desktop-Dropdown und mobiles Menü einmal durchklicken. Die Bezeichnung «Über mich» ist
abgeleitet, nicht aus Figma.
