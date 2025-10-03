from codewars.MSE import mean_square_error
import pytest

def test_mse():
    assert mean_square_error([1,2,3], [4,5,6]) == 9
    assert mean_square_error([10,20,10,20], [10,25,10,25]) ==  12.5
    assert mean_square_error([0,0,0,0,0], [1,1,1,1,1]) == 1

def test_mse_empty_lists():
    with pytest.raises(ZeroDivisionError):
        mean_square_error([], [])
        mean_square_error([1,2,3], [])
        mean_square_error([], [1,2,3])