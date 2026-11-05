#!/usr/bin/env python3
"""Zip the rule packs (stored, no compression) for a plugin's assets folder.

    python3 scripts/pack_zip.py ../aether_software/plugins/hrms/hr_payroll/assets/rule_packs.zip

Only packs with both a `.cel` and a `.json` next to each other are included; stubs are skipped and listed.
"""
import pathlib, sys, zipfile

root = pathlib.Path(__file__).resolve().parent.parent / "countries"
out = pathlib.Path(sys.argv[1])
out.parent.mkdir(parents=True, exist_ok=True)
count = 0
with zipfile.ZipFile(out, "w", zipfile.ZIP_STORED) as z:
    for cel in sorted(root.rglob("*.cel")):
        meta = cel.with_suffix(".json")
        if not meta.exists() or cel.stat().st_size == 0:
            print("skipped (incomplete):", cel.relative_to(root))
            continue
        for f in (cel, meta):
            z.write(f, f.relative_to(root).as_posix())
        count += 1
print(f"{count} packs -> {out}")
