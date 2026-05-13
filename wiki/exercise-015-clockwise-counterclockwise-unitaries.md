---
title: Lesson 15: Clockwise and Counterclockwise Unitaries
entity_type: exercise_completion_note
source_files:
  - raw/GoodNotes/Solution_Pics/IMG_7045.HEIC
  - raw/GoodNotes/Solution_Pics/IMG_7046.HEIC
  - raw/GoodNotes/Solution_Pics/IMG_7047.HEIC
  - raw/GoodNotes_JPEG/llm-readings/IMG_7045.md
  - raw/GoodNotes_JPEG/llm-readings/IMG_7046.md
  - raw/GoodNotes_JPEG/llm-readings/IMG_7047.md
  - "resources/exercises/md/015 - #15⧸100： Hadamard is unitary... ｜｜ Quantum Computer Programming in 100 Easy Lessons.md"
source_quality_notes:
  - The images show norm-preservation proofs for clockwise and counterclockwise matrices, plus their inverse relationship.
---

# Lesson 15: Clockwise and Counterclockwise Unitaries

## Completed Work
- Verified the clockwise matrix `[[0.8, 0.6], [-0.6, 0.8]]` preserves the norm of a real one-qubit state.
- Verified the counterclockwise matrix `[[0.8, -0.6], [0.6, 0.8]]` preserves the norm of a real one-qubit state.
- Multiplied the counterclockwise and clockwise matrices and showed their product is the identity.

## Approach Taken
- Applied each matrix to an arbitrary state `(a, b)^T`.
- Expanded the squared norm of the output.
- Used cancellation of cross terms, such as `0.48ab - 0.48ab`, to recover `a^2 + b^2 = 1`.
- Confirmed the two operations undo each other by direct matrix multiplication.

## Concepts Practiced
- Single-qubit real rotations
- Unitary transformations
- Probability conservation
- Inverse operations
- Matrix multiplication as sequential gate composition

## Caveats
- The work assumes real amplitudes; a full complex proof would use conjugates.
- Some subscripts are handwritten and slightly ambiguous, but the clockwise/counterclockwise matrices are readable.
