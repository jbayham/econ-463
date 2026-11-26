"""Build and check the private classroom and public student Reveal decks."""
import argparse
import hashlib
from html import escape
from html.parser import HTMLParser
import fcntl
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
PUBLIC = ROOT / "modules"
PRIVATE = ROOT / "dev/instructor-slides"
MANIFEST = Path(__file__).with_name("student-files.json")
FILES = ("slides.qmd", "slides.html")
COMMENTS = re.compile(r"<!--.*?-->", re.S)
DIV = re.compile(r"^ {0,3}(:{3,})[ \t]*(.*?)[ \t]*$")
NOTE_CLASS = re.compile(r"(?:^|[\s{])\.notes(?=[\s}]|$)")
NOTE_ATTR = re.compile(r"""\s+data-notes\s*=\s*(?:"[^"]*"|'[^']*'|[^\s>]+)""", re.I)


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def write(path, text):
    """Replace a complete file only after its new contents exist."""
    if path.is_file() and path.read_text() == text:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", dir=path.parent, delete=False) as tmp:
        tmp.write(text)
    os.chmod(tmp.name, 0o644)
    os.replace(tmp.name, path)


def split_source(source):
    # Comments can contain entire retired slides, including nested note blocks.
    src = COMMENTS.sub("", source)
    if "<!--" in src:
        raise ValueError("Unclosed slide source comment")
    # Remove title notes, including YAML block scalars and their continuation lines.
    header, separator, body = src.removeprefix("---\n").partition("\n---\n")
    if not separator:
        raise ValueError("Missing Quarto front matter")
    title_note = r"(?m)^(?P<pad> *)data-notes:[^\n]*(?:\n(?:(?P=pad) +[^\n]*|[ \t]*(?=\n)))*\n?"
    header, count = re.subn(title_note, "", header + "\n")
    header = re.sub(r"(?m)^( *)title-slide-attributes: *\n(?!\1 +\S)", "", header).rstrip("\n")

    visible = []
    depth = 0
    code = None
    for line in body.splitlines(keepends=True):
        fence = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if code is not None:
            if fence and fence[1][0] == code[0] and len(fence[1]) >= len(code) and not fence[2].strip():
                code = None
        elif fence:
            code = fence[1]
        else:
            div = DIV.fullmatch(line.rstrip("\r\n"))
            if div and (depth or div[2] == "notes" or NOTE_CLASS.search(div[2])):
                if depth == 0:
                    count += 1
                depth += 1 if div[2] else -1
                continue
        if not depth:
            visible.append(line)
    if depth:
        raise ValueError("Unclosed speaker-note div in source")
    clean = "---\n" + header + separator + "".join(visible)
    if re.search(r"(?im)(?:\bdata-notes\s*[:=]|class\s*=\s*[\"'][^\"']*\bnotes\b|^\s*:{3,}[^\n]*\.notes\b|^\s*::: *notes\b)", clean):
        raise ValueError("Unsupported speaker-note markup in the public source; use ::: {.notes}")
    if clean != source:
        clean = clean.rstrip("\n") + "\n"
    return clean, count


class SlideHTML(HTMLParser):
    """Remove only actual note markup, preserving all other HTML byte for byte."""
    def __init__(self, source):
        super().__init__(convert_charrefs=False)
        self.source = source
        self.lines = [0] + [m.end() for m in re.finditer("\n", source)]
        self.cuts = []
        self.comments = []
        self.note_tag = None
        self.depth = 0
        self.count = 0
        self.feed(source)
        self.close()
        if self.note_tag:
            raise ValueError("Unclosed speaker-note element in HTML")

    def source_index(self):
        row, col = self.getpos()
        return self.lines[row - 1] + col

    def handle_starttag(self, tag, attrs):
        if self.note_tag:
            self.depth += tag == self.note_tag
            return
        attrs = dict(attrs)
        if "notes" in (attrs.get("class") or "").split():
            self.note_tag, self.start, self.depth = tag, self.source_index(), 1
            self.count += 1
        elif "data-notes" in attrs:
            pos = self.source_index()
            matches = list(NOTE_ATTR.finditer(self.get_starttag_text()))
            if len(matches) != 1:
                raise ValueError("Ambiguous data-notes attribute")
            self.cuts.append((pos + matches[0].start(), pos + matches[0].end()))
            self.count += 1
        if attrs.get("id") in {"quarto-embedded-source-code", "quarto-code-full-source"}:
            raise ValueError("Disable embedded Quarto source before sharing the slides")

    def handle_endtag(self, tag):
        if self.note_tag == tag:
            self.depth -= 1
            if not self.depth:
                self.cuts.append((self.start, self.source.index(">", self.source_index()) + 1))
                self.note_tag = None

    def handle_comment(self, text):
        if not self.note_tag and text.strip() != "reveal.js plugins":
            start = self.source_index()
            self.comments.append((start, start + len(text) + 7))

    def without(self, spans):
        parts = []
        end = 0
        for a, b in sorted(spans):
            parts.append(self.source[end:a])
            end = b
        return "".join(parts) + self.source[end:]

    def student(self):
        return self.without(self.cuts + self.comments)


