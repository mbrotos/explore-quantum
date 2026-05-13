---
title: Lesson 19: Toggles Detective Cube Diagrams
entity_type: exercise_completion_note
source_files:
  - raw/GoodNotes/Exercises.pdf
  - raw/GoodNotes_JPEG/pdf-pages/Exercises-1.jpg
  - raw/GoodNotes_JPEG/llm-readings/Exercises-1.md
  - "resources/exercises/md/019 - #19⧸100： How Toggles Detective works (Part 2⧸2) ｜｜ Quantum Computer Programming in 100 Easy Lessons.md"
source_quality_notes:
  - The PDF conversion produced one JPEG page, read separately by the multimodal model.
  - The page shows a procedure and cube diagram but not every intermediate amplitude value in full detail.
---

# Lesson 19: Toggles Detective Cube Diagrams

## Completed Work
- Drew a three-qubit computational-basis cube with states from `|000>` through `|111>`.
- Labeled axes/qubits as `X1`, `X2`, and `Ans`.
- Wrote the Toggles Detective procedure:
  1. create new qubits `X1`, `X2`, `Ans`
  2. toggle `Ans`
  3. apply Hadamard to all
  4. apply `MysteryToggles(X1, X2, Ans)`
  5. apply Hadamard to all
  6. extract all
- Added notes that associate Hadamard stages with adding/differencing along cube directions.

## Approach Taken
- Represented the three-qubit state space as a cube of computational basis states.
- Used Hadamards before and after the mystery operation to turn hidden toggle structure into measurable information.
- Interpreted toggles and controlled toggles as transformations along cube directions.
- Tracked the algorithm conceptually through basis-state geometry instead of only algebra.

## Concepts Practiced
- Toggles Detective
- Three-qubit basis-state cubes
- Hadamard transforms
- Hidden operation / oracle detection
- Amplitude differencing
- Measurement after interference

## Caveats
- The page appears to be a high-level worked diagram/procedure rather than a complete listing of all intermediate amplitude-labeled cube diagrams requested by the exercise.
- Some small labels near arrows are ambiguous in the model reading.
