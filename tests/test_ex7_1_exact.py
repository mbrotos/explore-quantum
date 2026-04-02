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


def test_raises_if_bit_index_is_out_of_range():
    with pytest.raises(IndexError):
        ex7_1_exact.apply_NOT({0: Fraction(1, 1)}, 4, 4)
