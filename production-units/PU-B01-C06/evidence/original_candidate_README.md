# Lesson 6 notebook candidate — v0.1.0

**Eigenvalues, Eigenvectors, and Spectral Intuition · PU-B01-C06**

Start with `notebooks/M1/M1_N06_eigenvalues_eigenvectors_spectral_intuition_v0.1.0.ipynb`.
This is a notebook/runtime review package, not the completed lesson release. The chapter, standalone exercise document, Executive Brief, slides, video and publication records will follow. Do not upload this ZIP as the final Lesson 6 release.

## What is included

- Expanded notebook with derivations, illustrated examples, ten exercises and worked solutions.
- Exact `srai_math` 1.1.1rc1 wheel and its corresponding source archive.
- Requirements, explicit lesson-level residual safeguards, mathematical tests and markup validator.
- Source identities, change record, execution evidence and SHA-256 file inventory.

## Windows / VS Code — first run

1. Extract the ZIP to a new folder, outside existing production folders. Do not run files inside the ZIP viewer.
2. In VS Code, choose **File → Open Folder** and select the extracted folder containing this README.
3. Install/enable the Microsoft Python and Jupyter extensions if absent. Use Python 3.11 or later; 3.12 is the development test target.
4. Open **Terminal → New Terminal**, choose PowerShell, and run these commands separately. Stop on any error:

```powershell
py -3.12 -m venv .venv
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt
& .\.venv\Scripts\python.exe -m pip check
& .\.venv\Scripts\python.exe -m unittest discover -s tests -v
& .\.venv\Scripts\python.exe tools\validate_srai_notebook_markup.py notebooks\M1\M1_N06_eigenvalues_eigenvectors_spectral_intuition_v0.1.0.ipynb
```

If Python 3.12 is not installed, use an installed Python 3.11+ interpreter explicitly rather than guessing which `python` command is active. Dependency installation requires Internet access. No environment activation or execution-policy bypass is needed for the commands above.

5. Open the notebook. At its upper right select **Select Kernel → Python Environments** and choose this folder's `.venv` interpreter.
6. Choose **Restart → Run All**. Expected final message: `LESSON 6 NOTEBOOK CHECKS: PASS`. Inspect all rendered equations and both figures; errors must not be ignored.
7. The runtime bootstrap searches for the wheel in the current directory and two parent levels. Opening the whole extracted folder supports both a package-root and a notebook-directory kernel. If the wheel is absent it attempts the pinned public download, not an arbitrary PyPI package.

## Google Colab — notebook-only use

1. Visit https://colab.research.google.com/ and choose **File → Upload notebook**.
2. Select the `.ipynb` from the extracted package. No manual wheel upload or Drive mount is required.
3. Connect a fresh Python runtime, review the two setup cells, then choose **Runtime → Run all**.
4. The first cell downloads the exact runtime from the previously configured public GitHub release and checks its SHA-256. The next cell installs any missing/out-of-range numerical dependencies using the current kernel's Python.
5. Wait for the final PASS and inspect all equations, tables and figures. Record the environment, date and notebook hash. Download the executed notebook as evidence if reviewing this candidate.

The notebook's public runtime URL is:
https://github.com/mbayekebe/srai-book-01-mathematical-foundations/releases/download/srai-math-v1.1.1rc1/srai_math-1.1.1rc1-py3-none-any.whl

**Do not mistake a configured URL for a verified download.** See `evidence/VALIDATION_REPORT.json` for the developer's actual network/execution results. Live Colab and Windows VS Code acceptance must still be recorded. A release-tag-based “Open in Colab” badge can be added only after Lesson 6 is actually published; this candidate invents no public Lesson 6 URL.

## Runtime boundaries and reproducibility

The bundled prerelease wheel is unchanged from Lesson 5. Expected SHA-256:
`6e7033465ad3d9bf4650227a11be0380512a44fd476a83d5828ad4ec4f07e923`.
Its source archive accompanies it. Lesson 5's approval is not automatically Lesson 6 approval. The owner must confirm reuse/rights and the explicit treatment of its known spectral limitations before public release. No new license grant is made by this candidate.

The wheel's `verify_eigenpair` accepts zero vectors; its legacy `power_iteration` can stop on a stabilized scalar without a small residual. The notebook uses its own visible, tested residual functions for those two jobs. Other spectral calculations use the actual bundled `srai_math` functions. The lesson does not redefine the shared package or claim that every library function was audited.

`tools/lesson6_reference.py` duplicates the tagged reference-function cell exactly (apart from its NumPy import); a consistency test protects against divergence. These small dense real-matrix iteration routines are teaching code, not a general sparse/complex iterative solver. The residual checker supports complex eigenpairs.

The requirements declare supported ranges, not a guarantee for every possible combination. Exact observed versions are recorded in execution evidence. All examples use synthetic data. All equations use ordinary Markdown with inline dollar delimiters and standalone double-dollar display blocks; automatic markup checks do not replace human rendering review.

## If something fails

| Symptom | Safe action |
|---|---|
| Wrong kernel / missing NumPy | Select the intended `.venv`; install requirements with its Python |
| Runtime download times out | Check public URL/connectivity; in VS Code keep bundled `wheels` in place; do not substitute an unverified version |
| SHA-256 mismatch | Stop; redownload from the approved source and reconcile identity; never disable the check |
| Another `srai_math` already loaded | Restart kernel and Run all; do not delete modules to bypass the guard |
| An imported dependency needs updating | Restart first, rerun setup; if pip requests another restart, do so |
| Power iteration refuses convergence | Check assumptions/start/iteration limit; do not convert an exception into a passing result |
| Eigenvectors differ only by sign | Compare residuals and eigenspaces, not signed columns |
| Raw equation delimiters appear | Confirm Markdown cell type and renderer; stop acceptance and report the section |
| Test/assertion fails | Preserve the error and environment; do not weaken tolerances without mathematical justification |

After a fresh extraction, `python tools/verify_candidate.py` checks the file inventory and notebook markup. It does not execute a notebook or grant release approval. To repeat the mathematical tests use `python -m unittest discover -s tests -v` after installing requirements.

## Owner acceptance still required

Clean local and live Colab runs, visual markup review, chapter/notebook alignment, runtime reuse approval, qualified mathematical review and all publication approvals remain explicit gates. No Git, website, Studio or production-server changes are made by this package.
