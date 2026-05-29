# Shibuya Canon Palace — Whole-Building Airbnb Conversion Yield

Underwriting a Tokyo whole-building apartment (Shibuya Canon Palace, **¥1.93B**, [realestate.co.jp listing 1321745](https://realestate.co.jp/en/forsale/view/1321745)) as a buy-and-convert short-term-rental (Airbnb/minpaku) play, versus its long-term-rent base case.

**Open the dossier → [`index.html`](./index.html)**

## Bottom line

- Long-term rent nets **1.63%** (in-place) to **2.46%** (stabilized, full occupancy at today's rents).
- On a conservative ADR (studio ¥30k all-in/night, ×0.84 Airbnb fees), an Airbnb conversion lifts net yield to **3.46%** (flat) → **4.14%** (high-season) → **4.58%** (optimistic) — all within the **180-night minpaku cap (~50% occupancy)**.
- Pushing to 70% occupancy (5.8–6.4%) needs a 旅館業 hotel licence that residential zoning generally blocks.
- **Realistic legal STR range ≈ 3.5–4.6% net** — above long-term rent, but only after ¥31M conversion capex and far higher management effort. The binding constraint is legal (minpaku 180-night cap), not demand.

## Reports

**Main**
- [`property_report.html`](./property_report.html) — building details, regulatory data, full 23-unit rent roll (current + upside)
- [`airbnb_adr_handpick.html`](./airbnb_adr_handpick.html) — hand-picked comp set (8×1BR + 3×2BR, 5 seasons): base ADR + peak multipliers
- [`airbnb_yield_model.html`](./airbnb_yield_model.html) — conversion yield model: net yield by ADR pricing × occupancy, full P&L

**Appendix** (supporting / superseded)
- [`airbnb_comp_report.html`](./airbnb_comp_report.html) — 36 nearby STR listings (price, size, photo, link)
- [`airbnb_adr_analysis.html`](./airbnb_adr_analysis.html) — earlier broad-comp ADR study (superseded by the hand-picked set)
- [`airbnb_highseason_strategy.html`](./airbnb_highseason_strategy.html) — high-season-only minpaku play
- [`airbnb_analysis.md`](./airbnb_analysis.md) — methodology: room-size survey, occupancy estimation, the 180-night legal cap

## Data & scripts

- Source data: `rent_roll.csv`, `airbnb_comps.csv`, `property_details.md`
- `generators/` — Python scripts that emit the data-driven HTML reports; shared styling in `report.css`. See `generators/README.md`. `index.html` and `airbnb_adr_analysis.html` are hand-maintained.
- `images/` — rent-roll source sheets, 36 Airbnb comp photos/screenshots, 64 ADR comp thumbnails.

## Key caveats

- The hand-picked 1BR comps are 33–34 m² units sleeping 4–5 guests; Canon Palace's studios are 24–30 m² 1K (1–2 guests). The ADR assumption (¥30k) is deliberately set below the raw comps (¥38.5k) to reflect this — treat the comp ADR as an upper bound absent a capacity remodel.
- Model is unlevered / pre-tax and excludes a capex/FF&E reserve, income tax, and ramp/vacancy drag (see the yield model's "what's deliberately not in here").
- ADR is a live assumption; the model scales roughly linearly with it.