def resources():
    """Make the same themes, inputs and relative classroom links work in both trees."""
    PRIVATE.mkdir(parents=True, exist_ok=True)
    def link(src, dest):
        if dest.is_symlink() and dest.resolve() == src.resolve():
            return
        if dest.exists() or dest.is_symlink():
            raise ValueError(f"Private resource path already occupied: {dest}")
        dest.symlink_to(os.path.relpath(src, dest.parent), target_is_directory=src.is_dir())
    for name in ("_quarto.yml", "references.bib", "styles"):
        link(PUBLIC / name, PRIVATE / name)
    for directory in sorted(PUBLIC.glob("[0-9][0-9]-*")):
        mirror = PRIVATE / directory.name
        mirror.mkdir(exist_ok=True)
        for src in directory.iterdir():
            if src.name in {"assets", "R", "data", "_metadata.yml"} or (
                src.is_file() and src.suffix in {".pdf", ".html", ".xlsx", ".csv", ".epub"}
                and src.name != "slides.html" and not src.name.startswith(("~", "."))
            ):
                link(src, mirror / src.name)


def build(name):
    master, target = PRIVATE / name, PUBLIC / name
    source = (master / FILES[0]).read_text()
    qmd, expected_notes = split_source(source)
    # Quarto can leave a partial HTML file if an embedded resource fails to download.
    # Give it a temporary output so a failed render also preserves the last classroom deck.
    with tempfile.NamedTemporaryFile(dir=master, prefix="slide-build-", suffix=".html") as rendered:
        output = Path(rendered.name)
        subprocess.run(["quarto", "render", FILES[0], "--to", "revealjs",
                        "--output", output.name], cwd=master, check=True)
        html = SlideHTML(output.read_text())
    if source != (master / FILES[0]).read_text():
        raise ValueError(f"{name}: source changed during rendering; rerun build")
    if html.count != expected_notes:
        raise ValueError(f"{name}: expected {expected_notes} instructor notes, found {html.count}")
    # Retired slide drafts are comments, not presenter notes. Omit them from both HTMLs.
    write(master / FILES[1], html.without(html.comments))
    write(target / FILES[0], qmd)
    write(target / FILES[1], html.student())
    write(master / ".built-from", digest(source))
    return {f: digest((target / f).read_text()) for f in FILES}


def check_student(name, hashes, qmd, html):
    if split_source(qmd)[0] != qmd or SlideHTML(html).student() != html:
        raise ValueError(f"{name}: notes or private comments in a student file")
    for filename, text in zip(FILES, (qmd, html)):
        if hashes.get(filename) != digest(text):
            raise ValueError(f"{name}/{filename}: student content differs from the verified build")

def check_pair(name, qmd, html):
    master = PRIVATE / name
    original = (master / FILES[0]).read_text()
    classroom = SlideHTML((master / FILES[1]).read_text())
    clean, expected_notes = split_source(original)
    if classroom.count != expected_notes:
        raise ValueError(f"{name}: expected {expected_notes} instructor notes, found {classroom.count}")
    if clean != qmd or classroom.comments or classroom.student() != html:
        raise ValueError(f"{name}: the instructor and student versions differ outside notes")
    if (master / ".built-from").read_text() != digest(original):
        raise ValueError(f"{name}: the instructor source has changed; rebuild the pair")
    print(f"{name}: same content, {classroom.count} instructor note containers/attributes")


