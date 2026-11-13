# Module 1: Location, Cities, and Agglomeration

Explore how natural advantages, transport costs, scale economies, and agglomeration shape the location of economic activity.

## Materials

- [Reader (HTML)](reader.html) or [reader (PDF)](reader.pdf): explanations, worked examples, practice questions, and a reading guide.
- [Lecture slides](slides.html): class discussion, calculations, and optional practice.
- [R calculations](R/examples.R) and [location-cost data](data/location-costs.csv): reproduce the examples and explore different assumptions.

The examples compare three plant locations, one plant versus two plants, and the mechanisms behind a hypothetical industrial cluster. All numerical data are synthetic; monetary amounts use illustrative currency units (CU).

## Work through the examples

Read each setup, predict the result, and try the calculation before consulting the worked answer. Explain the mechanism and identify an assumption that could change your conclusion. The exercises are ungraded practice.

To reproduce the calculations, download the R script and CSV, keeping the `R/` and `data/` folders together inside `01-location/`. Set R's working directory to that module folder, then run:

```r
source("R/examples.R")
location_costs(tau = 1)
location_costs(tau = 0.5)
location_threshold()
plant_costs(t = 4)
plot_location()
```

Only base R is needed. `tau` changes outbound freight only. The `outbound` column retains baseline freight; `total` applies the multiplier. In the plant comparison, `q` is demand per market. Keep revenue fixed when interpreting cost rankings as profit rankings.

## Readings

Start with Brueckner, *Lectures on Urban Economics*, Chapter 1, §§1.1–1.5, pp. 1–18. The reader identifies supplemental selections from Hoover and Giarratani, optional advanced discussion from Glaeser and Gottlieb, and a historical Vietnam illustration from the World Bank.

Use the reader's reading guide for section and page references. The PDF reader can be used offline.
