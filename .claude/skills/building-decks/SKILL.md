---
name: building-decks
description: Build a PowerPoint deck (.pptx) from a template in Assets/Templates/. Picks the template, reads its layouts, drafts an outline for approval, then fills the template's own layouts and placeholders so the fonts, colors, and branding stay intact. Use when the user says "make a deck", "build slides", "create a presentation", "turn this into a PowerPoint", or asks for slides on a topic.
---

# Building Decks

Make a `.pptx` that looks like it came from the user's own template: the template's layouts, theme, fonts, and colors, with new content in its placeholders.

The scripts need Python 3 and `python-pptx` (`pip install python-pptx`).

## 1. Pick the template

Look in `Assets/Templates/` for `.pptx` and `.potx` files.

- One template: use it.
- Several: list them and ask which one, unless the request names one (for example "use the dark template").
- None: say so, and ask the user to add their template to `Assets/Templates/` (see `Assets/Templates/AGENTS.md`). If they would rather not, offer to continue with the plain python-pptx default template. To use the default, pass a blank deck made with `python3 -c 'from pptx import Presentation; Presentation().save("/tmp/Default.pptx")'`.

Never edit the template file. The build writes a new file.

## 2. Read the layouts

```bash
python3 .claude/skills/building-decks/scripts/list_layouts.py "Assets/Templates/<Template>.pptx"
```

It prints each layout name and its placeholders (idx, type, name, size). Pick layouts by what they hold: a title slide, section headers, title and content, two content, picture with caption, title only, closing. Use only layouts the template has.

## 3. Draft the outline and get approval

Gather the content first. Sources can be the conversation, notes in `Notes/`, research results (`researching`), a model (`financial-modeling`), or a diagram (`architecture-diagram`, exported to PNG).

Show the outline in chat as a numbered list: slide title, layout, and the bullets or visual. Wait for the user to approve or change it.

Content rules:

- One idea per slide. The title states the takeaway ("Option B costs 18% less over 3 years"), not the topic ("Costs").
- At most 6 bullets per slide and 2 levels. Short phrases, not paragraphs.
- Put detail and talking points in speaker notes.
- Use only facts, numbers, and quotes from the sources. Add a sources slide when the deck cites outside material.
- For a long deck, add section header slides between parts.

## 4. Write the outline file and build

Write the approved outline as JSON next to where the deck will go. The format is documented at the top of `build_deck.py`. In short:

```json
{
  "slides": [
    {"layout": "Title Slide", "placeholders": {"title": "Deck title", "1": "Subtitle"}, "notes": "Speaker notes"},
    {"layout": "Title and Content", "placeholders": {"title": "One takeaway", "1": ["Point", ["Sub-point", 1]]}},
    {"layout": "Two Content", "placeholders": {"title": "Before and after", "1": {"image": "Architecture.png"}, "2": {"table": [["Option", "Cost"], ["A", "$10"]]}}}
  ]
}
```

- Placeholder keys are `"title"`, an idx from step 2 as a string, or a placeholder name.
- Values are text, a list of bullet lines (`[text, level]` for indented lines), `{"image": path}`, or `{"table": rows}`. Image paths are relative to the outline file.
- Placeholders you leave out are removed from the slide, so no empty prompts remain.

```bash
python3 .claude/skills/building-decks/scripts/build_deck.py "<path>/Outline.json" "Assets/Templates/<Template>.pptx" "<path>/<Deck Title>.pptx"
```

The template's own slides are removed from the output. Pass `--keep-slides` only if the user wants them, for example a fixed legal slide at the start.

The script does not set fonts, sizes, or colors. The template's layouts decide those. If text overflows a placeholder, shorten the text or split the slide; do not shrink fonts.

## 5. Check it

- Rebuild after every outline change. Do not edit the output by hand and then rebuild over it.
- If LibreOffice is installed, render a PDF and look at it: `soffice --headless --convert-to pdf --outdir /tmp "<deck>.pptx"`. With `pdftoppm` (from poppler) you can turn pages into images: `pdftoppm -png -r 60 /tmp/<deck>.pdf /tmp/slide`. Look for overflowing text, stretched images, and empty slides.
- Without LibreOffice, ask the user to open the deck in PowerPoint and report problems.

## 6. Save and report

- Working copy: next to the related note, for example `Notes/Accounts/<Name>/<Project>/<Deck Title>.pptx`.
- Finished deck to send: `Outbox/<Deck Title>.pptx`.

In chat, give the path, the slide count, and anything you left out or could not fill. To open it on macOS: `open -a "Microsoft PowerPoint" "<deck>.pptx"`.

## Rules

- Once the user edits a generated deck by hand, edit their saved copy. Do not rebuild over it.
- Never copy slides, logos, or images from a template into a deck for a different organization unless the user says to.
