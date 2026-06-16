---
title: IBM Qiskit QInfo Lesson 4: Entanglement in Action
entity_type: course_section_note
source_files:
  - raw/IBM_Qiskit_QInfo_Slides/04-entanglement-in-action.pdf
  - raw/IBM_Qiskit_QInfo_Slides/md/04-entanglement-in-action.md
  - raw/IBM_Qiskit_QInfo_Slides/images/04-entanglement-in-action/
  - raw/IBM_Qiskit_QInfo_Slides/lecture_transcripts/006-GSsElSQgMbU-Entanglement in Action ｜Understanding Quantum Information & Computation ｜ Lesson 04.txt
source_urls:
  - https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information/entanglement-in-action/introduction
---

# IBM Qiskit QInfo Lesson 4: Entanglement in Action

## Learning Objectives
- Treat entanglement as a usable information-processing resource.
- Study three foundational examples: quantum teleportation, superdense coding, and the CHSH game.
- Understand how shared entanglement combines with classical communication or local measurements.
- See how quantum correlations differ from classical shared randomness.

## Entanglement As A Resource
- The central resource is one e-bit: Alice and Bob share the Bell state `|phi+> = (|00> + |11>) / sqrt(2)`.
- Alice holds one qubit and Bob holds the other.
- The shared state can be consumed to communicate quantum information, send more classical information than expected through a qubit channel, or win nonlocal games more often than classical strategies allow.

## Quantum Teleportation
- Goal: Alice transfers an unknown qubit state to Bob without physically sending that qubit.
- Resources: one shared e-bit and two classical bits sent from Alice to Bob.
- Alice applies `CNOT` and `H`, measures her two qubits, and sends the two measurement bits to Bob.
- Bob applies a correction based on the received bits: `I`, `Z`, `X`, or `ZX`.
- The original state appears on Bob's qubit, including any correlations the original qubit had with external systems.
- The protocol does not clone the state; Alice's original qubit is measured and the e-bit is consumed.

## Superdense Coding
- Goal: Alice sends two classical bits to Bob by transmitting one qubit, assuming they already share one e-bit.
- Alice encodes two bits by applying one of four operations to her half of the e-bit.
- Bob receives Alice's qubit, converts the Bell basis back to the computational basis, and measures to recover the two classical bits.
- The protocol complements teleportation: teleportation uses two classical bits plus entanglement to transmit one qubit, while superdense coding uses one qubit plus entanglement to transmit two classical bits.

## CHSH Game
- Alice and Bob receive input bits `x` and `y` and must output bits `a` and `b` without communicating after receiving the inputs.
- They win when `a xor b = x and y`.
- Classical strategies can win with probability at most `3/4`.
- With a shared Bell state and appropriate measurement bases, the quantum strategy wins with probability `(2 + sqrt(2)) / 4`, about `0.85`.
- This is a Bell-test style example of non-classical correlations.

## Mathematical Toolkit
- Bell states form an orthonormal basis for two qubits.
- The lesson repeatedly uses `X`, `Z`, `H`, `CNOT`, standard-basis measurement, and classically controlled corrections.
- CHSH analysis uses angle-parameterized states such as `|psi_theta> = cos(theta)|0> + sin(theta)|1>`.
- The identity `<psi_alpha|psi_beta> = cos(alpha - beta)` supports the CHSH probability calculations.

## Connections To Ryan O'Donnell Notes
- Ryan's current materials emphasize quantum advantage through amplitude paths, Hadamards, and interference.
- IBM adds a complementary advantage story: entanglement as a resource for communication and nonlocal correlations.
- The note connects back to Ryan exercises on valid quantum states, matrix products, unitarity, adjoints, inner products, and Toggles Detective style interference.

## Source Quality Notes
- The PDF and rendered slide images are best for protocol diagrams and formulas.
- The extracted Markdown contains formula and spacing artifacts.
- The transcript contains ASR errors, including names and theorem terminology, so use it mainly for explanation rather than exact formulas.
- The slide deck notes a correction to a video typo in one CHSH state expression.
