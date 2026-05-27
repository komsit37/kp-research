#!/usr/bin/env python3
# NOTE: these scripts depend on:
#  - a local MinIO/filesystem store of EDINET yuho XBRL documents at STORAGE_ROOT
#  - the `edinet` CLI (https://github.com/komsit37 - private)
# Adapt STORAGE_ROOT and OUT_DIR to your local setup before running.

"""Extract the 'PlannedAdditionsRetirementsEtcOfFacilities' text block from each
name's latest yuho. The output is a per-company HTML→text dump that captures
the standardized 設備の新設、除却等の計画 disclosure (plant name, location, purpose,
planned investment, start/completion dates).

Output: /tmp/hbf_capex_v2/orderbook/facilities/<sec>.txt + facilities/_index.json
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from html.parser import HTMLParser

STORAGE_ROOT = Path("/srv/bulk/apps/jp-stock-filings/storage/edinet/docs")
OUT_DIR = Path("/tmp/hbf_capex_v2/orderbook/facilities")

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
    ("4063", "Shin-Etsu Chemical"),
    ("4004", "Resonac"),
    ("7741", "Hoya"),
    ("7735", "SCREEN Holdings"),
    ("4186", "Tokyo Ohka Kogyo"),
    ("6315", "TOWA"),
    ("6728", "Ulvac"),
    ("4109", "Stella Chemifa"),
    ("6967", "Shinko Electric"),
    ("6383", "Daifuku"),
    ("285A", "Kioxia"),
    ("4183", "Mitsui Chemicals"),
    ("6963", "ROHM"),
    ("6723", "Renesas"),
    ("6266", "Tazmo"),
]

TARGET_TAGS = [
    "jpcrp_cor:PlannedAdditionsRetirementsEtcOfFacilitiesTextBlock",
    "jpcrp_cor:MajorFacilitiesTextBlock",
    "jpcrp_cor:OverviewOfCapitalExpendituresEtcTextBlock",
]

def get_latest_doc(sec_code):
    out = subprocess.run(
        ["edinet", "search", sec_code, "--doc-type", "120", "--limit", "1", "--format", "json"],
        capture_output=True, text=True, timeout=60,
    )
    if out.returncode != 0:
        return None
    data = json.loads(out.stdout)
    docs = data.get("documents", [])
    if not docs:
        return None
    return docs[0]["doc_id"], docs[0]["period_end"]

def ensure_extract(doc_id):
    p = STORAGE_ROOT / doc_id / "extract.html"
    if p.exists():
        return p
    subprocess.run(["edinet", "xbrl", "extract", doc_id], capture_output=True, text=True, timeout=180)
    return p if p.exists() else None

# Find an iXBRL text block: <ix:nonNumeric ... name="..." ...>...</ix:nonNumeric>
# Text blocks can be long and may contain nested tags. Use a non-greedy match.
def extract_text_block(html, tag_name):
    pattern = re.compile(
        r'<ix:nonNumeric\b[^>]*?name="' + re.escape(tag_name) + r'"[^>]*?>(.*?)</ix:nonNumeric>',
        re.DOTALL,
    )
    m = pattern.search(html)
    if not m:
        return None
    return m.group(1)

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.in_tr = False
        self.row_cells = []
        self.in_td = False
        self.cell_text = ""
    def handle_starttag(self, tag, attrs):
        if tag in ("br", "p", "div"):
            self.parts.append("\n")
        if tag == "tr":
            self.in_tr = True
            self.row_cells = []
        if tag in ("td", "th"):
            self.in_td = True
            self.cell_text = ""
    def handle_endtag(self, tag):
        if tag in ("p", "div"):
            self.parts.append("\n")
        if tag in ("td", "th"):
            self.in_td = False
            self.row_cells.append(self.cell_text.strip())
            self.cell_text = ""
        if tag == "tr":
            self.in_tr = False
            if self.row_cells:
                self.parts.append(" | ".join(c for c in self.row_cells if c) + "\n")
            self.row_cells = []
    def handle_data(self, data):
        if self.in_td:
            self.cell_text += data
        else:
            self.parts.append(data)
    def text(self):
        raw = "".join(self.parts)
        # collapse multiple blank lines
        out = re.sub(r'\n\s*\n+', '\n', raw)
        # collapse internal whitespace
        out = re.sub(r'[ \t　]+', ' ', out)
        return out.strip()

def to_text(html_fragment):
    if not html_fragment:
        return ""
    p = TextExtractor()
    try:
        p.feed(html_fragment)
        p.close()
    except Exception:
        return re.sub(r'<[^>]+>', ' ', html_fragment)
    return p.text()

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    index = {}
    for sec_code, name in NAMES:
        print(f"== {sec_code} {name}", file=sys.stderr)
        doc = get_latest_doc(sec_code)
        if not doc:
            print(f"   ! no doc", file=sys.stderr)
            continue
        doc_id, period_end = doc
        path = ensure_extract(doc_id)
        if not path:
            print(f"   ! no extract", file=sys.stderr)
            continue
        html = path.read_text(encoding="utf-8", errors="replace")
        blocks = {}
        for tag in TARGET_TAGS:
            block_html = extract_text_block(html, tag)
            if block_html:
                blocks[tag.split(":")[-1]] = to_text(block_html)
        if not blocks:
            print(f"   ! no target tags found", file=sys.stderr)
            continue
        # Write per-company file
        out_path = OUT_DIR / f"{sec_code}.txt"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"# {sec_code} {name}\n")
            f.write(f"# doc_id: {doc_id}  period_end: {period_end}\n\n")
            for key, text in blocks.items():
                f.write(f"## {key}\n\n")
                f.write(text)
                f.write("\n\n---\n\n")
        index[sec_code] = {
            "name": name,
            "doc_id": doc_id,
            "period_end": period_end,
            "blocks": list(blocks.keys()),
            "planned_chars": len(blocks.get("PlannedAdditionsRetirementsEtcOfFacilitiesTextBlock", "")),
        }
        print(f"   wrote {out_path} ({len(blocks)} blocks, {sum(len(v) for v in blocks.values())} chars total)", file=sys.stderr)
    with open(OUT_DIR / "_index.json", "w") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
