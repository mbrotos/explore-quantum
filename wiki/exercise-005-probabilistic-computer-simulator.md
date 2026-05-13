---
title: Lesson 5: Probabilistic Computer Simulator
entity_type: exercise_completion_note
source_files:
  - src/ex5_1.py
  - tests/test_ex5_1.py
  - resources/instructs/i1.txt
  - "resources/exercises/md/005 - #5⧸100： The physics of qubits ｜｜ Quantum Computer Programming in 100 Easy Lessons.md"
source_quality_notes:
  - This is code-backed evidence, so the implementation files and tests are stronger evidence than handwritten notes for this exercise.
  - The exercise prompt text in the markdown is visibly truncated near the end, but the implemented instruction set matches the visible prompt.
---

# Lesson 5: Probabilistic Computer Simulator

## Completed Work
- Implemented a command-line probabilistic bit-circuit simulator in `src/ex5_1.py`.
- Supports the visible exercise instruction set: `NOT`, `CNOT`, `CCNOT`, and `RNG`.
- Accepts a bit count and instruction-file path from the command line.
- Initializes all bits to `0`, parses 1-based instruction indices, converts them to 0-based Python indices, executes the instructions once, and prints final bit values.
- Includes example instruction input in `resources/instructs/i1.txt`.

## Approach Taken
- Represents the machine state as a Python list of classical bits.
- Implements `NOT` as toggling `bits[i]` between `0` and `1`.
- Implements `CNOT` and `CCNOT` as conditional toggles on the target bit.
- Implements `RNG` with `random.randint(0, 1)`, matching the exercise's requirement to use pseudorandomness for one simulated run.
- Keeps parsing simple by assuming instruction names and integer operands, with explicit rejection of unknown operations.

## Code Entrypoints
- Run the simulator with:

```bash
python src/ex5_1.py 4 resources/instructs/i1.txt
```

- Focused tests:

```bash
pytest tests/test_ex5_1.py
```

## Concepts Practiced
- Classical probabilistic simulation as a stepping stone toward quantum simulation
- Bit registers initialized to `0`
- Reversible classical gates: `NOT`, `CNOT`, `CCNOT`
- Pseudorandom sampling via `RNG`
- Parsing external instruction files
- 1-based course notation versus 0-based Python indexing

## Caveats
- The simulator performs one sampled run, not an exact probability calculation.
- It assumes instruction operands are otherwise well-formed, matching the exercise's simplifying assumption.
- The parser rejects blank lines as empty instruction lines, which is stricter than many file formats.
