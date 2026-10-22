#!/usr/bin/env python3
"""List the slide layouts in a PowerPoint template and their placeholders.

Prints each layout's index and name, then one line per placeholder with its
idx, type, name, and size in inches. Use the layout names and placeholder
idx values in the outline passed to build_deck.py.

Usage:
    list_layouts.py TEMPLATE.pptx|TEMPLATE.potx [--json]
"""

import argparse
import json
from pathlib import Path

from deck_template import open_deck

EMU_PER_INCH = 914400


def describe(path: Path) -> dict:
    prs = open_deck(path)
    layouts = []
    for i, layout in enumerate(prs.slide_layouts):
        layouts.append({
            "index": i,
            "name": layout.name,
            "placeholders": [
                {
                    "idx": ph.placeholder_format.idx,
                    "type": str(ph.placeholder_format.type).split(".")[-1].split(" ")[0],
                    "name": ph.name,
                    "inches": [round(v / EMU_PER_INCH, 2) for v in (ph.left or 0, ph.top or 0, ph.width or 0, ph.height or 0)],
                }
                for ph in layout.placeholders
            ],
        })
    return {
        "template": str(path),
        "slide_size_inches": [round(prs.slide_width / EMU_PER_INCH, 2), round(prs.slide_height / EMU_PER_INCH, 2)],
        "existing_slides": len(prs.slides),
        "layouts": layouts,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("template", type=Path)
    parser.add_argument("--json", action="store_true", help="print JSON instead of text")
    args = parser.parse_args()

    info = describe(args.template)
    if args.json:
        print(json.dumps(info, indent=2))
        return
    w, h = info["slide_size_inches"]
    print(f"{info['template']}: {w} x {h} in, {info['existing_slides']} existing slides")
    for layout in info["layouts"]:
        print(f"\n[{layout['index']}] {layout['name']}")
        for ph in layout["placeholders"]:
            print(f"\tidx {ph['idx']:>3}  {ph['type']:<12} {ph['name']}  {ph['inches']}")


if __name__ == "__main__":
    main()
