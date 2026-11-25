---
layout: page
title: "Course Schedule"
permalink: /schedule/
course_year: 2026
---


This schedule is tentative. Additional handouts will accompany the relevant module. All Problem Sets are due at the **beginning of class** on the listed due date.

<!-- Edit this table directly. No spreadsheet or conversion step is required. -->

<div id="course-schedule" class="schedule-table" markdown="1">

| Date       | Topics                                                                                                                                           | Reading                                            | Due                                                                 |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------- | ------------------------------------------------------------------- |
| Mon Nov 23 | Course introduction. **[M1]:** Firm location, natural advantages, transportation costs, scale economies, and agglomeration.                      | Brueckner ch. 1 and §11.1.                         |                                                                     |
| Tue Nov 24 | **No class.**                                                                                                                                    | —                                                  |                                                                     |
| Wed Nov 25 | **[M2]:** Regional growth and structural change, trade, migration, and convergence.                                                              | Hoover–Giarratani §11.2.                           |                                                                     |
| Thu Nov 26 | **[M2]**; **[M3]:** Regional boundaries, comparable data, location quotients, and shift-share analysis.                                          | Hoover–Giarratani §§11.5–11.6.                     |                                                                     |
| Fri Nov 27 | **[M3]**;                                                                                                                                        | Schaffer ch. 2 and Note A.                         |                                                                     |
| Mon Nov 30 | **[M4]:** Land use, commuting and bid rents, wages and rents across cities.                                                                      | Brueckner ch. 2 and §11.2.                         | **[Problem Set 1]({{ site.baseurl }}/problem-sets/#problem-set-1)** |
| Tue Dec 1  | **[Problem set review (PS 1)]({{ site.baseurl }}/problem-sets/#problem-set-1).** **[M5]:** Hedonic regressions, amenity capitalization, sorting. | Brueckner §6.2.                                    |                                                                     |
| Wed Dec 2  | **[M5]**                                                                                                                                         | Hall, Lawson, and Shia, ch. 5.                     |                                                                     |
| Thu Dec 3  | **[M4]**; **[M5]**                                                                                                                               | [M4]–[M5] notes and the supplied hedonic exercise. |                                                                     |
| Fri Dec 4  | **Full-session review for Exam 1 ([M1]–[M5]).**                                                                                                  | Review [M1]–[M5].                                  |                                                                     |
| Mon Dec 7  | **Exam 1: Regional foundations, spatial equilibrium, and hedonics ([M1]–[M5]).**                                                                 |                                                    | **Problem Set 2**                                                   |
| Tue Dec 8  | **Problem set review (PS 2).** **[M6]:** Input-output accounting, the Leontief model, and regional multipliers.                                  | Schaffer ch. 4–5.                                  |                                                                     |
| Wed Dec 9  | **[M6]**                                                                                                                                         | Schaffer ch. 6; supplied IO exercise.              |                                                                     |
| Thu Dec 10 | **[M6]**; **[M7]:** Regional CGE modeling, social accounting, market adjustment and closure, and counterfactual comparisons with IO.             | Hewings §§4.1 and 7.2.                             |                                                                     |
| Fri Dec 11 | **[M7]**: Regional CGE                                                                                                                           |                                                    |                                                                     |
| Mon Dec 14 | **[M7]**: Regional CGE                                                                                                                           |                                                    | **Problem Set 3**                                                   |
| Tue Dec 15 | **Problem set review (PS 3).** **[M7]**                                                                                                          |                                                    |                                                                     |
| Wed Dec 16 | **[M7]**; **[M8]:** Regional policy evaluation, counterfactuals, opportunity costs, externalities, and distribution.                             | Hoover–Giarratani §12.2                            |                                                                     |
| Thu Dec 17 | **[M8]**. Final-exam review.                                                                                                                     |                                                    | **Problem Set 4**                                                   |
| Fri Dec 18 | **Final exam: [M1]–[M8] (Cumulative)**                                                                                                           |                                                    |                                                                     |

</div>

[M1]: {{ site.baseurl }}/modules/#module-1
[M2]: {{ site.baseurl }}/modules/#module-2
[M3]: {{ site.baseurl }}/modules/#module-3
[M4]: {{ site.baseurl }}/modules/#module-4
[M5]: {{ site.baseurl }}/modules/#module-5
[M6]: {{ site.baseurl }}/modules/#module-6
[M7]: {{ site.baseurl }}/modules/#module-7
[M8]: {{ site.baseurl }}/modules/#module-8

Full citations and online links appear in the [syllabus]({{ site.baseurl }}/syllabus/#materials-and-reading).

<script>
  (function () {
    var table = document.querySelector('#course-schedule table');
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
