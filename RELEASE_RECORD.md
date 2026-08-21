# PU-B01-C01 technical release record

| Field | Value |
|---|---|
| Production unit | PU-B01-C01 |
| Release | 1.0.0 release candidate |
| Date assembled | 2026-08-21 |
| Owner | Mbaye Kebe |
| Status | Private technical release candidate; owner review pending |
| Canonical notebook | `notebooks/M1_N01_mathematical_thinking.ipynb` |

## Included controlled assets

- GitHub landing page / `README.md` v1.0
- canonical notebook M1_N01
- minimal `srai_math` reproducibility utilities required by the notebook
- Executive Brief v1.1 PDF
- Educational Exercises and Solutions v1.0 PDF
- validation script and GitHub Actions workflow
- citation, rights, manifest and checksums

## Validation criteria

The release candidate is acceptable when:

1. every notebook code cell executes sequentially from a clean namespace;
2. predictions equal `[170.0, 182.5, 195.0]`;
3. the sensitivity output equals `[2.5]`;
4. the recorded seed equals `42`;
5. expected notebook assertions pass;
6. required files and internal Markdown links resolve; and
7. SHA-256 checksums match the packaged files.

## Publication control

This package is not yet authorized for public release. Before publication, confirm the final repository name and URL, owner approval, licence decision, public contact channel, tested GitHub workflow, release tag and cross-links to the SRAI website, LinkedIn announcement and YouTube channel.
