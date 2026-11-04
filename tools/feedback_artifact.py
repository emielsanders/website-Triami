"""Bouwt dist/feedback/index.html: feedbackpagina (artifact) met alle schermen van de
nieuwe site, dezelfde bladnummers als het PDF-feedbackboek en opslag van opmerkingen
in de artifact-database (db-capability)."""
import html, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist" / "feedback"; OUT.mkdir(parents=True, exist_ok=True)
TOC = json.load(open(ROOT / "dist" / "feedbackboek-toc.json"))
NR = TOC["paginas"]
import importlib.util
spec = importlib.util.spec_from_file_location("fp", ROOT / "tools" / "feedback_pdf.py")
fp = importlib.util.module_from_spec(spec); spec.loader.exec_module(fp)
PAGINAS, COMPONENTEN = fp.PAGINAS, fp.COMPONENTEN
chk = fp.checks()
ONDERDELEN_NR = dict(TOC["toc"]).__class__  # placeholder
toc_by_title = {t: n for n, t in TOC["toc"]}

vragen = []
for r in (ROOT / "docs/ophaallijst-bestuur.md").read_text().splitlines():
    m = re.match(r"\|\s*(\d+)\s*\|(.*?)\|(.*?)\|(.*?)\|", r)
    if m:
        vragen.append((int(m.group(1)), m.group(2).strip(), m.group(3).strip(), m.group(4).strip()))

def e(s): return html.escape(s, quote=True)

schermen = []  # data voor JS
secties = []

# Algemeen: opbouw + huisstijl
algemeen = [
    (toc_by_title["Opbouw van de site"], "Opbouw van de site", "Dertien pagina's, één menu met submenu Vereniging. Hoofdroute voor een nieuw lid: Home → Trainingen → Lidmaatschap → inschrijfformulier. Vragen: klopt de indeling, moet Start2Tri prominenter?", None),
    (toc_by_title["Huisstijl"], "Huisstijl", "Rood, zwart en wit zoals het logo; Montserrat voor koppen, Source Sans 3 voor tekst; hartslaglijn als clubmotief. Vraag: past dit bij hoe Triami zich wil tonen?", None),
]
for n, t, d, _ in algemeen:
    schermen.append({"blad": n, "titel": t})

paginas_html = ""
for slug, titel, url, doel in PAGINAS:
    n = NR[slug]
    schermen.append({"blad": n, "titel": titel})
    checks = "".join(f"<li>{e(c.replace('Check bestuur: ', ''))}</li>" for c in chk.get(slug, []))
    checks_html = f'<details class="check"><summary>Check bestuur ({len(chk.get(slug, []))})</summary><ul>{checks}</ul></details>' if checks else ""
    paginas_html += f"""
<article class="kaart" id="blad-{n}" data-blad="{n}">
  <header class="kaart-kop"><span class="nr">{n}</span><div><h3>{e(titel)}</h3><div class="url">www.triami.nl{e(url)}</div></div></header>
  <p>{e(doel)}</p>
  {checks_html}
  <div class="tabs" role="tablist"><button class="tab is-actief" data-weergave="desktop" role="tab" aria-selected="true">Computer</button><button class="tab" data-weergave="mobiel" role="tab" aria-selected="false">Telefoon</button></div>
  <div class="scherm scherm-desktop"><img loading="lazy" src="img/{slug}-desktop.webp" alt="Weergave van de pagina {e(titel)} op een computer"></div>
  <div class="scherm scherm-mobiel" hidden><img loading="lazy" src="img/{slug}-mobiel.webp" alt="Weergave van de pagina {e(titel)} op een telefoon"></div>
  <div class="fb" data-blad="{n}" data-titel="{e(titel)}"></div>
</article>"""

comp_nr = toc_by_title["Onderdelen (bouwstenen)"]
onderdelen_html = ""
for i, (key, naam, uitleg) in enumerate(COMPONENTEN):
    n = f"{comp_nr}.{i+1}"
    schermen.append({"blad": n, "titel": naam})
    onderdelen_html += f"""
<article class="kaart kaart-klein" id="blad-{n.replace('.', '-')}" data-blad="{n}">
  <header class="kaart-kop"><span class="nr">{n}</span><h3>{e(naam)}</h3></header>
  <p>{e(uitleg)}</p>
  <div class="scherm scherm-comp{' smal' if key == 'menu-mobiel' else ''}"><img loading="lazy" src="img/{key}.webp" alt="{e(naam)}"></div>
  <div class="fb" data-blad="{n}" data-titel="{e(naam)}"></div>
</article>"""

