#!/usr/bin/env python3
"""Build a single interactive Plotly map of JP semi facilities with zoom presets,
plus a sortable + filterable HTML table below.

Output: hbf-nand-jp-facilities-map-2026-05-27.html
"""
import json
import math
import os
import plotly.graph_objects as go

# ===== Load per-company revenue + fixed-assets for size normalization =====
CAPEX_DIR = "../data"
ORDERBOOK_DATA = "../data/orderbook-data.json"

def load_company_metrics():
    """Return {sec_code: {revenue_jpy, fixed_assets_jpy, capex_jpy}} from FY-latest filings."""
    out = {}
    # Revenue from capex JSON (back out via capex_pct_revenue)
    for fn in os.listdir(CAPEX_DIR):
        if not fn.endswith(".json") or fn.startswith("_"):
            continue
        sec = fn.replace(".json", "")
        try:
            rows = json.load(open(os.path.join(CAPEX_DIR, fn)))
        except Exception:
            continue
        if not rows:
            continue
        latest = rows[0]  # rows are sorted FY desc
        capex = latest.get("capex_jpy")
        pct = latest.get("capex_pct_revenue")
        revenue = None
        if capex and pct:
            revenue = capex / (pct / 100.0)
        out.setdefault(sec, {})["revenue_jpy"] = revenue
        out[sec]["capex_jpy"] = capex
    # Fixed assets (PP&E + CIP) from orderbook _data.json
    try:
        ob = json.load(open(ORDERBOOK_DATA))
        for sec, v in ob.items():
            yrs = v.get("by_year", {})
            if not yrs:
                continue
            latest_yr = max(yrs.keys(), key=lambda k: int(k) if str(k).isdigit() else 0)
            fy = yrs[latest_yr]
            ppe = fy.get("ppe_jpy") or 0
            cip = fy.get("cip_jpy") or 0
            out.setdefault(sec, {})["fixed_assets_jpy"] = ppe + cip
    except Exception as e:
        print(f"WARN: orderbook data load: {e}")
    return out

COMPANY_METRICS = load_company_metrics()

