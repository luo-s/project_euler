from p14_longest_collatz_seq import longest_collatz_sequence
import pytest

@pytest.mark.parametrize("test_input,expected", 
    [("longest_collatz_sequence(14)", 9), 
     ("longest_collatz_sequence(5847)", 3711), 
     ("longest_collatz_sequence(46500)", 35655), 
     ("longest_collatz_sequence(54512)", 52527), 
     ("longest_collatz_sequence(100000)", 77031), 
     ("longest_collatz_sequence(1000000)", 837799)])

def test_eval(test_input, expected):
    assert eval(test_input) == expected