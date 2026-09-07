# PU-B01-C06 — Eigenvalues, Eigenvectors and Spectral Intuition

Published controlled release v1.0.0 for SRAI Book 1 — Mathematical Foundations.

The PDF and editable-document filenames retain the approved source-asset versions. The production-unit release number does not imply that those source files were independently audited or substantively revised.

## Released resources

- [GitHub release v1.0.0](https://github.com/mbayekebe/srai-book-01-mathematical-foundations/releases/tag/pu-b01-c06-v1.0.0)
- [Controlled chapter PDF](docs/PU-B01-C06_Chapter6_Controlled_Candidate_v0.1.0.pdf)
- [Canonical notebook](notebooks/M1/M1_N06_eigenvalues_eigenvectors_spectral_intuition_v0.1.0.ipynb)
- [Exercises and solutions PDF](docs/PU-B01-C06_Exercises_and_Solutions_v0.1.0.pdf)
- [Executive Brief PDF](docs/PU-B01-C06_Executive_Brief_v0.1.0.pdf)
- [Video lesson deck](slides/PU-B01-C06_Lesson6_Teaching_Deck_v0.1.2.pptx)
- [Public video lesson](https://youtu.be/a3jAhbDX2A0)

## VS Code

Open the production-unit directory, use Python 3.11+ and create a dedicated virtual environment. Install `requirements.txt`, select that interpreter as the notebook kernel, restart the kernel and run all cells. Keep `wheels/` in the production-unit directory.

## Google Colab

Upload the notebook and run all cells in a fresh runtime. Its bootstrap downloads the exact public `srai_math` wheel and verifies its SHA-256. Internet access is required. Do not remove the hash check or substitute another runtime.

Expected final notebook message:

```text
LESSON 6 NOTEBOOK CHECKS: PASS
```

## Runtime and evidence

`srai_math 1.1.1rc1` is an explicitly accepted prerelease. The notebook handles its documented eigenpair and power-iteration limitations. Owner-reported VS Code and Colab success is distinct from historical developer tests and from independent review.

All sample data are synthetic. Explained variance is not accuracy; sector weights are not budget recommendations.

## Verification

From the production-unit directory:

```powershell
python tools/verify_candidate.py
python -m unittest discover -s tests -v
```

The verification command checks file hashes and notebook markup; it does not change the review status.

## Control status

Lesson 6 is published on the SRAI website and preserved through the qualified GitHub release above. See `RIGHTS_AND_REUSE.md`, `RELEASE_RECORD.md`, `VALIDATION_REPORT.json` and `evidence/` for the governing records and limitations.