# (sec, company, plant, city, prefecture, country, lat, lon, capex_jpym, completion, cluster, cap_disclosed)
PLANTS = [
    ("6525", "KOKUSAI Electric", "Toyama 事業所", "Toyama", "Toyama", "Japan", 36.6953, 137.2113, 8386, "2026-03", "Deposition", False),
    ("6525", "KOKUSAI Electric", "KSE Corp Oregon", "Hillsboro", "Oregon", "USA", 45.5229, -122.9898, 16542, "2026-09", "Deposition", False),
    ("4369", "Tri Chemical", "Uenohara HQ + #2", "Uenohara", "Yamanashi", "Japan", 35.6303, 139.1095, 5606, "2029-01", "Deposition", False),
    ("4369", "Tri Chemical", "Minami-Alps 事業所", "Minami-Alps", "Yamanashi", "Japan", 35.6086, 138.4658, 4528, "2029-01", "Deposition", False),
    ("4369", "Tri Chemical (TW)", "Sanhua HQ", "Miaoli", "Miaoli", "Taiwan", 24.5604, 120.8214, 2364, "2029-01", "Deposition", False),
    ("8035", "TEL", "Yamanashi 事業所", "Nirasaki", "Yamanashi", "Japan", 35.7156, 138.4502, 23340, "2028-05", "Etch tools", False),
    ("8035", "TEL Miyagi", "Yamato HQ — process-eval", "Yamato", "Miyagi", "Japan", 38.4302, 140.8819, 70395, "2028-03", "Etch tools", False),
    ("8035", "TEL Miyagi", "Yamato — R&D facility", "Yamato", "Miyagi", "Japan", 38.4302, 140.8819, 52000, "2025-04", "Etch tools", False),
    ("8035", "TEL Miyagi", "Yamato — production/logistics (+250%)", "Yamato", "Miyagi", "Japan", 38.4302, 140.8819, 104000, "2027-08", "Etch tools", True),
    ("8035", "TEL Solutions", "Yamanashi HQ — process-eval", "Nirasaki", "Yamanashi", "Japan", 35.7156, 138.4502, 32815, "2027-09", "Etch tools", False),
    ("8035", "TEL Solutions", "Oshu — production/logistics (+50%)", "Oshu", "Iwate", "Japan", 39.1444, 141.1372, 22000, "2025-09", "Etch tools", True),
    ("8035", "TEL Solutions", "Nirasaki — process-eval", "Nirasaki", "Yamanashi", "Japan", 35.7156, 138.4502, 16300, "2026-10", "Etch tools", False),
    ("8035", "TEL Kyushu", "Koshi — process-eval", "Koshi", "Kumamoto", "Japan", 32.8841, 130.7837, 18164, "2027-08", "Etch tools", False),
    ("8035", "TEL Kyushu", "Koshi — R&D facility", "Koshi", "Kumamoto", "Japan", 32.8841, 130.7837, 43000, "2025-08", "Etch tools", False),
    ("8035", "TEL Korea", "Hwaseong — office/R&D/demo", "Hwaseong", "Gyeonggi", "Korea", 37.1996, 126.8311, 62521, "2027-04", "Etch tools", False),
    ("6590", "Shibaura Mech", "Yokohama Sakae 事業所", "Yokohama", "Kanagawa", "Japan", 35.3537, 139.5707, 804, "2026-03", "Etch tools", False),
    ("6590", "Shibaura Mech", "Sagamino 事業所", "Ebina", "Kanagawa", "Japan", 35.4456, 139.3925, 1363, "2026-03", "Etch tools", False),
    ("4047", "Kanto Denka", "Mizushima", "Kurashiki", "Okayama", "Japan", 34.5050, 133.7795, 22783, "2027-10", "Etch gases", True),
    ("4047", "Xuancheng Kediker", "Xuancheng plant", "Xuancheng", "Anhui", "China", 30.9457, 118.7585, 6150, "2025-03", "Etch gases", True),
    ("6871", "Nihon Micronics", "Aomori — capacity expansion", "Hirakawa", "Aomori", "Japan", 40.5825, 140.5694, 7744, "2026-12", "Test & probe", False),
    ("6871", "Nihon Micronics", "Aomori — building", "Hirakawa", "Aomori", "Japan", 40.5825, 140.5694, 2914, "2026-12", "Test & probe", False),
    ("6871", "MEK (Korea)", "Bucheon HQ", "Bucheon", "Gyeonggi", "Korea", 37.5036, 126.7660, 4041, "2026-12", "Test & probe", False),
    ("6627", "TeraProbe", "JP + Taiwan aggregate", "Multi", "Multi", "Japan", 34.6937, 135.5023, 16000, "2026", "Test & probe", False),
    ("6961", "Enplas", "Kawaguchi", "Kawaguchi", "Saitama", "Japan", 35.8076, 139.7237, 2565, "2026-03", "Test & probe", False),
    ("6961", "Enplas", "Saitama R&D", "Saitama-shi", "Saitama", "Japan", 35.8616, 139.6455, 15000, "2026-08", "Test & probe", False),
    ("4062", "Ibiden", "Kawama 事業場", "Ogaki", "Gifu", "Japan", 35.3614, 136.6173, 143000, "TBD", "Substrate", False),
    ("4062", "Ibiden", "Ogaki 事業場", "Ogaki", "Gifu", "Japan", 35.3614, 136.6173, 12900, "2026-04", "Substrate", False),
    ("4062", "Ibiden", "Ohno 事業場 (ABF Cell5/6)", "Ibi-gun", "Gifu", "Japan", 35.4842, 136.5856, 119500, "2026-12", "Substrate", False),
    ("4062", "Ibiden", "Ohno add'l", "Ibi-gun", "Gifu", "Japan", 35.4842, 136.5856, 23000, "2027-02", "Substrate", False),
    ("4975", "JCU", "Kumamoto 事業所", "Mashiki", "Kumamoto", "Japan", 32.7800, 130.8225, 11400, "2025-12", "Substrate", False),
    ("4975", "JCU Thailand", "Thailand new plant", "Bangkok", "—", "Thailand", 13.7563, 100.5018, 3300, "2026-12", "Substrate", False),
    ("6146", "Disco", "Haneda R&D Center", "Ota-ku", "Tokyo", "Japan", 35.5494, 139.7798, 14200, "2027-12", "Adv. packaging", False),
    ("6988", "Nitto Denko", "Tohoku 事業所", "Osaki", "Miyagi", "Japan", 38.5773, 140.9555, 3326, "2026-12", "Adv. packaging", False),
    ("6988", "Nitto Denko", "Kanto 事業所", "Fukaya", "Saitama", "Japan", 36.1975, 139.2814, 3889, "2027-08", "Adv. packaging", False),
    ("6988", "Nitto Denko", "Toyohashi 事業所", "Toyohashi", "Aichi", "Japan", 34.7691, 137.3915, 18821, "2028-04", "Adv. packaging", False),
    ("6988", "Nitto Denko", "Kameyama 事業所", "Kameyama", "Mie", "Japan", 34.8568, 136.4513, 25514, "2027-09", "Adv. packaging", False),
    ("6988", "Nitto Denko", "Shiga 事業所", "Kusatsu", "Shiga", "Japan", 35.0131, 135.9608, 16589, "2027-04", "Adv. packaging", False),
    ("6988", "Nitto Denko", "Onomichi", "Onomichi", "Hiroshima", "Japan", 34.4087, 133.2058, 29711, "2028-03", "Adv. packaging", False),
    ("6988", "Nitto Denko", "Ibaraki R&D", "Ibaraki", "Osaka", "Japan", 34.8166, 135.5687, 10264, "2028-02", "Adv. packaging", False),
    ("6988", "Nitto Shinko", "Sakai-shi", "Sakai", "Fukui", "Japan", 36.1681, 136.2316, 6540, "2027-01", "Adv. packaging", False),
    ("6988", "Kinovate Life Sci", "Oceanside CA", "Oceanside", "California", "USA", 33.1959, -117.3795, 13456, "2026-02", "Adv. packaging", False),
    ("6988", "Nitto Denko Avecia", "Milford MA", "Milford", "Massachusetts", "USA", 42.1396, -71.5161, 15416, "2025-12", "Adv. packaging", False),
    ("6988", "Nitto Denko (TW)", "Kaohsiung", "Kaohsiung", "Kaohsiung", "Taiwan", 22.6273, 120.3014, 19024, "2028-05", "Adv. packaging", False),
    ("6988", "Nitto Material Tech", "Chengdu", "Chengdu", "Sichuan", "China", 30.5728, 104.0668, 17691, "2026-01", "Adv. packaging", False),
    ("6988", "Nitto Denko Vietnam", "Binh Duong", "Binh Duong", "Binh Duong", "Vietnam", 11.1747, 106.6604, 18519, "2026-03", "Adv. packaging", False),
    ("6988", "Nitto Vietnam", "Bac Ninh", "Bac Ninh", "Bac Ninh", "Vietnam", 21.1861, 106.0763, 17214, "2026-05", "Adv. packaging", False),
    ("4203", "SBHPP", "Semi materials JP aggregate", "Tokyo (agg)", "—", "Japan", 35.6762, 139.6503, 3800, "FY25", "Adv. packaging", False),
    ("4203", "SBHPP", "High-perf plastics JP aggregate", "Tokyo (agg)", "—", "Japan", 35.6762, 139.6503, 8800, "FY25", "Adv. packaging", False),
    ("3433", "Tocalo", "Kobe ZAC coating", "Kobe", "Hyogo", "Japan", 34.6901, 135.1956, 1250, "2025-04", "OEM parts", False),
    ("3433", "Tocalo", "Tokyo plant / Gyoda", "Funabashi", "Chiba", "Japan", 35.6938, 139.9826, 6735, "2026-11", "OEM parts", False),
    ("3433", "Tocalo", "Kitakyushu plant", "Kanda-machi", "Fukuoka", "Japan", 33.7831, 130.9826, 3204, "2026-09", "OEM parts", False),
    ("4063", "Shin-Etsu Chemical", "Electronic materials JP+OS agg", "Tokyo (agg)", "—", "Japan", 35.6762, 139.6503, 246000, "FY25", "Wafer/materials", False),
    ("4063", "Shin-Etsu Chemical", "Functional materials agg", "Tokyo (agg)", "—", "Japan", 35.6762, 139.6503, 53000, "FY25", "Wafer/materials", False),
    ("4063", "Shin-Etsu Chemical", "生活環境基盤 agg", "Tokyo (agg)", "—", "Japan", 35.6762, 139.6503, 65000, "FY25", "Wafer/materials", False),
    ("4004", "Resonac", "Semi & EM CCL capacity agg", "Tokyo (agg)", "—", "Japan", 35.6762, 139.6503, 83696, "FY25", "Materials", False),
    ("4004", "Resonac", "Mobility / chem / Krasus agg", "Tokyo (agg)", "—", "Japan", 35.6762, 139.6503, 50553, "FY25", "Materials", False),
    ("7741", "Hoya", "Nagasaka + Hachioji + Akishima", "Hachioji", "Tokyo", "Japan", 35.6663, 139.3160, 3925, "—", "Mask/optics", False),
    ("7741", "HOYA Electronics SG", "Tampines (mask blanks)", "Tampines", "—", "Singapore", 1.3526, 103.9450, 13677, "—", "Mask/optics", False),
    ("7741", "Chongqing MAS Tek", "Chongqing electronics", "Chongqing", "Chongqing", "China", 29.4316, 106.9123, 12561, "—", "Mask/optics", False),
    ("7741", "HOYA Lens Thailand", "Pathum Thani", "Pathum Thani", "Pathum Thani", "Thailand", 14.0203, 100.5256, 3684, "—", "Healthcare", False),
    ("7741", "HOYA Lamphun", "Lamphun", "Lamphun", "Lamphun", "Thailand", 18.5786, 99.0086, 6502, "—", "Healthcare", False),
    ("7735", "SCREEN", "HQ + SPE mission-critical IT", "Kyoto", "Kyoto", "Japan", 35.0290, 135.7568, 10760, "2027-01", "Cleaning", False),
    ("7735", "SCREEN", "Yasu site (new shell)", "Yasu", "Shiga", "Japan", 35.0689, 136.0314, 4700, "TBD", "Cleaning", False),
    ("7735", "SCREEN", "Overseas R&D base (TBD)", "Overseas (TBD)", "—", "—", 13.7563, 100.5018, 11000, "—", "Cleaning", False),
    ("4186", "TOK", "Koriyama electronics materials", "Koriyama", "Fukushima", "Japan", 37.4002, 140.3590, 20000, "2026 mid", "Materials", False),
    ("4186", "TOK Korea", "Pyeongtaek high-purity chem", "Pyeongtaek", "Gyeonggi", "Korea", 36.9912, 127.1129, 12000, "2027 mid", "Materials", False),
    ("4109", "Stella Chemifa", "Sanpo plant — HF filling line (~2× cap)", "Sakai", "Osaka", "Japan", 34.5733, 135.4831, 6220, "2026-03", "Etch gases", True),
    ("6967", "Shinko Electric (delisted)", "Plastic pkg expansion agg", "Nagano", "Nagano", "Japan", 36.6485, 138.1947, 48300, "2026-03", "Substrate", False),
    ("6967", "Shinko Electric (delisted)", "Plastic pkg new product agg", "Nagano", "Nagano", "Japan", 36.6485, 138.1947, 53300, "2030-03", "Substrate", False),
    ("6967", "Shinko Electric (delisted)", "Chikuma flip-chip (+50% cap)", "Chikuma", "Nagano", "Japan", 36.5305, 138.1245, 140000, "2026-03", "Substrate", True),
    ("6967", "Shinko Electric (delisted)", "Arai plastic BGA", "Myoko", "Niigata", "Japan", 37.0386, 138.2467, 10200, "2029-03", "Substrate", True),
    ("6967", "Shinko Electric (delisted)", "Metal pkg agg", "Nagano", "Nagano", "Japan", 36.6485, 138.1947, 15100, "2026-03", "Substrate", False),
    ("6383", "Daifuku", "Shiga Hino new plant", "Hino", "Shiga", "Japan", 35.0211, 136.2418, 33000, "2028-03", "Fab automation", False),
    ("285A", "Kioxia", "Yokkaichi (gen-8 3D NAND)", "Yokkaichi", "Mie", "Japan", 34.9650, 136.6244, 31500, "—", "NAND fab", True),
    ("285A", "Kioxia", "Kitakami (gen-8 3D NAND)", "Kitakami", "Iwate", "Japan", 39.2864, 141.1130, 31500, "—", "NAND fab", True),
    ("4183", "Mitsui Chem", "Basic & Green Materials agg", "Tokyo (agg)", "—", "Japan", 35.6762, 139.6503, 41000, "FY25", "Chemicals (non-semi)", False),
    ("4183", "Mitsui Chem", "ICT (semi-grade) agg", "Tokyo (agg)", "—", "Japan", 35.6762, 139.6503, 29000, "FY25", "Chemicals", False),
    ("4183", "Mitsui Chem", "Mobility / Life&HC / Other agg", "Tokyo (agg)", "—", "Japan", 35.6762, 139.6503, 84000, "FY25", "Chemicals (non-semi)", False),
    ("6963", "ROHM", "Kyoto HQ", "Kyoto", "Kyoto", "Japan", 35.0116, 135.7681, 9217, "2026-03", "Power/SiC", False),
    ("6963", "ROHM Apollo", "Hirokawa-machi", "Hirokawa", "Fukuoka", "Japan", 33.2370, 130.5897, 5617, "2026-03", "Power/SiC", False),
    ("6963", "Lapis Semi", "Yokohama Kohoku", "Yokohama", "Kanagawa", "Japan", 35.5083, 139.6175, 53527, "2026-03", "Power/SiC", False),
    ("6963", "SiCrystal GmbH", "Nuremberg (SiC substrate)", "Nuremberg", "Bavaria", "Germany", 49.4521, 11.0767, 4604, "2026-03", "Power/SiC", False),
    ("6723", "Renesas", "Aggregate (Kofu reopening etc)", "Tokyo (agg)", "—", "Japan", 35.6762, 139.6503, 85000, "FY26", "Auto/logic", False),
    ("6266", "Tazmo", "Process eq + land/bldg agg", "Okayama (agg)", "—", "Japan", 34.6617, 133.9344, 6200, "FY26", "Coater/dev", False),
]

