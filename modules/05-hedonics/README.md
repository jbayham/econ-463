# Module 5. Housing, Land Use, and Hedonics

Draft teaching plan for instructor review.

How do access to jobs and local amenities show up in rents and house prices? Students relate price differences to housing supply and land use, then estimate and interpret a hedonic regression in R (LO4).

## Progression of ideas

1. **Measure the value of access.** Return to the two homes in Module 4. Derive the rent–distance gradient under a common job location, then plot rents against commuting distance in R. Interpret the fitted slope and ask what else differs between nearby and distant homes.
2. **Connect land use to capitalization.** Compare two neighborhoods that gain equally valuable access to jobs. Where more homes can be built, construction can accommodate part of the increase in demand. Where a binding limit restricts construction, expect a larger rent increase, all else equal. Then use airport noise to ask how a local disamenity shows up in sale prices.
3. **Decide what the gradient can explain.** Compare specifications and consider who sorts into each neighborhood. State what evidence would support attributing a price change to noise abatement. Revisit that distinction in Module 8 when an intervention changes both economic activity and local amenities.

## Topic outline

### Commuting, land use, and housing supply

- In the rent–distance R demo, interpret the slope in monthly rent per unit of distance. Predict how cheaper commuting changes the gradient when jobs stay at the center and the homes are otherwise alike.
- Compare how rents and the number of homes respond to better access when new construction is feasible and when a land-use rule limits density. Use this comparison to introduce capitalization into land and housing values.

**Instructor notes:**

### Capitalization and the housing bundle

- Use the airport-noise case to compare sale prices of otherwise similar homes in the same labor market. Define the exposure, outcome, units, and relevant market.
- Sources of a raw price gap, including structural characteristics, neighborhood amenities, and access to employment.

**Instructor notes:**

### Hedonic estimation and interpretation

- Specify and estimate a price equation in R. Translate the exposure coefficient into a predicted price difference for a meaningful change in noise.
- Compare specifications using the same homes. Explain why adding a location control might change the estimated gradient.

**Instructor notes:**

### Sorting, policy effects, and welfare

- Households differ in their preferences and ability to pay, and choose among bundles of housing, access, and noise exposure.
- Distinguish the conditional price gradient from the effect of noise abatement. Identify what additional comparison or assumptions would support a causal or welfare claim.

**Instructor notes:**

## Readings and teaching materials

Complete Brueckner, ch. 2, §§2.5–2.8, for housing production, density, and the spatial pattern of development. Use §6.2, pp. 116–119, for the hedonic approach. The airport-noise application in Hall, Lawson, and Shia, ch. 5, pp. 65–75, especially §§5.4–5.5, connects specification choices with results. Komarek’s amenities notes, PDF pp. 8–25, provide supporting lecture material.

## Assessment connection

PS 2 is due Dec 7 with an R estimate and interpretation. The Dec 7 exam can supply regression output and ask which claim the evidence supports.

## Decision for review

Choose a housing dataset with documented price and exposure units. Can students fit both specifications during guided practice?
