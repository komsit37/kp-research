import os as _os; _os.chdir(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
# CSS: shared report.css + this page's overrides (normal string -> literal braces)
CSS = '<link rel="stylesheet" href="report.css">\n<style>\n' + ':root{--ink:#222;--mut:#888}\nheader{padding:24px 28px} h1{font-size:22px}\n.wrap{padding:18px 28px 60px;max-width:none}\nth,td{vertical-align:top} th{position:sticky;top:0}\ntd.big{font-weight:700;font-size:16px}\n.photo img{width:120px;height:80px;object-fit:cover;border-radius:6px;display:block}\n.title a{color:var(--ink);font-weight:600;text-decoration:none} .title a:hover{color:var(--a)}\n.links{font-size:12px;margin-top:4px} .links a{color:var(--a);text-decoration:none}\n.rate{white-space:nowrap;font-size:13px}\ntr.relA{background:#fffafc} tr.relB{background:#fafcff}\n.tag{display:inline-block;padding:2px 8px;border-radius:10px;font-size:12px;margin-right:6px}\n.tA{background:#fde7f0;color:#b00857} .tB{background:#e7f0fd;color:#1456b0} .tC{background:#eee;color:#666}\n.note{border-left:5px solid var(--a)}\n.legend{margin:14px 0;font-size:13px;color:var(--ink)}\n.kpi b{font-size:20px}' + '\n</style>'
import json, os, re, html, datetime
data=json.load(open('generators/data/ab_merged.json',encoding='utf-8'))
BADGES={'Guest favorite','Top guest favorite','Superhost'}

def clean_title(d):
    t=d['title'].strip()
    if t in BADGES or len(t)<4:
        # fall back: search raw not stored; use id label
        return d.get('rawtitle', t) or ('Listing '+d['id'][-5:])
    return t

# relevance: studio/1BR up to ~44m² near Shibuya = direct comp to Canon Palace units
def relevance(d):
    a=d['area']; typ=d['type']
    am=int(re.sub(r'\D','',a)) if a else None
    if d['type'] in ('Studio',) or (typ=='1BR' and (am is None or am<=44)):
        return ('A','Direct studio/1BR comp')
    if typ=='2BR' or (am and 45<=am<=80):
        return ('B','Comp for 901 (77 m² 2LDK)')
    return ('C','Larger / context only')

for d in data:
    d['ctitle']=clean_title(d)
    d['rel'],d['relnote']=relevance(d)
    d['net']=round(d['pernight']*0.75) if d['pernight'] else None

order={'A':0,'B':1,'C':2}
data.sort(key=lambda d:(order[d['rel']], -(d['pernight'] or 0)))

def fmt(n): return '¥{:,}'.format(n) if n else '—'

rows=[]
for d in data:
    photo=f"images/airbnb/{d['id']}_photo.jpg"
    shot=f"images/airbnb/{d['id']}_shot.png"
    relcls={'A':'relA','B':'relB','C':'relC'}[d['rel']]
    rev=d['reviews']; rating=d['rating']
    ratecell=(f"{rating} ⭐<br><span class='muted'>{rev} rev</span>" if rating and rating!='New' else "<span class='muted'>New</span>")
    rows.append(f"""<tr class="{relcls}">
  <td class="photo"><a href="{d['url']}" target="_blank"><img src="{photo}" loading="lazy"></a></td>
  <td class="title"><a href="{d['url']}" target="_blank">{html.escape(d['ctitle'])}</a>
      <div class="muted">{d['relnote']}{(' · '+d['walk']+' to Shibuya') if d['walk'] else ''}</div>
      <div class="links"><a href="{d['url']}" target="_blank">listing ↗</a> · <a href="{shot}" target="_blank">full screenshot ↗</a></div></td>
  <td>{d['area'] or '—'}</td>
  <td>{d['type'] or '—'}<br><span class="muted">{html.escape(d['beds'] or '')}</span></td>
  <td class="num">{fmt(d['total'])}<br><span class="muted">5 nights</span></td>
  <td class="num big">{fmt(d['pernight'])}</td>
  <td class="num">{fmt(d['net'])}</td>
  <td class="rate">{ratecell}</td>
</tr>""")

a_ct=sum(1 for d in data if d['rel']=='A')
today=os.environ.get('TODAY','2026-05-29')
htmldoc=f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Airbnb Comps — Shibuya 2-chome (Canon Palace model)</title>
{CSS}</head><body>
<header>
<h1>Airbnb / STR Comps — Shibuya 2-chome</h1>
<div class="sub">For the Canon Palace whole-building model (¥1.93B). Captured {today} · {len(data)} listings · prices for Jun–Jul 2026 dates (include cleaning + service fees).</div>
</header>
<div class="wrap">
<a class="backlink" href="index.html">← Dossier home</a>
<div class="kpis">
<div class="kpi"><b>{a_ct}</b><span>direct studio/1BR comps</span></div>
<div class="kpi"><b>~¥22,000</b><span>studio gross/night (median)</span></div>
<div class="kpi"><b>~¥16,500</b><span>studio net ADR est.</span></div>
<div class="kpi"><b>180 nt/yr</b><span>minpaku legal cap (residential zone)</span></div>
</div>
<div class="legend">
<span class="tag tA">A</span>Direct comp to Canon Palace studios/1K (24–44 m²)
<span class="tag tB">B</span>Comp for unit 901 (77 m² 2LDK)
<span class="tag tC">C</span>Larger / market context
</div>
<table>
<thead><tr><th>Photo</th><th>Listing</th><th>Size</th><th>Type / beds</th><th>5-night total</th><th>~ /night (gross)</th><th>net ADR est.</th><th>Rating</th></tr></thead>
<tbody>
{''.join(rows)}
</tbody></table>
<div class="note">
<b>How to read these numbers.</b> Airbnb search totals are per <b>5-night stay including cleaning + ~14% service fee</b>. <b>~/night (gross)</b> = total ÷ 5. <b>Net ADR est.</b> ≈ gross × 0.75 (strips cleaning + host fee) — the figure to feed a revenue model.
<br><br>
<b>⚠️ Legal cap.</b> Canon Palace is zoned <b>Residential</b>. Legal STR there is <b>minpaku (住宅宿泊事業法), hard-capped at 180 nights/year (≈49% max occupancy)</b>; a year-round 旅館業 hotel licence is generally not available in residential zones. The year-round comps below are likely hotel-licensed or in commercial zones. Model STR upside under the 180-night cap; confirm the exact 用途地域 and Minato/Shibuya minpaku ordinance before assuming more. Full analysis in <code>airbnb_analysis.md</code>; long-term rent base case in <code>rent_roll.csv</code>.
</div>
</div></body></html>"""
open('airbnb_comp_report.html','w',encoding='utf-8').write(htmldoc)
print("wrote airbnb_comp_report.html with", len(data), "rows")
