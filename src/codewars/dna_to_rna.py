#https://www.codewars.com/kata/5556282156230d0e5e000089

def dna_to_rna(dna):
    """Converts a DNA sequence to its RNA complement. 
    Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems.
    It is composed of four bases: G, C, T(thymine), and A.
    In RNA uracil (U) replaces thymine (T).

    Args:
        dna (str): A string representing a DNA sequence. The array can be empty.

    Returns:
        str: The RNA complement of the DNA sequence. Our sequence with all the T replaced by U.
    """
    rsl = ""
    for lettre in dna:
        if lettre == "T":
            rsl += "U"
        else : 
            rsl += lettre
    return rsl