# How Toggles Detective works (Part 1⧸2)

- Starts analyzing the `mystery toggles` algorithm in a reduced three-qubit case with `x1`, `x2`, and an answer qubit.
- Rewrites the Hadamard steps as `add and diff` operations and tracks the eight amplitudes on the corners of a cube for clarity.
- Shows how repeated add-and-difference operations spread amplitudes across all basis states with a structured sign pattern.
- Works through the simplest mystery case, where the mystery subroutine contains no toggles, and observes that the final Hadamards undo the initial ones.
- Key takeaway: the detective algorithm is built so the surrounding Hadamard layers prepare and then decode information about the hidden subroutine.
