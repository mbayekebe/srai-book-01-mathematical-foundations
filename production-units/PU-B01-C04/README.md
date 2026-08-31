# PU-B01-C04 - Matrix Algebra and Linear Systems

Controlled release v1.0.0.

This production unit provides the independently reviewed and reproducibly validated assets for Lesson 4 of SRAI Book 1 - Mathematical Foundations:

- audited controlled chapter in DOCX and PDF;
- executable notebook v0.1.3 and complete srai_math source;
- educational exercises and complete solutions in DOCX and PDF;
- Executive Brief in DOCX and PDF;
- editable 16-slide video lesson deck v1.2 using the verified SRAI visual system;
- complete audience-facing narration for all 16 slides;
- targeted mathematical tests and independent-review evidence.

## Video lesson

YouTube: https://youtu.be/IBTHb6iWROk

Approved video master: v1.1
Duration: 00:13:33
SHA-256: 83b5fe465f24173677749f9caa2eb05c677cc0e2f810b90cf4c9d075f47ae025

## Local notebook setup

From the extracted package root, run:

    py -m pip install -e ".[dev]"

Then open:

    notebooks/M1/M1_N04_matrix_algebra_linear_systems_v0.1.3.ipynb

## Verification

Run the controlled mathematical tests with:

    py -m pytest tests -q

Verify package files against SHA256SUMS.txt before use.

## Control status

The chapter, notebook, exercises, Executive Brief, presentation, narration and video master have passed their applicable review and production gates. This unit is approved for controlled GitHub release and subsequent SRAI website integration.
