from p10_prime_sums import primeSum
import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("primeSum(17)", 41), 
     ("primeSum(2001)", 277050),
     ("primeSum(140759)", 873608362),
     ("primeSum(2000000)", 142913828922)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected

