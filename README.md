# ECON 463 Course Website

Jekyll course scaffold using Steve Miller's [course website template](https://github.com/svmiller/course-website).

- `_config.yml`: course title, description, site address, optional `githubdir`, and optional `canvas_url`.
- `_data/schedule.yml`: class dates, topics, and readings. The list is empty; a commented example preserves the format.
- `_data/modules.yml`: module descriptions and links to readings, problem sets, and additional materials. The list is empty; a commented example preserves the format.
- `modules/`: add new module folders and teaching materials here. Shared Quarto settings and PDF styling are retained.
- `syllabus/`: copied syllabus files are unchanged and still need review for the new course.
- `course-materials.md` and `model_lab.md`: empty page scaffolds.
- `_layouts/`, `_includes/`, `_sass/`, and `_css/`: shared layout and styling.

On this computer, run `serve463` in a new Bash or Zsh terminal to build and preview at `http://127.0.0.1:4463/econ-463/`. The command opens the browser and rebuilds when files change; refresh the browser to see updates. Press Ctrl+C to stop.

Alternatively, run `bundle exec jekyll serve --port=4463 --open-url`; build without serving with `bundle exec jekyll build`.

The copied Git history and remotes have been removed. To start a new local repository:

```sh
git init -b main
git add .
git commit -m "Initialize ECON 463 course site"
```

Create an empty GitHub repository, connect it as `origin`, and push `main`. For a repository named `econ-463` under `jbayham`, the current `url` and `baseurl` settings are ready for GitHub Pages. If the repository name or owner differs, update `_config.yml` accordingly. Set `githubdir` to the new `owner/repository` to show the repository link in the footer.

In GitHub Settings → Pages, select **Deploy from a branch**, branch **main**, and folder **/ (root)**. GitHub Pages will build the Jekyll site.

Keep `LICENSE`, including Steven V. Miller's copyright and MIT permission notice, with the template-derived code. A GitHub fork relationship is not required.
