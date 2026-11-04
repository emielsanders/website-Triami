# Content-inventaris huidige website www.triami.nl

Peildatum: 4 november 2026. Bron: live HTML-pagina's en de WordPress REST API (`/wp-json/wp/v2/pages`, `/wp-json/wp/v2/posts`, `/wp-json/`).

## 0. Technische basis (uit `/wp-json/` en paginabron)

- Sitenaam: **Triami Triathlonvereniging**; tagline: *Dé triathlonvereniging van Deventer en omstreken*; tijdzone Europe/Amsterdam.
- WordPress + thema **Hestia** (ThemeIsle), pagina's gebouwd met **Elementor 4.3.6** (+ Elementor Pro).
- Herkenbare plugins via REST-namespaces: Elementor (incl. elementor-ai, elementor-one, elementor-mcp-composer), WPForms, Otter Blocks, Akismet, Duplicator, Ea11y (toegankelijkheid), Instagram Feed (Smash Balloon, v6.15.1, geladen maar nergens zichtbaar als feed), WooCommerce-CSS in het thema (geen webshop aanwezig). Geen Contact Form 7, geen Yoast.
- Google Fonts: Open Sans en Roboto.
- Favicon: `/wp-content/uploads/2019/04/cropped-favicon-1-*.png`.
- Logo's: `/wp-content/uploads/2019/04/Triami-logo-nieuw-96px.png` (header, 301x96) en `/wp-content/uploads/2019/04/Triami-logo-nieuw-white1.png` (footer, wit).
- Headerfoto's (Elementor-achtergronden, 2019/2020): `2019/03/triami_fietsen.jpg` (home), `2020/01/triami_header_1.jpg` (trainingen, nieuws), `2020/01/triami_header_2.jpg` (clubcompetitie, trainers, faq), `2019/12/triami_header_3-1.jpg` (vereniging, lidmaatschap, start2tri, vertrouwenscontactpersoon), `2019/12/triami_header_4.jpg` (bestuur, teamcompetitie, clubkleding).

## 1. Overzicht pagina's (REST API, 14 stuks, allemaal top-level)

| ID | Slug | Titel | Laatst gewijzigd |
|---|---|---|---|
| 124 | / (triami-front) | Front Page | 2019-04-19 |
| 2 | vereniging | VERENIGING | 2025-04-13 |
| 348 | bestuur | BESTUUR | 2025-11-16 |
| 363 | trainers | TRAINERS | 2025-04-13 |
| 530 | trainingen | TRAININGEN | 2025-11-16 |
| 550 | teamcompetitie | TEAMCOMPETITIE | 2025-04-13 |
| 567 | clubcompetitie | CLUBCOMPETITIE | 2025-04-13 |
| 451 | clubkleding | CLUBKLEDING | 2023-02-23 |
| 456 | lidmaatschap-2 | LIDMAATSCHAP | 2026-06-07 |
| 462 | start2tri | START2TRI | 2026-03-05 |
| 110 | faq | FAQ | 2025-11-16 |
| 171 | nieuws | NIEUWS | 2019-12-30 |
| 560 | vertrouwenscontactpersoon | VERTROUWENSCONTACTPERSOON | 2025-02-10 |
| – | bestuur/huishoudelijk-reglement-vastgesteld-19-1-2025 | Huishoudelijk reglement vastgesteld 19.1.2025 | (upload nov 2025) |

Niet bestaand: `/wedstrijden/` geeft een foutmelding (client error / 404). Er is geen aparte contactpagina.

## 2. Menustructuur (live)

**Hoofdmenu (header)**
- VERENIGING (`/vereniging/`)
  - BESTUUR (`/bestuur/`)
  - CLUBCOMPETITIE (`/clubcompetitie/`)
  - CLUBKLEDING (`/clubkleding/`)
  - TRAINERS (`/trainers/`)
  - TEAMCOMPETITIE (`/teamcompetitie/`)
- TRAININGEN (`/trainingen/`)
- START2TRI (`/start2tri/`)
- LIDMAATSCHAP (`/lidmaatschap-2/`)
  - FAQ (`/faq/`)

