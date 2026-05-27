---
title: "Japan HBF / NAND Supply Chain — Group Capex + MTP Deep-Dive"
date: "2026-05-26"
type: thematic-screen
theme: "hbf-nand-jp"
parent: "(parent screen — not published)"
candidates: 35
tags: [japan, thematic-screen, hbf, nand, hbm, capex, mtp, semicap]
summary: "Extends the 23-name HBF/NAND screen with 5–10y historical capex + Medium-Term Plan / FY25 earnings synthesis across 20 names organized into 9 process clusters. Headline: capex is forking — Deposition (+29pp), Test & probe (+24pp), Substrate & plating chemistry (+16pp, new cluster anchored by Ibiden ¥500B 3y plan), Advanced packaging (+15pp) are accelerating clusters; Wafer (+3pp), OEM parts (−4pp), Lithography (−10pp) are digesting. Forward MTPs are HBM/AI-server-explicit but HBF-silent in all 20 plans. **2026-05-27 addendum** adds PP&E + CIP + customer advances + 受注実績 order-book signals from yuho XBRL: Ibiden electronic backlog +109% YoY (biggest forward-demand surge), Lasertec promoted to Tier 1 on ¥64B locked advances + digested capex, Shibaura is a CIP +306% / advances −44% divergence trade, Enplas CIP +476% YoY surfaces a new watch. **Extension to 35 names** (Shin-Etsu, Resonac, Hoya, SCREEN, TOK + 10 broader semi) closes the obvious gaps: SCREEN customer advances ×10 over 5y (¥100B booked), TOK CIP +602% (EUV photoresist), Shin-Etsu ¥2T PP&E + ¥451B CIP (largest absolute footprint), Kioxia first-post-IPO baseline. Cross-cycle read: HBM/substrate is the *only* cluster with rising backlogs; NAND/power/auto all −13% to −37% YoY = non-AI semi in digestion."
visualizations: "./cluster-dashboard.html, ./facilities-map.html"
---

# Why this deep-dive

The 2026-05-24 screen tiered 23 Japanese filers by HBF/NAND specificity but stopped at one-fiscal-year snapshots. The user asked for: (a) **group historical + forward capex**, (b) **MTP projection synthesis**, (c) **cluster by process / domain**, (d) **visualization**. This is the answer for **20** of the 23 names — the full Tier A (12) plus the 5 Tier B picks that anchor the second-derivative debate, plus **3 substrate/plating-chemistry names** (Ibiden, JCU, C. Uyemura) added in a follow-up extension because the substrate buildup is the single largest absolute-yen capex pool in the screen and is HBM/AI-server explicit in management commentary.

**The single most important read of this exercise:** *no Japanese filer in the 17-name set names "HBF" in its current Medium-Term Plan.* Exposure is HBM-by-proxy: same hybrid-bonding tools, same probe-card moat, same advanced-packaging materials. If HBF lands as SanDisk + SK Hynix have implied, it lands through the HBM supply chain — and that chain is **already inflecting upward** on the capex line, ahead of any explicit HBF orderbook.

**Method:** capex/R&D history pulled via `edinet capex <secCode>` (5–10y per name); MTP and FY25 earnings commentary scraped from company IR + recent call transcripts via 4 parallel research agents (deposition/etch, test/probe, advanced packaging, wafer/litho/OEM-parts).

# Process-step cluster taxonomy

20 names, 9 process clusters covering the NAND fab flow from front-end to back-end:

| Cluster | Names (mcap-weighted anchor first) | Process role |
|---|---|---|
| **Deposition** (2) | KOKUSAI Electric (6525), Tri Chemical Labs (4369) | Batch ALD/CVD tools + Hf/Ti/Zr precursors for 200–300L NAND |
| **Etch & clean — tools** (2) | Tokyo Electron (8035), Shibaura Mech (6590) | Etcher + cleaner + coater/developer; aspirational hybrid-bonder |
| **Etch & clean — gases** (1) | Kanto Denka (4047) | NF3 / WF6 / F2 / CF4 / C4F6 specialty fluorine gases |
| **Lithography & mask** (1) | Lasertec (6920) | Actinic EUV mask inspection (sole supplier globally) |
| **Wafer & handling** (2) | SUMCO (3436), Mirial (4238) | 300mm silicon wafers + FOUP/FOSB carriers |
| **Test & probe** (5) | Advantest (6857), Nihon Micronics (6871), JEM (6855), TeraProbe (6627), Enplas (6961) | Memory testers, probe cards, IC sockets, outsourced wafer test |
| **Substrate & plating chemistry** (3) | Ibiden (4062), JCU (4975), C. Uyemura (4966) | ABF substrates + Cu via-fill / electroless plating chemistry for IC packages |
| **Advanced packaging** (3) | Disco (6146), Nitto Denko (6988), Sumitomo Bakelite (4203) | Dicing/grinding tools, dicing tapes, EMC encapsulants |
| **OEM chamber parts** (1) | Tocalo (3433) | Thermal-spray chamber coatings (TEL + AMAT customers) |

The **interactive dashboard** (sibling `./cluster-dashboard.html`) renders the per-name capex trajectories, cluster aggregates, and bubble matrix.

---

# Headline: capex is forking by cluster

Cluster-level capex/revenue ratio over the last 5 fiscal years (FY2021–FY2025/26, depending on fiscal-year end). **Trend (pp)** = FY25 reading minus the first reading in the same 5y window — i.e. how much the cluster's capex intensity has *changed* over the window.

| Rank | Cluster | n | 5y avg capex/rev | FY25 capex/rev | 5y trend (pp) | 5y cumulative capex (¥B) | Read |
|---|---|---:|---:|---:|---:|---:|---|
| 1 | **Deposition** | 2 | 24.2% | 42.3% | **+29.3** | 56 | Scale-up: Tri Chemical doubled (30%→70%); KOKUSAI flat ahead of FY28 recovery |
| 2 | **Test & probe** | 5 | 27.1% | 41.4% | **+24.2** | 252 | HBM probe + memory-test megaramp; Micronics + TeraProbe + JEM all building |
| 3 | **Substrate & plating chemistry** | 3 | 17.2% | 27.6% | **+16.3** | 597 | Ibiden ¥500B FY26-28 board-approved; JCU FY25 capex 30% (Kumamoto build); Uyemura conservative plan already eclipsed |
| 4 | **Advanced packaging** | 3 | 16.7% | 25.7% | **+14.7** | 587 | Disco capex doubled YoY (Gohara plant); SBHPP HBM materials build |
| 5 | **Etch & clean (gases)** | 1 | 25.1% | 27.2% | **+8.9** | 65 | Kanto Denka flat-high; Xuancheng China comes on FY27 |
| 6 | **Etch & clean (tools)** | 2 | 7.8% | 13.1% | **+8.2** | 487 | TEL slow ramp toward ¥3T plan; Shibaura HB hopeful |
| 7 | **Wafer & handling** | 2 | 42.0% | 20.4% | **+3.0** | 825 | SUMCO Yoshinogawa **pushed out**; Mirial −8.7% rev FY25 |
| 8 | **OEM chamber parts** | 1 | 13.5% | 12.8% | **−3.8** | 23 | Tocalo MTP hit 1y early — record FY26, new plan May 11 |
| 9 | **Lithography & mask** | 1 | 21.4% | 7.2% | **−10.3** | 32 | Lasertec capex digestion post FY23 ¥21B spike; FY26 guide raised |

**Two-thesis read:**

1. **HBM/AI-logic-pull cluster is in build mode** (deposition + test + packaging + OEM parts inflecting up on disclosure). The capex going in now is HBM-named in management commentary, but the physical infrastructure — thin-wafer grinding, ALD precursors, hybrid-bond evaluation, probe cards for stacked die — is **HBF-fungible**. If SanDisk/SK ramps HBF in 2027–2028, these are the assets that get reused.

2. **Bulk-NAND cluster is digesting** (wafer + Lasertec mask inspection both showing capex push-out language). SUMCO's president openly told Q1 FY26 callers that Yoshinogawa is on hold. KOKUSAI's CEO flagged a "temporary slowdown" in NAND tool investment with FY3/2028 recovery. **This is the air-pocket window** — and also why some Tier A names trade as deep-cyclicals.

The dashboard's cluster-trend bar chart is the cleanest single picture of this.

---

# Per-cluster detail

## Cluster 1 — Deposition (+29pp, the loudest signal)

| Ticker | Name | FY25 capex (¥B) | FY25 capex/rev | 5y avg | 5y trend (pp) | MTP target |
|---|---|---:|---:|---:|---:|---|
| 6525 | KOKUSAI Electric | 20.3 | 14.2% | 17.4% | 0.0 | Long-range "over ¥330B" (no fixed end); FY3/2027 guide ¥280B |
| 4369 | Tri Chemical Labs | 8.2 | 70.5% | 30.9% | **+58.6** | **FY1/2028 ¥31.5B / OP ¥8.62B** (2x rev / 3x OP vs FY1/2025) |

