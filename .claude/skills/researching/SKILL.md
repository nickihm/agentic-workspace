---
name: researching
description: Research a question from primary sources and answer with citations. Covers technical topics, products, vendors, standards, regulations, markets, and how-tos. Optionally saves the result to Notes/Resources/. Use when the user says "research", "look into", "find out", "compare X and Y", "what are the options for", or asks a factual question that needs current sources.
---

# Researching

Answer a question from sources you can cite, not from memory. Every claim that a reader might act on gets a link.

## 1. Pin down the question

Ask only if the answer changes the research:

- What exactly is being decided or explained?
- For whom or what situation? If it is about an account or project, read its note in `Notes/Accounts/` or `Notes/Projects/` first for context.
- How deep: a quick answer, a comparison, or a full write-up?

## 2. Search

Use what is connected, in this order:

1. **Domain tools.** MCP servers for documentation or knowledge bases (a vendor's docs server, an internal wiki, a local search index). Prefer these for the topics they cover.
2. **The user's notes.** Search `Notes/` for earlier research, decisions, and contacts on the topic.
3. **Web search and fetch.** Go to the primary source: official documentation, standards bodies, regulators, company filings, release notes, peer-reviewed papers. Use secondary sources (blogs, news, forums) to find primary ones or to show practice, and label them as such.

Rules while searching:

- Read the page you cite. Do not cite from a search snippet.
- Check dates. Note when a source is older than about a year on a topic that changes fast, and look for a newer one.
- Cross-check numbers (prices, limits, dates, versions) against a second source, or say there is only one.
- Keep a list of every URL you use.

## 3. Answer

Lead with the answer. Then give only the detail the user asked for:

```markdown
## <Topic>

**Answer:** 2-3 sentences.

**Details**
- Fact, with its limit or condition [1]
- Fact [2]

**Options** (for comparisons)
| Option | Fits when | Watch out for | Source |
|---|---|---|---|

**Open questions**
- What the sources do not settle, and where to look next

**Sources**
1. Title - publisher, date - URL
2. ...
```

- Separate what a source states from your own inference, and label the inference.
- Mark preview, beta, or proposed items as such.
- Note regional, version, or jurisdiction limits when they apply.
- If the sources do not answer the question, say so and say where an answer might be found. Do not fill the gap with a guess.

## 4. Save, if asked

When the user wants to keep the research, save it to `Notes/Resources/<Topic>/<Title>.md` (or `Notes/Resources/<Title>.md` for a single note), in Title Case with spaces. Put the date at the top and keep the source list. Link it from the related account or project note with a `[[wikilink]]` only if the user asks.

## Related skills

- A design to draw: `architecture-diagram`.
- Costs, prices, or a model to build: `financial-modeling`.
- An email to send about it: `drafting-email`.
