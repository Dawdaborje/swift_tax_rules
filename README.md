# Swift Tax Rules

Open tax and contribution rules for payroll, written as data and as expressions in a small CEL-style
language, so a rule can be read, reviewed and tested without reading a program. Built for the
[Swift Payroll Engine](../swift_payroll_engine) (it runs them; Odoo keeps the same kind of rule as XML
inside modules, ERPNext as spreadsheet-like tables).

## A rule pack

Two files side by side:

* `paye_2025.cel` — one expression that gives the amount for **one pay period**. Numbers are exact
  decimals (never binary floating point). `bracket(x, [[upper, rate], ...])` is progressive tax by bands.
* `paye_2025.json` — what it is: country, kind, validity dates, **source** (the law it follows),
  **verified** (true only once someone has checked every figure against that source), the names it reads,
  its tables, and **tests** with the expected results.

See `countries/example/` for a complete pack and `schemas/tax_rule.schema.json` for the format.

## Sources and what a test proves

* `source` in each pack cites the law or notice. `source_files` lists the saved copy of it under
  [`sources/`](sources), each with its SHA-256 and the URL and date it was read in
  [`sources/MANIFEST.json`](sources/MANIFEST.json). Pages change; the saved copy is what the pack was checked
  against. `python3 scripts/verify_sources.py` checks the hashes and that every verified pack has its sources.
* Each test says where its expected value comes from, in `origin`: `authority` (a figure or worked example the
  tax authority prints, with `source_ref` saying where), `secondary` (a third party's example) or `calculated`
  (worked out by hand from the source's rates). A `calculated` test shows the expression applies the cited
  figures correctly; it does not show the source gives that result. Packs not yet reviewed have no `origin`.

## Checking

```bash
cd ../swift_payroll_engine
cargo run -p swift_payroll_engine -- check-rules ../swift_tax_rules/countries
```

Every pack loads, its expression is parsed, and its tests run; a pack with no tests fails. A pack that is
not `verified` is reported as such: do not pay anyone with one.

## Countries

Packs checked against an official source (see each pack's `source`): Kenya (ke: PAYE, NSSF, SHIF, housing
levy), Ghana (gh: PAYE 2026), Nigeria (ng: PAYE, pension), Uganda (ug: PAYE 2026), The Gambia (gm: PAYE) and
Senegal (sn: income tax, TRIMF, employer contribution).

Packs written but **unverified**; see [TO_CONFIRM.md](TO_CONFIRM.md) before using any of them: Ghana SSNIT,
Gambia SSHFC, Senegal IPRES and CSS (written from a secondary source), Bangladesh (bd), Egypt (eg), Hong Kong (hk), Indonesia (id), India (in), Morocco (ma),
Malaysia (my), Nigeria NHF, Pakistan (pk), Turkey (tr), Uganda NSSF.

`example/` holds demonstration packs with illustrative figures, including `gm.paye.demo` and
`gm.social.demo` (Gambian shape, invented numbers). Not law.

**Adding a country needs the official schedule** (the revenue authority's notice or the Finance Act
section) so that `source` can cite it and the tests are worked from it. Figures from memory do not belong
here.
