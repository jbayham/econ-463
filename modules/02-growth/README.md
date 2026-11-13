# Module 2: Regional Growth and Interregional Connections

Instructor-review draft for ECON 463, prepared November 11, 2026. Matches Module 1's Quarto reader/deck structure and visual style. Covers LO2–LO3 in 120 working minutes: 60 on November 25 after M1, and 60 on November 26 before M3. Examples assume intermediate microeconomics, basic arithmetic/algebra, and introductory R familiarity.

## Materials

- [slides.qmd](slides.qmd) → [slides.html](slides.html): 33-slide, 16:9 Reveal.js deck, including a title, a break, references, and two optional backups. Speaker notes contain timings, expected answers, assumptions, and transitions. Press **S** for speaker view.
- [reader.qmd](reader.qmd) → [reader.html](reader.html) and [reader.pdf](reader.pdf): 13 pages and approximately 4,600 words with explanations, worked answers, R practice, and a bounded reading guide.
- [R/growth.R](R/growth.R): shared indicators, feedback and moving-budget calculations, and figure functions.
- [data/regional-growth.csv](data/regional-growth.csv) and [data/sector-change.csv](data/sector-change.csv): synthetic inputs, with definitions below.
- [R/checks.R](R/checks.R): numerical checks, accounting identities, sensitivity cases, and input-domain checks.
- `assets/slides.scss`: Module 1's deck styling copied locally. Bibliography inherited from `modules/references.bib`; no changes to shared configuration or existing M1 files.

The deck and reader follow the same sequence. Example 1 compares River and Harbor, including a separate sector-reallocation counterfactual and a return to convergence. Example 2 traces an exogenous addition to local income through a scalar feedback model. Example 3 traces a hypothetical transport corridor through trade, competition, migration, capital, and rural–urban connections, including a small private moving-budget calculation.

## Teaching sequence

Slide numbers include the title slide.

| Date / section | Slides | Working minutes |
|---|---|---:|
| Nov 25: Opening, growth measures, and structural change | 1–8 | 28 |
| Export demand, feedback, sensitivity, and supply constraints | 9–14 | 24 |
| Individual response, paired comparison, and debrief | 15 | 8 |
| Nov 26: Trade, migration, and rural–urban connections | 16–23 | 30 |
| Convergence and evidence | 24–27 | 16 |
| Guided calculation and R check | 28 | 8 |
| Synthesis and M3 bridge | 29 | 6 |
| Nov 26 break before M3 | 30 | 10 (not working time) |
| Reading reference | 31 | No additional time |
| Optional backups: decline and reallocation | 32–33 | Outside scheduled teaching |

On November 25, take the day's 10-minute break between M1 and M2. On November 26, teach M2's 60 minutes, take the break, and leave the remaining 60 working minutes for M3. Do not treat either day as a full M2 meeting. No advance reading is needed to follow the calculations; selected readings deepen the discussion afterward.

These are ungraded teaching examples with deliberately student-facing answers. The graded M2 component of A1 remains to be prepared separately and integrated with M1/M3. There is no new assignment or private answer key. A1 release (Nov 23), checkpoint (Nov 27), final deadline (Nov 30), and Exam 1 scope (M1–M5, Dec 4) remain unchanged.

## Data and interpretation

All observations are synthetic, not Vietnamese empirical estimates. Monetary amounts use illustrative CU. The period-0 and period-1 production data use constant prices and consistent definitions; the period length is unspecified, so percentage changes are not annual rates.

| File / variable | Definition |
|---|---|
| `regional-growth.csv`: `region`, `period` | Fictional River/Harbor and comparable observations 0/1 |
| `population` | Total residents, people |
| `employment` | Employed workers; assume no cross-boundary commuting in this example |
| `real_value_added` | Output less purchased intermediates, constant-price CU per period |
| `sector-change.csv`: `scenario`, `sector` | Baseline or separate Reallocation counterfactual; Agriculture or Other |
| `employment` | Workers in that sector; total remains 500 |
| `value_added_per_worker` | Constant-price CU per worker per period, held fixed within each sector |