**Footer (op elke pagina gelijk)**
- Wit logo (link naar home)
- E-mail: secretaris@triami.nl (mailto)
- Menu: VERENIGING · TRAININGEN · LIDMAATSCHAP · START2TRI
- Links: *Privacy verklaring* (`https://www.triami.nl/privacystatement.pdf`, laadt, HTTP 200) · *Vertrouwenscontactpersoon* (`/vertrouwenscontactpersoon/`)
- Credit: "Hestia | Developed by ThemeIsle" (link naar themeisle.com)
- Geen social-media-iconen, geen copyright, geen adres of telefoonnummer.

NIEUWS en VERTROUWENSCONTACTPERSOON staan niet in het hoofdmenu; de VCP-pagina alleen in de footer; NIEUWS is nergens gelinkt.

## 3. Inhoud per pagina

### 3.1 Home (`/`)
- Hero met achtergrondfoto `2019/03/triami_fietsen.jpg`, H1 **TRIAMI**, subkop *Dé triathlonvereniging van Deventer en omstreken!*, knop **"Maak vrijblijvend kennis!"** → `/lidmaatschap-2/`.
- Verder géén inhoud: geen intro, geen nieuws, geen trainingsoverzicht, geen socials, geen Instagram-feed (plugin wel geladen).
- Status: zeer mager; pagina sinds 2019 niet gewijzigd.

### 3.2 Vereniging (`/vereniging/`)
Koppen: VERENIGING (H1), Triami, Een greep uit onze activiteiten.
- Triami is opgericht in **2006**, "bloeiende, actieve triathlonvereniging met **ruim 100 leden**", voor iedereen uit Deventer en omgeving. Onder deskundige begeleiding werken aan zwem- en loopconditie, op alle onderdelen aandacht voor techniek.
- Voor beginner én topsporter. Zwemtrainingen gericht op borstcrawltechniek; **advies: eerst een borstcrawlcursus volgen** voor lidmaatschap.
- Citaat over de naam/het logo: "Triami staat zeer vrij vertaald voor vrienden van de triathlon. Het logo bestaat uit het hartritme, de P Q R S T van het ECG. Het ultieme teken van leven, van een gezond leven, een sportief leven. Het is een link naar de sport waarom alles draait om de hartslag en natuurlijk om hart hebben voor.."
- Activiteiten: wekelijkse zwem- en looptrainingen; jaarlijks trainingsweekend; jaarlijkse **mini-triathlon in sportpark Keizerslanden** (link → `http://www.triathlondeventer.nl/`); gemiddeld 1 dames- en 3 herenteams in de landelijke Teamcompetities (link → `/teamcompetitie/`); clubcompetitie (link → `/clubcompetitie/`); "Bij alle sportevenementen in de wijde omgeving kom je onze clubleden tegen."
- Afbeeldingen: alleen het logo (herhaald in de body).
- Verouderd: "1 dames- en 3 herenteams" strijdt met teamcompetitie-pagina (2 herenteams komend seizoen); ledental controleren.

### 3.3 Bestuur (`/bestuur/`)
Koppen: BESTUUR, Bestuur, Algemene gegevens, Overige gegevens, Statuten.
| Naam | Functie | E-mail |
|---|---|---|
| Heleen | Voorzitter | voorzitter@triami.nl |
| Alma | Secretaris | secretaris@triami.nl |
| Edwin | Penningmeester | penningmeester@triami.nl |
| Emiel | Algemeen bestuurslid | algemeenbestuurslid@triami.nl |
- Foto's (nov 2025, 150x150, lege alt): `uploads/2025/11/Heleen-150x150.png`, `Alma-2-150x150.png`, `Edwin-150x150.png`, `Emiel-150x150.png`.
- Overige gegevens: **Bankrekening NL04INGB0005059468**, **BIC INGBNL2A**, **KvK 08147105**, **NTB lidnr. 2019**.
- Statuten: "Onze statuten zijn hier in te zien" → `https://www.triami.nl/statuten_akte-van-oprichting_18-5-2006.pdf` (HTTP 200).
- Huishoudelijk reglement: → `/bestuur/huishoudelijk-reglement-vastgesteld-19-1-2025/`, een kale subpagina met enkel een link naar `uploads/2025/11/Huishoudelijk-reglement-vastgesteld-19.1.2025.pdf`.
- Opmerking: alleen voornamen, geen achternamen; bestuurspagina is recent (nov 2025) en lijkt actueel.