cluster_colors = {
    "Substrate": "#1f77b4",
    "Etch tools": "#ff7f0e",
    "Etch gases": "#d62728",
    "Deposition": "#2ca02c",
    "Test & probe": "#9467bd",
    "Adv. packaging": "#8c564b",
    "OEM parts": "#e377c2",
    "Wafer/materials": "#7f7f7f",
    "Materials": "#bcbd22",
    "Mask/optics": "#17becf",
    "Cleaning": "#aec7e8",
    "Fab automation": "#ffbb78",
    "NAND fab": "#c5b0d5",
    "Power/SiC": "#c49c94",
    "Auto/logic": "#f7b6d2",
    "Coater/dev": "#dbdb8d",
    "Chemicals": "#9edae5",
    "Chemicals (non-semi)": "#cccccc",
    "Healthcare": "#dddddd",
}

# Bubble sizes — sqrt scale. Three modes:
#   abs : raw plant capex ¥M (current default)
#   rev : plant capex ¥ / company revenue ¥ (capacity bet as % of revenue)
#   fa  : plant capex ¥ / company PP&E+CIP ¥ (capacity bet as % of existing fixed-asset base)
# Scaled per-mode so the largest bubble is ~60 diameter.

def compute_size_arrays():
    """Return dict {mode: [size for each plant in PLANTS order]}."""
    abs_vals = [p[8] * 1e6 for p in PLANTS]  # plant_capex_jpy
    rev_vals = []
    fa_vals = []
    for p in PLANTS:
        sec = p[0]
        capex_jpy = p[8] * 1e6
        metrics = COMPANY_METRICS.get(sec, {})
        rev = metrics.get("revenue_jpy")
        fa = metrics.get("fixed_assets_jpy")
        rev_vals.append(capex_jpy / rev if rev else 0.0)
        fa_vals.append(capex_jpy / fa if fa else 0.0)
    def scale_to_diameter(vals, target_max=60.0, min_d=6.0):
        if not vals:
            return []
        m = max(vals) or 1.0
        # sqrt scale so smaller plants are still visible
        return [max(min_d, math.sqrt(v / m) * target_max) for v in vals]
    return {
        "abs": scale_to_diameter(abs_vals, target_max=62.0, min_d=8.0),
        "rev": scale_to_diameter(rev_vals, target_max=58.0, min_d=6.0),
        "fa":  scale_to_diameter(fa_vals,  target_max=58.0, min_d=6.0),
    }

def size_of(jpym):
    """Back-compat: used for the initial figure render with absolute size."""
    return max(8, math.sqrt(jpym) * 0.55)

