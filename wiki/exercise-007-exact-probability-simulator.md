---
title: Lesson 7: Exact Probability Simulator
entity_type: exercise_completion_note
source_files:
  - src/ex7_1.py
  - src/ex7_1_exact.py
  - tests/test_ex7_1_exact.py
  - scripts/run_all_tests.sh
  - resources/instructs/test1.txt
  - resources/instructs/test2.txt
  - resources/instructs/test3.txt
  - resources/instructs/test4.txt
  - "resources/exercises/md/007 - #7⧸100： Classical reversible instructions ｜｜ Quantum Computer Programming in 100 Easy Lessons.md"
source_quality_notes:
  - `src/ex7_1_exact.py` is the source-backed exact implementation for the exercise.
  - `src/ex7_1.py` is explicitly documented as a first-order independent-bit approximation and should not be treated as a complete exact solution.
---

# Lesson 7: Exact Probability Simulator

## Completed Work
- Implemented an exact probability simulator in `src/ex7_1_exact.py` for the same instruction language used in Lesson 5.
- Tracks the full probability distribution over bitstrings instead of sampling one run.
- Computes and prints the exact probability of ending in the all-zero state `|00...0>`.
- Uses exact rational arithmetic through `fractions.Fraction`.
- Includes tests for `NOT`, `CNOT`, `CCNOT`, `RNG`, instruction parsing, invalid repeated indices, and a full pipeline example.

## Approach Taken
- Represents a bitstring as an integer key in a probability dictionary: `dict[int, Fraction]`.
- Starts from `{0: Fraction(1, 1)}`, meaning all probability mass is on the all-zero bitstring.
- Applies deterministic reversible gates by moving probability mass to toggled integer states.
- Applies `RNG` by splitting probability mass equally between the original and partner state for the randomized bit.
- Reads the exact all-zero probability as `dist.get(0, Fraction(0, 1))` after all instructions execute.

## Approximate Attempt
- `src/ex7_1.py` tracks only per-bit marginal probabilities and multiplies them at the end.
- Its module docstring says it assumes bits remain independent and does not model correlations.
- This is useful as a learning contrast, but it is not the exact Lesson 7 solution when instructions create correlations between bits.

## Code Entrypoints
- Run the exact simulator with:

```bash
python src/ex7_1_exact.py --num-bits 4 --instructions resources/instructs/test3.txt
```

- Run the approximate simulator with:

```bash
python src/ex7_1.py --num-bits 4 --instructions resources/instructs/test3.txt
```

- Focused tests:

```bash
pytest tests/test_ex7_1_exact.py
```

## Concepts Practiced
- Exact probability distributions over classical states
- Rational arithmetic for exact results
- Probability mass transfer under reversible gates
- Randomness as distribution branching rather than sampling
- Correlations between bits after controlled operations
- Why marginal-only simulation can fail for exact joint behavior

## Caveats
- The exact implementation stores the full joint distribution, so it is intentionally not scalable to very large `n`; this matches the exercise's warning that exact handling only needs to work for small `n`.
- `scripts/run_all_tests.sh` currently runs `src/ex7_1.py`, the approximate simulator, across instruction files; use `pytest tests/test_ex7_1_exact.py` or call `src/ex7_1_exact.py` directly to verify the exact implementation.