Key qualifications:

- `Y/N` measures production per resident, not resident disposable income or welfare. `L/N` is workers divided by all residents, not one minus unemployment.
- Sector reallocation starts from River's baseline but does not explain its actual period-1 observation. The example assumes additional jobs and complementary inputs are available at fixed productivity; average gaps do not identify the gain from moving a particular worker.
- In `demand_effect(delta_X, b)`, `delta_X` is an exogenous regional-income addition associated with outside demand, already net of imported intermediate inputs. It is not gross sales. `b` is effective local-income feedback, with `0 <= b < 1`. The calculation is a one-period level response under fixed prices and available capacity; rounds are not years. It is not an IO/CGE solution or a long-run growth forecast.
- The migration budget uses annual wages/costs and a one-time moving expense. It assumes certain employment, constant prices, identical other expenses/amenities, and no discounting. It is not a spatial-equilibrium or full welfare model.
- Do not add results across the examples: their outcomes, horizons, and assumptions differ. No continuing empirical dataset or causal estimate has been selected for later modules.

## Render and reproduce

From the repository root:

```sh
quarto render modules/02-growth/slides.qmd --to revealjs
quarto render modules/02-growth/reader.qmd --to html
quarto render modules/02-growth/reader.qmd --to pdf
```

Quarto, R, knitr, and rmarkdown are required; the PDF also needs XeLaTeX and standard Quarto TeX packages. Calculations use base R. Explicit formats avoid the parent project's legacy PDF defaults. Outputs remain beside sources.

Set R's working directory to `modules/02-growth/` and run:

```r
source("R/growth.R")
growth_indicators()
growth_comparison()
sector_summary()
demand_effect(delta_X = 80, b = 0.5)
demand_rounds()
move_budget(destination_cost = 85)
plot_growth()
plot_rounds()
```

For numerical verification, run `Rscript R/checks.R` from the module directory. Check both rendered documents after changing inputs; explanatory prose and slide tables also contain worked numeric values that must stay synchronized.

## Reading verification

Checked against the local Hoover–Giarratani fourth-edition web version, updated 2020. Printed page + 1 = PDF page.

- Selected primary: §11.2, pp. 223–224; §11.5, pp. 234–236; §11.6, pp. 237–239.
- Targeted support: opening of §11.3.1, pp. 224–225; §11.4, pp. 233–234; §10.3, pp. 197–208.
- Optional cities/development context: §11.7, pp. 239–242.

The broader chapter in `docs/Readings.md` is a selection menu. Detailed IO calculations are deferred to M6. Historical illustrations are not current facts about Vietnam. The local reference PDF is not copied into student materials.

## Review and handoff

The three formats were rendered, all 33 slides and all PDF pages were visually inspected, and slide checks found no overflow. Numerical checks cover growth rates, the per-resident accounting identity, sector totals, positive/negative/zero demand changes, two leakage sensitivities, finite-round convergence, migration horizons and living-cost sensitivity, and invalid parameter values. HTML images, internal anchors, and math rendering were checked. The reader uses nonbreaking numerical tables in PDF to keep the short regional comparison together.

HTML embeds principal resources, but Quarto's math renderer can request web resources. Open the materials on the classroom computer before teaching; the PDF is an offline reader. Instructor review of content and pacing, classroom R access, and separate graded A1 questions remain.

M3 receives boundary/comparability questions and the distinction between within-sector and compositional change, without a prescribed dataset. M4 receives migration costs and wage–rent adjustment questions. M6 receives the demand-feedback intuition, with income and sales explicitly distinguished. M7/M8 receive the limitations of fixed prices, capacity assumptions, and activity versus welfare.

The course-site navigation and shared schedule were not changed, and nothing was published, staged, or committed. `docs/` and `references/` remain ignored. The `R/growth.R` name avoids the existing `*exam*` ignore rule that affects M1's `examples.R`; the new module's required files are visible to ordinary Git staging. Cross-module status is recorded in `docs/module-development-handoff.md`.
