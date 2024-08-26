from p3_largest_prime_factor import largest_prime_factor
import pytest

@pytest.mark.parametrize("test_input,expected",[("largest_prime_factor(2)", 2), ("largest_prime_factor(3)", 3), ("largest_prime_factor(5)", 5), ("largest_prime_factor(7)", 7), ("largest_prime_factor(32)", 2), ("largest_prime_factor(13195)", 29), ("largest_prime_factor(600851475143)", 6857)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected

