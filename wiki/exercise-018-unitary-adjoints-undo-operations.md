---
title: Lesson 18: Unitary Adjoints Undo Operations
entity_type: exercise_completion_note
source_files:
  - raw/GoodNotes/Solution_Pics/IMG_7055.HEIC
  - raw/GoodNotes_JPEG/llm-readings/IMG_7055.md
  - "resources/exercises/md/018 - #18⧸100： How Toggles Detective works (Part 1⧸2) ｜｜ Quantum Computer Programming in 100 Easy Lessons.md"
source_quality_notes:
  - The image is labeled Ex 18 and shows the identity matrix plus the start of the arbitrary-state proof.
---

# Lesson 18: Unitary Adjoints Undo Operations

## Completed Work
- Drew the identity operation on two qubits, mapping each basis state to itself.
- Wrote the 4 by 4 identity matrix.
- Began the proof that if `U dagger U = I`, then applying `U` and then `U dagger` returns an arbitrary state to itself.
- Used a general state vector with amplitudes `a, b, c, d`.

## Approach Taken
- First verified behavior on computational basis states.
- Then extended the identity behavior to an arbitrary superposition using linearity.
- Used the path-diagram interpretation of composing `U` with `U dagger` and compressing to identity.

## Concepts Practiced
- Identity operator
- Unitary matrices
- Adjoint / conjugate transpose
- Reversibility of quantum operations
- Arbitrary state vectors
- Linearity over amplitudes

## Caveats
- The lower proof is partly hard to read, but the intended conclusion `U dagger U = I` is clear.
- The exact illustrative picture requirement from the prompt may continue outside the visible image.
