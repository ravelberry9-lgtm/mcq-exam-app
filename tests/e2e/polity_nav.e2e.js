// Playwright click-through of every way into a recall card and back out. Run with the preview server on :5099:
//   NODE_PATH=$(npm root -g) node tests/e2e/polity_nav.e2e.js [shotDir]
const { chromium } = require('playwright');
const B = process.env.BASE || 'http://localhost:5099/learn/polity/unit6';
const SHOTS = process.argv[2] || '';
const rows = []; let fails = 0;
function rec(vp, path, ok, note) { rows.push([vp, path, ok ? 'PASS' : 'FAIL', note]); if (!ok) fails++; console.log((ok ? 'PASS ' : 'FAIL ') + vp + ' | ' + path + ' | ' + note); }
const wait = (p, ms) => p.waitForTimeout(ms);
async function settle(p) { await p.waitForLoadState('load'); await wait(p, 700); }
async function nodeInView(p, sel = 'a.cd[data-id]') {
  return p.evaluate((sel) => { const h = innerHeight; for (const a of document.querySelectorAll(sel)) { const r = a.getBoundingClientRect(); if (r.top > h * 0.35 && r.bottom < h * 0.8) return a.dataset.id; } for (const a of document.querySelectorAll(sel)) { const r = a.getBoundingClientRect(); if (r.top > 60 && r.bottom < h) return a.dataset.id; } return null; }, sel);
}
async function treeState(p) {
  return p.evaluate(() => ({ y: Math.round((document.querySelector('main') || document.scrollingElement).scrollTop), hash: location.hash, path: location.pathname, hl: (document.querySelector('.nd.hl a.cd,.ls.hl a.cd') || {}).dataset?.id || null,
    tab: (document.querySelector('.tr-tabs [aria-selected=true]') || {}).dataset?.tab, q: document.getElementById('tr-q')?.value, pyq: document.getElementById('tr-pyq')?.checked,
    chip: (document.querySelector('#tr-chips [aria-pressed=true]') || {}).dataset?.chip }));
}
async function openFromTrees(p, tab, prep, sel) {
  await p.goto(B + '/recall/hub-not-used'.replace('/hub-not-used', '')); await settle(p); // hub first, so history has a page before Trees
  await p.goto(B + '/recall/trees#' + tab); await settle(p);
  if (prep) await prep(p);
  await p.evaluate(() => { const m = document.querySelector('main'); m.scrollTop = Math.min(m.scrollHeight - m.clientHeight, 2600); }); await wait(p, 500);
  const id = await nodeInView(p, sel || 'a.cd[data-id]'); const before = await treeState(p);
  const elTop = await p.evaluate((id) => document.querySelector(`a.cd[data-id="${id}"]`).getBoundingClientRect().top, id);
  await p.click(`${sel || 'a.cd'}[data-id="${id}"]`); await settle(p);
  return { id, before, elTop };
}
async function backCheck(p, vp, label, o, how) {
  const opened = await p.evaluate(() => document.getElementById('ac-detail')?.dataset.id);
  if (how === 'collapse') await p.click('#ac-collapse'); else if (how === 'xback') await p.click('#ac-xback'); else await p.goBack();
  await settle(p);
  const s = await treeState(p);
  const elTop = await p.evaluate((id) => { const e = document.querySelector(`a.cd[data-id="${id}"]`); return e ? e.getBoundingClientRect().top : null; }, o.id);
  const ok = opened === o.id && s.path.endsWith('/recall/trees') && s.hl === o.id && s.tab === o.before.tab && elTop !== null && Math.abs(elTop - o.elTop) < 40 &&
    s.q === o.before.q && s.pyq === o.before.pyq && (s.chip || '') === (o.before.chip || '');
  rec(vp, label + ' → ' + how, ok, `node ${o.id} top ${Math.round(o.elTop)}→${elTop === null ? '-' : Math.round(elTop)}, scrollY ${o.before.y}→${s.y}, tab ${s.tab}, hl ${s.hl}, q "${s.q}" pyq ${s.pyq} chip ${s.chip || ''}`);
  return s;
}
(async () => {
  const b = await chromium.launch();
  for (const [w, h, vp] of [[400, 800, 'phone 400x800'], [1280, 900, 'desktop 1280x900']]) {
    const ctx = await b.newContext({ viewport: { width: w, height: h }, hasTouch: w < 500 });
    const p = await ctx.newPage(); p.on('pageerror', (e) => rec(vp, 'JS error', false, e.message));
    // Trees, each tab, each way out
    for (const tab of ['am', 'case', 'both', 'lines']) for (const how of ['collapse', 'back', 'xback']) {
      const o = await openFromTrees(p, tab); await backCheck(p, vp, 'Trees ' + tab, o, how);
      if (tab === 'am' && how === 'collapse' && SHOTS) await p.screenshot({ path: `${SHOTS}/after_trees_return_${w}.png` });
    }
    // Trees with filters and with search
    let o = await openFromTrees(p, 'case', async (p) => { if (await p.isHidden('#tr-sheet')) await p.click('#tr-fbtn'); await p.click('#tr-chips button[data-chip]:nth-child(3)'); await p.check('#tr-pyq'); await wait(p, 400); });
    await backCheck(p, vp, 'Trees case + theme chip + PYQ filter', o, 'collapse');
    o = await openFromTrees(p, 'case', async (p) => { await p.fill('#tr-q', 'nath'); await wait(p, 600); });
    await backCheck(p, vp, 'Trees search results', o, 'back');
    // Together: a relation ↳ jump, then open the node it landed on
    await p.goto(B + '/recall'); await p.goto(B + '/recall/trees#both'); await settle(p);
    const go = await p.evaluate(() => { const a = [...document.querySelectorAll('a.rl[data-go]')][8]; return a && a.dataset.go; });
    await p.click(`a.rl[data-go="${go}"] >> nth=0`).catch(() => {}); await wait(p, 1200);
    await wait(p, 1200); // smooth scroll settles
    const bt = await treeState(p);
    const top = await p.evaluate((id) => { const a = document.querySelector(`a.cd[data-id="${id}"]`); const t = a.closest('.nd').getBoundingClientRect().top; a.click(); return a.getBoundingClientRect().top + 0 * t; }, go); // tap without auto-scroll
    await settle(p);
    await backCheck(p, vp, 'Trees both ↳ relation jump', { id: go, before: bt, elTop: top }, 'collapse');
    // no double-back trap: Trees → card → Back → Back leaves Trees for the hub
    o = await openFromTrees(p, 'am'); await p.goBack(); await settle(p); await p.goBack(); await settle(p);
    rec(vp, 'Trees → card → Back → Back', /\/recall$/.test(new URL(p.url()).pathname), 'lands on ' + new URL(p.url()).pathname);
    // forward again re-opens the card, back returns to Trees
    await p.goForward(); await settle(p); await p.goForward(); await settle(p);
    const fid = await p.evaluate(() => document.getElementById('ac-detail')?.dataset.id);
    await p.goBack(); await settle(p); const fs = await treeState(p);
    rec(vp, 'browser forward to card, back again', fid === o.id && fs.hl === o.id, `forward card ${fid}, back hl ${fs.hl}`);
    // deck matrix → card → collapse: same matrix page, tile highlighted
    await p.goto(B + '/recall/amendments'); await settle(p);
    await p.click('#ac-start'); await wait(p, 600);
    if (await p.isEnabled('#ac-pnext')) { await p.click('#ac-pnext'); await wait(p, 400); }
    const pg = await p.textContent('#ac-page'); const tile = await p.evaluate(() => { const t = document.querySelectorAll('.ac-tile'); return t[Math.min(3, t.length - 1)].dataset.i; });
    await p.click(`.ac-tile[data-i="${tile}"]`); await wait(p, 900); await p.click('#ac-collapse'); await wait(p, 900);
    let hl = await p.evaluate(() => document.querySelector('.ac-tile.ac-hl')?.dataset.i);
    rec(vp, 'Deck matrix → card → collapse', hl === tile && (await p.textContent('#ac-page')) === pg && await p.isHidden('#ac-detail'), `page ${pg}, tile ${tile}, highlighted ${hl}`);
    await p.click(`.ac-tile[data-i="${tile}"]`); await wait(p, 900); await p.goBack(); await wait(p, 900);
    hl = await p.evaluate(() => document.querySelector('.ac-tile.ac-hl')?.dataset.i);
    rec(vp, 'Deck matrix → card → phone Back', hl === tile && await p.isHidden('#ac-detail') && await p.isVisible('#ac-grid'), `highlighted ${hl}`);
    // card → in-text link to another deck's card → collapse / back → first card; again → its matrix
    let first = null, xl = null;
    for (let i = 0; i < 25 && !xl; i++) {
      const t = await p.evaluate((i) => document.querySelectorAll('.ac-tile')[i]?.dataset.i, i % 18); if (t == null) break;
      if (await p.isHidden('#ac-detail')) { await p.click(`.ac-tile[data-i="${t}"]`); await wait(p, 900); }
      xl = await p.evaluate(() => { const a = [...document.querySelectorAll('#ac-detail a.xl[data-go]')].find((a) => a.dataset.deck && a.dataset.deck !== 'amendments'); return a ? a.dataset.go : null; });
      first = await p.evaluate(() => document.getElementById('ac-detail').dataset.id);
      if (!xl) { await p.click('#ac-next'); await wait(p, 700); }
    }
    if (xl) {
      for (const how of ['collapse', 'back']) {
        await p.click(`#ac-detail a.xl[data-go="${xl}"] >> nth=0`); await settle(p);
        const there = await p.evaluate(() => document.getElementById('ac-detail').dataset.id);
        if (how === 'collapse') await p.click('#ac-collapse'); else await p.goBack();
        await settle(p);
        const now = await p.evaluate(() => !document.getElementById('ac-detail').hidden && document.getElementById('ac-detail').dataset.id);
        rec(vp, `Card → cross-deck link → ${how}`, there === xl && now === first, `${first} → ${there} → back on ${now}`);
      }
      await p.click('#ac-collapse'); await wait(p, 900);
      rec(vp, 'Cross-deck return, then collapse first card', await p.isHidden('#ac-detail') && await p.isVisible('#ac-grid'), 'matrix shown: ' + await p.isVisible('#ac-grid'));
    } else rec(vp, 'Card → cross-deck link', false, 'no cross-deck link found');
    // Related row (?for=) → matrix → card → collapse → exit → first card
    await p.goto(B + '/recall/cases?open=CS-kesavananda-1973'); await settle(p);
    const fa = await p.evaluate(() => { const a = document.querySelector('#ac-detail a[data-for]'); return a && a.getAttribute('href'); });
    if (fa) {
      await p.click('#ac-detail a[data-for] >> nth=0'); await settle(p);
      await p.click('.ac-tile >> nth=0'); await wait(p, 900); await p.click('#ac-collapse'); await wait(p, 800);
      const inFor = await p.isVisible('#ac-grid') && p.url().includes('for=');
      await p.click('#ac-exit'); await settle(p);
      const back = await p.evaluate(() => !document.getElementById('ac-detail').hidden && document.getElementById('ac-detail').dataset.id);
      rec(vp, 'Related row ?for= → matrix → card → collapse → exit', inFor && back === 'CS-kesavananda-1973', `for-matrix ${inFor}, back on ${back}`);
      await p.click('#ac-detail a[data-for] >> nth=0'); await settle(p); await p.goBack(); await settle(p);
      const back2 = await p.evaluate(() => !document.getElementById('ac-detail').hidden && document.getElementById('ac-detail').dataset.id);
      rec(vp, 'Related row ?for= → phone Back', back2 === 'CS-kesavananda-1973', 'back on ' + back2);
    } else rec(vp, 'Related row ?for=', false, 'no related link on Kesavananda');
    // PYQ chip inside a card scrolls the card only; collapse still goes back to Trees
    o = await openFromTrees(p, 'case', null, 'a.cd:has(.tg.q)');
    const pq = await p.$('#ac-detail a[data-pyq]'); if (pq) { await pq.click(); await wait(p, 600); }
    rec(vp, 'PYQ chip in card (no history entry)', new URL(p.url()).search.includes('open='), 'pyq chip ' + (pq ? 'clicked' : 'absent'));
    await backCheck(p, vp, 'Trees case → PYQ chip', o, 'collapse');
    // Fresh deep links (new tab, no history)
    const q = await ctx.newPage(); await q.goto(B + '/recall/cases?open=CS-kesavananda-1973'); await settle(q);
    await q.click('#ac-collapse'); await wait(q, 900);
    rec(vp, 'Fresh deep link → collapse', await q.isVisible('#ac-grid') && await q.isHidden('#ac-detail') && (await q.evaluate(() => document.querySelector('.ac-tile.ac-hl') !== null)), 'deck matrix with card highlighted');
    await q.click('#ac-exit'); await wait(q, 600);
    rec(vp, 'Fresh deep link → collapse → exit', await q.isVisible('#ac-start'), 'deck setup');
    await q.goto(B + '/recall/amendments'); await settle(q);
    const amId = await q.evaluate(() => JSON.parse(document.getElementById('ac-data').textContent).cards[30].id);
    await q.close();
    const r = await ctx.newPage(); await r.goto(B + `/recall/amendments?open=${amId}&back=trees:am`); await settle(r);
    await r.click('#ac-collapse'); await settle(r); const rs = await treeState(r);
    rec(vp, 'Fresh deep link with back=trees → collapse', rs.path.endsWith('/recall/trees') && rs.hl === amId, `trees ${rs.hash}, hl ${rs.hl}`); await r.close();
    // Hub and Polity page tiles → deck, back
    await p.goto(B + '/recall'); await settle(p);
    await p.click('a[href$="/recall/amendments"] >> nth=0'); await settle(p); await p.goBack(); await settle(p);
    rec(vp, 'Hub tile → deck → Back', /\/recall$/.test(new URL(p.url()).pathname), new URL(p.url()).pathname);
    await p.goto(B + '/'); await settle(p);
    const tl = await p.$('a[href*="/recall/"]'); if (tl) { await tl.click(); await settle(p); await p.goBack(); await settle(p); }
    rec(vp, 'Polity page tile → deck → Back', new URL(p.url()).pathname.replace(/\/$/, '').endsWith('/unit6'), new URL(p.url()).pathname);
    await ctx.close();
  }
  await b.close();
  require('fs').writeFileSync(process.env.OUT || '/dev/null', JSON.stringify(rows));
  console.log(fails ? fails + ' FAILED' : 'ALL PASS'); process.exit(fails ? 1 : 0);
})();
