# Module 6. Input-Output Analysis and Regional Linkages

Draft teaching plan for instructor review.

How does an order placed with one regional industry change production elsewhere? Students solve a regional input-output model in R and explain the assumptions behind its multiplier (LO6).

## Progression of ideas

1. **Define the shock and its boundary.** Return to Module 2’s demand spillovers and Module 3’s regional boundary. An additional order creates demand for inputs, but purchases from outside the region leave its production chain.
2. **Turn purchases into a model.** From a transactions table, derive the local inputs needed per unit of each sector’s output. Follow successive rounds of orders to motivate the Leontief inverse, then use it in R to solve for the total production response.
3. **Interpret the multiplier.** Separate gross output from value added and vary local sourcing. Ask where the extra workers and inputs would come from if firms expanded together. That question motivates the resource constraints in Module 7.

## Topic outline

### The regional transactions table

- Define the region and an outside order for one sector. Distinguish intermediate sales, final demand, imports, and value added in a two-sector economy.
- Derive local input coefficients from each purchasing sector’s column. Interpret them as requirements per unit of output.

**Instructor notes:**

### From supplier orders to the Leontief solution

- Trace successive rounds of local purchases to derive the output balance and motivate the inverse.
- Solve for the change in gross output in R. Check that increased production covers both additional intermediate demand and the original order.

**Instructor notes:**

### Interpreting a regional multiplier

- Direct and indirect production effects, and the induced spending channel when households are endogenous. Use value added to distinguish income generated from total sales across production stages.
- Vary local sourcing while holding the shock fixed. Consider how the result would change if suppliers competed for scarce workers instead of meeting each order at fixed prices.

**Instructor notes:**

## Readings and teaching materials

Schaffer, chs. 4–5, pp. 48–62, covers accounting and solution. Ch. 6, pp. 63–69, develops multipliers. Hewings, §4.1, pp. 28–30, supplies an impact application. The CSU workshop two-sector example can guide practice. The Viet Nam tables illustrate national linkages and require regional sourcing assumptions for a subnational application.

## Assessment connection

For PS 3, use a supplied table for the R solution, one demand shock, and one sensitivity comparison. The final exam can ask why a multiplier changes.

## Decision for review

Which shock and regional purchasing assumption should carry into M7 so students can compare the models?
