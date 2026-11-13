# ECON 463 Course Website

Jekyll course scaffold using Steve Miller's [course website template](https://github.com/svmiller/course-website).

- `_config.yml`: course title, description, site address, optional `githubdir`, and optional `canvas_url`.
- `schedule.md`: edit the published course schedule table directly here. No Excel, R, or YAML conversion is needed.
- `_data/modules.yml`: module descriptions and links to available readings and teaching materials. Add resources as each module is developed.
- `modules/`: add new module folders and teaching materials here. Shared Quarto settings and PDF styling are retained.
- `syllabus/`: regional economics syllabus in Markdown/PDF. The Excel workbook is retained as a historical reference and no longer drives the website. The retired conversion script is archived locally in `dev/legacy-schedule/`.
- `course-materials.md`: course-materials scaffold. `model_lab.md` supplies the Problem Sets page at `/problem-sets/`.
- `_layouts/`, `_includes/`, `_sass/`, and `_css/`: shared layout and styling.

On this computer, run `serve463` in a new Bash or Zsh terminal to build and preview at `http://127.0.0.1:4463/econ-463/`. The command opens the browser and rebuilds when files change; refresh the browser to see updates. Press Ctrl+C to stop.

Alternatively, run `bundle exec jekyll serve --port=4463 --open-url`; build without serving with `bundle exec jekyll build`.

The GitHub repository is [jbayham/econ-463](https://github.com/jbayham/econ-463). GitHub Pages uses **Deploy from a branch**, branch **module-1**, and folder **/ (root)**, matching the built-in Jekyll setup used by the other course sites.

The course site is [jbayham.github.io/econ-463](https://jbayham.github.io/econ-463/). Push reviewed site changes to `module-1` to trigger a Pages build. The `_config.yml` values `url`, `baseurl`, and `githubdir` point to this repository. Local planning, reference, development, and output directories are excluded from the site build.

Keep `LICENSE`, including Steven V. Miller's copyright and MIT permission notice, with the template-derived code. A GitHub fork relationship is not required.
