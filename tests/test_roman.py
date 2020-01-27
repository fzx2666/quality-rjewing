import os, sys
print(__file__)
currentdir = os.path.dirname(__file__)
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pytest
from roman import to_roman

def test_roman_in_range():
    assert to_roman(1) == 'I'
    assert to_roman(3999) == 'MMMCMXCIX'
    assert to_roman(123) == 'CXXIII'
    assert to_roman(4) == 'IV'

def test_roman_out_of_range():
    with pytest.raises(AssertionError):
        to_roman(0)
    with pytest.raises(AssertionError):
        to_roman(4000)
    with pytest.raises(AssertionError):
        to_roman(-100)

def test_roman_wrong_input():
    with pytest.raises(AssertionError):
        to_roman('123')
    with pytest.raises(AssertionError):
        to_roman(5.0)
    with pytest.raises(AssertionError):
        to_roman('ABCDEF')

# def test_should_fail():
#     assert False
