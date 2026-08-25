# Prompt für Claude Code — Seite «Event-Reportage» bauen

Alles ab der Linie kopieren. Der gestaltete Entwurf liegt als PDF vor; dieser Text enthält alle Inhalte, du brauchst das PDF nicht.

---

Bau eine neue Seite `src/pages/reportage.astro`, erreichbar unter `/reportage`.

## Wofür sie da ist

Eine Landingpage für Firmenkunden und Private, die eine Reportage für einen Anlass suchen. Sie wird **nicht** ins Kopfmenü aufgenommen. Man kommt über einen QR-Code auf einem gedruckten Angebot dorthin und über einen Verweis auf der Kontaktseite.

**Ansprache: Sie.** Das ist der einzige Ort auf der Website, an dem gesiezt wird — Firmenkunden erwarten es. Nicht mischen.

**Logo:** die Fassung ohne Untertitel, also `src/assets/Logos/Secondary/SVG/Secondary White.svg` beziehungsweise `Secondary Dark.svg`. Nicht das Primärlogo mit «prozessorientierte Fotografie».

## Aufbau

Gleiche Bausteine, Farben, Schriftskala und Abstände wie der Rest der Website. `src/pages/kontakt.astro` ist der Massstab. Mobil nach den Regeln aus `spec/mobil.json`.

### Hero — Hintergrund Oliv, vollflächiges Bild mit dunklem Schleier

Platzhalter `hero-reportage`, vollflächig, darüber ein Schleier `rgba(47,50,45,0.42)`. Logo hell oben links. Text unten links.

- Überzeile: `EVENT-REPORTAGE`
- Titel: «Ich fotografiere, was passiert.» / «Nicht, was gestellt ist.» — der Umbruch steht so
- Untertitel: «Reportagen für Firmenanlässe und private Feste — im Aareland und weit darüber hinaus.»
- Knopf: «Anfrage senden» → `/kontakt`

### 01 Wer fotografiert — Hintergrund Creme

Links Platzhalter `seraina-portrait` im Verhältnis 3 : 4, rechts der Text.

- Kapitelmarke: `01 — WER FOTOGRAFIERT`
- Titel: «Seraina Wild»
- Hervorgehoben: «Zehn Jahre Fotografie, vier Jahre Eventmanagement — und ein echtes Interesse an Menschen.»
- «Ich fotografiere seit zehn Jahren: draussen, an Anlässen und im klassischen Studio. Vier Jahre davon habe ich selber Events organisiert. Ich weiss deshalb, wie so ein Abend von innen aussieht — wo es eng wird, wann der Moment kommt und wann man besser einen Schritt zurücktritt.»
- «Dazu habe ich aus Interesse ein Diplom in Individualpsychologie gemacht. Nicht um zu therapieren, sondern um Menschen besser zu verstehen. Das sieht man den Bildern an.»

### 02 Arbeitsweise — Hintergrund Dunkel

Kapitelmarke `02 — ARBEITSWEISE`, Titel «Ich bin da, aber ich stehe nicht im Weg.», darunter drei gleich hohe Karten in Oliv nebeneinander, mobil untereinander.

- **Unauffällig** — «Ich arbeite so lange wie möglich mit dem Licht, das da ist. Kein Blitzgewitter, keine Kommandos, keine unterbrochenen Gespräche.»
- **Vorbereitet** — «Vier Jahre Eventmanagement haben mir beigebracht, wie so ein Abend von innen aussieht. Ich weiss, wann der Moment kommt.»
- **Nah bei den Leuten** — «Gruppenbilder gehören dazu. Aber die Bilder, die bleiben, entstehen dazwischen.»

### 03 Bildstrecke — Hintergrund Creme, wischbar

Kapitelmarke `03 — EIN BLICK`, Titel «Aus vergangenen Anlässen», Text «Wischbare Bildstrecke. Die Auswahl folgt, sobald du die Bilder freigegeben hast.» — **dieser Satz ist ein Hinweis an Seraina und muss vor dem Livegang ersetzt werden. Trag ihn in `OFFEN.md` ein.**

Fünf Platzhalter `reportage-galerie-01` bis `-05`, 300 × 380 auf dem Rechner, 260 × 340 mobil, darunter Wischpunkte. Gleicher Baustein wie die bestehenden Wischleisten.

### 04 Angebot — Hintergrund Oliv

Kapitelmarke `04 — ANGEBOT`, Titel «Was enthalten ist». Zweispaltig: links die Leistungen als Liste mit feinen Trennlinien darüber, rechts zwei Kästen untereinander. Mobil alles untereinander.

Leistungen, je Titel und Beschrieb:

1. **Vorgespräch** — «Ablauf, Räume, Lichtverhältnisse — und die Menschen, die auf keinem Bild fehlen dürfen.»
2. **Reportage vor Ort** — «So lange wie vereinbart. Ich bin früh da und kenne den Ablauf, bevor er beginnt.»
3. **Auswahl und Bearbeitung** — «Licht, Farbe und Ausschnitt bei jedem einzelnen Bild. Keine Filter von der Stange.»
4. **Webgalerie in voller Auflösung** — «Passwortgeschützt, teilbar. Ihre Gäste laden ihre Bilder selber herunter.»
5. **Nutzungsrechte** — «Für Ihre Kommunikation — intern wie extern, zeitlich unbegrenzt.»
6. **Lieferung** — «In der Regel innert zwei Wochen. Einzelne Bilder für die Kommunikation auch früher.»

