# Airbnb / STR comps near Shibuya 2-chome (for Canon Palace model)

**Captured:** 2026-05-29 via authenticated Airbnb search "Shibuya 2-chome".
**Purpose:** estimate short-term-rental (STR) upside for Canon Palace units (studios ~24–31 m², plus 901 = 77 m² 2LDK, plus 1F shop).
Raw comps in `airbnb_comps.csv`.

> ⚠️ **Pricing note:** Airbnb search totals are **per 5-night stay including cleaning + ~14% service fee**. `per_night_gross` = total ÷ 5 (slightly inflated by the one-time cleaning fee). **Net ADR to host ≈ 70–80% of the gross-per-night** after cleaning fee + Airbnb host fee are stripped out. Dates sampled were Jun–Jul 2026 (shoulder/early-summer; not peak).

## Room-size survey nearby (what exists on Airbnb in this micro-market)

| Size band | Examples found | Typical config |
|---|---|---|
| ~24–31 m² (studio/1R) | #802 (31 m²), "3min biz" units, Tokyo City Center 103/302/303 | studio, 1–3 guests, 1 bed |
| ~33–35 m² | #701 (35 m²), "Vibe Shibuya" 33 m², "10-min walk 33 m²", "[9 min] 33 m²" | 1BR, 3–6 guests, 3–4 beds (bunk/sofa) |
| ~44 m² | #204, #602 | 1BR, 3–4 beds |
| ~60 m² | "Near Shibuya 3BR house 60 m²" | 3BR house, 5 guests |
| ~77–90 m²+ | Sangenjaya 90 m², villas 232 m², 4–6BR homes | multi-bed homes |

**Key observation:** the **#701/#802/#204/#602 series are unit-numbered STR conversions inside apartment buildings** — i.e. exactly the play one would run at Canon Palace. They are the most direct comps. The #802 listing's "industrial-waste" garbage rule confirms it operates as a **registered minpaku (住宅宿泊事業)**, not a hotel.

## Per-night benchmarks (gross-per-night, Jun–Jul 2026)

| Unit type | Canon Palace analog | Gross/night range | Mid | Est. **net ADR** (×0.75) |
|---|---|---|---|---|
| Studio 24–31 m² | 201–602, 801, 1K units | ¥14,000–28,000 | ~¥22,000 | **~¥16,500** |
| 1BR / 33–44 m² | 203/303/403/503/603/803 (30 m²) | ¥21,000–43,000 | ~¥30,000 | **~¥22,500** |
| 2LDK ~60–77 m² | 901 (77 m²) | ¥28,000–32,000 | ~¥30,000 | **~¥23,000** |

(Outliers excluded: luxury penthouse ¥175k/nt, 4BR ¥101k/nt.)

## Occupancy rate estimation

Airbnb does **not** publish occupancy. Estimated two ways:

1. **Market benchmark (AirDNA-style, central Tokyo / Shibuya-Minato 2024–25):** well-managed, high-rating STRs run **~80–90% occupancy of *available* nights**, ADR ~¥18,000–25,000 for studios. The high review counts here (Ebisu 2101 = 86 reviews, "5min/4SD" = 178 reviews, "9min 2BR" = 68) corroborate heavy, consistent booking.
2. **Review-velocity proxy:** at ~0.4 reviews/stay and ~3–4 night avg stays, 30–80 reviews/yr implies the units are booked most available nights → consistent with 80%+ of-available occupancy.

### 🚨 The binding constraint is legal, not demand
Canon Palace is **zoned Residential**. Two legal STR paths in Japan:
- **民泊 / minpaku (住宅宿泊事業法):** allowed in residential zones **but hard-capped at 180 nights/year** (≈ **49% max annual occupancy**), plus Minato/Shibuya local by-laws often further restrict weekday operation.
- **旅館業 (hotel/simple-lodging license):** year-round, but generally **not permitted in residential zones** and requires building/fire compliance.

So model STR at Canon Palace under the **180-night cap** as the realistic base case (the year-round comps are likely in commercial zones or hotel-licensed). Verify the exact youtou-chiiki (用途地域) and any Minato/Shibuya minpaku ordinance before assuming more.

## STR revenue scenarios — per studio unit (illustrative)

Assume net ADR ¥18,000, and ~38% STR operating cost (cleaning, OTA fees, STR management 15–20%, utilities, supplies, linen):

| Scenario | Nights sold | Gross/yr | Net after 38% opex | vs current LTR* |
|---|---|---|---|---|
| **Minpaku cap (legal base)** | 180 × 90% = 162 | ¥2,916,000 | **¥1,808,000** | ≈ same as LTR net |
| Minpaku full 180 | 180 | ¥3,240,000 | **¥2,009,000** | +~12% |
| Year-round (if licensed) | 330 × 85% = 280 | ¥5,040,000 | **¥3,125,000** | +~75% |

*Current long-term rent for a studio ≈ ¥150,000/mo × 12 = ¥1,800,000/yr gross; LTR opex is far lower (~10–15%), so LTR net ≈ ¥1.55M. 

**Takeaway:** Under the realistic **180-night minpaku cap**, STR per-studio net is roughly **comparable to long-term rent** once STR operating costs are included — the legal cap erases most of the nightly-rate premium. STR only clearly wins if the building can obtain a **旅館業 hotel license** (zoning-dependent, likely not feasible as residential). For a whole-building income model, **long-term lease (the rent rolls in `rent_roll.csv`) is the sound base case**; treat STR as upside only with legal confirmation.

## Sources
- Airbnb search: Shibuya 2-chome, Shibuya City, Tokyo (Jun–Jul 2026 dates), 2 result pages captured.
- Representative listing inspected: airbnb.com/rooms/1394902032787456062 (#802, 31 m² studio).