# Pre-compute size arrays (used by figure-build below and by JS)
SIZE_ARRAYS = compute_size_arrays()

# Build figure: one trace per cluster. Track plant-id ↔ (trace, point) mapping for JS.
fig = go.Figure()
sorted_clusters = sorted({p[10] for p in PLANTS})
# plant_index[i] = (trace_idx, point_idx) — used by client-side JS
plant_index = [None] * len(PLANTS)
trace_clusters = []  # parallel to figure traces

for cluster in sorted_clusters:
    trace_idx = len(fig.data)
    trace_clusters.append(cluster)
    # Stable order: filter PLANTS by cluster while preserving original index
    indexed = [(i, p) for i, p in enumerate(PLANTS) if p[10] == cluster]
    point_lons = []
    point_lats = []
    point_texts = []
    point_sizes = []
    for pt_idx, (i, r) in enumerate(indexed):
        plant_index[i] = (trace_idx, pt_idx)
        point_lons.append(r[7])
        point_lats.append(r[6])
        # Ratios for hover (None if not available)
        metrics = COMPANY_METRICS.get(r[0], {})
        plant_capex_jpy = r[8] * 1e6
        rev_pct = (plant_capex_jpy / metrics["revenue_jpy"] * 100) if metrics.get("revenue_jpy") else None
        fa_pct = (plant_capex_jpy / metrics["fixed_assets_jpy"] * 100) if metrics.get("fixed_assets_jpy") else None
        rev_txt = f"{rev_pct:.1f}%" if rev_pct is not None else "n/a"
        fa_txt = f"{fa_pct:.1f}%" if fa_pct is not None else "n/a"
        point_texts.append(
            f"<b>{r[1]}</b><br>"
            f"Plant: {r[2]}<br>"
            f"Location: {r[3]}, {r[4]}, {r[5]}<br>"
            f"Capex: <b>¥{r[8]/1000:.1f}B</b><br>"
            f"&nbsp;&nbsp;· of company revenue: <b>{rev_txt}</b><br>"
            f"&nbsp;&nbsp;· of PP&E+CIP: <b>{fa_txt}</b><br>"
            f"Completion: {r[9]}<br>"
            f"Sec: {r[0]} · Cluster: {r[10]}<br>"
            f"Hard capacity %: {'YES ⭐' if r[11] else 'no'}"
        )
        # Initial size = abs mode; restyle replaces on first applyFilters() call
        point_sizes.append(SIZE_ARRAYS["abs"][i])
    fig.add_trace(go.Scattergeo(
        lon=point_lons,
        lat=point_lats,
        text=point_texts,
        hovertemplate="%{text}<extra></extra>",
        name=cluster,
        marker=dict(
            size=point_sizes,
            color=cluster_colors.get(cluster, "#888888"),
            line=dict(width=1, color="white"),
            opacity=0.78,
            sizemode="diameter",
        ),
    ))

# Hard-cap overlay trace (last trace)
hard_trace_idx = len(fig.data)
hard = [(i, p) for i, p in enumerate(PLANTS) if p[11]]
fig.add_trace(go.Scattergeo(
    lon=[r[1][7] for r in hard],
    lat=[r[1][6] for r in hard],
    text=["⭐" for _ in hard],
    mode="text",
    textfont=dict(size=18, color="gold"),
    hoverinfo="skip",
    showlegend=False,
    name="⭐ hard cap %",
))

# Highlight overlay trace (initially empty, populated by JS when table is hovered)
highlight_trace_idx = len(fig.data)
fig.add_trace(go.Scattergeo(
    lon=[None],
    lat=[None],
    mode="markers",
    marker=dict(size=30, color="rgba(255,0,0,0)", line=dict(width=4, color="#ff3333"), symbol="circle"),
    hoverinfo="skip",
    showlegend=False,
    name="_highlight",
))

# View presets — lat range + center lon. Lon range is computed CLIENT-SIDE
# from the plot's actual width/height so the map always fills the .fig pane.
# Equirectangular projection so 1° lat = 1° lon at the equator (then we apply
# a latitude correction for the display center).
PRESETS_DEFS = {
    "Japan + Korea": dict(lat_range=[28, 47], center_lon=137),
    "All Asia": dict(lat_range=[2, 52], center_lon=122),
    "Kumamoto zoom": dict(lat_range=[32.55, 33.20], center_lon=130.85),
    "Gifu / ABF zoom": dict(lat_range=[35.15, 35.70], center_lon=136.60),
    "World": dict(lat_range=[-58, 75], center_lon=20),
}
# We no longer use updatemenus — buttons are rendered as plain HTML and call JS.
buttons = []
initial_preset_name = "Japan + Korea"
initial = dict(
    center=dict(lat=(PRESETS_DEFS[initial_preset_name]["lat_range"][0] + PRESETS_DEFS[initial_preset_name]["lat_range"][1]) / 2,
                lon=PRESETS_DEFS[initial_preset_name]["center_lon"]),
    projection_scale=1.0,
)

fig.update_layout(
    title=dict(
        text=(f"<b>JP Semiconductor Supply Chain — Disclosed New-Build Facility Capex</b><br>"
              f"<sub>From yuho 設備の新設、除却等の計画 across 35 names. Bubble = ¥M disclosed. ⭐ = hard capacity % disclosed. "
              f"Total pipeline: ¥{sum(p[8] for p in PLANTS)/1000:.0f}B across {len(PLANTS)} plant line items.</sub>"),
        x=0.02, xanchor="left", font=dict(size=18),
    ),
    geo=dict(
        scope="world",
        showcountries=True, countrycolor="#cccccc", countrywidth=0.5,
        showsubunits=True, subunitcolor="#dddddd", subunitwidth=0.4,
        showland=True, landcolor="#f8f8f8",
        showocean=True, oceancolor="#e8f1f6",
        projection_type="equirectangular",
        center=initial["center"],
        lataxis_range=PRESETS_DEFS[initial_preset_name]["lat_range"],
        # lonaxis_range is computed client-side in applyPreset() to match plot aspect
        resolution=50,
        domain=dict(x=[0, 1], y=[0, 1]),
    ),
    legend=dict(
        title="Process cluster (click to toggle)",
        bgcolor="rgba(255,255,255,0.92)",
        bordercolor="#888888", borderwidth=1,
        x=0.005, y=0.99, xanchor="left", yanchor="top",
        itemsizing="constant",
        font=dict(size=11),
    ),
    margin=dict(l=10, r=10, t=80, b=10),
    height=820,
    autosize=True,
    paper_bgcolor="white",
)

# Table rows — preserve original PLANTS index for sync.
rows_sorted = sorted(enumerate(PLANTS), key=lambda x: -x[1][8])

def color_for(cluster):
    return cluster_colors.get(cluster, "#888888")

