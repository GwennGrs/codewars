from codewars.sum_multiple_3_5  import sum_multiples_3_5
import pytest

def test_sum_multiples_3_5():
    assert sum_multiples_3_5(10) == 23
    assert sum_multiples_3_5(0) == 0
    assert sum_multiples_3_5(-5) == 0
    assert sum_multiples_3_5(16) == 60 
    assert sum_multiples_3_5(1921) == 861120

def test_input_types():
    with pytest.raises(TypeError):
        sum_multiples_3_5("100")
    with pytest.raises(TypeError):
        sum_multiples_3_5(10.5)