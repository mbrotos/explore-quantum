"""Probabilistic bit-circuit simulator (exact / full joint distribution).

Unlike `src/ex7_1.py` (first-order, independent-bit approximation), this script
is intended to track the full probability distribution over all 2^n bitstrings.

# Representation suggestion:
# - Use a dict: `dist: dict[int, Fraction]` mapping a bitstring encoded as an int
#   (0..2^n-1) to its probability.
# - Bit i corresponds to the i-th bit in the instruction file (1-based there),
#   but you will likely convert to 0-based indices internally.
"""

import argparse
from fractions import Fraction


def parse_instructions(instruction_str, num_bits):
    """Parse an instruction file into a list of (op, indices).

    Indices are converted to 0-based.
    """
    instructions = []
    for i, line in enumerate(instruction_str.strip().splitlines()):
        parts = line.split()
        if not parts:
            raise ValueError("Empty instruction line.")
        op = parts[0]
        indices = list(map(lambda x: x - 1, map(int, parts[1:])))
        for indx in indices:
            if not (0 <= indx < num_bits):
                raise IndexError(
                    f"Line {i+1} contains an bit index which is out of range."
                )
        instructions.append((op, indices))
    return instructions


def apply_NOT(dist, i, n):
    """Apply NOT (X) gate to bit i.

    Move probability mass from each bitstring to the bitstring with bit i
    flipped.
    """

    mask = 1 << i  # only the bit with index i from the right is 1.
    dist_new = {}

    for k, v in dist.items():
        toggled_state = k ^ mask
        dist_new[toggled_state] = v  # Move probability mass

    return dist_new


def apply_CNOT(dist, i, j, n):
    """Apply CNOT with control i and target j.

    For each bitstring, if control bit is 1, flip the target bit.
    """

    mask_control = 1 << i
    mask_target = 1 << j
    dist_new = {}

    for k, v in dist.items():
        if k & mask_control > 0:
            # control bit is 1
            k_new = k ^ mask_target
            dist_new[k_new] = v
        else:
            dist_new[k] = v  # No change

    return dist_new


def apply_CCNOT(dist, i, j, k, n):
    """Apply CCNOT (Toffoli) with controls i, j and target k.

    TODO: For each bitstring, if both control bits are 1, flip the target bit.
    """
    raise NotImplementedError


def apply_RNG(dist, i, n):
    """Randomize bit i to be 0/1 with probability 1/2 each.

    TODO: Split probability mass for each bitstring into two outcomes where bit
    i is forced to 0 vs forced to 1.
    """
    raise NotImplementedError


def apply_instruction(dist, op, indices, n):
    """Dispatch one instruction to the appropriate transition."""
    if op == "NOT":
        return apply_NOT(dist, indices[0], n)
    if op == "CNOT":
        return apply_CNOT(dist, indices[0], indices[1], n)
    if op == "CCNOT":
        return apply_CCNOT(dist, indices[0], indices[1], indices[2], n)
    if op == "RNG":
        return apply_RNG(dist, indices[0], n)
    raise ValueError(f"Unknown instruction: {op}")


def main():
    parser = argparse.ArgumentParser(
        description="Probabilistic Computer Simulator (Exact Distribution)"
    )
    parser.add_argument("num_bits", type=int, help="Number of bits")
    parser.add_argument("instructions_path", type=str, help="Path to instructions file")
    args = parser.parse_args()

    n = args.num_bits
    if n <= 0:
        print("Number of bits must be positive.")
        return

    # Distribution over all bitstrings; start in |0...0> with prob 1.
    dist = {0: Fraction(1, 1)}

    with open(args.instructions_path, "r") as f:
        instruction_str = f.read()

    instructions = parse_instructions(
        instruction_str,
    )

    for op, indices in instructions:
        if not (0 <= indices < n):
            raise IndexError(f"Cannot apply NOT to i={indices} since n={n}")
        dist = apply_instruction(dist, op, indices, n)

    # Probability of the all-zeros state is just the mass on bitstring 0.
    p0 = dist.get(0, Fraction(0, 1))
    print("Prob of |0...0>: ", p0, "= ", float(p0))


if __name__ == "__main__":
    main()
