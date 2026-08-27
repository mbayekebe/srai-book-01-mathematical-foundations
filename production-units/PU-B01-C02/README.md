# PU-B01-C02 — Sets, Logic, Relations and Functions

Controlled final release for SRAI Book 1, Lesson 2.

## Video lesson

Watch the coordinated long-form lesson on the official SRAI YouTube channel:

**[Sets, Logic, Relations and Functions | SRAI Book 1, Lesson 2](https://youtu.be/VYXyB1-wUFs)**

## Exercises and solutions

The controlled practice package provides 16 graded exercises covering sets, logic,
relations, functions, reproducible computation and applied decision systems, with
complete worked solutions and Python reference implementations:

- `docs/PU-B01-C02_Exercises_and_Solutions_v1.0.pdf`
- `docs/PU-B01-C02_Exercises_and_Solutions_v1.0.docx`

## Executive brief

The professional Executive Brief translates the lesson's mathematical foundations
into practical controls for classification, eligibility rules, data relationships
and accountable decision systems:

- `docs/PU-B01-C02_Executive_Brief_v1.0.pdf`
- `docs/PU-B01-C02_Executive_Brief_v1.0.docx`

## Google Colab

Open `notebooks/M1_N02_sets_logic_relations_functions.ipynb` in Colab, run the bootstrap cell, and upload the complete repository ZIP when prompted. Then select **Runtime → Restart session and run all**.

## Local validation

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
python scripts/validate_notebook.py
```

## Release status

Version `1.0.1` retains the approved Lesson 2 chapter, notebook and platform materials from v1.0.0 and adds the controlled standalone exercises-and-solutions package.

Version `1.0.2` adds the controlled Executive Brief in PDF and DOCX formats. The approved chapter, notebook, code, exercises and lesson content are unchanged from v1.0.1.
