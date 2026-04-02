import argparse
import random


def toggle_bit(bits, i):
    bits[i] = 1 - bits[i]


def random_bit(bits, i):
    bits[i] = random.randint(0, 1)


instructions_dict = {
    "NOT": lambda i, bits: toggle_bit(bits, i),
    "CNOT": lambda i, j, bits: toggle_bit(bits, j) if bits[i] == 1 else bits[j],
    "CCNOT": lambda i, j, k, bits: (
        toggle_bit(bits, k) if bits[i] == 1 and bits[j] == 1 else bits[k]
    ),
    "RNG": lambda i, bits: random_bit(bits, i),
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

    bits = [0] * n

    # Read instructions from file
    instruction_str = ""
    with open(args.instructions_path, "r") as f:
        instruction_str = f.read()

    # Parse instructions
    instructions = parse_instructions(instruction_str)

    # Execute instructions
    for op, indices in instructions:
        instructions_dict[op](*indices, bits)

    # Print final bits
    print("Final bits:", bits)


if __name__ == "__main__":
    main()