table_rows_html = "\n".join(
    f'<tr data-pid="{idx}" data-sec="{r[0]}" data-cluster="{r[10]}" data-country="{r[5]}" data-company="{r[1].lower()}">'
    f'<td>{r[0]}</td>'
    f'<td>{r[1]}</td>'
    f'<td>{r[2]}</td>'
    f'<td>{r[3]}, {r[4]}</td>'
    f'<td>{r[5]}</td>'
    f'<td style="text-align:right;font-variant-numeric:tabular-nums;"><b>{r[8]/1000:.1f}</b></td>'
    f'<td>{r[9]}</td>'
    f'<td><span class="chip" style="background:{color_for(r[10])};">{r[10]}</span></td>'
    f'<td style="text-align:center;">{"⭐" if r[11] else ""}</td>'
    f'</tr>'
    for idx, r in rows_sorted
)

# JS data array — plant_id → trace+point mapping + lat/lon + size arrays (3 modes)
plant_js = json.dumps([
    {
        "pid": i,
        "trace": plant_index[i][0],
        "point": plant_index[i][1],
        "lat": p[6],
        "lon": p[7],
        "sizeAbs": SIZE_ARRAYS["abs"][i],
        "sizeRev": SIZE_ARRAYS["rev"][i],
        "sizeFa":  SIZE_ARRAYS["fa"][i],
        # used by the highlight overlay; default to absolute
        "size": SIZE_ARRAYS["abs"][i],
        "capex": p[8],
        "capexJpy": p[8] * 1e6,
        "sec": p[0],
        # ratios as percentages for tooltip (-1 if not available)
        "revRatio": (COMPANY_METRICS.get(p[0], {}).get("revenue_jpy") and
                     round(p[8] * 1e6 / COMPANY_METRICS[p[0]]["revenue_jpy"] * 100, 2)) or None,
        "faRatio":  (COMPANY_METRICS.get(p[0], {}).get("fixed_assets_jpy") and
                     round(p[8] * 1e6 / COMPANY_METRICS[p[0]]["fixed_assets_jpy"] * 100, 2)) or None,
    }
    for i, p in enumerate(PLANTS)
])
trace_clusters_js = json.dumps(trace_clusters)
print(f"Companies with revenue data: {sum(1 for sec, m in COMPANY_METRICS.items() if m.get('revenue_jpy'))}/{len(COMPANY_METRICS)}")
print(f"Companies with FA data: {sum(1 for sec, m in COMPANY_METRICS.items() if m.get('fixed_assets_jpy'))}/{len(COMPANY_METRICS)}")

# Distinct values for filter dropdowns
all_clusters = sorted({r[10] for r in PLANTS})
all_countries = sorted({r[5] for r in PLANTS})
all_secs = sorted({r[0] for r in PLANTS})

cluster_options = "\n".join(f'<option value="{c}">{c}</option>' for c in all_clusters)
country_options = "\n".join(f'<option value="{c}">{c}</option>' for c in all_countries)
sec_options = "\n".join(f'<option value="{s}">{s}</option>' for s in all_secs)

