---
title: Lesson 8: Left Cyclic Shift Path Diagrams
entity_type: exercise_completion_note
source_files:
  - raw/GoodNotes/Solution_Pics/IMG_7028.HEIC
  - raw/GoodNotes/Solution_Pics/IMG_7029.HEIC
  - raw/GoodNotes_JPEG/llm-readings/IMG_7028.md
  - raw/GoodNotes_JPEG/llm-readings/IMG_7029.md
  - "resources/exercises/md/008 - #8⧸100： Path diagrams⧸matrices for instructions ｜｜ Quantum Computer Programming in 100 Easy Lessons.md"
source_quality_notes:
  - The evidence shows path-diagram and matrix work for a three-bit cyclic shift, though some labels are cropped.
---

# Lesson 8: Left Cyclic Shift Path Diagrams

## Completed Work
- Drew computational basis states for a three-qubit register and began the path diagram for `LeftCyclicShift(A,B,C)`.
- Wrote an 8 by 8 permutation matrix for the basis-state mapping.
- Identified the undo operation as `RightCyclicShift(A,B,C)`.
- Noted a SWAP decomposition for the cyclic shift and its reverse.

## Approach Taken
- Treated the classical reversible instruction as a permutation of computational basis states.
- Filled the matrix as a permutation matrix, with one `1` per row/column for each basis-state remapping.
- Used SWAP operations as simpler reversible building blocks for cyclic permutation.

## Concepts Practiced
- Path diagrams
- Computational basis ordering
- Reversible classical instructions as quantum-safe operations
- Permutation matrices
- Inverse operations
- SWAP-based decomposition

## Caveats
- Some path labels and the lower mapping table are partially cut off.
- The exact qubit ordering convention is inferred from the visible `A B C` labels.