### 3.4 Trainers (`/trainers/`)
Koppen: TRAINERS, Onze trainers.
- Intro: alle trainers zijn ervaren (tri)atleten met relevant trainersdiploma; bestuur en trainers hebben zich gecommitteerd aan gedragsregels voor veilig en waardig sporten, gebaseerd op de gedragscodes van NOC*NSF (link → `https://nocnsf.nl/high5-stappenplan/kennisbank`).
| Naam | Rol | Diploma |
|---|---|---|
| Christianne | Hoofdtrainer i.o. | TTN-3 |
| Marten | Looptrainer | TTN-1 |
| Harco | Looptrainer | TTN-1 |
| Alette | Looptrainer | TTN-1 |
| Sander | Zwemtrainer / zwemanalyse | TTN-1 |
| Ron | Zwemtrainer | TTN-1 |
| (geen naam) | Zwemtrainer, in opleiding | – |
| (geen naam) | Zwemtrainer, in opleiding | – |
- Oproep: "Lijkt het jou ook leuk om als trainer een vrijwillige bijdrage te kunnen leveren aan Triami? Stuur dan een mailtje naar secretaris@triami.nl".
- Afbeeldingen: geen trainersfoto's.
- Placeholder/verouderd: twee naamloze "In opleiding"-kaarten; inconsistente schrijfwijze (LOOPTrainer, zwemTrainer, ttn-1).

### 3.5 Trainingen (`/trainingen/`)
Koppen: TRAININGEN, Onze trainingen, Zwemmen, Hardlopen, Fietsen.
- Alle trainingen onder leiding van gediplomeerde trainers; voor beginner en ervaren triatleet; **lid moet de borstcrawl al in enige mate beheersen**.
- Toegewerkt naar triathlonseizoen (**mei – september**); schema's gericht op **Sprint en OD**; voor lange afstand zelf bijtrainen.
- Hardlooptrainingen in principe het hele jaar, behalve feestdagen en extreem weer. Zwemtrainingen in de Scheg en het Borgelerbad: **zomerstop** (beperkte beschikbaarheid zwembadpersoneel). Alle trainingen vervallen op feestdagen. Afgelastingen via **Spond**.
- Schema:
  - Zwemmen **dinsdag 19:30 – 20:30 u, De Scheg** (volgens jaarschema)
  - Zwemmen **donderdag 20:45 – 21:45 u, Borgelerbad** (volgens jaarschema)
  - Hardlopen **woensdag 19:30 – 20:30 u, Atletiekbaan AV Daventria**; afwisselend o.l.v. Marten, Harco of Alette, met aandacht voor loopscholing
  - Fietsen: geen vaste training; leden doen voorstellen via WhatsApp of Spond; afstand en tempo onderling; afspraak **"samen uit = samen thuis"**
- Afbeeldingen: `uploads/elementor/thumbs/de-scheg-….jpg`, `uploads/elementor/thumbs/borgelerbad-….jpg`, `uploads/2020/01/hardlopen.jpg`.
- Opmerking: lidmaatschapspagina belooft "vier trainingsmomenten per week", hier staan er drie vaste. Jaarschema zwemmen wordt genoemd maar niet gelinkt.

### 3.6 Teamcompetitie (`/teamcompetitie/`)
Koppen: TEAMCOMPETITIE, Hoe werkt het?, Teams.
- "Wie denkt dat triathlon een sport is voor individuen heeft het mis!" Landelijke teamcompetitie (link → `https://teamcompetities.nl/`): serie van **5 wedstrijden** in verschillende formats en afstanden; promotie/degradatie; team van **4 mannen of 4 vrouwen**; formats: individueel sprint en OD, en **TeamTimeTrial**.
- "Voorgaande jaren is Triami uitgekomen met 1 dames- en 3 herenteams. Triami komt komend seizoen met **2 herenteams** uit." Interesse: via teamcaptain of secretaris@triami.nl.
- Teams: **Dames – 2e Divisie Noord – captain Leoniek**; **Heren 1 – 1e Divisie Noord – captain Jorn**; **Heren 2 – 2e Divisie Noord – captain Simon**; **Heren 3 – 3e Divisie Noord – captain Simon**.
- Afbeeldingen (2019, Facebook-exports): `uploads/2019/11/65018053_…_o.jpg` (dames), `60964022_…_o-1.jpg` (heren 1), `64908631_…_o.jpg` (heren 2), `PHOTO-2019-09-18-20-28-38.jpg` (lightbox "appelloop").
- Verouderd: tekst zegt 2 herenteams, maar er staan nog 4 teamblokken; divisies en captains zijn van 2019/2020; foto's uit 2019.