vragen_nr = toc_by_title["Open vragen aan het bestuur"]
vragen_html = "".join(f"""
<div class="vraag" data-vraag="{nr}">
  <div class="vraag-kop"><span class="nr nr-klein">{nr}</span><div><strong>{e(nodig)}</strong><div class="meta">{e(waar)} · {e(wie)}</div></div></div>
  <div class="antwoorden" data-vraag="{nr}"></div>
  <form class="antwoord-form" data-vraag="{nr}"><textarea rows="2" placeholder="Jouw antwoord" aria-label="Antwoord op vraag {nr}"></textarea><button type="submit" class="knop knop-klein">Antwoord opslaan</button></form>
</div>""" for nr, nodig, waar, wie in vragen)

algemeen_html = "".join(f"""
<article class="kaart kaart-klein" id="blad-{n}" data-blad="{n}">
  <header class="kaart-kop"><span class="nr">{n}</span><h3>{e(t)}</h3></header><p>{e(d)}</p>
  <div class="fb" data-blad="{n}" data-titel="{e(t)}"></div>
</article>""" for n, t, d, _ in algemeen)

logo_svg = (ROOT / "theme/triami/assets/img/logo.svg").read_text()
hart = re.search(r"<svg.*?</svg>", (ROOT / "theme/triami/patterns/hartslaglijn.php").read_text(), re.S).group(0)