**The Tri Chemical scale-up is the single most aggressive capex commitment in the screen.** 70% capex/revenue in FY1/2026 while the company also commits to a FY1/2028 doubling — a ¥15B cumulative 5y capex spend on a ¥11B revenue base. The Minami-Alps plant (etch materials extension, not just precursors) + Taiwan subsidiary plant are the visible commitments. The MTP frames "FY1/2028 vs FY1/2025: revenue 2x, op profit 3x" — i.e. ~67% revenue growth over 3 years with ~25% op margin. CXMT 10.8% customer disclosure remains the unique read-through into China-memory.

**KOKUSAI's flat line tells the other half of the story:** management explicitly flagged a "**temporary slowdown in NAND tool investment**" in FY3/2026 with FY3/2028 recovery. The long-range ¥330B framework + ASMPT hybrid-bonding partnership keeps the optionality alive but FY27 guidance ¥280B (+19.1%) is the near-term anchor. Mgmt: "200–300-layer generations expected to account for **80%+ of NAND-related equipment sales**" — i.e. the entire NAND tool budget tilts toward KEC's batch ALD strength once the cycle resumes.

## Cluster 2 — Test & probe (+24pp, the broadest beat)

| Ticker | Name | FY25 capex (¥B) | FY25 capex/rev | 5y avg | 5y trend (pp) | MTP target |
|---|---|---:|---:|---:|---:|---|
| 6857 | Advantest | 21.0 | 7.7% | 9.0% | −1.8 | FY27 3y-avg ¥835–930B (raised from 560–700); FY26 alone ¥950B |
| 6871 | Nihon Micronics | 15.3 | 38.1% | 25.1% | **+26.7** | **FY26/12 ¥80B** (raised by ¥15B); cum capex **¥56.3B FY23–26** |
| 6855 | JEM | 4.0 | 21.7% | 11.4% | **+14.4** | FY27/3 ord profit ¥5B; Amagasaki greenfield Aug 2028 completion |
| 6627 | TeraProbe | 30.6 | **117.8%** | 78.9% | **+67.3** | No MTP; FY26 OP raised to ¥10.22B (+71.5% YoY) |
| 6961 | Enplas | 6.4 | 21.7% | 11.0% | **+14.4** | FY26–FY28 cum capex **¥29.5B** + ¥2.5B SH returns |

**TeraProbe is the capex-intensity outlier** at 117% — they are spending more on physical test capacity than they generate in revenue. The Q1 FY26 upward revision (OP +71.5% YoY) and "server + AI-related demand" commentary suggests this is **front-running** the test-capacity inflection. The May 2025 *downward* revision in the same line — when memory was weaker — is the cyclicality warning.

**Micronics' FV26 plan is the cleanest of the cluster**: explicit ¥80B sales target, ¥56.3B cumulative capex (the most aggressive ratio at 70% capex/end-yr-sales), Aomori new building operational since Dec 2024, Korean MEK facility for HBM/DRAM probe-card capacity. The plan **explicitly flags NAND as underperforming with declining share** — Micronics is a pure-play *HBM-DRAM* probe-card name, not a NAND probe-card name. That's a useful disambiguation for the HBF thesis: Micronics doesn't *currently* benefit from HBF unless probe-card families port across.

**JEM's Amagasaki greenfield (Feb 2026 announce, Aug 2028 completion)** spills past the FY24–FY26 MTP — a multi-year demand bet. But the plan discloses *no yen sales target*, only ord-profit margin ≥10% and ROE ≥10%, which is a disclosure handicap relative to Micronics.

**HBF is not named in any of the 5 test/probe MTPs.** Advantest has the platform to extend its HBM tester families if HBF arrives; the probe-card names (Micronics, JEM) would need new probe families (stacked-die contact configurations differ from current HBM stacks).

## Cluster 3 — Substrate & plating chemistry (+16pp, the AI-server substrate buildup)

| Ticker | Name | FY25 capex (¥B) | FY25 capex/rev | 5y avg | 5y trend (pp) | MTP target |
|---|---|---:|---:|---:|---:|---|
| 4062 | Ibiden | **157.3** | 48.6% | 38.7% | **+18.8** | **MNS115 FY23–FY27**; FY27 OP raised to ¥150B (+67%); **¥500B capex FY26–FY28 board-approved**; FY30 ≥¥1T rev / ¥300B OP |
| 4975 | JCU | 6.4 | **30.0%** | 8.3% | **+28.1** | **JCU VISION 2035 1st stage** FY3/25–FY3/27; FY27 ¥31B sales; ¥11.4B Kumamoto facility (Dec 2025 complete, May 2026 trial production) |
| 4966 | C. Uyemura | 2.3 | 4.1% | 4.6% | **+1.8** | FY3/25–FY3/27; FY27 ¥89.1B sales / ¥14.5B OP **already exceeded in FY25 (OP ¥18.83B)**; ¥20B 3y growth capex |

**Ibiden is the single largest absolute-yen capex commitment in the screen.** The Feb 2026 board approval of **¥500B over FY2026–FY2028** for high-performance IC package substrates is a 3-year-forward commitment of ~¥100B/yr capex — phased into Gama Plant Cell6 (¥220B, Ogaki) and Ono Plant (¥280B, Ibi-gun). The customer pull is explicit: "AI Servers and High-performance Servers," with customers seeking commitments through CY2029. The technical roadmap — die size 3.5 reticle → 9+ reticle, substrate body 80×80mm → 130×130mm+, SAP layers 9-X-9 → 14-X-14 — is what HBM4 and HBF stacks both need on the package side. **Mgmt explicitly says "the binding constraint is headcount and engineering talent, not capital"** — i.e. orderbook is not the issue, manufacturing scale-up is.

**The FY25 results (May 11 2026) flagged one watch-item**: customer advance payments declined from ¥92.1B → ¥81.0B. Ibiden frames this as "customers converting to volume" but the bear-case read is orderbook normalization. FY26 ASP/mix is +¥20.5B vs volume only +¥1.5B — i.e. the FY26 uplift is **price-mix, not unit growth, until late-FY26**. Watch volume re-acceleration as the read on whether the ¥500B capex is being timed correctly.

**JCU is the small-cap pure-play that just stepped up 10× in one year.** FY3/2024 capex was 3.4% of revenue (¥0.8B); FY3/2025 jumped to 30.0% (¥6.4B) — the Kumamoto Facility build going through the P&L. The plant total is **¥11.4B**, adjacent to TSMC JASM gigafabs in Mashiki, Kumamoto Prefecture; trial production starts May 2026. JCU's wedge is **Cu via-filling plating chemistry** for HDI and advanced semiconductor packaging — a near-monopolistic chemistry niche where ASP scales with via density (more layers = more via-fill volume per substrate). The "JCU VISION 2035" frames a 10-year doubling: ¥31B by FY27 → ¥50B by FY35. **The May 2026 FY3/26 print is the first results window where Kumamoto contribution starts showing up** — the AI-mix call-out at that print is the catalyst.

**C. Uyemura is the conservative-plan, reality-breakthrough name.** The FY3/2025–FY3/2027 MTP set FY27 targets at ¥89.1B sales / ¥14.5B OP — *down* from FY24 actual ¥15.8B OP. Reality blew through in year one: FY3/2025 actual sales ¥83.85B (+4.5% YoY), **OP ¥18.83B (+25.6% YoY) — already past the FY27 OP target.** Yet management's FY3/2026 pre-announcement guidance is **sales −1.4%, OP −20.3%** citing US tariff/tax-policy uncertainty. The share price hit an all-time high (¥24,650 on Apr 15 2026), suggesting the market is pricing through the conservative guide. **May 13 2026 FY3/26 print = guidance-beat setup if the conservatism proves overdone.**

Uyemura's product positioning is the strongest among the chemistry names: dominant **electroless Ni/Au and electroless Cu chemistry** into the ABF substrate chain (Ibiden, Unimicron, ASE, Nan Ya PCB) plus high-end PKG/BGA/FC-CSP plating. The MTP names PLP (panel-level packaging), RDL, interposer, Bump as growth wedges — directly the HBM/HBF interposer and substrate buildup workflow.

**Cluster HBF read-through**: zero of the three plans names HBF. All three explicitly name AI-server substrates / advanced-packaging chemistry. If HBF stacks adopt similar substrate-bumping-RDL workflow as HBM4 (likely from a packaging-physics standpoint), all three benefit by demand pull-through — without needing new product development.

## Cluster 4 — Advanced packaging (+15pp, the megacap accelerator)

