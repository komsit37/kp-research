import os as _os; _os.chdir(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
# CSS: shared report.css + this page's overrides (normal string -> literal braces)
CSS = '<link rel="stylesheet" href="report.css">\n<style>\n' + '.wrap{max-width:1000px}\n.kpi b{font-size:22px}\n.verdict{border-left-color:var(--b)} .verdict b{color:var(--b)}\ntr.hi td{background:#eef6ff}' + '\n</style>'
import json
hs=json.load(open('generators/data/hs_new.json',encoding='utf-8')); host=hs['host']; alloc=hs['alloc']; bh=hs['bh']
def y(n): return '¥{:,.0f}'.format(round(n))
PRICE=1_930_000_000; ALLIN=2_082_090_000; adr_sum=592729; adr_blend=adr_sum/22
commercial=466667*12; VAR=0.42; FIXED=2_460_126+1_163_316+289_092+500_000
def yld(adr,occ=0.50):
    fc=adr/adr_blend; sg=adr_sum*fc*365*occ; noi=(sg+commercial)-VAR*sg-FIXED
    return dict(per_unit=sg/22, noi=noi, nyp=noi/PRICE*100, nya=noi/ALLIN*100)
flat=yld(adr_blend); high=yld(bh); ny=yld(host['p4_newyear'])
arow=''.join(f"<tr><td>{l}</td><td class='num'>{n}</td><td class='num'>{y(r)}</td></tr>" for l,n,r in [('Cherry blossom (late Mar–Apr)',alloc[0][1],alloc[0][2]),('Golden Week',alloc[1][1],alloc[1][2]),('Summer holidays (Jul–Aug)',alloc[2][1],alloc[2][2]),('Autumn foliage (Nov)',alloc[3][1],alloc[3][2]),('Christmas / New Year',alloc[4][1],alloc[4][2]),('High-demand weekends',alloc[5][1],alloc[5][2])])
def srow(adr,note,hi=False):
    r=yld(adr); cls=" class='hi'" if hi else ''
    return f"<tr{cls}><td class='num'>{y(adr)}</td><td class='num'>{y(r['per_unit'])}</td><td class='num b'>{r['nyp']:.2f}%</td><td class='num'>{r['nya']:.2f}%</td><td class='muted'>{note}</td></tr>"
scen=(srow(adr_blend,'flat year-round (annual blended ADR)')+
 srow(bh,'high-season-concentrated 180 nights',hi=True)+
 srow(host['p3_autumn'],'autumn-level')+
 srow(host['p4_newyear'],'New-Year-level (only ~2 wks/yr available)'))
today='2026-05-29'
html=f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>High-Season Minpaku Strategy — Shibuya Canon Palace</title>
{CSS}</head><body>
<header><h1>High-Season-Only Minpaku Strategy</h1>
<div class="sub">Rent short-term only in high/mid-high season, ~50% annual occupancy (≈180 nights) to comply with the minpaku 180-night cap. Re-based on the corrected nearby ADR data ({today}).</div></header>
<div class="wrap">
<a class="backlink" href="index.html">← Dossier home</a>

<div class="verdict">
<b>Updated finding: with the corrected nearby comps, timing matters less than I first thought.</b> Within this micro-market the seasonal spread is modest and noisy (nearby winter rates are already high; the summer sample is thin) — so concentrating the 180 legal nights into "high season" (blended host ADR ≈ {y(bh)}) yields <b>{high['nyp']:.2f}% @50%</b>, essentially the <b>same as operating year-round at 50%</b> ({flat['nyp']:.2f}%). The real driver is the higher <b>overall</b> ADR (~{y(adr_blend)}), not the calendar. The one genuinely premium window is <b>New Year (~{y(host['p4_newyear'])} host)</b> — worth prioritising, but it's only ~2 weeks. The large high-season premium shown earlier was an artifact of the contaminated broad-area data.
</div>

<div class="kpis">
<div class="kpi g"><span>Flat year-round @50%</span><b>{flat['nyp']:.2f}%</b></div>
<div class="kpi g"><span>High-season @50%</span><b>{high['nyp']:.2f}%</b></div>
<div class="kpi b"><span>New Year host ADR</span><b>{y(host['p4_newyear'])}</b></div>
<div class="kpi"><span>vs long-term rent</span><b>2.87%</b></div>
</div>

<h2>180 legal nights — high-season calendar (corrected ADRs)</h2>
<table><tr><th>Window</th><th class="num">Nights</th><th class="num">Host ADR</th></tr>{arow}
<tr class="hi"><td>Blended</td><td class="num">180</td><td class="num">{y(bh)}</td></tr></table>
<div class="legend">Host ADR = nearby studio asking median × 0.849 (platform fees) × 0.75 (realism) — same basis as <a href="airbnb_adr_analysis.html">ADR Analysis</a>. New Year/sakura/autumn are measured; Golden Week, summer, weekends are reasoned estimates. Note summer ({y(host['p2_summer'])}) ≈ winter — little upside outside New Year.</div>

<h2>Net yield @50% occ by realized ADR</h2>
<table><tr><th class="num">Host ADR</th><th class="num">Rev/unit/yr</th><th class="num">Net yield (price)</th><th class="num">Net (all-in)</th><th>Note</th></tr>{scen}</table>
<div class="legend">Occupancy fixed at the 50% legal cap; only the nightly rate varies. Net yield on ¥1.93B price; all-in adds ¥152M (txn + ¥45M conversion).</div>

<div class="note">
<b>Takeaway.</b> Under corrected data the strategy choice is mostly about <b>ADR level and hitting the 180-night cap</b>, not seasonal timing. Operate year-round at ~50% for simplicity, but <b>block out and prioritise New Year</b> (and other true peak weekends) where rates are materially higher. The earlier "concentrate everything in peak" thesis no longer adds much. The genuine upgrade remains a <b>hybrid</b>: nightly minpaku in peak + 1-month+ furnished leases (not minpaku-capped) in troughs to avoid dark units.
</div>
<div class="muted">Generated {today}. ADR basis: <a href="airbnb_adr_analysis.html">airbnb_adr_analysis.html</a>. Companion: <code>airbnb_yield_model.html</code>.</div>
</div></body></html>"""
open('airbnb_highseason_strategy.html','w',encoding='utf-8').write(html)
print(f"rewrote high-season: flat@50 {flat['nyp']:.2f}% | high-season@50 {high['nyp']:.2f}% | NY-adr@50 {ny['nyp']:.2f}%")
