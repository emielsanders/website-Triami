"""Maakt docs/feedbackboek-<datum>.pdf: elke pagina een groot nummer rechtsboven,
zodat het bestuur per nummer feedback kan geven. Gebruikt schermafbeeldingen uit
/home/claude/pg/pdfshots (zie pg/shots_pdf.py)."""
import asyncio, base64, html, json, os, re, sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SHOTS = Path(sys.argv[1] if len(sys.argv) > 1 else "/home/claude/pg/pdfshots")
DATUM = "4 november 2026"
OUT = ROOT / "docs" / "feedbackboek-2026-11-04.pdf"
HTML = ROOT / "dist" / "feedbackboek.html"
CHUNKS = ROOT / "dist" / "chunks"; CHUNKS.mkdir(parents=True, exist_ok=True)

# Desktop: 1280 css px over 186 mm -> hoogte per vel ~ 1540 css px (= 3080 px @2x)
DESK_CHUNK = 3080
# Mobiel: 390 css px over 58 mm, 3 kolommen per vel -> 1540 css px (= 3080 px @2x)
MOB_CHUNK = 3080

PAGINAS = [
    ("home", "Home", "/", "Eerste indruk, de vier kernboodschappen, het trainingsschema en de aanmeldroute (proeflid)."),
    ("vereniging", "Vereniging", "/vereniging/", "Wie we zijn, geschiedenis, NTB-lidmaatschap, Spond en Strava."),
    ("bestuur", "Bestuur", "/bestuur/", "Bestuursleden met foto en mailadres; statuten en huishoudelijk reglement; KvK-gegevens."),
    ("trainers", "Trainers", "/trainers/", "Overzicht trainers en hun NTB-licentie."),
    ("teamcompetitie", "Teamcompetitie", "/teamcompetitie/", "Teams in de NTB-teamcompetitie, captains en hoe je meedoet."),
    ("clubcompetitie", "Clubcompetitie", "/clubcompetitie/", "Interne competitie: telling, wedstrijden en Triami Sprint Triathlon."),
    ("clubkleding", "Clubkleding", "/clubkleding/", "Wedstrijd- en trainingskleding bestellen."),
    ("vertrouwenscontactpersoon", "Vertrouwenscontactpersoon", "/vertrouwenscontactpersoon/", "Wat de VCP doet en hoe je haar bereikt."),
    ("trainingen", "Trainingen", "/trainingen/", "Weekschema zwemmen, hardlopen en fietsen; niveau en meetrainen."),
    ("start2tri", "Start2Tri", "/start2tri/", "Beginnersprogramma: opzet, kosten en aanmelden."),
    ("lidmaatschap", "Lidmaatschap", "/lidmaatschap/", "Proeflid, tarieven en het inschrijfformulier (Microsoft Forms)."),
    ("faq", "Veelgestelde vragen", "/faq/", "Uitklapbare antwoorden op vragen van nieuwe leden."),
    ("contact", "Contact", "/contact/", "Mailadressen bestuur, VCP, trainingslocaties, Spond/Strava, gegevens."),
    ("nieuws", "Nieuws", "/nieuws/", "Berichtenoverzicht; nu leeg. Besluit bestuur: gebruiken of weglaten."),
    ("bestaat-niet", "Foutpagina (404)", "/een-oude-link/", "Wat een bezoeker ziet bij een verouderde of verkeerde link."),
]

