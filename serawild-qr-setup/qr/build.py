#!/usr/bin/env python3
"""
Baut aus qr/qr-codes.json:
  1. den Weiterleitungs-Block in .htaccess (zwischen den Markern, idempotent)
  2. je einen QR-Code als PNG (Web/Vorschau) und SVG (Druck) in qr/out/

Aufruf:  python3 qr/build.py
Voraussetzung:  pip install "qrcode[pil]"
"""

import json
import pathlib
import sys

import qrcode

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONFIG = ROOT / "qr" / "qr-codes.json"
OUTDIR = ROOT / "qr" / "out"
HTACCESS = ROOT / ".htaccess"

START = "# === QR-WEITERLEITUNGEN START (generiert von qr/build.py – nicht von Hand bearbeiten) ==="
END = "# === QR-WEITERLEITUNGEN ENDE ==="

EC = {
    "L": qrcode.constants.ERROR_CORRECT_L,
    "M": qrcode.constants.ERROR_CORRECT_M,
    "Q": qrcode.constants.ERROR_CORRECT_Q,
    "H": qrcode.constants.ERROR_CORRECT_H,
}


def lade_config():
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    slugs = [c["slug"] for c in cfg["codes"]]
    doppelt = {s for s in slugs if slugs.count(s) > 1}
    if doppelt:
        sys.exit(f"FEHLER: doppelte slugs in qr-codes.json: {', '.join(sorted(doppelt))}")
    for c in cfg["codes"]:
        if not c["ziel"].startswith("/"):
            sys.exit(f"FEHLER: ziel von '{c['slug']}' muss mit / beginnen: {c['ziel']}")
    return cfg


def ziel_mit_utm(code):
    """Hängt die UTM-Parameter ans Ziel, respektiert ein evtl. vorhandenes ?."""
    trenner = "&" if "?" in code["ziel"] else "?"
    return (
        f"{code['ziel']}{trenner}"
        f"utm_source={code['slug']}"
        f"&utm_medium=qr"
        f"&utm_campaign={code['kampagne']}"
    )


def baue_htaccess(cfg):
    zeilen = [
        START,
        "RewriteEngine On",
        "RewriteBase /",
        "",
    ]
    for code in cfg["codes"]:
        zeilen.append(f"# {code['slug']}: {code.get('notiz', '')}".rstrip())
        # R=302 (temporär) ist Absicht: 301 wird von Browsern und Scannern dauerhaft
        # gecacht – ein späterer Zielwechsel käme bei diesen Geräten nie an.
        zeilen.append(
            f"RewriteRule ^go/{code['slug']}/?$ {ziel_mit_utm(code)} [R=302,L,NE]"
        )
        zeilen.append("")

    zeilen += [
        "# Unbekannter oder vertippter Code -> Startseite statt 404",
        "RewriteRule ^go/.*$ / [R=302,L]",
        "",
        END,
    ]
    block = "\n".join(zeilen)

    alt = HTACCESS.read_text(encoding="utf-8") if HTACCESS.exists() else ""
    if START in alt and END in alt:
        vorher = alt.split(START)[0]
        nachher = alt.split(END, 1)[1]
        neu = vorher + block + nachher
    else:
        neu = (alt.rstrip() + "\n\n" if alt.strip() else "") + block + "\n"

    HTACCESS.write_text(neu, encoding="utf-8")
    print(f"  .htaccess aktualisiert ({len(cfg['codes'])} Weiterleitungen)")


def als_svg(matrix, fg, bg, rand=4, modul=10):
    """Schreibt die QR-Matrix als SVG – scharf in jeder Grösse, ideal für Druck."""
    n = len(matrix)
    gesamt = (n + 2 * rand) * modul
    pfad = []
    for y, reihe in enumerate(matrix):
        for x, dunkel in enumerate(reihe):
            if dunkel:
                px = (x + rand) * modul
                py = (y + rand) * modul
                pfad.append(f"M{px} {py}h{modul}v{modul}h-{modul}z")
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {gesamt} {gesamt}" '
        f'width="{gesamt}" height="{gesamt}" shape-rendering="crispEdges">'
        f'<rect width="{gesamt}" height="{gesamt}" fill="{bg}"/>'
        f'<path fill="{fg}" d="{"".join(pfad)}"/>'
        f"</svg>"
    )


def baue_codes(cfg):
    OUTDIR.mkdir(parents=True, exist_ok=True)
    fg = cfg["farben"]["vordergrund"]
    bg = cfg["farben"]["hintergrund"]
    ec = EC[cfg.get("fehlerkorrektur", "Q").upper()]

    for code in cfg["codes"]:
        url = f"{cfg['base_url']}/go/{code['slug']}"

        qr = qrcode.QRCode(error_correction=ec, box_size=16, border=4)
        qr.add_data(url)
        qr.make(fit=True)

        png = OUTDIR / f"qr-{code['slug']}.png"
        qr.make_image(fill_color=fg, back_color=bg).save(png)

        svg = OUTDIR / f"qr-{code['slug']}.svg"
        svg.write_text(als_svg(qr.get_matrix(), fg, bg), encoding="utf-8")

        print(f"  {code['slug']:<16} {url}  ->  {code['ziel']}")


if __name__ == "__main__":
    cfg = lade_config()
    print("QR-Codes bauen ...")
    baue_codes(cfg)
    print("Weiterleitungen schreiben ...")
    baue_htaccess(cfg)
    print("\nFertig. Dateien in qr/out/, Regeln in .htaccess.")
