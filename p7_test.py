from p7_nth_prime_num import nth_prime
import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("nth_prime(6)", 13), 
     ("nth_prime(10)", 29), 
     ("nth_prime(100)", 541), 
     ("nth_prime(1000)", 7919), 
     ("nth_prime(10001)", 104743)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected