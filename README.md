# Agentic Remediation ROI Calculator — prototype

**Live prototype:** https://aditya-endor.github.io/agentic-remediation-calculator/
**Production page:** https://www.endorlabs.com/agentic-remediation-roi-calculator

This repo is the working spec for the Endor Labs Agentic Remediation ROI Calculator. The prototype mirrors the production page's layout and copy, plus the changes listed below. The web team implements from it.

| File | What it is |
|---|---|
| `index.html` | The calculator. Self-contained HTML/CSS/JS, scoped under `#endor-arc`. |
| `pricing.json` | **The model pricing table.** The page fetches it on every load. Edit this to add, remove, or reprice a model. |
| `scripts/sync-fallback.py` | Copies `pricing.json` into the built-in fallback block inside `index.html`. Optional; see below. |

## Updating model pricing

1. Open `pricing.json` on GitHub and click the pencil icon.
2. Edit, then commit to `main`.
3. Reload the prototype after a minute or two. GitHub Pages redeploys automatically.

Fields:

```json
{
  "asOf": "September 2026",          // shown in the sources table and the disclaimer
  "reference": "claude-opus-4-8",    // the 1.00x model the "Current Cost Per Fix" is anchored on
  "default": "claude-opus-5",        // model selected on load and after Reset
  "compare": ["gpt-5-5", "claude-fable-5"],   // initial top and bottom rows of the comparison table
  "models": [
    { "id": "claude-opus-5", "provider": "Claude", "name": "Claude Opus 5", "input": 5, "output": 25 }
  ]
}
```

- `input` and `output` are public list prices in USD per million tokens.
- **The multiplier is derived:** `output ÷ reference output` (Opus 4.8 output is $25, so Sonnet 5 at $10 is 0.40×, GPT-5.5 at $30 is 1.20×). This matches the spreadsheet. Add `"multiplier": 1.2` to a model to override the derived value.
- `provider` is the group heading in the dropdowns. Order in the file is the order in the dropdowns.
- `id` must be unique and stable. It is what `default`, `compare`, and `reference` point at.

The page also carries a built-in copy of `pricing.json` so it still renders if the fetch fails. It is used only in that case. Refresh it whenever convenient with `python3 scripts/sync-fallback.py` and commit `index.html`. Drift between the two is harmless on GitHub Pages because the live file wins.

## For the web team: changes vs. the live page (as of September 21, 2026)

Layout and copy are otherwise identical to production. Everything below is a deliberate change.

**Inputs**
1. `PRs/Dev/Month` → **`Fixes/Dev/Month`**. Hint unchanged.
2. Each slider now has an **editable number** where the green value was, so a 3,000-developer org can be entered. Slider range stays 10–1,000 developers (typed values above the slider max are allowed; the slider pins at max).
3. `Seat license ($ / seat / month)` → **`Coding agent seat ($ / user / month)`**. Hint: "Per-user cost of Claude Code, Codex, etc. · $100/month is typical". Range **$0–$1,000** (production clamps to $50–$200, which made $0 or $20 snap back to $50). `$` prefix inside the field.
4. `Current Cost Per Fix`: **`$` prefix inside the field**, new hint "Reference price on Claude Opus 4.8 · other models scale from it · default $20". The selected model's resulting `$/fix` and multiplier are shown under the model dropdown so the reference-vs-selected relationship is visible.
5. `Reduction in Tokens Required to Remediate`: slider max **91.7 → 99**, with a tick mark at 91.7 (the benchmark). Hint gains "(tick mark)".
6. **Remediation model dropdown lists every model in `pricing.json`**, grouped by provider (model names only; the `$/fix` for the selected model shows in the hint underneath). **Default model is Claude Opus 5** (same list price as Opus 4.8, so default results are unchanged: $230,400 / 49.2%).

**Comparison table**
7. `All Three Models at Your Volume` → **`Compare Across Models`**.
8. Three rows. **Middle row is locked to the selected model** (lock icon, "Selected" tag, highlighted) and follows the main dropdown. **Top and bottom rows are dropdowns** listing every other model; each disables the other row's current pick so no model appears twice. If the user selects a model that is already in a comparison row, that row swaps to the previously selected model. Initial rows come from `compare` in `pricing.json`.

**Under the hood, sources, disclaimer**
9. **Step-by-step numbers are now live.** On production they are static text and Step B reads "150 × 14 × 12 = 25,200 fixes … $504,000" regardless of inputs (does not match the defaults).
10. Sources: seat and reference bullets reworded to match the new labels; multiplier bullet explains the derivation; the **pricing table renders from `pricing.json`** (Model / Input $/MTok / Output $/MTok / Cost vs. Claude Opus 4.8 / $/Fix at the current Current Cost Per Fix, grouped by provider, reference row tagged). The "Cost vs." column is the multiplier. Production's table is static with five models and duplicate element ids.
11. Disclaimer "as of mid-2026" → **"as of {asOf}"** from `pricing.json`.

**PDF (handled by the web team, not in this prototype)**
12. The PDF generator hardcodes three models and the old labels. It needs: `Fixes/Dev/Month`; the new seat label; `Compare Across Models` with **the three rows currently shown** (two picks plus the selected model, highlighted); the selected model's name from the dropdown rather than a fixed list. The gating form is unchanged.

**Pricing source for production.** Two options: fetch `https://aditya-endor.github.io/agentic-remediation-calculator/pricing.json` from endorlabs.com (GitHub Pages sends `Access-Control-Allow-Origin: *`; the page falls back to its built-in copy on failure), or paste the JSON into the Webflow embed and update it by hand. Either way, keep the derived-multiplier logic so only two numbers per model need maintaining.

## Local preview

```bash
python3 -m http.server 8765
# open http://localhost:8765/
```

Opening `index.html` directly from disk also works; it uses the built-in pricing copy because browsers block `fetch` on `file://`.

## Math (unchanged from the spreadsheet)

- **A. Seat floor** = developers × seat cost × 12
- **B. Token bill** = developers × fixes/dev/month × 12 × (reference $/fix × model multiplier)
- **C. With Endor Labs** = token bill × (1 − reduction) + seat floor
- Savings = A+B − C

Defaults: 150 developers, 8 fixes/dev/month, $100 seat, $20 reference, 80% reduction, Claude Opus 5 → $468,000 without, $237,600 with, $230,400 saved (49.2%).
