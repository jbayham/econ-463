"""Check reviewed student-facing slide evidence against current problem-set sources."""

import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAP = Path(__file__).with_name("coverage.json")
PROBLEM = re.compile(r"^## Problem (\d+)\b[^\n]*", re.M)
PART = re.compile(r"^\*\*\(([a-z])\)\*\*", re.M)
STEP = re.compile(r"^(\d+)\.\s", re.M)
SLIDE = re.compile(r"^## (.+)$", re.M)
PLACEHOLDER = re.compile(r"\*Add the \w+ problem prompt here\.\*")


def blocks(pattern, source, include_heading=False):
    matches = list(pattern.finditer(source))
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(source)
        start = match.start() if include_heading else match.end()
        yield match[1], source[start:end]


def visible_source(source):
    source = re.sub(r"<!--.*?-->", "", source, flags=re.S)
    return re.sub(r"^::: \{\.notes\}.*?^:::[ \t]*$", "", source, flags=re.M | re.S)


def question_parts(body):
    result = []
    for letter, text in blocks(PART, body):
        steps = STEP.findall(text)
        result.extend([f"{letter}.{n}" for n in steps] or [letter])
    return result or STEP.findall(body) or ["whole"]


def read_slides():
    evidence = {}
    for path in sorted((ROOT / "modules").glob("[0-9][0-9]-*/slides.qmd")):
        module = path.parent.name.split("-")[0]
        for title, body in blocks(SLIDE, visible_source(path.read_text())):
            title = re.sub(r"\s+\{[^{}]*\}$", "", title.strip())
            key = (module, title)
            if key in evidence:
                raise ValueError(f"Ambiguous slide title in module {module}: {title}")
            evidence[key] = body
    return evidence


def check():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fingerprints", action="store_true",
                        help="show current review fingerprints alongside findings")
    args = parser.parse_args()
    reviews = json.loads(MAP.read_text())
    slides = read_slides()
    seen = set()
    issues = []
    counts = dict(supported=0, gap=0, pending=0, stale=0)
    files = sorted((ROOT / "problem sets").glob("problem-set-*.qmd"))
    if not files:
        issues.append("No problem-set sources found.")
    for path in files:
        ps = int(path.stem.split("-")[-1])
        problems = list(blocks(PROBLEM, visible_source(path.read_text()), include_heading=True))
        if not problems:
            issues.append(f"PS{ps}: no '## Problem N' headings found.")
        for n, body in problems:
            key = f"PS{ps}.{n}"
            if key in seen:
                issues.append(f"{key}: duplicate problem number.")
            seen.add(key)
            prompt = PROBLEM.sub("", body, count=1)
            prompt = re.sub(r"```\{=latex\}\s*\\answerspace(?:\[[^\]]*\])?\s*```", "", prompt)
            if PLACEHOLDER.fullmatch(prompt.strip()) and key not in reviews:
                counts["pending"] += 1
                print(f"PENDING {key} — template prompt")
                continue
            if key not in reviews:
                issues.append(f"{key}: new question needs a foundation review.")
                continue
            record = reviews[key]
            parts = question_parts(body)
            reviewed = record["parts"]
            if set(parts) != set(reviewed) or len(parts) != len(set(parts)):
                issues.append(f"{key}: question parts {parts} do not match reviewed parts {list(reviewed)}.")
            evidence = [body]
            supported = []
            for part, item in reviewed.items():
                label = f"{key}({part})"
                cited = []
                for ref in item["slides"]:
                    module, title = (ref.split("/", 1) if re.match(r"^\d\d/", ref)
                                     else (record["module"], ref))
                    body_text = slides.get((module, title))
                    if not body_text or not body_text.strip():
                        issues.append(f"{label}: missing slide in M{module}: {title}")
                    else:
                        evidence.extend([module, title, body_text])
                        cited.append(title)
                if item.get("gap") or not cited or len(cited) != len(item["slides"]):
                    counts["gap"] += 1
                    issues.append(f"{label} — {item.get('gap') or 'No slide evidence.'}")
                else:
                    supported.append(f"{label} — {item['skill']} [{', '.join(cited)}]")
            # Normalize prose wrapping. Changes to the shared stem or any cited slide
            # reopen the review for the whole problem, including multipart questions.
            text = "\n".join(" ".join(block.split()) for block in evidence)
            digest = hashlib.sha256(text.encode()).hexdigest()[:16]
            if args.fingerprints:
                print(f"FINGERPRINT {key} {digest}")
            if record.get("reviewed") != digest:
                counts["stale"] += len(supported)
                issues.append(f"{key}: prompt or slide evidence changed; review before updating the fingerprint.")
            else:
                counts["supported"] += len(supported)
                for entry in supported:
                    print("SUPPORTED", entry)
    for key in sorted(reviews.keys() - seen):
        issues.append(f"{key}: reviewed question no longer exists.")
    for issue in issues:
        print("REVIEW", issue)
    print(f"{counts['supported']} supported parts, {counts['gap']} parts with gaps, "
          f"{counts['stale']} awaiting re-review, {counts['pending']} pending template prompts.")
    return bool(issues)


if __name__ == "__main__":
    raise SystemExit(check())
