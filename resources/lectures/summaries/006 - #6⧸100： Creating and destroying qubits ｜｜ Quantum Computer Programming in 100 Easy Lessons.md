# Creating and destroying qubits

- The lecture separates quantum instructions into state-manipulation operations and two special edge cases: creating qubits with `new qubit` and destroying them with `extract all`.
- `new qubit` allocates a named qubit and initializes it to the basic state `|0>`, which can also be viewed as a special superposition with all amplitude on one basis state.
- Multiple qubits together form a larger joint state, so even a simple basis state like `|00>` is really shorthand for amplitudes over all possible combined outcomes.
- `extract all` measures the qubits, returns ordinary classical bits according to the measurement probabilities, and logically destroys the qubits afterward.
- Key takeaway: measurement is not just reading data; it is the moment where fragile quantum state is converted into classical information and the original qubits are no longer available.
