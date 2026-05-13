---
title: Lesson 1: Reversible Toggle Subroutines
entity_type: exercise_completion_note
source_files:
  - raw/GoodNotes/Solution_Pics/IMG_6871.HEIC
  - raw/GoodNotes/Solution_Pics/IMG_6872.HEIC
  - raw/GoodNotes/Solution_Pics/IMG_6873.HEIC
  - raw/GoodNotes/Solution_Pics/IMG_6874.HEIC
  - raw/GoodNotes_JPEG/llm-readings/IMG_6871.md
  - raw/GoodNotes_JPEG/llm-readings/IMG_6872.md
  - raw/GoodNotes_JPEG/llm-readings/IMG_6873.md
  - raw/GoodNotes_JPEG/llm-readings/IMG_6874.md
  - "resources/exercises/md/001 - #1⧸100： Toggling qubits ｜｜ Quantum Computer Programming in 100 Easy Lessons.md"
source_quality_notes:
  - Multimodal readings identify work for parts a through i, but some handwriting is cropped or ambiguous.
  - Part i is described conceptually rather than shown with a complete Python REPL transcript.
---

# Lesson 1: Reversible Toggle Subroutines

## Completed Work
- Part a implements `if (A OR B) then toggle C` using the allowed toggle instructions and Boolean decomposition.
- Part b implements a negative control, `if (NOT A) then toggle B`, by toggling `A`, applying the positive control, then toggling `A` back.
- Part c gives `IncrMod4 A,B` as carry-style reversible logic: toggle the high bit when the low bit carries, then toggle the low bit.
- Part d extends the same carry pattern to `IncrMod8 A,B,C`.
- Part e gives visible steps for `IncrMod3 A,B`, including preserving the invalid `11` case.
- Part f uses XOR-swap reasoning for `SWAP A,B`.
- Parts g and h use pairwise swaps to build left and right cyclic shifts on `A,B,C`.
- Part i notes that Python's XOR-swap version works by the same reversible algebra, with integers treated through their bit representations.

## Approach Taken
- Reduced new instructions to the three allowed reversible primitives: unconditional toggle, single-control toggle, and two-control toggle.
- Used conjugation with toggles to simulate a negative control while restoring the control qubit.
- Treated modular increment as binary carry propagation.
- Treated `SWAP` and cyclic shifts as reversible permutations rather than destructive assignments.

## Concepts Practiced
- Boolean logic as reversible computation
- Controlled toggles and negative controls
- Modular increment and carry logic
- XOR identities
- SWAP and cyclic permutations
- Preserving input qubits after helper toggles

## Caveats
- The model reading flags parts of the handwriting as ambiguous, especially the first page and the lower continuation of part i.
- The source evidence supports completion of the handwritten exercise, but not a separate executable Python transcript for part i.
