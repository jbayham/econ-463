---
layout: page
title: "Course Schedule"
permalink: /schedule/
course_year: 2026
---

November 23–December 18, 2026. Both sections follow the same schedule. There is **no class on November 24** or on weekends. See the [syllabus]({{ site.baseurl }}/syllabus/) for meeting times and rooms.

This schedule is tentative. Problem Sets 1–3 are due at the **end of class** on the listed Mondays. The shortened Problem Set 4 is due at the **end of the final exam**. Changes will be announced in class.

<!-- Edit this table directly. No spreadsheet or conversion step is required. -->

<div class="schedule-table" markdown="1">

| Date | Course milestone | Due |
| --- | --- | --- |
| Mon Nov 23 | Course begins | |
| Tue Nov 24 | No class | |
| Mon Nov 30 | | **PS 1** |
| Fri Dec 4 | Full-session review for Exam 1 (M1–M5) | |
| Mon Dec 7 | **Exam 1 (M1–M5)** | **PS 2** |
| Mon Dec 14 | | **PS 3** |
| Thu Dec 17 | Final review | |
| Fri Dec 18 | **Final exam (M6–M8)** | **PS 4 (shortened)** |
{: #course-schedule }

</div>

## Module topics and readings

| Module | Topics | Authors and chapters |
| --- | --- | --- |
| 1. Location | Firm location, transport costs, scale economies, and agglomeration | Hoover and Giarratani, Chapters 1 and 2 · Brueckner, Chapter 1 |
| 2. Growth | Structural change, market access, trade, migration, and spillovers | Hoover and Giarratani, Chapter 11 |
| 3. Measurement | Regional boundaries, comparable data, location quotients, and shift-share | Schaffer, Chapter 2 |
| 4. Spatial equilibrium | Bid rents, housing supply, wages, and mobility | Brueckner, Chapters 2 and 11 |
| 5. Hedonics | Capitalization, sorting, regression specifications, and interpretation | Brueckner, Chapter 6 · Lawson, Chapter 5 in Hall, Lawson, and Shia |
| 6. Input-output analysis | Accounts, technical coefficients, multipliers, leakages, and sensitivity | Schaffer, Chapters 4–6 · Hewings, Chapter 4 |
| 7. CGE | Social accounting, baseline replication, closure, counterfactuals, and factor mobility | Hewings, Chapter 7 |
| 8. Policy evaluation | Model comparison, opportunity cost, welfare, externalities, and distribution | Hoover and Giarratani, Chapter 12 |

For reading assignments and handouts, see the [module materials]({{ site.baseurl }}/modules/). The [syllabus]({{ site.baseurl }}/syllabus/#materials-and-reading) lists the books and links to them.

<script>
  (function () {
    var table = document.getElementById('course-schedule');
    if (!table) return;
    var year = {{ page.course_year | jsonify }};
    var months = { Jan: '01', Feb: '02', Mar: '03', Apr: '04', May: '05', Jun: '06',
      Jul: '07', Aug: '08', Sep: '09', Oct: '10', Nov: '11', Dec: '12' };
    var parts = new Intl.DateTimeFormat('en-US', {
      timeZone: 'Asia/Ho_Chi_Minh', year: 'numeric', month: '2-digit', day: '2-digit'
    }).formatToParts(new Date());
    var date = {};
    parts.forEach(function (part) { date[part.type] = part.value; });
    var today = date.year + '-' + date.month + '-' + date.day;
    var nextClassFound = false;
    table.querySelectorAll('tbody tr').forEach(function (row) {
      var match = row.cells[0].textContent.match(/\b([A-Z][a-z]{2})\s+(\d{1,2})\s*$/);
      if (!match || !months[match[1]]) return;
      var classDate = year + '-' + months[match[1]] + '-' + match[2].padStart(2, '0');
      var topic = row.cells[1].textContent.trim().toLowerCase();
      var noClass = topic.indexOf('no class') === 0;
      row.dataset.date = classDate;
      row.classList.toggle('noclass-row', noClass);
      row.classList.toggle('exam-row', /^(exam\s+\d|final exam)/.test(topic));
      row.classList.toggle('past-day', classDate < today);
      var nextClass = !nextClassFound && classDate >= today && !noClass;
      row.classList.toggle('next-class', nextClass);
      if (nextClass) nextClassFound = true;
    });
  })();
</script>
