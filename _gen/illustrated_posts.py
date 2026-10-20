"""New illustrated editorial articles, one JSON source per publication."""
import json
from pathlib import Path

ARTICLES = [json.loads(p.read_text(encoding="utf-8")) for p in sorted((Path(__file__).parent / "posts").glob("*.json"))]
