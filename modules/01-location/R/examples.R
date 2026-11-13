# All monetary values are illustrative currency units (CU), not observed data.
location_data <- read.csv("data/location-costs.csv", stringsAsFactors = FALSE)
location_costs <- function(tau = 1) {
  stopifnot(length(tau) == 1, is.finite(tau), tau >= 0)
  transform(location_data, total = production + inbound + tau * outbound)
}
location_threshold <- function(first = "Resource", second = "Junction") {
  a <- location_data[match(first, location_data$site), ]
  b <- location_data[match(second, location_data$site), ]
  ((b$production + b$inbound) - (a$production + a$inbound)) /
    (a$outbound - b$outbound)
}
plant_costs <- function(t = 4, F = 1200, c = 20, q = 100) {
  stopifnot(all(is.finite(c(t, F, c, q))), t >= 0, F >= 0, c >= 0, q > 0)
  c(centralized = F + c * 2 * q + t * q,
    dispersed = 2 * F + c * 2 * q)
}
fmt <- function(x) format(x, big.mark = ",", trim = TRUE, scientific = FALSE)
base_location <- location_costs()
low_location <- location_costs(0.5)
base_plants <- plant_costs()
plot_location <- function() {
  old <- par(mar = c(4.3, 4.4, 1, 1)); on.exit(par(old))
  tau <- seq(0, 2, length.out = 201)
  costs <- sapply(tau, function(t) location_costs(t)$total)
  matplot(tau, t(costs), type = "l", lty = 1:3, lwd = 3,
          col = c("#176B87", "#AC501C", "#555555"),
          xlab = "Outbound freight multiplier (tau)",
          ylab = "Delivered cost (CU per unit)")
  abline(v = location_threshold(), lty = 3, col = "#999999")
  legend("topleft", location_data$site, col = c("#176B87", "#AC501C", "#555555"),
         lty = 1:3, lwd = 3, bty = "n")
}
plot_plants <- function() {
  old <- par(mar = c(4.3, 4.4, 1, 1)); on.exit(par(old))
  t <- seq(0, 20, length.out = 201)
  costs <- sapply(t, plant_costs)
  matplot(t, t(costs), type = "l", lty = 1:2, lwd = 3,
          col = c("#176B87", "#AC501C"),
          xlab = "Intermarket shipping cost (CU per unit)",
          ylab = "Total cost (CU per period)")
  abline(v = 12, lty = 3, col = "#999999")
  legend("topleft", c("One plant", "Two plants"),
         col = c("#176B87", "#AC501C"), lty = 1:2, lwd = 3, bty = "n")
}
plot_average_cost <- function() {
  old <- par(mar = c(4.3, 4.4, 1, 1)); on.exit(par(old))
  Q <- seq(20, 250, length.out = 200)
  plot(Q, 1200 / Q + 20, type = "l", lwd = 3, col = "#176B87",
       xlab = "Output per plant (units per period)",
       ylab = "Production average cost (CU per unit)")
  points(c(100, 200), c(32, 26), pch = 19, cex = 1.3)
  text(c(100, 200), c(32, 26), c("100 units: 32", "200 units: 26"), pos = 3)
}
