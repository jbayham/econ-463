# Axes are 100 times River/Harbor log ratios. Lines are the exact log equations.
rent_wage_plot <- function(worker = TRUE, firm = TRUE, a = 0, b = 0,
                          preference_regions = character(), case_rent = NULL,
                          case_step = "start") {
  s <- 0.25
  t <- 0.20
  worker_color <- "#126479"
  firm_color <- "#9B431A"
  ink <- "#172F3B"
  rent_ticks <- if (is.null(case_rent)) seq(-4, 12, 4) else seq(-12, 12, 4)
  x <- seq(min(rent_ticks), 13, length.out = 200)
  worker_wage <- function(x) s * x - a
  firm_wage <- function(x) (b - t * x) / (1 - t)
  par(mar = c(3.6, 4.0, 0.45, 0.35), mgp = c(2.25, 0.65, 0),
      family = "sans", fg = ink, col.lab = ink, col.axis = ink, las = 1,
      lend = "round", xaxs = "i", yaxs = "i")
  plot.new()
  plot.window(xlim = c(min(rent_ticks) - 0.5, if (is.null(case_rent)) 18 else 20),
              ylim = c(-4.2, 6.6))
  if (length(preference_regions)) {
    bounds <- par("usr")
    edges <- bounds[1:2]
    for (region in preference_regions) {
      lower <- region == "Harbor"
      edge_y <- if (lower) bounds[3] else bounds[4]
      fill <- if (lower) "#F7E8D7" else "#D6EBEA"
      polygon(c(edges, rev(edges)), c(worker_wage(edges), edge_y, edge_y),
              col = fill, border = NA)
    }
  }
  abline(h = seq(-4, 6, 2), col = "#E4EAEC", lwd = 0.9)
  abline(h = 0, v = 0, col = "#9AA9AD", lwd = 1.1)
  axis(1, at = rent_ticks, cex.axis = 1.35)
  axis(2, at = seq(-4, 6, 2), cex.axis = 1.35)
  title(xlab = "River rent gap, x (log points)", ylab = "River wage gap, y (log points)",
        cex.lab = 1.46)
  if (a != 0) lines(x, s * x, col = worker_color, lty = 2, lwd = 2)
  if (b != 0) lines(x, -t * x / (1 - t), col = firm_color, lty = 2, lwd = 2)
  if (length(preference_regions)) {
    lines(edges, worker_wage(edges), col = worker_color, lwd = 3)
    if ("River" %in% preference_regions)
      text(2.5, 4.7, "Prefer River", col = ink, font = 2, cex = 1.65)
    if ("Harbor" %in% preference_regions)
      text(9.5, -2.0, "Prefer Harbor", col = ink, font = 2, cex = 1.65)
    text(12.8, worker_wage(12.8) - 0.8, "Equal utility", col = worker_color, cex = 1.25)
  } else if (worker) {
    lines(x, worker_wage(x), col = worker_color, lwd = 3)
    text(13.05, worker_wage(13), "Workers", pos = 4, cex = 1.43, col = worker_color)
  }
  if (firm) {
    lines(x, firm_wage(x), col = firm_color, lwd = 3)
    text(13.05, firm_wage(13), "Firms", pos = 4, cex = 1.43, col = firm_color)
  }
  if (worker && firm) {
    points(0, 0, pch = 21, bg = "white", col = ink, lwd = 2, cex = 1.5)
    text(0, 0, expression(E[0]), pos = 1, offset = 0.8, cex = 1.45)
    if (a != 0 || b != 0) {
      new_rent <- (b + (1 - t) * a) / (t + (1 - t) * s)
      new_wage <- worker_wage(new_rent)
      segments(new_rent, 0, new_rent, new_wage, col = "#62777C", lty = 3)
      points(new_rent, new_wage, pch = 19, col = ink, cex = 1.4)
      text(new_rent, new_wage, expression(E[1]), pos = if (a != 0) 1 else 3,
           offset = 0.7, cex = 1.45)
    }
  }
  if (!is.null(case_rent)) {
    start_wage <- worker_wage(case_rent)
    mark <- "#63488B"
    segments(case_rent, start_wage, case_rent, firm_wage(case_rent),
             col = "#697980", lty = 3, lwd = 1.5)
    if (case_step %in% c("wage", "rent"))
      arrows(case_rent, start_wage, case_rent, 0, length = 0.12,
             angle = 27, lwd = 3, col = mark)
    if (case_step == "rent")
      arrows(case_rent, 0, case_rent / 2, 0, length = 0.12,
             angle = 27, lwd = 3, col = mark)
    points(case_rent, start_wage, pch = 21, bg = mark, col = "white", cex = 1.8)
    text(case_rent, start_wage, sprintf("(%g, %g)", case_rent, start_wage),
         pos = if (case_rent > 0) 3 else 1, offset = 0.65,
         cex = 1.35, font = 2, col = mark)
  }
}
