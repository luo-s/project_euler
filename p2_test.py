from p2_even_fibo_numbers import fiboEvenSum
import pytest

@pytest.mark.parametrize("test_input,expected",
    [("fiboEvenSum(10)", 10), 
     ("fiboEvenSum(60)", 44), 
     ("fiboEvenSum(1000)", 798), 
     ("fiboEvenSum(100000)", 60696), 
     ("fiboEvenSum(4000000)", 4613732)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected

