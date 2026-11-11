"""Maakt een Word-reviewversie van alle teksten van de website (docs/website-teksten-review.docx).

Per pagina: kop, adres en de leesbare tekst. Foto's, knoppen en de Instagram-feed staan als
[Foto: ...], [Knop: ...] zodat een reviewer weet wat er staat. Interne 'Check bestuur'-notities
blijven weg. Opnieuw draaien na elke tekstwijziging: python3 tools/review_docx.py
"""
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "content/pages"
PATTERNS = ROOT / "theme/triami/patterns"
OUT = ROOT / "docs/website-teksten-review.docx"
BASE = "https://nieuw.triami.nl"

HOME = ["hero", "intro", "fotostrook", "trainingsschema", "cta-proeflid", "start2tri-teaser", "volg", "home-contact"]
VOLGORDE = ["vereniging", "bestuur", "trainers", "activiteiten", "teamcompetitie", "clubcompetitie", "clubkleding",
            "vertrouwenscontactpersoon", "veilig-sportklimaat", "trainingen", "start2tri", "lidmaatschap", "faq",
            "contact", "privacy"]


def front(text):
    meta, body = {}, text
    if text.startswith("---"):
        _, fm, body = text.split("---", 2)
        for line in fm.strip().splitlines():
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip()
    return meta, body


def opschonen(html):
    html = re.sub(r"<\?php.*?\?>", "", html, flags=re.S)
    html = re.sub(r"<!--.*?-->", "", html, flags=re.S)
    html = re.sub(r"\[instagram-feed[^\]]*\]", "<p>[Instagram: de laatste zes foto's van @triami_triathlon]</p>", html)
    soup = BeautifulSoup(html, "html.parser")
    for el in soup.select(".triami-check, svg, script, style, iframe"):
        el.decompose()
    for img in soup.find_all("img"):
        alt = img.get("alt", "").strip()
        p = soup.new_tag("p")
        p.string = f"[Foto: {alt}]" if alt else "[Afbeelding]"
        (img.find_parent("figure") or img).replace_with(p)
    for a in soup.select(".wp-block-button a, a.wp-block-button__link"):
        href = a.get("href", "")
        p = soup.new_tag("p")
        p.string = f"[Knop: {a.get_text(' ', strip=True)} → {href}]"
        (a.find_parent(class_="wp-block-button") or a).replace_with(p)
    for d in soup.find_all("details"):
        s = d.find("summary")
        if s:
            q = soup.new_tag("h3")
            q.string = s.get_text(" ", strip=True)
            s.replace_with(q)
        d.unwrap()
    for a in soup.find_all("a"):  # relatieve links leesbaar maken
        if a.get("href", "").startswith("/"):
            a["href"] = BASE + a["href"]
    for el in soup.find_all(class_="triami-label"):
        el.string = f"[Label: {el.get_text(strip=True)}]"
    return str(soup).replace("­", "")


def nieuwe_pagina_per_kop(pad):
    """Elke pagina van de site (Kop 1) begint op een nieuwe pagina in Word, behalve de eerste."""
    import zipfile, shutil, tempfile
    tmp = Path(tempfile.mkdtemp()) / "x.docx"
    with zipfile.ZipFile(pad) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/document.xml":
                xml = data.decode("utf-8")
                teller = {"n": 0}
                def zet(m):
                    teller["n"] += 1
                    return m.group(0) if teller["n"] == 1 else m.group(0).replace('<w:pStyle w:val="Heading1" />', '<w:pStyle w:val="Heading1" /><w:pageBreakBefore />')
                xml = re.sub(r'<w:pPr>\s*<w:pStyle w:val="Heading1" />', zet, xml)
                data = xml.encode("utf-8")
            zout.writestr(item, data)
    shutil.move(tmp, pad)


def main():
    delen = [f"""<h1>Website Triami: teksten voor review</h1>
<p>Versie van {date.today().strftime('%d-%m-%Y')}, stagingsite {BASE}.</p>
<p><strong>Zo geef je feedback:</strong> zet in Word <em>Wijzigingen bijhouden</em> aan (tabblad Controleren)
en pas de tekst direct aan, of plaats een opmerking. Tussen haken staat wat er op de site te zien is,
zoals [Foto: ...] en [Knop: ...]. Elke pagina van de site begint op een nieuwe pagina.</p>
<p>Huisregels voor de site: alleen voornamen, functie-e-mailadressen en geen telefoonnummers,
adressen of trainingstijden.</p>"""]
    home = "".join(opschonen((PATTERNS / f"{p}.php").read_text()) for p in HOME)
    delen.append(f"<h1>Home</h1><p><em>{BASE}/</em></p>{home}")
    for slug in VOLGORDE:
        meta, body = front((PAGES / f"{slug}.html").read_text())
        titel = meta.get("title", slug).replace("&shy;", "")
        delen.append(f"<h1>{titel}</h1><p><em>{BASE}/{slug}/</em></p>{opschonen(body)}")
    html = "<html><head><meta charset='utf-8'></head><body>" + "".join(delen) + "</body></html>"
    OUT.parent.mkdir(exist_ok=True)
    subprocess.run(["pandoc", "-f", "html", "-t", "docx", "-o", str(OUT)], input=html.encode(), check=True)
    nieuwe_pagina_per_kop(OUT)
    print(OUT)


if __name__ == "__main__":
    sys.exit(main())
