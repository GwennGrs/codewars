# https://www.codewars.com/kata/52597aa56021e91c93000cb0

def move_zeros(lst):
    """Moves all the zeros at the end of the list preserving the order of the other elements.

    Args:
        lst (list): List of integers

    Returns:
        list: List with all the zeros at the end.
    """
    nl = []
    lz = []
    for n in lst:
        if n == 0:
            lz.append(0)
        else :
            nl.append(n)
    return nl+lz