# PU-B01-C03 — Vector Foundations

Controlled production baseline for SRAI Book 1, Lesson 3.

## Current approved assets

The owner-approved chapter and canonical notebook are:

- `docs/PU-B01-C03_Chapter3_Vector_Foundations_Audited_Controlled_Edition_v1.0.docx`
- `notebooks/M1_N03_vector_foundations.ipynb`

The chapter audit and notebook validation evidence is recorded in:

- `CHAPTER_AND_NOTEBOOK_AUDIT_REPORT.md`
- `VALIDATION_REPORT.json`

## Notebook scope

M1_N03 covers vector arithmetic, norms, distance, dot products, angles, cosine
similarity, projection and rejection, span, cross products, Gram–Schmidt
orthogonalization, statistical data matrices and a synthetic decision-intelligence
case. It includes zero-vector safeguards and preprocessing-sensitivity checks.

## Local validation

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
python -m unittest discover -s tests -v
python scripts/validate_notebook.py
```

## Google Colab

Open `notebooks/M1_N03_vector_foundations.ipynb` in a clean Colab runtime. Install
`requirements-colab.txt`, make the controlled `srai_math` package available, restart
the runtime if requested, and run all cells. Colab validation remains a release gate
until owner-confirmed.

## Production status

Baseline version `0.1.0` records the approved chapter, approved notebook and locally
validated vector package. It is not the final Lesson 3 release. The chapter PDF,
standalone exercises and solutions, Executive Brief, platform assets, clean Colab
validation and final release package remain pending.
