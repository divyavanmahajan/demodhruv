// Generates claims-and-sources.html (the published artifact) from claims.json.
// Run: node build_claims_html.js
const fs = require('fs');
const path = require('path');
const claims = require('./claims.json');

const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const data = JSON.stringify(claims).replace(/<\//g, '<\\/');

const html = `<title>AI Code Debt Evidence Ledger</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root{
  --bg:#F5F6F8; --surface:#FFFFFF; --ink:#1B1F27; --ink-2:#4A515E; --ink-3:#7A8290;
  --line:#DDE1E7; --accent:#0F6E8C; --accent-ink:#FFFFFF; --accent-soft:#E3F0F5;
  --high:#1E6B3F; --high-bg:#E2F3E8; --med:#8A5200; --med-bg:#FBEEDB; --low:#8F2E33; --low-bg:#F9E3E4;
  --row:#FAFBFC; --focus:#0F6E8C;
}
@media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){
  --bg:#14171C; --surface:#1C2027; --ink:#E7E9ED; --ink-2:#B4BAC5; --ink-3:#818897;
  --line:#2E343E; --accent:#5CB8D3; --accent-ink:#0E1418; --accent-soft:#1E3038;
  --high:#7FD3A0; --high-bg:#173A27; --med:#F0B85A; --med-bg:#3B2C10; --low:#F09096; --low-bg:#3E1F22;
  --row:#191D24; --focus:#5CB8D3;
}}
:root[data-theme="dark"]{
  --bg:#14171C; --surface:#1C2027; --ink:#E7E9ED; --ink-2:#B4BAC5; --ink-3:#818897;
  --line:#2E343E; --accent:#5CB8D3; --accent-ink:#0E1418; --accent-soft:#1E3038;
  --high:#7FD3A0; --high-bg:#173A27; --med:#F0B85A; --med-bg:#3B2C10; --low:#F09096; --low-bg:#3E1F22;
  --row:#191D24; --focus:#5CB8D3;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;font-size:14px;line-height:1.5}
.wrap{max-width:1360px;margin:0 auto;padding-inline:20px;padding-block:28px 56px}
header{display:flex;flex-wrap:wrap;gap:20px 40px;align-items:flex-end;justify-content:space-between;border-bottom:1px solid var(--line);padding-bottom:20px;margin-bottom:20px}
h1{font-size:26px;font-weight:600;letter-spacing:-0.01em;margin:0 0 6px;text-wrap:balance}
.sub{color:var(--ink-2);max-width:68ch;margin:0}
.sub a{color:var(--accent)}
.stats{display:flex;gap:22px;flex-wrap:wrap}
.stat{min-width:74px}
.stat b{display:block;font-size:24px;font-weight:600;font-variant-numeric:tabular-nums;line-height:1.1}
.stat span{font-size:11.5px;color:var(--ink-3);text-transform:uppercase;letter-spacing:.06em}
.stat.high b{color:var(--high)} .stat.med b{color:var(--med)} .stat.low b{color:var(--low)}
.controls{display:flex;flex-wrap:wrap;gap:10px 14px;align-items:center;margin-bottom:14px}
.controls label{font-size:12px;color:var(--ink-3);text-transform:uppercase;letter-spacing:.06em;display:flex;align-items:center;gap:8px}
select,input[type=search]{font:inherit;color:var(--ink);background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:7px 10px;min-width:150px}
input[type=search]{min-width:240px;flex:1 1 240px}
select:focus-visible,input:focus-visible,button:focus-visible,a:focus-visible{outline:2px solid var(--focus);outline-offset:2px}
.chips{display:flex;gap:6px;flex-wrap:wrap}
.chip{font:inherit;font-size:12.5px;padding:5px 11px;border-radius:999px;border:1px solid var(--line);background:var(--surface);color:var(--ink-2);cursor:pointer}
.chip[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}
.count{color:var(--ink-3);font-size:12.5px;margin-left:auto;font-variant-numeric:tabular-nums}
.tablewrap{overflow-x:auto;border:1px solid var(--line);border-radius:8px;background:var(--surface)}
table{border-collapse:collapse;width:100%;min-width:1100px}
th,td{text-align:left;vertical-align:top;padding:10px 12px;border-bottom:1px solid var(--line)}
th{position:sticky;top:0;background:var(--surface);font-size:11.5px;text-transform:uppercase;letter-spacing:.06em;color:var(--ink-3);font-weight:500;z-index:1;cursor:pointer;user-select:none;white-space:nowrap}
th[aria-sort="ascending"]::after{content:" \\2191"} th[aria-sort="descending"]::after{content:" \\2193"}
tbody tr:nth-child(even){background:var(--row)}
td.id,td.date{font-family:"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace;font-size:12.5px;white-space:nowrap;color:var(--ink-2)}
td.claim{min-width:340px;max-width:520px}
td.src{min-width:200px;max-width:280px}
td.src a{color:var(--accent);text-decoration:none;border-bottom:1px solid color-mix(in srgb,var(--accent) 40%,transparent)}
td.src a:hover{border-bottom-color:var(--accent)}
td.src small{display:block;color:var(--ink-3);margin-top:2px}
td.type{color:var(--ink-2);min-width:130px}
td.note{color:var(--ink-3);font-size:12.5px;min-width:200px;max-width:300px}
td.note a{color:var(--accent);word-break:break-all}
.theme{display:inline-block;font-size:11.5px;color:var(--ink-3);letter-spacing:.02em;white-space:nowrap}
.grade{display:inline-block;font-size:11.5px;font-weight:600;padding:2px 8px;border-radius:4px;white-space:nowrap}
.g-high{color:var(--high);background:var(--high-bg)} .g-med{color:var(--med);background:var(--med-bg)} .g-low{color:var(--low);background:var(--low-bg)}
.flag{display:inline-block;margin-left:6px;font-size:11px;color:var(--low);font-weight:600;letter-spacing:.04em}
.empty{padding:28px;color:var(--ink-3);text-align:center}
footer{margin-top:18px;color:var(--ink-3);font-size:12.5px;max-width:90ch}
footer a{color:var(--accent)}
@media (max-width:640px){
  h1{font-size:22px} .stat b{font-size:20px}
  table{min-width:0} thead{display:none}
  tbody tr{display:block;padding:10px 12px;border-bottom:1px solid var(--line)} tbody td{display:block;border:0;padding:3px 0;max-width:none;min-width:0}
  td.id::before{content:"";}
  td.type::before{content:"Type: ";color:var(--ink-3)} td.date::before{content:"Date: ";color:var(--ink-3)}
  td.note:empty{display:none}
}
@media (prefers-reduced-motion:no-preference){ .chip{transition:background .12s,color .12s} }
</style>
<div class="wrap">
<header>
  <div>
    <h1>AI Code Debt Evidence Ledger</h1>
    <p class="sub">Every claim used in the research paper <em>AI-Generated Code as the New Technical Debt</em> (12 September 2026), with its source, evidence type and grade. Grades: <b>High</b> = peer-reviewed, large-sample survey with methodology, primary vendor document about that vendor, or primary incident record; <b>Med</b> = vendor study with disclosed methodology, analyst report via secondary coverage, or credible practitioner analysis; <b>Low</b> = anecdotal or untraceable to a primary. <b>UNVERIFIED</b> marks figures reachable only through secondary coverage.</p>
  </div>
  <div class="stats" id="stats"></div>
</header>
<div class="controls">
  <label>Theme <select id="theme"><option value="">All</option></select></label>
  <label>Stream <select id="stream"><option value="">All</option></select></label>
  <div class="chips" id="grades" role="group" aria-label="Grade filter"></div>
  <input type="search" id="q" placeholder="Search claims, sources, organisations" aria-label="Search">
  <span class="count" id="count"></span>
</div>
<div class="tablewrap">
<table id="t">
<thead><tr>
  <th data-k="id">ID</th><th data-k="theme">Theme</th><th data-k="claim">Claim</th><th data-k="source">Source</th><th data-k="date">Date</th><th data-k="type">Type</th><th data-k="strength">Grade</th><th data-k="note">Verification note</th>
</tr></thead>
<tbody id="rows"></tbody>
</table>
</div>
<footer>Prefix key: P = premise (autonomous generation at scale), E = empirical debt evidence, C = comprehension and framing, S = security, D = dependency, T = strategic trend, M = mitigation. Streams 1-6 are the research subagents that surfaced each source. The paper, the prompts, the raw stream outputs and this table as JSON are kept together in the research repository.</footer>
</div>
<script id="data" type="application/json">${data}</script>
<script>
(function(){
  const claims = JSON.parse(document.getElementById('data').textContent);
  const $ = s => document.querySelector(s);
  const gradeKey = s => /^high/i.test(s) ? 'high' : /^low/i.test(s) ? 'low' : 'med';
  const themes = [...new Set(claims.map(c => c.theme.split(':')[0]))];
  const streams = [...new Set(claims.map(c => c.stream))].sort();
  const streamNames = {1:'1 Empirical quality',2:'2 Autonomous generation',3:'3 Comprehension & lock-in',4:'4 Security & incidents',5:'5 Corporate mitigations',6:'6 Strategic trends'};
  for (const t of themes) $('#theme').insertAdjacentHTML('beforeend', '<option>'+t+'</option>');
  for (const s of streams) $('#stream').insertAdjacentHTML('beforeend', '<option value="'+s+'">'+(streamNames[s]||s)+'</option>');
  const counts = {high:0, med:0, low:0};
  claims.forEach(c => counts[gradeKey(c.strength)]++);
  $('#stats').innerHTML = '<div class="stat"><b>'+claims.length+'</b><span>claims</span></div>'
    + '<div class="stat high"><b>'+counts.high+'</b><span>High</span></div>'
    + '<div class="stat med"><b>'+counts.med+'</b><span>Med</span></div>'
    + '<div class="stat low"><b>'+counts.low+'</b><span>Low</span></div>';
  const gradeState = {high:true, med:true, low:true};
  for (const g of ['high','med','low']) {
    const b = document.createElement('button'); b.className='chip'; b.textContent = g[0].toUpperCase()+g.slice(1); b.setAttribute('aria-pressed','true');
    b.onclick = () => { gradeState[g] = !gradeState[g]; b.setAttribute('aria-pressed', String(gradeState[g])); render(); };
    $('#grades').appendChild(b);
  }
  let sortK = null, sortDir = 1;
  const esc = s => String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  const linkify = s => esc(s).replace(/https?:\\/\\/[^\\s)]+/g, u => '<a href="'+u+'" target="_blank" rel="noopener">'+u.replace(/^https?:\\/\\//,'').slice(0,60)+(u.length>68?'…':'')+'</a>');
  function render(){
    const q = $('#q').value.trim().toLowerCase(), th = $('#theme').value, st = $('#stream').value;
    let rows = claims.filter(c => gradeState[gradeKey(c.strength)]
      && (!th || c.theme.split(':')[0] === th) && (!st || c.stream === st)
      && (!q || (c.claim+' '+c.source+' '+c.org+' '+c.note+' '+c.theme+' '+c.id).toLowerCase().includes(q)));
    if (sortK) rows = rows.slice().sort((a,b) => sortDir * String(a[sortK]).localeCompare(String(b[sortK]), undefined, {numeric:true}));
    $('#count').textContent = rows.length + ' of ' + claims.length + ' claims';
    $('#rows').innerHTML = rows.length ? rows.map(c => {
      const g = gradeKey(c.strength), unv = /UNVERIFIED/.test(c.strength) || /UNVERIFIED/.test(c.note||'');
      return '<tr><td class="id">'+esc(c.id)+'</td><td><span class="theme">'+esc(c.theme)+'</span></td>'
        + '<td class="claim">'+esc(c.claim)+'</td>'
        + '<td class="src"><a href="'+esc(c.url)+'" target="_blank" rel="noopener">'+esc(c.source)+'</a><small>'+esc(c.org)+'</small></td>'
        + '<td class="date">'+esc(c.date)+'</td><td class="type">'+esc(c.type)+'</td>'
        + '<td><span class="grade g-'+g+'">'+esc(c.strength.replace(/\\s*\\(UNVERIFIED[^)]*\\)/,''))+'</span>'+(unv?'<span class="flag">UNVERIFIED</span>':'')+'</td>'
        + '<td class="note">'+linkify(c.note)+'</td></tr>';
    }).join('') : '<tr><td colspan="8" class="empty">No claims match these filters.</td></tr>';
  }
  document.querySelectorAll('th[data-k]').forEach(th => th.onclick = () => {
    const k = th.dataset.k; if (sortK === k) sortDir = -sortDir; else { sortK = k; sortDir = 1; }
    document.querySelectorAll('th[data-k]').forEach(x => x.removeAttribute('aria-sort'));
    th.setAttribute('aria-sort', sortDir === 1 ? 'ascending' : 'descending'); render();
  });
  ['#q','#theme','#stream'].forEach(s => $(s).addEventListener('input', render));
  render();
})();
</script>
`;
const out = path.join(__dirname, 'claims-and-sources.html');
fs.writeFileSync(out, html);
console.log('wrote', out, html.length, 'bytes');
