# PU-B01-C03 Chapter and Notebook Audit Report

## Control status

- Production unit: **PU-B01-C03 — Vector Foundations**
- Chapter: **Book 1, Chapter 3**
- Notebook: **M1_N03_vector_foundations.ipynb**
- Audit date: **29 August 2026**
- Current disposition: **Audit candidate passed technical and computational checks**
- Publication authority: **Final publication remains subject to owner review and approval**

## Provenance

The chapter extract was derived from the verified `SRAI_Book1_Ch1_5_Word_Native_Release_v1.1` package. The package release record identifies Stage 17, Word-native master v1.1, dated 28 July 2026. Its two controlled release files were independently verified against the supplied checksum manifest:

- Word master SHA-256: `7aa5d68760130cd62669b9085d549adfe54df674bf7c13c76092a0c74859410e`
- PDF edition SHA-256: `783dc456b1f162075a1df91064329deb20d00b2ff569b591ab16bf8f3cd7ec5b`

The durable Word bookmark `chapter-3---vector-foundations` was used to extract Chapter 3. The extracted source begins with Chapter 3 and ends with the Chapter 3 instructor solutions; no Chapter 2 or Chapter 4 content was found.

## Source inputs

| Input | SHA-256 |
|---|---|
| `PU-B01-C03_Chapter3_Vector_Foundations_Source_Extract_v0.1.docx` | `315190bd70cd9b2f53a8e636bb0e0bdfd2acb37f541579aa9510d9a72cfbb628` |
| `M1_N03_vector_foundations.ipynb` | `c759b183fa205caf1c0c1d7457972c9c5c0136cd7a85975d6feb0038fdc678ea` |
| `M1_N03_srai_math_source.zip` | `ae0cbd7a50c0cf4be65640d7fe8f22426296bd211184c104b62ca7c71befbaed` |

## Chapter findings and corrections

The source extract was structurally complete but required controlled correction and strengthening.

1. Corrected the duplicated visible chapter number in the title.
2. Restored the missing infinity symbol in the discussion and exercise on the $L^1$, $L^2$ and $L^\infty$ norms.
3. Restored missing vector symbols and the nonzero-direction condition in the projection section.
4. Stated explicitly that cosine similarity is undefined when either vector is zero.
5. Expanded Gram–Schmidt from a brief reference into a defined procedure with native Word equations and a worked exact example.
6. Replaced the placeholder worked-example language with a complete projection, rejection, orthogonality and perturbation calculation.
7. Replaced generic repeated material with chapter-specific computational checkpoints, domain conditions, numerical safeguards and verification questions.
8. Added a notebook verification checklist covering clean execution, zero-vector failures, residual invariants and preprocessing sensitivity.
9. Updated the technical audit note to distinguish completed technical checking from outstanding owner approval.

The final controlled chapter renders as eight pages. Every rendered page was visually inspected. No clipping, overlap, missing glyphs or cross-chapter contamination was found in the final render. The accessibility audit returned **0 high, 0 medium and 0 low findings**. The document contains **1 Heading 1, 28 Heading 2 and 3 Heading 3 paragraphs**, with native Office Math retained and extended.

## Notebook findings and corrections

The uploaded notebook contained coherent content and syntactically valid code, but all code cells initially had null execution counts and no retained outputs. The controlled audit candidate now:

1. records its status as an executed audit candidate awaiting owner approval;
2. tests `ValueError` handling for zero-vector normalization, cosine similarity and projection;
3. verifies the projection rejection directly through $u^\top r=0$;
4. labels the vector, projection and rejection in the retained plot;
5. compares raw, standardized and deliberately reweighted state-vector distances; and
6. uses portable `$...$` inline and `$$ ... $$` display-math delimiters for correct rendering in VS Code and Jupyter environments; and
7. retains sequential execution counts and outputs as reproducibility evidence.

All **22 code cells** were executed from a clean namespace against the supplied `srai_math` source. A second independent clean execution also passed. There were **0 execution errors**, and one plot output was retained.

Selected verified results:

| Check | Result |
|---|---:|
| $L^1$ norm of $(3,-4)$ | 7 |
| $L^2$ norm of $(3,-4)$ | 5 |
| $L^\infty$ norm of $(3,-4)$ | 4 |
| Euclidean distance from $(1,2)$ to $(4,6)$ | 5 |
| Angle between standard basis vectors | $\pi/2$ |
| Projection of $(3,4)$ onto $(1,0)$ | $(3,0)$ |
| Rejection | $(0,4)$ |
| Gram–Schmidt invariant | $Q^\top Q\approx I$ |

The synthetic policy example also confirms that preprocessing changes numerical geometry: the A–B distance is `4.733920` in raw coordinates, `0.780467` after standardization and `1.127137` after the illustrative inflation reweighting.

## Primary technical references

- [NumPy linear algebra norms](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html)
- [NumPy dot product](https://numpy.org/doc/stable/reference/generated/numpy.dot.html)
- [scikit-learn StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)

## Controlled outputs

| Output | SHA-256 |
|---|---|
| `PU-B01-C03_Chapter3_Vector_Foundations_Audited_Controlled_Edition_v1.0.docx` | `641242bf217ab431f05cfb26e589c7ebd5591cae8e0349f179541c5a3a43c6d3` |
| `M1_N03_vector_foundations.ipynb` | `2727aac9f07a6a5874dbc42ed9f154b0d05ca218044bc02834651f7f410297d6` |

## Release gate

Technical audit and clean notebook execution have passed. The next gate is the owner’s substantive and visual review of the two controlled outputs. Only after approval should the files be copied into the PU-B01-C03 repository, the production-unit metadata be advanced, and the remaining release assets be developed.