| Ticker | Name | FY25 capex (¥B) | FY25 capex/rev | 5y avg | 5y trend (pp) | MTP target |
|---|---|---:|---:|---:|---:|---|
| 6146 | Disco | **135.8** | 38.2% | 20.8% | **+21.5** | **No formal MTP** by policy; Gohara plant ¥40B+, ~14× cap by 2035 |
| 4203 | Sumitomo Bakelite | 17.6 | 19.6% | 15.6% | **+14.0** | **FY26 ¥340B**; Suzhou EMC 1.3× cap; FY25 NP +32% |
| 6988 | Nitto Denko | 93.0 | 19.3% | 13.8% | **+8.7** | "Nitto for Everyone 2025" final yr; ¥300B cum 3y capex on plan; **next MTP unveil May 2026** |

**Disco's FY2025 capex doubled YoY (¥69B → ¥135.8B)** for the Gohara Plant in Kure — a phased build targeting ~14× output capacity for precision processing tools by ~2035, ≥¥40B initial. This is the **single biggest capex commitment in the screen by absolute yen**. Management refuses to issue a formal MTP "because of cycle volatility" — instead investors model bookings + Gohara phasing. The HBM/HBF read-through is direct: wafer thinning is mandatory for stacking, and Disco owns ~70% global share. Thinning TAM grows from $582m (2025) → $845m (2030) per third-party analysis.

**Sumitomo Bakelite is the over-deliverer**: FY25 actual ¥316.5B beat the original ¥310B guide; net profit +32% YoY on AI/power-semi encapsulant pull. The FY26 ¥340B MTP target — final year of the FY24-26 plan — is achievable with ~7.4% growth. Suzhou EMC plant complete Jan 2025 (1.3× capacity); Taiwan + Singapore expansions complete 2024 specifically for HBM packaging materials. Sumikon EME (epoxy molding compound) is the SKU. **HBM-named capacity build is the most explicit in this cluster.**

**Nitto Denko is the disclosure-light name**: dicing tape + die-attach film + thermal-release sheet supplier with ~¥300B cumulative MTP capex on plan, but **no explicit hybrid-bonding underfill SKU** — that role is led by Resonac and Showa Denko in the HBM stack. Nitto's exposure runs through tape + thin-wafer handling. The **next MTP unveil expected at FY26 results (May 2026)** is the key catalyst: watch for a semi-segment carve-out and any explicit HB line.

## Cluster 5 — Etch & clean (mixed: +9pp gases, +8pp tools)

| Ticker | Name | FY25 capex (¥B) | FY25 capex/rev | 5y avg | 5y trend (pp) | MTP target |
|---|---|---:|---:|---:|---:|---|
| 4047 | Kanto Denka | 14.1 | 27.2% | 25.1% | **+8.9** | **MTP ends FY3/2026** with ¥100B / ¥15B OP target (below pace); FY27 capex <¥10B/yr |
| 8035 | Tokyo Electron | 162.1 | 11.6% | 8.0% | **+4.9** | **¥3T+ rev / 35%+ OPM**; FY3/27 H1 ¥1.57T guide; advanced packaging +60% by 2027 |
| 6590 | Shibaura Mech | 6.5 | 14.5% | 7.7% | **+11.6** | FY3/24–FY3/26 plan ends; HB tools deferred 1–2yr+; flip-chip is run-rate |

**Kanto Denka's MTP is at its terminal year** (FY3/2026 just closed). The ¥100B / ¥15B OP target did not fully clear due to NF3 + battery-materials weakness; capex elevates to ¥11.9B in the final year and management has telegraphed **<¥10B/yr post-FY27** — i.e. capacity is in place for the ¥100B run-rate. The most interesting forward catalyst: **Mitsui Chemicals announced its March 2026 NF3 exit**, and Kanto's CEO sees customer multi-source BCP driving NF3 demand recovery. The Xuancheng (China) plant comes online FY3/2027 producing CF4/C4F6/WF6 — i.e. China-memory etch-gas optionality.

**TEL's ¥3T MTP is the megacap HBM play in this cluster**: 2027 segment outlook frames "coater/developer +50%+, etch +30%, **advanced packaging +60%+**" driven by "EUV, GAA, **HBM, heterogeneous integration**." The May 2026 Q4 call cited "**NAND investment +42.5% in 2025**" + DRAM/HBM expansion — a more bullish read than KOKUSAI on the NAND cycle, possibly because TEL's etcher franchise has broader logic+memory exposure. R&D commitment ≥¥1.5T cumulative is the emphasized investment vector.

**Shibaura is the asymmetric-payoff name**: third-party reads (Lumen Alpha, SemiAnalysis) confirm Shibaura is **NOT shipping hybrid-bonding tools to TSMC in CY25**; mass shipments not within 1–2 years. BESI dominates, Shibaura at best second-source. Current revenue from TFC-6600 *flip-chip* bonders (Blackwell/Rubin CoWoS-L + Apple WMCM ~140–160 units, ¥200M ASP, 4–5yr). At fwd P/E 7.1 (the cheapest in the screen) the question is whether the HB optionality is being given away free.

## Cluster 6 — Wafer & wafer-handling (+3pp, the digestion cluster)

| Ticker | Name | FY25 capex (¥B) | FY25 capex/rev | 5y avg | 5y trend (pp) | MTP / status |
|---|---|---:|---:|---:|---:|---|
| 3436 | SUMCO | 80.0 | 23.8% | 54.0% | **−2.9** | **Yoshinogawa pushed out**; FY25 capex ¥79.9B (−¥135B YoY); Q1 FY26 acceptance just ¥9.4B |
| 4238 | Mirial | 1.0 | 17.0% | 30.0% | **+8.8** | **MTP "中期成長戦略 2028" ¥23.9B by Jan 2029** (~13% CAGR); FY25 rev −8.7% YoY |

**SUMCO is the most explicit push-out in the entire 17-name set.** President Ryuta on the Q1 FY26 call: "**the facilities in place at this [Imari] location represent sufficient room for capacity expansion for the time being… only once this site is fully populated would we then potentially revisit Yoshinogari after rigorously studying the then current market conditions.**" The original 2021 ¥228.7B program is paused at the back end. FY25 capex came down by ¥135B YoY. **This is the supply-side anchor that says NAND bit-growth capex is digesting.** Counterweighting: "uptick in NAND projected ahead" + HBM-related leading-edge wafer demand strong.

**Mirial is the microcap echo of SUMCO**: FY25 revenue −8.7% YoY, OP −55.4% — wafer-carrier orders track SUMCO/Shin-Etsu/Samsung capex digestion. The FY29 ¥23.9B target (13% CAGR) requires the wafer-fab capex cycle to re-accelerate. Read this name as a high-beta SUMCO derivative; **only sleeve-sized at ¥12B mcap**.

## Cluster 7 — Lithography & mask (−10pp, but raised guide)

| Ticker | Name | FY25 capex (¥B) | FY25 capex/rev | 5y avg | 5y trend (pp) | MTP target |
|---|---|---:|---:|---:|---:|---|
| 6920 | Lasertec | 5.0 | 7.2% | 21.4% | **−10.3** | **¥400–500B by FY06/2030** (35%+ OPM); FY06/26 guide raised to ¥220B / OP ¥100B |

Lasertec is the cluster's only constituent and capex is digesting after an FY23 ¥21B spike. **But operating performance just accelerated**: Q2 FY06/26 sales ¥74.1B vs ¥57.3B guide, FY06/26 guidance *raised* to ¥220B revenue / ¥100B OP / ¥72B NP / ¥132 div. The Oct 2025 ACTIS A200HiT launch (next-gen actinic patterned mask inspection) lands ahead of Samsung's V-NAND EUV ramp. **The H1 mask-blank weakness was tied directly to Samsung NAND/foundry capex revisions** — i.e. Lasertec's order book is *currently* taking the NAND push-out the wafer cluster talks about. Long-dated to the FY30 ¥400–500B target.

## Cluster 8 — OEM chamber parts (−4pp, but record FY26)

| Ticker | Name | FY25 capex (¥B) | FY25 capex/rev | 5y avg | 5y trend (pp) | MTP target |
|---|---|---:|---:|---:|---:|---|
| 3433 | Tocalo | 5.0 | 12.8% | 13.5% | **−3.8** | **FY21–25 MTP hit 1y early**; FY26 record ¥57B / OP ¥13B; 2030 vision ¥80B |

Tocalo's FY21–25 MTP hit targets one year early and FY26 guidance (¥57B revenue / ¥13B ord profit / 22.8% OPM) sets a new record. FY26 capex plan ¥9.0B includes **new Vietnam plant + Chandler AZ facility** (co-locating with AMAT, announced Apr 2026). Japanese government secured ¥3.7B Growth Investment Subsidy for ¥11.1B strategic capex. **The May 11 2026 earnings + new MTP unveil is the next catalyst** for the screen — Tocalo's plan will be a near-real-time read of TEL/AMAT-chamber demand.

---

# Forward picks — refined by MTP + capex signal

