# PU-B01-C07 video narration — controlled draft v0.1

Target duration: 16–17 minutes  
Presentation: `PU-B01-C07_Lesson_Presentation_v0.1.pptx`

## Slide 1 — What can you remove without losing the decision?

Dimensionality reduction is often described as a technical convenience. In practice, it is a decision about information removal. This lesson asks a stricter question: what can we compress while preserving the evidence required for the intended decision?

## Slide 2 — Learning route

We will answer four questions. Which directions dominate the matrix? How well does a rank-k approximation preserve the original? What does PCA retain after centering? And which losses are acceptable for the intended use?

## Slide 3 — SVD anatomy

For a real matrix A, the singular value decomposition is A equals U Sigma V transpose. V transpose identifies input directions. Sigma records the strength of each direction. U identifies the corresponding output directions. The factors become meaningful only when we retain the definition of the data and the purpose of the analysis.

## Slide 4 — Verification

A decomposition should be tested, not merely printed. Reconstruct A from U, Sigma and V transpose within a stated numerical tolerance. Verify that the columns of U and V are orthonormal. Confirm that singular values are nonnegative and ordered from largest to smallest. These assertions turn an output into reproducible evidence.

## Slide 5 — Low-rank approximation

Keeping the first k singular directions gives A sub k. This is the best rank-k approximation in Frobenius norm. But mathematical optimality under one norm is not the same as fitness for every decision. Report reconstruction error and validate the reduced representation against its downstream use.

## Slide 6 — PCA from SVD

PCA begins with centered data. Decompose the centered matrix using SVD. The rows of V transpose are principal directions, while U Sigma gives the scores. Standardization may be appropriate when scales differ materially, but it changes the geometry and must be justified.

## Slide 7 — Explained variance

The explained-variance share for a direction is its squared singular value divided by the sum of all squared singular values. This measures retained centered variation. It does not establish importance, causality, fairness or predictive accuracy. Inspect residuals, rare events and subgroup reconstruction loss.

## Slide 8 — National-indicator case

Imagine five correlated indicators covering agriculture, food availability, electricity, health and transport. Two components may summarize a shared regional pattern. That compression may be useful, but it does not authorize us to name the first component development, infer a causal mechanism or convert its loadings into budget shares.

## Slide 9 — Failure modes

Four failures deserve attention. Fitting preprocessing on the entire dataset creates leakage. Choosing k only because a percentage looks convenient avoids downstream validation. Naming components causally overstates mathematical association. And discarding the route to original variables makes consequential losses difficult to audit.

## Slide 10 — Responsible workflow

A defensible workflow defines the use, prepares the data reproducibly, computes SVD or PCA, validates loss and documents the decision. The record should state what is preserved, what is removed, who can reverse the choice and which evidence triggers revision or stopping.

## Slide 11 — Reasoning clinic

Before accepting a reduced representation, ask why centering was required, what the reconstruction error omits, which groups have the largest residuals and what evidence would require a revise or stop decision. A retained percentage alone cannot answer these questions.

## Slide 12 — Closing

SVD reveals dominant directions. PCA summarizes variation in centered data. Responsible dimensionality reduction quantifies what is retained and lost before the result supports a decision. Compress the matrix, preserve the evidence, and keep accountable human authority over the final use.

