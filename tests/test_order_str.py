from codewars.order_str import order
import pytest

def test_order_str():
    assert order("s5uis pens2e j4e 3donc j1e ") == "j1e pens2e 3donc j4e s5uis"
    assert order("ch2eval le1 T4roie d3e") == "le1 ch2eval d3e T4roie"
    assert order("autre4s c'2est L'en1fer le3s") == "L'en1fer c'2est le3s autre4s"