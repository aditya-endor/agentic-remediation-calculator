#!/usr/bin/env python3
"""Copy pricing.json into index.html's built-in fallback block.

Run after editing pricing.json:  python3 scripts/sync-fallback.py
The live page fetches pricing.json directly; the built-in copy is only
used when that fetch fails (offline, file://, or a broken JSON commit).
"""
import json, pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
pricing = root / "pricing.json"
html_path = root / "index.html"

raw = pricing.read_text(encoding="utf-8")
json.loads(raw)  # fail loudly on invalid JSON before touching index.html

html = html_path.read_text(encoding="utf-8")
pattern = re.compile(r'(<script type="application/json" id="arc-pricing-fallback">)(.*?)(</script>)', re.S)
if not pattern.search(html):
    sys.exit("fallback block not found in index.html")
new = pattern.sub(lambda m: m.group(1) + "\n" + raw.strip() + "\n" + m.group(3), html, count=1)
html_path.write_text(new, encoding="utf-8")
print("synced pricing.json into index.html fallback block")
