---
title: IBM Qiskit Basics of Quantum Information Course Overview
entity_type: course_overview
source_files:
  - raw/IBM_Qiskit_QInfo_Slides/README.md
  - raw/IBM_Qiskit_QInfo_Slides/01-single-systems.pdf
  - raw/IBM_Qiskit_QInfo_Slides/02-multiple-systems.pdf
  - raw/IBM_Qiskit_QInfo_Slides/03-quantum-circuits.pdf
  - raw/IBM_Qiskit_QInfo_Slides/04-entanglement-in-action.pdf
  - raw/IBM_Qiskit_QInfo_Slides/lecture_transcripts/
source_urls:
  - https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information
---

# IBM Qiskit Basics of Quantum Information Course Overview

## Course Role
- This IBM Quantum Learning course is a formal introduction to quantum information and computation.
- It starts from finite classical systems and builds toward quantum state vectors, measurements, unitary operations, tensor products, circuits, and entanglement protocols.
- Compared with the Ryan O'Donnell course notes in this repo, IBM uses the standard field vocabulary earlier: Dirac notation, stochastic matrices, unitary matrices, tensor products, projective measurements, Bell states, and Qiskit circuit conventions.

## Section Map
- [Single Systems](ibm-qiskit-qinfo-01-single-systems.md): finite classical systems, probability vectors, Dirac notation, quantum state vectors, measurement, and unitaries.
- [Multiple Systems](ibm-qiskit-qinfo-02-multiple-systems.md): Cartesian-product state spaces, tensor products, product states, partial measurement, entanglement, and controlled operations.
- [Quantum Circuits](ibm-qiskit-qinfo-03-quantum-circuits.md): circuit notation, Qiskit ordering, inner products, projections, projective measurements, global phase, no-cloning, and state discrimination.
- [Entanglement in Action](ibm-qiskit-qinfo-04-entanglement-in-action.md): teleportation, superdense coding, and the CHSH game as examples of entanglement as a computational and communication resource.

## High-Level Progression
- Classical information is modeled with probability vectors and stochastic operations.
- Quantum information is modeled with complex unit vectors and unitary operations.
- Measurement converts amplitudes into classical outcomes through squared magnitudes.
- Multiple systems are combined with tensor products, which makes entanglement possible.
- Circuits organize unitary gates and measurements into an operational computation model.
- Entanglement enables communication and correlation protocols with no direct classical analogue.

## How This Complements The Ryan Notes
- Ryan's course emphasizes programming intuition, toggles, path diagrams, amplitude flow, and interference.
- IBM's course gives the standard mathematical and software-facing formalism behind those intuitions.
- Together, they support two views of the same material: how quantum programs behave operationally, and how the broader field writes them formally.

## Source Quality Notes
- The PDFs are the primary raw slide sources.
- `raw/IBM_Qiskit_QInfo_Slides/md/` contains `pdftotext -layout` extractions. These are useful for search and text synthesis, but formulas and matrices can be garbled.
- `raw/IBM_Qiskit_QInfo_Slides/images/` contains per-slide JPEG renders for visual checking.
- `raw/IBM_Qiskit_QInfo_Slides/lecture_transcripts/` contains lecture transcripts. They are useful for explanation and emphasis, but may contain automatic-transcription errors.
