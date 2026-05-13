---
title: Lesson 13: Composite Quantum Instructions
entity_type: exercise_completion_note
source_files:
  - raw/GoodNotes/Solution_Pics/IMG_7040.HEIC
  - raw/GoodNotes_JPEG/llm-readings/IMG_7040.md
  - "resources/exercises/md/013 - #13⧸100： Composite quantum instructions ｜｜ Quantum Computer Programming in 100 Easy Lessons.md"
source_quality_notes:
  - The image covers visible parts a through c; later parts may not be shown in this photo.
---

# Lesson 13: Composite Quantum Instructions

## Completed Work
- Built a controlled version of `MySub(B)` as a block matrix where the `A = 0` branch is identity and the `A = 1` branch applies the `2 x 2` matrix with entries `u, v, x, y`.
- Built `NoOpAndMySub(A,B)` as a block-diagonal operation applying the same `MySub` behavior regardless of `A`.
- Started an amplitude-tree calculation for applying `OtherSub(A)` and `MySub(B)` to fresh qubits.
- Wrote visible final expressions showing amplitudes combine by multiplying along paths and summing contributions.

## Approach Taken
- Represented subroutines as matrices over computational basis states.
- Used block structure to distinguish controlled behavior from unconditional behavior.
- Used path/amplitude trees rather than only symbolic matrix multiplication.

## Concepts Practiced
- Controlled quantum operations
- Block matrices
- Amplitude propagation
- Linearity of quantum operations
- Tensor-product-like independence of operations on different qubits

## Caveats
- The lower-right part of the page is cropped, so the evidence does not fully confirm parts d and e.
- The handwritten label for `MySub(B)` is slightly ambiguous but aligns with the exercise prompt.
