import os as _os; _os.chdir(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
# CSS: shared report.css + this page's overrides (normal string -> literal braces)
CSS = '<link rel="stylesheet" href="report.css">\n<style>\n' + '.wrap{max-width:1080px}\n.kpi b{font-size:23px}\nth.ltr{background:#eef3fb;color:var(--b)}\nth.hs{background:#fff3e0;color:var(--o)}\nth.opt{background:#e9f6ec;color:var(--g)}\ntd.dash{color:var(--mut)} .lbl{color:#333}\n.scn td:nth-child(2),.scn td:nth-child(3){background:#f6f9fe}\n.scn tr.hi td:nth-child(2),.scn tr.hi td:nth-child(3){background:#eef3fb}\n.scn td:nth-child(6),.scn tr.hi td:nth-child(6){background:#fff8ee}\n.scn td:nth-child(7),.scn tr.hi td:nth-child(7){background:#eef8f0}\n.note ul{margin:8px 0 0;padding-left:20px;line-height:1.6} .note li{margin:5px 0}' + '\n</style>'
def y(n): return '¥{:,.0f}'.format(round(n))
def pct(n): return '{:.2f}%'.format(n*100)

# ---------- ADR assumption (user-set, all-in asking; below raw comps to reflect smaller units) ----------
# Hand-picked comp base is studio ¥38,471 / 2BR ¥64,697 (33-34 m², 4-5 guests). Canon Palace
# units are smaller (24-30 m² studios, 1-2 guests), so these are set conservatively.
STUDIO_BASE, STUDIO_HS = 30_000, 36_000   # studio/1BR: base & high-season, all-in
U901_BASE,   U901_HS   = 60_000, 72_000   # 901 2LDK:   base & high-season, all-in
OPT_1BR, OPT_2BR = 1.10, 1.20             # optimistic uplift on high-season: 1BR +10%, 2BR +20%
FEE = 0.84                                 # ×0.84: Airbnb guest service + host fee deducted

# ---------- ACQUISITION ----------
PRICE = 1_930_000_000
brokerage = PRICE*0.03*1.10
acq_tax, reg_tax, stamp = 30_000_000, 12_000_000, 1_000_000
txn_costs = brokerage+acq_tax+reg_tax+stamp
capex_per_unit = 1_000_000               # furnishing + fit-out per room
RESI_UNITS = 22
STUDIOS = 21
CONV_ITEMS = [   # one-time conversion capex (label, ¥)
 (f'Furnishing &amp; fit-out ({RESI_UNITS} rooms × {y(capex_per_unit)})', capex_per_unit*RESI_UNITS),
 ('Minpaku license, fire/safety compliance &amp; permits', 8_000_000),
 ('Initial STR insurance &amp; setup', 1_000_000),
]
capex = sum(v for _,v in CONV_ITEMS)     # = ¥31M total conversion
ALLIN = PRICE+txn_costs+capex            # STR all-in (incl conversion)
LTR_ALLIN = PRICE+txn_costs              # LTR all-in (no conversion capex)

# ---------- OPEX ----------
VAR_ITEMS = [   # % of NET booking revenue (platform fee already removed via FEE)
 ('STR management', 'pricing, listing, guest comms, check-in, cleaning coordination', 0.20),
 ('Cleaning', 'turnover cleaning between stays', 0.08),
 ('Utilities', 'elec / gas / water (guest-inclusive in STR)', 0.06),
 ('Supplies / consumables', 'linens, toiletries, amenities, replacements', 0.04),
]
VAR = sum(p for _,_,p in VAR_ITEMS)   # = 0.38
fixed = dict(property_tax=2_460_126, building_mgmt=1_163_316, internet=289_092, insurance=500_000)
FIXED = sum(fixed.values())
COMMERCIAL_MONTHLY = 466667
commercial_annual = COMMERCIAL_MONTHLY*12

# ---------- STR scenarios ----------
def scenario(occ, s_adr, u_adr):
    nights = 365*occ
    net1   = STUDIOS*s_adr*nights*FEE            # 1BR net booking revenue
    net2   = 1*u_adr*nights*FEE                  # 2BR (901) net booking revenue
    gross  = (STUDIOS*s_adr + 1*u_adr)*nights    # guest-paid all-in bookings/yr
    fees   = gross*(1-FEE)                        # Airbnb guest+host fees
    net    = gross*FEE                            # host-collected booking revenue
    var    = VAR*net
    total  = net+commercial_annual
    noi    = total-var-FIXED
    return dict(occ=occ, nights=nights, s_adr=s_adr, u_adr=u_adr, net1=net1, net2=net2,
                gross=gross, fees=fees, net=net, var=var,
                total=total, noi=noi, gy=total/PRICE, ny=noi/PRICE, ny_allin=noi/ALLIN,
                per_unit=net/RESI_UNITS)
A = scenario(0.50, STUDIO_BASE, U901_BASE)              # minpaku cap, flat base rate
B = scenario(0.70, STUDIO_BASE, U901_BASE)              # needs hotel licence (>180 nts)
C = scenario(0.50, STUDIO_HS,   U901_HS)                # minpaku cap, high-season pricing
D = scenario(0.50, STUDIO_HS*OPT_1BR, U901_HS*OPT_2BR)  # optimistic: high-season + 1BR +10% / 2BR +20%
E = scenario(0.70, STUDIO_HS,   U901_HS)                # high-season pricing @ 70% (needs licence)
F = scenario(0.70, STUDIO_HS*OPT_1BR, U901_HS*OPT_2BR)  # optimistic @ 70% (needs licence)
# pricing × occupancy matrix: (label, 50% scenario, 70% scenario)
MATRIX = [('Base (flat)', A, B), ('High-season', C, E), (f'Optimistic (1BR +{(OPT_1BR-1)*100:.0f}% / 2BR +{(OPT_2BR-1)*100:.0f}%)', D, F)]
# ADR tiers (label, studio all-in, 901 all-in)
ADR_TIERS = [('Base (normal season)', STUDIO_BASE, U901_BASE),
             ('High-season', STUDIO_HS, U901_HS),
             (f'Optimistic (high-szn, 1BR +{(OPT_1BR-1)*100:.0f}% / 2BR +{(OPT_2BR-1)*100:.0f}%)', STUDIO_HS*OPT_1BR, U901_HS*OPT_2BR)]

# ---------- LTR benchmarks (seller rent rolls) ----------
ltr_op = 5_664_108
ltr_1f = COMMERCIAL_MONTHLY*12                       # 1F at current lease
inp_total = 37_190_004; inp_resi = inp_total-ltr_1f  # in-place
inp_noi   = inp_total-ltr_op
stb_total = 53_078_004; stb_resi = stb_total-ltr_1f  # 満室想定: full occ at TODAY's rents
stb_noi   = stb_total-ltr_op
ups_total = 61_284_000; ups_noi = ups_total-5_934_906  # seller upside (marked-up) — note only
# residential split into 1BR (21 studios) vs 2BR (901). 901 in-place rent+common = ¥514,000/mo (vacant now)
ltr_901_stb = 514_000*12             # 901 stabilized = 6,168,000
inp_1br, inp_2br = inp_resi, 0        # 901 vacant in-place → 0 income
stb_2br = ltr_901_stb; stb_1br = stb_resi-stb_2br

# ---------- table builder: [LTR in-place, LTR stabilized, A, B, C, D] ----------
def cell(v, fmt):
    if v is None: return "<td class='num dash'>—</td>"
    if isinstance(v,str): return f"<td class='num dash'>{v}</td>"
    return f"<td class='num'>{fmt(v)}</td>"
def row(label, vals, fmt=y, hi=False):
    cls=" class='hi'" if hi else ''
    return f"<tr{cls}><td class='lbl'>{label}</td>{''.join(cell(v,fmt) for v in vals)}</tr>"
HEAD=("<tr><th>{}</th><th class='num ltr'>LTR in-place</th><th class='num ltr'>LTR stabilized</th>"
      "<th class='num'>STR 50% (minpaku)</th><th class='num'>STR 70%†</th><th class='num hs'>STR 50% high-season</th>"
      "<th class='num opt'>STR 50% optimistic</th></tr>")

def adrrow(label, n, key):  # text row: "n × ¥adr" per STR scenario, "n · lease" for LTR
    cells=(f"<td class='num dash'>{n} · lease</td>"*2 +
           ''.join(f"<td class='num'>{n} × {y(s[key])}</td>" for s in (A,B,C,D)))
    return f"<tr><td class='lbl'>{label}</td>{cells}</tr>"
scn_rows=[
 row("Nights sold / unit / yr", ['lease','lease', A['nights'], B['nights'], C['nights'], D['nights']], fmt=lambda v:f'{v:.0f} nts'),
 adrrow("1BR studios — units × ADR (all-in/nt)", STUDIOS, 's_adr'),
 adrrow("2BR · 901 — units × ADR (all-in/nt)", 1, 'u_adr'),
 row("Gross bookings (all-in, guest pays)", [None,None, A['gross'], B['gross'], C['gross'], D['gross']]),
 row("− Airbnb fees (×0.84 → −16%)", [None,None, -A['fees'], -B['fees'], -C['fees'], -D['fees']]),
 row("1BR residential revenue (net, 21 units)", [inp_1br, stb_1br, A['net1'], B['net1'], C['net1'], D['net1']]),
 row("2BR residential revenue (net, 901)", [inp_2br, stb_2br, A['net2'], B['net2'], C['net2'], D['net2']]),
 row("+ 1F commercial lease", [ltr_1f, ltr_1f, commercial_annual, commercial_annual, commercial_annual, commercial_annual]),
 row("= Total gross income", [inp_total, stb_total, A['total'], B['total'], C['total'], D['total']], hi=True),
 row("− Variable opex (mgmt/clean/util/supplies 38%)", [None,None, -A['var'], -B['var'], -C['var'], -D['var']]),
 row("− Fixed / direct opex", [-ltr_op, -ltr_op, -FIXED, -FIXED, -FIXED, -FIXED]),
 row("= NOI", [inp_noi, stb_noi, A['noi'], B['noi'], C['noi'], D['noi']], hi=True),
]
scn_table = HEAD.format("Line")+''.join(scn_rows)

yld_rows=[
 row("Acquisition price", [PRICE]*6),
 row("+ Transaction costs (~3.5%)", [txn_costs]*6),
 row("+ Conversion capex (furnish + license + insurance)", [0,0, capex, capex, capex, capex]),
 row("= All-in invested", [LTR_ALLIN, LTR_ALLIN, ALLIN, ALLIN, ALLIN, ALLIN], hi=True),
 row("NOI / yr", [inp_noi, stb_noi, A['noi'], B['noi'], C['noi'], D['noi']]),
 row("Gross yield (on price ¥1.93B)", [inp_total/PRICE, stb_total/PRICE, A['gy'], B['gy'], C['gy'], D['gy']], fmt=pct),
 row("Net yield / cap rate (on price)", [inp_noi/PRICE, stb_noi/PRICE, A['ny'], B['ny'], C['ny'], D['ny']], fmt=pct, hi=True),
 row("Net yield (on all-in invested)", [inp_noi/LTR_ALLIN, stb_noi/LTR_ALLIN, A['ny_allin'], B['ny_allin'], C['ny_allin'], D['ny_allin']], fmt=pct, hi=True),
 row("Net booking revenue / unit / yr", [None,None, A['per_unit'], B['per_unit'], C['per_unit'], D['per_unit']]),
]
yield_table = HEAD.format("Yield")+''.join(yld_rows)

# variable opex breakdown (% of net booking revenue, with ¥ per STR scenario)
varop_rows=''.join(
 f"<tr><td>{nm}<div class='muted'>{desc}</div></td><td class='num'>{p*100:.0f}%</td>"
 f"<td class='num'>{y(p*A['net'])}</td><td class='num'>{y(p*B['net'])}</td><td class='num'>{y(p*C['net'])}</td><td class='num'>{y(p*D['net'])}</td></tr>"
 for nm,desc,p in VAR_ITEMS)
varop_rows+=(f"<tr class='hi'><td>Total variable opex</td><td class='num'>{VAR*100:.0f}%</td>"
 f"<td class='num'>{y(VAR*A['net'])}</td><td class='num'>{y(VAR*B['net'])}</td><td class='num'>{y(VAR*C['net'])}</td><td class='num'>{y(VAR*D['net'])}</td></tr>")

# ADR tiers rows (all-in → net per unit type)
adr_tier_rows=''.join(
 f"<tr{' class=hi' if i==2 else ''}><td class='lbl'>{lbl}</td>"
 f"<td class='num'>{y(s)}</td><td class='num'>{y(s*FEE)}</td>"
 f"<td class='num'>{y(u)}</td><td class='num'>{y(u*FEE)}</td></tr>"
 for i,(lbl,s,u) in enumerate(ADR_TIERS))

# pricing × occupancy matrix rows (net yield on price + NOI)
matrix_rows=''.join(
 f"<tr><td class='lbl'>{lbl}</td>"
 f"<td class='num'><b>{pct(s50['ny'])}</b><div class='muted'>NOI {y(s50['noi'])}</div></td>"
 f"<td class='num'><b>{pct(s70['ny'])}</b><div class='muted'>NOI {y(s70['noi'])}</div></td></tr>"
 for lbl,s50,s70 in MATRIX)

# conversion capex breakdown (acquisition table)
conv_rows=''.join(f"<tr><td>Conversion — {nm}</td><td class='num'>{y(v)}</td></tr>" for nm,v in CONV_ITEMS)
conv_rows+=f"<tr><td class='b'>Conversion subtotal</td><td class='num b'>{y(capex)}</td></tr>"

# unit mix
units = [
 ('1K studio · 24.18 m² (×7)', 7, 24.18, STUDIO_BASE, STUDIO_HS),
 ('1K studio · 25.97 m² (×6)', 6, 25.97, STUDIO_BASE, STUDIO_HS),
 ('1R/1K · 30.44 m² (×7)',     7, 30.44, STUDIO_BASE, STUDIO_HS),
 ('1R · 23.22 m² (801)',       1, 23.22, STUDIO_BASE, STUDIO_HS),
 ('2LDK · 76.91 m² (901)',     1, 76.91, U901_BASE,   U901_HS),
]
adr_avg = sum(c*b for _,c,_,b,_ in units)/RESI_UNITS
unit_rows=''.join(
 f"<tr><td>{l}</td><td class='num'>{c}</td><td class='num'>{sqm:.2f} m²</td>"
 f"<td class='num'>{y(b)}</td><td class='num'>{y(h)}</td>"
 f"<td class='num'>{y(b*FEE)}</td><td class='num'>{y(h*FEE)}</td></tr>"
 for l,c,sqm,b,h in units)

today='2026-05-29'
html=f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Airbnb Conversion Yield Model — Shibuya Canon Palace</title>
{CSS}</head><body>
<header>
<h1>Airbnb / STR Conversion — Yield Model</h1>
<div class="sub">Shibuya Canon Palace · whole building · asking ¥1,930,000,000 · model dated {today}. Convert 22 residential units to short-term rental; keep 1F as commercial lease. Unlevered (cash) basis. ADR from the <span style="color:var(--b)">hand-picked comp set</span>; Airbnb fees deducted via ×0.84.</div>
</header>
<div class="wrap">
<a class="backlink" href="index.html">← Dossier home</a>
<div class="note" style="border-left:5px solid #1456b0">ADR assumption (all-in asking): studio/1BR <b>{y(STUDIO_BASE)}</b> base / <b>{y(STUDIO_HS)}</b> high-season; 2LDK 901 <b>{y(U901_BASE)}</b> base / <b>{y(U901_HS)}</b> high-season; then <b>×{FEE}</b> to strip Airbnb guest + host fees. Set <b>below</b> the raw hand-picked comps (studio ¥38,471 / 2BR ¥64,697 — see <a href="airbnb_adr_handpick.html">ADR — hand-picked comps</a>) to reflect Canon Palace's smaller, lower-capacity units.</div>

<div class="verdict">
<b>Bottom line.</b> On the assumed ADR (studio {y(STUDIO_BASE)} / 901 {y(U901_BASE)} base, all-in), conversion pencils to <b>{pct(A['ny'])} net at 50% occ</b> (≈ the 180-night minpaku ceiling) and <b>{pct(C['ny'])} if those 180 nights are concentrated in high season</b> — both legal, vs long-term rent at <b>{pct(inp_noi/PRICE)} (in-place)</b> / <b>{pct(stb_noi/PRICE)} (stabilized)</b>. Pushing to <b>{pct(B['ny'])} needs 70% occupancy</b>, which requires a 旅館業 hotel licence (residential zoning generally won't allow it). <b>Among legal options, high-season-only ({pct(C['ny'])}) dominates flat ({pct(A['ny'])})</b> — same legal nights, higher rate. An <b>optimistic</b> high-season case (1BR +{(OPT_1BR-1)*100:.0f}% / 2BR +{(OPT_2BR-1)*100:.0f}% ADR) reaches <b>{pct(D['ny'])}</b>.
</div>

<div class="note"><b>On the ADR assumption.</b> Studio base ¥{STUDIO_BASE:,} is ~22% below the hand-picked comp base (¥38,471) — a deliberate haircut, since those comps are 33–34 m² units sleeping 4–5 guests while Canon Palace's studios are 24–30 m² 1K (1–2 guests). Net of fees that's ¥{round(STUDIO_BASE*FEE):,}/night, close to the earlier consolidated estimate. High-season is taken at a flat <b>+20%</b>. These are inputs you can move — the yield scales roughly linearly with ADR.</div>

<h2>ADR tiers (all-in asking → net of Airbnb fees)</h2>
<div class="scrollx"><table>
<tr><th>ADR tier</th><th class="num">Studio/1BR all-in</th><th class="num">Studio/1BR net</th><th class="num">901 2LDK all-in</th><th class="num">901 2LDK net</th></tr>
{adr_tier_rows}
</table></div>
<div class="legend">Net = all-in × {FEE} (Airbnb guest + host fees). The three scenarios use these tiers: flat → <b>Base</b>, high-season → <b>High-season</b>, optimistic → <b>Optimistic</b> (high-season + 1BR +{(OPT_1BR-1)*100:.0f}% / 2BR +{(OPT_2BR-1)*100:.0f}%).</div>

<div class="kpis">
<div class="kpi b"><span>LTR stabilized (benchmark)</span><b>{pct(stb_noi/PRICE)}</b></div>
<div class="kpi g"><span>STR 50% (minpaku cap)</span><b>{pct(A['ny'])}</b></div>
<div class="kpi" style="border-color:#f0d9b0"><span>STR 50% high-season</span><b style="color:var(--o)">{pct(C['ny'])}</b></div>
<div class="kpi" style="border-color:#bfe3c8"><span>STR 50% optimistic</span><b style="color:var(--g)">{pct(D['ny'])}</b></div>
<div class="kpi g"><span>STR 70% (needs licence)</span><b>{pct(B['ny'])}</b></div>
</div>

<h2>Scenario P&amp;L (annual) — with long-term-rent comparison</h2>
<div class="scrollx"><table class="scn">{scn_table}</table></div>
<div class="legend">STR gross = all-in nightly (22 units) × 365 × occ; <b>×{FEE}</b> removes Airbnb's guest service + host fee (≈16%); variable opex {int(VAR*100)}% of net (mgmt 20 + clean 8 + util 6 + supplies 4). 1F kept as commercial lease (¥{COMMERCIAL_MONTHLY:,}/mo). LTR columns: in-place rent roll, and "stabilized" = full occupancy at <i>today's</i> rents (満室想定, ¥{stb_total:,}/yr). †STR 70% exceeds the 180-night minpaku cap → needs a 旅館業 hotel licence.</div>

<h2>Yield summary</h2>
<div class="scrollx"><table class="scn">{yield_table}</table></div>
<div class="legend">Net yield on all-in: STR denominator ¥{ALLIN/1e9:.2f}B (price + transaction costs + ¥{capex/1e6:.0f}M conversion capex); LTR denominator ¥{LTR_ALLIN/1e9:.2f}B (no conversion). Seller's <i>marked-up upside</i> rent roll (¥{ups_total:,}/yr) would put LTR at {pct(ups_noi/PRICE)} — not used here as the benchmark; see <a href="property_report.html">rent roll</a>.</div>

<h2>Scenario matrix — net yield by ADR pricing × occupancy</h2>
<table>
<tr><th>ADR pricing</th><th class="num">50% occ&nbsp;<span class="muted">(≤180 nts · minpaku legal)</span></th><th class="num">70% occ&nbsp;<span class="muted">(needs 旅館業 licence)</span></th></tr>
{matrix_rows}
</table>
<div class="legend">Net yield on price (¥1.93B); annual NOI below each. The <b>50% column is the legal ceiling</b> under the 180-night minpaku cap; the <b>70% column needs a hotel licence</b> residential zoning generally blocks. So the realistic shortlist is <b>flat 50% ({pct(A['ny'])})</b> → <b>high-season 50% ({pct(C['ny'])})</b> → <b>optimistic 50% ({pct(D['ny'])})</b>; the 70% column shows what an out-of-cap operation would add. Headline pair: <b>flat 50% = {pct(A['ny'])}</b>, <b>high-season 70% = {pct(E['ny'])}</b>.</div>

<h2>STR vs. Long-term rent (net yield on price)</h2>
<table>
<tr><th>Strategy</th><th class="num">NOI / yr</th><th class="num">Net yield</th><th>Notes</th></tr>
<tr><td>Long-term rent — in-place</td><td class="num">{y(inp_noi)}</td><td class="num">{pct(inp_noi/PRICE)}</td><td class="muted">as-is rent roll, 5 units vacant</td></tr>
<tr><td>Long-term rent — stabilized</td><td class="num">{y(stb_noi)}</td><td class="num">{pct(stb_noi/PRICE)}</td><td class="muted">full occ at today's rents; low opex, low effort</td></tr>
<tr class="hi"><td>Airbnb @ 50% (minpaku legal cap, flat)</td><td class="num">{y(A['noi'])}</td><td class="num">{pct(A['ny'])}</td><td class="muted">~180 nts year-round; legal in residential zone</td></tr>
<tr class="hi"><td>Airbnb @ 50% (minpaku cap, high-season only)</td><td class="num">{y(C['noi'])}</td><td class="num">{pct(C['ny'])}</td><td class="muted">same 180 nts concentrated in peaks — best legal play</td></tr>
<tr><td>Airbnb @ 50% optimistic (high-szn, 1BR +{(OPT_1BR-1)*100:.0f}% / 2BR +{(OPT_2BR-1)*100:.0f}%)</td><td class="num">{y(D['noi'])}</td><td class="num">{pct(D['ny'])}</td><td class="muted">bull case if units reconfigured to lift capacity/ADR</td></tr>
<tr><td>Airbnb @ 70% (needs hotel licence)</td><td class="num">{y(B['noi'])}</td><td class="num">{pct(B['ny'])}</td><td class="muted">exceeds minpaku cap; not available in residential zoning</td></tr>
</table>

<div class="two">
<div>
<h2>Acquisition / all-in cost</h2>
<table>
<tr><td>Purchase price</td><td class="num">{y(PRICE)}</td></tr>
<tr><td>Brokerage (3% + 10% tax)</td><td class="num">{y(brokerage)}</td></tr>
<tr><td>Acquisition tax (est)</td><td class="num">{y(acq_tax)}</td></tr>
<tr><td>Registration + scrivener (est)</td><td class="num">{y(reg_tax)}</td></tr>
<tr><td>Stamp / misc</td><td class="num">{y(stamp)}</td></tr>
{conv_rows}
<tr class="hi"><td>All-in invested (STR)</td><td class="num">{y(ALLIN)}</td></tr>
<tr><td>All-in invested (LTR, no conversion)</td><td class="num">{y(LTR_ALLIN)}</td></tr>
</table>
</div>
<div>
<h2>Unit mix &amp; assumed ADR</h2>
<table>
<tr><th>Unit type</th><th class="num">#</th><th class="num">Size</th><th class="num">Base all-in</th><th class="num">High-szn all-in</th><th class="num">Net base</th><th class="num">Net high-szn</th></tr>
{unit_rows}
<tr class="hi"><td>Blended</td><td class="num">{RESI_UNITS}</td><td></td><td class="num">{y(adr_avg)}</td><td class="num">{y(adr_avg*STUDIO_HS/STUDIO_BASE)}</td><td class="num">{y(adr_avg*FEE)}</td><td class="num">{y(adr_avg*FEE*STUDIO_HS/STUDIO_BASE)}</td></tr>
</table>
<div class="legend">All-in = guest-paid nightly (assumption set below the raw comps to reflect Canon Palace's smaller units). Net = all-in × {FEE} (Airbnb fees). High-season ≈ +20% over base.</div>
<h2>Fixed opex (annual)</h2>
<table>
<tr><td>Property tax (固定資産税)</td><td class="num">{y(fixed['property_tax'])}</td></tr>
<tr><td>Building management (BM)</td><td class="num">{y(fixed['building_mgmt'])}</td></tr>
<tr><td>Internet</td><td class="num">{y(fixed['internet'])}</td></tr>
<tr><td>Insurance (annual)</td><td class="num">{y(fixed['insurance'])}</td></tr>
<tr class="hi"><td>Total fixed</td><td class="num">{y(FIXED)}</td></tr>
</table>
</div>
</div>

<h2>Variable opex (% of net booking revenue)</h2>
<div class="scrollx"><table>
<tr><th>Component</th><th class="num">% of net</th><th class="num">STR 50%</th><th class="num">STR 70%</th><th class="num hs">STR 50% high-szn</th><th class="num opt">STR 50% optimistic</th></tr>
{varop_rows}
</table></div>
<div class="legend">Applied to <b>net</b> booking revenue (after the ×{FEE} Airbnb fee), so the platform cut isn't double-counted. Cleaning &amp; utilities scale with occupancy; modelling them as a flat % is a simplification (a fixed per-turnover minimum would raise the effective rate at low occupancy).</div>

<h2>What's deliberately not in here (worth knowing)</h2>
<div class="note warn"><b>These omissions make NOI slightly optimistic — fold them in before underwriting.</b>
<ul>
<li><b>Capex / FF&amp;E reserve</b> — furniture, appliances and refurb wear out far faster under STR turnover. A reserve of ~3–5% of revenue is normal; it's <b>not</b> included here. At the 50% high-season case that's ~¥5M/yr, which would pull the net yield from {pct(C['ny'])} to ~{pct((C['noi']-0.04*C['net'])/PRICE)}.</li>
<li><b>Income tax</b> and <b>financing costs</b> — model is unlevered / pre-tax.</li>
<li><b>Property-tax reassessment</b> on change of use, and <b>higher building management</b> from heavier common-area turnover (trash, wear) — both kept flat/conservative.</li>
<li><b>Ramp / vacancy drag</b> — assumes the target occupancy is hit from year one; a new listing typically takes 6–12 months to reach steady-state reviews and pricing.</li>
<li><b>Airbnb platform fee</b> — <i>is</i> captured, but as the explicit ×{FEE} line above opex, not inside the {int(VAR*100)}% variable rate.</li>
</ul></div>

<div class="note warn">
<b>⚠️ Legal constraint (decisive).</b> Canon Palace is zoned <b>Residential</b>. <b>minpaku (住宅宿泊事業法)</b> is allowed but <b>capped at 180 nights/yr (~49% occupancy)</b>; <b>旅館業 (hotel licence)</b> is year-round but generally not permitted in residential zones. The <b>two 50% columns are the practical legal maximum</b>; the 70% column needs a licence path that residential zoning likely blocks.
</div>

<div class="note">
<b>Modelling notes.</b> Unlevered/all-cash. ADR is the user-set assumption above; the flat 50%/70% scenarios price every night at the <b>base</b> rate, the high-season scenario prices every night at the <b>high-season</b> rate (+20%). Airbnb fees taken as <b>×{FEE}</b> on all-in bookings (≈14% guest service + ~3% host fee). Variable opex {int(VAR*100)}% of net booking revenue; cleaning sits inside it. LTR uses the seller's rent rolls (<code>rent_roll.csv</code>); the marked-up "upside" roll is shown only in the yield note, not as the benchmark.
</div>

<div class="muted">Generated {today}. Companion: <code>airbnb_adr_handpick.html</code>, <code>property_report.html</code>, <code>airbnb_comp_report.html</code>, <code>rent_roll.csv</code>.</div>
</div></body></html>"""
open('airbnb_yield_model.html','w',encoding='utf-8').write(html)
print("regenerated airbnb_yield_model.html")
print(f"ADR studio {y(STUDIO_BASE)}/{y(STUDIO_HS)} | 901 {y(U901_BASE)}/{y(U901_HS)} | FEE {FEE}")
print(f"LTR in-place {pct(inp_noi/PRICE)} | stabilized {pct(stb_noi/PRICE)}")
print(f"STR 50% flat {pct(A['ny'])} | 70% {pct(B['ny'])} | 50% high-season {pct(C['ny'])} | 50% optimistic {pct(D['ny'])}")
