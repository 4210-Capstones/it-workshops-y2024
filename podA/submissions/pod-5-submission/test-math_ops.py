# test math_ops.py

import pytest
from math_ops import add, subtract

def test_add():
    # Test addition
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    # Test subtraction 
    assert subtract(10, 5) == 5
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0
