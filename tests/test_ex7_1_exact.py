from fractions import Fraction

import pytest

from src import ex7_1_exact


def test_swaps_probability_between_partner_states():
    dist = {0: Fraction(1, 4), 4: Fraction(1, 2), 11: Fraction(1, 4)}

    result = ex7_1_exact.apply_NOT(dist.copy(), 2, 4)

    assert result == {0: Fraction(1, 2), 4: Fraction(1, 4), 15: Fraction(1, 4)}


def test_moves_probability_to_new_state_when_partner_absent():
    dist = {0: Fraction(1, 1)}

    result = ex7_1_exact.apply_NOT(dist.copy(), 1, 2)

    assert result == {2: Fraction(1, 1)}


def test_cnot_leaves_states_unchanged_when_control_bit_is_zero():
    dist = {0: Fraction(1, 2), 2: Fraction(1, 2)}

    result = ex7_1_exact.apply_CNOT(dist.copy(), 0, 1, 2)

    assert result == dist


def test_cnot_flips_target_bit_when_control_bit_is_one():
    dist = {1: Fraction(1, 4), 3: Fraction(3, 4)}

    result = ex7_1_exact.apply_CNOT(dist.copy(), 0, 1, 2)

    assert result == {3: Fraction(1, 4), 1: Fraction(3, 4)}


def test_cnot_updates_multiple_bitstrings_in_one_distribution():
    dist = {
        0: Fraction(1, 4),
        1: Fraction(1, 4),
        2: Fraction(1, 4),
        3: Fraction(1, 4),
    }

    result = ex7_1_exact.apply_CNOT(dist.copy(), 0, 1, 2)

    assert result == {
        0: Fraction(1, 4),
        1: Fraction(1, 4),
        2: Fraction(1, 4),
        3: Fraction(1, 4),
    }


def test_ccnot_leaves_states_unchanged_when_a_control_bit_is_zero():
    dist = {0: Fraction(1, 2), 1: Fraction(1, 2)}

    result = ex7_1_exact.apply_CCNOT(dist.copy(), 0, 1, 2, 3)

    assert result == dist


def test_ccnot_flips_target_bit_when_both_control_bits_are_one():
    dist = {3: Fraction(1, 4), 7: Fraction(3, 4)}

    result = ex7_1_exact.apply_CCNOT(dist.copy(), 0, 1, 2, 3)

    assert result == {7: Fraction(1, 4), 3: Fraction(3, 4)}


def test_ccnot_updates_multiple_bitstrings_in_one_distribution():
    dist = {
        0: Fraction(1, 4),
        3: Fraction(1, 4),
        5: Fraction(1, 4),
        7: Fraction(1, 4),
    }

    result = ex7_1_exact.apply_CCNOT(dist.copy(), 0, 1, 2, 3)

    assert result == {
        0: Fraction(1, 4),
        7: Fraction(1, 4),
        5: Fraction(1, 4),
        3: Fraction(1, 4),
    }


def test_ccnot_raises_when_indices_are_not_unique():
    with pytest.raises(ValueError):
        ex7_1_exact.apply_CCNOT({3: Fraction(1, 1)}, 0, 1, 1, 3)
