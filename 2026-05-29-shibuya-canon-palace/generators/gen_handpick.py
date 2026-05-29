import os as _os; _os.chdir(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
# CSS: shared report.css + this page's overrides (normal string -> literal braces)
CSS = '<link rel="stylesheet" href="report.css">\n<style>\n' + 'body{font-size:14.5px}\n.kpi b{font-size:20px}\n.scrollx{border:1px solid var(--line);border-radius:8px}\ntable{border:none;border-radius:0;margin:0} .std table{border:1px solid var(--line);border-radius:8px;margin:8px 0}\nth,td{padding:6px 9px;font-size:12.5px;white-space:nowrap}\nth{font-size:10.5px;letter-spacing:.02em}\ntd.ti{color:#555;max-width:220px;overflow:hidden;text-overflow:ellipsis}\ntd.base{background:#eef6ff}\ntd.ph img{width:88px;height:60px;object-fit:cover;border-radius:5px;display:block} td.ph{padding:4px 6px}\n.mut{color:var(--mut);font-size:10px}\n.find{border-left:5px solid var(--o)} .find b{color:var(--o)}\n.note{margin:12px 0}' + '\n</style>'
import json, html
d=json.load(open('generators/data/hp2.json',encoding='utf-8'))
FAC=d['FAC']; MID=d['MID']; TOP=d['TOP']; b1=d['b1']; b2_60=d['b2_60']; b2_lg=d['b2_lg']
mult=d['mult']; hs=d['hs']; rates=d['rates']; META=d['meta']; setof=d['setof']
periods=[('p1_winter','Winter','base'),('p2_summer','Summer','base'),('p3_autumn','Autumn','mid-pk'),('p4_newyear','New Year','top-pk'),('p5_sakura','Sakura','mid-pk')]
pk=[p[0] for p in periods]
def y(n): return '¥{:,.0f}'.format(round(n)) if n else '—'
def host(x): return round(x)
def rowhtml(i):
    m=META.get(i,{}); r=rates.get(i,{})
    cells=''.join(f"<td class='num{' base' if p in ('p1_winter','p2_summer') else ''}'>{y(r.get(p))}</td>" for p in pk)
    sz=(str(m['sqm'])+' m²') if m.get('sqm') else "<span class='mut'>n/a</span>"
    ph=f"<td class='ph'><a href='https://www.airbnb.com/rooms/{i}' target='_blank'><img loading='lazy' src='images/adr/{i}.jpg' onerror=\"this.style.display='none'\"></a></td>"
    return f"<tr>{ph}<td><a href='https://www.airbnb.com/rooms/{i}' target='_blank'>{i}</a></td><td>{html.escape(m.get('loc','')[:11])}</td><td class='num'>{sz}</td><td>{m.get('beds','')}</td><td class='ti'>{html.escape(m.get('title','')[:34])}</td>{cells}</tr>"
phead=''.join(f"<th class='num'>{l}<br><span class='mut'>{tag}</span></th>" for _,l,tag in periods)
rows1=''.join(rowhtml(i) for i in d['br1'])
rows2=''.join(rowhtml(i) for i in d['br2'])
today='2026-05-29'
doc=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>ADR — hand-picked comps (base + peak multipliers)</title>
{CSS}</head><body>
<header><h1>ADR — hand-picked comps: base rate + peak multipliers</h1>
<div class="sub">8 chosen 1BR (2 guests) + 3 chosen 2BR (4 guests) near Shibuya 2-chome, re-probed with fallback dates across 5 seasons. All-in per night. {today}.</div></header>
<div class="wrap">
<a class="backlink" href="index.html">← Dossier home</a>

<div class="tldr">
<b>Method change you steered me to.</b> The comps barely flex for peak (autumn/sakura come in at 1.0–1.26× their own base) and the true New Year week was <b>sold out</b> on most — i.e. they use near-flat pricing and fill up, so <b>observed peak is a floor, not the achievable rate.</b> So I take the <b>base (normal) ADR from the data</b> (all-in asking) and apply <b>your peak multipliers</b> (mid-peak ×1.5, New Year ×2.0) for the upside. (Platform fee left out here — add ×0.849 in the model.)
<br><br><b>Base estimated ADR (all-in asking):</b> 1BR <b>¥{host(b1):,}</b> · 2BR-60 m² <b>¥{host(b2_60):,}</b> · 2BR-large <b>¥{host(b2_lg):,}</b>.
</div>

<div class="kpis">
<div class="kpi b"><span>1BR base ADR (all-in)</span><b>¥{host(b1):,}</b></div>
<div class="kpi"><span>2BR-60 m² base ADR</span><b>¥{host(b2_60):,}</b></div>
<div class="kpi"><span>New Year (×2)</span><b>¥{host(b1*TOP):,}</b><span>1BR top-peak</span></div>
<div class="kpi g"><span>2BR-60 ÷ 2×1BR</span><b>{host(b2_60)/(2*host(b1))*100:.0f}%</b></div>
</div>

<h2>Refreshed data — all-in per night (first available date per season)</h2>
<div class="muted">Blue = base/normal season (winter, summer). Blanks = unavailable / sold out across all 3 candidate dates tried.</div>
<h3>1BR (2 guests)</h3>
<div class="scrollx"><table><tr><th>Photo</th><th>Listing</th><th>Loc</th><th class="num">Size</th><th>Beds</th><th>Title</th>{phead}</tr>{rows1}</table></div>
<h3>2BR (4 guests)</h3>
<div class="scrollx"><table><tr><th>Photo</th><th>Listing</th><th>Loc</th><th class="num">Size</th><th>Beds</th><th>Title</th>{phead}</tr>{rows2}</table></div>

<h2>The finding: flat pricing + New Year sell-outs</h2>
<div class="note find">
Observed peak-vs-own-base ratios are tiny: 1BR autumn 1.06–1.07×, sakura 1.12–1.26×; 2BR autumn 0.97–1.09×, sakura 1.00×. The 2BR comp <code>1578848</code> literally shows the same ¥81,217 in winter, summer and sakura — <b>a flat year-round price.</b> Meanwhile the true New Year week (Dec 29–Jan 2) returned <b>no availability</b> on both 2BRs and several 1BRs. <b>Conclusion (your point): these hosts underprice peak and sell out</b>, so their listed peak rates understate what the dates can actually fetch. Hence: trust the data for <b>base</b>, model peak with multipliers.
</div>

<h2>ADR table — base × your peak multipliers</h2>
<div class="std"><table>
<tr><th>Unit</th><th class="num">Base (all-in)</th><th class="num">Mid-peak ×{MID}</th><th class="num">New Year ×{TOP}</th></tr>
<tr><td>1BR</td><td class="num b">¥{host(b1):,}</td><td class="num">¥{host(b1*MID):,}</td><td class="num">¥{host(b1*TOP):,}</td></tr>
<tr><td>2BR · 60 m² (2-studio-merge analog)</td><td class="num b">¥{host(b2_60):,}</td><td class="num">¥{host(b2_60*MID):,}</td><td class="num">¥{host(b2_60*TOP):,}</td></tr>
<tr><td>2BR · large (~80–100 m²)</td><td class="num b">¥{host(b2_lg):,}</td><td class="num">¥{host(b2_lg*MID):,}</td><td class="num">¥{host(b2_lg*TOP):,}</td></tr>
</table></div>
<div class="muted">Base = median of winter+summer observed all-in (asking). The ~15% Airbnb platform fee (×0.849) is applied later in the model, not here. Multipliers are your assumption (mid-peak = sakura/autumn/Obon/GW; top-peak = New Year/Christmas).</div>

<h2>Blended ADR — where the multipliers matter</h2>
<div class="std"><table>
<tr><th>Operating mode</th><th class="num">Blended mult.</th><th class="num">1BR ADR</th><th class="num">2BR-60 ADR</th></tr>
<tr><td>Flat, year-round</td><td class="num">×{mult}</td><td class="num">¥{host(b1*mult):,}</td><td class="num">¥{host(b2_60*mult):,}</td></tr>
<tr style="background:#f0f8f1"><td class="b">Minpaku high-season-only (180 nts concentrated in peak)</td><td class="num b">×{hs}</td><td class="num b">¥{host(b1*hs):,}</td><td class="num b">¥{host(b2_60*hs):,}</td></tr>
</table></div>
<div class="note">
Key nuance: peaks are only ~9 weeks/year, so for <b>flat year-round</b> operation they lift the blended ADR just ~{ (mult-1)*100:.0f}% above base. But the <b>minpaku 180-night cap lets you sell <i>only</i> the best nights</b> — concentrating in New Year (×2) + mid-peaks (×1.5) raises the effective ADR ~{(hs-1)*100:.0f}% (1BR ≈ ¥{host(b1*hs):,}). So your peak-multiplier insight is decisive for the legal high-season strategy, not for a flat model.
</div>

<h2>2BR vs two 1BRs (at base, all-in ADR)</h2>
<div class="std"><table>
<tr><th>Config</th><th class="num">ADR (all-in)</th><th class="num">vs 2×1BR</th></tr>
<tr style="background:#f0f8f1"><td class="b">2 × 1BR</td><td class="num b">¥{2*host(b1):,}</td><td class="num">100%</td></tr>
<tr><td>1 × 2BR · 60 m² (realistic merge)</td><td class="num">¥{host(b2_60):,}</td><td class="num">{host(b2_60)/(2*host(b1))*100:.0f}% ({host(b2_60)/host(b1):.2f}×)</td></tr>
<tr><td>1 × 2BR · large (~80–100 m²)</td><td class="num">¥{host(b2_lg):,}</td><td class="num">{host(b2_lg)/(2*host(b1))*100:.0f}% ({host(b2_lg)/host(b1):.2f}×)</td></tr>
</table></div>
<div class="note warn">
On <b>base ADR</b>, a realistic 2-studio→2BR merge (~60 m²) earns <b>{host(b2_60)/(2*host(b1))*100:.0f}% of two 1BRs</b> ({host(b2_60)/host(b1):.2f}×) — slightly behind on ADR, but it needs only <b>one cleaning turnover and one listing</b>, and serves families/groups. Only an <b>80–100 m²</b> 2BR actually beats two 1BRs on ADR ({host(b2_lg)/(2*host(b1))*100:.0f}%), and that needs more floor area than two studios provide. The remodel verdict therefore rests on the <b>opex/occupancy</b> side — the investment thesis to run next.
</div>
<div class="muted">Generated {today}. Figures are <b>estimated ADR = all-in asking nightly</b>; apply the ~15% platform fee (×0.849) when you model net revenue. Peak multipliers (×{MID}/×{TOP}) are an explicit assumption you supplied. Companion: <code>airbnb_adr_analysis.html</code>.</div>
</div></body></html>"""
open('airbnb_adr_handpick.html','w',encoding='utf-8').write(doc)
print(f"rebuilt | 1BR base host ¥{host(b1):,} | 2BR-60 ¥{host(b2_60):,} | flat-blend 1BR ¥{host(b1*mult):,} | HS 1BR ¥{host(b1*hs):,}")
