# PU-B01-C01 coordinated release record

| Field | Value |
|---|---|
| Production unit | PU-B01-C01 |
| Release | 1.0.1 |
| Date assembled | 2026-08-30 |
| Owner | Mbaye Kebe |
| Status | APPROVED FINAL CONTROLLED RELEASE |
| Audited chapter | `docs/SRAI_Book1_Chapter1_Audited_Controlled_Edition_v1.0.pdf` |
| Canonical notebook | `notebooks/M1_N01_mathematical_thinking.ipynb` |
| YouTube lesson | https://www.youtube.com/watch?v=q4wa_3KRGUo |
| Video duration | 12:36 |

## Included controlled assets

- audited Chapter 1 controlled-edition PDF v1.0
- GitHub landing page / `README.md` v1.1
- canonical notebook M1_N01
- minimal `srai_math` reproducibility utilities required by the notebook
- Executive Brief v1.1 PDF
- Educational Exercises and Solutions v1.0 PDF
- 12:36 published YouTube lesson
- local and Google Colab setup controls
- validation script
- citation, rights, manifest and checksums

## Validation criteria

The release candidate is acceptable when:

1. every notebook code cell executes sequentially from a clean namespace;
2. predictions equal `[170.0, 182.5, 195.0]`;
3. the sensitivity output equals `[2.5]`;
4. the recorded seed equals `42`;
5. expected notebook assertions pass;
6. required files and internal Markdown links resolve; and
7. chapter, notebook, video and landing-page claims are substantively aligned; and
8. SHA-256 checksums match the packaged files.

## Publication control

Version 1.0.1 is the approved final controlled metadata and packaging repair release. Owner approval was confirmed on 2026-08-30. This patch aligns the release record with the already published Lesson 1, adds a self-contained rights statement, generates a versioned release ZIP and refreshes validation controls. It does not alter the approved chapter, notebook, exercises, Executive Brief or YouTube lesson.
