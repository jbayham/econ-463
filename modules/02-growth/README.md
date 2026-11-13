# Module 2: Regional Growth and Interregional Connections

Explore why regions grow differently and how trade, migration, capital, and knowledge connect their economies.

## Materials

- [Reader (HTML)](reader.html) or [reader (PDF)](reader.pdf): explanations, worked examples, practice questions, and a reading guide.
- [Lecture slides](slides.html): class discussion, calculations, and optional practice.
- [R calculations](R/growth.R): reproduce growth indicators, income feedback, moving budgets, and figures.
- [Regional-growth data](data/regional-growth.csv) and [sector-change data](data/sector-change.csv): inputs for the numerical examples.

River and Harbor are fictional regions. All observations are synthetic, and monetary amounts use illustrative currency units (CU). The examples compare regional growth, trace an income-feedback response, and examine a hypothetical transport corridor.

## Work through the examples

Try each calculation before consulting the worked answer. State the outcome, the comparison, and the assumptions behind your explanation. The exercises are ungraded practice.

Download the R script and both CSV files, keeping the `R/` and `data/` folders together inside `02-growth/`. Set R's working directory to that module folder, then run:

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

Only base R is needed.

## Data and interpretation

| File / variable | Definition |
|---|---|
| `regional-growth.csv`: `region`, `period` | Fictional River/Harbor and comparable observations 0/1 |
| `population` | Total residents, people |
| `employment` | Employed workers; no cross-boundary commuting in this example |
| `real_value_added` | Output less purchased intermediates, constant-price CU per period |
| `sector-change.csv`: `scenario`, `sector` | Baseline or separate Reallocation counterfactual; Agriculture or Other |
| `employment` | Workers in that sector; total remains 500 |
| `value_added_per_worker` | Constant-price CU per worker per period, held fixed within each sector |

The period length is unspecified, so percentage changes are not annual rates. Production per resident is not resident disposable income or welfare. The reallocation scenario is a separate counterfactual, not an explanation of River's observed period-1 production.

In `demand_effect()`, `delta_X` is an exogenous addition to regional income, net of imported intermediate inputs. The feedback coefficient must satisfy `0 <= b < 1`. The calculation holds prices fixed and assumes available capacity; accounting rounds are not years.

The moving budget uses annual wages and costs plus a one-time moving expense. It assumes certain employment, constant prices, identical other expenses and amenities, and no discounting. Do not add results across the examples: their outcomes, horizons, and assumptions differ.

## Readings

Start with Hoover and Giarratani, *An Introduction to Regional Economics*, §11.2, pp. 223–224; §11.5, pp. 234–236; and §11.6, pp. 237–239. The reader's reading guide lists supporting selections and page references. The PDF reader can be used offline.