Kasten oben, Hintergrund Creme, Titel «Die Webgalerie»:

- «Alle Bilder in voller Auflösung, hinter einem Passwort. Sie erhalten einen Link, den Sie weitergeben können — an Gäste, an die Geschäftsleitung, an die Agentur.»
- «Jede Person lädt sich selber herunter, was sie braucht. Kein Versand von Ordnern, keine geschrumpften Bilder in E-Mails.»

Kasten unten, Hintergrund Terracotta: «Jeder Anlass ist anders. Sagen Sie mir Datum, Ort und Dauer — Sie bekommen eine Offerte, in der alles steht.»

**Es stehen keine Preise auf dieser Seite.** Nicht ergänzen.

### 05 Anlässe — Hintergrund Creme

Kapitelmarke `05 — ANLÄSSE`, Titel «Wofür ich gebucht werde». Darunter sechs Schlagworte als Umrandungen in Sand, umbrechend: Firmenjubiläen · Mitarbeiteranlässe · Kongresse und Tagungen · Preisverleihungen · Eröffnungen · Generalversammlungen.

Darunter, abgesetzt mit einer 3 px breiten Linie in Rostorange links: «Und privat? Hochzeiten, runde Geburtstage, Taufen, Familienfeste. Dieselbe Haltung, derselbe Ablauf — nur mit mehr Umarmungen.»

### 06 Ablauf — Hintergrund Dunkel

Kapitelmarke `06 — ABLAUF`, Titel «Von der Anfrage bis zur Galerie». Vier Schritte nebeneinander, mobil untereinander, je mit einem Kreis in Terracotta und der Nummer darin — derselbe Baustein wie auf der Kontaktseite.

1. **Anfrage** — «Datum, Ort, Dauer, Anlass. Ein paar Zeilen genügen.»
2. **Offerte** — «Sie bekommen ein schriftliches Angebot, in dem alles steht. Keine Positionen, die später dazukommen.»
3. **Reportage** — «Ich bin vor Ort, bevor es losgeht.»
4. **Galerie** — «Passwortgeschützt, in voller Auflösung, zum Weitergeben.»

### Zitat — Hintergrund Terracotta, mittig

«Die besten Bilder entstehen, wenn jemand kurz vergisst, dass ich da bin.»

### 07 Kontakt — Hintergrund Creme

Links der Text, rechts Platzhalter `reportage-kontakt` im Verhältnis 4 : 5.

- Kapitelmarke `07 — KONTAKT`
- Titel: «Erzählen Sie mir von Ihrem Anlass.»
- «Datum, Ort, ungefähre Dauer und worum es geht. Ich melde mich innert zwei Arbeitstagen mit einer Offerte.»
- «Wenn Sie lieber reden: rufen Sie an. Ein Anlass lässt sich in fünf Minuten besser klären als in fünf E-Mails.»
- Knopf «Anfrage senden» → `/kontakt`
- Darunter Telefon und E-Mail als Links

### Footer

Der bestehende Footer.

## Verlinkung

- **Nicht** ins Menü in `Navigation.astro` aufnehmen — weder auf dem Rechner noch im mobilen Menü.
- Auf `src/pages/kontakt.astro` im Abschnitt «Event-Reportage»: Der Knopf «ANFRAGE SCHICKEN» führt heute ins Leere. Er zeigt neu auf `/reportage`, und die Beschriftung wird zu «MEHR ZUR REPORTAGE».
- In `src/pages/sitemap.xml.ts` als Eintrag mit Priorität `0.7` ergänzen. Die Seite soll gefunden werden, sie steht nur nicht im Menü.
- Die feste Leiste am unteren Rand bleibt auf dieser Seite sichtbar. Kein Punkt ist aktiv.

## Bilder

Sechs neue Einträge in `spec/bilder.json` anlegen: `hero-reportage`, `reportage-galerie-01` bis `-05`, `reportage-kontakt`. Feld `aktiv` auf `false`, `datei` leer lassen, im Feld `alt` einen Platzhaltertext mit dem Hinweis, dass er noch geschrieben werden muss. `seraina-portrait` existiert bereits und wird wiederverwendet.

Solange die Dateien fehlen: Rechteck in Beige `#A0886D` in der richtigen Grösse mit dem Namen als Beschriftung, wie du es bei den mobilen Seiten machst. In `OFFEN.md` eintragen.

## Titel und Beschreibung

- Titel: `Event-Reportage — sera Wild`
- Beschreibung: `Reportagen für Firmenanlässe und private Feste. Unaufdringlich fotografiert, geliefert in einer passwortgeschützten Webgalerie in voller Auflösung.`

## Zum Schluss

Prüf die Seite auf dem Rechner und bei 390 px. Melde, was du gebaut hast und was in `OFFEN.md` gelandet ist.
