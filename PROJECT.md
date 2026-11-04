# Triami-website — projectgeheugen

Dit bestand is het vertrekpunt van elke werksessie (mens of AI). Lees het eerst; werk het bij aan het eind.

## Doel
Nieuwe website voor Triami Triathlonvereniging Deventer (triami.nl), beheerbaar door niet-technische bestuursleden, als vervanging van de WordPress-site met Hestia-thema en Elementor.

## Stand van zaken (4 november 2026)
- Eigen WordPress **block theme** `triami` gebouwd (theme.json v3, templates, header/footer, patterns). Geen Elementor.
- Alle pagina's als blokinhoud in `content/pages/` (13 stuks), met `Check bestuur`-markeringen voor onbevestigde feiten.
- Bouwscripts: `tools/build.py` (thema-zip + WXR-import) en `tools/blueprint.py` (Playground-blueprint met alles inline).
- Demo bekeken in WordPress Playground; geen console-fouten op desktop en mobiel.
- Favicon (hartslag-SVG) en 301-redirects van oude URL's zitten in `functions.php`.
- Testronde 4 nov: linkcheck, SEO-basis, axe, mobiel, Lighthouse, UX-review; bevindingen verwerkt. Zie `docs/testrapport-2026-11-04.md` en `docs/ux-review.md`.
- Nog niet: hosting, staging, plugins, livegang.

## Keuzes
| Onderwerp | Keuze | Reden |
|---|---|---|
| Techniek | Block theme, geen pagebuilder | Lichter, geen lock-in, volledig in git; redacteuren werken in de blokeditor |
| Hosting (voornemen) | Antagonist Plus + WP, kloon op `test.triami.nl` als staging | Zie `docs/technische-aanpak.md` |
| Fonts | Montserrat (koppen) + Source Sans 3 (tekst), lokaal gehost als variabele woff2 in `assets/fonts/` (AVG) | De Playground-demo valt terug op Google Fonts, omdat binaire bestanden niet inline in de blueprint passen |
| Kleur | Rood `#ED1E24` alleen als accent (lijnen, hartslag); knoppen op donkerrood `#C4151B` voor contrast; palet rood/zwart/wit, geen blauw | Huisstijl + kleurenblindheidstoets, zie `docs/huisstijl-voorstel.md` |
| Toegankelijkheid | Kleur nooit enige drager van informatie; witte tekst op rood alleen groot/vet, kleine tekst op `#C4151B` | Contrastratio's in stijltegel |
| URL's | Alle pagina's top-level (`/bestuur/`, `/faq/`), zoals op de oude site | Korte URL's, minder redirects |
| Nieuws | Pagina + Query Loop aanwezig, geen berichten | Bestuur beslist of nieuws op de site komt |
| Inschrijfformulier | Microsoft Forms-embed behouden | Werkt nu; later eventueel Fluent Forms |
| Bankrekening | Niet op de site | Fraude/privacy |
| Logo | `assets/img/logo.svg` (afgeleid uit vector-PDF, svgo-geoptimaliseerd); footer gebruikt dezelfde SVG met CSS-filter naar wit | Officiële SVG ontbreekt nog |

## Sitemap en menu
Home · Vereniging (Bestuur, Trainers, Teamcompetitie, Clubcompetitie, Clubkleding, Vertrouwenscontactpersoon) · Trainingen · Start2Tri · Lidmaatschap (Veelgestelde vragen) · Contact · Nieuws (alleen in footer/Query Loop).
Menu staat vast in `theme/triami/parts/header.html` (navigation-links met vaste URL's); footer in `parts/footer.html`.

## Mappen
```
theme/triami/        het thema (dit gaat naar WordPress)
  theme.json         kleuren, fonts, spacing, blokstijlen
  templates/         front-page, page, single, index/archive, 404
  parts/             header, footer
  patterns/          hero, intro, trainingsschema, cta-proeflid, start2tri-teaser, home-contact, hartslaglijn, logo
  assets/css/triami.css  aanvullende stijlen (kaart, donker, hartslag, persoon, triami-check)
content/pages/*.html pagina-inhoud als blok-HTML met front matter (title, slug, order)
tools/build.py       maakt dist/triami.zip en dist/triami-paginas-import.xml
tools/blueprint.py   maakt dist/blueprint-inline.json + dist/playground-url.txt
playground/          (gereserveerd voor blueprint.json zodra er een GitHub-repo is)
docs/                rapporten, handleiding, ophaallijst, screenshots
dist/                bouwresultaat (niet in git)
```

## Werkwijze
1. Tekst wijzigen: pas `content/pages/<slug>.html` aan (blok-HTML). Vormgeving: `theme.json` of `assets/css/triami.css`. Vaste blokken: `patterns/`.
2. `python3 tools/build.py && python3 tools/blueprint.py`
3. Lokaal bekijken: `npx @wp-playground/cli server --mount=theme/triami:/wordpress/wp-content/themes/triami --mount=dist:/wordpress/wp-content/triami-import --blueprint=playground/local-blueprint.json --port=9400`
4. Commit met duidelijke boodschap.

## Volgende stappen
1. Ophaallijst bestuur afwerken (`docs/ophaallijst-bestuur.md`) en `Check bestuur`-regels verwijderen.
2. GitHub-repo aanmaken en pushen; `playground/blueprint.json` met `installTheme` via raw-URL (zie `docs/technische-aanpak.md`).
3. Hosting bestellen; kloon `test.triami.nl`; thema-zip uploaden, WXR importeren, menu/instellingen controleren.
4. Plugins: Fluent Forms, Smash Balloon (als socials bestaan), UpdraftPlus, The SEO Framework, Complianz.
5. Site-icoon instellen (nu favicon uit thema); og-image; echte logo-SVG en bestuursfoto's in de mediabibliotheek.
6. Bestuur laten testen op staging; DNS/SSL; livegang; Hestia/Elementor verwijderen.
