# How Toggles Detective works (Part 2⧸2)

- Continues the cube-based amplitude analysis for the case where the mystery subroutine contains `if x1 then toggle answer` but not the `x2` version.
- Models the mystery call as swapping amplitudes on specific cube edges, rather than relabeling the basis states.
- Applies `add and diff` again on the answer, `x2`, and `x1` directions, causing large-scale cancellation of many amplitudes.
- Ends with all amplitude concentrated on the single basis state `101`, which reveals exactly which hidden toggle is present.
- Key takeaway: the algorithm works by arranging interference so wrong answers cancel out and the correct hidden pattern survives with full amplitude.
