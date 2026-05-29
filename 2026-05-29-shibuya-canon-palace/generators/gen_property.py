import os as _os; _os.chdir(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
# CSS: shared report.css + this page's overrides (normal string -> literal braces)
CSS = '<link rel="stylesheet" href="report.css">\n<style>\n' + '.wrap{max-width:1080px}\ntd.rm{font-weight:700} td.k{color:#555;width:42%}\ntr.vacrow td{background:#fff6f4}\n.occ{color:var(--g);font-size:12px;font-weight:600} .vac{color:var(--r);font-size:12px;font-weight:600}\n.rem{color:var(--mut);font-size:12px}\n.group{background:#eef;font-weight:700}\n.imgs{display:flex;gap:14px;flex-wrap:wrap} .imgs figure{margin:0;flex:1;min-width:300px}\n.imgs img{width:100%;border:1px solid var(--line);border-radius:8px} figcaption{font-size:12px;color:var(--mut);margin-top:4px}\n.note{border-left:5px solid var(--a)}' + '\n</style>'
import csv, html
def y(v):
    try: return '¥{:,.0f}'.format(float(v))
    except: return v or '—'
rows=list(csv.DictReader(open('rent_roll.csv',encoding='utf-8')))

# headline / building data
headline=[('Asking price','¥1,930,000,000'),('Gross yield (listed)','2.45%'),
 ('Building size (GFA)','791.82 m²'),('Land area','213.38 m²'),('Land rights','Freehold'),
 ('Floors','9F (RC, flat roof)'),('Units','22 residential + 1F shop/office'),
 ('Completed','July 2013'),('Occupancy','Occupied (income-producing)'),('Available from','2026-02-27')]
building=[('Type / layout','Apartment · Whole Building'),('Structure','Reinforced Concrete (RC)'),
 ('Zoning','Residential (office use permitted)'),('Floor Area Ratio','500.0% (eff. 360% by road width)'),
 ('Building Coverage Ratio','80.0%'),('Direction facing','Southeast'),('Road width','5.99 m (public, N & SE)'),
 ('Location','Shibuya 2-chome, Shibuya-ku, Tokyo'),
 ('Nearest stations','Shibuya (JR Yamanote) 8 min · Omotesando (Metro) 8 min'),
 ('Transaction type','Non-Exclusive'),('Brokerage fee','price × 3% + 10% consumption tax'),
 ('Listing ref','AK002 — eXp Japan'),('Sheet date','2026-01-07')]

def unit_row(r):
    vac = r['status_current']=='vacant'
    badge = "<span class='vac'>vacant</span>" if vac else "<span class='occ'>occupied</span>"
    upbadge = "<span class='vac'>vacant</span>" if r['ups_status']=='vacant' else "<span class='occ'>occ</span>"
    rem = html.escape(r['cur_remarks']) if r['cur_remarks'] not in ('','recruiting') else ('募集中 / recruiting' if vac else '')
    cls = " class='vacrow'" if vac else ''
    return f"""<tr{cls}>
<td class='rm'>{r['room']}</td><td>{'Shop' if r['use']=='shop' else 'Resi'}</td><td>{badge}</td>
<td class='num'>{r['area_sqm']}</td><td class='num'>{r['area_tsubo']}</td>
<td class='num'>{y(r['cur_rent'])}</td><td class='num'>{y(r['cur_common'])}</td><td class='num b'>{y(r['cur_rent_plus_common'])}</td>
<td class='num'>{y(r['ups_rent'])}</td><td class='num b'>{y(r['ups_rent_plus_common'])}</td>
<td class='rem'>{rem}</td></tr>"""

unit_rows=''.join(unit_row(r) for r in rows)

# totals (from seller sheets)
totals={
 'cur':dict(area='521.07',tsubo='157.52',rent=2_859_667,common=239_500,rc=3_099_167),
 'man':dict(area='712.52',tsubo='215.40',rent=4_083_667,common=339_500,rc=4_423_167),
 'ups':dict(area='712.52',tsubo='215.40',rent=4_679_000,common=428_000,rc=5_107_000),
}
deposit=3_486_998
scn=f"""
<tr><th>Scenario</th><th class='num'>Leased area</th><th class='num'>Monthly rent</th><th class='num'>Monthly common</th><th class='num'>Rent + common /mo</th><th class='num'>Annualized ×12</th></tr>
<tr><td>Current (現況, in-place)</td><td class='num'>{totals['cur']['area']} m²</td><td class='num'>{y(totals['cur']['rent'])}</td><td class='num'>{y(totals['cur']['common'])}</td><td class='num b'>{y(totals['cur']['rc'])}</td><td class='num'>{y(totals['cur']['rc']*12)}</td></tr>
<tr><td>Full-occupancy assumption (満室想定)</td><td class='num'>{totals['man']['area']} m²</td><td class='num'>{y(totals['man']['rent'])}</td><td class='num'>{y(totals['man']['common'])}</td><td class='num b'>{y(totals['man']['rc'])}</td><td class='num'>{y(totals['man']['rc']*12)}</td></tr>
<tr class='hi'><td>Upside projection (アップサイド見込み)</td><td class='num'>{totals['ups']['area']} m²</td><td class='num'>{y(totals['ups']['rent'])}</td><td class='num'>{y(totals['ups']['common'])}</td><td class='num b'>{y(totals['ups']['rc'])}</td><td class='num'>{y(totals['ups']['rc']*12)}</td></tr>
"""

opex=f"""
<tr><th>Item</th><th class='num'>Current (税込/yr)</th><th class='num'>Upside (税込/yr)</th><th>Basis</th></tr>
<tr><td>PM (property mgmt)</td><td class='num'>¥1,751,574</td><td class='num'>¥2,022,372</td><td class='muted'>≈ full-occ rent × 3%</td></tr>
<tr><td>BM (building mgmt)</td><td class='num'>¥1,163,316</td><td class='num'>¥1,163,316</td><td class='muted'>actual</td></tr>
<tr><td>Internet</td><td class='num'>¥289,092</td><td class='num'>¥289,092</td><td class='muted'>actual</td></tr>
<tr><td>Property tax (固定資産税)</td><td class='num'>¥2,460,126</td><td class='num'>¥2,460,126</td><td class='muted'>FY2025</td></tr>
<tr class='hi'><td>Total opex</td><td class='num'>¥5,664,108</td><td class='num'>¥5,934,906</td><td></td></tr>
"""

def kv(rows_): return ''.join(f"<tr><td class='k'>{k}</td><td>{v}</td></tr>" for k,v in rows_)
today='2026-05-29'
doc=f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Shibuya Canon Palace — Property &amp; Rent Roll</title>
{CSS}</head><body>
<header>
<h1>Shibuya Canon Palace — Property &amp; Rent Roll</h1>
<div class="sub">Whole-building apartment/office · AK002 (eXp Japan) · captured {today} · rent roll as of 2026-01-07 · <a href="https://realestate.co.jp/en/forsale/view/1321745" target="_blank">source listing ↗</a></div>
</header>
<div class="wrap">
<a class="backlink" href="index.html">← Dossier home</a>

<div class="kpis">
<div class="kpi"><span>Asking price</span><b>¥1.93B</b></div>
<div class="kpi"><span>Gross yield (listed)</span><b>2.45%</b></div>
<div class="kpi"><span>Units</span><b>22 + 1F shop</b></div>
<div class="kpi"><span>GFA / land</span><b>791.8 / 213.4 m²</b></div>
<div class="kpi"><span>Built</span><b>Jul 2013</b></div>
</div>

<div class="two">
<div><h2>Headline</h2><table>{kv(headline)}</table></div>
<div><h2>Building &amp; regulatory</h2><table>{kv(building)}</table></div>
</div>

<h2>Unit-level rent roll</h2>
<div class="scrollx"><table>
<tr><th rowspan="2">Room</th><th rowspan="2">Use</th><th rowspan="2">Status</th><th colspan="2" class="num">Area</th><th colspan="3" class="num">Current (現況) monthly</th><th colspan="2" class="num">Upside (見込み) monthly</th><th rowspan="2">Remarks</th></tr>
<tr><th class="num">m²</th><th class="num">坪</th><th class="num">Rent</th><th class="num">Common</th><th class="num">Rent+Common</th><th class="num">Rent</th><th class="num">Rent+Common</th></tr>
{unit_rows}
<tr class="hi"><td>現状 Total</td><td>—</td><td>—</td><td class="num">{totals['cur']['area']}</td><td class="num">{totals['cur']['tsubo']}</td><td class="num">{y(totals['cur']['rent'])}</td><td class="num">{y(totals['cur']['common'])}</td><td class="num">{y(totals['cur']['rc'])}</td><td class="num">{y(totals['ups']['rent'])}</td><td class="num">{y(totals['ups']['rc'])}</td><td class="rem">deposits held {y(deposit)}</td></tr>
</table></div>
<div class="muted">Vacant units (募集中): 203, 603, 801, 803, 901 — rents shown are asking. Full data: <code>rent_roll.csv</code>.</div>

<h2>Income scenarios</h2>
<table>{scn}</table>

<h2>Operating expenses (annual, tax-incl)</h2>
<table>{opex}</table>
<div class="note">Net operating income (income − listed opex, before vacancy/capex/financing): current ≈ <b>¥31.5M (1.63%)</b>, full-occupancy ≈ <b>¥47.4M (2.46%)</b>, upside ≈ <b>¥55.3M (2.87%)</b> on the ¥1.93B price. See the Airbnb-conversion alternative in <code>airbnb_yield_model.html</code>.</div>

<h2>Source rent-roll sheets</h2>
<div class="imgs">
<figure><a href="images/rentroll_current_hires.jpeg" target="_blank"><img src="images/rentroll_current_hires.jpeg"></a><figcaption>現況レントロール — current / in-place rent roll (2026-01-07)</figcaption></figure>
<figure><a href="images/rentroll_upside_hires.jpeg" target="_blank"><img src="images/rentroll_upside_hires.jpeg"></a><figcaption>アップサイド見込みレントロール — upside projection</figcaption></figure>
</div>

<div class="muted" style="margin-top:18px">Generated {today}. Companion files: <code>airbnb_yield_model.html</code>, <code>airbnb_comp_report.html</code>, <code>property_details.md</code>, <code>rent_roll.csv</code>.</div>
</div></body></html>"""
open('property_report.html','w',encoding='utf-8').write(doc)
print("wrote property_report.html with", len(rows), "units")
