#!/usr/bin/env python3
"""Write an HTML preview for a .drawio file.

Embeds the diagram XML in a page that loads the draw.io viewer, so the
diagram can be zoomed and panned in any browser. The output file has the
same base name as the input, with an .html extension.

Usage:
    drawio_to_html.py DIAGRAM.drawio [--title TITLE]
"""

import argparse
import html
import json
import xml.etree.ElementTree as ET
from pathlib import Path

PAGE = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{title}</title>
</head>
<body>
  <div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{config}"></div>
  <script type="text/javascript" src="https://viewer.diagrams.net/js/viewer-static.min.js"></script>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("diagram", type=Path)
    parser.add_argument("--title")
    args = parser.parse_args()

    xml = args.diagram.read_text(encoding="utf-8")
    ET.fromstring(xml)  # fail early on malformed XML

    config = {
        "highlight": "#0000ff",
        "nav": True,
        "resize": True,
        "toolbar": "zoom layers tags lightbox",
        "edit": "_blank",
        "xml": xml,
    }
    out = args.diagram.with_suffix(".html")
    out.write_text(
        PAGE.format(
            title=html.escape(args.title or args.diagram.stem),
            config=html.escape(json.dumps(config), quote=True),
        ),
        encoding="utf-8",
    )
    print(out)


if __name__ == "__main__":
    main()
