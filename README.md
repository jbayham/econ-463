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

The GitHub repository is [jbayham/econ-463](https://github.com/jbayham/econ-463). GitHub Pages uses **Deploy from a branch**, branch **Course-Website**, and folder **/ (root)**, matching the built-in Jekyll setup used by the other course sites.

The course site is [jbayham.github.io/econ-463](https://jbayham.github.io/econ-463/). Push reviewed site changes to `Course-Website` to trigger a Pages build. The `_config.yml` values `url`, `baseurl`, and `githubdir` point to this repository. Local planning, reference, development, and output directories are excluded from the site build.

Keep `LICENSE`, including Steven V. Miller's copyright and MIT permission notice, with the template-derived code. A GitHub fork relationship is not required.

For the recurring check of whether the module slides prepare students for graded problem-set questions, run `python3 .github/assessment/check.py`. The [assessment review procedure](.github/assessment/README.md) explains how to review a new question, record slide evidence, and resolve a gap.

## Teaching and posting slides

Edit `dev/instructor-slides/<module>/slides.qmd`. This local master holds the slide text, speaker notes, and draft comments. For a new deck, use the same module directory name as its public folder under `modules/`. Run these commands from the repository root, omitting the module name to build or check all decks.

```sh
python3 .github/slides/decks.py build 03-measurement
python3 .github/slides/decks.py check 03-measurement
```

The build writes the classroom HTML beside the master. It produces the student HTML by removing speaker notes from that same render, and it writes a student Quarto source with notes and draft comments removed. The Modules page links to `modules/<module>/slides.html`. The parity check compares the complete HTML and source of each pair and checks that the instructor render retained the source’s note blocks.

For class, serve the instructor directory on this computer:

```sh
python3 -m http.server 4464 --bind 127.0.0.1 --directory dev/instructor-slides
```

Open [the classroom deck list](http://127.0.0.1:4464/), select a module, and press **S** for the speaker view. Project the slide window and keep the speaker window on your display.

Git ignores `dev/` and Jekyll excludes it from the website. A fresh clone contains only student versions. Enable the staged-file check in each checkout with `git config --local core.hooksPath .github/hooks`. It checks the files a commit would actually sync, including a force-added instructor file. GitHub Actions runs the same public-file check. To verify downloaded student files without the local masters, run `python3 .github/slides/decks.py check-public` in a clone.