These supersede the 2026-05-24 screen's preliminary 5-name list because we now have MTP-grade visibility. Picks are still **research-shortlist**, not stock-picking calls.

**Tier 1 — strongest MTP discipline + cleanest HBF read-through:**

1. **4062 Ibiden** — **single biggest absolute-yen capex commitment in the screen**: ¥500B board-approved FY26–FY28 (Gama ¥220B + Ono ¥280B); FY27 OP target raised to ¥150B (+67%); FY30 vision ≥¥1T rev / ¥300B OP. AI-server substrate king; customers seeking commitments through CY2029. Mgmt: "binding constraint is headcount, not capital." **Watch: customer advance payments trajectory (declined ¥92B→¥81B) — convert-to-volume signal vs orderbook normalization.**
2. **6146 Disco** — capex doubled YoY into Gohara; HBM/HBF universal enabler (~70% share dicing/grinding); no MTP but bookings-driven model. Single biggest *Plant-scale* capex commitment among the tooling names. **Watch: FY27/3 results for Gohara phase-1 ¥ disclosure.**
3. **4369 Tri Chemical Labs** — only ALD-precursor name with **explicit 2x rev / 3x OP MTP** through FY1/2028; 70% capex/rev in FY1/2026; CXMT-named customer + Minami-Alps etch-materials extension. The clearest small-cap scale-up. **Watch: Taiwan plant commissioning + Minami-Alps revenue contribution.**
4. **4203 Sumitomo Bakelite** — final-year MTP over-delivery (¥316.5B vs ¥310B); HBM-named capacity build (Suzhou + Taiwan + Singapore); FY26 ¥340B target = re-rating fuel. **Watch: FY26 results to confirm ¥340B landing.**
5. **6871 Nihon Micronics** — FV26 ¥80B target raised; HBM = 92% of Q2 probe revenue; Korea-skewed memory (Samsung/SK). **Mind: NAND probe-card flagged as underperforming — this is a pure HBM-DRAM play, not HBF.**

**Tier 2 — asymmetric / optionality / catalyst-driven:**

6. **4966 C. Uyemura** — already broke through FY27 OP target in FY25 (¥18.8B actual vs ¥14.5B plan); FY3/26 guidance −20% OP looks materially conservative against ATH share price ¥24,650 (Apr 15 2026); dominant electroless Ni/Au + Cu chemistry into ABF + PLP/RDL/Bump line. **Watch: May 13 2026 FY3/26 print = guidance-beat setup.**
7. **4975 JCU** — small-cap pure-play with FY25 capex stepped up 10× (3.4%→30% of rev) on ¥11.4B Kumamoto facility build adjacent TSMC JASM; Cu via-fill chemistry near-monopoly. **Watch: May 2026 FY3/26 print = first AI-mix call-out post-Kumamoto trial-production start.**
8. **3433 Tocalo** — MTP hit 1y early; **May 11 2026 new-MTP unveil** is the catalyst; Chandler AZ + Vietnam = co-location with AMAT. Best quality-vs-price in the OEM-parts tier.
9. **6920 Lasertec** — raised FY06/26 guide despite NAND/Samsung mask-blank weakness; ACTIS A200HiT new product; long-dated ¥400–500B FY30 target with 35%+ OPM. **Caveat: NAND push-out is a current headwind, not a tailwind, until Samsung V-NAND re-accelerates.**
10. **6590 Shibaura Mech** — fwd P/E 7.1 with HB optionality. Third-party reads say HB tool shipments deferred 1–2yr+ at TSMC; flip-chip is the run-rate. **Use as a deep-value optionality slot, not a primary HBF expression.**

**Tier 3 — cyclical / wait-for-MTP / disclosure-handicapped:**

- **6525 KOKUSAI Electric** — anchor NAND-deposition pick but **FY3/26 slowdown** flagged by mgmt with FY3/28 recovery. Wait for the air-pocket to clear.
- **4047 Kanto Denka** — MTP ends FY3/26 with ¥100B target below pace; next plan is the read. NF3 demand recovery on Mitsui exit is the FY27 tailwind.
- **6627 TeraProbe** — 117% capex/rev + 71.5% OP growth FY26, but no MTP, sharp cyclicality (May 2025 downward revision). Trade carefully.
- **3436 SUMCO** — Yoshinogawa pushed out; trough earnings; wait for capex re-acceleration before re-entering.

---

# Addendum (2026-05-27) — Order book + fixed-asset proxy

The capex/MTP narrative above is what management *promises*. This addendum is what the **balance sheet** and **order book** actually show: how much of the promised capacity is already on the BS (PP&E), how much is still in-flight (CIP — construction in progress), and how much forward demand is locked in (受注残高 order backlog + customer advances / contract liabilities).

**Method:** PP&E (`jppfs_cor:PropertyPlantAndEquipment`), CIP (`jppfs_cor:ConstructionInProgress`), customer advances / contract liabilities (`jppfs_cor:AdvancesReceived` / `ContractLiabilities`) pulled from yuho XBRL across FY20–FY25 for the 20 names; 受注実績 (orders received + backlog) parsed from the yuho 受注実績 table where disclosed (8 of 20). All values normalized to ¥B.

## A. Fixed-asset proxy — what's actually built vs. in-flight

Total PP&E + CIP captures **cumulative capex minus disposals + depreciation** — i.e. the sticky physical-asset footprint. **CIP / (PP&E+CIP) ratio** is the share of fixed assets still in-flight (capex committed but not yet in service). High CIP ratio = capacity coming online soon.

| Cluster | Sec | Name | PP&E FY25 (¥B) | CIP FY25 (¥B) | CIP / FA | CIP YoY | 5y FA growth (FY20→FY25) |
|---|---|---|---:|---:|---:|---:|---:|
| Deposition | 6525 | KOKUSAI Electric | 46.9 | 2.2 | 4.5% | **−85%** | n/a (2y data) |
| Deposition | 4369 | Tri Chemical Labs | 17.2 | 1.0 | 5.4% | −63% | **+111%** |
| Etch tools | 8035 | Tokyo Electron | 441.7 | **137.0** | 23.7% | **+57%** | +182% |
| Etch tools | 6590 | Shibaura Mech | 17.7 | 5.0 | 21.9% | **+306%** | +88% |
| Etch gases | 4047 | Kanto Denka | 55.2 | 17.2 | 23.8% | **+72%** | +124% |
| Litho | 6920 | Lasertec | 30.3 | **0.1** | 0.2% | **−94%** | +282% |
| Wafer | 3436 | SUMCO | 663.4 | 123.4 | 15.7% | **−67%** | +235% |
| Wafer | 4238 | Mirial | 15.6 | 0.2 | 1.3% | −74% | +153% |
| Test | 6857 | Advantest | 78.6 | 5.7 | 6.8% | −38% | +134% |
| Test | 6871 | Nihon Micronics | 38.7 | 4.4 | 10.1% | +55% | **+346%** |
| Test | 6855 | JEM | 10.6 | 0.4 | 4.0% | −59% | +60% |
| Test | 6627 | TeraProbe | 69.1 | 1.8 | 2.6% | −37% | +83% |
| Test | 6961 | Enplas | 21.5 | 5.2 | 19.4% | **+476%** | +87% |
| Substrate | 4062 | Ibiden | 460.1 | **202.0** | **30.5%** | −14% | **+198%** |
| Substrate | 4975 | JCU | 11.8 | 5.6 | **32.2%** | **+1932%** | +181% |
| Substrate | 4966 | C. Uyemura | 24.6 | 0.3 | 1.2% | +93% | +32% |
| Adv. packaging | 6146 | Disco | 204.0 | 16.9 | 7.7% | +19% | +92% |
| Adv. packaging | 4203 | Sumitomo Bakelite | 123.0 | 12.0 | 8.9% | −40% | +42% |
| Adv. packaging | 6988 | Nitto Denko | 417.6 | 46.7 | 10.1% | +26% | +67% |
| OEM parts | 3433 | Tocalo | 37.4 | 5.4 | 12.5% | +28% | +56% |

**Three reads:**

1. **Highest forward-load (CIP / FA + CIP YoY positive)** — **JCU (32%, +1932%)** is the cleanest "build in progress" — Kumamoto facility going through CIP and not yet productive; **Ibiden (30%, −14%)** has the biggest absolute CIP balance (¥202B) but already starting to transfer to PP&E (PP&E +13% YoY, ¥51B added); **TEL (24%, +57%)** is the next ¥137B wave of advanced-packaging + etch capacity; **Kanto Denka (24%, +72%)** = Xuancheng China NF3 in build; **Shibaura (22%, +306%)** flags below — speculative HB build.

