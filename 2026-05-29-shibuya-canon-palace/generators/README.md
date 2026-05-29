# Report generators

Python scripts that emit the dossier's HTML reports. Run from **anywhere** —
each script `chdir`s to the dossier root, so output lands beside `report.css`.

```bash
python3 generators/gen_comp.py        # -> airbnb_comp_report.html
python3 generators/gen_property.py    # -> property_report.html   (reads ../rent_roll.csv)
python3 generators/gen_yield.py       # -> airbnb_yield_model.html (constants inline)
python3 generators/gen_highseason.py  # -> airbnb_highseason_strategy.html
python3 generators/gen_handpick.py    # -> airbnb_adr_handpick.html
```

## Inputs
| Generator | Output | Data |
|---|---|---|
| gen_comp | airbnb_comp_report.html | `data/ab_merged.json` |
| gen_property | property_report.html | `../rent_roll.csv` |
| gen_yield | airbnb_yield_model.html | — (inline constants) |
| gen_highseason | airbnb_highseason_strategy.html | `data/hs_new.json` |
| gen_handpick | airbnb_adr_handpick.html | `data/hp2.json` |

## Styling
Each generator emits `<link rel="stylesheet" href="report.css">` plus a small
inline `<style>` of page-specific overrides (the `CSS` variable at the top of
each script). Shared chrome lives once in `../report.css` — edit that to
restyle everything. Do **not** paste a full `<style>` block back into a
generator; it would re-bloat and diverge from `report.css`.

## Hand-maintained (no generator)
- **index.html** — landing page; static content, edit directly.
- **airbnb_adr_analysis.html** — the consolidated ADR report was finalized by
  hand (its old `/tmp` generator diverged: stale numbers / 0.637 vs 0.849
  basis). Edit the HTML directly, or re-derive a generator before regenerating.

All scripts read/write UTF-8 explicitly. Don't run a `perl -pi` substitution
over them — perl's latin-1 default double-encodes the multibyte chars (¥ — ↗).
