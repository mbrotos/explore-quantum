"""Exercise 20: Quantum Programming Paradigm 1.

This exercise extends the earlier probabilistic simulator into a quantum
computer simulator. The input format is almost the same as before, but the
variables now represent qubits, and `HAD` (Hadamard) replaces the earlier `RNG`
instruction.

The simulator should output two things: the exact final amplitude on the
all-zero basis state |00...0>, and one sampled n-bit string representing what
would happen if the program ended with an "extract all" measurement. The exact
amplitude should be deterministic across runs; the sampled bitstring may change.
"""

import argparse

from sympy import Rational, sqrt


def parse_instructions(instruction_str, num_qubits):
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
            if not (0 <= indx < num_qubits):
                raise IndexError(
                    f"Line {i+1} contains a qubit index which is out of range."
                )
        instructions.append((op, indices))
    return instructions


def apply_NOT(amplitudes, i):
    """Apply NOT (X) gate to qubit i.

    Move each amplitude to the computational basis state with qubit i flipped.
    """

    mask = 1 << i  # only the basis-state bit for qubit i is 1.
    amplitudes_new = {}

    for basis_state, amplitude in amplitudes.items():
        toggled_state = basis_state ^ mask
        amplitudes_new[toggled_state] = amplitude

    return amplitudes_new


def apply_CNOT(amplitudes, i, j):
    """Apply CNOT with control i and target j.

    For each computational basis state, if the control qubit is 1, flip the
    target qubit.
    """
    if i == j:
        raise ValueError("CNOT indices must be unique.")

    mask_control = 1 << i
    mask_target = 1 << j
    amplitudes_new = {}

    for basis_state, amplitude in amplitudes.items():
        if basis_state & mask_control > 0:
            # control qubit is 1
            basis_state_new = basis_state ^ mask_target
            amplitudes_new[basis_state_new] = amplitude
        else:
            amplitudes_new[basis_state] = amplitude  # No change

    return amplitudes_new


def apply_CCNOT(amplitudes, i, j, k):
    """Apply CCNOT (Toffoli) with controls i, j and target k.

    For each computational basis state, if both control qubits are 1, flip the
    target qubit.
    """

    if i == j or j == k or i == k:
        raise ValueError("CCNOT indices must be unique.")

    mask_control_i = 1 << i
    mask_control_j = 1 << j
    mask_target_k = 1 << k

    amplitudes_new = {}

    for basis_state, amplitude in amplitudes.items():
        if basis_state & mask_control_i > 0 and basis_state & mask_control_j > 0:
            # control qubits i and j are 1
            basis_state_new = basis_state ^ mask_target_k
            amplitudes_new[basis_state_new] = amplitude
        else:
            amplitudes_new[basis_state] = amplitude  # No change

    return amplitudes_new


def apply_HAD(amplitudes, i):
    """Apply Hadamard gate to qubit i.

    Split amplitude from each computational basis state based on the following
    single-qubit rules:
    - |0> -> |0> with amplitude sqrt(1/2),
    - |0> -> |1> with amplitude sqrt(1/2),
    - |1> -> |0> with amplitude sqrt(1/2), and
    - |1> -> |1> with amplitude -sqrt(1/2).

    """
    mask = 1 << i
    amplitudes_new = {}

    for basis_state, amplitude in amplitudes.items():
        untoggled_sign = 1
        new_state = basis_state ^ mask  # get the toggled state
        if basis_state < new_state:  # then qubit i was |...1...>
            untoggled_sign *= -1  # therefore, the untoggled state has -ev amp.
        new_amp = amplitude * sqrt(
            Rational(1, 2)
        )  # The new amplitude will be a factor of sqrt(1/2).
        amplitudes_new[basis_state] = (
            amplitudes_new.get(basis_state, Rational(0, 1)) + untoggled_sign * new_amp
        )  # untoggled states get ±new_amp
        amplitudes_new[new_state] = (
            amplitudes_new.get(new_state, Rational(0, 1)) + new_amp
        )  # toggled gets new_amp

    return amplitudes_new


def apply_instruction(amplitudes, op, indices):
    """Dispatch one instruction to the appropriate transition."""
    if op == "NOT":
        return apply_NOT(amplitudes, indices[0])
    if op == "CNOT":
        return apply_CNOT(amplitudes, indices[0], indices[1])
    if op == "CCNOT":
        return apply_CCNOT(amplitudes, indices[0], indices[1], indices[2])
    if op == "HAD":
        return apply_HAD(amplitudes, indices[0])
    raise ValueError(f"Unknown instruction: {op}")


def format_all_amps(amplitudes, num_qubits):
    all_amps = "Full quantum state:\n"
    for basis_state, amplitude in sorted(amplitudes.items()):
        all_amps += f"\t|{basis_state:0{num_qubits}b}>: {amplitude}\n"

    return all_amps


def main():
    parser = argparse.ArgumentParser(description="Quantum Computer Simulator")
    parser.add_argument(
        "--num-qubits", "-n", type=int, required=True, help="Number of qubits"
    )
    parser.add_argument(
        "--instructions",
        "-i",
        dest="instructions_path",
        required=True,
        help="Path to instructions file",
    )
    args = parser.parse_args()

    n = args.num_qubits
    if n <= 0:
        print("Number of qubits must be positive.")
        return

    # Amplitudes over computational basis states; start in |0...0>.
    amplitudes = {0: Rational(1, 1)}

    with open(args.instructions_path, "r") as f:
        instruction_str = f.read()

    instructions = parse_instructions(instruction_str, n)

    for op, indices in instructions:
        amplitudes = apply_instruction(amplitudes, op, indices)

    # Amplitude of the all-zero computational basis state.
    amp0 = amplitudes.get(0, Rational(0, 1))
    print("Amplitude of |0...0>: ", amp0, "= ", float(amp0))

    print(format_all_amps(amplitudes, args.num_qubits))

    # TODO: extract_all
    # basically we will turn the amplitudes into probs and then sample.


if __name__ == "__main__":
    main()
