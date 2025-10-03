from codewars.tribonacci import tribonacci
import pytest

def test_tribonacci():
    assert tribonacci([1, 1, 1], 10) == [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
    assert tribonacci([0, 0, 1], 10) == [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
    assert tribonacci([0, 1, 1], 10) == [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]
    assert tribonacci([1, 2, 3], 10) == [1, 2, 3, 6, 11, 20, 37, 68, 125, 230]
    assert tribonacci([3, 2, 1], 10) == [3, 2, 1, 6, 9, 16, 31, 56, 103, 190]
    assert tribonacci([1, -1, -1], 10) == [1, -1, -1, -1, -3, -5, -9, -17, -31, -57]
    
def test_input_types():
    with pytest.raises(AttributeError):
        tribonacci("100", 10)
    with pytest.raises(IndexError):
        tribonacci([1, 2], 10)