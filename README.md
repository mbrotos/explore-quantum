# Explore Quantum

Explore Quantum is a small learning repo for building intuition about classical bits, probability, and quantum amplitudes through simple circuit simulators.

The code is intentionally direct: each simulator is a Python file you can run, inspect, and modify while working through the exercises.

## Learning Sources

This repo draws from Ryan O'Donnell's CMU quantum computing course materials:

- YouTube playlist: https://www.youtube.com/watch?v=XtDJXHYQ41U&list=PLm3J0oaFux3bF48kurxGR6jrmPaQf6lkN
- Ryan O'Donnell: https://www.cs.cmu.edu/~odonnell/

For a more formal refresher, IBM Quantum Learning's [Basics of quantum information](https://qiskit.qotlabs.org/learning/courses/basics-of-quantum-information) is a useful reference. It is less software-engineering-oriented as a first introduction to the quantum circuit model, but helpful once the simulator examples have built some intuition.

## Start Here

Use Python 3.10 or newer.

```bash
uv sync
source .venv/bin/activate
pytest
```

The rest of the commands assume the virtual environment is active.

The examples below use small programs from [`resources/instructs/`](resources/instructs/); open those files to see the exact gates being applied.

Try the quantum-amplitude simulator:

```bash
python src/ex20.py --num-qubits 2 --instructions resources/instructs/test_had_1.txt
```

This example applies a `NOT` and then a Hadamard gate. The simulator prints the nonzero basis-state amplitudes; pedagogically, read that output as the state

$$
|\psi\rangle = \frac{1}{\sqrt{2}}|00\rangle - \frac{1}{\sqrt{2}}|10\rangle.
$$

For exact classical probabilities, try:

```bash
python src/ex7_1_exact.py --num-bits 4 --instructions resources/instructs/i1.txt
```

It starts in the all-zero bitstring, applies the instructions, and prints the probability of ending back at `|0...0>`.

## What Is In This Repo?

- `src/ex5_1.py`: deterministic bit simulator for `NOT`, `CNOT`, `CCNOT`, and random bit instructions.
- `src/ex7_1_exact.py`: exact probabilistic simulator that tracks the full distribution over bitstrings.
- `src/ex20.py`: quantum-amplitude simulator using `HAD` instead of `RNG`; measurement sampling is still a TODO.
- `src/ex7_1.py`: older approximate probabilistic simulator that tracks each bit independently; prefer `src/ex7_1_exact.py` for probability behavior.
- `resources/instructs/`: small instruction files for trying the simulators.
- `resources/lectures/` and `resources/exercises/`: course transcripts, summaries, exercise images, and markdown.
- `wiki/`: source-backed notes for completed exercises and IBM Quantum Learning material.
- `tests/`: pytest coverage for the deterministic and exact probabilistic simulators.

## Instruction Files

Instruction files are plain text. Indices are 1-based in files, even though the Python code converts them to 0-based indices internally.

Example:

```text
NOT 1
CNOT 1 2
CCNOT 1 2 3
RNG 4
```

Classical/probabilistic instructions:

- `NOT i`: flip bit `i`.
- `CNOT i j`: flip bit `j` if bit `i` is `1`.
- `CCNOT i j k`: flip bit `k` if bits `i` and `j` are both `1`.
- `RNG i`: randomize bit `i` to `0` or `1` with probability `1/2` each.

Quantum-amplitude instruction:

- `HAD i`: apply a Hadamard gate to qubit `i`.

## Run The Simulators

Deterministic simulator:

```bash
python src/ex5_1.py --num-bits 4 --instructions resources/instructs/i1.txt
```

Exact probability simulator:

```bash
python src/ex7_1_exact.py --num-bits 4 --instructions resources/instructs/i1.txt
```

Quantum-amplitude simulator:

```bash
python src/ex20.py --num-qubits 2 --instructions resources/instructs/test_had_1.txt
```

Approximate probability simulator, mostly useful for comparison with the exact simulator:

```bash
python src/ex7_1.py --num-bits 4 --instructions resources/instructs/i1.txt
```

The approximate and exact probability simulators can disagree on programs where operations create correlations between bits. Use `src/ex7_1_exact.py` when you want the reference behavior.

## Tests And Formatting

Run everything:

```bash
pytest
```

Run one test file:

```bash
pytest tests/test_ex7_1_exact.py
```

Run one test:

```bash
pytest tests/test_ex7_1_exact.py::test_full_pipeline_matches_test3_distribution
```

Format code:

```bash
black src tests
```

Check formatting without changing files:

```bash
black --check src tests
```

## Notes For Future Work

- `src/ex20.py` still needs `extract_all` measurement sampling.
- `scripts/run_all_tests.sh` is a simulator smoke-test script over `resources/instructs/test[0-9]*.txt`, not the pytest suite.
- Integer-encoded bitstrings use the least-significant bit as internal index `0`, so read binary output with that convention in mind.
