# Prompt für Claude Code — Untermenü in der Navigation

Alles ab der Linie kopieren.

---

Das aufgeklappte Untermenü am Rechner in `src/components/Navigation.astro` wirkt wie ein fremdes Element, das über der Seite schwebt. Es soll aussehen wie ein Teil der Menüleiste.

Betroffen ist der Block mit der Klasse `nav-submenu`, um Zeile 110:

```
absolute left-0 top-[calc(100%+0.75rem)] min-w-[13rem] rounded-[0.75rem] bg-dark py-[0.5rem] shadow-lg
```

Das mobile Vollbild-Menü bleibt unberührt.

## Was daran nicht passt

- **Runde Ecken.** Auf der ganzen Website gibt es keine runden Ecken ausser an Knöpfen. Hier stehen 12 px.
- **Deckender Hintergrund.** Ein voll deckendes Dunkelgrün auf hellem Grund gibt eine harte Kante. Die Menüleiste selbst ist beim Scrollen halbtransparent mit Weichzeichner — das Untermenü sollte dasselbe Material haben.
- **Schlagschatten.** Sonst nirgends auf der Website.
- **Abstand von 12 px zur Leiste.** Dadurch schwebt der Kasten frei, statt an der Leiste zu hängen. Der Abstand macht ausserdem das Überfahren mit der Maus anfälliger.
- **Der Text bricht um.** «Simonas Geschichte» steht auf zwei Zeilen, weil die Mindestbreite zu knapp ist.

## Neu

```
absolute left-0 top-full min-w-[13rem] w-max py-[0.375rem]
border-t border-[rgba(160,136,109,0.35)]
```

Dazu im Style-Block:

```css
.nav-submenu {
  background-color: rgba(47, 50, 45, 0.55);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
}
@supports not (backdrop-filter: blur(10px)) {
  .nav-submenu { background-color: rgba(47, 50, 45, 0.94); }
}
```

Im Einzelnen:

- **Eckig.** `rounded-[0.75rem]` ersatzlos streichen.
- **Milchglas statt deckend.** Dieselbe Mischung wie `#site-header.nav-scrolled`, nur etwas dichter — 55 statt 50 Prozent, damit der Text darauf sicher lesbar bleibt. Für Browser ohne `backdrop-filter` die Rückfalllösung oben.
- **Kein Schatten.** `shadow-lg` streichen.
- **Direkt an der Leiste.** `top-[calc(100%+0.75rem)]` wird `top-full`.
- **Feine Linie oben** in Sand auf 35 Prozent, als Trennung zur Leiste.
- **Kein Umbruch.** `w-max` dazu, und den Einträgen `whitespace-nowrap`.

## Die Einträge

Etwas mehr Luft, damit die Fläche ruhig wirkt: Polsterung `0.5rem` oben und unten, `1.25rem` seitlich. Beim Überfahren wechselt die Schriftfarbe auf Rostorange `#BC541F` — keine Hintergrundfläche, kein Rahmen.

Die aktive Unterseite bleibt wie bisher gekennzeichnet.

## Prüfen

- Über einem hellen Abschnitt **und** über einem Hero-Bild aufklappen. Der Weichzeichner verhält sich auf beiden Untergründen anders — der Text muss in beiden Fällen gut lesbar sein.
- Mit der Maus vom Menüpunkt ins Untermenü fahren, ohne dass es zuklappt. Ohne den 12-px-Abstand sollte das zuverlässiger sein als vorher.
- Bei 1440 und 1728 px.
- Am Handy darf sich nichts ändern.

Melde mir, wie es über dem Hero-Bild aussieht — das ist der kritische Fall.
