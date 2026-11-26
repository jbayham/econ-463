# River and Harbor: a first R exercise
# Open this script in RStudio. Work from the top, one line or block at a time.
# Each gap compares River with Harbor and is measured in log points.

## ---- first-calculation
0.25 * 8

## ---- model-inputs
s <- 0.25  # Households' land budget share
t <- 0.20  # Firms' land cost share
a <- 0     # Amenity gap
b <- 4     # Productivity gap

## ---- one-rent
x <- 8
worker <- s * x - a
firm <- (b - t * x) / (1 - t)
c(worker = worker, firm = firm)

## ---- several-rents
x <- c(0, 8, 10, 12)
worker <- s * x - a
firm <- (b - t * x) / (1 - t)
data.frame(x, worker, firm)

## ---- park-access
a <- 2  # Better park access
x <- c(10, 12, 14, 16)
worker <- s * x - a
firm <- (b - t * x) / (1 - t)
data.frame(x, worker, firm)

## ---- exact-intersection
coefficients <- rbind(c(-s, 1), c(t, 1 - t))
colnames(coefficients) <- c("rent", "wage")
solve(coefficients, c(-a, b))
