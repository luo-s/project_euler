from p12_divisor_count import divisibleTriangleNumber
import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("divisibleTriangleNumber(5)", 28), 
     ("divisibleTriangleNumber(23)", 630), 
     ("divisibleTriangleNumber(167)", 1385280), 
     ("divisibleTriangleNumber(374)", 17907120), 
     ("divisibleTriangleNumber(500)", 76576500)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected

