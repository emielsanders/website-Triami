# Testrapport demo-site Triami — 4 november 2026

Geautomatiseerde testronde op de lokale Playground-demo (WordPress 7.1, PHP 8.3), vóór de volgende stap (hosting/staging). Alle genoemde fixes zijn verwerkt, gecommit en opnieuw getest.

## 1. Wat is getest

| Test | Middel | Omvang |
|---|---|---|
| Linkcheck en crawl | Playwright-crawler (`docs/technische-audit.json`) | 13 pagina's + alle interne links |
| SEO-basis | Crawler: titel, meta description, Open Graph, canonical, één H1, kopvolgorde, alt-teksten, taal | alle pagina's |
| Toegankelijkheid | axe-core 4.10 (WCAG 2.1 AA + best practices) | alle pagina's |
| Mobiel | Playwright op 400 px: horizontaal scrollen, menu openen, tikdoelen ≥ 24 px, kleinste lettergrootte | home, trainingen, lidmaatschap, faq |
| Prestaties, SEO, best practices | Lighthouse 12 (mobiel en desktop) | home, lidmaatschap |
| Gebruiksvriendelijkheid en volledigheid | Heuristische review tegen checklist verenigingswebsite (`docs/ux-review.md`, 24 bevindingen) | hele site |

## 2. Resultaat na fixes

- Alle 13 pagina's bereikbaar (200), geen dode interne links, geen console-fouten.
- Elke pagina: unieke titel, meta description, Open Graph-tags (incl. og-image 1200×630), canonical, precies één H1, kopvolgorde kloppend, alle afbeeldingen met alt-tekst, `lang="nl"`. JSON-LD (SportsClub) op de homepage.
- axe: 0 fouten in de site zelf. De 2 resterende meldingen komen uit de WordPress-beheerbalk (alleen zichtbaar voor ingelogde beheerders).
- Mobiel: geen horizontaal scrollen meer, hamburgermenu opent met alle 11 items, kleinste tekst 14 px, resterende kleine tikdoelen zijn beheerbalk-knoppen.
- Lighthouse: toegankelijkheid 99–100, SEO 100, best practices 100 (home). Prestatiescores (58–93) zijn in Playground niet representatief: de server draait in de browser; op echte hosting met caching ligt dit hoger.
- Lidmaatschap: best practices 78 door het Microsoft Forms-iframe (third-party cookies). Zie open punten.

## 3. Opgelost in deze ronde

1. Trainingsschema stond vast op 4 kolommen → kaarten werden op telefoon afgekapt. Nu responsief.
2. Knoptekst wit op Triami-rood haalde 4,36:1 (net onder WCAG AA). Knoppen nu op donkerrood `#C4151B` (6,05:1); het heldere rood blijft voor lijnen en accenten.
3. Dubbele `<header>`/`<footer>`-landmarks (template-part én groep) → één landmark per rol.
4. Footerkoppen h4 na h2/h3 (kopvolgorde) → h2 in kleine stijl; bestuurspagina kreeg een h2 boven de kaarten.
5. Footerlinks 13 px en lage tikdoelen → 14 px met 24 px hoogte; headerlinks ruimer.
6. Geen meta description/OG/JSON-LD → toegevoegd in het thema (schakelt zichzelf uit zodra een SEO-plugin actief is).
7. Sitetaal `en-US` → Nederlands (blueprint `setSiteLanguage` + fallback in het thema).
8. Submenu onder Vereniging (Bestuur, Trainers, Teamcompetitie, Clubcompetitie, Clubkleding, VCP): alle pagina's nu in het menu bereikbaar.
9. Knop "Word proeflid" in de header; alle aanmeldknoppen linken naar het formulier zelf (`/lidmaatschap/#inschrijven`); aanmeldroute op Trainingen gelijkgetrokken.
10. MS Forms-iframe in het Nederlands (`lang=nl-NL`), vaste hoogte per schermbreedte (minder layoutverschuiving) en een "open in nieuw venster"-link voor telefoons.
11. Nieuws in de footer opgenomen (was nergens gelinkt).
12. Naamgeving gelijkgetrokken: "Triami Sprint Triathlon".
13. Favicon en 301-redirects van oude URL's; fonts lokaal gehost (geen Google Fonts-verzoek meer op de echte site).

## 4. Open punten

**Zelf te doen bij livegang (geen bestuur nodig)**
- Bestuursfoto's en PDF's (statuten, reglement, privacyverklaring) naar de mediabibliotheek van de nieuwe site; nu verwijzen ze naar de oude site.
- Site-icoon instellen in WordPress (favicon komt nu uit het thema).
- Cookiebanner/consent: het Microsoft Forms-iframe plaatst third-party cookies. Of consent via Complianz, of formulier vervangen door Fluent Forms (dan geen externe cookies). Advies: Fluent Forms.
- Privacyverklaring als pagina (nu PDF op de oude site) en cookieverklaring.
- "Check bestuur"-blokken verbergen zodra de site aan leden wordt getoond (CSS-regel `.triami-check { display:none }` of verwijderen).
- Zoekfunctie: bewust weggelaten bij 13 pagina's; eventueel op de 404-pagina.

**Pas na input van het bestuur** (zie `docs/ophaallijst-bestuur.md`)
- Agenda/wedstrijdkalender (clubcompetitie, Triami Sprint Triathlon, trainingsweekend): gebruikelijk op een verenigingssite, nu afwezig.
- Social media: Instagram/Facebook/TikTok-koppelingen en eventueel feed; nu alleen Strava en Spond.
- Foto's van trainingen en teams (homepage en Trainingen zijn nu tekst-only).
- Tarieven 2026, teamindeling, trainers, VCP-mailadres, Start2Tri-editie, kledingleverancier.
- Besluit over nieuws op de site, en over een vrijwilligers-/sponsorpagina.

## 5. Herhalen
`cd pg && python3 audit.py` (crawler + axe + mobiel) en `npx lighthouse <url>` draaien tegen de staging-site zodra die bestaat; dan zijn ook de prestatiescores betekenisvol.