def check(name, hashes, public_only):
    qmd, html = ((PUBLIC / name / f).read_text() for f in FILES)
    check_student(name, hashes, qmd, html)
    if not public_only:
        check_pair(name, qmd, html)


def classroom_index():
    links = []
    for slide in sorted(PRIVATE.glob("[0-9][0-9]-*/slides.html")):
        title = re.search(r"^title:\s*(.+)$", slide.with_suffix(".qmd").read_text(), re.M)
        label = title[1].strip("\"'") if title else slide.parent.name
        links.append(f'<li><a href="{escape(slide.relative_to(PRIVATE).as_posix())}">{escape(label)}</a></li>')
    write(PRIVATE / "index.html", """<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>ECON 463 classroom slides</title>
<style>body{font:1.2rem/1.6 system-ui;max-width:46rem;margin:4rem auto;padding:0 1.5rem}li{margin:.7rem 0}</style>
<h1>ECON 463 classroom slides</h1>
<p>Open a deck and press <kbd>S</kbd> for the speaker view.</p>
<ul>""" + "\n".join(links) + "</ul></html>\n")


def check_index():
    # Read the Git index, not the working tree: partially staged edits must be safe too.
    paths = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
    if any(p.startswith("dev/instructor-slides/") for p in paths):
        raise ValueError("The local instructor directory has been staged for syncing")
    def staged(path):
        return subprocess.check_output(["git", "show", ":" + path], cwd=ROOT).decode()
    manifest = json.loads(staged(MANIFEST.relative_to(ROOT).as_posix()))
    names = {p.split("/")[1] for p in paths if re.fullmatch(r"modules/[0-9]{2}-[^/]+/slides\.(html|qmd)", p)}
    if not names or names != manifest.keys():
        raise ValueError("The staged deck list differs from the verified student decks")
    changed = set(subprocess.check_output(
        ["git", "diff", "--cached", "--name-only", "-z"], cwd=ROOT
    ).decode().split("\0"))
    for name in sorted(names):
        files = [f"modules/{name}/{f}" for f in FILES]
        qmd, html = (staged(f) for f in files)
        check_student(name, manifest[name], qmd, html)
        if changed.intersection(files) and (PRIVATE / name / "slides.qmd").exists():
            check_pair(name, qmd, html)
    # A second copy under a different name could bypass the canonical deck checks.
    registered = {f"modules/{name}/{f}" for name in names for f in FILES}
    for path in paths:
        if path in registered or not path.endswith((".qmd", ".html")):
            continue
        data = staged(path)
        if path.endswith(".qmd"):
            frontmatter = data.partition("\n---\n")[0]
            if re.search(r"(?m)^ *(?:revealjs *:|format: *revealjs\b)", frontmatter) and split_source(data)[0] != data:
                raise ValueError(f"{path}: unregistered slide source contains notes or draft comments")
        elif re.search(r"""class=["']reveal["']""", data) and SlideHTML(data).student() != data:
            raise ValueError(f"{path}: unregistered slide deck contains notes or draft comments")
    print(f"Verified {len(names)} staged student decks; instructor files are excluded.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["build", "check", "check-public", "check-index"])
    parser.add_argument("modules", nargs="*", help="module directory names (default: all)")
    args = parser.parse_args()
    if args.command == "check-index":
        return check_index()
    manifest = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    dirs = {p.parent.name for p in PUBLIC.glob("[0-9][0-9]-*/slides.*") if p.name in FILES}
    if args.command != "check-public":
        dirs.update(p.parent.name for p in PRIVATE.glob("[0-9][0-9]-*/slides.qmd"))
    names = sorted(set(args.modules) or dirs | manifest.keys())
    if not names or set(names) - dirs:
        parser.error("No matching slide pair for one or more modules")
    if args.command == "build":
        PRIVATE.mkdir(parents=True, exist_ok=True)
        with (PRIVATE / ".build.lock").open("a") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            manifest = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
            resources()
            for name in names:
                manifest[name] = build(name)
                check(name, manifest[name], False)
                write(MANIFEST, json.dumps(manifest, indent=2, sort_keys=True) + "\n")
            classroom_index()
    else:
        for name in names:
            check(name, manifest.get(name, {}), args.command == "check-public")
        if args.command == "check-public":
            print(f"Verified {len(names)} public decks against their notes-free build fingerprints.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        sys.exit(str(error))
