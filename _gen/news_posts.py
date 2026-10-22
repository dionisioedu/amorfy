"""Notícias com fontes primárias e fotografias creditadas."""
import json
from pathlib import Path

ARTICLES = [json.loads(p.read_text(encoding="utf-8")) for p in sorted((Path(__file__).parent / "news").glob("*.json"))]