COMPONENTEN = [
    ("c-header", "Kopbalk (desktop)", "Logo, menu met submenu Vereniging, knop Word proeflid. Blijft op elke pagina gelijk."),
    ("c-submenu", "Submenu Vereniging (open)", "Bestuur, Trainers, Teamcompetitie, Clubcompetitie, Clubkleding, Vertrouwenscontactpersoon."),
    ("menu-mobiel", "Menu op telefoon (open)", "Volledig scherm, zwart, submenu ingesprongen."),
    ("c-hero", "Openingsblok homepage", "Donker vlak, kop in Montserrat, twee knoppen, hartslaglijn als clubmotief."),
    ("c-intro-kaarten", "Kaart (voorbeeld)", "Witte kaart met rand en schaduw, gebruikt voor de vier kernboodschappen op de homepage."),
    ("c-trainingsschema", "Trainingsschema", "Kaart per training met pictogram, dag, tijd en locatie. Op telefoon onder elkaar."),
    ("c-cta-band", "Oproepbalk", "Donkerrode band met oproep om proeflid te worden; staat op Home en Trainingen."),
    ("c-persoon", "Persoonskaart", "Ronde foto, naam, functie en mailadres (Bestuur)."),
    ("c-tabel", "Tabel (tarieven)", "Zebra-strepen, kop in Montserrat; ook gebruikt voor trainers en bestuursgegevens."),
    ("c-faq-item", "Uitklapvraag (FAQ)", "Open- en dichtklappen zonder script; werkt ook met toetsenbord en voorleessoftware."),
    ("c-formulier", "Inschrijfformulier (Microsoft Forms)", "Ingebed in het Nederlands; op telefoon ook een link om het in een nieuw venster te openen."),
    ("c-check-bestuur", "Markering \"Check bestuur\"", "Lichtrode notitie op pagina's waar het bestuur iets moet bevestigen. Verdwijnt vóór livegang."),
    ("c-footer", "Voettekst", "Logo, korte tekst, Snel naar, Contact, KvK/NTB, Strava en Spond, privacyverklaring."),
]

def img64(p: Path) -> str:
    return "data:image/" + ("svg+xml" if p.suffix == ".svg" else "png") + ";base64," + base64.b64encode(p.read_bytes()).decode()

def font64(p: Path) -> str:
    return "data:font/woff2;base64," + base64.b64encode(p.read_bytes()).decode()

def chunk(name: str, h: int, first: int | None = None) -> list[Path]:
    """Knipt een lange schermafbeelding in gelijkmatige stukken van hoogstens h px;
    'first' begrenst het eerste stuk (dat naast uitleg op het blad staat)."""
    import math
    src = SHOTS / f"{name}.png"
    im = Image.open(src)
    grenzen = [0]
    if first and im.height > first:
        grenzen.append(first)
    rest = im.height - grenzen[-1]
    n = max(1, math.ceil(rest / h))
    stap = math.ceil(rest / n)
    for k in range(1, n):
        grenzen.append(grenzen[-1] + stap if k == 1 else grenzen[-1] + stap)
    grenzen.append(im.height)
    out = []
    for i, (a, b) in enumerate(zip(grenzen, grenzen[1:])):
        p = CHUNKS / f"{name}-{i}.png"
        im.crop((0, a, im.width, b)).save(p, optimize=True)
        out.append(p)
    return out

def checks() -> dict[str, list[str]]:
    d = {}
    for f in (ROOT / "content" / "pages").glob("*.html"):
        slug = re.search(r"^slug:\s*(\S+)", f.read_text(), re.M).group(1)
        d[slug] = [html.unescape(m) for m in re.findall(r'<p class="triami-check">(.*?)</p>', f.read_text(), re.S)]
    return d

