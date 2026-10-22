---
name: financial-modeling
description: Build a cost, price, or financial model as an Excel workbook with live formulas: cost estimates, pricing a product or service, total cost of ownership, build vs. buy, budgets, break-even, ROI, and cash flow. Researches current prices, collects the inputs, and saves an .xlsx with an assumptions sheet. Use when the user says "estimate the cost", "price this", "build a model", "TCO", "break-even", "ROI", "budget for", or "what would X cost".
---

# Financial Modeling

Turn a question about money into a workbook the user can change and trust: every input in one place, every result a formula, every price with a source.

## 1. Frame the model

Find out, from the request or by asking:

- **Question**: what decision the model supports. For example "Which plan is cheaper over 3 years?" or "What price gives a 40% margin?".
- **Model type**:
  - Cost estimate: what something will cost, by component.
  - Pricing: what to charge, from costs and target margin, or from comparable prices.
  - Comparison or TCO: two or more options over the same period.
  - Budget or forecast: planned spend or revenue by month or quarter.
  - Break-even, ROI, payback, NPV: when or whether an investment pays off.
- **Period and granularity**: monthly, quarterly, or annual, and for how long.
- **Currency**, and the location or market if prices vary by it.

If the model is for an account or project, read its note in `Notes/Accounts/` or `Notes/Projects/` for context.

## 2. Research prices and rates

- Get unit prices from the seller's current published price list, a quote the user has, or the user's own records. Use the `researching` skill for anything that needs a search.
- Record each price with its source URL or document and the date you checked it.
- Include every cost component, not only the headline price: setup fees, per-use charges, storage, transfer, support, taxes, licenses, labor, maintenance.
- Note free tiers, volume discounts, and commitment discounts, and model them as separate options when they change the answer.
- If you cannot find a price, say so and leave the input blank and highlighted. Never invent one.

## 3. Collect inputs

Ask only for what drives the result, in grouped, short questions. Use stated defaults where they are reasonable (for example, 730 hours in a month for something that runs all the time) and list them as assumptions.

## 4. Build the workbook

Write it with Python and `openpyxl` (`pip install openpyxl` if missing). If an `xlsx` skill is installed in `.claude/skills/`, follow its rules as well.

**Sheet 1: Assumptions**
- Every input on one sheet: quantities, unit prices, rates, growth, discount rate, period.
- Columns: Input | Value | Unit | Source | Date checked.
- Inputs in blue text. Key assumptions with a light yellow fill.

**Sheet 2: Model**
- One block per component or option. Columns fit the model type, for example: Item | Unit | Quantity | Unit Price | Monthly | Annual.
- Every number is a formula that references Assumptions. No typed-in results.
- Subtotals per block. Order cost blocks largest first.

**Sheet 3: Summary**
- The answer to the question in step 1: total, cheapest option, break-even month, ROI, or margin.
- For comparisons: Option | Monthly | Annual | Total over period | Difference vs. baseline (amount and %).
- A sensitivity table for the 1-2 inputs that move the result most.

**Formatting**
- Currency `#,##0.00` with the currency symbol; percentages `0.0%`.
- Formulas in black text.
- A notes block on Summary: "Prices as of YYYY-MM-DD", the sources, and "Estimates; actual results depend on usage, terms, and taxes."

## 5. Check it

- Open the workbook with `openpyxl` and confirm no cell on Model or Summary holds a typed-in number where a formula belongs.
- If LibreOffice is installed, recalculate headless (`soffice --headless --convert-to xlsx --outdir /tmp <file>`) and read the computed values back to check for `#REF!`, `#DIV/0!`, and `#NAME?`.
- Recompute one or two totals by hand in chat and confirm they match.

## 6. Save and report

- Working copy: next to the related note, for example `Notes/Accounts/<Name>/<Project>/Cost Estimate - <Description>.xlsx`, or `Notes/Projects/<Project>/`.
- Finished deliverable for someone else: `Outbox/<Title>.xlsx`.

In chat, give a short markdown table of the main result, the 2-3 assumptions that matter most, and any price you could not find.

## Rules

- No invented prices, rates, or quotes. A blank, flagged input is better than a guess.
- Once the user edits a generated workbook, edit their saved copy. Do not regenerate it from the script and overwrite their changes.
