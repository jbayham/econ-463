# Module 7. Regional CGE Modeling and Model Comparison

Draft teaching plan for instructor review.

How does the impact estimate change when firms and households respond to prices and resources are scarce? Students reproduce a benchmark with a supplied computable general equilibrium model in R, run a counterfactual, and explain the difference from IO (LO6).

## Progression of ideas

1. **Follow production income back to demand.** Extend Module 6’s transactions table to a social accounting matrix. A payment for labor becomes household income, which helps determine purchases from firms.
2. **Specify how the region adjusts.** Add choices about inputs and consumption, market-clearing conditions, and a closure that specifies which quantities or prices can adjust. Use the supplied CGE model in R to reproduce the benchmark before changing demand.
3. **Explain the difference between models.** Apply a comparable shock in IO and CGE. Trace a difference in output or income to a particular mechanism, such as a higher wage when labor is scarce. Vary one assumption to see whether that explanation holds. Module 8 uses the comparison to assess a policy claim.

## Topic outline

### Social accounts and economic behavior

- Trace income from producers to factors and households, then from household purchases back to producers. Connect the IO table to a social accounting matrix.
- Production choices, substitution, household budgets, and goods and factor market clearing. Identify the behavioral assumptions needed to simulate a change from the observed accounts.

**Instructor notes:**

### Closure, calibration, and the benchmark

- Specify which factors can move, how the region trades, and which prices or quantities adjust. Distinguish these closure choices from the choice of numeraire.
- Calibrate the supplied model and reproduce the benchmark in R. Check quantities, relative prices, and market balances against the base economy.

**Instructor notes:**

### Counterfactuals and comparison with IO

- Align the region, baseline, units, and shock with Module 6. Trace an outcome difference through wages, substitution, or trade.

**Instructor notes:**

### Sensitivity and incidence

- Vary one closure assumption, such as labor mobility, and explain the economic reason for the change in results.
- Distinguish sector output from household income and identify any welfare measure supported by the selected model.

**Instructor notes:**

## Readings and teaching materials

Hewings, §7.2, pp. 52–54, and §7.4, pp. 55–57, bridges IO and social accounting. The workshop SAM elements description supports account mapping. A model-specific guide still needs to cover calibration, closure, solution in R, and the interpretation of outputs.

## Assessment connection

PS 4 draws on the baseline, scenario output, and mechanism. Sensitivity and interpretation connect the comparison to policy evaluation.

## Decision for review

Select the small model, its closure, and a shock comparable to PS 3 before drafting the guide. Which welfare measure, if any, does that model actually produce?
