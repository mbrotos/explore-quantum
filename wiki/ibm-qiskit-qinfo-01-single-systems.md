---
title: IBM Qiskit QInfo Lesson 1: Single Systems
entity_type: course_section_note
source_files:
  - raw/IBM_Qiskit_QInfo_Slides/01-single-systems.pdf
  - raw/IBM_Qiskit_QInfo_Slides/md/01-single-systems.md
  - raw/IBM_Qiskit_QInfo_Slides/images/01-single-systems/
  - raw/IBM_Qiskit_QInfo_Slides/lecture_transcripts/003-3-c4xJa7Flk-Single Systems ｜ Understanding Quantum Information & Computation ｜ Lesson 01.txt
source_urls:
  - https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information/single-systems/introduction
---

# IBM Qiskit QInfo Lesson 1: Single Systems

## Learning Objectives
- Model one finite information-bearing system mathematically.
- Compare classical deterministic, probabilistic, and quantum descriptions.
- Introduce Dirac notation for standard basis vectors and arbitrary states.
- Define measurement as the interface from state descriptions to observed classical outcomes.
- Identify unitary matrices as the simplified model of valid quantum operations.

## Classical Reference Model
- A system has a finite classical state set `Sigma`.
- A deterministic classical state is represented by a basis vector such as `|a>`.
- A probabilistic state is a vector with nonnegative real entries summing to `1`.
- Measuring a probabilistic state returns a classical state with its corresponding probability and updates the state to the observed basis vector.
- A deterministic operation is a function `f: Sigma -> Sigma`, represented by a matrix that maps `|a>` to `|f(a)>`.
- A general probabilistic operation is represented by a stochastic matrix: entries are nonnegative and columns sum to `1`.

## Dirac Notation
- `|a>` denotes a standard basis column vector indexed by classical state `a`.
- `<a|` denotes the corresponding row vector.
- `<a|b>` is `1` when `a = b` and `0` otherwise.
- `|a><b|` is an outer-product matrix useful for defining operations by their action on basis states.
- For an arbitrary state `|psi>`, `<psi|` is the conjugate transpose of `|psi>`.

## Quantum States And Measurement
- A quantum state is a complex unit vector indexed by the same classical state set.
- A qubit state has the form `alpha|0> + beta|1>`, with `|alpha|^2 + |beta|^2 = 1`.
- Standard-basis measurement returns outcome `a` with probability equal to the squared magnitude of the amplitude on `|a>`.
- Measurement discards phase information directly visible in the amplitudes, but phases still matter because later operations can convert phase differences into measurable probability differences.

## Unitary Operations
- In the simplified quantum model, operations are represented by unitary matrices.
- A matrix `U` is unitary when `U^dagger U = I = U U^dagger`.
- Unitaries preserve vector norm, so they map valid quantum states to valid quantum states.
- Composition order follows matrix multiplication: if `M1` happens first and `M2` happens second, the combined operation is `M2 M1`.

## Core Examples
- `|+> = (|0> + |1>) / sqrt(2)` and `|-> = (|0> - |1>) / sqrt(2)` both measure to `0` or `1` with probability `1/2`, but behave differently under later operations.
- `X` is the quantum NOT or bit-flip gate.
- `Z` is a phase-flip gate that maps `|1>` to `-|1>` while leaving `|0>` fixed.
- `H` maps `|0>` to `|+>`, `|1>` to `|->`, `|+>` to `|0>`, and `|->` to `|1>`.
- Phase gates `P_theta`, especially `S` and `T`, introduce complex phases.
- `HSH` is a square root of NOT: applying it twice gives `X`.

## Connections To Ryan O'Donnell Notes
- Supports the valid-state and normalization work in `wiki/exercise-004-valid-quantum-states.md`.
- Formalizes the probability-vector ideas behind `src/ex5_1.py` and `src/ex7_1_exact.py`.
- Connects directly to the unitary-property notes in `wiki/exercise-014-unitary-property.md` and Hadamard notes in `wiki/exercise-015-clockwise-counterclockwise-unitaries.md`.
- Gives standard notation for ideas Ryan introduces through path diagrams, toggles, and amplitude flow.

## Source Quality Notes
- The PDF and slide images are best for formulas and matrices.
- The extracted Markdown is useful for search but contains layout artifacts in fractions and matrices.
- The transcript is explanatory but contains automatic-transcription errors, including occasional terminology mistakes around Dirac notation.