### 3.7 Clubcompetitie (`/clubcompetitie/`)
Koppen: CLUBCOMPETITIE, Hoe werkt het?, Puntentelling.
- Jaarlijkse **Triami Club Competitie (TCC)** als aanvulling op trainingen; eindklassement van de beste **6** resultaten (intro) resp. **7** resultaten (puntentelling) – tegenstrijdig; hoogste man en vrouw worden clubkampioen. Laagdrempelige trainingswedstrijdjes (wisselen oefenen, progressie zwemsnelheid).
- Puntentelling: dames- en herencategorie; 1e 15 pt, 2e 14, 3e 13 … t/m 2 pt; deelnemen 1 pt; volbrengen min. 2 pt; vrijwilligers 5 pt; wisselbeker voor beste dame en heer op de ALV.
- Onderdelen: 500 m zwemtest zwembad; wisselwedstrijd 300 m lopen / 1 km fietsen (6x lopen, 5x fietsen); Deventer Sprint Triathlon; duathlon/zwemloop 500 m zwemmen + 4x 1 km lopen; zwemfiets 500 m + 10 km; zwemtest open water Bussloo; tijdrit 10 km; Coopertest 12 min; cross-duathlon bos 5 km lopen, 3 ronden fietsen, 2,5 km lopen.
- Afbeelding: `uploads/2019/12/clubcompetitie.jpg` (lege alt).
- Geen kalender/data, geen standen.

### 3.8 Clubkleding (`/clubkleding/`)
- Trisuits op voorraad en te passen bij **Koffiedok, Scheepvaartstraat 6B** (link `http://koffiedok.nl/contact/`).
- Overige kleding (fiets- en loopkleding) 2-jaarlijks via de **webshop van Bioracer** (geen URL); secretaris informeert leden wanneer bestellen weer kan.
- Afbeelding: `uploads/2019/05/triami_wielershirt-300x300.jpg` (lege alt). Geen prijzen.
- Laatst gewijzigd feb 2023; controleren of Koffiedok/Bioracer nog kloppen.

### 3.9 Lidmaatschap (`/lidmaatschap-2/`)
Koppen: LIDMAATSCHAP, (Proef)lid worden, Tarieven 2025, Wij bieden:.
- Vrijblijvend 1 of 2 trainingen meedoen; **proeflidmaatschap: 10 weken alle trainingen en activiteiten voor €35,-**. Vragen via secretaris@triami.nl.
- Inschrijfformulier: ingebedde **Microsoft Forms** iframe (`https://forms.office.com/Pages/ResponsePage.aspx?id=7tsW9NdBGk2ozxeMbr7PRQwgd8BVLdNLmkOHyP_6nEtUM0oxVUVYUVg0U0I5VDYwNEFXQ0VIVVFHNC4u&embed=true`, 640x480).
- **Tarieven 2025**: vast bedrag, altijd incl. NTB-basislidmaatschap, jaarlijks vastgesteld op de ALV in januari. **Basislidmaatschap €193,- per jaar = €144,- Triami + €51,50 NTB**. **Atletenlicentie NTB €35,- optioneel**, zelf aanvragen via `http://mijn.triathlonbond.nl`. **Donateur min. €25,-**.
- "Wij bieden": vier trainingsmomenten per week; gediplomeerde trainers, afgestemd op ambitie en niveau; teamcompetities; sociale contacten, samen deelnemen aan triathlons, duathlons, zwemlopen, crosslopen en eigen evenementen; sociale activiteiten: trainingsweekend, Triami Club Competitie, eigen Triami triathlon, **zomerbarbecue**; NTB-lidmaatschap voordeliger via vereniging; verzekering via NTB (beperkte aansprakelijkheid en ongevallen); optionele atletenlicentie (voordelig bij >3 NTB-evenementen per jaar).
- Afbeelding: `uploads/2019/12/teamcompetitie.jpg` (lege alt).
- Verouderd/slordig: kop "Tarieven 2025" (nu 2026); typefout "natuurlijke aan de evenementen"; "€35,-" bij proeflidmaatschap botst met "€50" op Start2Tri-pagina.

