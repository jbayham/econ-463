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

# Illustrative basket technology: reeds available as needed; fixed workforce 100.
basket_output <- function(L) L * (1 + sqrt(L))
basket_table <- data.frame(
  Arrangement = c("100 workshops", "One factory"),
  Plants = c(100, 1), Workers_per_plant = c(1, 100),
  Output_per_worker = basket_output(c(1, 100)) / c(1, 100),
  Total_output = c(100 * basket_output(1), basket_output(100)))
plot_baskets <- function(stage = 2) {
  old <- par(mar = c(4.3, 4.6, 1, 1)); on.exit(par(old))
  L <- seq(0, 105, length.out = 200)
  plot(L, basket_output(L), type = "l", lwd = 3, col = "#176B87",
       xlab = "Workers per establishment (L)", ylab = "Baskets per period (Q)",
       xlim = c(0, 115), ylim = c(0, 1320))
  if (stage >= 1) {
    segments(0, 0, 100, 600, lty = 2, col = "#AC501C", lwd = 2)
    points(25, 150, pch = 19, col = "#AC501C")
    text(25, 150, "A: 25 workers, 150 baskets", pos = 4, cex = .85)
    text(65, 300, "Ray slope: Q/L = 6", col = "#AC501C", cex = .9)
  }
  if (stage >= 2) {
    segments(0, 0, 100, 1100, lty = 3, lwd = 2)
    points(100, 1100, pch = 19)
    text(100, 1100, "B: 100 workers, 1,100 baskets", pos = 2, cex = .85)
    text(48, 660, "Ray slope: Q/L = 11", cex = .9)
  }
}
plot_market_map <- function(show_both = FALSE) {
  if (show_both) {
    old <- par(mar = c(0, 0, 0, 0)); on.exit(par(old))
    plot.new(); plot.window(xlim = c(0, 12), ylim = c(0, 6))
    for (row in c(0, 3)) {
      rect(c(2.7, 8.3), row + .3, c(6.1, 11.7), row + 2.6,
           border = "#176B87", lwd = 2)
      text(c(4.4, 10), row + 2.1, c("Market A", "Market B"), font = 2)
      text(c(4.4, 10), row + 1.4, "Demand: 100 units")
    }
    text(1.2, 4.5, "One plant", font = 2)
    text(4.4, 3.7, "Plant: makes 200")
    arrows(6.3, 3.7, 8.1, 3.7, length = .12, lwd = 2, col = "#AC501C")
    text(7.2, 4.4, "Ship 100", cex = .95)
    text(1.2, 1.5, "Two plants", font = 2)
    text(c(4.4, 10), .7, "Plant: makes 100")
    return(invisible(NULL))
  }
  old <- par(mar = c(0, 0, 0, 0)); on.exit(par(old))
  plot.new(); plot.window(xlim = c(0, 10), ylim = c(0, 4))
  rect(c(.4, 6.6), 1.1, c(3.4, 9.6), 3.3, border = "#176B87", lwd = 2)
  text(c(1.9, 8.1), 2.8, c("Market A", "Market B"), font = 2)
  text(c(1.9, 8.1), 2.1, "Demand: 100 units")
  text(1.9, 1.5, "One plant: makes 200")
  arrows(3.6, 1.6, 6.4, 1.6, length = .12, lwd = 2, col = "#AC501C")
  text(5, 2.1, "Ship 100 units", cex = .95)
  text(5, .5, "Alternative: one 100-unit plant in each market; no intermarket freight.", cex = .9)
}
plot_transport_average <- function() {
  old <- par(mfrow = c(1, 2), mar = c(4.3, 4.5, 1, 1)); on.exit(par(old))
  k <- seq(10, 100, length.out = 100)
  plot(k, 20 + 2*k, type = "l", lwd = 3, col = "#176B87",
       xlab = "Distance (miles)", ylab = "Shipping charge (CU/ton)")
  plot(k, 20/k + 2, type = "l", lwd = 3, col = "#AC501C",
       xlab = "Distance (miles)", ylab = "Average charge (CU/ton-mile)")
}
