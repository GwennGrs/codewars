from codewars.sum_arrays import sum_array
import pytest

def test_sum_array():
    assert sum_array([1, 2, 3]) == 6
    assert sum_array([-1, -2, -3]) == -6
    assert sum_array([]) == 0

def test_sum_array_float():
    assert sum_array([1.5, 2.5, 3.0]) == 7.0
    assert sum_array([-1.5, -2.5, -3.0]) == -7.0

def test_input_types():
    with pytest.raises(TypeError):
        sum_array([1, '2', 3])
