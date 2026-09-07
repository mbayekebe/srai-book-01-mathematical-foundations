# PU-B01-C05 — Vector Spaces, Bases, Rank and Projections

Published controlled release v1.0.0.

The owner approved the chapter, notebook, exercises, Executive Brief, slide deck and video, and explicitly authorized public release without a separate independent review. This remains an owner-approved exception and must not be described as independent signoff.

The computational runtime is `srai_math 1.1.1rc1`, a checksum-pinned prerelease. Its use does not promote or rename it as a stable runtime.

## Released resources

- [GitHub release v1.0.0](https://github.com/mbayekebe/srai-book-01-mathematical-foundations/releases/tag/pu-b01-c05-v1.0.0)
- [Controlled chapter PDF](docs/PU-B01-C05_Chapter5_Vector_Spaces_Bases_Rank_and_Projections_Controlled_Edition_v1.0.pdf)
- [Canonical notebook](notebooks/M1/M1_N05_vector_spaces_bases_rank_projections_v0.2.2.ipynb)
- [Exercises and solutions PDF](docs/PU-B01-C05_Educational_Exercises_and_Solutions_v1.0.pdf)
- [Executive Brief PDF](docs/PU-B01-C05_Executive_Brief_v1.0.pdf)
- [Video lesson deck](video/PU-B01-C05_Video_Lesson_Deck_v1.0.pptx)
- [Narration](video/PU-B01-C05_Narration_v1.0.txt)
- [Public video lesson](https://www.youtube.com/watch?v=tZtdYcMEaIQ)

## Notebook execution

The notebook downloads the exact public `srai_math` wheel, verifies its SHA-256 and installs it into a temporary target for that kernel. Internet access and a working runtime are required. A previously imported different `srai_math` version requires a kernel restart.

## Verification

From the production-unit directory:

```powershell
py verify_package.py
```

With NumPy available:

```powershell
py verify_package.py --mathematics
```

Review `ASSET_INDEX.json`, `SHA256SUMS.txt`, `VALIDATION_REPORT.json` and the records under `evidence/` for exact integrity, execution and authorization evidence.

## Control status

Lesson 5 is published on the SRAI website and preserved through the qualified GitHub release above. The owner-authorized exception and prerelease-runtime disclosure remain applicable.
