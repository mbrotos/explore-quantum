# Explore Quantum Agent Guide

This is a learning repo for quantum-computing exercises, simulators, and source-backed notes. Favor helping the user understand over silently finishing work.

## Collaboration

- Treat exploratory requests as teaching moments: explain the concept, the check to run, and the result to look for.
- For bug reports, diagnose first with small REPL or `ipython` examples; patch only when the user asks for a fix or implementation.
- When making code changes, briefly connect the change to the bit, probability, amplitude, or programming concept involved.

## Python Commands

- Setup follows `README.md`: `uv sync`, then activate with `source .venv/bin/activate` and use normal commands.
- `pyproject.toml` requires Python `>=3.10`; runtime/dev dependencies are `black`, `pytest`, and `sympy`.
- Run all tests with `pytest` from the repo root; pytest gets imports from `pythonpath = ["."]`, so tests import modules as `from src import ex5_1`.
- Run focused tests with paths, for example `pytest tests/test_ex5_1.py` or `pytest tests/test_ex7_1_exact.py::test_full_pipeline_matches_test3_distribution`.
- Format Python with `black src tests`; check formatting with `black --check src tests`.
- There is no configured ruff, mypy, CI workflow, or pre-commit hook in this repo; do not invent those verification steps.

## Simulator Code

- There are no installed console entry points; run scripts by file path with explicit flags, for example `python src/ex7_1.py --num-bits 4 --instructions resources/instructs/i1.txt` or `python src/ex7_1_exact.py --num-bits 4 --instructions resources/instructs/i1.txt`.
- `scripts/run_all_tests.sh` is not the pytest suite; it runs `src/ex7_1.py` over classical `resources/instructs/test[0-9]*.txt` files using `NUM_BITS=4`.
- Instruction files use 1-based indices; parsers convert to 0-based indices internally.
- Integer-encoded states use `1 << i`, so internal index `0` is the least-significant bit, even when printed as binary.
- `src/ex7_1.py` is a first-order marginal approximation and intentionally does not track correlations between bits.
- `src/ex7_1_exact.py` tracks a full joint distribution as `dict[int, Fraction]` and is the reference for exact probabilistic behavior.
- `src/ex20.py` is the quantum-amplitude simulator: `HAD` replaces `RNG`, amplitudes use SymPy exact values, and `extract_all` is still a TODO.

## Learning Resources

- Keep lecture transcripts in `resources/lectures/transcripts/` and matching summaries in `resources/lectures/summaries/`; update `resources/lectures/summaries/index.md` when summaries are added or renamed.
- Keep exercise markdown in `resources/exercises/md/`; preserve the numbered filename prefixes and lesson titles.
- Completed exercise or course notes live in `wiki/`; update `wiki/index.md` whenever wiki notes are added or renamed.
- Wiki notes should cite source files, distinguish original sources from derived readings, and mark ambiguous handwriting or partial evidence instead of overclaiming completion.

## Raw Sources

- `raw/GoodNotes` is a symlink to the Google Drive `Undergraduate Quantum Computation` folder; keep originals unchanged.
- Treat `raw/GoodNotes/Exercises.pdf` and `raw/GoodNotes/Solution_Pics/` as primary handwritten exercise evidence.
- `raw/GoodNotes_JPEG/` holds transport JPEGs for multimodal review; store model readings in `raw/GoodNotes_JPEG/llm-readings/` and do not use local OCR as the reading source for handwriting.
- For handwritten review, use `opencode run -m openai/gpt-5.5` with one JPEG attached at a time, then cite both the original and the derived reading in wiki notes.
- IBM Quantum Learning source URLs are documented in `raw/IBM_Qiskit_QInfo_Slides/README.md`; derived slide text is under `raw/IBM_Qiskit_QInfo_Slides/md/` and lecture transcripts under `raw/IBM_Qiskit_QInfo_Slides/lecture_transcripts/`.