page = f"""<title>Triami feedback</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800&family=Source+Sans+3:wght@400;600&display=swap">
<style>
:root {{ --bg:#ffffff; --bg2:#f6f4f4; --fg:#1f1f1f; --gedempt:#5c5c5c; --lijn:#dfdfdf; --rood:#ED1E24; --rood-donker:#C4151B; --rood-tint:#fde8e8; --kaart:#ffffff; --schaduw:0 1px 2px rgba(0,0,0,.06),0 6px 20px rgba(0,0,0,.06); --ok:#1b7f3b; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --bg:#141414; --bg2:#1d1d1d; --fg:#f2f2f2; --gedempt:#b0b0b0; --lijn:#333; --rood:#F04A4F; --rood-donker:#E0353B; --rood-tint:#3a1c1d; --kaart:#1b1b1b; --schaduw:0 1px 2px rgba(0,0,0,.4); --ok:#5fcf80; color-scheme: dark }} }}
:root[data-theme="dark"] {{ --bg:#141414; --bg2:#1d1d1d; --fg:#f2f2f2; --gedempt:#b0b0b0; --lijn:#333; --rood:#F04A4F; --rood-donker:#E0353B; --rood-tint:#3a1c1d; --kaart:#1b1b1b; --schaduw:0 1px 2px rgba(0,0,0,.4); --ok:#5fcf80; color-scheme: dark }}
* {{ box-sizing: border-box }}
[hidden] {{ display:none !important }}
@media (max-width: 640px) {{ .top .titel {{ display:none }} .top .wrap {{ gap:.5rem }} .naam input {{ width: 9rem }} }}
body {{ background: var(--bg); color: var(--fg); font: 16px/1.5 'Source Sans 3', system-ui, sans-serif; margin:0; }}
h1,h2,h3 {{ font-family: Montserrat, system-ui, sans-serif; font-weight: 800; line-height:1.15; margin:0; text-wrap: balance }}
h1 {{ font-size: clamp(1.5rem, 4vw, 2.25rem); text-transform: uppercase; letter-spacing:.02em }}
h2 {{ font-size: 1.4rem; text-transform: uppercase; letter-spacing:.02em; margin: 2.5rem 0 .25rem }}
h2::after {{ content:""; display:block; width:3rem; height:4px; background:var(--rood); margin-top:.4rem }}
h3 {{ font-size: 1.1rem }}
a {{ color: var(--rood-donker) }}
.wrap {{ max-width: 1100px; margin: 0 auto; padding-block: 0 4rem; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }}
.top {{ position: sticky; top: env(safe-area-inset-top, 0px); z-index: 5; background: var(--bg); border-bottom: 1px solid var(--lijn); }}
body::before {{ content:""; position:fixed; inset:0 0 auto; height: env(safe-area-inset-top, 0px); background: var(--bg); z-index: 10 }}
.top .wrap {{ display:flex; gap:1rem; align-items:center; flex-wrap: wrap; padding-block:.6rem }}
.top .logo {{ height: 36px; width:auto }}
.top .titel {{ font: 700 .8rem Montserrat, sans-serif; text-transform: uppercase; letter-spacing:.08em; color: var(--gedempt); flex:1; min-width: 0 }}
.naam {{ display:flex; gap:.5rem; align-items:center; font-size:.9rem }}
input, textarea, select {{ font: inherit; color: var(--fg); background: var(--bg); border:1px solid var(--lijn); border-radius: 8px; padding:.5rem .7rem; max-width:100% }}
input:focus-visible, textarea:focus-visible, select:focus-visible, button:focus-visible {{ outline: 3px solid var(--rood); outline-offset: 2px }}
.status {{ font-size:.85rem; color: var(--gedempt) }}
.status.ok {{ color: var(--ok) }}
.intro {{ background: var(--rood-tint); border-radius: 12px; padding: 1rem 1.25rem; margin: 1.5rem 0; }}
.intro p {{ margin:.25rem 0 }}
.hart {{ width:100%; height: 36px; margin: 1rem 0 0 }}
.chips {{ display:flex; flex-wrap:wrap; gap:.4rem; margin: 1rem 0 }}
.chips a {{ text-decoration:none; font: 600 .85rem 'Source Sans 3', sans-serif; border:1px solid var(--lijn); border-radius: 999px; padding:.3rem .8rem; color: var(--fg) }}
.chips a:hover {{ border-color: var(--rood) }}
.kaart {{ background: var(--kaart); border:1px solid var(--lijn); border-radius: 14px; box-shadow: var(--schaduw); padding: 1.25rem; margin: 1.25rem 0; }}
.raster {{ display:grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1rem }}
.raster .kaart {{ margin:0; min-width:0 }}
.kaart-kop {{ display:flex; gap:.9rem; align-items:flex-start; margin-bottom:.5rem }}
.kaart-kop > div {{ min-width:0 }}
.nr {{ flex: none; display:inline-flex; align-items:center; justify-content:center; min-width: 3rem; height: 3rem; padding: 0 .5rem; border-radius: 10px; background: var(--rood); color:#fff; font: 800 1.4rem Montserrat, sans-serif; letter-spacing:-.02em }}
.nr-klein {{ min-width: 2.2rem; height: 2.2rem; font-size: 1rem; border-radius: 8px }}
.url {{ font-family: ui-monospace, Consolas, monospace; font-size: .85rem; color: var(--gedempt); overflow-wrap: anywhere }}
.check {{ background: var(--rood-tint); border-radius: 10px; padding: .6rem .9rem; margin: .75rem 0; font-size:.95rem }}
.check summary {{ cursor:pointer; font-weight:600 }}
.check ul {{ margin:.5rem 0 0; padding-left: 1.2rem }}
.tabs {{ display:flex; gap:.4rem; margin: .75rem 0 .5rem }}
.tab {{ font: 700 .85rem Montserrat, sans-serif; text-transform: uppercase; letter-spacing:.04em; border:2px solid var(--lijn); background: transparent; color: var(--fg); border-radius: 8px; padding:.4rem .8rem; cursor:pointer }}
.tab.is-actief {{ border-color: var(--rood-donker); background: var(--rood-donker); color:#fff }}
.scherm {{ border:1px solid var(--lijn); border-radius: 10px; overflow:auto; max-height: 70vh; background:#fff; -webkit-overflow-scrolling: touch }}
.scherm img {{ display:block; width:100%; height:auto; max-width:100% }}
.scherm-mobiel {{ max-width: 390px }}
.scherm-comp {{ max-height: 60vh }}
.scherm-comp.smal {{ max-width: 260px }}
.fb {{ margin-top: .9rem; border-top: 1px dashed var(--lijn); padding-top: .75rem }}
.fb-lijst {{ display:flex; flex-direction:column; gap:.5rem; margin-bottom:.6rem }}
.opm {{ background: var(--bg2); border-radius: 10px; padding:.6rem .8rem; font-size:.95rem; display:flex; gap:.6rem; align-items:flex-start }}
.opm .tekst {{ flex:1; min-width:0; white-space: pre-wrap; overflow-wrap:anywhere }}
.opm .meta {{ font-size:.8rem; color: var(--gedempt) }}
.prio {{ font: 700 .7rem Montserrat, sans-serif; text-transform: uppercase; letter-spacing:.05em; border-radius: 6px; padding:.15rem .4rem; background: var(--lijn); color: var(--fg); white-space:nowrap }}
.prio-moet {{ background: var(--rood-donker); color:#fff }}
.prio-graag {{ background: var(--rood-tint) }}
.knop {{ font: 700 .9rem Montserrat, sans-serif; background: var(--rood-donker); color:#fff; border:0; border-radius: 8px; padding:.6rem 1rem; cursor:pointer }}
.knop:hover {{ filter: brightness(.9) }}
.knop-licht {{ background: transparent; color: var(--fg); border:2px solid var(--lijn) }}
.knop-klein {{ padding:.4rem .8rem; font-size:.8rem }}
.knop-x {{ background:transparent; border:0; color: var(--gedempt); cursor:pointer; font-size:1.1rem; line-height:1; padding:.2rem }}
.fb-form {{ display:grid; gap:.5rem; grid-template-columns: 1fr; margin-top:.5rem }}
.fb-form textarea {{ width:100%; min-height: 4.5rem }}
.fb-form .rij {{ display:flex; gap:.5rem; flex-wrap:wrap; align-items:center }}
.vraag {{ padding: 1rem 0; border-bottom: 1px solid var(--lijn) }}
.vraag-kop {{ display:flex; gap:.8rem; align-items:flex-start }}
.vraag .meta {{ font-size:.85rem; color: var(--gedempt) }}
.antwoord-form {{ display:flex; gap:.5rem; flex-wrap:wrap; margin-top:.5rem }}
.antwoord-form textarea {{ flex:1; min-width: 220px }}
.antwoorden {{ display:flex; flex-direction:column; gap:.4rem; margin-top:.5rem }}
.melding {{ font-size:.9rem; color: var(--gedempt); margin:.3rem 0 0 }}
.noot {{ background: var(--bg2); border-radius: 10px; padding:.8rem 1rem; font-size:.95rem }}
.verborgen {{ display:none }}
footer {{ margin-top: 3rem; color: var(--gedempt); font-size:.85rem; border-top:1px solid var(--lijn); padding-top:1rem }}
@media (prefers-reduced-motion: no-preference) {{ html {{ scroll-behavior: smooth }} }}
</style>

<div class="top"><div class="wrap">
  <img class="logo" src="img/logo.svg" alt="Triami">
  <div class="titel">Nieuwe website — feedback bestuur</div>
  <label class="naam">Je naam <input id="naam" type="text" placeholder="bv. Marieke" autocomplete="name" size="14"></label>
  <span class="status" id="status">Verbinden…</span>
</div></div>

<main class="wrap">
  <h1 style="margin-top:1.5rem">Kijk mee met de nieuwe Triami-site</h1>
  <div class="hart">{hart}</div>
  <div class="intro">
    <p><strong>Zo werkt het.</strong> Vul bovenin je naam in. Bekijk per onderdeel het scherm (Computer of Telefoon), klik op <em>Opmerking plaatsen</em>, typ je opmerking en kies hoe belangrijk hij is. Je ziet ook wat anderen al schreven; reageren mag.</p>
    <p>De nummers zijn dezelfde als in het PDF-feedbackboek, dus "blad 14" betekent hier en daar hetzelfde. Rode notities <em>Check bestuur</em> zijn feiten van de oude site die we willen laten bevestigen.</p>
    <p>Onderaan staan <a href="#vragen">achttien open vragen</a> waarop we antwoord nodig hebben om de site af te maken.</p>
  </div>
  <nav class="chips" aria-label="Snel naar">
    <a href="#algemeen">Algemeen</a>
    {"".join(f'<a href="#blad-{NR[s]}">{e(t)}</a>' for s, t, *_ in PAGINAS)}
    <a href="#onderdelen">Onderdelen</a><a href="#vragen">Open vragen</a><a href="#overzicht">Alle opmerkingen</a>
  </nav>

  <h2 id="algemeen">Algemeen</h2>
  <div class="raster">{algemeen_html}</div>

  <h2 id="paginas">De pagina's</h2>
  {paginas_html}

  <h2 id="onderdelen">Onderdelen</h2>
  <p>Bouwstenen die op meerdere pagina's terugkomen; een opmerking hierover geldt voor de hele site.</p>
  <div class="raster">{onderdelen_html}</div>

  <h2 id="vragen">Open vragen aan het bestuur</h2>
  <p>Blad {vragen_nr} in het boek. Antwoord per vraag; een regel is genoeg. Als iemand anders al antwoordde, zie je dat hier en kun je aanvullen.</p>
  {vragen_html}

  <h2 id="overzicht">Alle opmerkingen</h2>
  <p class="status" id="telling"></p>
  <div class="rij" style="display:flex;gap:.5rem;flex-wrap:wrap;margin:.5rem 0 1rem"><button class="knop knop-licht knop-klein" id="kopieer">Kopieer alles als tekst</button></div>
  <div id="alles" class="fb-lijst"></div>

  <footer>Triami Triathlonvereniging · feedbackversie 4 november 2026 · <span id="voetstatus"></span></footer>
</main>

<script>
(() => {{
  const SCHERMEN = {json.dumps(schermen, ensure_ascii=False)};
  const $ = (s, r=document) => r.querySelector(s);
  const $$ = (s, r=document) => [...r.querySelectorAll(s)];
  const status = $('#status'), voet = $('#voetstatus');
  let db = null, user = null, uid = null, magSchrijven = null, isOwner = false;
  let opmerkingen = [], antwoorden = [];
  const lokaal = {{ get(k, d) {{ try {{ const v = localStorage.getItem('triami-fb-'+k); return v == null ? d : JSON.parse(v) }} catch {{ return d }} }}, set(k, v) {{ try {{ localStorage.setItem('triami-fb-'+k, JSON.stringify(v)) }} catch {{}} }} }};
  const naamVeld = $('#naam'); naamVeld.value = lokaal.get('naam', '');
  naamVeld.addEventListener('input', () => lokaal.set('naam', naamVeld.value.trim()));
  const naam = () => naamVeld.value.trim();
  const esc = s => String(s).replace(/[&<>"]/g, c => ({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]));
  const tijd = t => {{ try {{ return new Date(t).toLocaleString('nl-NL', {{dateStyle:'short', timeStyle:'short'}}) }} catch {{ return '' }} }};
  const titelVan = b => (SCHERMEN.find(s => String(s.blad) === String(b)) || {{}}).titel || '';

  // Tabs computer/telefoon
  $$('.tabs').forEach(t => t.addEventListener('click', ev => {{
    const b = ev.target.closest('.tab'); if (!b) return;
    const k = b.closest('.kaart');
    $$('.tab', t).forEach(x => {{ x.classList.toggle('is-actief', x === b); x.setAttribute('aria-selected', x === b) }});
    $('.scherm-desktop', k).hidden = b.dataset.weergave !== 'desktop';
    $('.scherm-mobiel', k).hidden = b.dataset.weergave !== 'mobiel';
  }}));

  // Feedbackblokken
  $$('.fb').forEach(fb => {{
    fb.innerHTML = `<div class="fb-lijst"></div><button class="knop knop-klein fb-open" type="button">Opmerking plaatsen</button>
      <form class="fb-form" hidden>
        <textarea required placeholder="Wat valt je op? Wees concreet: wat, waar, en wat zou beter zijn." aria-label="Opmerking bij blad ${{fb.dataset.blad}}"></textarea>
        <div class="rij"><label>Belang <select><option value="moet">Moet anders</option><option value="graag" selected>Graag anders</option><option value="idee">Idee / vraag</option></select></label>
        <button class="knop knop-klein" type="submit">Opslaan</button><button class="knop knop-licht knop-klein fb-annuleer" type="button">Annuleer</button></div>
        <p class="melding" hidden></p></form>`;
    const open = $('.fb-open', fb), form = $('.fb-form', fb);
    open.addEventListener('click', () => {{ form.hidden = false; open.hidden = true; $('textarea', form).focus() }});
    $('.fb-annuleer', fb).addEventListener('click', () => {{ form.hidden = true; open.hidden = false }});
    form.addEventListener('submit', async ev => {{
      ev.preventDefault();
      const tekst = $('textarea', form).value.trim(); if (!tekst) return;
      if (!naam()) {{ melding(form, 'Vul eerst je naam in (bovenaan).'); naamVeld.focus(); return }}
      const doc = {{ blad: String(fb.dataset.blad), scherm: fb.dataset.titel, naam: naam(), tekst, prioriteit: $('select', form).value, uid: uid || null, tijd: new Date().toISOString() }};
      const ok = await bewaarOpmerking(doc);
      if (ok) {{ $('textarea', form).value = ''; form.hidden = true; open.hidden = false }}
    }});
  }});
  function melding(form, t, ok=false) {{ const m = $('.melding', form); m.hidden = false; m.textContent = t; m.style.color = ok ? 'var(--ok)' : 'var(--rood-donker)' }}

  async function bewaarOpmerking(doc) {{
    if (db && magSchrijven !== false) {{
      try {{ await db.collection('opmerkingen').add(doc); return true }}
      catch (e) {{ if (e && e.code === 'invalid_argument') {{ magSchrijven = false; zetStatus() }} else {{ console.error(e) }} }}
    }}
    // Terugval: lokaal bewaren, later kopiëren
    const l = lokaal.get('lokaal', []); l.push(Object.assign({{ id: 'l' + Date.now(), lokaal: true }}, doc)); lokaal.set('lokaal', l);
    render(); return true;
  }}
  async function verwijder(o) {{
    if (o.lokaal) {{ lokaal.set('lokaal', lokaal.get('lokaal', []).filter(x => x.id !== o.id)); render(); return }}
    try {{ await db.collection('opmerkingen').doc(o.id).delete() }} catch (e) {{ console.error(e) }}
  }}

  function alleOpmerkingen() {{ return opmerkingen.concat(lokaal.get('lokaal', [])).sort((a, b) => (a.tijd || '').localeCompare(b.tijd || '')) }}
  function opmHtml(o, metBlad) {{
    const eigen = o.lokaal || (uid && o.uid === uid);
    return `<div class="opm" data-id="${{esc(o.id)}}"><span class="prio prio-${{esc(o.prioriteit||'graag')}}">${{ {{moet:'moet', graag:'graag', idee:'idee'}}[o.prioriteit] || 'graag' }}</span>
      <div class="tekst">${{metBlad ? `<strong>Blad ${{esc(o.blad)}} · ${{esc(titelVan(o.blad) || o.scherm || '')}}</strong><br>` : ''}}${{esc(o.tekst)}}<div class="meta">${{esc(o.naam || 'Anoniem')}} · ${{tijd(o.tijd)}}${{o.lokaal ? ' · alleen op dit apparaat bewaard' : ''}}</div></div>
      ${{(eigen || isOwner) ? `<button class="knop-x" type="button" title="Verwijder" aria-label="Verwijder opmerking">×</button>` : ''}}</div>`;
  }}
  function render() {{
    const alle = alleOpmerkingen();
    $$('.fb').forEach(fb => {{
      const mijn = alle.filter(o => String(o.blad) === String(fb.dataset.blad));
      $('.fb-lijst', fb).innerHTML = mijn.map(o => opmHtml(o, false)).join('');
      $('.fb-open', fb).textContent = mijn.length ? 'Nog een opmerking' : 'Opmerking plaatsen';
    }});
    $('#alles').innerHTML = alle.length ? alle.map(o => opmHtml(o, true)).join('') : '<p class="melding">Nog geen opmerkingen.</p>';
    $('#telling').textContent = alle.length ? `${{alle.length}} opmerking${{alle.length === 1 ? '' : 'en'}} van ${{new Set(alle.map(o => o.naam)).size}} ${{new Set(alle.map(o => o.naam)).size === 1 ? 'persoon' : 'personen'}}` : '';
    $$('.antwoorden').forEach(a => {{
      const mijn = antwoorden.filter(x => String(x.vraag) === a.dataset.vraag);
      a.innerHTML = mijn.map(x => `<div class="opm"><div class="tekst">${{esc(x.tekst)}}<div class="meta">${{esc(x.naam || 'Anoniem')}} · ${{tijd(x.tijd)}}</div></div></div>`).join('');
    }});
  }}
  document.addEventListener('click', ev => {{
    const x = ev.target.closest('.knop-x'); if (!x) return;
    const id = x.closest('.opm').dataset.id;
    const o = alleOpmerkingen().find(o => o.id === id); if (o) verwijder(o);
  }});

  // Antwoorden op open vragen
  $$('.antwoord-form').forEach(f => f.addEventListener('submit', async ev => {{
    ev.preventDefault();
    const tekst = $('textarea', f).value.trim(); if (!tekst) return;
    if (!naam()) {{ naamVeld.focus(); return }}
    const doc = {{ vraag: Number(f.dataset.vraag), naam: naam(), tekst, uid: uid || null, tijd: new Date().toISOString() }};
    let ok = false;
    if (db && magSchrijven !== false) {{ try {{ await db.collection('antwoorden').add(doc); ok = true }} catch (e) {{ if (e && e.code === 'invalid_argument') {{ magSchrijven = false; zetStatus() }} }} }}
    if (!ok) {{ const l = lokaal.get('lokaal', []); l.push(Object.assign({{ id: 'l' + Date.now(), lokaal: true, blad: 'vraag ' + doc.vraag, scherm: 'Open vraag ' + doc.vraag, prioriteit: 'idee' }}, doc)); lokaal.set('lokaal', l) }}
    $('textarea', f).value = ''; render();
  }}));

  // Kopieer alles
  $('#kopieer').addEventListener('click', async () => {{
    const t = alleOpmerkingen().map(o => `Blad ${{o.blad}} (${{titelVan(o.blad) || o.scherm || ''}}) [${{o.prioriteit}}] ${{o.naam}}: ${{o.tekst}}`).join('\\n');
    try {{ await navigator.clipboard.writeText(t); $('#kopieer').textContent = 'Gekopieerd' }}
    catch {{ const ta = document.createElement('textarea'); ta.value = t; document.body.appendChild(ta); ta.select(); $('#kopieer').textContent = 'Selecteer en kopieer de tekst hieronder'; }}
    setTimeout(() => $('#kopieer').textContent = 'Kopieer alles als tekst', 2500);
  }});

  function zetStatus() {{
    if (!db) {{ status.textContent = 'Opmerkingen worden alleen op dit apparaat bewaard; gebruik "Kopieer alles" en mail ze.'; status.className = 'status'; voet.textContent = 'niet verbonden met de opslag'; return }}
    if (magSchrijven === false) {{ status.textContent = 'Je kunt meelezen; eigen opmerkingen blijven op dit apparaat (kopieer en mail ze).'; status.className = 'status'; voet.textContent = 'alleen lezen'; return }}
    status.textContent = 'Opmerkingen worden centraal bewaard'; status.className = 'status ok'; voet.textContent = 'verbonden';
  }}

  render();
  (async () => {{
    const use = n => (window.claude && window.claude.use) ? window.claude.use(n) : Promise.resolve(null);
    [db, user] = await Promise.all([use('db'), use('user')]);
    if (user) {{ try {{ uid = await user.id(); isOwner = await user.isOwner(); magSchrijven = await user.can('data.write') }} catch {{}} }}
    zetStatus();
    if (!db) return;
    let timer = setTimeout(() => {{ status.textContent = 'Opslag nog niet bereikbaar…' }}, 10000);
    db.collection('opmerkingen').orderBy('tijd').onSnapshot(snap => {{
      if (!snap.metadata.fromCache) {{ clearTimeout(timer); zetStatus() }}
      opmerkingen = snap.docs.map(d => Object.assign({{ id: d.id }}, d.data())); render();
    }}, e => {{ clearTimeout(timer); console.error(e); status.textContent = 'Opslag niet beschikbaar' }});
    db.collection('antwoorden').orderBy('tijd').onSnapshot(snap => {{
      antwoorden = snap.docs.map(d => Object.assign({{ id: d.id }}, d.data())); render();
    }}, e => console.error(e));
  }})();
}})();
</script>
"""
(OUT / "index.html").write_text(page)
print("geschreven", OUT / "index.html", f"{len(page)/1024:.0f} kB")
