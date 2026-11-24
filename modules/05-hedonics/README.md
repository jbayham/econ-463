# Module 5. Hedonics and Interpretation of Spatial Evidence

Draft teaching plan for instructor review.

What can a house-price difference tell us about an amenity? Students estimate and interpret a hedonic regression in R and explain how sorting and omitted characteristics affect the estimate (LO4).

## Progression of ideas

1. **Turn a prediction into a comparison.** Module 4 suggests that households bid more for otherwise similar homes with better amenities. Use airport noise to specify which homes to compare and predict the sign of the price difference.
2. **Account for the housing bundle.** Homes also differ in size, quality, and access to jobs. Move from a raw price gap to a hedonic regression in R and express the estimated noise gradient in price units.
3. **Decide what the gradient can explain.** Compare specifications and consider who sorts into each neighborhood. State what evidence would support attributing a price change to noise abatement. Revisit that distinction in Module 8 when an intervention changes both economic activity and local amenities.

## Topic outline

### Capitalization and the housing bundle

- Use the airport-noise case to translate the Module 4 amenity prediction into a comparison between homes. Define the exposure, outcome, units, and relevant market.
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

Brueckner, §6.2, pp. 116–119, introduces capitalization. Use the airport-noise application in Hall, Lawson, and Shia, ch. 5, pp. 65–75, especially §§5.4–5.5, to connect specification choices with results. Komarek’s amenities notes, PDF pp. 8–25, provide supporting lecture material.

## Assessment connection

PS 2 is due Dec 7 with an R estimate and interpretation. The Dec 7 exam can supply regression output and ask which claim the evidence supports.

## Decision for review

Choose a housing dataset with documented price and exposure units. Can students fit both specifications during guided practice?
