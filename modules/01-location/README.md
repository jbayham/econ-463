# Module 1: Location, Cities, and Agglomeration

Instructor-review draft for ECON 463. Aligns with LO1–LO2, the dated semester schedule, and the local reading map. Assumes intermediate microeconomics and basic R familiarity. All numerical examples are synthetic, denominated in currency units (CU).

## Materials

- `slides.qmd` → `slides.html`: 33-slide, 16:9 Reveal.js deck, with speaker notes, timed activities, and staged answers.
- `reader.qmd` → `reader.html` and `reader.pdf`: approximately 5,000 words, with detailed explanations, worked answers, R examples, and reading guidance.
- `R/examples.R` and `data/location-costs.csv`: shared calculations, inputs, and figure functions used by both documents.
- `../references.bib`: shared course bibliography, inherited through `modules/_quarto.yml`. `assets/slides.scss` supplies the deck styling.

The reader and slides follow the same seven sections and three example labels. Example 1 compares three plant locations and freight thresholds. Example 2 compares one plant with two plants. Example 3 diagnoses supplier, labor, and learning mechanisms in a hypothetical precision-component cluster.

## Teaching sequence

| Date / section | Slides | Working minutes |
| --- | --- | ---: |
| Nov 23: Opening question | 1–4 | 15 |
| Natural advantages and firm location | 5–12 | 40 |
| Scale economies and city formation | 13–19 | 35 |
| Guided practice and synthesis | 20–22 | 30 |
| Nov 25: Agglomeration mechanisms | 23–27 | 30 |
| Limits and competing explanations | 28–31 | 20 |
| Retrieval and Module 2 bridge | 32 | 10 |
| Reading reference | 33 | No additional time |

November 23 has 120 working minutes plus a 10-minute break after slide 13 (60 working minutes into the meeting). November 25 devotes its first 60 working minutes to M1 and leaves 60 for M2; the shared meeting's break can fall at the module transition. November 24 has no class or required work. Speaker notes contain activity prompts and timings. Press **S** in Reveal.js for speaker view; arrow keys advance, including staged solution fragments.

These materials provide ungraded practice only. The graded M1 portion of A1 remains to be written separately. The established A1 release (Nov 23), checkpoint (Nov 27), and final deadline (Nov 30) are unchanged.

## Render and reproduce

From the repository root:

```sh
quarto render modules/01-location/slides.qmd --to revealjs
quarto render modules/01-location/reader.qmd --to html
quarto render modules/01-location/reader.qmd --to pdf
```

Dependencies: Quarto, R, knitr, and rmarkdown; PDF rendering additionally requires XeLaTeX and its normal Quarto packages. The examples themselves use base R. Outputs stay beside sources. Use explicit `--to` arguments because the parent Quarto project retains legacy PDF defaults. The module does not alter that shared configuration.

To explore the calculations interactively, set R's working directory to this module folder:

```r
source("R/examples.R")
location_costs(1)
location_costs(0.5)
location_threshold()
plant_costs(t = 4)
plot_location()
```

`tau` changes only outbound freight. The data and result table's `outbound` column always stores baseline outbound freight; `total` applies the multiplier. `q` is demand per market, not total output. Fixed operating cost is avoidable per plant per period. Keep revenue fixed when using cost rankings as profit rankings.

HTML outputs embed their principal resources. The current Quarto math renderer may request web resources, so open the deck on the classroom computer before teaching. The PDF reader provides an offline alternative. No materials have been published or added to course-site navigation.

## Reading verification

Verified against the local editions on November 2, 2026:

- Brueckner (2011), Ch. 1, §§1.1–1.5, printed pp. 1–18 (PDF pp. 12–29): introduction, scale, agglomeration, firm location, scale–transport tradeoff. Primary reading.
- Hoover–Giarratani, local fourth-edition web version (2020): Ch. 1, pp. 12–15; §§2.3–2.7, pp. 19–35; §§5.2–5.4, pp. 84–96. Supplemental selections; printed page + 1 gives PDF page.
- Glaeser–Gottlieb (2009), §3, pp. 999–1015 (PDF pp. 17–33): optional advanced discussion, not a full-article assignment.
- World Bank, *Vietnam Development Report 2019*, final report December 2019, copyright 2020: Chapter 4, Figure 4.1, printed p. 79 / PDF p. 99. Historical context only; no synthetic example is presented as Vietnamese empirical data.

Local reference PDFs are not copied into student materials. Bibliographic references use portable citations and, where appropriate, a public source URL. The reader gives printed/PDF page conversions.

## Review status

Rendered and reviewed on November 2, 2026 with Quarto 1.3.450: 33 slides and both reader formats. Browser checks found no slide overflow, broken reader images, or missing internal anchors. All PDF pages were visually reviewed.

Numeric checks cover baseline and reduced-freight rankings, both relevant site-switch thresholds, the pairwise tie versus third-site comparison, baseline plant costs, the shipping tie, a high-freight case, doubled demand, and a reduced-fixed-cost case. Check all rendered formats and inspect slide/PDF layout after editing figures or equations.

Outstanding instructor decisions: review pacing and examples; prepare graded A1 questions separately; confirm classroom display and R access. This module does not select a continuing empirical dataset for later modules.

## Repository persistence

Existing ignore rules were preserved. The root pattern `*exam*` also matches `R/examples.R`, so ordinary Git staging omits that required script. Include it explicitly with a force-add when committing the module, or deliberately revise the ignore rule in a separate repository-maintenance step. The handoff in `docs/` and the source collection in `references/` also remain ignored. No files were staged or committed in this build.