2. **Already-digested capacity (low CIP, big PP&E)** — **Lasertec** (CIP just ¥0.1B, −94% YoY) — fully done, all FY30 ¥400–500B target capacity is in PP&E now; **KOKUSAI** (CIP −85% YoY) — capacity already on B/S ahead of the NAND digestion air-pocket; **SUMCO** (CIP −67% YoY, ¥123B → ¥123B) — Yoshinogawa pause shows up directly in the CIP roll-off; **Sumitomo Bakelite** (CIP −40% YoY) — Suzhou EMC + Taiwan + Singapore plants moved to PP&E.

3. **Capex-to-PP&E translation efficiency** — Disco's 5y cumulative capex is ¥149B (sum of `_timeseries.json`); PP&E grew ¥111B (FY20 ¥93B → FY25 ¥204B); ratio ~75% — high, consistent with low disposal/depreciation given the recent build. Ibiden's 5y cumulative capex is ~¥740B; FA grew ¥440B; ratio ~60%. **The capex is showing up as real capacity, not maintenance.**

## B. Surprises the existing report under-states

Three signals the capex/MTP write-up didn't fully surface:

- **Shibaura Mech CIP +306% YoY (¥1.2B → ¥5.0B)** — management *is* building HB-tool capacity at the BS level even as third-party reads (Lumen Alpha) say TSMC mass-shipment is "deferred 1–2 years." This is a 4× scale-up in physical capacity-in-flight. **But customer advances dropped −44% (¥8.4B → ¥4.7B)** — customers are *not* pre-paying for this capacity yet. Read: speculative build by Shibaura, not order-funded. Asymmetric, but Shibaura is taking the risk on its own balance sheet.

- **Enplas CIP +476% YoY (¥0.9B → ¥5.2B, ratio 19%)** — IC-socket capacity build that the FY26–FY28 ¥29.5B cumulative-capex plan implied is now showing up. Coupled with the FY25 capex hitting 21.7% of revenue, Enplas is positioning for a meaningful production-capacity step-up. Not on the Tier 1 list in the original report — promote to "watch" given the BS-level confirmation.

- **JCU CIP +1932% YoY (¥0.3B → ¥5.6B, ratio 32%)** — the BS confirms what mgmt said about Kumamoto. The ¥5.6B in CIP is roughly half the announced ¥11.4B plant total, consistent with Dec 2025 completion + May 2026 trial production. The next yuho (FY3/26, expected May 2026) will show the second half flow into CIP or transfer to PP&E. **First post-Kumamoto print is the critical observation window** for JCU's small-cap pure-play thesis.

## C. Order book — explicit 受注実績 disclosure (8 of 20 names)

Order backlog (受注残高) and orders received (受注高) are disclosed in the yuho 受注実績 table for B2B equipment / specialty-chemicals makers with project-based revenue. FY25 (or latest) values + YoY direction:

| Sec | Name | FY25 receipts (¥B) | YoY | FY25 backlog (¥B) | YoY | Book-to-bill (B/B) | Read |
|---|---|---:|---:|---:|---:|---:|---|
| 6525 | KOKUSAI Electric | 224.9 | **+52%** | 135.6 | **−9%** | 1.66 | Receipts surging but backlog *drawing down* — burning through backlog faster than refilling; consistent with NAND-cycle pause |
| 6590 | Shibaura Mech | 69.8 | +13% | 48.6 | **−19%** | 1.44 | Backlog shrinking on HB delay; receipts +13% from flip-chip run-rate |
| 6871 | Nihon Micronics | 75.8 | +10% | 34.6 | **+19%** | 2.19 | Both up; backlog accelerating faster — DRAM/HBM probe-card pull |
| 6855 | JEM | 26.4 | **+39%** | 8.4 | **+44%** | 3.13 | Cleanest demand expansion in cluster; Amagasaki greenfield justified |
| 4238 | Mirial | 13.7 | +12% | 4.7 | **+16%** | 2.86 | Microcap echo turning up; wafer-carrier order build precedes wafer-fab capex |
| 4062 | Ibiden (electronic) | 184.8 | +10% | 30.6 | **+109%** | 6.04 | **Biggest forward-demand surge in the screen**; backlog more-than-doubled. Confirms the ¥500B capex is order-led, not speculative |
| 4966 | C. Uyemura | 9.4 | +90% | 9.8 | +2% | 0.96 | Strong receipts flow-through; backlog flat (orders converting to revenue quickly) |
| 6146 | Disco | n/d | n/d | n/d | n/d | n/d | **Voluntarily dropped 受注実績 disclosure after FY23** (last value: backlog ¥124.6B). Per mgmt "cycle volatility" rationale. **Disclosure regression worth flagging — Disco was once one of the cleanest order-book reads.** |

**Note:** The Ibiden 受注実績 table covers only the **Electronic segment** (substrates) — the Ceramic and Other segments are not in the order-table disclosure. So ¥30.6B FY25 backlog (+109% YoY) is the substrate orderbook specifically, which is what matters for HBM/AI-server reads.

## D. Customer advances / contract liabilities — the other forward-demand proxy

For names that don't disclose 受注実績, the BS line for customer advances (前受金 / 契約負債) is the next-best forward-demand signal. **All amounts in ¥B; YoY = FY24→FY25.**

| Sec | Name | FY25 advances (¥B) | YoY | 5y trajectory | Read |
|---|---|---:|---:|---|---|
| 8035 | Tokyo Electron | **256.4** | **−12%** | 135.3 → 256.4 (+89%) | Largest absolute base; peaking |
| 4062 | Ibiden | **92.1** | **+15%** | 6.0 → 92.1 (15×) | Still building — AI-server customer prepayments through CY2029 commitments |
| 6920 | Lasertec | **64.4** | −13% | 25.7 → 64.4 (+150%) | Peaking; matches NAND mask-blank weakness narrative but **¥64B locked** = strongest forward-visibility in the screen |
| 6146 | Disco | 43.9 | −9% | 17.5 → 43.9 (+150%) | Flat; substitute for the lost 受注実績 disclosure |
| 6590 | Shibaura Mech | 4.7 | **−44%** | 0.5 → 4.7 (10×) | **Customers stopped pre-paying** — HB tool demand cooling at the order level despite the CIP build |
| 4966 | C. Uyemura | 4.5 | +2% | 3.3 → 4.5 (+38%) | Flat |
| 4369 | Tri Chemical | 0.7 | (n/a) | — | Too small to matter |
| 6871 | Micronics | 0.5 | −11% | — | Too small (order book is the better read) |

**Two-thesis read:**

- **Lasertec is the highest forward-visibility name post the addendum**: capex digested (CIP just ¥0.1B), ¥64B customer advances locked, FY30 ¥400–500B revenue target underwritten. The NAND mask-blank weakness shows up in the advances trajectory (−13% YoY) but doesn't void the long-dated thesis.
- **Shibaura is the cleanest mixed signal in the screen**: capacity build *up* (CIP +306%), customer advances *down* (−44%). Either Shibaura is right about future demand and front-running, or third-party reads are right that HB shipments are deferred 1–2 years and Shibaura is building capacity that won't be filled. The mixed signal at fwd P/E 7.1 is the asymmetric bet thesis from the original report — addendum confirms it's an active divergence, not a settled story.

## E. Capacity translation summary (where management names physical units)

Below ties the BS-confirmed in-flight capex to the named capacity commitments from the MTP section.

| Sec | Name | Named capacity commitment | BS confirmation status |
|---|---|---|---|
| 4062 | Ibiden | Cell6 Ogaki ¥220B + Ono Plant ¥280B = ¥500B FY26–28; reticle 3.5→9+, body 80×80→130×130mm; SAP 9-X-9 → 14-X-14 | ✅ ¥202B CIP already on BS; backlog +109% YoY confirms orders flowing |
| 6146 | Disco | Gohara Plant ¥40B+ initial, ~14× cap by 2035 | ⚠️ Only ¥17B CIP visible; bulk of Gohara still future-dated (10y phasing) |
| 4203 | Sumitomo Bakelite | Suzhou EMC 1.3× cap (online Jan 2025); Taiwan + Singapore complete 2024 | ✅ CIP dropped −40% YoY = transferred to PP&E; PP&E flat (FY24 ¥123B → FY25 ¥123B) = already producing |
| 4975 | JCU | Kumamoto ¥11.4B (Dec 2025 complete, May 2026 trial production) | ✅ ¥5.6B CIP (50% of plant total) — first-half phase visible; second half due in next yuho |
| 4369 | Tri Chemical | Minami-Alps extension + Taiwan plant; FY1/2028 rev 2× / OP 3× | ⚠️ CIP only ¥1.0B (5.4% of FA) — capex is going to equipment in existing plants, not building new shell |
| 4047 | Kanto Denka | Xuancheng China (CF4/C4F6/WF6) online FY3/27 | ✅ CIP +72% YoY to ¥17B; Xuancheng coming through |
| 3433 | Tocalo | Vietnam plant + Chandler AZ (co-located with AMAT); ¥9.0B FY26 capex | ⚠️ CIP ¥5.4B (12.5% FA) — partial confirmation; Chandler not yet visible (announced Apr 2026) |
| 6855 | JEM | Amagasaki greenfield Feb 2026 announce → Aug 2028 completion | ⚠️ CIP just ¥0.4B (4%) — too early; will show up FY26+ |
| 8035 | TEL | ¥3T+ rev / 35%+ OPM by 2027; AP +60%, etch +30% | ✅ CIP +57% to ¥137B = single biggest in-flight investment in the screen |
| 6857 | Advantest | FY27 3y-avg ¥835–930B; FY26 ¥950B | ⚠️ CIP just ¥5.7B (7%); Advantest is asset-light (R&D + outsourced manufacturing) |
| 6920 | Lasertec | FY30 ¥400–500B target | ✅ CIP fully digested; ¥64B customer advances locked |
| 6871 | Nihon Micronics | FY26/12 ¥80B; cum capex ¥56.3B FY23–26; Aomori new building Dec 2024 + Korea MEK | ✅ Aomori already in PP&E (¥38.7B vs ¥9.8B start FY20 = +295%); CIP +55% YoY = Korea/MEK next |
| 6961 | Enplas | FY26–28 cum capex ¥29.5B | ✅ CIP +476% YoY (¥0.9B → ¥5.2B) = first wave visible |
| 6590 | Shibaura | Aspiration: hybrid-bonding capacity | ⚠️ CIP +306% YoY = capacity going up; **but advances −44% = orders are not** |
| 3436 | SUMCO | Yoshinogawa pushed out | ✅ CIP rolled off ¥365B → ¥123B (5y peak digestion); confirms pause |

