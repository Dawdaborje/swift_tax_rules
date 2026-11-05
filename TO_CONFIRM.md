# Rules to confirm

Every pack under `countries/` is `"verified": false` except those listed under *Verified* below. The figures were written from recollection of each
authority's published rates, **not** read from the source at the time of writing, and the tests in each pack
only prove that the expression matches the figures in its description, not that the figures match the law.
Do not run real payroll on these until someone has checked them against the source and set `verified: true`.

Odoo's payroll localisations (OEEL-1, proprietary) were used only to learn which parameters a country needs.
Nothing was copied from them.

## Verified (read from the official source on 2026-11-05)
`ke.paye.2025` (KRA page: bands to 35%, relief 2,400 a month), `ke.housing_levy.2024` (KRA notice 2099),
`ke.nssf.2026` (NSSF Year 4 notice, hosted copy), `ke.shif.2024` (SHA premium page), `gh.paye.2026` (GRA page), `ng.paye.2026` (Nigeria Tax Act 2025, Fourth Schedule and s.30, gazette copy), `ug.paye.2026` (URA PAYE rates page after the Income Tax (Amendment) Act 2026; gazetted Act not read), `ng.pension_employee.2014` (Pension Reform Act 2014 s.4(1) and s.120, gazetted copy).
`gh.paye.2024` is retired on 2026-08-31 and stays unverified. Still open: GRA's effective date (the page says
1 September 2026 under the annual table only), the text of Act 1178, Ghana tax reliefs, Kenya insurance relief.

## What to check, per pack

| Pack | Check against | Open points |
|---|---|---|
| `gh.ssnit_employee.2024` | SSNIT | 5.5% employee seen only in a search snippet of ssnit.org.gh; the insurable-earnings ceiling (vendors say 69,000 a month from 2026) needs an official SSNIT notice and is not applied. |
| `ng.nhf.1992` | FMBN, Business Facilitation (Miscellaneous Provisions) Act 2022 s.45 | 2.5% rate; whether private-sector contribution is now voluntary and whether the base is basic salary or monthly income. FMBN's copy of the Act could not be opened. |
| `ug.nssf_employee.2023` | NSSF Act (Uganda), nssfug.org | 5% employee and 10% employer seen only in NSSF's sustainability report; whether a ceiling applies (vendors disagree); the Act itself. |
| `eg.paye.2024` | Egyptian Tax Authority | Bands and the 20,000 exemption, and whether it comes off income or tax. Social insurance not written. |
| `ma.paye.2025` | DGI Morocco | Bands; family and professional-expense deductions not modelled. |
| `pk.paye.2026` | FBR | Slabs for tax year 2026; the surcharge above 10 million is not modelled. |
| `in.paye.2025` | Income Tax Department | New-regime slabs; the 75,000 standard deduction, the 87A rebate (nil tax to 1,200,000), surcharge and 4% cess are not modelled. |
| `my.paye.2023` | LHDN | Resident bands; reliefs and monthly MTD tables not modelled. |
| `id.pph21.2022` | DJP | Progressive rates; PTKP and the 2024 TER monthly method not modelled. |
| `tr.paye.2025` | GIB | 2025 brackets; Turkey is cumulative through the year, so the annualised form is approximate. |
| `bd.paye.2025` | NBR | Slabs for assessment year 2025-26; different thresholds for women, senior citizens and others. |
| `hk.salaries_tax.2024` | IRD | Rates and the standard-rate cap; allowances belong off income, not off tax as modelled. |

## Countries Odoo has that have no pack yet
`ae`, `sa` (no income tax; social insurance only), `jo`, `au`, `us`, `mx`, `be`, `fr`, `nl`, `pl`, `ro`, `sk`, `lt`, `lu`, `ch`.
Each needs a source read first. Several (US, Switzerland, Belgium, France) depend on filing status, region or
commune and need more inputs than one rule takes.

## Countries in the README with no usable pack
- `gm` (Gambia): `countries/gm/paye_2025.cel` is empty and has no description. No figures were written, because
  the secondary sources found (October 2026) disagree:
  - tax-free threshold of 12,000, 24,000 or 36,000 a year (36,000 said to apply from 1 January 2025);
  - top rate of 25% or 30%, with 5% to 25% in steps in one source and 15% / 25% / 30% above 72,000 in another;
  - employee SSHFC contribution of 5% of basic salary in most sources, 10% in one;
  - Industrial Injuries Compensation Fund: 1% of earnings, capped at 15 a month, employer-paid.
  The Gambia Revenue Authority's current monthly tax table settles all of these. Write the pack from that.
- `ng`: now has packs (above).
