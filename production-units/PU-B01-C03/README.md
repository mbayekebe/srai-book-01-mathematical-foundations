# PU-B01-C03 - Vector Foundations

Controlled Production Unit for SRAI Book 1, Lesson 3.

## Controlled learning package

- [Audited Chapter 3 DOCX](docs/PU-B01-C03_Chapter3_Vector_Foundations_Audited_Controlled_Edition_v1.0.docx)
- [Controlled Chapter 3 PDF](docs/PU-B01-C03_Chapter3_Vector_Foundations_Audited_Controlled_Edition_v1.0.pdf)
- [Exercises and Solutions DOCX](docs/PU-B01-C03_Exercises_and_Solutions_v1.0.docx)
- [Exercises and Solutions PDF](docs/PU-B01-C03_Exercises_and_Solutions_v1.0.pdf)
- [Executive Brief DOCX](docs/PU-B01-C03_Executive_Brief_v1.0.docx)
- [Executive Brief PDF](docs/PU-B01-C03_Executive_Brief_v1.0.pdf)
- [Canonical notebook](notebooks/M1_N03_vector_foundations.ipynb)
- [Audit report](CHAPTER_AND_NOTEBOOK_AUDIT_REPORT.md)
- [Validation report](VALIDATION_REPORT.json)
- [Controlled release record](RELEASE_RECORD.md)

## Scope

The unit covers vector representation, arithmetic, norms, distance, dot products,
angles, cosine similarity, projection and rejection, span, Gram-Schmidt
orthogonalization, data matrices and a synthetic decision-intelligence case. It
includes dimension checks, zero-vector safeguards, numerical invariants and
preprocessing-sensitivity analysis.

## Reproduce locally

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
python -m unittest discover -s tests -v
python scripts/validate_notebook.py
python scripts/build_release.py
```

## Google Colab validation

The owner opened `notebooks/M1_N03_vector_foundations.ipynb` in a clean Colab
runtime, installed the controlled `srai_math` package and ran all cells on
2026-08-30. All cells completed without red errors; formulas, tables and charts
rendered correctly.

## Coordinated lesson

- YouTube: https://www.youtube.com/watch?v=THvzO5_L-Zs
- Planned lesson page: https://srai.mbayekebe.net/learn/pu-b01-c03/

## Release status

Version `1.0.0` is the approved final controlled release. All document,
computational, visual, owner-review and clean Google Colab gates pass.
