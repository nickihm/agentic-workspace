# Templates

Document templates go here: PowerPoint (`.pptx`, `.potx`), Word (`.docx`, `.dotx`), Excel (`.xlsx`, `.xltx`), and any other file a new document should start from. Name each one in Title Case with spaces, for example `Company Deck.pptx` or `Statement of Work.docx`.

- `building-decks` builds every `.pptx` from a template in this folder.
- Never edit a template in place. Copy it, or build a new file from it, and save the result next to the note it belongs to or in `Outbox/`.

## If this folder is empty

This file and `.gitkeep` do not count. When a task needs a template and none is here, stop and ask the user to add one: a deck, document, or workbook in their own branding. Say which kind the task needs. Continue with a plain default only if the user says so.
