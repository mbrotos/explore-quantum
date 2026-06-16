---
title: IBM Qiskit QInfo Lesson 3: Quantum Circuits
entity_type: course_section_note
source_files:
  - raw/IBM_Qiskit_QInfo_Slides/03-quantum-circuits.pdf
  - raw/IBM_Qiskit_QInfo_Slides/md/03-quantum-circuits.md
  - raw/IBM_Qiskit_QInfo_Slides/images/03-quantum-circuits/
  - raw/IBM_Qiskit_QInfo_Slides/lecture_transcripts/005-30U2DTfIrOU-Quantum Circuits ｜ Understanding Quantum Information & Computation ｜ Lesson 03.txt
source_urls:
  - https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information/quantum-circuits/introduction
---

# IBM Qiskit QInfo Lesson 3: Quantum Circuits

## Learning Objectives
- Introduce the quantum circuit model as an acyclic left-to-right computation model.
- Connect circuit diagrams to matrix products and tensor-product ordering.
- Define inner products, orthonormal bases, projections, and projective measurements.
- Explain global phase equivalence, no-cloning, and limits on distinguishing quantum states.
- Prepare the formal language needed for teleportation, superdense coding, and CHSH.

## Quantum Circuit Model
- Wires carry qubits through time.
- Gates represent unitary operations or measurements.
- Information flows left to right, so the circuit operation is a matrix product in reverse visual order.
- Circuits may include classical wires, usually shown as double lines, to store measurement outcomes or classically control later operations.

## Qiskit Ordering Convention
- Qiskit's top qubit has index `0`.
- In tuple/string/tensor-product ordering, that top qubit corresponds to the rightmost position.
- This is a frequent source of confusion when comparing circuit diagrams, basis strings, matrices, and local simulators.
- Future local quantum simulators should choose and document a single convention before implementing multi-qubit gates.

## Circuit Examples
- A one-qubit circuit applying `H`, then `S`, then `H`, then `T` has total operation `T H S H`.
- A Bell-state circuit applies `H` to one qubit and then `CNOT` to create `(|00> + |11>) / sqrt(2)` from `|00>`.
- Measurement gates can either write to classical bits or be understood as discarding the post-measurement qubit.

## Inner Products And Orthonormality
- The inner product `<psi|phi>` is computed using the conjugate transpose of `|psi>`.
- A vector norm is `sqrt(<psi|psi>)`.
- Orthogonal states have inner product `0`.
- An orthonormal basis is a basis of unit vectors that are pairwise orthogonal.
- A unitary matrix has orthonormal rows and columns.

## Projections And Projective Measurements
- A projection `Pi` satisfies `Pi^dagger = Pi` and `Pi^2 = Pi`.
- A projective measurement is a collection of projections whose sum is the identity.
- Outcome probability is `|| Pi_a |psi> ||^2`, equivalently `<psi|Pi_a|psi>`.
- The post-measurement state is `Pi_a |psi> / || Pi_a |psi> ||`.
- Standard-basis measurement is the special case with projections `|a><a|`.
- Partial measurement can be represented by projections such as `|a><a| tensor I`.

## Limits On Quantum Information
- Global phase is physically irrelevant: `|psi>` and `alpha|psi>` represent the same physical state when `|alpha| = 1`.
- Relative phase is not irrelevant because later operations can convert it into measurement differences.
- No universal unitary can clone arbitrary quantum states.
- Non-orthogonal states cannot be perfectly distinguished.

## Connections To Ryan Notes And Local Simulators
- Ryan's path diagrams and matrix exercises are an operational route to the same circuit formalism.
- `wiki/exercise-017-path-diagrams-adjoints-inner-products.md` and `wiki/exercise-018-unitary-adjoints-undo-operations.md` align closely with IBM's inner-product, projection, and adjoint language.
- `src/ex5_1.py` and `src/ex7_1_exact.py` are classical/probabilistic precursors, not full quantum simulators.
- A lesson-20 style local quantum simulator will need complex amplitudes, full state vectors, unitary application, measurement sampling, and a documented bit-ordering convention.

## Source Quality Notes
- Circuit diagrams and exact matrices should be checked against the PDF or slide images.
- The extracted Markdown can drop or distort conjugation marks and matrix layout.
- The transcript contains ASR errors such as gate and product-name mishearings, but it is useful for explanatory flow.