### 3.10 Start2Tri (`/start2tri/`)
Koppen: START2TRI, Je 1e triathlon, Voor wie, Wat kun je verwachten, Praktisch.
- Kennismaken met triathlon; programma van **5 weken** met Start2Tri-clinics + reguliere trainingen, daarna **5 weken meetrainen als proeflid**, eventueel lid worden. Zwemmen, fietsen, lopen én wisselen; zonder prestatiedruk.
- Mogelijk eindpunt: **Triami Sprint Triatlon op zondag 3 mei 2025 in Deventer (1/16e triathlon)** (link `https://www.triathlondeventer.nl/`), optioneel.
- Voor wie: enige sportieve basis (min. één discipline); **minimumleeftijd 18 jaar**; beginners en licht ervaren sporters.
- Verwachten: gezamenlijke momenten (zwemmen, wisseltraining, parcoursverkenning), reguliere trainingen, ervaren trainers, persoonlijke aandacht.
- Praktisch: **periode eind maart – mei 2025**; **kosten €50 (3 maanden proeflidmaatschap Triami + NTB)**; **5–10 deelnemers**; aanmelden via www.triami.nl, kies proeflidmaatschap.
- Afbeelding: `uploads/2026/03/ChatGPT-Image-5-mrt-2026-21_29_18.png` (AI-gegenereerd, lege alt, portrait 683x1024).
- Verouderd: data 2025 (pagina zelf gewijzigd maart 2026); tekst is per woord in losse spans geplakt (copy-paste uit Word) – slordige HTML.

### 3.11 FAQ (`/faq/`)
Secties: Lidmaatschap, NTB licentie, Communicatie (Elementor-accordeons).
- Intro: vragen aan secretaris@triami.nl.
- **Lid worden**: inschrijf- en machtigingsformulier invullen, ondertekenen, digitaal naar secretaris; formulier op pagina Lidmaatschap. Later in het jaar lid: contributie naar rato; Triami-deel alleen voor de maanden lid; **NTB vanaf 1 september 50% korting, vanaf 1 november 75% korting**.
- **Contributie**: contributiejaar 1 jan – 31 dec, incl. NTB-basislidmaatschap, jaarlijks vastgesteld op de ALV; actuele bedragen op pagina lidmaatschap.
- **Wanneer afgeschreven?**: jaarlijks in het voorjaar in 1 termijn via incassomachtiging; penningmeester informeert vooraf; ook latere instromers in 1x.
- **Opzeggen**: vóór **30 november** per e-mail aan secretaris@triami.nl; bevestiging per e-mail; lidmaatschap stopt per 31 december.
- **Per direct opzeggen**: in principe niet mogelijk; alleen met zwaarwegende argumenten, bestuur oordeelt.
- **Tijdelijk stopzetten**: alleen bij onmacht (breuk, operatie), medische verklaring nodig, minimaal 3 maanden.
- **Inschrijfkosten**: geen.
- **NTB**: aangesloten bij de Nederlandse Triathlon Bond (link `https://www.triathlonbond.nl/`), overkoepelende bond multidisciplinaire duursporten, lid van NOC*NSF, ETU en ITU.
- **Basislicentie**: inbegrepen; verzekering (beperkte aansprakelijkheid en ongevallen) tijdens trainingen en wedstrijden; 6x per jaar magazine 'Transition'; bij NTB-wedstrijden daglicentiekosten.
- **Atletenlicentie**: geen daglicentiekosten; voordelig bij 3+ NTB-wedstrijden per seizoen; **verplicht voor teamcompetitie en NK's**; aanvragen via mijn.triathlonbond.nl; stopt automatisch per 31-12, jaarlijks zelf verlengen; afspraken NTB met KNWU, KNZB, Atletiekunie (link `https://www.triathlonbond.nl/leden/vragen-over-lidmaatschap/`).
- **Atletenlicentie opzeggen**: stopt automatisch per 31-12.
- **Spond**: communicatie over trainingen/evenementen; toegang vragen via invite `https://spond.com/invite/WFYQG`.
- **Nieuwsbrief**: e-mailnieuwsbrief (uitslagen/standen clubcompetitie, bestuursmededelingen, aankondigingen trainingsweekend, wedstrijdverslagen); niet ontvangen → secretaris@triami.nl.
- **WhatsApp**: aparte, vrijwillige app-groep voor sociale communicatie "en soms gewoon slap geouwehoer".
- **Strava**: club `https://www.strava.com/clubs/triami` (plus een "latest rides"-feedlink naar club-id 101737).
- Placeholders: **"Empty"** 3x (lege accordeon-items vóór "Lid worden", vóór "Basislicentie" en in sectie Lidmaatschap), **"Titel accordeon" / "Inhoud accordeon"** onder Communicatie. Verder: "Ledervergadering" (typefout), formulier-instructie (ondertekend formulier) strijdt met het online MS Forms-formulier, "Transition"-magazine controleren.

