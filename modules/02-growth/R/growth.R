# Synthetic teaching examples. Monetary amounts are constant-price currency units
# (CU) unless stated otherwise. Run with the module folder as working directory.
growth_data <- read.csv("data/regional-growth.csv", stringsAsFactors = FALSE)
sector_data <- read.csv("data/sector-change.csv", stringsAsFactors = FALSE)

scalar <- function(x, lower = -Inf, upper = Inf) {
  is.numeric(x) && length(x) == 1L && is.finite(x) && x >= lower && x <= upper
}
growth_indicators <- function(data = growth_data) {
  stopifnot(all(is.finite(as.matrix(data[c("population", "employment", "real_value_added")]))),
            all(data$population > 0), all(data$employment > 0),
            all(data$real_value_added >= 0))
  transform(data, productivity = real_value_added / employment,
            employment_ratio = employment / population,
            per_resident = real_value_added / population)
}
growth_comparison <- function(data = growth_data) {
  d <- growth_indicators(data)
  do.call(rbind, lapply(unique(d$region), function(region) {
    z <- d[d$region == region, ]
    stopifnot(nrow(z) == 2L, setequal(z$period, c(0, 1)))
    z <- z[order(z$period), ]
    data.frame(region = region,
      output_pct = 100 * (z$real_value_added[2] / z$real_value_added[1] - 1),
      population_pct = 100 * (z$population[2] / z$population[1] - 1),
      productivity_pct = 100 * (z$productivity[2] / z$productivity[1] - 1),
      per_resident_pct = 100 * (z$per_resident[2] / z$per_resident[1] - 1))
  }))
}
sector_summary <- function(data = sector_data) {
  d <- transform(data, value_added = employment * value_added_per_worker)
  a <- aggregate(cbind(employment, value_added) ~ scenario, d, sum)
  a$productivity <- a$value_added / a$employment
  a[match(unique(data$scenario), a$scenario), ]
}

# b is the incremental local-income feedback per CU of regional income,
# not a gross sales multiplier or a separately estimated consumption propensity.
demand_effect <- function(delta_X = 100, b = 0.6) {
  stopifnot(scalar(delta_X), scalar(b, 0), b < 1)
  c(direct = delta_X, multiplier = 1 / (1 - b), total = delta_X / (1 - b))
}
demand_rounds <- function(delta_X = 100, b = 0.6, last_round = 12) {
  demand_effect(delta_X, b)
  stopifnot(scalar(last_round, 0, 10000), last_round == floor(last_round))
  k <- 0:last_round
  data.frame(round = k, income = delta_X * b^k,
             cumulative = cumsum(delta_X * b^k))
}

# Illustrative annual private budget. No endogenous wage/rent solution.
move_budget <- function(origin_wage = 100, origin_cost = 40,
                        destination_wage = 140, destination_cost = 70,
                        moving_cost = 15, years = 3) {
  stopifnot(all(vapply(list(origin_wage, origin_cost, destination_wage,
                          destination_cost, moving_cost), scalar, logical(1), lower = 0)),
            scalar(years, 1), years == floor(years))
  stay <- origin_wage - origin_cost
  move <- destination_wage - destination_cost
  data.frame(year = seq_len(years), stay = stay,
             move = move - c(moving_cost, rep(0, years - 1)),
             cumulative_gain = cumsum(move - stay - c(moving_cost, rep(0, years - 1))))
}

indicators <- growth_indicators()
growth_rates <- growth_comparison()
sectors <- sector_summary()
fmt <- function(x, digits = 0) format(round(x, digits), big.mark = ",", trim = TRUE,
                                    scientific = FALSE, nsmall = digits)
plot_growth <- function() {
  old <- par(mar = c(4.3, 4.6, 1, 1)); on.exit(par(old))
  d <- growth_indicators()
  x <- rbind(d$per_resident[d$region == "River"][order(d$period[d$region == "River"])],
             d$per_resident[d$region == "Harbor"][order(d$period[d$region == "Harbor"])])
  matplot(c(0, 1), t(x), type = "b", pch = c(16, 17), lty = 1:2, lwd = 3,
          col = c("#176B87", "#AC501C"), xaxt = "n", ylim = c(9, 18),
          xlab = "Period", ylab = "Real value added per resident (CU)")
  axis(1, at = c(0, 1))
  legend("topleft", c("River", "Harbor"), col = c("#176B87", "#AC501C"),
         lty = 1:2, pch = c(16, 17), lwd = 3, bty = "n", horiz = TRUE)
  text(c(0.5, 0.5), c(10.5, 15.5), c("10 to 11: +10%", "15 to 16: +6.7%"), pos = 3)
}
plot_rounds <- function() {
  old <- par(mar = c(4.3, 4.6, 1, 1)); on.exit(par(old))
  a <- demand_rounds(b = 0.6); b <- demand_rounds(b = 0.4)
  matplot(a$round, cbind(a$cumulative, b$cumulative), type = "b", pch = c(16, 17),
          lty = 1:2, lwd = 2, col = c("#176B87", "#AC501C"), ylim = c(0, 300),
          xlab = "Accounting round (not a year)", ylab = "Cumulative income change (CU)")
  abline(h = c(250, 100 / 0.6), lty = 3, col = c("#176B87", "#AC501C"))
  legend("bottomright", c("b = 0.6; limit 250", "b = 0.4; limit 166.7"),
         col = c("#176B87", "#AC501C"), lty = 1:2, pch = c(16, 17), bty = "n")
}