✅ = BS confirms the announced plan; ⚠️ = BS shows partial or asymmetric signal.

## F. Extended universe — 15 additional JP semi names (2026-05-27)

The original 20-name set was HBF/NAND-themed and missed five major adjacent process steps. Running the same XBRL extraction on **15 additional names** completes the JP semi supply chain to ~35 listed filers. Tiered by relevance to the HBM/AI-semi thesis:

### Tier 1 additions — directly HBM/AI-semi relevant (5 names)

| Sec | Name | Role | PP&E FY25 (¥B) | CIP (¥B) | CIP/FA | CIP YoY | 5y FA growth | Advances FY25 (¥B) | Adv YoY | Adv 5y growth |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 4063 | Shin-Etsu Chemical | Silicon wafer + photoresist | **2,066** | **451** | 17.9% | −1% | +69% | n/a | n/a | n/a |
| 4004 | Resonac | HBM underfill + CMP + EMC | 663 | 67 | 9.2% | +21% | −5% | n/a | n/a | n/a |
| 7741 | Hoya | EUV mask blanks | 211 | 36 | 14.6% | −13% | +31% | n/a | n/a | n/a |
| 7735 | SCREEN Holdings | Wafer cleaning tools | 113 | 5 | 3.9% | −30% | +73% | **100.4** | **−27%** | **+892%** |
| 4186 | Tokyo Ohka Kogyo | Photoresist | 110 | **32** | **22.5%** | +41% | **+147%** | 0.2 | +61% | +1629% |

**Five-name read:**

- **4063 Shin-Etsu**: ¥2.07T PP&E + ¥451B CIP is the **largest fixed-asset footprint in the entire 35-name JP semi screen** — bigger than SUMCO (¥786B FA) and Kioxia (¥1.10T) combined. CIP/FA 17.9% says ~¥451B of capacity is still in-flight (semi wafer + photoresist + magnets together). The 5y FA growth +69% on a multi-trillion-yen base is the *absolute-yen capacity buildup champion* — bigger than any other in the screen. **Missing this name from the original 20 was a material oversight.**

- **4004 Resonac**: PP&E down 9% over 5y reflects the petchem divestiture; CIP +21% YoY (¥56B → ¥67B) shows the **semiconductor materials capacity build** offsetting legacy disposals. HBM hybrid-bonding underfill (Naoetsu plant — same site as their EMC/CMP slurry) is the most direct HBM-stack exposure in the screen. The capex is going where it matters but the headline PP&E shrinkage masks it.

- **7741 Hoya**: PP&E +38% over 5y is the *most disciplined* capex profile among the Tier 1 names — EUV mask-blank monopoly throws off ~30% OPM with single-digit capex/revenue. CIP −13% YoY = capacity digested. **Quality moat, not capacity-growth story.** Buy for cash flow + multiple, not buildout.

- **7735 SCREEN Holdings**: the **single biggest customer-advances build** in the screen — ¥10.1B → ¥100.4B over 5 years (×10). FY25 YoY −27% (off the FY24 peak ¥137B) but absolute level still massive — cleaning-tool orders booked through ~2026–27. **PP&E +85% over 5y** confirms physical buildout. Strongest forward-demand visibility among the Tier 1 additions. SCREEN also stopped disclosing 受注実績 after FY22 (similar pattern to Disco).

- **4186 Tokyo Ohka Kogyo**: **CIP ¥4.6B → ¥32B over 5y (+602%)** = the photoresist capacity step-up; pairs with EUV ramp. CIP/FA = 22.5% (highest among Tier 1 additions). PP&E +107% over 5y. Customer advances are too small to read (off ¥14M base).

### Tier 2 additions — adjacent process steps (5 names)

| Sec | Name | Role | PP&E FY25 (¥B) | CIP (¥B) | CIP/FA | CIP YoY | 5y FA growth | Adv FY25 (¥B) | Backlog FY25 (¥B) | Back YoY |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 6315 | TOWA | AP molding tools | 25 | 0.8 | 3.3% | +257% | +83% | 1.8 (−30%) | 25.3 | **−19%** |
| 6728 | Ulvac | PVD/sputter | 77 | 5 | 6.1% | −20% | +18% | 23.0 (−14%) | 115.8 | **−20%** |
| 4109 | Stella Chemifa | HF (etch chemistry) | 27 | 5 | 14.9% | +8% | +20% | n/a | n/a | n/a |
| 6967 | Shinko Electric | IC substrates | 202 | 71 | 26.1% | +19% | +247% | 35.9 | n/a | n/a |
| 6383 | Daifuku | Fab automation/MHE | 108 | 6 | 5.2% | n/a | +130% | 74.2 (−7%) | 632.2 | **+6%** |

**Tier 2 read:**

- **6967 Shinko Electric — confirmed delisted state.** Last yuho filed FY3/2024 (no FY25 filing); DNP/JIC consortium tender closed mid-2024 and Shinko is now under private ownership. Historical data shows PP&E ¥93B → ¥202B (+116% in 5y) and CIP ¥31B → ¥71B — i.e. the substrate-capacity build that Ibiden's ¥500B plan competes against was already going aggressively at Shinko before privatization. **Track as ex-listco comparable for Ibiden, not as an investable name.**
- **6728 Ulvac**: backlog ¥145B → ¥116B (−20% YoY) + advances ¥27B → ¥23B (−14%) + receipts −13% = **deposition-tool cycle cooling**, aligned with KOKUSAI's "NAND tool investment slowdown" narrative at a different process-step (PVD vs ALD).
- **6315 TOWA**: CIP +257% YoY (¥0.2B → ¥0.8B) on a small base = AP-molding capacity build for HBM/CoWoS pull-through; but backlog −19% YoY = order book softening. Similar mixed signal to Shibaura.
- **6383 Daifuku**: backlog ¥632B vs revenue ~¥700B = ~10 months of orders in hand; YoY +6% backlog growth is steady. **Diversified across semi + EV battery + e-commerce MHE** — not a clean semi-pure-play.
- **4109 Stella Chemifa**: too small to move portfolio needles (¥30B mcap), but HF chemistry monopoly position makes it the materials counterpart to Kanto Denka. CIP/FA 14.9% with +8% YoY = modest build.

### Tier 3 additions — broader JP semi context (5 names)

| Sec | Name | Role | PP&E FY25 (¥B) | CIP (¥B) | CIP/FA | CIP YoY | 5y FA growth | Backlog FY25 (¥B) | Back YoY |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 285A | Kioxia | NAND maker (Dec 2024 IPO) | **1,100** | 56 | 4.9% | n/a (1y) | n/a (1y) | n/a | n/a |
| 4183 | Mitsui Chemicals | NF3 (exiting Mar 2026) | 623 | **108** | 14.8% | +15% | +42% | n/a | n/a |
| 6963 | ROHM | Power/SiC | 491 | 78 | 13.8% | −26% | **+111%** | 168.2 | **−13%** |
| 6723 | Renesas | Auto/logic | 356 | **131** | **26.9%** | +11% | +145% | n/a | n/a |
| 6266 | Tazmo | Coater/developer (small-cap) | 8 | 0.6 | 7.0% | +63% | +42% | 19.7 | **−37%** |

**Tier 3 read:**

