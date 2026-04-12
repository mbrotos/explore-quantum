# Unnormalized states

- Introduces unnormalized states as a bookkeeping trick: you may scale all amplitudes by the same nonzero constant during calculations.
- Uses this to drop the repeated `sqrt(1/2)` factors from Hadamard and replace it with the cleaner "add and difference" rule.
- Defines the simplified rule: from amplitudes `x` and `y`, the new amplitudes become `x+y` and `x-y`.
- Explains that normalization only needs to be restored when you are about to measure, since probabilities come from the normalized amplitudes.
- Key takeaway: unnormalized states make algebra much cleaner while preserving the real physical answer once you rescale at the end.
