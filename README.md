# SRAI Book 1 — Mathematical Foundations

This repository contains the controlled computational and educational production units for **SRAI Book 1 — Mathematical Foundations**.

SRAI — Statistics, Reasoning and Artificial Intelligence — connects mathematical and statistical reasoning with reproducible computation, machine learning, responsible artificial intelligence and defensible decision-making.

## Published and controlled production units

| Production unit | Chapter | Title | Notebook | Status |
|---|---:|---|---|---|
| [PU-B01-C01](production-units/PU-B01-C01/) | 1 | Mathematical Thinking and Reproducible Computation | `M1_N01_mathematical_thinking.ipynb` | Published |
| [PU-B01-C02](production-units/PU-B01-C02/) | 2 | Sets, Logic, Relations and Functions | `M1_N02_sets_logic_relations_functions.ipynb` | Approved v1.0.0 |

Additional chapters will be added progressively as independently validated production units.

## Repository structure

```text
production-units/
├── PU-B01-C01/
└── PU-B01-C02/
```

Each production unit is self-contained and may include its own notebook, controlled documents, Python utilities, requirements, validation script, release evidence and platform assets.

## Validation

GitHub Actions validates every controlled notebook from its own production-unit directory. Local validation can be run independently:

```bash
cd production-units/PU-B01-C01
python -m pip install -r requirements.txt
python scripts/validate_notebook.py
```

```bash
cd production-units/PU-B01-C02
python -m pip install -r requirements.txt
python scripts/validate_notebook.py
```

Google Colab portability is validated separately using each production unit's controlled release ZIP.

## Versioning

Lesson-level tags use production-unit-qualified names:

```text
pu-b01-c01-v1.0.0
pu-b01-c02-v1.0.0
```

Book-level releases will use names such as `book-01-v1.0.0` when the corresponding controlled book release is complete.

## Public ecosystem

- Website: https://srai.mbayekebe.net/
- YouTube: https://www.youtube.com/@SRAIStatisticsReasoningandAI

## Rights and reuse

Copyright © 2026 Mbaye Kebe. All rights reserved. See [RIGHTS_AND_REUSE.md](RIGHTS_AND_REUSE.md).
