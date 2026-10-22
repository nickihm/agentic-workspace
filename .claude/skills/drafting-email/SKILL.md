---
name: drafting-email
description: Draft an email in the user's own voice, matched to the samples in Assets/Samples/Emails/. Saves it as a draft in a connected mail tool, or as a markdown file in Outbox/ when none is connected. Never sends. Use when the user says "draft an email", "write an email", "compose a reply", or asks for an email about a topic.
---

# Drafting Email

Write an email that sounds like the user, then save it as a draft. Recipients stay blank; the user fills them in and sends it.

Never send. Only draft.

## Inputs

Ask for anything missing:

- **Purpose**: what the email should get done.
- **Audience**: who will read it. Use this for tone only; do not fill in recipients.
- **Key points**: facts, asks, deadlines, links.
- **Subject** (optional): write one if none is given.

If the user points at a note, an interaction log entry, or a thread, read it first.

## Voice

Read 1-2 files in `Assets/Samples/Emails/` before drafting, picking the closest in purpose. Copy their greeting, sign-off, signature, sentence length, and level of formality.

If the folder is empty, use these defaults and tell the user that adding 3-5 of their own sent emails there (as `.md` or `.txt`, with names and addresses removed) will make drafts sound like them:

- `Hi <FirstName>,` then a blank line.
- One sentence that states the purpose or the answer.
- Short prose for context; bullets for lists of items, questions, or links.
- A short sign-off such as `Thanks,` and then the user's first name. If you do not know the name, leave `<Your name>`.

## Formatting rules

- No em dashes. Use a comma, a period, or a new sentence.
- No backticks around product, file, or service names in a sentence. Code formatting is for actual code or commands.
- Bold sparingly: at most the one thing the email is about, or the lead word of a key bullet.
- No headings in the body.
- Dash bullets. Sub-bullets only when the content is nested.
- Plain URLs are fine.

## Steps

1. **Read the samples** as described above.
2. **Draft in markdown** and show it to the user in chat. Keep it short. Lead with the ask or the answer.
3. **Save the draft.**
   - **Mail tool connected** (an Outlook, Gmail, or other email MCP server): convert to minimal HTML (`<p>`, `<ul>`, `<li>`, `<strong>`, `<a>`; no inline CSS, fonts, or headings) and call the tool's create-draft operation with only a subject and body. Leave To, CC, and BCC empty. Never set a send flag or call a send operation.
   - **No mail tool**: write `Outbox/Email - <Subject>.md` with `Subject:` on the first line, a blank line, then the body.
4. **Confirm** in chat: where the draft is, the subject, and a one-line summary. Mention that recipients are blank on purpose.

## Do not

- Fill in recipients, even if they seem obvious.
- Send, schedule, or forward anything.
- Use a formal sign-off ("Best regards", "Sincerely") unless the samples do.
- Add facts, dates, or commitments the user did not give you or that are not in the notes you read.
