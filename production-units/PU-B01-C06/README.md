# SRAI Lesson 6 - Eigenvalues, Eigenvectors and Spectral Intuition

Book 1: Mathematical Foundations. Production unit PU-B01-C06.
Proposed release v1.0.0. This is an assembled integration candidate; publication is a separate gate.

## Learn and run
Read docs/PU-B01-C06_Chapter6_Controlled_Candidate_v0.1.0.pdf, then open
notebooks/M1/M1_N06_eigenvalues_eigenvectors_spectral_intuition_v0.1.0.ipynb.
The PDF/editable filenames retain the actual approved asset versions; package v1.0.0
does not imply that their contents were revised or independently audited.
Exercises and the Executive Brief are in docs/. The 28-slide presentation in slides/
contains full audience-facing speaker notes. Video: https://youtu.be/a3jAhbDX2A0

## VS Code
Extract the full package. Open its root folder in VS Code. Use Python 3.11+ and create
a dedicated virtual environment. Install requirements.txt with that interpreter,
select it as the notebook kernel, restart and Run All. Keep wheels/ in this folder.
Follow evidence/original_candidate_README.md for detailed setup and troubleshooting.

## Google Colab
Upload the notebook alone to Colab and Run All in a fresh runtime. Its bootstrap
downloads the exact public srai_math wheel and checks the expected SHA-256.
Internet access is required. Do not remove the hash check or substitute a runtime.
Expected final notebook message: LESSON 6 NOTEBOOK CHECKS: PASS.

## Runtime and evidence
srai_math 1.1.1rc1 is an explicitly accepted prerelease, unchanged from the candidate.
The notebook visibly handles the runtime's known eigenpair/power-iteration limitations.
Owner-reported VS Code/Colab success is recorded separately from historical developer
tests. Preserve those historical reports; their pending fields describe their dates.
No independent review, public URL validation or server deployment is asserted here.
All sample data are synthetic. Explained variance is not accuracy; sector weights
are not budget recommendations.

## Integrity
From this folder run: python tools/verify_candidate.py
This verifies file hashes and notebook markup; it does not grant publication approval.
For the mathematical tests after dependency setup: python -m unittest discover -s tests -v
See RIGHTS_AND_REUSE.md and RELEASE_RECORD.md before redistribution.
