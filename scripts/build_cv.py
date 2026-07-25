#!/usr/bin/env python3
"""
Parses _pages/cv.md (the Jekyll/academicpages CV source) and renders a
LaTeX CV from it, then compiles it to assets/cv.pdf.

This keeps the markdown file as the single source of truth: whenever it
changes and this script runs (locally or in CI), the PDF is regenerated
to match.
"""
import re
import subprocess
import sys
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parent.parent
CV_MD = ROOT / "_pages" / "cv.md"
TEMPLATE_DIR = ROOT / "templates"
BUILD_DIR = ROOT / "build"
OUTPUT_PDF = ROOT / "assets" / "cv.pdf"

# Fallbacks used only if cv.md's front matter doesn't set these.
DEFAULTS = {
    "cv_name": "Your Name",
    "cv_tagline": "",
    "cv_email": "",
    "cv_location": "",
    "cv_website": "",
}


def tex_escape(text: str) -> str:
    """Escape LaTeX special characters in plain text (not already-LaTeX markup)."""
    chars = {
        "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_",
        "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return re.sub("|".join(re.escape(k) for k in chars), lambda m: chars[m.group()], text)


def md_inline_to_tex(text: str) -> str:
    """Convert a small subset of inline markdown (bold/italic) to LaTeX,
    escaping everything else."""
    text = text.replace("–", "--").replace("—", "---")
    parts = re.split(r"(\*\*.+?\*\*|\*.+?\*)", text)
    out = []
    for part in parts:
        if part.startswith("**") and part.endswith("**"):
            out.append(r"\textbf{" + tex_escape(part[2:-2]) + "}")
        elif part.startswith("*") and part.endswith("*"):
            out.append(r"\textit{" + tex_escape(part[1:-1]) + "}")
        else:
            out.append(tex_escape(part))
    return "".join(out)


def extract_front_matter(raw: str):
    """Return (front_matter_dict, body_without_front_matter)."""
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, flags=re.DOTALL)
    if not m:
        return {}, raw
    fm = yaml.safe_load(m.group(1)) or {}
    return fm, m.group(2)


def strip_html(body: str) -> str:
    # Drop the <style>...</style> block
    body = re.sub(r"<style>.*?</style>", "", body, flags=re.DOTALL)
    # Drop the download button <a>...</a>
    body = re.sub(r"<a href=\"/assets/cv\.pdf\".*?</a>", "", body, flags=re.DOTALL)
    return body


def split_sections(body: str):
    """Split into an ordered list of (heading, section_text) on '## Heading' markers."""
    # Remove standalone '---' horizontal-rule lines (section separators)
    body = re.sub(r"^\s*---\s*$", "", body, flags=re.MULTILINE)
    chunks = re.split(r"^##\s+(.+)$", body, flags=re.MULTILINE)
    sections = []
    # chunks[0] is preamble before first '##'; then alternating heading, text
    for i in range(1, len(chunks), 2):
        heading = chunks[i].strip()
        text = chunks[i + 1].strip() if i + 1 < len(chunks) else ""
        sections.append((heading, text))
    return sections


EDUCATION_ENTRY_RE = re.compile(
    r"\*\*(?P<degree>.+?)\*\*\s*<span class=\"cv-year\">(?P<years>.+?)</span>\s*\n"
    r"(?P<inst>[^\n]+?)\s*(?:\n\*Advisor:\*\s*(?P<advisor>[^\n]+))?"
    r"(?=\n\*\*|\Z)",
    re.MULTILINE,
)

SKILLS_LINE_RE = re.compile(r"-\s*\*\*(.+?):\*\*\s*(.+)")


def parse_education(text: str):
    entries = []
    for m in EDUCATION_ENTRY_RE.finditer(text):
        entries.append({
            "degree": md_inline_to_tex(m.group("degree").strip()),
            "years": md_inline_to_tex(m.group("years").strip()),
            "institution": md_inline_to_tex(m.group("inst").strip()),
            "advisor": md_inline_to_tex(m.group("advisor").strip()) if m.group("advisor") else None,
        })
    return entries


