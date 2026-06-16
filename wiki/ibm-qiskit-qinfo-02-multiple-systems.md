---
title: IBM Qiskit QInfo Lesson 2: Multiple Systems
entity_type: course_section_note
source_files:
  - raw/IBM_Qiskit_QInfo_Slides/02-multiple-systems.pdf
  - raw/IBM_Qiskit_QInfo_Slides/md/02-multiple-systems.md
  - raw/IBM_Qiskit_QInfo_Slides/images/02-multiple-systems/
  - raw/IBM_Qiskit_QInfo_Slides/lecture_transcripts/004-DfZZS8Spe7U-Multiple Systems ｜ Understanding Quantum Information & Computation ｜ Lesson 02.txt
source_urls:
  - https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information/multiple-systems/introduction
---

# IBM Qiskit QInfo Lesson 2: Multiple Systems

## Learning Objectives
- Extend single-system state vectors to compound systems.
- Use Cartesian products for classical state spaces and tensor products for vector spaces.
- Distinguish product states from correlated classical states and entangled quantum states.
- Understand partial measurement of one subsystem.
- Represent independent and controlled operations on multiple systems.

## Compound Systems
- If system `X` has classical state set `Sigma` and system `Y` has state set `Gamma`, then the combined system has state set `Sigma x Gamma`.
- For multiple bits, this gives bitstrings such as `00`, `01`, `10`, and `11`.
- IBM emphasizes an ordering convention: basis states are ordered lexicographically, and in Qiskit the top wire has index `0` but corresponds to the rightmost position in the tuple/string convention.

## Tensor Products
- The tensor product combines independent vectors and matrices.
- If `|phi> = sum_a alpha_a |a>` and `|psi> = sum_b beta_b |b>`, then `|phi> tensor |psi>` has amplitudes `alpha_a beta_b` on `|ab>`.
- Matrix tensor products satisfy `(M tensor N)(|phi> tensor |psi>) = M|phi> tensor N|psi>`.
- Tensor products are the algebraic tool behind independent subsystems, independent operations, and multi-qubit state spaces.

## Correlation And Entanglement
- A probabilistic state is independent when joint probabilities factor into products of marginal probabilities.
- A quantum product state is one that can be written as `|phi> tensor |psi>`.
- In the simplified pure-state setting, an entangled state is a multi-system quantum state that is not a product state.
- The Bell state `(|00> + |11>) / sqrt(2)` is the central example of a two-qubit entangled state.

## Partial Measurement
- Measuring one subsystem aggregates probability over the unmeasured subsystem.
- In quantum notation, write `|psi> = sum_a |a> tensor |phi_a>`.
- The probability of outcome `a` is `|| |phi_a> ||^2`.
- The post-measurement state is the normalized projection onto the measured outcome branch.
- This is the formal basis for later circuit measurements and entanglement protocols.

## Multi-System Operations
- Independent operations are represented by tensor products such as `U tensor V`.
- Controlled operations are not generally product operations.
- A controlled-`U` can be written as `|0><0| tensor I + |1><1| tensor U`.
- Important examples include `CNOT`, controlled-`Z`, `SWAP`, Fredkin, and Toffoli.

## Important Examples
- Correlated classical state: probability `1/2` on `00` and `1/2` on `11`.
- Bell states: `phi+`, `phi-`, `psi+`, and `psi-`.
- Three-qubit entangled states such as GHZ and W states.
- `H tensor I` versus `I tensor H`, illustrating how wire/system ordering matters.

## Connections To Ryan O'Donnell Notes
- Formalizes the multi-qubit path diagrams from `wiki/exercise-008-left-cyclic-shift-path-diagrams.md` and `wiki/exercise-009-matrix-multiplication-path-counts.md`.
- Provides the linear-algebra language behind composite operations in `wiki/exercise-013-composite-quantum-instructions.md` and `wiki/exercise-016-composite-operations-matrix-products.md`.
- Connects to Ryan Lesson 16 on Hadamard acting while other qubits are present.
- Adds a clearer field-standard definition of entanglement than the early Ryan notes have reached so far.

## Source Quality Notes
- The PDF and images should be used for exact tensor-product and matrix layouts.
- The extracted Markdown has visible layout artifacts around matrices and radicals.
- The transcript is useful but contains ASR errors, especially around ket notation and gate names.
- The slide deck notes a video typo in one partial-measurement formula, so verify formulas against the corrected slide text/images.
