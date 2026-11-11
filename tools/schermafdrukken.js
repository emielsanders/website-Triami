// Schermafdrukken (eerste scherm) van elke pagina voor de Word-reviewversie.
// Gebruik: node tools/schermafdrukken.js [basis-url]  (standaard de lokale Playground op poort 9400)
const { chromium } = require('playwright');
const path = require('path');
const base = process.argv[2] || 'http://127.0.0.1:9400';
const slugs = ['', 'vereniging', 'bestuur', 'trainers', 'activiteiten', 'teamcompetitie', 'clubcompetitie', 'clubkleding',
  'vertrouwenscontactpersoon', 'veilig-sportklimaat', 'trainingen', 'start2tri', 'lidmaatschap', 'faq', 'contact', 'privacy'];
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 1 });
  for (const s of slugs) {
    await p.goto(`${base}/${s}${s ? '/' : ''}`, { waitUntil: 'networkidle' });
    await p.addStyleTag({ content: '#wpadminbar{display:none!important} html{margin-top:0!important} header.wp-block-template-part{top:0!important}' });
    await p.waitForTimeout(300);
    const naam = s || 'home';
    await p.screenshot({ path: path.join(__dirname, '..', 'docs', 'schermen', `${naam}.jpg`), type: 'jpeg', quality: 80 });
    console.log(naam);
  }
  await b.close();
})();
