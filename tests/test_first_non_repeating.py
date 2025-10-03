from codewars.first_non_repeating import first_non_repeating_letter
import pytest

def test_first_non_repeating_letter():
    assert first_non_repeating_letter("sTreSS") == "T"
    assert first_non_repeating_letter("nnaeaeaeaeasqdqsdzdadadsuqdzenn") == "u"
    assert first_non_repeating_letter("Ta bete te bat") == ""

def test_error():
    with pytest.raises(AttributeError):
        first_non_repeating_letter(0)