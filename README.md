# ECON 463 Course Website

Jekyll course scaffold using Steve Miller's [course website template](https://github.com/svmiller/course-website).

- `_config.yml`: course title, description, site address, optional `githubdir`, and optional `canvas_url`.
- `_data/schedule.yml`: class dates, topics, and readings. The list is empty; a commented example preserves the format.
- `_data/modules.yml`: module descriptions and links to readings, problem sets, and additional materials. The list is empty; a commented example preserves the format.
- `modules/`: add new module folders and teaching materials here. Shared Quarto settings and PDF styling are retained.
- `syllabus/`: regional economics syllabus draft in Markdown/PDF. The existing Excel workbook retains its older sheets and contains the current calendar in `ECON463_2026`; `schedule_convert.R` reads that sheet. Grading weights, meeting logistics, and course policies still need instructor review.
- `course-materials.md` and `model_lab.md`: empty page scaffolds.
- `_layouts/`, `_includes/`, `_sass/`, and `_css/`: shared layout and styling.

On this computer, run `serve463` in a new Bash or Zsh terminal to build and preview at `http://127.0.0.1:4463/econ-463/`. The command opens the browser and rebuilds when files change; refresh the browser to see updates. Press Ctrl+C to stop.

Alternatively, run `bundle exec jekyll serve --port=4463 --open-url`; build without serving with `bundle exec jekyll build`.

The GitHub repository is [jbayham/econ-463](https://github.com/jbayham/econ-463). GitHub Pages uses **Deploy from a branch**, branch **module-1**, and folder **/ (root)**, matching the built-in Jekyll setup used by the other course sites.

The course site is [jbayham.github.io/econ-463](https://jbayham.github.io/econ-463/). Push reviewed site changes to `module-1` to trigger a Pages build. The `_config.yml` values `url`, `baseurl`, and `githubdir` point to this repository. Local planning, reference, development, and output directories are excluded from the site build.

Keep `LICENSE`, including Steven V. Miller's copyright and MIT permission notice, with the template-derived code. A GitHub fork relationship is not required.
