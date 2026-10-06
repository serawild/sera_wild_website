# Neuen Partner auf der Netzwerk-Seite aufnehmen

Seite: `src/pages/w-netzwerk.astro` · Baustein: `src/components/blocks/NetzwerkEintrag.astro`
Alle Inhalte stehen in `spec/seiten/netzwerk.json` → Abschnitt `partner` → `eintraege`.
**Im Code ist nichts anzupassen** — nur JSON, Logo und Foto.

## Was Seraina liefert

1. **Name** des Partners und **Link** (Website oder Instagram).
2. **Logo** — in den Chat oder in den Ordner. Möglichst PNG, freigestellt.
3. **Foto** — quer, 3 : 2 oder 7 : 5, mindestens 1050 × 750 px (ideal 2400 × 1600).
4. **Stichworte**: Was macht der Partner? Wie habt ihr euch kennengelernt bzw. was
   verbindet dich?

## Was Claude daraus macht

### 1. Texte vorschlagen — und erst nach Freigabe eintragen
- **Beschrieb:** genau **zwei Sätze**. Was der Partner macht, wofür er steht.
- **Geschichte:** genau **zwei Sätze**. Ich-Form, Seraina erzählt. Warm, nicht
  sentimental, keine Werbesprache («Herzblut» statt «hohes Engagement»).
- Seraina will **möglichst wenig Text**. Lieber kürzen als ergänzen.
- Eigene Ergänzungen von Claude als solche kennzeichnen und nachfragen.
- Nichts eintragen, bevor Seraina die Texte freigegeben hat.

### 2. Logo ablegen
- Original nach `logos-original/` (geht nicht ins Web).
- Freigestellte Fassung (transparenter Hintergrund) nach `public/logo-partner/<kurzname>.png`.
- Erst prüfen, ob das Logo schon da ist (gleiche Grösse/gleicher Inhalt).

### 3. Foto ablegen
- Datei: `src/assets/images/Galerie_3-2/netzwerk-<kurzname>.jpg` — Name ist verbindlich.
- Eintrag in `spec/bilder.json` nach dem Muster der bestehenden `netzwerk-*`-Einträge:
  `figmaEbene`, `baustein: "Netzwerk-Eintrag"`, `seite: "Netzwerk"`, Anzeige 700 × 500,
  `verhaeltnis: "7 : 5"`, `aktiv: true`, `datei` mit dem Pfad oben.
- **ALT-Text** nach Sichtung des Bildes schreiben: was zu sehen ist, keine Deutung.
  Person mit Vornamen nennen, aber nur, wenn Seraina bestätigt, wer abgebildet ist.
- Fehlt das Foto, zeigt die Seite automatisch Logo und Name statt Bild. Kein Platzhalter.

### 4. Eintrag in `spec/seiten/netzwerk.json`
In `eintraege` ein Objekt nach diesem Muster ergänzen:

```json
{
  "id": "netzwerk-<kurzname>",
  "name": "Anzeigename",
  "link": "DOMAIN.CH",
  "linkZiel": "https://domain.ch",
  "logo": "/logo-partner/<kurzname>.png",
  "foto": "netzwerk-<kurzname>",
  "beschrieb": "Zwei Sätze.",
  "geschichte": "Zwei Sätze.",
  "platzhalter": false,
  "aktiv": true
}
```

- **Reihenfolge** = Reihenfolge im Array. Seraina fragen, wo der Partner hin soll.
  Bildseite links/rechts wechselt automatisch.
- **Einladungs-Banner** steht nach Eintrag Nr. `einladungNachEintrag` (zurzeit 2).
- **Label:** Standard ist «WIE WIR UNS KENNENGELERNT HABEN». Wenn Seraina dort selbst
  arbeitet oder gearbeitet hat (wie AHA, Fotostudio Fokus):
  `"label": "WAS MICH MIT DIESEM ORT VERBINDET"`.
- Partner vorübergehend ausblenden: `"aktiv": false` (nicht löschen).

### 5. Festhalten und prüfen
- Kurzen Eintrag in `OFFEN.md` (Datum, was dazukam, was offen ist).
- Build laufen lassen, Seite auf Rechner und Handy anschauen.
- Seite ist online — eine Änderung geht mit dem nächsten Deploy live.

## Stand 06.10.2026
Fünf Partner: Studio Benanti · Baravital · *Einladung* · Esmeralda Cosmetics ·
Aeschbachhalle Aarau · Fotostudio Fokus. Alle mit Text, Logo und Foto.