- **285A Kioxia**: only 1 yuho post-IPO. ¥1,100B PP&E is in the same league as Shin-Etsu's silicon-wafer franchise — i.e. **Kioxia's own NAND fab capex is the lever everyone downstream depends on**. The next yuho (FY3/2026 expected Jun 2026) will show whether the FY25 ¥56B CIP grew into ¥100B+ in FY26 (i.e. Kitakami / Yokkaichi build accelerating) or contracted (capex pause). **This is the single highest-information-content next-filing watch in the whole study.**
- **4183 Mitsui Chemicals**: CIP ¥30B → ¥108B (+261%) over 5y is **not** about NF3 (which they're exiting) — it's their battery materials + mobility solutions buildup. Demonstrates that within a diversified chemicals filer, the NF3 line is a tiny fraction of total capex; the Kanto Denka NF3 tailwind from Mitsui's exit is unlikely to move Mitsui's own results materially.
- **6963 ROHM**: PP&E +101% over 5y, CIP +200% over 5y but **−26% YoY** = SiC capacity build peaking. **Backlog −13% YoY** = order book confirms the cycle pullback. This is the JP power-semi (Tesla / EV-skew) cycle, distinct from the HBM/AI cycle covered by the rest of the screen. Watch as a *contrast* read on which JP semi cycles are inflecting vs digesting.
- **6723 Renesas**: CIP ¥12B → ¥131B (+1025% over 5y, +11% YoY) is the **largest 5y CIP growth in the screen** by % — driven by greenfield auto/logic capacity (Kofu re-opening for power semis). Renesas doesn't disclose 受注実績 but the BS clearly shows a multi-year capacity step-up. Auto-semi theme, complementary to ROHM.
- **6266 Tazmo**: backlog ¥40B (FY23 peak) → ¥20B (FY25) = halved. **Backlog −37% YoY** is the steepest decline in the entire 35-name screen. Read as the small-cap canary for the coater/developer cycle — if Tazmo's backlog is rolling off this fast, TEL's coater segment guidance for FY27 deserves scrutiny.

### Cross-screen ranking after extension

**Highest-CIP-ratio names (capacity still in-flight):**

| Rank | Sec | Name | CIP/FA | Read |
|---|---|---|---:|---|
| 1 | 4975 | JCU | 32.2% | Kumamoto build first half |
| 2 | 4062 | Ibiden | 30.5% | ¥500B 3y plan execution |
| 3 | 6723 | Renesas | 26.9% | Auto/logic greenfield |
| 4 | 6967 | Shinko Electric | 26.1% | Pre-delisting substrate buildout (frozen) |
| 5 | 4047 | Kanto Denka | 23.8% | Xuancheng China NF3 |
| 6 | 8035 | TEL | 23.7% | ¥3T plan capacity |
| 7 | 4186 | TOK | 22.5% | EUV photoresist |
| 8 | 6590 | Shibaura | 21.9% | HB optionality (speculative) |
| 9 | 6961 | Enplas | 19.4% | Test-socket FY26-28 plan |
| 10 | 4063 | Shin-Etsu | 17.9% | Wafer + photoresist (largest absolute) |

**Biggest customer-advances build (5y % growth, where data available):**

| Rank | Sec | Name | FY20 → FY25 advances | 5y growth |
|---|---|---|---|---:|
| 1 | 4186 | TOK | ¥14M → ¥242M | +1629% (off tiny base) |
| 2 | 4062 | Ibiden | ¥6.0B → ¥92.1B | +1,432% |
| 3 | 7735 | SCREEN | ¥10.1B → ¥100.4B | **+892%** |
| 4 | 6920 | Lasertec | ¥25.7B → ¥64.4B | +150% |
| 5 | 6146 | Disco | ¥17.5B → ¥43.9B | +150% |
| 6 | 6728 | Ulvac | ¥11.6B → ¥23.0B | +99% |
| 7 | 8035 | TEL | ¥135.3B → ¥256.4B | +89% |
| 8 | 6383 | Daifuku | ¥40.7B → ¥74.2B | +82% |

**Biggest order-backlog YoY change FY25 (where 受注実績 disclosed):**

| Sec | Name | Backlog FY24 → FY25 (¥B) | YoY |
|---|---|---|---:|
| 4062 | Ibiden (electronic) | 14.7 → 30.6 | **+109%** |
| 6855 | JEM | 5.8 → 8.4 | +44% |
| 6871 | Micronics | 29.0 → 34.6 | +19% |
| 4238 | Mirial | 4.4 → 4.7 | +16% |
| 6383 | Daifuku | 596.7 → 632.2 | +6% |
| 4966 | C. Uyemura | 9.6 → 9.8 | +2% |
| 6525 | KOKUSAI | 149.7 → 135.6 | −9% |
| 6963 | ROHM | 193.3 → 168.2 | −13% |
| 6590 | Shibaura | 59.8 → 48.6 | −19% |
| 6315 | TOWA | 31.3 → 25.3 | −19% |
| 6728 | Ulvac | 145.0 → 115.8 | −20% |
| 6266 | Tazmo | 31.1 → 19.7 | **−37%** |

**Two cycle reads from this ranking:**

1. **HBM/AI-substrate names are the *only* ones with sharply rising backlogs** — Ibiden +109%, JEM +44%, Micronics +19%. Everyone else is flat to sharply declining.
2. **NAND-tooling + power-semi + auto-semi are *all* showing −13% to −37% backlog declines** — KOKUSAI, ROHM, Shibaura, TOWA, Ulvac, Tazmo cluster in the same range. The cross-cycle read is that **non-AI semi capex is unambiguously in a digestion phase**, while HBM/substrate is the only acceleration vector. This sharpens the original report's "capex is forking" thesis with order-book confirmation.

### Promoted to watch from the extension

- **7735 SCREEN Holdings** — promoted into the screen as a Tier 1 watch given the ¥100B customer-advances book + 85% PP&E growth + 5y advances ×10. Cleaning-tool franchise is HBM-relevant (memory wafer count per die scales with stack height).
- **4063 Shin-Etsu Chemical** — promoted into the screen as the largest absolute-yen capacity-build name in JP semi. The mega-cap parent in a thesis previously anchored on the more-volatile small/mid-caps.
- **4186 Tokyo Ohka Kogyo** — promoted as Tier 1 watch. The +602% CIP build is the loudest single-name capacity signal in the extension.
- **285A Kioxia** — first post-IPO yuho establishes baseline. Next yuho (Jun 2026) is the single most important upstream demand read for the entire NAND-supply-chain thesis.

### Demoted / context-only from the extension

- **6967 Shinko Electric** — delisted; track as historical comparable for Ibiden but not investable.
- **6963 ROHM, 6723 Renesas, 4183 Mitsui Chemicals** — different semi cycles (power, auto, diversified chemicals). Useful contrast reads but belong in a separate study.

## G. Refreshed view on the Tier 1/2 picks

Based on the BS + order-book signals, the original Tier 1 picks largely hold, with two adjustments:

- **Lasertec promoted to Tier 1.** The combination of CIP fully digested + ¥64B customer advances + raised FY06/26 guide + long-dated FY30 ¥400–500B target makes it the highest forward-visibility name in the screen. The NAND mask-blank weakness is a *current* (FY26 first-half) headwind, not a structural risk to the FY30 frame.
- **Ibiden conviction reinforced.** Electronic-segment backlog +109% YoY at the 受注実績 line is the single biggest forward-demand inflection across the 8 disclosing names. Customer advances still building (+15% YoY to ¥92B). CIP already starting to transfer to PP&E (PP&E +13%, CIP −14%) = capacity is going from "in-flight" to "in service" on schedule.
- **Shibaura redefined as a divergence trade, not a deep-value HB bet.** CIP +306% YoY says management is building; advances −44% YoY says customers aren't ordering. Either side of the trade is now anchored at the BS level. fwd P/E 7.1 is buying the divergence, not the consensus.
- **Enplas added to "watch" list (was Tier B in parent screen).** CIP +476% YoY is the second-largest CIP build by % among the test/probe cluster (after Micronics aggregation); pairs with the FY26–28 ¥29.5B cumulative-capex plan.
- **Disco disclosure regression flagged.** Voluntarily dropping 受注実績 after FY23 means investors lose ~70% of the forward-demand transparency. Customer advances ¥44B is the only remaining BS-level proxy. The thesis still holds (Gohara, ~70% dicing/grinding share, capex doubled YoY), but the visibility-discount should be priced.

## H. Facility locations & new-build pipeline (2026-05-27)

Pulled from yuho 「設備の新設、除却等の計画」 (planned facility additions) text-block across all 35 names. **¥M throughout (千円 figures /1000).** Full per-name tables in `./data/facilities-synthesis.md`. Headline observations below.

**Interactive map**: `./facilities-map.html` (sibling file) — Plotly scatter_geo with bubble size = ¥M disclosed, color = process cluster, ⭐ = hard physical-capacity % disclosed (only 6 plants). 84 active plant line items totaling **¥2,413B disclosed pipeline**. Asia view + world view.

**Six names disclosed NO new-build plans at all** (CIP / capex is going into equipment-into-existing-shells, not new construction):

| Sec | Name | Implication |
|---|---|---|
| 6920 | Lasertec | Confirms asset-light model — capex inside existing Yokohama footprint |
| 3436 | SUMCO | Striking silence — Yoshinogawa pause shows up at BS (CIP −67% YoY) but next phase not in yuho |
| 6857 | Advantest | Confirms asset-light — outsourced manufacturing model |
| 6315 | TOWA | Zero new-build despite TC-bonder demand suggests OPEX-leveraging existing footprint |
| 6728 | Ulvac | Asset-light versus the deposition demand wave |
| 4966 | C. Uyemura | Capex going into existing 3 JP plants (Tsumura, Saitama, Kakegawa) |

**Geographic clusters with material new-build activity:**

| Region | Names + plants | Cumulative ¥ disclosed |
|---|---|---:|
| **Gifu (Ogaki/Ibi-gun)** | Ibiden — Kawama ¥143B + Ogaki ¥12.9B + Ohno ¥119.5B + Ohno-add ¥23B | **¥298.4B** (single-firm cluster, ABF substrate) |
| **Kumamoto (TSMC JASM gravity)** | TEL Kyushu Koshi ¥61B + JEM Kikuchi ¥1.3B (4 lines) + JCU Mashiki ¥11.4B | **¥73.7B** |
| **Miyagi / Iwate (TEL belt)** | TEL Miyagi Yamato ¥226B + TEL Solutions Oshu ¥22B | **¥248B** |
| **Korea (memory belt — SK/Samsung)** | TEL Korea Hwaseong ¥62.5B + TOK Pyeongtaek ¥12B + Micronics Bucheon ¥4B + JCU Thailand sub ¥3.3B | **¥81.8B** |
| **Fukushima / Ibaraki (materials)** | TOK Koriyama ¥20B + Resonac materials JP aggregate ¥83.7B (segment-level only) | — |
| **Nagano / Niigata (substrate)** | Shinko Chikuma ¥140B + Shinko Arai ¥10.2B | ¥150.2B (delisted) |
| **Mie / Iwate (NAND fabs)** | Kioxia Yokkaichi + Kitakami ~¥63B 1Q FY26 paid basis | ~¥63B (¥-base understates; gen-8 ramp ongoing) |

**Only 6 hard physical-capacity numbers disclosed across the 35 names:**

| Sec | Plant | Capacity disclosed | Why notable |
|---|---|---|---|
| 8035 | TEL Miyagi production/logistics (¥104B) | **+250% capacity** | Largest hard-number disclosure in the screen |
| 8035 | TEL Solutions Iwate (¥22B) | **+50%** | Coater/developer capacity |
| 6967 | Shinko Chikuma (¥140B) | **+50% overall** | Flip-chip pkg buildout; now privatized but historical reference |
| 6967 | Shinko Arai (¥10.2B) | Plastic BGA cap expansion | — |
| 4109 | Stella Sanpo (¥6.2B) | **~2× filling capacity** (12-hr op) | HF acid niche |
| 4047 | Kanto Denka Mizushima (¥22.8B) | "新設・増強" | Fluorine + battery |

Every other filer hides behind 算定が困難 boilerplate — **any forward-looking model that requires hard capacity numbers from yuho is structurally limited to these six data points**. The rest must be triangulated via mgmt commentary, IR decks, and CIP-balance flow.

**Disclosed plans materially smaller than BS CIP — off-yuho pipeline candidates:**

| Sec | Name | Disclosed in yuho | CIP on BS | Gap implication |
|---|---|---|---|---|
| 6857 | Advantest | zero | ¥5.7B | Minor; asset-light |
| 3436 | SUMCO | zero | ¥123B | **Material gap** — Yoshinogawa is paused but other capex undisclosed |
| 6315 | TOWA | zero | ¥0.8B | Minor but striking given backlog softening |
| 6723 | Renesas | ¥85B (aggregate, 1Q FY26 ID basis) | ¥131B | Kofu 12-inch reopening not broken out at plant level |
| 4062 | Ibiden | ¥298.4B (currently disclosed) | ¥202B | FY26 yuho (June 2026) will refresh with the May 2026 board-approved ¥500B (Cell6 ¥220B + Ono ¥280B); current disclosure is the *prior* round |

**Notable single names:**

- **Ibiden's ¥298B disclosed pipeline is pre-board ¥500B**: the FY25 yuho shows 4 active projects (Kawama ¥143B, Ogaki ¥12.9B, Ohno ¥119.5B, Ohno-add ¥23B) representing the FY22–24 commitment rounds. The May 2026 board approval (¥500B FY26–28 = Cell6 Ogaki ¥220B + Ono ¥280B) will appear in the June 2026 yuho — i.e. the next yuho is the catalyst to confirm the official upgrade.
- **JEM's entire probecard pipeline is Kumamoto + Sanda**: every single of 6 line items lands in 熊本県菊池市 or 兵庫県三田市. The Sanda site is also where Murata/TI feed; Kumamoto is the JASM gravity well. **JEM is a Kumamoto pure-play on the probecard side.**
- **TEL Miyagi ¥104B production/logistics (+250%)** is the single largest *hard-disclosed* capacity expansion in the screen. Pairs with the FY27 ¥3T MTP target.
- **Shinko Chikuma ¥140B with +50% overall capacity** is the most aggressive substrate-side disclosure in the screen — but Shinko is delisted post-DNP/JIC, so this is now historical reference for Ibiden's competitive context.
- **Kioxia's ¥63B 1Q FY26 paid-basis** is the only disclosure that ties capex to a specific NAND generation milestone (8th-gen 3D NAND). The next yuho (June 2026) will be the first full-year baseline.
- **Mitsui Chemicals: ¥41B largest segment is Basic & Green Materials (petchem/EV), not ICT (¥29B)** — confirms semi is not where Mitsui's capex is going. The Kanto Denka NF3 exit tailwind is unlikely to be reciprocated by Mitsui expanding its own semi-chemicals.
- **SCREEN's new Yasu (滋賀県野洲市) land acquisition ¥4.7B** — early-stage but signals a third production site outside Hikone and Yasu existing footprint.

---

# What's missing / next research

- **HBF orderbook visibility**: none of the 17 MTPs name HBF. Catalysts to track: (i) SanDisk + SK Hynix HBF JDP product roadmap update; (ii) Kioxia FY3/27 capex guidance (Kioxia is unlisted as a single line in the JP supply chain, mostly via Toshiba/WD JV — but its Kitakami/Yokkaichi capex shapes the entire JP downstream).
- **Next-MTP unveils** clustered in May–June 2026: **Tocalo (May 11), Nitto Denko (May, likely with FY26 results), KOKUSAI (likely re-baselined post FY26 NAND slowdown), Kanto Denka (post FY3/26 MTP terminal)**. The 4-to-6 week window starting now will refresh forward visibility on roughly half the screen.
- **Hybrid-bonding share**: Shibaura's positioning vs BESI is the central second-derivative debate. Third-party (Lumen Alpha) framing says "not within 1–2 years" — re-read in 2027 if TSMC/Samsung diversifies suppliers.

# Cross-references

- **Parent screen**: `(parent screen — not published)` (23 names, valuation tiering, customer disclosure)
- **Dashboard**: `./cluster-dashboard.html` (interactive Plotly: cluster trends, per-name trajectories, capex bubble matrix)
- **Facilities map**: `./facilities-map.html` (interactive Plotly geo: 84 plant locations across 35 names, bubble size = ¥M disclosed in yuho 設備の新設 plan)
- **Adjacent screens**: `optics-photonics-jp-2026-05-24.md` (AI-DC optics), `~/brain/md/investments/stocks/6627-TeraProbe/` (per-name deep-dive)
- **Data**: `./data/` — `_enriched.json` (per-name aggregates), `_timeseries.json` (5–10y series), `mtp_*.md` (4 cluster MTP briefs)
- **Addendum data**: `./data/` — `_data.json` (raw per-name 6y series), `_master.json` (cluster-organized table), `_extension.json` (15 added names), `extract.py` (XBRL extraction script)
- **Facilities data**: `./data/facilities/` — `<sec>.txt` (per-company planned-facilities text dump), `_synthesis.md` (consolidated tables for all 35 names + cross-reads), `facilities.py` (extraction script)
- **Tools**: `edinet capex <secCode>` — per-filer 5–10y capex/R&D from XBRL; `./scripts/extract.py` — PP&E + CIP + advances + 受注実績 extractor; `./scripts/facilities.py` — yuho 設備の新設 plan extractor
