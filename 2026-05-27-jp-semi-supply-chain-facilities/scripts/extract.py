#!/usr/bin/env python3
# NOTE: these scripts depend on:
#  - a local MinIO/filesystem store of EDINET yuho XBRL documents at STORAGE_ROOT
#  - the `edinet` CLI (https://github.com/komsit37 - private)
# Adapt STORAGE_ROOT and OUT_DIR to your local setup before running.

"""Extract PP&E, CIP, advances/contract liabilities, and 受注実績 backlog
across 20 HBF/NAND screen names × 5 fiscal years from EDINET XBRL filings.

Output: /tmp/hbf_capex_v2/orderbook/_data.json
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

STORAGE_ROOT = Path("/srv/bulk/apps/jp-stock-filings/storage/edinet/docs")
OUT_DIR = Path("/tmp/hbf_capex_v2/orderbook")

# Names from the screen, in cluster order. Tier ext = extended universe (2026-05-27 additions).
NAMES = [
    ("6525", "KOKUSAI Electric"),
    ("4369", "Tri Chemical Labs"),
    ("8035", "Tokyo Electron"),
    ("6590", "Shibaura Mech"),
    ("4047", "Kanto Denka"),
    ("6920", "Lasertec"),
    ("3436", "SUMCO"),
    ("4238", "Mirial"),
    ("6857", "Advantest"),
    ("6871", "Nihon Micronics"),
    ("6855", "JEM"),
    ("6627", "TeraProbe"),
    ("6961", "Enplas"),
    ("4062", "Ibiden"),
    ("4975", "JCU"),
    ("4966", "C. Uyemura"),
    ("6146", "Disco"),
    ("6988", "Nitto Denko"),
    ("4203", "Sumitomo Bakelite"),
    ("3433", "Tocalo"),
    # 2026-05-27 extension — broader JP semi supply chain
    ("4063", "Shin-Etsu Chemical"),     # silicon wafer + photoresist + magnets
    ("4004", "Resonac"),                # HBM underfill, CMP slurry, EMC
    ("7741", "Hoya"),                   # EUV mask blanks
    ("7735", "SCREEN Holdings"),        # wafer cleaning tools
    ("4186", "Tokyo Ohka Kogyo"),       # photoresist
    ("6315", "TOWA"),                   # IC molding tools (AP)
    ("6728", "Ulvac"),                  # PVD/sputter
    ("4109", "Stella Chemifa"),         # HF etch chemistry
    ("6967", "Shinko Electric"),        # IC substrates (delisting in progress 2024)
    ("6383", "Daifuku"),                # fab automation/MHE
    ("285A", "Kioxia"),                 # NAND maker (Dec 2024 IPO)
    ("4183", "Mitsui Chemicals"),       # NF3 exit story
    ("6963", "ROHM"),                   # power/SiC
    ("6723", "Renesas"),                # auto/logic
    ("6266", "Tazmo"),                  # coater/developer (small-cap TEL echo)
]

# Target XBRL tags — use jppfs_cor (JGAAP) and jpigp_cor (IFRS) namespaces.
# For each, we want CurrentYearInstant (consolidated, current period).
TARGET_TAGS = {
    "ppe": [
        "jppfs_cor:PropertyPlantAndEquipment",
        "jpigp_cor:PropertyPlantAndEquipmentIFRS",
        "jpigp_cor:PropertyPlantAndEquipmentIFRSSummaryOfBusinessResults",
    ],
    "cip": [
        "jppfs_cor:ConstructionInProgress",
        "jpigp_cor:ConstructionInProgressIFRS",
    ],
    "advances": [
        "jppfs_cor:AdvancesReceived",
        "jppfs_cor:ContractLiabilities",
        "jpigp_cor:ContractLiabilitiesCAIFRS",
        "jpigp_cor:ContractLiabilitiesIFRS",
    ],
}

# Order book table parsing — looks for 受注高 and 受注残高 columns.

def search_yuho_docs(sec_code, limit=6):
    """Return list of (doc_id, period_end) for the most recent yuho filings."""
    out = subprocess.run(
        ["edinet", "search", sec_code, "--doc-type", "120", "--limit", str(limit), "--format", "json"],
        capture_output=True, text=True, timeout=60,
    )
    if out.returncode != 0:
        print(f"  ! search failed for {sec_code}: {out.stderr[:200]}", file=sys.stderr)
        return []
    data = json.loads(out.stdout)
    docs = []
    for d in data.get("documents", []):
        docs.append((d["doc_id"], d["period_end"]))
    return docs

def ensure_extract(doc_id):
    """Ensure extract.html exists for doc_id; return path or None."""
    p = STORAGE_ROOT / doc_id / "extract.html"
    if p.exists():
        return p
    out = subprocess.run(
        ["edinet", "xbrl", "extract", doc_id],
        capture_output=True, text=True, timeout=180,
    )
    if p.exists():
        return p
    print(f"  ! extract failed for {doc_id}: {out.stderr[:200]}", file=sys.stderr)
    return None

# Match <ix:nonFraction ... name="NAME" ... contextRef="CTX" ... scale="N" ...>VALUE</ix:nonFraction>
IX_RE = re.compile(
    r'<ix:nonFraction\b([^>]*?)>([^<]+)</ix:nonFraction>',
    re.DOTALL,
)
ATTR_NAME_RE = re.compile(r'\bname="([^"]+)"')
ATTR_CTX_RE = re.compile(r'\bcontextRef="([^"]+)"')
ATTR_SCALE_RE = re.compile(r'\bscale="([^"]+)"')
ATTR_SIGN_RE = re.compile(r'\bsign="([^"]+)"')

def extract_tags(html_path):
    """Return dict of {tag_name: {ctx: value_jpy_int}} for all ix:nonFraction in file."""
    text = html_path.read_text(encoding="utf-8", errors="replace")
    out = {}
    for m in IX_RE.finditer(text):
        attrs, raw = m.group(1), m.group(2).strip()
        nm = ATTR_NAME_RE.search(attrs)
        ctx = ATTR_CTX_RE.search(attrs)
        if not nm or not ctx:
            continue
        name = nm.group(1)
        # Filter to tags of interest
        keep = False
        for tags in TARGET_TAGS.values():
            if name in tags:
                keep = True
                break
        if not keep:
            continue
        ctx_v = ctx.group(1)
        # Parse number
        raw_clean = raw.replace(",", "").replace("△", "-").replace("−", "-")
        try:
            num = float(raw_clean)
        except ValueError:
            continue
        scale = ATTR_SCALE_RE.search(attrs)
        if scale:
            num = num * (10 ** int(scale.group(1)))
        sign = ATTR_SIGN_RE.search(attrs)
        if sign and sign.group(1) == "-":
            num = -num
        out.setdefault(name, {})[ctx_v] = int(num)
    return out

def pick_value(tag_data, tag_list, ctx_pref=("CurrentYearInstant", "Prior1YearInstant")):
    """Return (value, ctx_used) for the first tag/ctx match, or (None, None)."""
    for tag in tag_list:
        if tag in tag_data:
            for ctx in ctx_pref:
                if ctx in tag_data[tag]:
                    return tag_data[tag][ctx], f"{tag}@{ctx}"
    return None, None

# Order book table extraction.
# Pattern: find 受注実績 table, parse the column header to determine unit (千円 vs 百万円),
# find the 合計 (total) row or single data row, pull 受注高 / 受注残高 values.

# Match the unit cell from column header — both half-width () and full-width （）, allow whitespace/HTML between 受注高 and unit
UNIT_RE = re.compile(r'受注高.{0,500}?[\(（](千円|百万円|円)[\)）]', re.DOTALL)
# Numeric cells: look for >NNN,NNN< pattern, integer only (YoY% has decimals)
CELL_NUM_RE = re.compile(r'>\s*([0-9,]+(?:\.[0-9]+)?)\s*<')

def extract_order_book(html_path):
    """Return (orders_received_mm, order_backlog_mm) normalized to MM JPY, or (None, None)."""
    text = html_path.read_text(encoding="utf-8", errors="replace")
    if "受注実績" not in text or "受注残高" not in text:
        return None, None
    # Find 受注実績 section
    m = re.search(r'受注実績(.{0,30000}?)(?:生産実績|販売実績|（ロ）|\(ロ\))', text, re.DOTALL)
    if not m:
        return None, None
    section = m.group(1)
    # Detect unit
    unit_m = UNIT_RE.search(section)
    if not unit_m:
        return None, None
    unit = unit_m.group(1)
    unit_factor = {"千円": 1e-3, "百万円": 1.0, "円": 1e-6}[unit]  # convert to MM JPY
    # Find 合計 row first; if none, take first data row after the column-header section
    gm = re.search(r'合計(.{0,3000}?)</tr>', section, re.DOTALL)
    if gm:
        row = gm.group(1)
    else:
        # Take first <tr> that comes after the last column-header label
        header_end = section.rfind("前年同期比")
        if header_end < 0:
            return None, None
        body = section[header_end:]
        # Skip the % header row and find the first data row
        gm2 = re.search(r'</tr>\s*(.{0,3000}?)</tr>', body, re.DOTALL)
        if not gm2:
            return None, None
        row = gm2.group(1)
    nums = CELL_NUM_RE.findall(row)
    # Filter to integers only (cells without decimal point are 受注高/受注残高; YoY% has decimal)
    big_nums = [int(n.replace(",", "")) for n in nums if "." not in n]
    if len(big_nums) >= 2:
        recv = big_nums[0] * unit_factor
        back = big_nums[1] * unit_factor
        return int(round(recv)), int(round(back))
    return None, None

def main():
    results = {}
    for sec_code, name in NAMES:
        print(f"== {sec_code} {name}", file=sys.stderr)
        docs = search_yuho_docs(sec_code, limit=6)
        if not docs:
            results[sec_code] = {"name": name, "error": "no_docs"}
            continue
        per_fy = {}
        for doc_id, period_end in docs:
            fy_year = int(period_end[:4])  # period end year
            # FY label: if period end is March year YYYY, FY = YYYY (e.g. 2025-03-31 → FY25)
            # If December (e.g. Tri Chemical Jan-end), still tag by period_end year.
            path = ensure_extract(doc_id)
            if not path:
                continue
            tags = extract_tags(path)
            ppe_v, ppe_src = pick_value(tags, TARGET_TAGS["ppe"])
            cip_v, cip_src = pick_value(tags, TARGET_TAGS["cip"])
            adv_v, adv_src = pick_value(tags, TARGET_TAGS["advances"])
            ord_recv, ord_back = extract_order_book(path)
            per_fy[fy_year] = {
                "doc_id": doc_id,
                "period_end": period_end,
                "ppe_jpy": ppe_v,
                "ppe_src": ppe_src,
                "cip_jpy": cip_v,
                "cip_src": cip_src,
                "advances_jpy": adv_v,
                "advances_src": adv_src,
                "orders_received_mm": ord_recv,
                "order_backlog_mm": ord_back,
            }
            print(f"   FY{fy_year}: ppe={ppe_v} cip={cip_v} adv={adv_v} recv={ord_recv} back={ord_back}", file=sys.stderr)
        results[sec_code] = {"name": name, "by_year": per_fy}
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / "_data.json"
    out_path.write_text(json.dumps(results, indent=2, ensure_ascii=False))
    print(f"\nWrote {out_path}", file=sys.stderr)

if __name__ == "__main__":
    main()
