# Huisstijl- en designsysteemvoorstel – Triami Triathlonvereniging Deventer

*Afgeleid uit de aangeleverde logobestanden (analyse 4 november 2026).*

## 1. Inventarisatie logobestanden

Belangrijkste bevinding vooraf: **alle vijf bestanden met de extensie `.png` zijn in werkelijkheid JPEG-bestanden** (JFIF-header, geen alfakanaal). Er is dus geen enkele transparante rasterversie. De twee PDF's zijn wél echte vectorbestanden (Serif Affinity, maart 2019; tekst is omgezet naar paden, geen ingesloten fonts of bitmaps).

| Bestand (origineel) | Wat is het | Afmeting | Formaat/kleurruimte | Geschikt voor web |
|---|---|---|---|---|
| `logo.jpg` | Oud logo, breed, wit vlak | 432 × 114 px, 88 dpi | JPEG RGB | Nee – oud ontwerp, laag, wazig |
| `Triami logo oud.jpg` | Oud logo, breed, veel witruimte | 743 × 223 px, 72 dpi | JPEG RGB | Nee – archief/historie |
| `Triami logo nieuw.jpg` | Nieuw logo kleur, **compact** (beeldmerk boven, woordmerk eronder) | 780 × 430 px, 300 dpi | JPEG **CMYK** | Beperkt – CMYK geeft in browsers kleurafwijking; alleen na conversie naar sRGB |
| `Triami logo nieuw1.jpg` | Nieuw logo kleur, **breed** (beeldmerk links, woordmerk rechts) | 1349 × 430 px, 300 dpi | JPEG CMYK | Beperkt – idem; beste bron voor header na conversie |
| `Triami logo nieuw.png` | Nieuw logo kleur, breed, op **zwarte** achtergrond; woordmerk is zwart en dus onzichtbaar | 1349 × 430 px | JPEG (geen PNG!) RGB | Nee – woordmerk valt weg; vermoedelijk exportfout |
| `Triami logo nieuw96px.png` | Idem, verkleind | 301 × 96 px | JPEG RGB | Nee – zelfde fout, te klein |
| `Triami logo nieuw  white.png` | Nieuw logo **wit** (diapositief) op zwart, compact | 780 × 430 px | JPEG RGB | Ja voor donkere footer, mits achtergrond exact `#000000`; geen transparantie |
| `Triami logo nieuw  white1.png` | Nieuw logo wit op zwart, breed | 1349 × 430 px | JPEG RGB | Ja voor donkere footer/header-dark; zelfde beperking |
| `Triami logo nieuw bw.jpg` | Nieuw logo **zwart-wit**, compact | 780 × 430 px, 300 dpi | JPEG CMYK | Print/zw-w drukwerk; web alleen na sRGB-conversie |
| `Triami logo nieuw bw 1.jpg` | Nieuw logo zwart-wit, breed | 1349 × 430 px, 300 dpi | JPEG CMYK | Idem |
| `Triami logo wide.pdf` | Nieuw logo kleur, breed, **vector** | 323,8 × 103 pt | PDF (Affinity), paden | **Beste bron** – kan verliesvrij naar SVG/PNG elke maat |
| `Triami logo small.pdf` | Nieuw logo kleur, compact, **vector** | 187,2 × 103 pt | PDF (Affinity), paden | **Beste bron** voor favicon/og-image/social |

Het nieuwe logo bestaat uit: een rode hartslaglijn (ECG) die rechts uitloopt in een lichtrode "staart", een zwart vlak met daarin een rode zwemmer, en daarboven een zwarte fietser en loper; woordmerk "TRIAMI" in zware schreefloze kapitalen met daaronder "TRIATHLONVERENIGING DEVENTER" in lichte kapitalen.

## 2. Gemeten kleuren

Methode: Python (PIL + numpy), dominante kleuren per bestand; de vector-PDF op 300 dpi gerasterd en de SVG-export gelezen voor de exacte vulkleuren.

