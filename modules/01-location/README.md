# Module 1: Location, Cities, and Agglomeration

Explore how natural advantages, transport costs, scale economies, and agglomeration shape the location of economic activity.

## Materials

- [Reader (HTML)](reader.html) or [reader (PDF)](reader.pdf): explanations, worked examples, practice questions, and a reading guide.
- [Course introduction and syllabus](../00-course-introduction/slides.html): opening deck, including instructor introduction placeholders.
- [Lecture slides](slides.html): class discussion, calculations, and optional practice.
- Optional EPUB: `module-01-location-reader.epub`.

The examples compare three plant locations, one plant versus two plants, and the mechanisms behind a hypothetical industrial cluster. All numerical data are synthetic; monetary amounts use illustrative currency units (CU).

## Work through the examples

Read each setup, predict the result, and try the calculation before consulting the worked answer. Explain the mechanism and identify an assumption that could change your conclusion. The exercises are ungraded practice.

Day 1 requires no advance reading, coding, or software setup. Use paper and optionally a calculator. The basket story introduces specialization; the plant example first compares production costs, then adds freight. Practice changing fixed cost to 600 CU and shipping to 8 CU per unit before checking the reader's answer.

## Teaching sequence

November 23 has 120 working minutes: separate opening deck 35 (instructor introduction 5, overview 10, syllabus 20), foundations 10, location baseline 15, transport change 15, scale and city formation 25, paired hand calculations 20. Take the 10-minute break after the location baseline. Stop after the paired exercise; no midpoint recap. November 24 has no class; the required readings provide follow-up between meetings.

November 25 uses 60 minutes: agglomeration 30, limits 20, closing summary/retrieval/Module 2 bridge 10. The optional retail and doubled-demand slides have no scheduled time. Introduce all course learning outcomes only in the separate course-introduction deck; omit outcome lists from module decks.

## Authoring and rendering

`R/examples.R` and `data/location-costs.csv` are internal shared calculation and figure inputs. Students do not run these for Module 1. The shared bibliography is `../references.bib`.

From the repository root:

```sh
quarto render modules/01-location/slides.qmd --to revealjs
quarto render modules/01-location/reader.qmd --to html
quarto render modules/01-location/reader.qmd --to pdf
quarto render modules/01-location/reader.qmd --to epub
```

Rendered files stay beside their sources. The basket figure advances on a click in the slides and appears complete in the reader. MathJax remains configured for this deck; adopting it as course-wide policy still awaits instructor approval.

## Readings

Required: Hoover–Giarratani, Chapter 1, pp. 12–15, and Chapter 2, §§2.3–2.7, pp. 19–35, for regional framing, resource endowments, and location choice; Brueckner, *Lectures on Urban Economics*, Chapter 1, §§1.1–1.5, pp. 1–18, for scale, agglomeration, and transport connections. These are follow-up readings, not Day 1 prerequisites. Hoover–Giarratani Chapter 5 and Brueckner §1.6 remain supplemental; Glaeser–Gottlieb remains optional advanced background, and the World Bank illustration is optional.

Use the reader's reading guide for section and page references. The PDF reader can be used offline.

## Verification

Verified November 21: Reveal.js HTML and reader HTML/PDF/EPUB rendered successfully. Checked all 45 slides and 28 PDF pages visually; enlarged the staged production figure and improved equation/bibliography page breaks. Verified A-to-B reveal on one keypress. MathJax produced 29 SVG expressions with no errors. Reader HTML: 31 navigation links, no broken internal anchors, six loaded figures with descriptions, and no displayed code blocks. EPUB archive/XHTML and manifest resources passed structural checks; no displayed code blocks. Independently checked baseline and reduced-freight location costs, both decision thresholds, production-only and freight-inclusive plant costs, the revised practice result, and basket totals. The existing regional/urban comparison remains intentionally scrollable. Native e-reader display and classroom pacing remain instructor review items.

Graded Module 1 A1/PS1 questions remain a separate outstanding task.
