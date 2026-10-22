#!/usr/bin/env python3
"""Build a .pptx deck from a JSON outline and a PowerPoint template.

The template's slide masters, layouts, theme fonts, and colors are kept.
Any slides already in the template are removed unless --keep-slides is set.
Each outline slide picks a layout by name and fills its placeholders.

Outline format:
    {
      "slides": [
        {
          "layout": "Title Slide",
          "placeholders": {"title": "Deck title", "1": "Subtitle"},
          "notes": "Speaker notes"
        },
        {
          "layout": "Title and Content",
          "placeholders": {
            "title": "One takeaway per slide",
            "1": ["First point", ["A sub-point", 1], "Second point"]
          }
        },
        {
          "layout": "Two Content",
          "placeholders": {
            "title": "Before and after",
            "1": {"image": "Assets/diagram.png"},
            "2": {"table": [["Option", "Cost"], ["A", "$10"], ["B", "$12"]]}
          }
        }
      ]
    }

Placeholder keys: "title", a placeholder idx as a string (see
list_layouts.py), or a placeholder name. Values: a string, a list of bullet
lines (a line can be [text, level]), {"image": path}, or {"table": rows}.
Image paths are relative to the outline file. Placeholders left out of a
slide are removed so no "Click to add text" prompts remain.

Usage:
    build_deck.py OUTLINE.json TEMPLATE.pptx|.potx OUTPUT.pptx [--keep-slides]
"""

import argparse
import json
from pathlib import Path

from deck_template import open_deck

try:
    from PIL import Image
except ImportError:  # Pillow ships with python-pptx; fall back to stretch-to-fit
    Image = None


def remove_slides(prs) -> None:
    id_list = prs.slides._sldIdLst
    for sld_id in list(id_list):
        prs.part.drop_rel(sld_id.rId)
        id_list.remove(sld_id)


def find_layout(prs, name: str):
    for layout in prs.slide_layouts:
        if layout.name.strip().lower() == name.strip().lower():
            return layout
    names = ", ".join(repr(l.name) for l in prs.slide_layouts)
    raise SystemExit(f"layout {name!r} not in template; available: {names}")


def find_placeholder(slide, key: str):
    if key == "title":
        if slide.shapes.title is None:
            raise SystemExit(f"layout {slide.slide_layout.name!r} has no title placeholder")
        return slide.shapes.title
    for ph in slide.placeholders:
        if key.isdigit() and ph.placeholder_format.idx == int(key):
            return ph
        if ph.name.strip().lower() == key.strip().lower():
            return ph
    found = ", ".join(f"{ph.placeholder_format.idx}={ph.name!r}" for ph in slide.placeholders)
    raise SystemExit(f"placeholder {key!r} not in layout {slide.slide_layout.name!r}; available: {found}")


def fill_text(ph, value) -> None:
    lines = [value] if isinstance(value, str) else value
    tf = ph.text_frame
    tf.clear()
    for i, line in enumerate(lines):
        text, level = (line, 0) if isinstance(line, str) else (line[0], int(line[1]))
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.text = text
        para.level = level


def add_image(slide, ph, path: Path) -> None:
    left, top, width, height = ph.left, ph.top, ph.width, ph.height
    if Image is not None:
        with Image.open(path) as img:
            ratio = img.width / img.height
        if width / height > ratio:
            new_w = int(height * ratio)
            left, width = left + (width - new_w) // 2, new_w
        else:
            new_h = int(width / ratio)
            top, height = top + (height - new_h) // 2, new_h
    slide.shapes.add_picture(str(path), left, top, width, height)
    remove_shape(ph)


def add_table(slide, ph, rows: list) -> None:
    n_cols = max(len(r) for r in rows)
    table = slide.shapes.add_table(len(rows), n_cols, ph.left, ph.top, ph.width, ph.height).table
    for r, row in enumerate(rows):
        for c in range(n_cols):
            table.cell(r, c).text = str(row[c]) if c < len(row) else ""
    remove_shape(ph)


def remove_shape(shape) -> None:
    el = shape._element
    el.getparent().remove(el)


def build(outline_path: Path, template: Path, output: Path, keep_slides: bool) -> int:
    outline = json.loads(outline_path.read_text(encoding="utf-8"))
    base = outline_path.parent
    prs = open_deck(template)
    if not keep_slides:
        remove_slides(prs)

    for n, spec in enumerate(outline["slides"], start=1):
        slide = prs.slides.add_slide(find_layout(prs, spec["layout"]))
        used = set()
        for key, value in spec.get("placeholders", {}).items():
            ph = find_placeholder(slide, key)
            used.add(ph.shape_id)
            if isinstance(value, dict) and "image" in value:
                add_image(slide, ph, base / value["image"])
            elif isinstance(value, dict) and "table" in value:
                add_table(slide, ph, value["table"])
            elif ph.has_text_frame:
                fill_text(ph, value)
            else:
                raise SystemExit(f"slide {n}: placeholder {key!r} takes an image or table, not text")
        for ph in list(slide.placeholders):
            if ph.shape_id not in used:
                remove_shape(ph)
        if spec.get("notes"):
            slide.notes_slide.notes_text_frame.text = spec["notes"]

    output.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(output))
    return len(outline["slides"])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("outline", type=Path)
    parser.add_argument("template", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--keep-slides", action="store_true", help="keep the template's existing slides")
    args = parser.parse_args()
    if args.output.suffix.lower() != ".pptx":
        raise SystemExit("output must end in .pptx")
    count = build(args.outline, args.template, args.output, args.keep_slides)
    print(f"wrote {args.output} ({count} slides)")


if __name__ == "__main__":
    main()
