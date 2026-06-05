# kp-research

Standalone ad-hoc research notes, dashboards, and data — primarily Japan equities and the Japan semiconductor supply chain, but topic-agnostic. Each entry is a self-contained dated subdirectory.

## Conventions

- One entry = one directory: `YYYY-MM-DD-{short-slug}/`
- Each entry contains its own `README.md` describing the work, plus the actual deliverables (HTML reports, markdown analysis, data files, scripts)
- Entries are independent; nothing in this repo cross-references or depends on other entries
- Data files live in `<entry>/data/`, scripts in `<entry>/scripts/`
- Visualizations are self-contained HTML files (Plotly via CDN, no build step needed)

## Index

| Date | Entry | Theme |
|---|---|---|
| 2026-05-27 | [JP Semiconductor Supply Chain — Disclosed New-Build Facility Capex](./2026-05-27-jp-semi-supply-chain-facilities/) | Japan semis: 35-name screen, ¥2,413B disclosed capex pipeline, facility geography, capacity-add normalization |
| 2026-05-29 | [Shibuya Canon Palace — Whole-Building Airbnb Conversion Yield](./2026-05-29-shibuya-canon-palace/) | Tokyo real estate: ¥1.93B whole-building, minpaku-capped STR conversion model, hand-picked ADR comps, ~3.5–4.6% legal net yield |
| 2026-06-05 | [JP Semicap — NAND Cycle, Packaging Roadmap & the Plating Chain](./2026-06-05-jp-nand-packaging-plating/) | Japan semis: two-vector NAND capex framework, 200→300-layer, hybrid bonding, ABF 2nd-order crunch + glass-core counter, and a JCU/Uyemura plating-chemistry deep-dive |

## Author

[komsit37](https://github.com/komsit37) — researching Japan equities, semis, and adjacent themes.
