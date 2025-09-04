from src.math_operation import add, sub

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    

def test_sub():
    assert(5, 3) == 2
    assert(4, 3) == 1