---
title: Lesson 4: Valid Quantum States
entity_type: exercise_completion_note
source_files:
  - raw/GoodNotes/Solution_Pics/IMG_6891.HEIC
  - raw/GoodNotes/Solution_Pics/IMG_6892.HEIC
  - raw/GoodNotes/Solution_Pics/IMG_6893.HEIC
  - raw/GoodNotes_JPEG/llm-readings/IMG_6891.md
  - raw/GoodNotes_JPEG/llm-readings/IMG_6892.md
  - raw/GoodNotes_JPEG/llm-readings/IMG_6893.md
  - "resources/exercises/md/004 - #4⧸100： What is a qubit？  ｜｜ Quantum Computer Programming in 100 Easy Lessons.md"
source_quality_notes:
  - The photos cover the validity checks for part b, including real, complex, multi-basis, and trigonometric examples.
  - Some complex-amplitude work appears ambiguous and may include arithmetic or method errors.
---

# Lesson 4: Valid Quantum States

## Completed Work
- Checked candidate states by summing squared amplitude magnitudes and comparing the total to `1`.
- Confirmed examples using `sqrt(1/2)` and `0.8i, 0.6` as valid based on normalization.
- Marked `0.4, 0.9`, the four-amplitude real vector, and `0.1, 0.2, 0.3, 0.4` as invalid because their probability totals do not equal `1`.
- Used `cos^2(theta) + sin^2(theta) = 1` to identify the trigonometric state as valid.

## Approach Taken
- Translated amplitudes into probabilities by squaring magnitudes.
- Used the normalization rule as the deciding test for whether a written state is physically valid.
- For complex numbers, attempted to account for imaginary components when checking total probability.

## Concepts Practiced
- Superposition state notation
- Amplitudes versus probabilities
- Normalization of quantum states
- Complex magnitudes
- Multi-basis state vectors
- Trigonometric parameterization of normalized states

## Caveats
- The multimodal reading notes possible mistakes in the complex cases: complex amplitudes should be checked with magnitude squared, not ordinary complex squaring.
- The reading specifically flags item vi as likely misclassified if magnitude squared is used, since `|0.7 + 0.1i|^2 + |-0.1 + 0.7i|^2 = 1`.
