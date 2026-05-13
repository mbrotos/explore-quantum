---
title: Lesson 16: Composite Operations As Matrix Products
entity_type: exercise_completion_note
source_files:
  - raw/GoodNotes/Solution_Pics/IMG_7048.HEIC
  - raw/GoodNotes/Solution_Pics/IMG_7049.HEIC
  - raw/GoodNotes_JPEG/llm-readings/IMG_7048.md
  - raw/GoodNotes_JPEG/llm-readings/IMG_7049.md
  - "resources/exercises/md/016 - #16⧸100： Hadamard's unitary even w⧸ other qubits ｜｜ Quantum Computer Programming in 100 Easy Lessons.md"
source_quality_notes:
  - IMG_7049 directly matches the matrix-product proof by gluing M and N path diagrams.
  - IMG_7048 is labeled Ex 16 by the model but has ambiguous context and may be related practice.
---

# Lesson 16: Composite Operations As Matrix Products

## Completed Work
- Drew path diagrams for applying operation `M` and then operation `N` on two-qubit basis states.
- Introduced notation like `C[ab -> cd]` for the composite transition amplitude.
- Expanded a composite amplitude as a sum over all intermediate basis states.
- Wrote the key relation that the amplitude from `|ab>` to `|cd>` in the composite equals the sum of products `N[intermediate -> cd] M[ab -> intermediate]`.

## Approach Taken
- Used path diagrams rather than starting from the matrix multiplication rule directly.
- Fixed an input and output basis state, then summed over every possible middle state.
- Interpreted this sum-over-intermediate-states as exactly the entry formula for `N * M`.

## Concepts Practiced
- Composite quantum operations
- Transition amplitudes
- Sum over paths
- Matrix multiplication from path gluing
- Order of operations: first `M`, then `N`, gives `N * M`

## Caveats
- Some lower-page handwriting is cropped.
- IMG_7048 includes related amplitude-tree work but its exact prompt context is less certain than IMG_7049.
