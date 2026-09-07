# PU-B01-C04 — Matrix Algebra and Linear Systems

Controlled release v1.0.0.

This production unit provides the independently reviewed and reproducibly validated assets for Lesson 4 of SRAI Book 1 — Mathematical Foundations:

- audited controlled chapter in DOCX and PDF;
- executable notebook v0.1.3 and complete `srai_math` source;
- educational exercises and complete solutions in DOCX and PDF;
- Executive Brief in DOCX and PDF;
- editable 16-slide video lesson deck v1.2 with audience-facing narration;
- targeted mathematical tests and independent-review evidence.

## Released resources

- [GitHub release v1.0.0](https://github.com/mbayekebe/srai-book-01-mathematical-foundations/releases/tag/pu-b01-c04-v1.0.0)
- [Controlled chapter PDF](docs/PU-B01-C04_Chapter4_Matrix_Algebra_and_Linear_Systems_Audited_Controlled_Edition_v1.0.pdf)
- [Canonical notebook](notebooks/M1/M1_N04_matrix_algebra_linear_systems_v0.1.3.ipynb)
- [Exercises and solutions PDF](docs/PU-B01-C04_Educational_Exercises_and_Solutions_v1.0.pdf)
- [Executive Brief PDF](docs/PU-B01-C04_Executive_Brief_v1.0.pdf)
- [Video lesson deck](video/PU-B01-C04_Video_Lesson_Deck_v1.2.pptx)
- [Public video lesson](https://youtu.be/IBTHb6iWROk)

## Video evidence

Approved video master: v1.1  
Duration: 00:13:33  
SHA-256: `83b5fe465f24173677749f9caa2eb05c677cc0e2f810b90cf4c9d075f47ae025`

## Local notebook setup

From the production-unit directory:

```powershell
py -m pip install -e ".[dev]"
```

Then open:

```text
notebooks/M1/M1_N04_matrix_algebra_linear_systems_v0.1.3.ipynb
```

## Verification

Run the controlled mathematical tests with:

```powershell
py -m pytest tests -q
```

Verify package files against `SHA256SUMS.txt` before use.

## Control status

The chapter, notebook, exercises, Executive Brief, presentation, narration and video master passed their applicable review and production gates. The production unit is published on the SRAI website and preserved through the qualified GitHub release above.
