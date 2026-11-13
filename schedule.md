---
layout: page
title: "Course Schedule"
permalink: /schedule/
course_year: 2026
---

November 23–December 18, 2026. Both sections follow the same schedule. There is **no class on November 24** or on weekends. See the [syllabus]({{ site.baseurl }}/syllabus/) for meeting times and rooms.

This schedule is tentative. Readings are selected excerpts; additional handouts will accompany the relevant module. Problem set submissions are due at the **end of class** on the listed dates. Changes will be announced in class.

<!-- Edit this table directly. No spreadsheet or conversion step is required. -->

<div class="schedule-table" markdown="1">

| Date | Topics | Reading | Due |
| --- | --- | --- | --- |
| Mon Nov 23 | **M1:** Regions, city formation, natural advantages, transportation costs, and scale economies. Course introduction, syllabus discussion, worked examples, and R access check. | No advance reading. [M1 reader]({{ site.baseurl }}/modules/01-location/reader.html) for follow-up. |  |
| Tue Nov 24 | **No class.** | — |  |
| Wed Nov 25 | **M1:** Agglomeration, clusters, and specialization; **M2:** Regional growth and structural change. | M1 reader; [M2 reader]({{ site.baseurl }}/modules/02-growth/reader.html). Hoover–Giarratani §11.2, pp. 223–224. |  |
| Thu Nov 26 | **M2:** Market access, trade, migration, and spillovers; **M3:** Regional boundaries and data comparability. | M2 reader; Hoover–Giarratani §§11.5–11.6, pp. 234–239. |  |
| Fri Nov 27 | **M3:** Location quotients and shift-share; **M4:** Commuting costs and bid rents. | Schaffer ch. 2, pp. 6–9; Note A, pp. 43–47 (selected excerpts). | **PS 1 checkpoint** |
| Mon Nov 30 | **M4:** Housing supply, land-use constraints, spatial equilibrium, mobility, and capitalization. | Brueckner ch. 2 and §11.2 (selected diagrams and mechanisms). | **PS 1 final submission** |
| Tue Dec 1 | **M5:** Hedonics, amenities, and property values. | Brueckner §6.2, pp. 116–119; supplied hedonic exercise. |  |
| Wed Dec 2 | **M5:** Sorting, omitted variables, specification comparisons, and limits to causal and welfare interpretation. | Hall, Lawson, and Shia, ch. 5, pp. 65–75 (selected specification and results). | **PS 2 final submission** |
| Thu Dec 3 | **M4:** Spatial-equilibrium consolidation; **M5:** Hedonics consolidation; Exam 1 review (M1–M5). | Review M1–M5 notes, worked examples, and PS 1–PS 2 feedback. |  |
| Fri Dec 4 | **Exam 1: Regional foundations, spatial equilibrium, and hedonics (M1–M5).** |  |  |
| Mon Dec 7 | **M6:** IO accounting, technical coefficients, final demand, and the Leontief inverse. | Schaffer chs. 4–5, pp. 48–62 (selected excerpts). |  |
| Tue Dec 8 | **M6:** Multipliers, imports and leakages, household spending, and output/value-added distinctions. | Schaffer ch. 6, pp. 63–69; multiplier appendix as needed. |  |
| Wed Dec 9 | **M6:** Model interpretation and limitations. | Hewings §4.1, pp. 28–30; supplied IO exercise. | **PS 3 final submission** |
| Thu Dec 10 | **M6:** Input-output assumptions and limitations; **M7:** Resource constraints, price adjustment, and behavioral responses. | Hewings §7.2, pp. 52–54; supplied accounting notes. |  |
| Fri Dec 11 | **M7:** Social accounting, production, households, budgets, and market clearing. **Regular teaching day.** | Supplied CGE model guide and accounting handout (forthcoming). |  |
| Mon Dec 14 | **M7:** Baseline replication, closure, factor markets, and regional trade. | Supplied baseline and closure notes (forthcoming). |  |
| Tue Dec 15 | **M7:** Counterfactuals, substitution, constraints, and factor mobility. | Supplied counterfactual and model-comparison exercise (forthcoming). | **PS 4 checkpoint:** baseline, scenario output, and mechanism explanation. |
| Wed Dec 16 | **M7:** Sensitivity analysis; **M8:** Policy interpretation, opportunity costs, welfare, externalities, and distribution. | Hoover–Giarratani §12.2, pp. 250–255 (selected excerpt); supplied sensitivity exercise. | **PS 4 final submission** |
| Thu Dec 17 | **M8:** Policy synthesis, model comparison, and final-exam review. | Review IO/CGE notes, worked examples, and PS 3–PS 4 feedback. |  |
| Fri Dec 18 | **Final exam: IO, CGE, and policy interpretation (M6–M8).** |  |  |
{: #course-schedule }

</div>

Book page references use the printed pages in the course editions. Full citations and online links appear in the [syllabus]({{ site.baseurl }}/syllabus/#materials-and-reading). Module readers and handouts provide guidance on the selected passages.

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
