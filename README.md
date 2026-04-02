# Explore Quantum

A small project for learning quantum-computing ideas through simple bit-circuit simulators.

## Course References

Lecture and exercise content in this repo is based on Ryan O'Donnell's CMU quantum computing course materials:

- YouTube playlist: https://www.youtube.com/watch?v=XtDJXHYQ41U&list=PLm3J0oaFux3bF48kurxGR6jrmPaQf6lkN
- Ryan O'Donnell (CMU): https://www.cs.cmu.edu/~odonnell/

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Run Tests

```bash
pytest
```

## Run The Simulators

Approximate simulator:

```bash
python src/ex7_1.py 4 resources/instructs/i1.txt
```

Exact simulator:

```bash
python src/ex7_1_exact.py 4 resources/instructs/i1.txt
```

## Example Instruction File

```text
NOT 1
CNOT 1 2
CCNOT 1 2 3
RNG 4
```

Indices in instruction files are 1-based.

## Valid Instructions

- `NOT i`: flip bit `i`
- `CNOT i j`: flip bit `j` if bit `i` is `1`
- `CCNOT i j k`: flip bit `k` if bits `i` and `j` are both `1`
- `RNG i`: set bit `i` randomly to `0` or `1` with probability `1/2` each

## Project Layout

- `src/`: simulator code
- `resources/lectures/`: lecture-related materials
- `resources/exercises/`: exercise-related materials
- `resources/instructs/`: example instruction files
- `tests/`: test suite
