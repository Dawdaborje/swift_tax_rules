# Rules to confirm

Every pack under `countries/` is `"verified": false` except those listed under *Verified* below. The figures were written from recollection of each
authority's published rates, **not** read from the source at the time of writing, and the tests in each pack
only prove that the expression matches the figures in its description, not that the figures match the law.
Do not run real payroll on these until someone has checked them against the source and set `verified: true`.

Odoo's payroll localisations (OEEL-1, proprietary) were used only to learn which parameters a country needs.
Nothing was copied from them.

## Verified (read from the official source on 2026-11-05)
`ke.paye.2025` (KRA page: bands to 35%, relief 2,400 a month), `ke.housing_levy.2024` (KRA notice 2099),
`ke.nssf.2026` (NSSF Year 4 notice, hosted copy), `ke.shif.2024` (SHA premium page), `gh.paye.2026` (GRA page), `ng.paye.2026` (Nigeria Tax Act 2025, Fourth Schedule and s.30, gazette copy), `ug.paye.2026` (URA PAYE rates page after the Income Tax (Amendment) Act 2026; gazetted Act not read), `gm.paye.2025` (GRA PAYE brochure; its text still says 'as at January 2018'; the 2025 start is corroborated by Sage and Payspace summaries; the Finance Acts were not found), `sn.ir.2025`, `sn.trimf.2025`, `sn.cfce.2025` (CGI January and October 2025 editions; Loi 2025-17 and the LFI 2026 checked on 2026-11-05 and do not change these articles; the 2026 amending bill was rejected on 3 November 2026), `ng.pension_employee.2014` (Pension Reform Act 2014 s.4(1) and s.120, gazetted copy).
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

| `gm.sshfc_employee.2025` | SSHFC, SSHFC Act | 5% employee, 10% employer of basic salary from payroll guides only; housing, health and injury-fund contributions disagree between sources. |
| `sn.ipres_*`, `sn.css_*` | IPRES (ipres.sn, secusociale.ipres.sn), Caisse de Sécurité Sociale, the decrees | Written 2026-11-05 from CLEISS (a French public body) 'as at 1 January 2026' only, because the Senegalese sites could not be reached. Need the official notice or decree for: general scheme 5.6% employee / 8.4% employer with a 432,000 monthly ceiling (the IPRES guide showed 360,000 from 2017); managers' scheme 2.4% / 3.6% between 432,000 and 1,296,000; CSS family benefits 7% up to 63,000; work-injury 1/3/5% up to 63,000; the SMIG floor; who counts as a cadre. Not written: health insurance (IPM, 2% to 7.5% each side, ceiling 250,000 per CLEISS, rate set by the institution). |
| `sn.ir.2025` | DGID | The reading of the art. 174 reduction (rate x tax kept between minimum and maximum); whether monthly withholding uses the annual computation divided by 12; a monthly withholding table, if the DGID publishes one. |

## Countries Odoo has that have no pack yet
`ae`, `sa` (no income tax; social insurance only), `jo`, `au`, `us`, `mx`, `be`, `fr`, `nl`, `pl`, `ro`, `sk`, `lt`, `lu`, `ch`.
Each needs a source read first. Several (US, Switzerland, Belgium, France) depend on filing status, region or
commune and need more inputs than one rule takes.

## Countries in the README with no usable pack
- `gm` (Gambia): now has `gm.paye.2025` (verified against the GRA PAYE brochure) and `gm.sshfc_employee.2025` (unverified).
- `ng`: now has packs (above).
