# test math_ops2.py

import pytest
from math_ops2 import multiply, divide

def test_multiply():
    # Test multiplication
    assert multiply(4, 5) == 20
    assert multiply(-1, 5) == -5
    assert multiply(0, 5) == 0

def test_divide():
    # Test division
    assert divide(10, 2) == 5
    assert divide(-10, 2) == -5
    assert divide(5, 2) == 2.5
    
    # Test division by zero raises ValueError
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
