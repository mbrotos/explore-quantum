# Mystery Toggles

- The lecture frames a black-box guessing game: a hidden subroutine may contain any subset of six instructions of the form `if xi then toggle answer`, giving 64 possible secrets.
- Classically, each call reveals only one bit of information, so identifying the hidden subset takes at least six carefully chosen queries when there are six controls.
- A quantum strategy uses `toggle answer`, `Hadamard all`, one call to the black box, and `Hadamard all` again to recover the entire hidden pattern in a single query.
- This demonstrates a real quantum advantage: superposition lets one query probe many possibilities at once, and interference turns that into useful information.
- Key takeaway: quantum speedups come from treating the hidden function as a black box and exploiting superposition, not from simply tracing ordinary 0/1 logic faster.