CSS = """
@page { size: A4; margin: 0; }
@font-face { font-family: Montserrat; src: url(@@MONT@@) format('woff2'); font-weight: 700 800; }
@font-face { font-family: 'Source Sans 3'; src: url(@@SS@@) format('woff2'); font-weight: 400 600; }
:root { --rood:#ED1E24; --donker:#C4151B; --zwart:#111; --tekst:#1F1F1F; --gedempt:#5C5C5C; --lijn:#DFDFDF; --zacht:#F4F4F4; --tint:#FDE8E8; }
* { box-sizing: border-box; }
body { margin:0; font-family:'Source Sans 3', Arial, sans-serif; color:var(--tekst); font-size:10.5pt; line-height:1.45; }
.vel { width:210mm; height:297mm; padding:14mm 12mm 12mm; position:relative; page-break-after:always; overflow:hidden; background:#fff; }
.vel:last-child { page-break-after:auto; }
.nr { position:absolute; top:8mm; right:10mm; font:800 34pt Montserrat, Arial, sans-serif; color:#fff; background:var(--rood); min-width:22mm; height:22mm; padding:0 4mm; border-radius:4mm; display:flex; align-items:center; justify-content:center; letter-spacing:-.02em; }
.kop { position:absolute; top:9mm; left:12mm; font:700 8pt Montserrat, Arial, sans-serif; text-transform:uppercase; letter-spacing:.08em; color:var(--gedempt); }
.voet { position:absolute; bottom:7mm; left:12mm; right:12mm; font-size:8pt; color:var(--gedempt); border-top:1px solid var(--lijn); padding-top:2mm; display:flex; justify-content:space-between; }
h1,h2,h3 { font-family:Montserrat, Arial, sans-serif; font-weight:800; line-height:1.15; margin:0 0 3mm; text-wrap:balance; }
h1 { font-size:26pt; text-transform:uppercase; letter-spacing:.02em; }
h2 { font-size:17pt; text-transform:uppercase; letter-spacing:.02em; margin-top:14mm; }
h3 { font-size:12pt; margin-top:5mm; }
p { margin:0 0 2.5mm; }
.groot { font-size:13pt; }
.url { font-family: ui-monospace, Consolas, monospace; font-size:9.5pt; color:var(--donker); }
.inhoud { margin-top:14mm; }
.hart { height:4px; background:var(--rood); width:28mm; margin:0 0 5mm; }
.kader { border:1px solid var(--lijn); border-radius:3mm; padding:4mm 5mm; margin:3mm 0; background:#fff; }
.tint { background:var(--tint); border-color:#F5C2C4; }
.zacht { background:var(--zacht); }
ul,ol { margin:0 0 3mm; padding-left:5mm; } li { margin-bottom:1.2mm; }
table { border-collapse:collapse; width:100%; font-size:9.5pt; }
th,td { text-align:left; padding:1.8mm 2.5mm; border-bottom:1px solid var(--lijn); vertical-align:top; }
th { font-family:Montserrat, Arial, sans-serif; font-weight:700; font-size:8.5pt; text-transform:uppercase; letter-spacing:.05em; background:var(--zacht); }
.shot { border:1px solid var(--lijn); display:block; }
.desk { width:186mm; }
.mobkol { display:flex; gap:6mm; align-items:flex-start; }
.mobkol img { width:58mm; }
.lab { font:700 8pt Montserrat, Arial, sans-serif; text-transform:uppercase; letter-spacing:.06em; color:var(--gedempt); margin:0 0 2mm; }
.swatches { display:grid; grid-template-columns:repeat(4,1fr); gap:4mm; }
.sw { border:1px solid var(--lijn); border-radius:2mm; overflow:hidden; font-size:8.5pt; }
.sw div:first-child { height:16mm; }
.sw div:last-child { padding:2mm 2.5mm; }
.knop { display:inline-block; font:700 10pt Montserrat, Arial, sans-serif; padding:2.6mm 5mm; border-radius:2mm; margin:0 2mm 2mm 0; }
.k1 { background:var(--donker); color:#fff; } .k2 { border:2px solid var(--zwart); color:var(--zwart); } .k3 { border:2px solid #fff; color:#fff; }
.donker { background:var(--zwart); color:#fff; padding:5mm; border-radius:3mm; }
.twee { display:grid; grid-template-columns:1fr 1fr; gap:6mm; }
.form td { height:11mm; }
.form td:first-child { width:14mm; } .form td:last-child { width:34mm; }
.toc td:first-child { width:12mm; font:800 11pt Montserrat; color:var(--rood); }
.cover { background:var(--zwart); color:#fff; }
.cover .nr { display:none; } .cover .kop, .cover .voet { color:#aaa; border-color:#333; }
.cover h1 { font-size:34pt; color:#fff; margin-top:60mm; }
.cover p { color:#ddd; }
.hartlijn { width:100%; height:14mm; margin-top:20mm; }
.logo { height:16mm; }
"""

