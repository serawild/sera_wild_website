#!/usr/bin/env python3
"""
Wertet die Hostpoint-Domlogs aus und zeigt, wie oft welcher QR-Code gescannt wurde.

Logs holen:  admin.hostpoint.ch -> Websites -> serawild.com -> Logs -> Tab "Domlogs"
             herunterladen und z.B. nach qr/logs/ legen.

Aufruf:  python3 qr/scan-report.py qr/logs/*.log
         python3 qr/scan-report.py qr/logs/          (ganzer Ordner, auch .gz)
         python3 qr/scan-report.py qr/logs/ --monat  (Aufschlüsselung pro Monat)

Ohne Zusatzpakete – reine Standardbibliothek.
"""

import collections
import gzip
import pathlib
import re
import sys

# Apache Combined Log Format
ZEILE = re.compile(
    r'^(?P<ip>\S+) \S+ \S+ \[(?P<zeit>[^\]]+)\] '
    r'"(?P<methode>\S+) (?P<pfad>\S+)[^"]*" '
    r'(?P<status>\d{3}) \S+ "(?P<referrer>[^"]*)" "(?P<ua>[^"]*)"'
)

GO = re.compile(r'^/go/([A-Za-z0-9_-]+)/?(?:\?.*)?$')

# Was eindeutig kein Mensch mit Handykamera ist
BOT = re.compile(
    r'bot|crawl|spider|slurp|preview|fetch|monitor|scan(?!ner-app)|curl|wget|'
    r'python-requests|headless|lighthouse|pingdom|uptime|facebookexternalhit|'
    r'whatsapp|telegram|slackbot|twitterbot|linkedinbot|discord|embedly',
    re.I,
)

MONATE = {
    "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
    "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12",
}


def dateien(argumente):
    gefunden = []
    for arg in argumente:
        p = pathlib.Path(arg)
        if p.is_dir():
            gefunden += sorted(x for x in p.iterdir() if x.is_file())
        elif p.is_file():
            gefunden.append(p)
    return gefunden


def zeilen(pfad):
    oeffnen = gzip.open if pfad.suffix == ".gz" else open
    try:
        with oeffnen(pfad, "rt", encoding="utf-8", errors="replace") as f:
            yield from f
    except OSError as e:
        print(f"  (übersprungen: {pfad.name} – {e})", file=sys.stderr)


def datum(zeitstempel):
    """'14/Aug/2026:09:12:33 +0200' -> ('2026-08-14', '2026-08')"""
    tag, monat, rest = zeitstempel.split("/", 2)
    jahr = rest[:4]
    return f"{jahr}-{MONATE.get(monat, '00')}-{tag}", f"{jahr}-{MONATE.get(monat, '00')}"


def main():
    argumente = [a for a in sys.argv[1:] if not a.startswith("--")]
    pro_monat = "--monat" in sys.argv

    if not argumente:
        sys.exit(__doc__)

    scans = collections.Counter()
    geraete = collections.defaultdict(set)
    monate = collections.defaultdict(collections.Counter)
    bots = 0
    tage = collections.defaultdict(set)

    gefunden = dateien(argumente)
    if not gefunden:
        sys.exit("Keine Logdateien gefunden.")

    for pfad in gefunden:
        for zeile in zeilen(pfad):
            m = ZEILE.match(zeile)
            if not m:
                continue
            treffer = GO.match(m.group("pfad"))
            if not treffer:
                continue
            if BOT.search(m.group("ua")):
                bots += 1
                continue

            slug = treffer.group(1)
            tag, monat = datum(m.group("zeit"))

            scans[slug] += 1
            # grobe Näherung für "unterschiedliche Geräte": IP + Browserkennung pro Tag
            geraete[slug].add((m.group("ip"), m.group("ua"), tag))
            monate[slug][monat] += 1
            tage[slug].add(tag)

    if not scans:
        print("Keine /go/-Aufrufe in den Logs gefunden.")
        print("Prüfen: richtige Logdatei? Weiterleitung schon live? Schon jemand gescannt?")
        return

    print(f"\nAusgewertet: {len(gefunden)} Datei(en), {bots} Bot-Aufrufe herausgefiltert\n")
    print(f"{'Code':<18}{'Scans':>8}{'ca. Geräte':>13}{'aktive Tage':>14}")
    print("-" * 53)
    for slug, anzahl in scans.most_common():
        print(f"{slug:<18}{anzahl:>8}{len(geraete[slug]):>13}{len(tage[slug]):>14}")
    print("-" * 53)
    print(f"{'Total':<18}{sum(scans.values()):>8}")

    if pro_monat:
        print("\nPro Monat:")
        for slug, _ in scans.most_common():
            reihe = "  ".join(f"{m}: {n}" for m, n in sorted(monate[slug].items()))
            print(f"  {slug:<18}{reihe}")

    print(
        "\nHinweis: 'ca. Geräte' ist eine Schätzung (IP + Browserkennung pro Tag). "
        "Mobilfunk teilt IPs, darum eher Unter- als Obergrenze."
    )


if __name__ == "__main__":
    main()
