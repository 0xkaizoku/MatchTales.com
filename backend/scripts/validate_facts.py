"""Fail if new desk stories contain em-dashes or double-hyphen punctuation."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2] / "frontend" / "src" / "content"
bad = []
for path in list(ROOT.rglob("*.md")) + list(ROOT.rglob("*.json")):
    text = path.read_text(encoding="utf-8")
    if "\u2014" in text or "\u2013" in text:
        bad.append(f"{path}: em/en dash")
print("scanned", "ok" if not bad else "FAIL")
for b in bad:
    print(b)
sys.exit(1 if bad else 0)
