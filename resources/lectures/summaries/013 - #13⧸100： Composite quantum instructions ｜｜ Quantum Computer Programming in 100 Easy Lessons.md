# Composite quantum instructions

- Introduces the idea that a block of quantum code can be treated as a new composite instruction with its own path diagram or matrix.
- Uses `Hadamard` followed by `Hadamard` to show that a composite instruction can act exactly like doing nothing, so Hadamard is its own undo.
- Works out a less trivial example, `double clockwise`, by analyzing what it does to `0` and `1` and packaging the result as a new operation.
- Extends the idea to superposition states: once you know how an instruction acts on basis states, amplitude trees tell you how it acts on arbitrary states too.
- Key takeaway: quantum subroutines can be understood as reusable transformations, and basis-state behavior fully determines their effect on larger computations.
