# Toggling qubits

- A quantum computer is introduced as a programmable device that natively supports a new data type called a qubit, with basic states written as `|0>` and `|1>`.
- The lecture walks through simple quantum pseudocode using `new qubit`, `toggle`, conditional toggles, and `extract all`, showing that qubits can initially behave like ordinary 0/1 variables.
- A sample program is traced step by step to show how four qubits change state and finally print `0111` after measurement.
- The key distinction is previewed: these reversible toggle-style operations are the "boring" part, while a special instruction called `Hadamard` is what creates genuinely quantum behavior.
- Key takeaway: before superposition feels mysterious, it helps to see that quantum programs still begin with familiar state changes you can trace exactly.