### 3.12 Nieuws (`/nieuws/`)
- Pagina bestaat (gewijzigd dec 2019) maar toont alleen titel NIEUWS, menu, footer en zijbalk "Geen categorieën". **0 berichten**: `wp-json/wp/v2/posts` geeft een lege lijst met `X-WP-Total: 0`. Niet in het menu gelinkt.

### 3.13 Vertrouwenscontactpersoon (`/vertrouwenscontactpersoon/`)
- Triami wil laagdrempelig en veilig zijn; trainers en bestuur gecommitteerd aan gedragsregels veilig en vertrouwd sporten.
- Bij (vermoeden van) grensoverschrijdend gedrag: **Leoniek Damman-Vrielink**, getoond adres **vertrouwenscontactpersoon@triami.nl**, maar de mailto-link verwijst naar **vcp@triami.nl** (inconsistentie). Leoniek is historicus en actief sporter bij de vereniging; onafhankelijk, vertrouwelijk luisterend oor, verwijst zo nodig door.
- Ook: vertrouwenscontactpersonen NOC*NSF via `https://centrumveiligesport.nl/doelgroepen/sporters`.
- Geen afbeeldingen. Laatst gewijzigd feb 2025.

### 3.14 Wedstrijden (`/wedstrijden/`)
- Niet te laden (fout bij de site); komt ook niet voor in de REST-paginalijst. Bestaat niet.

## 4. Nieuwsberichten
- Aantal: **0**. De REST API geeft geen enkel bericht (`X-WP-Total: 0`), de nieuwspagina is leeg. Er zijn geen categorieën. Alle "nieuws" loopt kennelijk via de e-mailnieuwsbrief en Spond.

## 5. Externe koppelingen en widgets

| Koppeling | Waar | Vorm |
|---|---|---|
| Microsoft Forms (inschrijfformulier) | Lidmaatschap | iframe-embed |
| Spond | Trainingen (tekst), FAQ | invite-link `https://spond.com/invite/WFYQG` |
| Strava | FAQ | links `strava.com/clubs/triami` en latest-rides feed club 101737 |
| triathlondeventer.nl | Vereniging, Start2Tri | tekstlinks (Triami Sprint Triathlon / mini-triathlon Keizerslanden) |
| NTB | Lidmaatschap, FAQ | `triathlonbond.nl`, `mijn.triathlonbond.nl`, vragen-over-lidmaatschap |
| teamcompetities.nl | Teamcompetitie | tekstlink |
| NOC*NSF | Trainers, VCP | `nocnsf.nl/high5-stappenplan/kennisbank`, `centrumveiligesport.nl/doelgroepen/sporters` |
| Koffiedok | Clubkleding | `koffiedok.nl/contact/` |
| Bioracer | Clubkleding | alleen genoemd, geen link |
| Facebook / Instagram | nergens | geen links of iconen; Instagram Feed-plugin is wel geïnstalleerd maar toont niets |
| PDF's | Footer, Bestuur | privacystatement.pdf, statuten_akte-van-oprichting_18-5-2006.pdf, Huishoudelijk-reglement-vastgesteld-19.1.2025.pdf |
| E-mailadressen | diverse | secretaris@, voorzitter@, penningmeester@, algemeenbestuurslid@, vertrouwenscontactpersoon@ / vcp@triami.nl |

## 6. Beoordeling

**1-op-1 mee (feiten kloppen of zijn recent bevestigd):**
- Bestuur: namen, functies, e-mailadressen, bank/BIC/KvK/NTB-nummer, links statuten en huishoudelijk reglement (nov 2025).
- Trainingsschema (zwemmen di De Scheg 19:30, do Borgelerbad 20:45, hardlopen wo AV Daventria 19:30, fietsen informeel) en de regels rond feestdagen/zomerstop/Spond.
- Vertrouwenscontactpersoon (naam, tekst, NOC*NSF-link) – wel het e-mailadres eenduidig maken.
- Tarieven en lidmaatschapsvormen (€193 / €144 + €51,50 / €35 licentie / €35 proef / €25 donateur) mits bevestigd voor 2026.
- FAQ-inhoud over contributie, opzeggen (vóór 30 november), incasso, NTB-licenties, Spond/Strava/nieuwsbrief/WhatsApp.
- Clubcompetitie: puntentelling en onderdelen.
- PDF's: privacyverklaring, statuten, huishoudelijk reglement.

**Herschrijven:**
- Homepage: nu alleen een hero met één knop; moet een echte landingspagina worden (wie we zijn, trainingen, proeflid worden, Start2Tri, contact, socials).
- Vereniging: tekst is prima als basis, maar ledental en teamaantallen actualiseren, logo-citaat redigeren.
- Start2Tri: generiek maken (zonder jaartal) of jaarlijks bijwerken; data 2025 eruit; AI-afbeelding vervangen door echte foto; €50 vs. €35 proeflidmaatschap uitleggen.
- Teamcompetitie: teams, divisies en captains actualiseren (tekst zegt 2 herenteams, pagina toont 4 teams); foto's uit 2019 vervangen.
- Trainers: naamloze "in opleiding"-blokken weg, schrijfwijze gelijktrekken, eventueel foto's.
- Clubcompetitie: 6 vs. 7 resultaten oplossen; kalender/standen toevoegen of expliciet naar nieuwsbrief verwijzen.
- FAQ: placeholders ("Empty", "Titel accordeon") verwijderen; "ondertekend formulier" afstemmen op het online MS Forms-formulier; typefouten.
- Lidmaatschap: "Tarieven 2025" → actueel jaar; "vier trainingsmomenten" afstemmen op schema (drie vaste).
- Clubkleding: controleren of Koffiedok en Bioracer nog kloppen; link naar webshop toevoegen.

**Kan vervallen:**
- Nieuwspagina (0 berichten sinds 2019) – tenzij het bestuur echt nieuws wil gaan plaatsen.
- Aparte subpagina "Huishoudelijk reglement" (gewoon directe PDF-link op Bestuur).
- Instagram Feed-plugin, WooCommerce-CSS, Hestia/ThemeIsle-credit, Elementor-afhankelijkheid.
- Headerfoto's uit 2019/2020 en Facebook-exports van teams (vervangen door recent beeld).

**Ontbreekt en moet bij het bestuur worden opgehaald:**
1. Actuele tarieven 2026 (ALV januari 2026) en bevestiging proeflidmaatschap €35 vs. Start2Tri €50.
2. Actuele teamcompetitie-indeling 2026: welke teams, divisies, captains.
3. Trainersbestand: volledige lijst, wie zijn de trainers in opleiding, toestemming voor namen/foto's; achternamen bestuur en trainers (of bewust alleen voornamen).
4. Juiste e-mailadres VCP (vertrouwenscontactpersoon@ of vcp@triami.nl) en of Leoniek nog VCP is.
5. Jaarschema zwemmen (wordt genoemd, nergens gepubliceerd) en de exacte zomerstop-periode; klopt "vier trainingsmomenten"?
6. Start2Tri-editie 2026/2027: data, kosten, aanmeldroute.
7. Clubcompetitie-kalender en actuele standen; definitief aantal tellende resultaten (6 of 7).
8. Clubkleding: huidige leverancier, webshop-URL, prijzen, pasmogelijkheid.
9. Social media: bestaan er Facebook-/Instagram-accounts die gelinkt moeten worden? Strava-club bevestigen.
10. Nieuws/agenda: wil het bestuur een nieuws- of agendafunctie op de site, of blijft dat nieuwsbrief/Spond?
11. Recente foto's (trainingen, teams, evenementen) met toestemming; eventueel ledental 2026.
12. Privacyverklaring: datum/versie controleren (PDF op root, zonder datum in de naam); contactpersoon AVG.
13. Relatie met triathlondeventer.nl (Triami Sprint Triathlon / mini-triathlon Keizerslanden): eigen evenement, hoe presenteren?
