---
title: Lesson 14: The Unitary Property
entity_type: exercise_completion_note
source_files:
  - raw/GoodNotes/Solution_Pics/IMG_7044.HEIC
  - raw/GoodNotes_JPEG/llm-readings/IMG_7044.md
  - "resources/exercises/md/014 - #14⧸100： The Unitary property ｜｜ Quantum Computer Programming in 100 Easy Lessons.md"
source_quality_notes:
  - The photo directly matches the diagonal 4 by 4 operation from the exercise.
---

# Lesson 14: The Unitary Property

## Completed Work
- Started from a general two-qubit state with amplitudes on `|00>`, `|01>`, `|10>`, and `|11>`.
- Applied the diagonal matrix with entries `1, -1, -1, -1`.
- Showed the output amplitudes become `[a, -b, -c, -d]`.
- Checked that squaring the output amplitudes preserves the original normalization total.

## Approach Taken
- Verified unitarity by norm preservation rather than by multiplying the matrix by its adjoint.
- Used the fact that sign flips do not change squared magnitudes.

## Concepts Practiced
- Two-qubit state vectors
- Diagonal phase-flip style operations
- Matrix-vector multiplication
- Norm preservation
- The unitary property as probability conservation

## Caveats
- The fourth coefficient symbol is ambiguous in the handwriting.
- The visible proof assumes real amplitudes, matching the course's simplified setting here.
