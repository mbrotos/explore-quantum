import argparse
from fractions import Fraction


def toggle_bit(i, bits):
    bits[i] = 1 - bits[i]


def random_bit(i, bits):
    bits[i] = Fraction(1, 2)


def CNOT_prob(i, j, bits):
    if isinstance(bits[i], Fraction) and bits[i] > 0:
        if isinstance(bits[j], Fraction):
            bits[j] = bits[j] * bits[i]
        elif bits[j] == 0:
            bits[j] = bits[i]
        elif bits[j] == 1:
            bits[j] = 1 - bits[i]
        else:
            raise ValueError("Invalid bit value.")
    elif bits[i] == 1:
        toggle_bit(j, bits)
    else:
        return


def CCNOT_prob(i, j, k, bits):
    conjunction_prob = None
    if isinstance(bits[i], Fraction) or isinstance(bits[j], Fraction):
        conjunction_prob = bits[i] * bits[j]

    if isinstance(conjunction_prob, Fraction):
        if conjunction_prob > 0:
            if isinstance(bits[k], Fraction):
                bits[k] = bits[k] * conjunction_prob
            elif bits[k] == 0:
                bits[k] = conjunction_prob
            elif bits[k] == 1:
                bits[k] = 1 - conjunction_prob
            else:
                raise ValueError("Invalid bit value.")
        else:
            return
    elif bits[i] == 1 and bits[j] == 1:
        toggle_bit(k, bits)
    else:
        return


instructions_dict = {
    "NOT": toggle_bit,
    "CNOT": CNOT_prob,  # pass through prob and rebase deoending on j
    "CCNOT": CCNOT_prob,
    "RNG": random_bit,  # 1/2
}


def parse_instructions(instruction_str):
    instructions = []
    for line in instruction_str.strip().splitlines():
        parts = line.split()
        if not parts:
            raise ValueError("Empty instruction line.")
        op = parts[0]
        if op in instructions_dict:
            indices = list(
                map(lambda x: x - 1, map(int, parts[1:]))
            )  # Convert to 0-based index
            instructions.append((op, indices))
        else:
            raise ValueError(f"Unknown instruction: {op}")
    return instructions


def main():
    parser = argparse.ArgumentParser(description="Probabilistic Computer Simulator")
    parser.add_argument("num_bits", type=int, help="Number of bits")
    parser.add_argument("instructions_path", type=str, help="Path to instructions file")
    args = parser.parse_args()

    n = args.num_bits
    if n <= 0:
        print("Number of bits must be positive.")
        return

    bits_probs = [0] * n

    # Read instructions from file
    instruction_str = ""
    with open(args.instructions_path, "r") as f:
        instruction_str = f.read()

    # Parse instructions
    instructions = parse_instructions(instruction_str)

    # Execute instructions
    for op, indices in instructions:
        instructions_dict[op](*indices, bits_probs)

    # Invert probs so that it's the prob of being 0
    bits_probs = [1 - Fraction(prob) for prob in bits_probs]

    # Multiply probs as Fractions
    prob = Fraction(1, 1)
    for p in bits_probs:
        prob *= p

    print("Prob of |0...0>: ", prob, "= ", float(prob))


if __name__ == "__main__":
    main()