| Kleur | Hex (uit vector-PDF, sRGB) | Opmerking |
|---|---|---|
| **Triami-rood** | `#ED1E24` | rgb(237, 30, 36) – exacte vulkleur van hartslaglijn, zwemmer en TRIAMI-accent. De CMYK-JPG's tonen na naïeve conversie `#FE0605`; dat is een conversie-artefact, niet de bedoelde kleur. De oude logo's gebruikten iets donkerder `#D22931`–`#DB232B`. |
| **Zwart** | `#000000` | Woordmerk, fietser, loper (zuiver zwart in de vector) |
| **Bijna-zwart** | `#070605` | Het zwarte "bergvlak" achter de zwemmer, warm-zwart |
| **Lichtrood (staart)** | `#F36B6F` | Uitloper van de hartslaglijn rechts (ca. 60 % tint van het rood) |
| **Grijs (diapositief)** | `#A5A5A5` | Staart in de witte variant |
| Wit | `#FFFFFF` | Achtergrond |

## 3. Compact designsysteem

### 3.1 Kleurenpalet

| Rol | Naam (slug) | Hex | Gebruik |
|---|---|---|---|
| Primair | `triami-rood` | `#ED1E24` | Knoppen, links, actieve nav, accentlijnen (de hartslaglijn als motief) |
| Primair donker | `triami-rood-donker` | `#C4151B` | Hover/active-state van knoppen, tekstlinks op licht (contrast 5,2:1 op wit) |
| Primair licht | `triami-rood-licht` | `#F36B6F` | Decoratief (staart-motief), badges, iconen op donker |
| Primair tint | `triami-rood-tint` | `#FDE8E8` | Achtergrond van uitgelichte blokken, meldingen |
| Secundair | `triami-zwart` | `#111111` | Koppen, footer-achtergrond, donkere secties (iets zachter dan #000 voor schermgebruik) |
| Tekst | `tekst` | `#1F1F1F` | Bodytekst op licht |
| Tekst gedempt | `tekst-gedempt` | `#5C5C5C` | Metadata, datums, bijschriften (contrast 6,6:1) |
| Lijn | `lijn` | `#DFDFDF` | Borders, scheidingslijnen, tabellen |
| Achtergrond zacht | `achtergrond-zacht` | `#F4F4F4` | Afwisselende secties, kaarten |
| Achtergrond | `wit` | `#FFFFFF` | Paginabasis |
| Accent (optioneel) | `water-blauw` | `#0E7490` | Alleen voor functionele kleurcodering (bv. zwemmen/fietsen/lopen in trainingsschema). Niet in het logo; spaarzaam gebruiken. |

Regels: rood is een *accentkleur*, geen vlakkleur – grote vlakken zijn wit, lichtgrijs of zwart; rood alleen voor actie en het hartslagmotief. Witte tekst op `#ED1E24` haalt 4,0:1 (alleen voor grote/vette tekst, bv. knoppen ≥ 16 px bold); voor kleine witte tekst op rood `#C4151B` gebruiken.

### 3.2 Typografie (Google Fonts)

| Rol | Font | Motivatie |
|---|---|---|
| Koppen, nav, knoppen | **Montserrat** (gewichten 700/800, kapitalen met `letter-spacing: 0.02em` voor H1/H2) | Brede, geometrische schreefloze met dezelfde "stevige kapitalen"-uitstraling als het woordmerk TRIAMI; oogt sportief en modern zonder agressief te worden. Werkt uitstekend in grote cijfers (afstanden, tijden, data van wedstrijden). |
| Bodytekst, formulieren | **Source Sans 3** (gewichten 400/600) | Humanistische schreefloze die dicht bij de onderregel "TRIATHLONVERENIGING DEVENTER" ligt (Gill Sans-achtig), zeer goed leesbaar bij 16–18 px, compact (veel tekst per regel in schema's en nieuwsberichten), licht in bestandsgrootte. Contrasteert net genoeg met Montserrat. |

Schaal (basis 16 px, factor ~1,25): 14 / 16 / 18 / 20 / 25 / 31 / 39 / 49 px. Regelafstand body 1,6; koppen 1,15. Alleen `woff2` laden met `font-display: swap`, of lokaal hosten (AVG).

### 3.3 Spacing, radius, overige tokens

- **Spacing-schaal** (basis 4 px): 4, 8, 12, 16, 24, 32, 48, 64, 96 px. Secties verticaal 64 px (mobiel 48), contentbreedte 1200 px, brede uitlijning 1400 px, leesbreedte tekst 720 px.
- **Radius**: 4 px (inputs, tags), 8 px (kaarten, knoppen), 999 px (pills/badges). Geen grote afrondingen: het logo is hoekig en scherp.
- **Lijnen**: 1 px `#DFDFDF`; accentlijn 4 px `#ED1E24` (bv. links van citaten of onder actieve nav – verwijst naar de hartslaglijn).
- **Schaduw**: zeer terughoudend, `0 2px 8px rgba(0,0,0,.08)` op kaarten.
- **Knoppen**: primair rood/wit, bold, 12 × 24 px padding, radius 8; secundair outline zwart; op donkere achtergrond wit/zwart.
- **Motief**: een horizontale hartslaglijn (uit de SVG geknipt) als sectiescheiding of in de hero; één keer per pagina, niet als behang.

### 3.4 Logogebruik per plek

| Plek | Variant | Bestand in `assets/logo/` |
|---|---|---|
| Header (lichte achtergrond) | Kleur, breed, hoogte 56–64 px (mobiel 44 px) | `triami-logo-kleur-breed-AFGELEID.svg` (voorkeur) of `triami-logo-kleur-breed.jpg` na sRGB-conversie |
| Header gekrompen/mobiel | Kleur, compact of alleen beeldmerk | `triami-logo-kleur-compact-AFGELEID.svg` |
| Footer (donker `#111111`) | Wit diapositief, breed | `triami-logo-wit-breed.png` – let op: achtergrond is ingebakken zwart `#000`; footer dus exact zwart maken óf (beter) een echte transparante witte versie laten aanmaken |
| Favicon / app-icoon | Alleen beeldmerk (hartslaglijn + zwemmer/fietser/loper) uit de compacte vector, 512 × 512 op wit of rood, 32/180/512 px | Af te leiden uit `triami-logo-kleur-compact-vector.pdf` |
| og-image / social (1200 × 630) | Compacte kleurvariant gecentreerd op wit, of wit diapositief op `#ED1E24` | Af te leiden uit `triami-logo-kleur-compact-vector.pdf` |
| Zwart-wit (print, e-mailhandtekening grijs) | Zwart-wit breed | `triami-logo-zw-breed.jpg` |
| Oude logo's | Niet gebruiken, alleen archief | niet gekopieerd |

## 4. Wat ontbreekt of opnieuw aangeleverd moet worden

1. **Officieel SVG-bestand** van beide logovarianten (breed en compact) in sRGB, geëxporteerd uit het Affinity-bronbestand. De twee SVG's in `assets/logo/` met suffix `-AFGELEID` zijn door mij uit de PDF's gegenereerd (pdftocairo); ze zijn bruikbaar maar niet "gezegend" door de ontwerper en kunnen een verborgen witte achtergrondrechthoek bevatten.
2. **Transparante PNG's** (echt PNG, RGBA) op minimaal 2000 px breed: kleur, wit en zwart. Nu bestaat geen enkele transparante versie; de "PNG's" zijn hernoemde JPEG's.
3. **Los beeldmerk** (zonder woordmerk) als SVG/PNG voor favicon, app-icoon en social-avatar. Nu alleen als onderdeel van het complete logo beschikbaar.
4. **Witte variant met rode hartslaglijn** (rood op donker): voor een footer in zwart zou rood + wit het logo herkenbaarder houden dan volledig wit. Bestaat nu niet.
5. **sRGB-versies van de CMYK-JPG's** (of gewoon vervangen door punt 2). De CMYK-bestanden geven in browsers en op Android een afwijkend, fel oranjerood.
6. Herstel van `Triami logo nieuw.png` / `…96px.png`: woordmerk valt weg op zwart; deze bestanden kunnen vervallen.
7. Het Affinity-bronbestand (`.afdesign`) zelf, zodat toekomstige exports niet afhankelijk zijn van de PDF.

## 5. Gekopieerde logovarianten (`assets/logo/`)

Alle bestanden zijn ongewijzigde kopieën van de originelen (behalve de twee als AFGELEID gemarkeerde SVG's):

| Nieuwe naam | Origineel | Waarom gekozen |
|---|---|---|
| `triami-logo-kleur-breed-vector.pdf` | `Triami logo wide.pdf` | Enige verliesvrije bron, brede variant |
| `triami-logo-kleur-compact-vector.pdf` | `Triami logo small.pdf` | Enige verliesvrije bron, compacte variant |
| `triami-logo-kleur-breed-AFGELEID.svg` | uit `Triami logo wide.pdf` | Direct bruikbaar als header-logo tot een officiële SVG er is |
| `triami-logo-kleur-compact-AFGELEID.svg` | uit `Triami logo small.pdf` | Basis voor favicon/og-image |
| `triami-logo-kleur-breed.jpg` | `Triami logo nieuw1.jpg` | Hoogste resolutie raster kleur, breed (CMYK!) |
| `triami-logo-kleur-compact.jpg` | `Triami logo nieuw.jpg` | Hoogste resolutie raster kleur, compact (CMYK!) |
| `triami-logo-wit-breed.png` | `Triami logo nieuw  white1.png` | Diapositief voor donkere footer (eigenlijk JPEG) |
| `triami-logo-wit-compact.png` | `Triami logo nieuw  white.png` | Diapositief compact (eigenlijk JPEG) |
| `triami-logo-zw-breed.jpg` | `Triami logo nieuw bw 1.jpg` | Zwart-wit, breed |
| `triami-logo-zw-compact.jpg` | `Triami logo nieuw bw.jpg` | Zwart-wit, compact |
| `triami-logo-kleur-breed-zwartbg.png` | `Triami logo nieuw.png` | Alleen ter referentie (woordmerk onzichtbaar); niet gebruiken |

Niet gekopieerd: `logo.jpg`, `Triami logo oud.jpg` (oud ontwerp), `Triami logo nieuw96px.png` (defect en te klein).

## 6. `theme.json`-fragment (WordPress, versie 3)

```json
{
  "$schema": "https://schemas.wp.org/trunk/theme.json",
  "version": 3,
  "settings": {
    "color": {
      "defaultPalette": false,
      "defaultGradients": false,
      "palette": [
        { "slug": "triami-rood",        "color": "#ED1E24", "name": "Triami rood" },
        { "slug": "triami-rood-donker", "color": "#C4151B", "name": "Triami rood donker" },
        { "slug": "triami-rood-licht",  "color": "#F36B6F", "name": "Triami rood licht" },
        { "slug": "triami-rood-tint",   "color": "#FDE8E8", "name": "Triami rood tint" },
        { "slug": "triami-zwart",       "color": "#111111", "name": "Triami zwart" },
        { "slug": "tekst",              "color": "#1F1F1F", "name": "Tekst" },
        { "slug": "tekst-gedempt",      "color": "#5C5C5C", "name": "Tekst gedempt" },
        { "slug": "lijn",               "color": "#DFDFDF", "name": "Lijn" },
        { "slug": "achtergrond-zacht",  "color": "#F4F4F4", "name": "Achtergrond zacht" },
        { "slug": "wit",                "color": "#FFFFFF", "name": "Wit" },
        { "slug": "water-blauw",        "color": "#0E7490", "name": "Water blauw (functioneel)" }
      ]
    },
    "typography": {
      "fluid": true,
      "fontFamilies": [
        {
          "slug": "kop",
          "name": "Montserrat",
          "fontFamily": "\"Montserrat\", \"Helvetica Neue\", Arial, sans-serif",
          "fontFace": [
            { "fontFamily": "Montserrat", "fontWeight": "700", "fontStyle": "normal", "fontDisplay": "swap", "src": [ "file:./assets/fonts/montserrat-700.woff2" ] },
            { "fontFamily": "Montserrat", "fontWeight": "800", "fontStyle": "normal", "fontDisplay": "swap", "src": [ "file:./assets/fonts/montserrat-800.woff2" ] }
          ]
        },
        {
          "slug": "tekst",
          "name": "Source Sans 3",
          "fontFamily": "\"Source Sans 3\", \"Segoe UI\", Arial, sans-serif",
          "fontFace": [
            { "fontFamily": "Source Sans 3", "fontWeight": "400", "fontStyle": "normal", "fontDisplay": "swap", "src": [ "file:./assets/fonts/source-sans-3-400.woff2" ] },
            { "fontFamily": "Source Sans 3", "fontWeight": "400", "fontStyle": "italic", "fontDisplay": "swap", "src": [ "file:./assets/fonts/source-sans-3-400-italic.woff2" ] },
            { "fontFamily": "Source Sans 3", "fontWeight": "600", "fontStyle": "normal", "fontDisplay": "swap", "src": [ "file:./assets/fonts/source-sans-3-600.woff2" ] }
          ]
        }
      ],
      "fontSizes": [
        { "slug": "small",    "size": "0.875rem", "name": "Klein" },
        { "slug": "medium",   "size": "1rem",     "name": "Normaal" },
        { "slug": "large",    "size": "1.25rem",  "name": "Groot" },
        { "slug": "x-large",  "size": "1.5625rem","name": "Extra groot" },
        { "slug": "xx-large", "size": "2.4rem",   "name": "Kop" },
        { "slug": "huge",     "size": "3rem",     "name": "Hero" }
      ]
    },
    "spacing": {
      "units": [ "px", "rem", "%", "vw" ],
      "spacingSizes": [
        { "slug": "10", "size": "0.25rem", "name": "4" },
        { "slug": "20", "size": "0.5rem",  "name": "8" },
        { "slug": "30", "size": "1rem",    "name": "16" },
        { "slug": "40", "size": "1.5rem",  "name": "24" },
        { "slug": "50", "size": "2rem",    "name": "32" },
        { "slug": "60", "size": "3rem",    "name": "48" },
        { "slug": "70", "size": "4rem",    "name": "64" },
        { "slug": "80", "size": "6rem",    "name": "96" }
      ]
    },
    "layout": { "contentSize": "720px", "wideSize": "1200px" }
  },
  "styles": {
    "color": { "background": "var(--wp--preset--color--wit)", "text": "var(--wp--preset--color--tekst)" },
    "typography": { "fontFamily": "var(--wp--preset--font-family--tekst)", "fontSize": "var(--wp--preset--font-size--medium)", "lineHeight": "1.6" },
    "elements": {
      "heading": { "typography": { "fontFamily": "var(--wp--preset--font-family--kop)", "fontWeight": "800", "lineHeight": "1.15" }, "color": { "text": "var(--wp--preset--color--triami-zwart)" } },
      "link": { "color": { "text": "var(--wp--preset--color--triami-rood-donker)" }, ":hover": { "color": { "text": "var(--wp--preset--color--triami-rood)" } } },
      "button": {
        "color": { "background": "var(--wp--preset--color--triami-rood)", "text": "var(--wp--preset--color--wit)" },
        "typography": { "fontFamily": "var(--wp--preset--font-family--kop)", "fontWeight": "700" },
        "border": { "radius": "8px" },
        ":hover": { "color": { "background": "var(--wp--preset--color--triami-rood-donker)" } }
      }
    }
  }
}
```

## Beslispunten

1. Akkoord met `#ED1E24` als officieel Triami-rood (vectorwaarde) in plaats van het fellere `#FE0605` uit de CMYK-JPG's?
2. Montserrat + Source Sans 3 als fontpaar, of liever één familie (bv. alleen Montserrat) voor eenvoud?
3. Footer: nu met wit-op-zwart-JPEG (footer exact `#000000`), of eerst een transparante witte PNG/SVG laten aanleveren?
4. Ontwerper/bronbestand benaderen voor punt 1–4 uit hoofdstuk 4 (SVG, transparante PNG's, los beeldmerk)?
5. Optionele functionele accentkleur `water-blauw` opnemen of palet strikt rood/zwart/wit houden?
