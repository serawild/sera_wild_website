# QR-Codes für serawild.com

Aktualisierbare QR-Codes mit Scan-Zählung – ohne Abo, ohne Drittanbieter, ohne Cookie-Banner.

## Die Idee in einem Satz

Der gedruckte Code zeigt nie direkt auf die Zielseite, sondern immer auf `serawild.com/go/<name>`.
Was hinter `/go/<name>` passiert, steht in der `.htaccess` – und die kannst du jederzeit ändern,
ohne dass ein einziger gedruckter Flyer wertlos wird.

## Dateien

```
qr/qr-codes.json     <- hier änderst du alles
qr/build.py          <- erzeugt QR-Codes + die .htaccess-Regeln
qr/scan-report.py    <- wertet die Hostpoint-Logs aus
qr/out/              <- fertige QR-Codes (PNG + SVG)
.htaccess            <- der generierte Block, kommt auf Hostpoint
```

## Einmalig einrichten

```bash
pip install "qrcode[pil]"
python3 qr/build.py
```

Dann die `.htaccess` auf Hostpoint bringen – entweder über deinen bestehenden Deploy-Weg
oder von Hand im Control Panel unter **Websites → serawild.com → Document Root**.

Danach im Browser testen: `https://www.serawild.com/go/flyer` muss auf der Zielseite landen.

## Neuen QR-Code anlegen

In `qr/qr-codes.json` einen Eintrag ergänzen:

```json
{
  "slug": "plakat-bahnhof",
  "ziel": "/w-erlaebnis/",
  "kampagne": "plakat-herbst-2026",
  "notiz": "A2-Plakat, Bahnhof Aarau, ab September"
}
```

Dann `python3 qr/build.py`, `.htaccess` hochladen, `qr/out/qr-plakat-bahnhof.svg` in die Druckdatei.

## Ziel eines gedruckten Codes ändern

Nur das Feld `ziel` anpassen, `python3 qr/build.py`, `.htaccess` hochladen. Fertig –
die gedruckten Codes zeigen ab sofort woanders hin.

## Scans auswerten

1. Logs holen: admin.hostpoint.ch → Websites → serawild.com → **Logs** → Tab **Domlogs** → herunterladen
2. Dateien nach `qr/logs/` legen
3. `python3 qr/scan-report.py qr/logs/ --monat`

Ausgabe:

```
Code                 Scans   ca. Geräte   aktive Tage
-----------------------------------------------------
flyer                    5            1             1
visitenkarte             2            1             1
```

Bots (Googlebot, WhatsApp-Vorschau, Uptime-Checker) werden herausgefiltert – sonst zählst du
Linkvorschauen als echte Scans.

Weil an jedes Ziel automatisch UTM-Parameter angehängt werden, tauchen die Scans später auch
sauber getrennt in Plausible oder Matomo auf, falls du das mal ergänzt. Du musst dich jetzt
nicht entscheiden.

## Drei Dinge, die man leicht falsch macht

**302 statt 301.** Die Regeln nutzen bewusst `R=302`. Ein 301 wird von Browsern und
QR-Apps dauerhaft gecacht – wenn du später das Ziel änderst, kommt die Änderung bei genau den
Leuten nie an, die den Code schon einmal gescannt haben. Nicht auf 301 umstellen.

**Die `.htaccess` verschwindet beim Deploy.** Dateien mit Punkt am Anfang werden von vielen
Deploy-Tools und `rsync`-Aufrufen stillschweigend ignoriert. Nach dem ersten Deploy einmal
prüfen, ob sie wirklich auf dem Server liegt.

**Slug nie wiederverwenden.** Wenn `flyer` mal ausgedient hat: Eintrag im JSON stehen lassen und
das Ziel auf die Startseite legen. Löschst du ihn, laufen alte gedruckte Flyer in die
Fallback-Regel – und du weisst nicht mehr, woher die Aufrufe kamen.

## Für den Druck

Nimm die **SVG**-Datei, nicht das PNG. SVG ist vektorbasiert und bleibt in jeder Grösse scharf.
Faustregel für die Grösse: Scanabstand geteilt durch 10. Visitenkarte (ca. 25 cm Abstand)
→ mindestens 2,5 cm Kante. Plakat aus 3 m Distanz → mindestens 30 cm.

Die Codes sind in deinen Markenfarben (`#2F322D` auf `#F5F3ED`, Kontrast 11,7:1) – deutlich über
dem, was Scanner brauchen. Wenn du die Farben je änderst: dunkel auf hell, nie umgekehrt, und
mindestens 3:1 Kontrast.
