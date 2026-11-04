# Technische aanpak herbouw website Triami (november 2026)

Kort onderzoek (ca. 8 minuten webresearch) naar de beste technische route voor het herbouwen van de verenigingswebsite van Triami: ca. 12 pagina's plus nieuws, beheer door niet-technische bestuursleden, huidige site WordPress 7.0 met Hestia-thema en Elementor 3.33.

Hoofdadvies in één zin: **blijf op WordPress, stap over op een eigen block theme (Full Site Editing, theme.json) zonder Elementor, bouw het thema als git-repo met Claude Code, test het in WordPress Playground/Studio, en host het op een pakket met PHP 8.3+, SSL en automatische back-ups.**

---

## 1. Aanbevolen route: block theme zonder pagebuilder

### De drie opties gewogen

| Criterium | (a) WordPress block theme (FSE) | (b) Klassiek thema + Elementor | (c) Statische site generator (Astro, Hugo, Eleventy) |
|---|---|---|---|
| Beheer door niet-technische redacteuren | Goed. Nieuws en pagina's via de standaard blokeditor; layout zit vast in patterns/templates, dus weinig stuk te maken. | Goed, maar meer knoppen en meer manieren om de layout te breken. | Slecht. Redacteuren moeten Markdown/git of een headless CMS leren; extra laag. |
| Onderhoudslast | Laag. Geen pagebuilder-plugin, geen premium-licentie, minder plugin-afhankelijkheden. | Hoger. Elementor + Hestia + add-ons moeten blijven matchen met WP-core; Elementor Pro is betaald. | Laag voor de site zelf, maar hoog voor het CMS-stuk en formulieren (externe diensten nodig). |
| Snelheid | Hoog. Alleen core-blokken, geen frontend-renderlaag. | Lager; audits melden regelmatig 2-3 s extra laadtijd op mobiel voor builder-sites. | Hoogst. |
| Kosten | Hosting + 0-2 betaalde plugins. | Hosting + Elementor Pro (jaarlijks) + evt. add-ons. | Hosting goedkoop/gratis, maar formulieren, feeds en CMS kosten los geld of tijd. |
| AI-bouwen (Claude Code) + git | Zeer goed. Een block theme is platte tekst: `theme.json`, HTML-templates, patterns, `style.css`. Perfect versioneerbaar en genereerbaar. | Matig. Elementor-layouts zitten als JSON in de database (`_elementor_data`), niet in git. | Zeer goed, maar met bovenstaand CMS-nadeel. |
| Lock-in | Laag: content blijft bruikbaar bij themawissel. | Hoog: bij deactiveren van Elementor blijven shortcodes/kale markup over. | Middel (framework-specifiek). |

### Advies

Kies **(a) een eigen block theme**. Argumenten:

1. WordPress 7.x is volledig op het Site Editor-model gebouwd (Block API v3, iframed editor afgedwongen vanaf 7.1, DataViews-admin, real-time samenwerking). Een block theme volgt de kern en veroudert dus het minst snel. ([O'Brien Media, WP 7.0](https://obrienmedia.co.uk/wordpress-7-0-what-hosting-providers-and-developers-need-to-know-with-faq))
2. Elementor voegt een extra renderlaag en lock-in toe; voor een site van 12 pagina's levert het geen voordeel meer op nu de blokeditor volwassen is. ([wpbase.co.uk, "Why I stopped recommending Elementor"](https://wpbase.co.uk/posts/why-stopped-recommending-elementor/), [NexterWP, Gutenberg vs Elementor 2026](https://nexterwp.com/blog/gutenberg-vs-elementor/))
3. Voor niet-technische bestuursleden is het belangrijkste dat ze **nieuwsberichten plaatsen, tekst aanpassen en foto's wisselen** zonder de layout stuk te maken. Dat regel je met vastgezette templates, block patterns (bijv. "Trainingsschema", "Lid worden-kaart") en `templateLock`. Zij hoeven de Site Editor nooit in.
4. Een block theme is 100% tekstbestanden en dus ideaal om met Claude Code in een git-repo te bouwen, te reviewen en terug te draaien.
5. Een statische generator (c) is technisch het snelst en goedkoopst, maar verplaatst de complexiteit naar het bestuur (contentbeheer, formulieren, feeds). Niet passend bij "beheer door niet-technische bestuursleden".

Praktische invulling:

- Begin vanaf **Twenty Twenty-Five** of een minimaal starterthema (bijv. via het Create Block Theme-plugin exporteren) en bouw een eigen child/eigen thema `triami` met: `theme.json` (kleuren uit het nieuwe logo, typografie, spacing), templates (`front-page`, `page`, `single`, `archive`, `404`), template parts (header, footer) en 6-10 patterns.
- Nieuws = gewone WordPress-berichten met een categorie; Query Loop-blok op de homepage en een archiefpagina. Geen extra nieuwsplugin nodig.
- Houd het aantal plugins onder de 8.

---

## 2. Actuele versies en hostingeisen

### WordPress en PHP (stand 4 november 2026)

- **WordPress 7.0** verscheen op 9 april 2026; **WordPress 7.1** stond gepland voor 19 augustus 2026 en is de huidige major. WordPress 7.0 liet PHP 7.2/7.3 vallen; minimum is PHP 7.4, aanbevolen is **PHP 8.3 of hoger**. ([O'Brien Media WP 7.0](https://obrienmedia.co.uk/wordpress-7-0-what-hosting-providers-and-developers-need-to-know-with-faq), [O'Brien Media WP 7.1](https://obrienmedia.co.uk/?p=212132), [DreamHost WP 7.1](https://www.dreamhost.com/blog/wordpress-release-7-1/))
- **PHP**: 8.5 is de nieuwste branch (actieve support tot eind 2027), 8.4 heeft actieve support tot 31 december 2026, 8.3 krijgt alleen nog security-fixes tot eind 2027, 8.2 loopt eind 2026 af en 8.1 is al end-of-life. Kies dus **PHP 8.3 of 8.4** op de hosting (8.4 heeft de voorkeur als alle plugins het ondersteunen). ([endoflife.date/PHP](https://endoflife.date/PHP))

### Minimale eisen hostingpakket

| Eis | Waarom |
|---|---|
| PHP 8.3/8.4 zelf instelbaar | Snelheid, veiligheid, WP 7.x-compatibiliteit |
| Gratis SSL (Let's Encrypt) + HTTPS-forcering | Standaard, AVG, SEO |
| Automatische dagelijkse back-ups met zelf terugzetten | Bestuur moet zonder helpdesk kunnen herstellen |
| Staging/kloon-mogelijkheid | Thema-updates en herbouw testen naast de live site |
| MariaDB/MySQL 8, object cache (Redis) is een plus | Snelheid bij nieuwsoverzichten |
| Nederlandse datacenters en Nederlandstalige support | AVG, bestuur |
| WP-CLI / SSH-toegang (wenselijk) | Deploy vanuit git met Claude Code |

### Antagonist (NL): staging?

- Antagonist biedt drie WordPress-pakketten: **Slim + WP** (1 site, 50 GB), **Plus + WP** (3 sites, 75 GB, Redis 128 MB) en **Pro + WP** (5 sites, 100 GB, Redis 256 MB). Alle met vrije PHP-keuze, gratis SSL en automatische back-ups (Slim: elke 2 uur gedurende 24 uur, 12-uurlijks 7 dagen, wekelijks 2 weken; Plus/Pro: elk uur gedurende 24 uur, elke 4 uur 7 dagen, dagelijks 21-28 dagen). ([antagonist.nl/webhosting/wordpress-hosting](https://www.antagonist.nl/webhosting/wordpress-hosting))
- **Een aparte, één-klik staging-omgeving wordt op de productpagina niet genoemd.** Antagonist's eigen werkwijze is: in DirectAdmin de WordPress-installatie **klonen met Installatron** naar een submap (bijv. `/ontwikkelomgeving`) of subdomein, eventueel met wachtwoord beveiligen, en daarna handmatig terugzetten. Dat werkt op **elk pakket** zolang er schijfruimte is; het is dus geen pakketfeature maar een DirectAdmin/Installatron-functie. ([Antagonist blog: ontwikkelomgeving](https://www.antagonist.nl/blog/ontwikkelomgeving-gebruiken/))
- Praktisch: op **Plus + WP** (3 websites) kun je een subdomein `test.triami.nl` als volwaardige tweede WordPress-site gebruiken; dat is de nette staging-oplossing bij Antagonist. Op Slim + WP moet het via een submap-kloon.
- Prijzen staan niet op de pagina die kon worden opgehaald; controleer actuele maandprijzen (excl. btw) op de site.

### Alternatieven

- **TransIP Managed WordPress** (Core/Pro/Max Managed, introductietarieven vanaf ca. € 3,99-9,99 p/m, daarna € 12,50-32,50 excl. btw). Beheerde updates en dagelijkse back-ups; staging niet expliciet genoemd in de bron. ([whtop.com TransIP](https://www.whtop.com/review/transip.nl))
- **Vimexx** (DirectAdmin, Installatron/Softaculous, gratis wildcard-SSL, dagelijkse back-ups; staging werkt net als bij Antagonist via kloon). Let op meldingen over renewal-prijsstijgingen. ([websiteplanet Vimexx](https://www.websiteplanet.com/nl/web-hosting/vimexx/))
- Hostnet kon in de tijd niet geverifieerd worden; controleer specifiek of hun WordPress-pakket een staging-knop heeft.

Conclusie hosting: Antagonist Plus + WP (of vergelijkbaar) is afdoende; echte één-klik staging is bij geen van de goedkope NL-aanbieders standaard, kloon via Installatron/subdomein volstaat voor deze schaal.

---

## 3. Lokaal ontwikkelen en testen zonder lokale WordPress

| Tool | Installatie nodig? | Snelste weg naar "iets zichtbaar"? | Geschikt voor |
|---|---|---|---|
| **WordPress Playground** (playground.wordpress.net) | Nee, alleen browser | **Ja, direct** | Thema-zip tonen aan bestuur, snelle iteraties, demo-links delen |
| **Studio by WordPress.com** | Desktop-app (gratis, geen Docker, Playground/SQLite onder de motorkap) | Binnen minuten | Dagelijks ontwikkelen, 7-daagse preview-links delen, Studio Sync naar productie |
| **Local (WP Engine)** | Desktop-app (gratis) | Binnen een minuut | Klassiek lokaal ontwikkelen met echte MySQL/NGINX |
| **wp-env** | Node.js + Docker | Traagst om op te zetten | CI, theme-unit-tests, ontwikkelaars |

([Seahawk: Studio by WordPress](https://seahawkmedia.com/wordpress/studio-by-wordpress/), [NexterWP: local dev environments](https://nexterwp.com/blog/best-local-wordpress-development-environments/))

### Advies

1. **Vandaag**: Playground. Claude Code bouwt het thema in de git-repo, maakt een zip, en genereert een Playground-link met blueprint. De gebruiker klikt en ziet de site.
2. **Daarna**: Studio by WordPress.com op de laptop van de bouwer voor doorontwikkeling en preview-links voor het bestuur. Geen Docker, geen MySQL.
3. wp-env alleen als er later geautomatiseerde tests in CI komen.

### Kan Playground een thema-zip laden via een blueprint-URL? Ja.

- Blueprints kennen de stap `installTheme` met `themeData` als resource `url` (publieke zip), `wordpress.org/themes` (slug) of `git:directory`. ([Playground Blueprint steps](https://developer.wordpress.org/playground/blueprints/steps/), [Blueprint examples](https://developer.wordpress.org/playground/blueprints/examples/))
- Een blueprint geef je mee als **`?blueprint-url=https://.../blueprint.json`** (of een zip-bundle), als **JSON in het URL-fragment** (`#{...}`, URL-encoded) of **base64 in het fragment**. ([Using Blueprints](https://developer.wordpress.org/playground/blueprints/using-blueprints/))
- Voorwaarde: blueprint en zip moeten publiek bereikbaar zijn **met CORS-header `Access-Control-Allow-Origin: *`**. `raw.githubusercontent.com` wordt in de docs als voorbeeld gebruikt en werkt hiervoor in de praktijk; GitHub Releases-assets kunnen CORS-problemen geven, gebruik dan de raw-URL of een eigen host.

Minimaal voorbeeld (`blueprint.json` in een publieke GitHub-repo):

```json
{
  "landingPage": "/",
  "preferredVersions": { "php": "8.3", "wp": "latest" },
  "login": true,
  "steps": [
    {
      "step": "installTheme",
      "themeData": {
        "resource": "url",
        "url": "https://raw.githubusercontent.com/<org>/<repo>/main/dist/triami.zip"
      },
      "options": { "activate": true }
    },
    {
      "step": "importWxr",
      "file": {
        "resource": "url",
        "url": "https://raw.githubusercontent.com/<org>/<repo>/main/content/triami-export.xml"
      }
    }
  ]
}
```

Openen met:
`https://playground.wordpress.net/?blueprint-url=https://raw.githubusercontent.com/<org>/<repo>/main/blueprint.json`

Let op: Playground bewaart niets tussen sessies (tenzij je OPFS/sync aanzet) en draait op SQLite; het is een demo/testomgeving, geen hosting.

---

## 4. Minimale, betrouwbare plugins

| Categorie | Aanbeveling | Waarom |
|---|---|---|
| Formulieren (lid worden, contact) | **Fluent Forms (gratis)** | Gratis versie heeft conditionele velden, meerdere formulieren, spamfilter en e-mailnotificaties zonder upsell-druk; lichter dan WPForms Lite en gebruiksvriendelijker dan Contact Form 7. Alternatief als je het nóg kaler wilt: Contact Form 7 + Flamingo. ([fs-code vergelijking](https://www.fs-code.com/blog/best-wordpress-contact-form-plugins), [Fluent Forms vs CF7](https://wpmanageninja.com/wp-fluent-form-vs-contact-form-7-which-one-is-the-best/)) Combineer altijd met **WP Mail SMTP** of de SMTP van de host, anders komen formuliermails niet aan. |
| Instagram/TikTok-feed | **Smash Balloon Instagram Feed (gratis)** + **Smash Balloon TikTok Feeds (gratis)** | Grootste en best onderhouden feed-familie; gratis Instagram-versie toont de eigen tijdlijn (geen hashtags/Reels), gratis TikTok-versie toont profielfeed. Dat is precies wat een vereniging nodig heeft. Pro vanaf $49/jaar alleen als Reels/hashtags gewenst zijn. ([fs-poster Smash Balloon review](https://www.fs-poster.com/blog/smash-balloon-review)) Overweeg i.v.m. AVG een "klik om te laden"-variant of alleen een link naar de kanalen. |
| Nieuws | **Geen plugin**: WordPress-berichten + Query Loop-blok | Core-functionaliteit, geen onderhoud, redacteuren kennen het. |
| Back-ups | **UpdraftPlus (gratis)** naast de host-back-ups | Bewezen, plant automatisch naar Google Drive/OneDrive van de vereniging; onafhankelijk van de hoster. (Als hosting al goede terugzetbare back-ups heeft, is dit de "tweede kopie".) |
| SEO | **The SEO Framework** of **Rank Math (gratis)** | The SEO Framework: geen advertenties/upsells, lichtgewicht, automatische meta's; ideaal voor niet-technische beheerders. Rank Math als je meer wilt sturen. Yoast kan ook maar is zwaarder en upsell-rijk. |
| Cookiebanner (AVG) | **Complianz (gratis)** | Nederlandse maker (Really Simple Plugins), genereert cookiebeleid en privacyverklaring in het Nederlands, scant de site op cookies, blokkeert embeds (Instagram/YouTube) tot toestemming. Gratis versie volstaat voor NL-only. ([Seahawk cookie-tools 2026](https://seahawkmedia.com/nl/wordpress/tools-voor-het-beheren-van-cookie-toestemming/)) Als de site geen trackers/embeds heeft, kan een banner zelfs achterwege blijven; Complianz vertelt dat na de scan. |
| Overig | **Create Block Theme** (alleen tijdens bouw), **Solid Security/Wordfence** optioneel | Create Block Theme exporteert Site Editor-wijzigingen terug naar thema-bestanden voor git. |

Totaal in productie: 5-7 plugins.

---

## 5. Migratie van bestaande content (WXR met Elementor-pagina's)

### Wat behoud je automatisch via WXR-import

- **Berichten (nieuws)**: titels, datums, auteurs, categorieën, tags, uitgelichte afbeeldingen en de inhoud. Oude berichten in de klassieke editor worden "Classic"-blokken; met **"Convert to blocks"** in de editor worden ze nette core-blokken.
- **Media**: de hele mediabibliotheek (vink "Download and import file attachments" aan bij import; de oude site moet dan nog online zijn, of kopieer `wp-content/uploads` mee).
- **Pagina-structuur**: slugs, hiërarchie, menu's (menu's zelf moeten in het block theme opnieuw als Navigation-blok worden opgebouwd, maar de pagina's en URL's blijven).
- **Gebruikers/auteurs**, reacties, custom fields.

### Wat moet handmatig

- **Alle Elementor-pagina's.** Elementor slaat de layout op als JSON in `_elementor_data`; in `post_content` staat een platgeslagen HTML-kopie met Elementor-wrappers. Er bestaat **geen betrouwbare één-klik-conversie** naar schone blokken; "Convert to blocks" werkt alleen op klassieke HTML, niet op Elementor-layouts. ([NexterWP: Elementor to Gutenberg 2026](https://nexterwp.com/blog/elementor-to-gutenberg/), [Seahawk: Elementor to Gutenberg](https://seahawkmedia.com/wordpress/elementor-to-gutenberg-conversion/))
- Werkwijze voor ca. 12 pagina's:
  1. Exporteer de WXR (is al gebeurd: `triamitriathlonvereniging.WordPress.2026-05-26.xml`).
  2. Laat Claude Code de WXR parsen: per pagina de **tekst, koppen, afbeeldingsverwijzingen en links** eruit halen (uit `post_content` of, netter, uit de `_elementor_data`-JSON in de postmeta), en per pagina een **blok-HTML-bestand** of pattern genereren met core-blokken.
  3. Importeer de berichten en media met de standaard WordPress-importer in de nieuwe (test)site.
  4. Maak de 12 pagina's opnieuw aan op **dezelfde slug** met de gegenereerde blokinhoud; controleer per pagina desktop/mobiel.
  5. Bouw menu, formulieren en feeds opnieuw.
  6. Zet 301-redirects voor URL's die veranderen (bijv. via de hosting of een lichte Redirection-plugin).
  7. Pas daarna Elementor + Hestia deactiveren/verwijderen; ruim `_elementor_*`-postmeta op.
- **Formulieren** (Elementor-forms of een losse plugin): inzendingen gaan niet mee; formulieren opnieuw opbouwen in Fluent Forms.
- **Hestia-instellingen** (Customizer-kleuren, header-afbeeldingen): niet overdraagbaar; terug laten komen in `theme.json` en templates.
- **Shortcodes** van verwijderde plugins: zoeken en vervangen.

### Tip voor de volgorde

Bouw eerst het thema met dummy-content in Playground; importeer daarna de echte WXR in Studio of op `test.triami.nl`; pas als alles klopt de live-domeinwissel doen.

---

## Bronnen

- https://obrienmedia.co.uk/wordpress-7-0-what-hosting-providers-and-developers-need-to-know-with-faq
- https://obrienmedia.co.uk/?p=212132
- https://www.dreamhost.com/blog/wordpress-release-7-1/
- https://endoflife.date/PHP
- https://wpbase.co.uk/posts/why-stopped-recommending-elementor/
- https://nexterwp.com/blog/gutenberg-vs-elementor/
- https://www.antagonist.nl/webhosting/wordpress-hosting
- https://www.antagonist.nl/blog/ontwikkelomgeving-gebruiken/
- https://www.whtop.com/review/transip.nl
- https://www.websiteplanet.com/nl/web-hosting/vimexx/
- https://developer.wordpress.org/playground/blueprints/steps/
- https://developer.wordpress.org/playground/blueprints/examples/
- https://developer.wordpress.org/playground/blueprints/using-blueprints/
- https://developer.wordpress.org/playground/developers/build-an-app/
- https://seahawkmedia.com/wordpress/studio-by-wordpress/
- https://nexterwp.com/blog/best-local-wordpress-development-environments/
- https://www.fs-code.com/blog/best-wordpress-contact-form-plugins
- https://wpmanageninja.com/wp-fluent-form-vs-contact-form-7-which-one-is-the-best/
- https://www.fs-poster.com/blog/smash-balloon-review
- https://seahawkmedia.com/nl/wordpress/tools-voor-het-beheren-van-cookie-toestemming/
- https://nexterwp.com/blog/elementor-to-gutenberg/
- https://seahawkmedia.com/wordpress/elementor-to-gutenberg-conversion/
