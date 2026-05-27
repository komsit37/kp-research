# Japan Semiconductor Supply Chain — Disclosed New-Build Facility Capex

**Date:** 2026-05-27  
**Theme:** HBF/NAND/HBM Japan supply chain  
**Scope:** 35 listed JP semi-supply-chain filers (deposition, etch, lithography, wafer, test/probe, substrate, advanced packaging, OEM parts + 15 broader semi names)  
**Source:** EDINET yuho XBRL — capex, PP&E, CIP, customer advances, 受注実績 order backlog, and 設備の新設、除却等の計画 planned-facility text blocks  
**Total pipeline disclosed:** ¥2,413B across 84 active plant line items

## Files in this entry

| File | Description |
|---|---|
| [`REPORT.md`](./REPORT.md) | Full analytical write-up — methodology, cluster-by-cluster MTP synthesis, addendum on order book + fixed-asset proxy, extension to 35 names, facility-locations analysis |
| [`facilities-map.html`](./facilities-map.html) | **Interactive map** — 84 plant line items plotted globally, bubble size = ¥M disclosed, color = process cluster. Aspect-aware presets (Japan+Korea / All Asia / Kumamoto / Gifu / World), sortable+filterable table, bidirectional map↔table hover sync, switchable bubble metric (¥ absolute / capex÷revenue / capex÷PP&E+CIP) |
| [`cluster-dashboard.html`](./cluster-dashboard.html) | Original cluster-level dashboard — per-name capex trajectories, cluster aggregates, capex/revenue bubble matrix |
| [`data/orderbook-data.json`](./data/orderbook-data.json) | Raw 6-year per-name series: PP&E, CIP, advances, 受注高, 受注残高 |
| [`data/orderbook-master.json`](./data/orderbook-master.json) | Cluster-organized YoY-delta table (original 20 names) |
| [`data/orderbook-extension.json`](./data/orderbook-extension.json) | Same for the 15 extension names |
| [`data/facilities-synthesis.md`](./data/facilities-synthesis.md) | Per-name consolidated tables of disclosed 設備の新設 plans + cross-reads |
| [`scripts/extract.py`](./scripts/extract.py) | XBRL extractor (PP&E / CIP / advances / order book) |
| [`scripts/facilities.py`](./scripts/facilities.py) | Planned-facilities text-block extractor |
| [`scripts/build_map.py`](./scripts/build_map.py) | Plotly map renderer |

## Headline findings

1. **Capex is forking by cluster.** Deposition (+29pp), Test & probe (+24pp), Substrate & plating chemistry (+16pp), Advanced packaging (+15pp) are accelerating; Wafer (+3pp), OEM parts (−4pp), Lithography (−10pp) are digesting. Forward MTPs are HBM/AI-server-explicit but **HBF-silent in all 20 plans**.

2. **Order-book confirms the fork.** Only HBM/substrate names show rising FY25 backlogs (Ibiden +109%, JEM +44%, Micronics +19%); every NAND-tool, power-semi, auto-semi name shows −9% to −37% YoY backlog declines.

3. **Six names disclosed NO new-build plans** — Lasertec, SUMCO, Advantest, TOWA, Ulvac, Uyemura. CIP / capex is going into equipment-into-existing-shells, not new construction.

4. **Six explicit hard physical-capacity numbers in the entire 35-name screen** — TEL Miyagi +250%, TEL Solutions Iwate +50%, Shinko Chikuma +50%, Shinko Arai BGA, Stella Sanpo ~2× filling, Kanto Denka Mizushima 新設・増強. Every other filer hides behind 算定が困難 boilerplate.

5. **Geographic clusters:** Gifu (Ibiden ¥298B alone), Miyagi/Iwate TEL belt (¥248B), Kumamoto TSMC-JASM gravity (¥73.7B across TEL Kyushu + JEM + JCU), Korea memory belt (¥81.8B), Nagano (Shinko ¥150B but delisted).

## How to use

- **Quick read:** [`REPORT.md`](./REPORT.md) — 8 sections including addendum (order book + fixed-asset proxy) + extension (15 extra names) + facility-locations.
- **Visual exploration:** open [`facilities-map.html`](./facilities-map.html) in a browser. Drag the divider to resize map vs table. Hover bubbles to highlight table rows. Toggle clusters via legend. Switch bubble metric via the size dropdown.
- **Reproduce data:** see [`scripts/`](./scripts/). Requires an EDINET XBRL corpus and the `edinet` CLI tool (see script headers).

## Caveats

- "Disclosed" capex covers what filers put in the yuho 設備の新設、除却等の計画 section. **Off-yuho announcements** (e.g. Renesas Kofu reopening, Advantest's Gunma site) are not captured.
- Aggregate-only disclosers (Shin-Etsu, Resonac, Mitsui Chem, Renesas, SBHPP, Tazmo) appear in the map at company HQ as placeholders marked "(agg)".
- Shinko Electric (6967) delisted mid-2024 post DNP/JIC consortium tender — historical comparable only.
- Kioxia (285A) has only one post-IPO yuho (Dec 2024 IPO); next filing (~Jun 2026) is the first full-year baseline.
