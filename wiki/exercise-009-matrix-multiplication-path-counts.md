---
title: Lesson 9: Matrix Multiplication From Path Counts
entity_type: exercise_completion_note
source_files:
  - raw/GoodNotes/Solution_Pics/IMG_7030.HEIC
  - raw/GoodNotes_JPEG/llm-readings/IMG_7030.md
  - "resources/exercises/md/009 - #9⧸100： Superposition-creating instructions ｜｜ Quantum Computer Programming in 100 Easy Lessons.md"
source_quality_notes:
  - The image is readable enough to identify matrices A, B, and C, with minor cropping near labels.
---

# Lesson 9: Matrix Multiplication From Path Counts

## Completed Work
- Wrote the blue graph matrix `B` as a `2 x 3` matrix.
- Used the given amber graph matrix `A` as a `3 x 4` matrix.
- Computed `C = BA` as a `2 x 4` matrix:

```text
C = [7 5 7 1
     0 2 4 0]
```

## Approach Taken
- Matched dimensions before multiplying: `B` is `p x n`, `A` is `n x m`, so `C` is `p x m`.
- Computed each entry of `C` with row-column dot products.
- Interpreted matrix multiplication as counting all two-step paths through the glued middle layer.

## Concepts Practiced
- Directed path counting
- Matrix dimensions
- Matrix multiplication
- Composition of path diagrams
- Why composed quantum/classical operations multiply as matrices

## Caveats
- The top-right label is partly cropped, but the matrix entries and final product are clear.