out_path = "../facilities-map.html"

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>JP Semi Facilities Map (2026-05-27)</title>
<script src="https://cdn.plot.ly/plotly-3.0.1.min.js"></script>
<style>
* {{ box-sizing: border-box; }}
html, body {{ height: 100%; }}
body {{ margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; background: #fbfbfb; color: #222; overflow: hidden; display: flex; flex-direction: column; }}
.report-meta {{ flex: 0 0 auto; padding: 6px 18px; background: #1f2937; color: #fff; font-size: 12px; letter-spacing: 0.3px; }}
.report-meta b {{ color: #fff; }}
.upper-pane {{ flex: 0 0 65vh; overflow-y: auto; overscroll-behavior: contain; padding-top: 12px; min-height: 80px; }}
.divider {{ flex: 0 0 26px; background: linear-gradient(to bottom, #f4f4f4, #dadada, #f4f4f4); cursor: row-resize; border-top: 1px solid #c5c5c5; border-bottom: 1px solid #c5c5c5; position: relative; transition: background 0.15s; display: flex; align-items: center; justify-content: center; gap: 8px; user-select: none; }}
.divider:hover, .divider.dragging {{ background: linear-gradient(to bottom, #e3eef9, #b7d3ee, #e3eef9); }}
.divider .grip {{ width: 36px; height: 3px; background: #999; border-radius: 2px; }}
.divider .preset-btn {{ font-size: 11px; padding: 2px 9px; border: 1px solid #aaa; background: #fff; border-radius: 4px; cursor: pointer; color: #444; }}
.divider .preset-btn:hover {{ background: #1f78d1; color: #fff; border-color: #1f78d1; }}
.divider .label {{ font-size: 11px; color: #555; margin: 0 4px; }}
.lower-pane {{ flex: 1 1 0; min-height: 120px; display: flex; flex-direction: column; }}
h1 {{ font-size: 20px; margin: 6px 0; }}
.intro {{ margin: 0 12px 12px 12px; padding: 14px 18px; background: #fff; border: 1px solid #e0e0e0; border-radius: 6px; font-size: 14px; line-height: 1.55; }}
.intro b {{ color: #111; }}
.intro ul {{ margin: 6px 0; padding-left: 22px; }}
.intro details summary {{ cursor: pointer; font-weight: 600; color: #1f78d1; padding: 4px 0; user-select: none; }}
.intro details summary:hover {{ color: #0f5da8; }}
.intro details[open] summary {{ margin-bottom: 6px; }}
.fig {{ margin: 0 12px 12px; background: #fff; border: 1px solid #e0e0e0; border-radius: 6px; padding: 6px; box-sizing: border-box; }}
.preset-bar {{ display: flex; align-items: center; gap: 6px; padding: 6px 14px; flex-wrap: wrap; background: #fff; margin: 0 12px 0; border: 1px solid #e0e0e0; border-bottom: none; border-radius: 6px 6px 0 0; }}
.preset-bar + .fig {{ margin-top: 0; border-top: none; border-radius: 0 0 6px 6px; }}
.preset-label {{ font-size: 12px; color: #555; }}
.preset-bar button.preset {{ font-size: 12px; padding: 4px 10px; border: 1px solid #aaa; background: #fff; border-radius: 4px; cursor: pointer; color: #333; }}
.preset-bar button.preset:hover {{ background: #1f78d1; color: #fff; border-color: #1f78d1; }}
.preset-bar button.preset.active {{ background: #1f78d1; color: #fff; border-color: #1f78d1; }}
.fig > div {{ width: 100% !important; }}
.table-wrap {{ margin: 0 12px 12px; background: #fff; border: 1px solid #e0e0e0; border-radius: 6px; padding: 14px; display: flex; flex-direction: column; flex: 1 1 0; min-height: 0; }}
.table-wrap h2 {{ margin: 0 0 10px; font-size: 17px; flex: 0 0 auto; }}
.table-wrap .filters {{ flex: 0 0 auto; }}
.table-scroll {{ flex: 1 1 0; min-height: 0; overflow-y: auto; overflow-x: auto; overscroll-behavior: contain; border: 1px solid #eee; border-radius: 4px; -webkit-overflow-scrolling: touch; }}
.filters {{ display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 12px; align-items: center; }}
.filters label {{ font-size: 12px; color: #555; }}
.filters input, .filters select {{ font-size: 13px; padding: 5px 8px; border: 1px solid #bbb; border-radius: 4px; min-width: 120px; }}
.filters input[type="text"] {{ min-width: 220px; }}
.filters button {{ font-size: 12px; padding: 5px 10px; border: 1px solid #888; background: #f4f4f4; border-radius: 4px; cursor: pointer; }}
.filters button:hover {{ background: #e8e8e8; }}
.count {{ font-size: 12px; color: #666; margin-left: auto; }}
table {{ width: 100%; border-collapse: collapse; font-size: 12.5px; }}
.table-scroll thead th {{ position: sticky; top: 0; background: #f4f4f4; padding: 8px 6px; text-align: left; font-weight: 600; border-bottom: 2px solid #ccc; cursor: pointer; user-select: none; z-index: 2; }}
.table-scroll thead th:hover {{ background: #ebebeb; }}
thead th.sortedAsc::after {{ content: " ▲"; font-size: 10px; color: #666; }}
thead th.sortedDesc::after {{ content: " ▼"; font-size: 10px; color: #666; }}
tbody tr {{ border-bottom: 1px solid #eee; cursor: pointer; }}
tbody tr:hover, tbody tr.row-highlight {{ background: #fffbe0; box-shadow: inset 3px 0 0 #f5a623; }}
tbody td {{ padding: 6px 6px; vertical-align: top; }}
.chip {{ display: inline-block; padding: 2px 7px; border-radius: 10px; font-size: 11px; color: #fff; font-weight: 500; white-space: nowrap; }}
.hidden {{ display: none !important; }}
.sync-badge {{ display: inline-block; padding: 2px 8px; background: #1f78d1; color: #fff; border-radius: 10px; font-size: 11px; font-weight: 500; }}
</style>
</head>
<body>
<div class="report-meta">
<b>Report date: 2026-05-27</b> · Data source: yuho XBRL through FY25 filings · Sibling to <code>hbf-nand-jp-capex-mtp-2026-05-26.md</code> · Companion dashboard: <code>hbf-nand-jp-dashboard-2026-05-26.html</code>
</div>
<div class="upper-pane">
<div class="intro">
<h1>JP Semiconductor Supply Chain — Disclosed New-Build Facility Capex (2026-05-27)</h1>
<p>Source: yuho 「設備の新設、除却等の計画」 across <b>35 JP semi-supply-chain filers</b>. Bubble size on the map is proportional to ¥M disclosed in the latest annual yuho. <b>Total disclosed pipeline: ¥{sum(p[8] for p in PLANTS)/1000:.0f}B</b> across <b>{len(PLANTS)} active plant line items</b>.</p>
<ul>
<li><b>View buttons below the map</b> jump between presets: Japan+Korea (default), All Asia, Kumamoto zoom (TSMC JASM gravity), Gifu zoom (Ibiden ABF cluster), and World (US/EU/SE Asia subsidiaries).</li>
<li><b>⭐ = hard capacity % disclosed in yuho</b> (only 6 cases across 35 names): TEL Miyagi +250%, TEL Solutions Iwate +50%, Shinko Chikuma +50%, Shinko Arai BGA, Stella Sanpo ~2× filling, Kanto Denka Mizushima 新設・増強, Kioxia Yokkaichi/Kitakami gen-8.</li>
<li><b>Six names disclosed NO new-build at all</b> (not on the map): 6920 Lasertec, 3436 SUMCO, 6857 Advantest, 6315 TOWA, 6728 Ulvac, 4966 Uyemura. CIP/capex is going into equipment-into-existing-shells, not new construction.</li>
<li><b>Note:</b> Several filers disclose only at segment-level aggregate (Shin-Etsu, Resonac, Mitsui Chem, Renesas, SBHPP, Tazmo) — those rows are plotted at the company HQ city as a placeholder marked "(agg)".</li>
</ul>
</div>

<div class="preset-bar">
  <span class="preset-label"><b>View:</b></span>
  <button class="preset" data-preset="Japan + Korea">Japan + Korea</button>
  <button class="preset" data-preset="All Asia">All Asia</button>
  <button class="preset" data-preset="Kumamoto zoom">Kumamoto zoom</button>
  <button class="preset" data-preset="Gifu / ABF zoom">Gifu / ABF zoom</button>
  <button class="preset" data-preset="World">World</button>
</div>
<div class="fig" id="fig1"></div>
</div><!-- /upper-pane -->

<div class="divider" id="divider" title="Drag to resize map ↔ table">
  <button type="button" class="preset-btn" onclick="setSplit('map')" title="Maximize map view">▲ map</button>
  <span class="grip"></span>
  <span class="label">drag to resize</span>
  <span class="grip"></span>
  <button type="button" class="preset-btn" onclick="setSplit('table')" title="Maximize table view">table ▼</button>
  <button type="button" class="preset-btn" onclick="setSplit('even')" title="50/50 split">⇅ even</button>
</div>

<div class="lower-pane">
<div class="table-wrap">
<h2>All plant line items — filterable + sortable</h2>
<div class="filters">
<label>Search: <input type="text" id="searchInput" placeholder="company / plant / city" /></label>
<label>Cluster: <select id="clusterFilter"><option value="">All clusters</option>{cluster_options}</select></label>
<label>Country: <select id="countryFilter"><option value="">All countries</option>{country_options}</select></label>
<label>Sec code: <select id="secFilter"><option value="">All sec codes</option>{sec_options}</select></label>
<label>Bubble size:
<select id="sizeMode">
<option value="abs">Absolute ¥ capex</option>
<option value="fa">Capex / (PP&amp;E+CIP) — capacity-add %</option>
<option value="rev">Capex / Revenue — commitment %</option>
</select></label>
<label><input type="checkbox" id="hardOnly"/> Hard-capacity only (⭐)</label>
<label><input type="checkbox" id="syncViewport"/> 🗺️ Sync table to map view</label>
<button id="resetBtn">Reset</button>
<span class="count" id="count"></span>
</div>
<div class="table-scroll" id="tableScroll">
<table id="plantTable">
<thead>
<tr>
<th data-key="0">Sec</th>
<th data-key="1">Company</th>
<th data-key="2">Plant</th>
<th data-key="3">City / Prefecture</th>
<th data-key="4">Country</th>
<th data-key="5" data-numeric="true">Capex ¥B</th>
<th data-key="6">Completion</th>
<th data-key="7">Cluster</th>
<th data-key="8">⭐</th>
</tr>
</thead>
<tbody id="plantBody">
{table_rows_html}
</tbody>
</table>
</div><!-- /table-scroll -->
</div><!-- /table-wrap -->
</div><!-- /lower-pane -->

<script>
var PLANTS = {plant_js};
var TRACE_CLUSTERS = {trace_clusters_js};
var HIGHLIGHT_TRACE_IDX = {highlight_trace_idx};
var N_CLUSTERS = TRACE_CLUSTERS.length;

// Preset definitions — lat range + center lon. Lon range computed dynamically
// based on .fig width/height so the map fills the pane.
var PRESETS = {json.dumps(PRESETS_DEFS)};
var currentPresetName = "{initial_preset_name}";

function getPlotDims() {{
  // Plot area dimensions inside .fig (subtract margins/borders/title)
  var fig = document.getElementById('fig1');
  var rect = fig.getBoundingClientRect();
  var w = Math.max(200, rect.width - 20);   // 10px L/R margin from layout
  var h = Math.max(150, rect.height - 90);  // 80px title + 10px bottom
  return {{ w: w, h: h }};
}}

function computeLonRangeForPreset(name) {{
  var preset = PRESETS[name];
  if (!preset) return null;
  var dims = getPlotDims();
  var aspect = dims.w / dims.h;
  var latRange = preset.lat_range;
  var latSpan = latRange[1] - latRange[0];
  // equirectangular: 1° lat = 1° lon (visual pixels), so lon_span = lat_span * aspect
  var lonSpan = latSpan * aspect;
  var lonCenter = preset.center_lon;
  return [lonCenter - lonSpan / 2, lonCenter + lonSpan / 2];
}}

function applyPreset(name) {{
  var preset = PRESETS[name];
  if (!preset) return;
  currentPresetName = name;
  var latRange = preset.lat_range;
  var lonRange = computeLonRangeForPreset(name);
  var latCenter = (latRange[0] + latRange[1]) / 2;
  Plotly.relayout('fig1', {{
    'geo.center': {{ lat: latCenter, lon: preset.center_lon }},
    'geo.lataxis.range': latRange,
    'geo.lonaxis.range': lonRange,
  }});
  // Update active button styling
  document.querySelectorAll('.preset-bar button.preset').forEach(function(b) {{
    b.classList.toggle('active', b.dataset.preset === name);
  }});
}}

// Wire up preset buttons
document.querySelectorAll('.preset-bar button.preset').forEach(function(b) {{
  b.addEventListener('click', function() {{ applyPreset(b.dataset.preset); }});
}});

// ===== Resizable split (drag the divider) =====
var upperPane = document.querySelector('.upper-pane');
var divider = document.getElementById('divider');
var lowerPane = document.querySelector('.lower-pane');
var dragging = false;
var dragStartY = 0;
var dragStartUpperH = 0;
var SAVED_KEY = 'hbf-nand-jp-facilities-split-vh';

function setUpperHeight(px) {{
  // Clamp: at least 200px (so map stays visible), at most viewport - 160px (so table has room)
  var maxH = window.innerHeight - 160;
  px = Math.max(200, Math.min(maxH, px));
  upperPane.style.flex = '0 0 ' + px + 'px';
  // Trigger Plotly resize + re-apply preset so map keeps filling new pane size
  if (window.plotReady && window.Plotly && document.getElementById('fig1')) {{
    Plotly.Plots.resize('fig1');
    if (typeof applyPreset === 'function' && currentPresetName) {{
      applyPreset(currentPresetName);
    }}
  }}
}}

window.setSplit = function(mode) {{
  var vh = window.innerHeight;
  var target;
  if (mode === 'map') target = vh * 0.85;
  else if (mode === 'table') target = vh * 0.18;
  else target = vh * 0.50;  // 'even'
  setUpperHeight(target);
  try {{ localStorage.setItem(SAVED_KEY, String(target / vh)); }} catch(e) {{}}
}};

divider.addEventListener('mousedown', function(e) {{
  dragging = true;
  dragStartY = e.clientY;
  dragStartUpperH = upperPane.getBoundingClientRect().height;
  divider.classList.add('dragging');
  document.body.style.cursor = 'row-resize';
  document.body.style.userSelect = 'none';
  e.preventDefault();
}});
window.addEventListener('mousemove', function(e) {{
  if (!dragging) return;
  var delta = e.clientY - dragStartY;
  setUpperHeight(dragStartUpperH + delta);
}});
window.addEventListener('mouseup', function(e) {{
  if (!dragging) return;
  dragging = false;
  divider.classList.remove('dragging');
  document.body.style.cursor = '';
  document.body.style.userSelect = '';
  try {{
    var frac = upperPane.getBoundingClientRect().height / window.innerHeight;
    localStorage.setItem(SAVED_KEY, String(frac));
  }} catch(e) {{}}
}});
// Restore saved split — runs AFTER Plotly is fully rendered to avoid blanking the map
function restoreSavedSplit() {{
  try {{
    var saved = parseFloat(localStorage.getItem(SAVED_KEY));
    // Guard rails: must be a valid number AND in a sane range (≥0.30 to keep map visible)
    if (!isNaN(saved) && saved >= 0.30 && saved < 0.92) {{
      setUpperHeight(saved * window.innerHeight);
    }} else if (!isNaN(saved)) {{
      // Out-of-range saved value — clear it so we revert to CSS default
      localStorage.removeItem(SAVED_KEY);
    }}
  }} catch(e) {{}}
}}

var fig = {fig.to_json()};
var mapDiv = document.getElementById('fig1');

// Track ready state so synchronous code paths don't fight Plotly's initial render
window.plotReady = false;
Plotly.newPlot('fig1', fig.data, fig.layout, {{responsive: true}}).then(function() {{
  window.plotReady = true;
  attachMapEvents();
  restoreSavedSplit();
  Plotly.Plots.resize('fig1');
  // Apply initial preset with aspect-correct lon range so map fills pane
  applyPreset(currentPresetName);
  readMapBounds();
  // First filter pass — runs only after plot is fully initialized
  applyFilters();
}});
// On window resize: re-fit chart AND re-apply current preset so map keeps filling.
window.addEventListener('resize', function() {{
  if (!window.plotReady) return;
  Plotly.Plots.resize('fig1');
  applyPreset(currentPresetName);
}});

// ===== State =====
var rows = Array.from(document.querySelectorAll('#plantBody tr'));
// pid → row element
var pidToRow = {{}};
rows.forEach(function(tr) {{ pidToRow[parseInt(tr.dataset.pid)] = tr; }});

// pid → visible flag (after filters + viewport)
var visibleSet = new Set();
var mapBounds = null;  // {{lon:[min,max], lat:[min,max]}}

// ===== Map bounds reader =====
function readMapBounds() {{
  var fullLayout = mapDiv._fullLayout;
  if (!fullLayout || !fullLayout.geo) return;
  var g = fullLayout.geo;
  // Plotly stores effective ranges in lonaxis/lataxis._rangeProvided or geo._subplot._range,
  // but the simpler path: use the layout.geo.lonaxis.range / lataxis.range if set.
  var lo = (g.lonaxis && g.lonaxis.range) || (g._fullLayout && g._fullLayout.lonaxis.range);
  var la = (g.lataxis && g.lataxis.range) || (g._fullLayout && g._fullLayout.lataxis.range);
  if (lo && la) {{
    mapBounds = {{lon: lo.slice(), lat: la.slice()}};
  }}
}}

function pointInBounds(p) {{
  if (!mapBounds) return true;
  return p.lon >= mapBounds.lon[0] && p.lon <= mapBounds.lon[1]
      && p.lat >= mapBounds.lat[0] && p.lat <= mapBounds.lat[1];
}}

// ===== Size mode =====
function currentSize(p) {{
  var mode = document.getElementById('sizeMode').value;
  if (mode === 'rev') return p.sizeRev;
  if (mode === 'fa') return p.sizeFa;
  return p.sizeAbs;
}}

// ===== Apply filters → both table and map =====
function applyFilters() {{
  var q = document.getElementById('searchInput').value.toLowerCase().trim();
  var cluster = document.getElementById('clusterFilter').value;
  var country = document.getElementById('countryFilter').value;
  var sec = document.getElementById('secFilter').value;
  var hardOnly = document.getElementById('hardOnly').checked;
  var syncVp = document.getElementById('syncViewport').checked;

  visibleSet.clear();
  var shown = 0;
  rows.forEach(function(tr) {{
    var pid = parseInt(tr.dataset.pid);
    var p = PLANTS[pid];
    var match = true;
    if (q && tr.textContent.toLowerCase().indexOf(q) === -1) match = false;
    if (cluster && tr.dataset.cluster !== cluster) match = false;
    if (country && tr.dataset.country !== country) match = false;
    if (sec && tr.dataset.sec !== sec) match = false;
    if (hardOnly && tr.children[8].textContent.trim() === '') match = false;
    if (syncVp && !pointInBounds(p)) match = false;
    tr.classList.toggle('hidden', !match);
    if (match) {{ shown++; visibleSet.add(pid); }}
  }});

  document.getElementById('count').textContent =
    shown + ' of ' + rows.length + ' plants' + (syncVp ? ' (synced to map view)' : '');

  // Update map opacities + sizes based on current size mode
  var opacities = []; var sizes = [];
  for (var t = 0; t < N_CLUSTERS; t++) {{ opacities.push([]); sizes.push([]); }}
  PLANTS.forEach(function(p) {{
    var inView = visibleSet.has(p.pid);
    var s = currentSize(p);
    opacities[p.trace][p.point] = inView ? 0.78 : 0.06;
    sizes[p.trace][p.point] = inView ? s : Math.max(3, s * 0.35);
  }});
  Plotly.restyle('fig1', {{'marker.opacity': opacities, 'marker.size': sizes}},
                 Array.from({{length: N_CLUSTERS}}, function(_, i) {{ return i; }}));
}}

['searchInput','clusterFilter','countryFilter','secFilter','hardOnly','syncViewport','sizeMode'].forEach(function(id) {{
  var el = document.getElementById(id);
  el.addEventListener('input', applyFilters);
  el.addEventListener('change', applyFilters);
}});
document.getElementById('resetBtn').addEventListener('click', function() {{
  document.getElementById('searchInput').value = '';
  document.getElementById('clusterFilter').value = '';
  document.getElementById('countryFilter').value = '';
  document.getElementById('secFilter').value = '';
  document.getElementById('hardOnly').checked = false;
  document.getElementById('syncViewport').checked = false;
  applyFilters();
}});

// ===== Map events =====
function attachMapEvents() {{
  mapDiv.on('plotly_hover', function(data) {{
    if (!data.points || !data.points.length) return;
    var pt = data.points[0];
    // Find which plant matches (curveNumber, pointNumber)
    var pid = pidFromTracePoint(pt.curveNumber, pt.pointNumber);
    if (pid !== null) highlightRow(pid, true);
  }});
  mapDiv.on('plotly_unhover', function() {{ clearRowHighlight(); }});
  mapDiv.on('plotly_relayout', function(event) {{
    // After any pan/zoom/preset, recompute mapBounds and (if syncViewport on) refilter
    setTimeout(function() {{
      readMapBounds();
      if (document.getElementById('syncViewport').checked) applyFilters();
    }}, 50);
  }});
}}

function pidFromTracePoint(traceIdx, pointIdx) {{
  for (var i = 0; i < PLANTS.length; i++) {{
    if (PLANTS[i].trace === traceIdx && PLANTS[i].point === pointIdx) return PLANTS[i].pid;
  }}
  return null;
}}

function highlightRow(pid, scrollTo) {{
  clearRowHighlight();
  var tr = pidToRow[pid];
  if (!tr) return;
  tr.classList.add('row-highlight');
  if (scrollTo) {{
    // Only auto-scroll if row is not visible
    var rect = tr.getBoundingClientRect();
    if (rect.top < 60 || rect.bottom > window.innerHeight - 20) {{
      tr.scrollIntoView({{behavior: 'smooth', block: 'center'}});
    }}
  }}
}}
function clearRowHighlight() {{
  document.querySelectorAll('.row-highlight').forEach(function(tr) {{ tr.classList.remove('row-highlight'); }});
}}

// ===== Table → Map sync =====
function highlightMapPoint(pid) {{
  var p = PLANTS[pid];
  if (!p) return;
  var s = currentSize(p);
  Plotly.restyle('fig1', {{
    lon: [[p.lon]],
    lat: [[p.lat]],
    'marker.size': [Math.max(28, s + 14)],
  }}, [HIGHLIGHT_TRACE_IDX]);
}}
function clearMapHighlight() {{
  Plotly.restyle('fig1', {{lon: [[null]], lat: [[null]]}}, [HIGHLIGHT_TRACE_IDX]);
}}
rows.forEach(function(tr) {{
  tr.addEventListener('mouseenter', function() {{
    var pid = parseInt(tr.dataset.pid);
    highlightMapPoint(pid);
  }});
  tr.addEventListener('mouseleave', clearMapHighlight);
}});

// ===== Sort =====
var sortState = {{ col: 5, dir: 'desc' }};
var headers = document.querySelectorAll('#plantTable thead th');
headers.forEach(function(th, idx) {{
  th.addEventListener('click', function() {{
    var dir = (sortState.col === idx && sortState.dir === 'asc') ? 'desc' : 'asc';
    sortState = {{ col: idx, dir: dir }};
    var numeric = th.dataset.numeric === 'true';
    var sorted = rows.slice().sort(function(a, b) {{
      var av = a.children[idx].textContent.trim();
      var bv = b.children[idx].textContent.trim();
      if (numeric) {{ av = parseFloat(av) || 0; bv = parseFloat(bv) || 0; }}
      if (av < bv) return dir === 'asc' ? -1 : 1;
      if (av > bv) return dir === 'asc' ? 1 : -1;
      return 0;
    }});
    var tbody = document.getElementById('plantBody');
    sorted.forEach(function(tr) {{ tbody.appendChild(tr); }});
    headers.forEach(function(h) {{ h.classList.remove('sortedAsc','sortedDesc'); }});
    th.classList.add(dir === 'asc' ? 'sortedAsc' : 'sortedDesc');
  }});
}});
headers[5].classList.add('sortedDesc');

// Initialize count display only (no restyle yet — applyFilters() runs after Plotly.newPlot resolves)
(function initCount() {{
  document.getElementById('count').textContent = rows.length + ' of ' + rows.length + ' plants';
}})();
</script>
</body>
</html>
"""

with open(out_path, "w") as f:
    f.write(html)

import os
print(f"Wrote {out_path}")
print(f"File size: {os.path.getsize(out_path)/1024:.1f} KB")
print(f"Rows: {len(PLANTS)} | Total capex: ¥{sum(p[8] for p in PLANTS)/1000:.0f}B")
