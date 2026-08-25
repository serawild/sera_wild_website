# Prompt für Claude Code — Scheune wird zu W-Momänt

Alles ab der Linie kopieren.

---

Das kleine Angebot bekommt einen Namen: **W-Momänt**. Es gehört damit sichtbar zur selben Familie wie das W-Erläbnis, und die Grösse steckt schon in den Wörtern.

**Die wichtigste Unterscheidung:** Umbenannt wird das **Angebot**, nicht der **Ort**. Die Scheune ist ein echtes Gebäude in Gretzenbach und heisst weiterhin Scheune. Sätze wie «in einer alten Scheune, vier Kulissen, viel Holz» oder die Ortskarte «Die Scheune» auf dem W-Erläbnis bleiben, wie sie sind. Nur dort, wo «Scheune» oder «Shooting in der Scheune» als **Name des Angebots** steht, wird daraus W-Momänt.

## 1. Datei und Adresse

- `src/pages/scheune.astro` wird zu `src/pages/w-momaent.astro`. Die Adresse ist damit `/w-momaent` — ohne Umlaut, wie bei `w-erlaebnis`.
- In `astro.config.mjs` eine Weiterleitung ergänzen, damit bestehende Links und gedruckte Verweise nicht ins Leere laufen:

```js
redirects: {
  '/scheune': '/w-momaent',
},
```

Die Weiterleitung bleibt dauerhaft bestehen. Nicht später aufräumen.

## 2. Navigation

`src/components/Navigation.astro`:

- Untermenü-Eintrag: Beschriftung `W-Momänt`, Ziel `/w-momaent`
- `matchPaths` des Punkts «Angebot»: `['/w-erlaebnis', '/w-momaent']`

Beide Fassungen — Rechner und mobiles Menü.

## 3. Der Hero auf der Seite selbst

Heute steht dort «Dein Fotoshooting: vier Kulissen, eine Stimmung, ganz du.» Das Wort Fotoshooting soll weg, jetzt wo das Angebot einen Namen hat. Neu dreiteilig, wie auf den anderen Heros:

- Überzeile: `Der erste Schritt` — auf dem Handy in Grossbuchstaben, auf dem Rechner als grosse Zeile in `text-h1`
- Titel: `W-Momänt`
- Untertitel: `Vier Kulissen, eine Stimmung, ganz du.`

Falls der separate Prompt zur Scheune als Türöffner noch nicht umgesetzt ist: Die Überzeile dort ist dieselbe Änderung, also nur einmal machen.

## 4. Verweise auf anderen Seiten

`src/pages/w-erlaebnis.astro`:

- Die beiden Knöpfe «Zum Shooting in der Scheune» (mobil um Zeile 732, Rechner um Zeile 746) heissen neu **«Zum W-Momänt»** und zeigen auf `/w-momaent`.
- `ctaP1`, der Text im CTA-Banner: Der Anfang «Dann fangen wir kleiner an – in einer alten Scheune, vier Kulissen…» bleibt. Die Scheune ist hier der Ort, nicht der Name.
- FAQ, Frage «Wie viel kostet ein Shooting?»: «Das Shooting in der Scheune startet bei CHF 149» wird zu «**Das W-Momänt startet bei CHF 149**».
- FAQ, Frage «Wie viel Zeit sollte ich einplanen?»: «In der Scheune je nach Paket 15 bis 60 Minuten» wird zu «**Beim W-Momänt je nach Paket 15 bis 60 Minuten**».
- FAQ, Frage «Wo findet das Shooting statt?»: «Das Shooting in der Scheune findet in 5014 Gretzenbach statt» wird zu «**Das W-Momänt findet in 5014 Gretzenbach statt**».
- FAQ, Frage «Was passiert bei schlechtem Wetter?»: «In der Scheune sind wir vom Wetter unabhängig» bleibt — hier ist der Ort gemeint.
- Die Ortskarte «Die Scheune» im Abschnitt Orte bleibt unverändert.

`src/pages/kontakt.astro`, um Zeile 336: «Die Scheune-Shootings finden in Gretzenbach statt» wird zu «**Das W-Momänt findet in Gretzenbach statt**». Der Rest des Satzes bleibt.

Such danach im ganzen Projekt nach weiteren Stellen mit `Scheune` oder `/scheune` und melde mir, was du gefunden hast, bevor du dort etwas änderst — bei jeder Stelle muss einzeln entschieden werden, ob Ort oder Angebot gemeint ist.

## 5. Titel, Beschreibung, Sitemap

- Seitentitel: `W-Momänt — sera Wild`
- Beschreibung: `Der erste Schritt: 15 bis 60 Minuten in einer alten Scheune, vier Kulissen, ohne dass du etwas darstellen musst.`
- In `src/pages/sitemap.xml.ts` den Pfad `/scheune` durch `/w-momaent` ersetzen. Die Priorität `0.8` bleibt. Die alte Adresse kommt **nicht** in die Sitemap, sie ist nur eine Weiterleitung.

## 6. Spec-Dateien nachziehen

- `spec/seiten/scheune.json` umbenennen in `spec/seiten/w-momaent.json`, Feld `seite` anpassen.
- `spec/mobil.json`: Der Rahmen heisst weiterhin `M2.1_Scheune`, seine `route` wird `/w-momaent`. Notiere im `hinweis`, dass der Figma-Rahmen noch den alten Namen trägt.
- `spec/SPEC.md` und `CLAUDE.md`: Wo die Seite in Tabellen aufgeführt ist, den neuen Namen und die neue Adresse eintragen.
- In `spec/bilder.json` bleiben die Bild-IDs (`kulissen-01`, `neugier-01` und so weiter) **unverändert**. Nur das Feld `seite` von `Scheune` auf `W-Momänt` setzen.

## Zum Schluss

Bau, ruf `/scheune` auf und prüf, ob die Weiterleitung greift. Prüf die Seite auf dem Rechner und bei 390 px. Melde mir alle Stellen, an denen du «Scheune» stehen gelassen hast, mit kurzer Begründung.