def parse_bullets(text: str):
    """Parse a '- item\n  continuation' style bulleted list, joining wrapped
    continuation lines into each item."""
    items = []
    current = None
    for line in text.splitlines():
        if line.startswith("- "):
            if current:
                items.append(current)
            current = line[2:].strip()
        elif line.strip() and current is not None:
            current += " " + line.strip()
    if current:
        items.append(current)
    return items


def parse_label_value_bullets(text: str):
    """Parse '- **Label:** value' style bullets into (label, value) pairs."""
    pairs = []
    for line in text.splitlines():
        m = SKILLS_LINE_RE.match(line.strip())
        if m:
            pairs.append((md_inline_to_tex(m.group(1)), md_inline_to_tex(m.group(2))))
    return pairs


def classify_and_parse(heading: str, text: str) -> dict:
    """Auto-detect the shape of a section's markdown and parse it accordingly.
    This is what lets new sections in cv.md 'just work' with no code changes:
      - degree/year entries        -> type 'education'
      - '- **Label:** value' lines -> type 'labelvalue'
      - any other '- ' bullet list -> type 'bullets'
      - otherwise                  -> type 'prose'
    """
    if not text.strip():
        return {"heading": heading, "type": "prose", "prose": ""}

    if EDUCATION_ENTRY_RE.search(text):
        return {"heading": heading, "type": "education", "entries": parse_education(text)}

    bullet_lines = [l for l in text.splitlines() if l.strip().startswith("- ")]
    if bullet_lines:
        if all(SKILLS_LINE_RE.match(l.strip()) for l in bullet_lines):
            return {"heading": heading, "type": "labelvalue", "pairs": parse_label_value_bullets(text)}
        return {"heading": heading, "type": "bullets",
                "bullet_items": [md_inline_to_tex(i) for i in parse_bullets(text)]}

    return {"heading": heading, "type": "prose", "prose": md_inline_to_tex(text.strip())}


def main():
    if not CV_MD.exists():
        print(f"ERROR: {CV_MD} not found", file=sys.stderr)
        sys.exit(1)

    raw = CV_MD.read_text(encoding="utf-8")
    front_matter, body = extract_front_matter(raw)
    body = strip_html(body)
    raw_sections = split_sections(body)

    # Every '## Heading' in cv.md becomes an entry here automatically —
    # no per-section code needed to add, rename, or reorder sections.
    sections = [classify_and_parse(heading, text) for heading, text in raw_sections]

    def fm(key):
        return str(front_matter.get(key) or DEFAULTS[key])

    data = {
        "name": tex_escape(fm("cv_name")),
        "tagline": tex_escape(fm("cv_tagline")),
        "email": tex_escape(fm("cv_email")),
        "location": tex_escape(fm("cv_location")),
        "website": tex_escape(fm("cv_website")),
        "sections": sections,
    }

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        block_start_string="((*", block_end_string="*))",
        variable_start_string="(((", variable_end_string=")))",
        comment_start_string="((#", comment_end_string="#))",
        trim_blocks=True, lstrip_blocks=True,
    )
    template = env.get_template("cv_template.tex.j2")
    rendered = template.render(**data)

    BUILD_DIR.mkdir(exist_ok=True)
    tex_path = BUILD_DIR / "cv.tex"
    tex_path.write_text(rendered, encoding="utf-8")

    subprocess.run(
        ["xelatex", "-interaction=nonstopmode", "-halt-on-error", "cv.tex"],
        cwd=BUILD_DIR, check=True,
    )

    OUTPUT_PDF.parent.mkdir(exist_ok=True)
    (BUILD_DIR / "cv.pdf").replace(OUTPUT_PDF)
    print(f"Wrote {OUTPUT_PDF}")


if __name__ == "__main__":
    main()
