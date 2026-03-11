import argparse
import math


class Probability:
    def __init__(self, prob=1 / 2):
        self.prob = prob  # Prob of being 1

    def __add__(self, other):
        if isinstance(other, Probability):
            Probability(self.prob + other.prob)
        else:
            raise ValueError("Cannot add prob with bit.")

    def __mul__(self, other):
        if isinstance(other, Probability):
            Probability(self.prob * other.prob)
        else:
            return Probability(self.prob * other)


def toggle_bit(bits, i):
    bits[i] = 1 - bits[i]


def random_bit(i, bits):
    bits[i] = Probability(1 / 2)


def CNOT_prob(i, j, bits):
    if isinstance(bits[i], Probability) and bits[i].prob > 0.0:
        if isinstance(bits[j], Probability):
            bits[j] = bits[j] * bits[i]
        elif bits[j] == 0:
            bits[j] = bits[i]
        elif bits[j] == 1:
            bits[j] = 1 - bits[i]
        else:
            raise ValueError("Invalid bit value.")
    elif bits[i] == 1:
        toggle_bit(bits, j)
    else:
        return


def CCNOT_prob(i, j, k, bits):
    conjunction_prob = None
    if isinstance(bits[i], Probability) or isinstance(bits[j], Probability):
        conjunction_prob = bits[i] * bits[j]

    if isinstance(conjunction_prob, Probability):
        if conjunction_prob.prob > 0.0:
            if isinstance(bits[k], Probability):
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
        toggle_bit(bits, k)
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

    # Invert probs so that its the prob of being 0
    bits_probs = [1 - prob for prob in bits_probs]

    # Multiply probs
    prob = math.prod(bits_probs)

    print("Prob of |000...0>: ", prob)


if __name__ == "__main__":
    main()
