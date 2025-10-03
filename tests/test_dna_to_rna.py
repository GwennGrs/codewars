from codewars.dna_to_rna import dna_to_rna
import pytest

def test_dna_to_rna():
    assert dna_to_rna("TTTT") == "UUUU"
    assert dna_to_rna("ATGC") == "AUGC"
    assert dna_to_rna("GACCGCCGCC") == "GACCGCCGCC"
    assert dna_to_rna("") == ""

def test_empty_inputs():
    with pytest.raises(TypeError):
        assert dna_to_rna(0)
