#!/usr/bin/env python3
"""Check the saved sources: every file in sources/MANIFEST.json exists and matches its SHA-256, and every
`source_files` entry of a pack is in the manifest. Run from anywhere: python3 scripts/verify_sources.py"""
import hashlib, json, pathlib, sys

root = pathlib.Path(__file__).resolve().parent.parent
manifest = json.loads((root / "sources" / "MANIFEST.json").read_text())
listed = {f["path"]: f for f in manifest["files"]}
problems = []
for path, f in listed.items():
    file = root / "sources" / path
    if f.get("stored") is False:
        continue  # too large to keep; the manifest records its hash and URL only
    if not file.exists():
        problems.append(f"missing: {path}")
    elif hashlib.sha256(file.read_bytes()).hexdigest() != f["sha256"]:
        problems.append(f"changed: {path}")
for pack in sorted((root / "countries").glob("*/*.json")):
    info = json.loads(pack.read_text())
    for p in info.get("source_files", []):
        if p not in listed:
            problems.append(f"{pack.relative_to(root)}: source_files entry not in the manifest: {p}")
    if info.get("verified") and not info.get("source_files"):
        problems.append(f"{pack.relative_to(root)}: verified but has no source_files")
print("\n".join(problems) if problems else f"ok: {len(listed)} source files, all packs consistent")
sys.exit(1 if problems else 0)
