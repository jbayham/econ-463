from pathlib import Path
import json
import subprocess
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import decks


class DeckPrivacyTests(unittest.TestCase):
    def test_failed_render_preserves_both_decks_and_keeps_temporary_output_private(self):
        with TemporaryDirectory() as tmp, patch.object(decks, "PRIVATE", Path(tmp) / "private"), \
                patch.object(decks, "PUBLIC", Path(tmp) / "public"):
            name = "01-example"
            master, public = decks.PRIVATE / name, decks.PUBLIC / name
            decks.write(master / "slides.qmd", "---\ntitle: Example\n---\n## Question\n")
            decks.write(master / "slides.html", "Last classroom build")
            decks.write(public / "slides.html", "Last student build")
            def fail(command, cwd, check):
                self.assertEqual(cwd, master)
                self.assertEqual(command[2], "slides.qmd")
                output = cwd / command[command.index("--output") + 1]
                self.assertEqual(output.parent, master)
                self.assertNotEqual(output.name, "slides.html")
                output.write_text("Partial render")
                raise subprocess.CalledProcessError(1, command)
            with patch.object(decks.subprocess, "run", side_effect=fail), \
                    self.assertRaises(subprocess.CalledProcessError):
                decks.build(name)
            self.assertEqual((master / "slides.html").read_text(), "Last classroom build")
            self.assertEqual((public / "slides.html").read_text(), "Last student build")
            self.assertEqual(list(master.glob("slide-build-*")), [])

    def test_git_guard_checks_staged_bytes_and_rejects_instructor_files(self):
        with TemporaryDirectory() as tmp, patch.object(decks, "ROOT", Path(tmp)), \
                patch.object(decks, "MANIFEST", Path(tmp) / ".github/slides/student-files.json"), \
                patch.object(decks, "PRIVATE", Path(tmp) / "dev/instructor-slides"):
            root = Path(tmp)
            def git(*args):
                subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)
            git("init", "-q")
            name = "01-example"
            directory = root / "modules" / name
            qmd = "---\ntitle: Example\nformat: revealjs\n---\n## Prompt\n"
            html = '<div class="reveal"><section>Prompt</section></div>'
            decks.write(directory / "slides.qmd", qmd)
            decks.write(directory / "slides.html", html)
            decks.write(decks.MANIFEST, json.dumps({name: {
                "slides.qmd": decks.digest(qmd), "slides.html": decks.digest(html)}}))
            git("add", ".")
            decks.check_index()
            decks.write(directory / "slides.html", html + '<aside class="notes">Answer</aside>')
            git("add", "modules")
            decks.write(directory / "slides.html", html)
            with self.assertRaisesRegex(ValueError, "notes or private comments"):
                decks.check_index()
            git("add", "modules")
            decks.write(decks.PRIVATE / name / "slides.qmd", qmd)
            git("add", "-f", "dev")
            with self.assertRaisesRegex(ValueError, "staged for syncing"):
                decks.check_index()

    def test_source_notes_comments_and_multiline_title(self):
        source = """---
title: Example
title-slide-attributes:
  data-notes: |
    Instructor introduction

    Second paragraph
  class: opening
---
## Question
<!-- Retired answer -->
:::: {.notes}
Instructor answer
::: {.fragment}
More detail
:::
::::
::: {.fragment}
Visible hint
:::
"""
        clean, count = decks.split_source(source)
        self.assertEqual(count, 2)
        self.assertEqual(clean, """---
title: Example
title-slide-attributes:
  class: opening
---
## Question

::: {.fragment}
Visible hint
:::
""")

    def test_public_html_preserves_fragments_footnotes_and_javascript(self):
        visible = '<div class="fragment">Hint</div><aside class="aside-footnotes">Citation</aside>'
        library = '<script>const attribute = "data-notes";</script>'
        html = ('<section data-notes="private">' + visible + '<!--retired-->'
                '<aside class="notes"><aside>private</aside></aside></section>' + library)
        parsed = decks.SlideHTML(html)
        self.assertEqual(parsed.count, 2)
        self.assertEqual(parsed.student(), '<section>' + visible + '</section>' + library)

    def test_pair_detects_visible_drift_and_missing_instructor_notes(self):
        with TemporaryDirectory() as tmp, patch.object(decks, "PRIVATE", Path(tmp) / "private"), \
                patch.object(decks, "PUBLIC", Path(tmp) / "public"):
            name = "01-example"
            master, public = decks.PRIVATE / name, decks.PUBLIC / name
            source = "---\ntitle: Example\n---\n## Prompt\n::: {.notes}\nAnswer\n:::\n"
            clean, _ = decks.split_source(source)
            html = "<section>Prompt</section>"
            hashes = {f: decks.digest(data) for f, data in zip(decks.FILES, (clean, html))}
            for filename, data in [("slides.qmd", source), (".built-from", decks.digest(source))]:
                decks.write(master / filename, data)
            decks.write(public / "slides.qmd", clean)
            decks.write(public / "slides.html", html)
            decks.write(master / "slides.html", html)
            with self.assertRaisesRegex(ValueError, "expected 1 instructor notes"):
                decks.check(name, hashes, False)
            decks.write(master / "slides.html", '<section>Another prompt<aside class="notes">Answer</aside></section>')
            with self.assertRaisesRegex(ValueError, "differ outside notes"):
                decks.check(name, hashes, False)
            with self.assertRaisesRegex(ValueError, "notes or private comments"):
                decks.check_student(name, hashes, clean, html + '<aside class="notes">Answer</aside>')
            with self.assertRaisesRegex(ValueError, "differs from the verified build"):
                decks.check_student(name, hashes, clean, html.replace("Prompt", "Other"))
