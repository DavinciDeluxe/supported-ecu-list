#!/usr/bin/env python3
"""Search supported Cars & Heavy-Duty Trucks ECUs in DaVinci Deluxe Cloud Edition."""
import json
import pathlib
import sys

BASE = pathlib.Path(__file__).parent / "data"

def search(query: str) -> None:
    q = query.upper().strip()
    for label, fname in [("Cars & Vans", "cars_supported_ecus.json"), ("Trucks & Agri", "trucks_supported_ecus.json")]:
        fp = BASE / fname
        if not fp.exists():
            continue
        data = json.loads(fp.read_text(encoding="utf-8"))
        hits = []
        for brand, ecus in data.get("byBrand", {}).items():
            matched = [e for e in ecus if q in e.upper() or q in brand.upper()]
            if matched:
                hits.append((brand, matched))
        print(f"=== {label}: {len(hits)} brand(s) matched '{query}' ===")
        for b, m in hits[:25]:
            print(f"  {b}: {', '.join(m[:10])}")

if __name__ == "__main__":
    search(sys.argv[1] if len(sys.argv) > 1 else "EDC17")
