#https://www.codewars.com/kata/51edd51599a189fe7f000015

def mean_square_error(array_a, array_b):
    """Compute the mean square error between two arrays.

    Args:
        array_a (array): array of int
        array_b (array): array of int

    Returns:
        int: the error between the two arrays.
    """
    tmp_l = []
    for n1, n2 in zip(array_a, array_b):
        tmp_l.append((max(n1-n2, n2-n1))**2)
    return sum(tmp_l)/len(tmp_l)