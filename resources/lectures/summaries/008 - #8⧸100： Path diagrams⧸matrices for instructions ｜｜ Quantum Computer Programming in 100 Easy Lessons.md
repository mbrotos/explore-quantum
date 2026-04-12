# Path diagrams⧸matrices for instructions

- The lecture develops a visual and algebraic way to describe gates: path diagrams show how each incoming basis state connects to outgoing basis states, and matrices store the same information in table form.
- For classical reversible gates like `toggle`, `CNOT`, `CCNOT`, and `swap`, the diagrams mostly contain 0s and 1s because each basis state maps to exactly one basis state.
- The matrix columns correspond to incoming basis states, and the rows correspond to outgoing basis states, so each column tells you the full output superposition for one input basis state.
- This representation matters because once you know what a gate does to all basis states, you have enough information to determine its action on any superposition later.
- Key takeaway: path diagrams and matrices are the quantum version of a truth table, but they are built to handle amplitudes, not just deterministic bit outputs.
