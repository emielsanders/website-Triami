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

## Besluiten 4 nov (ronde 2)
- GitHub: Emiel maakt zelf repo `emielsanders/triami-website` aan (leeg, publiek); daarna koppelen en pushen.
- Hosting: komt bij Vimexx of andere partij; pas nodig bij staging/livegang, niet nu.
- Inschrijfformulier: MS Forms blijft. Gevolg: bij livegang cookieconsent (Complianz) voor het iframe.
- Feedback bestuur via `docs/feedbackboek-2026-11-04.pdf` (62 bladen, groot nummer rechtsboven; `tools/feedback_pdf.py` + `pg/shots_pdf.py`).

- Social media (4 nov, avond): blok `triami/volg` op de homepage: Strava-club (id 101737, 83 leden; officiële widget sinds jan 2026 onbetrouwbaar, dus link + kengetallen), Spond-uitnodiging met QR (`assets/img/spond-qr.svg`), Instagram-plaatshouders (feed via Smash Balloon bij livegang, accountnaam onbekend). Instagram-link ook in footer.
- Feedbackpagina (artifact "Triami feedback", db-opslag): `tools/feedback_artifact.py`; opmerkingen uitlezen met ArtifactData (collecties `opmerkingen`, `antwoorden`).

- Repo is publiek; demo via korte link: `https://playground.wordpress.net/?blueprint-url=https://raw.githubusercontent.com/emielsanders/website-Triami/main/playground/blueprint.json` (thema-zip en WXR staan in `playground/dist/`, na `tools/build.py` kopiëren en pushen).

- 5 nov avond: trainingsschema bijgewerkt uit nieuwsbrief jan 2026 (wo 19:30–20:45, vr 6:00 zelfstandig met De IJsel, zo-winter bonuszwemuur, fietsen op afspraak), racefiets-icoon; vereniging: geschiedenis (opgericht 11-4-2006), trainingsweekend april, Social Salad, ALV, samenwerking (De IJsel = zwemclubdeventer.nl; De Zwaluwe nog onbekend), sponsoren 3SL Sports + KoffieDok, Rechtop; 10 demo-afbeeldingen in theme/triami/assets/img/demo (tools/demo_afbeeldingen.py) + patroon fotostrook op home; Instagram @triami_triathlon; Smash Balloon geïnstalleerd op staging (koppelen door Emiel).
- Staging bijwerken: push naar GitHub, dan https://www.triami.nl/update-thema.php?token=…&actie=thema&wxr=1 en &actie=import (token niet in repo; zie sessie). Oude site: plugin WP File Manager nog verwijderen.

## Volgende stappen
1. Ophaallijst bestuur afwerken (`docs/ophaallijst-bestuur.md`) en `Check bestuur`-regels verwijderen.
2. GitHub-repo aanmaken en pushen; `playground/blueprint.json` met `installTheme` via raw-URL (zie `docs/technische-aanpak.md`).
3. Hosting bestellen; kloon `test.triami.nl`; thema-zip uploaden, WXR importeren, menu/instellingen controleren.
4. Plugins: Fluent Forms, Smash Balloon (als socials bestaan), UpdraftPlus, The SEO Framework, Complianz.
5. Site-icoon instellen (nu favicon uit thema); og-image; echte logo-SVG en bestuursfoto's in de mediabibliotheek.
6. Bestuur laten testen op staging; DNS/SSL; livegang; Hestia/Elementor verwijderen.

## Opruimen bij livegang
- `update-thema.php` en `beheer-lader.php` van www.triami.nl verwijderen (eerst `&actie=weg`).
- Plugin WP File Manager van de oude site verwijderen.
- `privacystatement.pdf` van www.triami.nl verwijderen (let op: statuten-PDF en huishoudelijk reglement wél overzetten, de nieuwe site linkt ernaar); de privacyverklaring staat nu op /privacy/ (vervangt de versie van juli 2018). Besluit Emiel (5 nov): redirect van de PDF naar /privacy/ (301).
- Password Protected uitzetten en zoekmachines toestaan op de nieuwe site.

## 5 november 2026 – menu-aanpassingen (akkoord Emiel, punten 1-4)
- Lidmaatschap & tarieven is een submenu met Tarieven en Veelgestelde vragen.
- Nieuws staat uit footer en import (`status: draft` in front matter) en is op staging concept, tot er berichten zijn.
- Nieuwe pagina Activiteiten (onder Vereniging, ook in footer en als kaart op Vereniging).
- Privacyverklaring is een pagina (/privacy/) op basis van de PDF van juli 2018; footer, Contact en Bestuur linken ernaar. Check bestuur: kanalen (Facebook/WhatsApp vs Spond), Run2Day, datum.

## 6 november 2026 – feedback reviewer verwerkt
- Sticky menu, mobiele verfijning (kop op één regel, fotostrook als veegrij, tabellen met afbreking, minder witruimte).
- E-mailadressen via antispambot() in alle blokken; geen e-mailadressen in de meta description.
- FAQ: zwembad/baan-lidmaatschap niet nodig, handdoek, elke fiets volstaat; geen dubbele info (bedragen alleen bij #tarieven).
- VCP alleen voornaam (besluit 6 nov). Start2Tri: geen zwemles/zekere basis, vol is vol, opmerkingenveld. Tarieven 2026: € 214,50.
- Deploy-les: raw.githubusercontent negeert de querystring voor caching per CDN-knooppunt; de server kan tot ~5 min een oudere zip krijgen. Na een thema-deploy controleren en zo nodig na 5 minuten opnieuw `actie=thema`.
