from codewars.zero_to_end import move_zeros
import pytest

def test_move_zeros():
    assert move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
    assert move_zeros([0, 1, None, 2, False, 1, 0]) == [1, None, 2, 1, 0, False, 0]
    assert move_zeros(['a', 'b']) == ['a', 'b']
    assert move_zeros([0, 'a', 'b', 0]) == ['a', 'b', 0, 0]
    assert move_zeros([0, 0]) == [0, 0]
    assert move_zeros([1,2,3]) == [1,2,3]
    assert move_zeros([]) == []
    assert move_zeros([False]) == [False]
    assert move_zeros([0]) == [0]
    assert move_zeros([None]) == [None]
    assert move_zeros([None, False, True]) == [None, True, False]
    assert move_zeros([None, False, True, 0]) == [None, True, False, 0]

def test_input_types():
    with pytest.raises(TypeError):
        move_zeros(100)