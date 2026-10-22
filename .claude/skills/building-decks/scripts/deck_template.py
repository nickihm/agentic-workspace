"""Shared helper: open a .pptx or .potx file with python-pptx.

python-pptx only opens presentations. A .potx template has a different main
content type, so it is rewritten in memory as a presentation before loading.
"""

import io
import zipfile
from pathlib import Path

from pptx import Presentation

TEMPLATE_TYPE = b"application/vnd.openxmlformats-officedocument.presentationml.template.main+xml"
PRESENTATION_TYPE = b"application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"


def open_deck(path: Path):
    if path.suffix.lower() != ".potx":
        return Presentation(str(path))
    buf = io.BytesIO()
    with zipfile.ZipFile(path) as src, zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as dst:
        for item in src.infolist():
            data = src.read(item.filename)
            if item.filename == "[Content_Types].xml":
                data = data.replace(TEMPLATE_TYPE, PRESENTATION_TYPE)
            dst.writestr(item, data)
    buf.seek(0)
    return Presentation(buf)