def vel(inhoud: str, nr: int, kop: str, extra_cls: str = "") -> str:
    return (f'<section class="vel {extra_cls}"><div class="kop">{html.escape(kop)}</div><div class="nr">{nr}</div>'
            f'<div class="inhoud">{inhoud}</div>'
            f'<div class="voet"><span>Triami — nieuwe website, feedbackversie {DATUM}</span><span>Geef feedback met het nummer rechtsboven · blad {nr}</span></div></section>')

def main():
    chk = checks()
    hart = (ROOT / "theme/triami/patterns/hartslaglijn.php").read_text()
    svg = re.search(r"<svg.*?</svg>", hart, re.S).group(0)
    logo = img64(ROOT / "theme/triami/assets/img/logo.svg")
    sheets: list[tuple[str, str, str]] = []  # (kop, inhoud, cls)
    toc: list[tuple[int, str]] = []

    def add(kop, inhoud, cls=""):
        sheets.append((kop, inhoud, cls))
        return len(sheets)

    # 0 omslag (blad 1)
    add("Omslag", f'<img class="logo" src="{logo}" style="filter:brightness(0) invert(1)"><h1>Nieuwe website<br>Triami</h1>'
        f'<p class="groot">Feedbackversie voor het bestuur — {DATUM}</p>'
        f'<p>Dit boek toont alle pagina\'s van de nieuwe site zoals ze nu in de demo staan, op computer en op telefoon, plus de huisstijl en de losse onderdelen. '
        f'Elk blad heeft rechtsboven een nummer. Noem dat nummer bij je opmerking, dan is meteen duidelijk waar het over gaat.</p>'
        f'<div class="hartlijn">{svg}</div>', "cover")

    # leeswijzer
    toc.append((add("Leeswijzer", """
<h1>Zo geef je feedback</h1><div class="hart"></div>
<p class="groot">Je hoeft niets te installeren en geen account te hebben. Blader door dit boek en noteer per opmerking het <strong>bladnummer rechtsboven</strong>.</p>
<div class="kader tint"><strong>Voorbeeld:</strong> "Blad 14 — bij Zwemmen donderdag staat Borgelerbad, maar dat is sinds 2025 De Scheg." <br>of: "Blad 6 — de kop vind ik te stellig, liever 'Samen trainen in Deventer'."</div>
<h3>Waar je op kunt letten</h3>
<ul>
<li><strong>Klopt het?</strong> Tijden, locaties, bedragen, namen, functies, mailadressen. Verouderde feiten van de oude site zijn overgenomen en gemarkeerd met een lichtrode notitie <em>Check bestuur</em>.</li>
<li><strong>Toon en tekst.</strong> Spreekt het nieuwe leden aan? Te lang, te kort, iets dat mist?</li>
<li><strong>Volgorde en menu.</strong> Staan de pagina's logisch bij elkaar? Mis je een pagina?</li>
<li><strong>Uiterlijk.</strong> Kleur, letters, foto's (er staan nog geen clubfoto's in), de hartslaglijn.</li>
<li><strong>Telefoon.</strong> De meeste bezoekers komen via hun telefoon; de smalle kolommen tonen die weergave.</li>
</ul>
<h3>Hoe je het terugstuurt</h3>
<p>Mail je opmerkingen (nummer + opmerking) aan Emiel, of vul de feedbackbladen achterin in en stuur een foto of scan. Wil je liever doorklikken? De demo draait in de browser; de link staat in de begeleidende mail.</p>
<h3>Wat dit boek niet is</h3>
<p>Geen eindversie. Foto's, tarieven 2026, teamindeling en social media wachten op jullie input (zie de lijst met open vragen achterin). De technische kant (hosting, formulieren, cookies) is apart geregeld.</p>
"""), "Zo geef je feedback"))

    # inhoudsopgave placeholder index
    toc_index = add("Inhoud", "@@TOC@@")
    toc.append((toc_index, "Inhoud"))

    # sitemap
    toc.append((add("Opbouw van de site", f"""
<h1>Opbouw van de site</h1><div class="hart"></div>
<p class="groot">Dertien pagina's, bereikbaar via één menu. De oude site had dezelfde onderwerpen, verspreid over meer pagina's met deels verouderde inhoud.</p>
<div class="twee">
<div class="kader"><p class="lab">Menu</p>
<ul><li><strong>Vereniging</strong><ul><li>Bestuur</li><li>Trainers</li><li>Teamcompetitie</li><li>Clubcompetitie</li><li>Clubkleding</li><li>Vertrouwenscontactpersoon</li></ul></li>
<li><strong>Trainingen</strong></li><li><strong>Start2Tri</strong></li><li><strong>Lidmaatschap</strong> (met inschrijfformulier en veelgestelde vragen)</li><li><strong>Contact</strong></li></ul>
<p>Knop in de kopbalk: <span class="knop k1" style="font-size:8pt;padding:1.5mm 3mm">Word proeflid</span></p></div>
<div class="kader"><p class="lab">Niet in het menu, wel bereikbaar</p>
<ul><li>Home (via het logo)</li><li>Veelgestelde vragen (via Lidmaatschap en de voettekst)</li><li>Nieuws (via de voettekst; nu leeg)</li><li>Privacyverklaring (PDF, voettekst)</li><li>Spond en Strava (voettekst en Contact)</li></ul>
<p class="lab" style="margin-top:4mm">Oude adressen</p><p>Links naar de oude site (bijv. <span class="url">/lidmaatschap-2/</span>) worden automatisch doorgestuurd naar de nieuwe pagina.</p></div>
</div>
<h3>Hoofdroute voor een nieuw lid</h3>
<p>Home → Trainingen (wanneer, waar, welk niveau) → Lidmaatschap (proeflid € 35 / 10 weken) → inschrijfformulier. Elke knop "Word proeflid" springt direct naar het formulier.</p>
<div class="kader zacht"><strong>Vraag aan het bestuur:</strong> klopt deze indeling? Moet Start2Tri prominenter (eigen knop op de homepage), of juist Lidmaatschap?</div>
"""), "Opbouw van de site"))

    # huisstijl
    toc.append((add("Huisstijl", f"""
<h1>Huisstijl</h1><div class="hart"></div>
<p class="groot">Rood, zwart en wit, zoals het logo. Rood is accent (lijnen, knoppen, markeringen), nooit de enige drager van informatie — ook leesbaar voor kleurenblinden (getest).</p>
<p class="lab">Kleuren</p>
<div class="swatches">
<div class="sw"><div style="background:#ED1E24"></div><div><strong>Triami-rood</strong><br>#ED1E24 · logo, lijnen, nummers</div></div>
<div class="sw"><div style="background:#C4151B"></div><div><strong>Rood donker</strong><br>#C4151B · knoppen, links</div></div>
<div class="sw"><div style="background:#111111"></div><div><strong>Zwart</strong><br>#111111 · kopbalk-overlay, voettekst, hero</div></div>
<div class="sw"><div style="background:#FDE8E8"></div><div><strong>Rood tint</strong><br>#FDE8E8 · notities, markering</div></div>
<div class="sw"><div style="background:#1F1F1F"></div><div><strong>Tekst</strong><br>#1F1F1F</div></div>
<div class="sw"><div style="background:#5C5C5C"></div><div><strong>Gedempt</strong><br>#5C5C5C · bijschriften</div></div>
<div class="sw"><div style="background:#F4F4F4"></div><div><strong>Zacht grijs</strong><br>#F4F4F4 · vlakken, tabelkop</div></div>
<div class="sw"><div style="background:#fff"></div><div><strong>Wit</strong><br>#FFFFFF · achtergrond</div></div>
</div>
<p class="lab" style="margin-top:6mm">Letters</p>
<div class="twee">
<div class="kader"><div style="font:800 20pt Montserrat;text-transform:uppercase;letter-spacing:.02em">Montserrat</div><p>Koppen, knoppen en menu. Vet, in hoofdletters: sportief en herkenbaar vanaf afstand.</p></div>
<div class="kader"><div style="font:400 20pt 'Source Sans 3'">Source Sans 3</div><p>Lopende tekst, tabellen en formulieren. Rustig leesbaar, ook klein op een telefoon. <strong>Halfvet</strong> voor nadruk.</p></div>
</div>
<p class="lab" style="margin-top:6mm">Knoppen</p>
<div><span class="knop k1">Word proeflid</span><span class="knop k2">Bekijk de trainingen</span><span class="donker" style="display:inline-block;padding:2mm 3mm"><span class="knop k3" style="margin:0">Op donker</span></span></div>
<p class="lab" style="margin-top:6mm">Clubmotief: hartslaglijn</p>
<div class="donker">{svg}</div>
<p style="margin-top:3mm">Een rode lijn met één uitslag, als een hartslag: inspanning, en de drie sporten in één lijn. Komt terug onder koppen (korte rode streep), op de homepage en in de favicon.</p>
<div class="kader zacht"><strong>Vraag aan het bestuur:</strong> past dit bij hoe Triami zich wil tonen? Het logo is ongewijzigd overgenomen; een officieel vectorbestand ontbreekt nog (open vraag 14).</div>
"""), "Huisstijl"))

    # per pagina
    for slug, titel, url, doel in PAGINAS:
        vragen = chk.get(slug, [])
        vr = "".join(f"<li>{html.escape(v.replace('Check bestuur: ', ''))}</li>" for v in vragen)
        vr_html = f'<div class="kader tint"><p class="lab">Check bestuur</p><ul>{vr}</ul></div>' if vr else '<div class="kader zacht">Geen openstaande feitelijke vragen op deze pagina; inhoudelijke en tekstuele opmerkingen blijven welkom.</div>'
        desk = chunk(f"{slug}-desktop", DESK_CHUNK, first=2060 if chk.get(slug) else 2300)
        mob = chunk(f"{slug}-mobiel", MOB_CHUNK)
        first = add(titel, f"""
<h1>{html.escape(titel)}</h1><div class="hart"></div>
<p><span class="url">www.triami.nl{html.escape(url)}</span></p>
<p class="groot">{html.escape(doel)}</p>
{vr_html}
<p class="lab" style="margin-top:5mm">Weergave op computer (deel 1 van {len(desk)})</p>
<img class="shot desk" src="{img64(desk[0])}" style="max-height:{'152mm' if vr else '168mm'};width:auto;max-width:186mm">
""")
        toc.append((first, titel))
        for i, p in enumerate(desk[1:], start=2):
            add(titel, f'<p class="lab">{html.escape(titel)} — weergave op computer (deel {i} van {len(desk)})</p><img class="shot desk" src="{img64(p)}">')
        for i in range(0, len(mob), 3):
            kols = "".join(f'<img class="shot" src="{img64(p)}">' for p in mob[i:i+3])
            add(titel, f'<p class="lab">{html.escape(titel)} — weergave op telefoon (lees de kolommen van links naar rechts{", vervolg" if i else ""})</p><div class="mobkol">{kols}</div>')

    # componenten
    comp_first = None
    for i in range(0, len(COMPONENTEN), 2):
        blok = ""
        for key, naam, uitleg in COMPONENTEN[i:i+2]:
            p = SHOTS / f"{key}.png"
            im = Image.open(p)
            w = min(186, im.width / 2 * 0.2646)  # css px -> mm bij 96 dpi
            style = f"width:{w:.0f}mm;max-height:95mm;object-fit:contain;object-position:left top"
            if key == "menu-mobiel": style = "width:50mm"
            blok += f'<h3>{html.escape(naam)}</h3><p>{html.escape(uitleg)}</p><img class="shot" src="{img64(p)}" style="{style}">'
        n = add("Onderdelen", (f'<h1>Onderdelen</h1><div class="hart"></div><p class="groot">Bouwstenen die op meerdere pagina\'s terugkomen. Een opmerking hierover geldt dus voor de hele site.</p>' if i == 0 else "") + blok)
        if comp_first is None: comp_first = n
    toc.append((comp_first, "Onderdelen (bouwstenen)"))

    # open vragen
    rows = (ROOT / "docs/ophaallijst-bestuur.md").read_text().splitlines()
    tr = ""
    for r in rows:
        m = re.match(r"\|\s*(\d+)\s*\|(.*?)\|(.*?)\|(.*?)\|", r)
        if m:
            tr += f"<tr><td><strong>{m.group(1)}</strong></td><td>{html.escape(m.group(2).strip())}</td><td>{html.escape(m.group(3).strip())}</td><td>{html.escape(m.group(4).strip())}</td></tr>"
    toc.append((add("Open vragen", f"""
<h1>Open vragen aan het bestuur</h1><div class="hart"></div>
<p class="groot">Achttien punten die we nodig hebben om de site af te maken. Antwoord mag per mail; per punt een regel is genoeg.</p>
<table><tr><th>#</th><th>Nodig</th><th>Waar</th><th>Wie</th></tr>{tr}</table>
"""), "Open vragen aan het bestuur"))

    # feedbackbladen
    fb_first = None
    for k in range(3):
        rijen = "".join('<tr><td></td><td></td><td></td></tr>' for _ in range(15))
        n = add("Feedbackblad", f"""
<h1>Feedbackblad {k+1}</h1><div class="hart"></div>
<p>Naam: ______________________________ &nbsp;&nbsp; Datum: ______________</p>
<table class="form"><tr><th>Blad</th><th>Opmerking</th><th>Prioriteit (moet / graag / idee)</th></tr>{rijen}</table>
""")
        if fb_first is None: fb_first = n
    toc.append((fb_first, "Feedbackbladen"))

    # toc invullen
    toc_html = "<h1>Inhoud</h1><div class=\"hart\"></div><table class=\"toc\">" + "".join(
        f"<tr><td>{n}</td><td>{html.escape(t)}</td></tr>" for n, t in toc if n != toc_index) + "</table>"
    toc_html += '<p style="margin-top:6mm" class="lab">Per pagina</p><p>Eerst een blad met uitleg en de weergave op computer, daarna (bij lange pagina\'s) het vervolg, en tot slot de weergave op telefoon in smalle kolommen.</p>'
    json.dump({"toc": toc, "paginas": {slug: n for n, t in toc for slug, titel, *_ in PAGINAS if t == titel}}, open(ROOT / "dist" / "feedbackboek-toc.json", "w"), ensure_ascii=False, indent=1)
    body = "".join(vel(inh.replace("@@TOC@@", toc_html), i + 1, kop, cls) for i, (kop, inh, cls) in enumerate(sheets))
    css = CSS.replace("@@MONT@@", font64(ROOT / "theme/triami/assets/fonts/montserrat-latin.woff2")).replace("@@SS@@", font64(ROOT / "theme/triami/assets/fonts/source-sans-3-latin.woff2"))
    HTML.write_text(f"<!doctype html><html lang=nl><meta charset=utf-8><title>Feedbackboek Triami</title><style>{css}</style><body>{body}</body></html>")
    asyncio.run(render())
    print("bladen:", len(sheets), "->", OUT, f"{OUT.stat().st_size/1e6:.1f} MB")

async def render():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        pg = await b.new_page()
        await pg.goto(HTML.as_uri(), wait_until="load")
        await pg.evaluate("document.fonts.ready")
        await pg.pdf(path=str(OUT), format="A4", print_background=True, prefer_css_page_size=True)
        await b.close()

if __name__ == "__main__":
    main()
