# https://www.codewars.com/kata/5410c0e6a0e736cf5b000e69


def hamming(a,b):
    """Compute the Hamming distance between two strings.

    Args:
        a (str): String of length n.
        b (str): String of length n.

    Returns:
        int: The number of positions where the characters are different.
    """
    cpt = 0
    for i in range(len(a)):
        if(a[i] != b[i]):
            cpt = cpt + 1
    return cpt