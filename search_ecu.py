#!/usr/bin/env python3
"""Search supported Cars, Heavy-Duty Trucks & Marine ECUs in DaVinci Deluxe Cloud Edition."""
import json, pathlib, sys
BASE = pathlib.Path(__file__).parent / "data"
q = (sys.argv[1] if len(sys.argv) > 1 else "EDC17").upper()
for label, fname in [("Cars", "cars_supported_ecus.json"), ("Trucks", "trucks_supported_ecus.json")]:
    fp = BASE / fname
    if fp.exists():
        d = json.loads(fp.read_text("utf-8"))
        hits = {b: [e for e in ecus if q in e.upper()] for b, ecus in d.get("byBrand", {}).items()}
        hits = {b: m for b, m in hits.items() if m}
        print(label, "matches:", len(hits))
