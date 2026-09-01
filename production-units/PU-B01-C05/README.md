# Lesson 5 — owner-authorized release preparation

The owner approved the chapter, notebook, exercises, Executive Brief, slide deck
and 16-minute video, and explicitly authorized public release without a separate
independent review. This is an owner-approved exception, not independent signoff.

Runtime: srai_math 1.1.1rc1 is a disclosed prerelease, pinned by SHA-256.
It has not been promoted or renamed as a stable runtime.

Video: https://www.youtube.com/watch?v=tZtdYcMEaIQ

Authority: evidence/RELEASE_AUTHORIZATION.json.
Final release packaging, GitHub publication, website verification and
communications closeout remain outstanding.

The following candidate instructions are preserved as historical context.
Any pending-owner-approval or no-publication-authorization statements below
are superseded by the authorization record above.

---

# Lesson 5 — controlled asset production candidate v0.1.0

Vector Spaces, Bases, Rank and Projections · PU-B01-C05

## Start here

Extract this ZIP into a new folder. Do not merge it into an earlier candidate or a Git repository yet. Preserve the previous packages.

Review these new production assets before recording:

- `docs/PU-B01-C05_Educational_Exercises_and_Solutions_v1.0.pdf` — 12 questions with complete worked solutions; editable DOCX beside it.
- `docs/PU-B01-C05_Executive_Brief_v1.0.pdf` — decision-facing interpretation and controls; editable DOCX beside it.
- `video/PU-B01-C05_Video_Lesson_Deck_v1.0.pptx` — 16 slides following the established Lesson 1/4 visual system. Each slide has a complete spoken narration, not instructions to the presenter.

`video/PU-B01-C05_Narration_v1.0.txt` provides the same 1,950-word narration separately. Allow roughly 15–18 minutes at an unhurried pace; actual recording duration will vary.

The controlled chapter is in `docs/`. Its mathematical paragraphs are preserved from the owner-approved chapter candidate. Only control labels and the final status note changed. The notebook is the exact owner-approved v0.2.2 file in `notebooks/M1/`.

## Notebook: no manual runtime upload required

Open the notebook in Colab and use a fresh runtime, then Run all. Its setup downloads the exact public `srai_math` wheel automatically, verifies its SHA-256 and installs it into a temporary target for that kernel. There is no embedded Base64 payload and no request to upload a wheel. Internet access and a working Colab runtime connection are required.

In VS Code, select the intended Python kernel. The setup uses the wheel if it is available in a `wheels` folder beneath the kernel's working directory; otherwise it uses the same verified public download. Numerical dependencies such as NumPy and Matplotlib must already be available. A previously imported different `srai_math` requires a kernel restart. Do not bypass operating-system security policy if an environment blocks execution.

The included wheel and source ZIP are unchanged copies of runtime `1.1.1rc1`. This is a prerelease, not a stable-version promotion. Do not rename it or silently substitute another runtime.

## Where everything is

- `ASSET_INDEX.json`: exact asset paths, sizes and hashes.
- `SHA256SUMS.txt`: integrity checks for all distributed files except itself.
- `evidence/`: owner statements, chapter-preservation check, notebook execution and markup evidence, mathematical tests, slide-template map and fidelity check.
- `VALIDATION_REPORT.json`: what was verified and which gates remain open.
- `tests/`: prior numerical tests, Lesson 5 regression checks and new worked-example checks.
- `runtime_source/`: matching runtime source archive.

## Optional read-only verification

From this extracted package's root:

```bat
py verify_package.py
```

With NumPy available, also run:

```bat
py verify_package.py --mathematics
```

The second command checks 20 unittest cases using the bundled wheel directly, without installing a package. The builder also ran all 50 pytest cases, including the 30 preserved core tests. Neither command commits, pushes or updates approval records.

## Approval boundary

The owner approved the chapter and notebook and authorized asset production. The new exercises, brief and deck still require owner review. No independent reviewer sign-off is recorded for Lesson 5. Successful code execution is not independent review. No video, lesson release, website deployment or public publication is authorized by this candidate.

No repository was changed by producing this package. Record the reviewed asset hashes and the approval decision in Operations before advancing to video production and release preparation. The asset index is a package index, not a replacement for the Operations lesson manifest.
