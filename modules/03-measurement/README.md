# Module 3. Defining and Measuring a Regional Economy

## Teaching materials

- [Lecture slides](slides.html) and the [opening seafood exercise (PDF)](seafood-order.pdf).
- [Cần Thơ Excel exercise and source data](can-tho-sector-data.xlsx). Students enter formulas on **Excel exercise** using the 2023 statistical yearbooks on **Sector data**. The 2021–23 series covers Cần Thơ’s pre-merger boundary. The 2023 figures are preliminary.
- [Worked examples reader (HTML)](reader.html) or [PDF](reader.pdf). The six sections match the printed page references in the slides.
- [Corridor workplace counts](corridor-jobs.csv) and [R script](regional-profile.R). From this folder run `Rscript regional-profile.R` to reproduce the profile.

The lecture develops sector shares, location quotients, and shift-share before introducing Cần Thơ. Students compare the 2022 employment and current-price value-added LQs for transportation and storage, then decompose the sector’s 2022–23 employment and real output growth. A separate [worked walkthrough (PDF)](../../dev/answer-keys/module-03/can-tho-excel-walkthrough.pdf) is available for the instructor to share. The fictional commuting and processing corridor provides optional practice. The reader also covers Atlanta retail and Pennsylvania manufacturing.

Which industries specialize locally, and how does their growth compare with national industry trends? Students build a profile in Excel (LO5, building on LO3). The corridor R script provides an optional second application.

## Progression of ideas

1. **Describe the sector mix.** Choose a boundary and calculate shares in people or value added. Connect the measure to workforce exposure or production.
2. **Compare with a benchmark.** Derive the LQ and consider what an employment or output LQ can tell a planner about local specialization.
3. **Account for growth.** Distinguish changes in local share from gains at national rates. Apply shift-share in people and in real value added, then discuss what evidence would justify a logistics training program. Module 4 develops the role of household and firm location choices.

## Topic outline

### Regional boundaries and comparable data

- Administrative regions and functional labor markets. The Module 2 commuting corridor illustrates how residence and workplace counts can describe different economies.
- Comparability across sector definitions, geographic boundaries, units, and years. Which employment figures can support a common comparison?

**Instructor notes:**

### Specialization relative to a benchmark

- Employment levels, sector shares, and the choice of reference economy. A small region can specialize in an industry that employs more people elsewhere.
- Use Excel to calculate the city’s employment and output LQs. In the optional corridor exercise, switch from a national to a provincial benchmark and ask which districts have an above-average processing share.

**Instructor notes:**

### Sources of regional employment and output change

- Starting with the city’s base-year industry level, calculate the gains implied by national growth overall and in the sector. Compare both with the observed gain. Repeat for real value added at 2010 prices.
- Read the regional shift alongside the initial location quotient. Could a region specialize in an industry and still add jobs more slowly than that industry grows nationally? Use the profile to identify one such pattern and ask what evidence on firms, workers, wages, or rents would help explain it.

**Instructor notes:**

## Readings and teaching materials

Schaffer, ch. 2, pp. 6–9, motivates the opening choice of region. Chapter 3, Note A, pp. 43–45, develops location quotients and shift-share. Its guidance on writing an area profile and presenting the results follows on pp. 45–47.

Use the full Chapter 3 (pp. 13–47) as a reference. Students who recall Module 2’s distinction between local and export sales can turn to pp. 19–21 to see how analysts use employment shares to infer exports and which assumptions that inference requires. Hoover and Giarratani provide supplemental reading on regions and their linkages in §§9.1–9.4 and on shift-share in appendix 12-1.

## Assessment connection

On PS 1, students use the supplied job counts to calculate location quotients and shift-share components and show their work on the handout. Exam 1 can ask students to interpret a quotient or a growth component.

## Data for class practice

The Excel workbook includes all-industry and sector levels for Cần Thơ and Vietnam. Students use current-price value added for 2022 composition and constant-price value added for the 2022–23 growth comparison. The separate corridor CSV provides workplace counts and alternative benchmarks for optional practice in R.
