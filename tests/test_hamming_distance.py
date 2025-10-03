from codewars.hamming_distance import hamming
import pytest

def hamming():
    assert hamming("Gwenn", "Swann") == 2
    assert hamming("karolin", "kathrin") == 3
    assert hamming("1011101", "1001001") == 2
    assert hamming("kayak", "kayak") == 0
    assert hamming("", "") == 0

def test_error():
    with pytest.raises(TypeError):
        hamming(0)
        hamming(12212121)

