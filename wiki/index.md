---
title: Exercise Wiki Index
entity_type: index
source_files:
  - raw/GoodNotes
  - raw/GoodNotes_JPEG/llm-readings/
source_quality_notes:
  - raw/GoodNotes is a symlink to the GoodNotes Undergraduate Quantum Computation folder.
  - raw/GoodNotes_JPEG contains JPEG transport copies used for multimodal model reading, not local OCR.
---

# Exercise Wiki Index

## Completed Exercise Notes
- [Lesson 1: Reversible Toggle Subroutines](exercise-001-reversible-toggle-subroutines.md)
- [Lesson 4: Valid Quantum States](exercise-004-valid-quantum-states.md)
- [Lesson 5: Probabilistic Computer Simulator](exercise-005-probabilistic-computer-simulator.md)
- [Lesson 7: Exact Probability Simulator](exercise-007-exact-probability-simulator.md)
- [Lesson 8: Left Cyclic Shift Path Diagrams](exercise-008-left-cyclic-shift-path-diagrams.md)
- [Lesson 9: Matrix Multiplication From Path Counts](exercise-009-matrix-multiplication-path-counts.md)
- [Lesson 13: Composite Quantum Instructions](exercise-013-composite-quantum-instructions.md)
- [Lesson 14: The Unitary Property](exercise-014-unitary-property.md)
- [Lesson 15: Clockwise and Counterclockwise Unitaries](exercise-015-clockwise-counterclockwise-unitaries.md)
- [Lesson 16: Composite Operations As Matrix Products](exercise-016-composite-operations-matrix-products.md)
- [Lesson 17: Path Diagrams, Adjoints, and Inner Products](exercise-017-path-diagrams-adjoints-inner-products.md)
- [Lesson 18: Unitary Adjoints Undo Operations](exercise-018-unitary-adjoints-undo-operations.md)
- [Lesson 19: Toggles Detective Cube Diagrams](exercise-019-toggles-detective-cube-diagrams.md)

## Source Method
- GoodNotes originals remain in `raw/GoodNotes/` through the symlink.
- HEIC photos and the PDF page were converted to JPEG transport files in `raw/GoodNotes_JPEG/`.
- Each JPEG was sent one at a time to `opencode run -m openai/gpt-5.5` for multimodal reading.
- The model readings are stored in `raw/GoodNotes_JPEG/llm-readings/` and are treated as derived source notes with caveats.
