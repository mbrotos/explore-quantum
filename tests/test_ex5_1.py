import pytest

from src import ex5_1


def test_parse_instructions_converts_indices_to_zero_based():
    instruction_str = "NOT 1\nCNOT 1 2\nCCNOT 1 2 3\nRNG 4"

    result = ex5_1.parse_instructions(instruction_str)

    assert result == [
        ("NOT", [0]),
        ("CNOT", [0, 1]),
        ("CCNOT", [0, 1, 2]),
        ("RNG", [3]),
    ]


def test_not_instruction_flips_the_target_bit():
    bits = [0, 0]

    ex5_1.instructions_dict["NOT"](0, bits)

    assert bits == [1, 0]


def test_cnot_flips_target_when_control_is_one():
    bits = [1, 0, 0]

    ex5_1.instructions_dict["CNOT"](0, 2, bits)

    assert bits == [1, 0, 1]


def test_ccnot_flips_target_when_both_controls_are_one():
    bits = [1, 1, 0]

    ex5_1.instructions_dict["CCNOT"](0, 1, 2, bits)

    assert bits == [1, 1, 1]


def test_rng_instruction_sets_bit_from_random_source(monkeypatch):
    # Make RNG deterministic for this test.
    monkeypatch.setattr(ex5_1.random, "randint", lambda _a, _b: 1)
    bits = [0]

    ex5_1.instructions_dict["RNG"](0, bits)

    assert bits == [1]


def test_parse_instructions_rejects_unknown_operations():
    with pytest.raises(ValueError):
        ex5_1.parse_instructions("HADAMARD 1")
