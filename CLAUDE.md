# CLAUDE.md — sera wild

Projektleitfaden für Claude Code. Diese Datei beschreibt Zweck, Tech-Stack,
Konventionen und Workflows der Website. Bei Unklarheiten oder Abweichungen:
nachfragen, statt raten.

---

## 1. Projektüberblick

- **Was**: Website für **sera Wild** — Einzelfirma für **prozessorientierte
  Fotografie** (Schweiz). Claim laut Branding: „prozessorientierte Fotografie".
- **Charakter**: Portfolio + Journal/Blog. Überwiegend statisch, inhaltsfokussiert.
  Bildstark — Fotografie steht im Zentrum, daher hoher Anspruch an Bildqualität
  und -performance.
- **Ziel**: Arbeiten (Kunden-„Geschichten") präsentieren, über die Firma
  informieren, Kontaktmöglichkeit bieten. Storytelling steht im Zentrum.
- **Zielpublikum**: Potenzielle Kund:innen (D-A-CH + international).

### Sitemap / Informationsarchitektur
Aus Figma (node `55:1467`). Vier Hauptbereiche + Story-Detailseiten. Bestimmt
Navigation und Routing (je unter `/de/…` und `/en/…`):

```
Startseite (serawild.com)
├── Angebot
│     W-Erlebnis · Fotoshooting · FAQs · Ablauf · Stimmen über Workshop
│     · „Du bist die richtige, wenn…" · Kontakt-CTA · passende Story
├── Geschichten                          ← Portfolio-/Story-Übersicht
│     Portfolio · Kundenstimmen
│     └── Einzelne Geschichte            ← Detailseite (Content Collection)
│           Storytelling · Ausgangslage · Herausforderung · Lösung
│           · Verlinkung Kunde
├── Sera Wild (Über)
│     Deine Werte · Mission · Vision · Geschichte · „Was macht dich aus"
│     · Partnerschaften · Stimmen über dich · Verlinkung Kontakt
└── Kontakt
      „Wo bist du zu Hause" · Kontaktdaten · Stimmen · Story-Cross-Link
```

- **Haupt-Navigation** (4 Punkte): Angebot · Geschichten · Sera Wild · Kontakt.
- **Einzige Content Collection**: `geschichten` (die Story-Detailseiten). Angebot,
  Sera Wild und Kontakt sind weitgehend statische Seiten mit festen Abschnitten.
- Wiederkehrende Bausteine: **Stimmen/Testimonials** und **Cross-Links** (Story ↔
  Angebot ↔ Kontakt) tauchen mehrfach auf → als wiederverwendbare Komponenten bauen.

---

## 2. Tech-Stack

| Bereich        | Wahl                                    |
| -------------- | --------------------------------------- |
| Framework      | **Astro** (statische Ausgabe, `output: 'static'`) |
| Sprache        | **TypeScript** (strict)                 |
| Styling        | **Tailwind CSS** (Design-Tokens aus Figma) |
| Inhalte        | **Markdown/MDX** via Astro Content Collections |
| Bilder         | `astro:assets` (automatische Optimierung, WebP/AVIF) |
| i18n           | Astro-i18n-Routing, **Deutsch + Englisch** |
| Formatierung   | **Prettier** (+ `prettier-plugin-astro`, `prettier-plugin-tailwindcss`) |
| Linting/Checks | **ESLint** + `astro check` (TypeScript-Prüfung) |
| Hosting        | **GitHub Pages** via GitHub Actions     |
| Domain         | **serawild.com** (eigene Domain, CNAME) |
| Kontakt        | Nur E-Mail / Social — **kein Formular** |

**Bewusst NICHT im Stack** (weil statisch gehostet): kein SSR, keine
Server-Functions, kein CMS, keine Datenbank. Falls später serverseitige Logik
nötig wird (z.B. echtes Kontaktformular mit eigener Verarbeitung), zuerst
Hosting-Wechsel (Vercel/Netlify) oder externen Dienst besprechen.

---

## 3. Projektstruktur

```
src/
  pages/
    de/            # deutschsprachige Seiten
    en/            # englischsprachige Seiten
  content/
    geschichten/   # Kunden-Geschichten / Story-Detailseiten (Content Collection, MD/MDX)
    config.ts      # Collection-Schemas (zod)
  components/      # Astro-/UI-Komponenten (PascalCase)
  layouts/         # Seiten-Layouts
  styles/          # globale Styles, Tailwind-Base
  i18n/            # Übersetzungs-Strings & Helfer
  assets/          # in den Build importierte Bilder/SVGs
public/            # statische Dateien 1:1 (Favicon, CNAME, robots.txt)
assets/            # QUELL-Brandmaterial (Logos, Fonts, Illustrationen) — NICHT der Build-Ordner
astro.config.mjs
tailwind.config.ts
```

Hinweis: Der bestehende Ordner `assets/` (Grossbuchstaben-Unterordner: `Logos`,
`Markenelement`, `Schriften`) enthält die **Quelldateien** des Brandings. Für die
Website verwendete Assets werden bewusst nach `src/assets/` bzw. `public/`
übernommen (nicht der ganze Ordner ausgeliefert).

---

## 4. Design-System / Brand

Verbindliche Design-Grundlage. Exakte Hex-Werte und Skalen kommen aus Figma
(siehe §5) und werden in `tailwind.config.ts` als Tokens hinterlegt.

### Farben (Markenpalette)
Aus Figma ausgelesen (Datei „SeraWild | Website", File-Key
`L1sORBHNF7ohDq9DXjruRm`; Styleguide-Farbseite node `85:146`). Die Gruppierung
Primary/Secondary/Akzente stammt aus dem Styleguide; die Tailwind-Tokens sind
die semantischen Namen für den Code.

| Gruppe    | Tailwind-Token | Figma-Variable | Hex       | Verwendung                    |
| --------- | -------------- | -------------- | --------- | ----------------------------- |
| Primary   | `dark`         | 1 Dunkelgrün   | `#2F322D` | Text / dunkler Grund          |
| Primary   | `cream`        | 6 Hell         | `#F5F3ED` | heller Grund / Off-White      |
| Secondary | `olive`        | 2 Hellgrün     | `#5B5C4F` | gedämpftes Oliv, Sekundärfläche|
| Secondary | `beige`        | 5 Beage        | `#A0886D` | warmes Beige/Taupe            |
| Akzent    | `rust`         | 3 Rostorange   | `#983515` | Hauptakzent                   |
| Akzent    | `orange`       | 4 Hellorange   | `#BC541F` | Hover / heller Akzent         |
| —         | `white`        | —              | `#FFFFFF` | reines Weiss (keine Variable) |

### Typografie
- **Primär (Headlines/Display)**: **Vollkorn** (Serif, Google Fonts), SemiBold (600)
- **Sekundär (Fliesstext/UI)**: **Roboto** (Sans, Google Fonts), Regular (400)
- Fonts self-hosted einbinden (Performance + DSGVO), nicht via Google-CDN.
- **Skala aus Figma-Styleguide** (Grössen in px, Desktop & Mobile; für Web
  rem-basiert umsetzen, responsiv per `clamp()` oder Breakpoint):

  | Stil               | Font / Style             | Desktop | Mobile | Extra              |
  | ------------------ | ------------------------ | ------- | ------ | ------------------ |
  | H1                 | Vollkorn SemiBold        | 80      | 44*    | *korrigiert (s.u.) |
  | H2                 | Vollkorn SemiBold        | 56      | 40     | —                  |
  | H3                 | Vollkorn SemiBold        | 40      | 28     | —                  |
  | H4                 | Roboto Regular           | 28      | 16     | **unterstrichen**  |
  | CTA                | Roboto Regular           | 28      | 24     | Letter-spacing 6 (Desktop) |
  | Body               | Roboto Regular           | 32      | 20     | Line-height ≈200 % |
  | Body Hervorgehoben | Vollkorn SemiBold Italic | 40      | 40     | Hervorhebung im Fliesstext |
  | Small / Navigation | Roboto Regular           | 24      | 24     | u.a. Navigation    |

  \* Korrektur (mit Seraina bestätigt): Im Figma steht Mobile-H1 = 36px und damit
  kleiner als H2 (40px) — das ist ein Fehler. Im Code muss **H1 grösser als H2**
  sein. Vorschlag: H1 mobile = **44px** (kann angepasst werden). Sobald das
  Figma korrigiert ist, hier den finalen Wert übernehmen.
  Referenz: `assets/Schriften/Typografie.pdf`.

### Spacing (Abstände)
5-stufige Skala aus dem Figma-Styleguide, je Desktop/Mobile. Als Tailwind-
Spacing-Tokens hinterlegen (responsiv umsetzen, z.B. `clamp()` oder `md:`):

| Token | Desktop | Mobile |
| ----- | ------- | ------ |
| `xs`  | 6       | 8      |
| `sm`  | 16      | 20     |
| `md`  | 40      | 40     |
| `lg`  | 80      | 56     |
| `xl`  | 200     | 100    |

(Grosszügige Abstände — v.a. `lg`/`xl` prägen den ruhigen, bildbetonten Look.)

### Logos & Markenelemente
- **Logos**: `assets/Logos/` — Varianten `Bildmarke` (das „W"-Zeichen),
  `Primary` (Wortmarke **mit** Claim „prozessorientierte Fotografie"),
  `Secondary` (Wortmarke ohne Claim), `Icon`. Je in EPS/PNG/SVG und in den
  Farbvarianten (Beige, Dark, Olivengrün, Rostorange, White). Für Web **SVG**;
  auf dunklem Grund die helle Variante verwenden, auf hellem die dunkle.
- **Markenelement**: `assets/Markenelement/` — 4 botanische Line-Art-
  Illustrationen (01–04: Zweig, Tulpe, Eukalyptus, Mohn) in Dark/Rostorange/
  White. Dekorative Akzente, sparsam einsetzen.

### Design-Quelle (Figma)
- Datei „SeraWild | Website", File-Key `L1sORBHNF7ohDq9DXjruRm`.
- Styleguide-Nodes: Farben `85:146`, Logo `85:147`, Bildmarke `85:472`,
  Illustrationen `85:499`, Typo Mobile `85:699` / Desktop `85:532`,
  Spacing Desktop `85:655` / Mobile `85:1075`.
- Sitemap: node `55:1467`.
- Seiten: `Elements` (Komponenten) und `Archiv` (fertige Seiten-Designs:
  Startseite, Angebot/„Experience", Geschichten, Sera Wild/„Simona", Sitemap).

### Verbindliche Design-Grundsätze (von Seraina festgelegt)
Diese Regeln gelten für **jede** Seite/Komponente:

1. **Bilder**: **immer rechteckig** (keine abgerundeten Ecken). Der sichtbare
   **Ausschnitt/Zoom** (object-position/scale) soll dem der Figma-Datei
   entsprechen — Bilder so einzoomen, dass der Crop wie im Design sitzt.
2. **Abschnitts-Abstände**: möglichst **immer gleich** (einheitlicher vertikaler
   Rhythmus, `py-xl`; Token aus §4-Spacing).
3. **Illustrationen** (Markenelemente, in mehreren Farben verfügbar):
   **abwechslungsreich** einsetzen — mal **überlappend** über zwei Abschnitte
   hinweg, mal nicht; **Grösse variieren** (einzoomen), **drehen**, teils nur als
   **Ausschnitt** ins Bild hineinragend, teils **klein als ganze Illustration**.
   Verteilung **unabhängig von Figma** gestalten → Abwechslung + Wiedererkennung.
   **Ausnahme**: die **Header-Illustration der Startseite** exakt wie Figma
   (Rostorange-Zweig von oben rechts hereinragend, Quelle node `13:629`,
   Datei `src/assets/deco-hero.png`).
4. **Buttons**: Farbe darf **variieren**, grundsätzlich in der **Akzentfarbe**
   (`rust`/`orange`); Varianten in `Button.astro`.
5. **Typografie**:
   - **Überschriften & Zitate immer Vollkorn**. Bei jeder neuen Verwendung
     **Seraina fragen**: *kursiv / fett / grösser / standard?*
   - Fliesstext/UI: **Roboto**, Grössen/Stile wie in Figma (§4-Skala).
6. **Nutzerführung**: Der/die Besucher:in soll aktiv **durch die Website geführt**
   werden. **Wichtig**: aktiv darauf hinweisen, wenn Nutzer irgendwo **„hängen
   bleiben"** könnten (Sackgassen, fehlende CTA/Weiterführung, unklarer nächster
   Schritt).
7. **Footer**: **immer identisch** auf allen Seiten. Muss enthalten:
   **Telefonnummer** (mit **WhatsApp-Icon** links daneben, Direktlink
   `https://wa.me/41797905701`) und **E-Mail** (`mailto:info@serawild.com`) —
   beide verlinkt. Umsetzung: `src/components/Footer.astro`.
8. **Favicon**: das dunkle „W" (Bildmarke) — `public/favicon.svg`
   (dunkles W auf Cream-Grund), eingebunden in `Base.astro`.

---

## 5. Figma-Workflow (MCP)

Figma Professional ist via MCP-Server angebunden. Der Design-Prozess ist
**Token-first, dann Komponenten**:

1. **Design-Tokens zuerst**: Farben, Typografie-Skala, Abstände (Spacing),
   Radien, Schatten aus Figma auslesen und in `tailwind.config.ts` als Tokens
   pflegen. Diese Tokens sind die einzige Quelle der Wahrheit — im Code **keine
   Magic Numbers**, sondern Tailwind-Tokens verwenden.
2. **Komponenten Frame für Frame**: Figma-Frames in Astro-Komponenten
   übersetzen, dabei ausschliesslich die definierten Tokens nutzen.
3. **Konsistenz-Check**: Weicht ein Figma-Wert von den Tokens ab, nachfragen —
   nicht stillschweigend einen neuen Wert einführen.

Beim Übernehmen aus Figma: semantische Namen bevorzugen (`bg-beige` statt
Rohwert), Struktur an bestehende Komponenten anlehnen.

---

## 6. Content-Workflow (Geschichten)

- **Geschichten** (Kunden-Stories / Case-Studies) liegen als `.md`/`.mdx` in
  `src/content/geschichten/`. Sie speisen die Übersicht „Geschichten" und die
  Detailseiten „Einzelne Geschichte".
- **Struktur einer Geschichte** (aus der Sitemap): Storytelling, Ausgangslage,
  Herausforderung, Lösung, Verlinkung Kunde. Als Frontmatter-Felder + Fliesstext
  abbilden.
- **Bilder im Content**: colokiert bei der Geschichte ablegen und relativ
  referenzieren (`![Alt](./bild.jpg)`). Optimierung übernimmt `astro:assets`
  automatisch beim Build. Immer **aussagekräftige Alt-Texte** setzen.
- **MDX** nutzen, wenn Komponenten gebraucht werden (Galerie, Vollbreit-Bild,
  Zitat-/Stimmen-Block).
- **Schema**: Frontmatter-Felder in `src/content/config.ts` via zod definieren
  (Titel, Datum, Sprache, Kunde, Cover, Ausgangslage, Herausforderung, Lösung …).
  Fehlende Felder werden beim Build gemeldet.
- **i18n**: Jede Geschichte existiert idealerweise in DE und EN. Sprache über
  Ordner/Frontmatter kennzeichnen; URLs unter `/de/…` und `/en/…`.

---

## 7. Konventionen

- **TypeScript strict**; keine `any` ohne guten Grund.
- **Komponenten**: PascalCase-Dateinamen (`WorkCard.astro`), ein Zweck pro Datei.
- **Styling nur über Tailwind-Tokens** (§4/§5). Kein Inline-CSS mit Rohwerten,
  keine willkürlichen `#hex`-Angaben im Markup.
- **Bilder** immer über `astro:assets` (`<Image />`) statt roher `<img>`, ausser
  bei bewusst statischen Dateien in `public/`.
- **Barrierefreiheit**: semantisches HTML, Alt-Texte, ausreichende Kontraste,
  Fokus-Zustände. Als Design-Firma ist sauberes A11y Teil der Visitenkarte.
- **Commit-Sprache**: Deutsch oder Englisch konsistent; kurze, präzise Messages.
- Vor grösseren Änderungen an Struktur/Stack kurz abstimmen.

---

## 8. Befehle

> Paketmanager: **pnpm** (via `packageManager`-Feld gepinnt, Corepack). Node ≥ 22.13.

```bash
pnpm install        # Abhängigkeiten installieren
pnpm dev            # lokaler Dev-Server (Hot Reload)
pnpm build          # Produktions-Build nach dist/
pnpm preview        # Build lokal ansehen
pnpm check          # astro check (TypeScript/Astro-Diagnostik)
pnpm format         # Prettier über das Projekt
pnpm lint           # ESLint
```

Vor jedem Commit sinnvoll: `pnpm check` + `pnpm format`.

**pnpm-Besonderheiten** (native Pakete):
- `sharp` ist **direkte** Dependency — sonst findet Astro es unter pnpms
  isolierten `node_modules` nicht (Bildoptimierung `astro:assets`).
- Build-Skripte von `esbuild`/`sharp` sind in `pnpm-workspace.yaml` freigegeben
  (`allowBuilds` + `onlyBuiltDependencies`).

---

## 9. Deployment

- **Ziel**: GitHub Pages, automatisiert über **GitHub Actions** (Build bei Push
  auf `main`, Deploy des `dist/`-Ordners).
- **Domain**: eigene Domain `serawild.com`.
  - `public/CNAME` mit Inhalt `serawild.com` anlegen.
  - In `astro.config.mjs`: `site: 'https://serawild.com'` setzen.
  - **Kein `base`-Pfad** nötig (eigene Domain, Root-Deployment).
- HTTPS über GitHub Pages aktivieren.

---

## 10. Kontakt / Formulare

- Kontakt läuft über **E-Mail-Adresse + Social-Links**, kein Formular.
- Kein serverseitiges Handling nötig → passt zum statischen Hosting.
- E-Mail: `info@serawild.com`.

---

## 11. Offene Punkte / TODO

- [x] Markenfarben aus Figma ausgelesen (§4) — noch in `tailwind.config.ts` überführen.
- [x] Typografie-Skala (Desktop+Mobile) aus Figma ausgelesen (§4) — noch in `tailwind.config.ts`.
- [x] Spacing-Skala (Desktop+Mobile) aus Figma ausgelesen (§4) — noch in `tailwind.config.ts`.
- [x] Branche = prozessorientierte Fotografie (bestätigt).
- [x] Mobile H1<H2 als Figma-Fehler bestätigt → H1 mobile grösser als H2 (Vorschlag 44px); Figma noch korrigieren.
- [x] Sitemap / Informationsarchitektur aus Figma erfasst (§1).
- [x] Projekt scaffolden (Astro + Tailwind + MDX, pnpm) + Tokens in `tailwind.config.ts`.
- [x] Vollkorn & Roboto self-hosten (via `@fontsource`, inkl. Vollkorn SemiBold Italic).
- [x] Content-Schema `geschichten` in `src/content/config.ts` definiert (Felder gem. §6).
- [x] Footer (Desktop + Mobile) als `src/components/Footer.astro` umgesetzt.
- [x] Komponenten: Navigation, CTA-Button (`Button.astro`) umgesetzt.
- [x] Startseite (erster Durchgang) — alle Abschnitte, Texte, Farben.
- [x] Echte Fotos aus `assets/Images` in die Startseite eingebaut (`src/assets/*.jpg`).
- [x] Fotos exakt per MD5 den Figma-Bildstellen zugeordnet (Quellbild == Repo-Datei).
- [ ] Rest-Bildstellen: W-Erläbnis-Seitenfotos ergänzen; Seraina-Quelle prüfen (matchte keine Repo-Datei).
- [x] Foto-Collagen (Prozess, Gesehen, Für alle) mit exakten Figma-Überlappungen umgesetzt.
- [ ] Card-Komponente (Hover-Overlay) für Geschichten-Teaser ausbauen.
- [ ] Mobile-Menü in der Navigation (aktuell nur Logo + Kontakt auf Mobile).
- [ ] Weitere Seiten: Angebot, Geschichten (Übersicht + Detail), Sera Wild, Kontakt — je DE/EN.
- [ ] i18n-Grundgerüst (Routing + Übersetzungs-Strings) vervollständigen.
- [ ] GitHub-Actions-Workflow für Pages-Deploy einrichten (mit pnpm).
