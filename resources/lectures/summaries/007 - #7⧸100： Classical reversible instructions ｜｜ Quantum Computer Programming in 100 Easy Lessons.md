# Classical reversible instructions

- The lecture introduces the main "classical" quantum gates such as `toggle`, `if A then toggle B`, `if A and B then toggle C`, plus derived operations like `swap`.
- These are called classical because they map basis states to basis states, so they still make sense if the variables are just ordinary bits.
- They are also reversible: every valid qubit-manipulation instruction must have an undo operation, which rules out familiar irreversible commands like `A := 1`.
- Many simple gates happen to be their own undo, though more complex reversible operations, like cyclic shifts, may require a different inverse.
- Key takeaway: the allowed non-measurement operations in quantum computing are tightly constrained by reversibility, which is a physical law, not just a programming style choice.
