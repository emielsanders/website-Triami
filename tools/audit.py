import asyncio, json, re, sys
from urllib.parse import urljoin, urlparse
from playwright.async_api import async_playwright

BASE = "http://127.0.0.1:9400"
AXE = open("node_modules/axe-core/axe.min.js").read()
OUT = "/home/claude/triami-website/docs/technische-audit.json"

async def main():
    results = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        ctx = await b.new_context(viewport={"width": 1280, "height": 900})
        pg = await ctx.new_page()
        await pg.goto(BASE + "/", wait_until="networkidle")
        # uitloggen zodat de admin-balk de audit niet vervuilt
        await ctx.clear_cookies()
        queue = ["/"]; seen = set(); external = set(); link_status = {}
        while queue:
            path = queue.pop(0)
            if path in seen: continue
            seen.add(path)
            errs = []
            pg.once("console", lambda m: errs.append(m.text) if m.type == "error" else None)
            resp = await pg.goto(BASE + path, wait_until="networkidle", timeout=60000)
            await pg.add_script_tag(content=AXE)
            axe = await pg.evaluate("axe.run(document, {runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21aa','best-practice']}})")
            info = await pg.evaluate("""() => {
                const q = s => [...document.querySelectorAll(s)];
                const hs = q('h1,h2,h3,h4,h5,h6').map(h => h.tagName + ': ' + h.textContent.trim().slice(0,60));
                return {
                  title: document.title, lang: document.documentElement.lang,
                  metaDesc: (document.querySelector('meta[name=description]')||{}).content || null,
                  og: q('meta[property^="og:"]').map(m => m.getAttribute('property')),
                  canonical: (document.querySelector('link[rel=canonical]')||{}).href || null,
                  h1: q('h1').length, headings: hs,
                  imgsNoAlt: q('img').filter(i => !i.hasAttribute('alt')).map(i => i.src),
                  links: q('a[href]').map(a => a.getAttribute('href')),
                  iframes: q('iframe').map(i => i.src),
                  skipLink: !!document.querySelector('a.skip-link, a[href="#wp--skip-link--target"]'),
                  hasSearch: !!document.querySelector('form[role=search], input[type=search]'),
                  wordCount: document.body.innerText.split(/\\s+/).length,
                  smallTargets: q('a,button').filter(e => { const r = e.getBoundingClientRect(); return r.width>0 && (r.height<24 || r.width<24); }).length
                };
            }""")
            for href in info["links"]:
                u = urljoin(BASE + path, href)
                pu = urlparse(u)
                if pu.scheme in ("mailto", "tel"): continue
                if pu.netloc == urlparse(BASE).netloc:
                    np = pu.path if pu.path.endswith("/") else pu.path + "/"
                    if "/wp-admin" in np or "/wp-login" in np: continue
                    if np not in seen and np not in queue: queue.append(np)
                else:
                    external.add(u)
            results[path] = {
                "status": resp.status if resp else None, "title": info["title"], "lang": info["lang"],
                "metaDesc": info["metaDesc"], "og": info["og"], "canonical": info["canonical"],
                "h1": info["h1"], "headings": info["headings"], "imgsNoAlt": info["imgsNoAlt"],
                "iframes": info["iframes"], "skipLink": info["skipLink"], "hasSearch": info["hasSearch"],
                "wordCount": info["wordCount"], "smallTargets": info["smallTargets"], "consoleErrors": errs,
                "axe": [{"id": v["id"], "impact": v["impact"], "help": v["help"], "nodes": len(v["nodes"]), "targets": [n["target"][0] for n in v["nodes"][:3]]} for v in axe["violations"]],
            }
            print(path, resp.status if resp else None, "axe:", len(axe["violations"]))
        # mobiel: alleen home + 2 pagina's op 400px
        mctx = await b.new_context(viewport={"width": 400, "height": 800}, is_mobile=True, has_touch=True)
        mp = await mctx.new_page()
        mobile = {}
        for path in ["/", "/trainingen/", "/lidmaatschap/", "/faq/"]:
            await mp.goto(BASE + path, wait_until="networkidle")
            m = await mp.evaluate("""() => ({
                hScroll: document.documentElement.scrollWidth > document.documentElement.clientWidth,
                scrollWidth: document.documentElement.scrollWidth,
                menuButton: !!document.querySelector('.wp-block-navigation__responsive-container-open'),
                smallTargets: [...document.querySelectorAll('a,button')].filter(e => { const r = e.getBoundingClientRect(); return r.width>0 && r.height<24; }).length,
                minFont: Math.min(...[...document.querySelectorAll('p,li,a,td,summary')].filter(e=>e.offsetParent).map(e => parseFloat(getComputedStyle(e).fontSize)))
            })""")
            # menu openen testen
            if m["menuButton"] and path == "/":
                await mp.click(".wp-block-navigation__responsive-container-open")
                await mp.wait_for_timeout(400)
                m["menuOpensWithItems"] = await mp.evaluate("document.querySelectorAll('.is-menu-open .wp-block-navigation-item').length")
            mobile[path] = m
            print("mobiel", path, m)
        results["_mobile"] = mobile
        results["_external"] = sorted(external)
        await b.close()
    json.dump(results, open(OUT, "w"), indent=1, ensure_ascii=False)
    print("geschreven:", OUT, "pagina's:", len([k for k in results if not k.startswith("_")]))

asyncio.run(main())
