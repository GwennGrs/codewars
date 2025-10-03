from codewars.order_weight import order_weight
import pytest

def test_order_weight():
    assert order_weight("12 01 12") == "01 12 12"
    assert order_weight("201") == "201"
    assert order_weight("56 65 74 100 99 68 86 180 90") == "100 180 90 56 65 74 68 86 99"

def test_wrong_inputs():
    with pytest.raises(AttributeError):
        assert order_weight(0)