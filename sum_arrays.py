# https://www.codewars.com/kata/53dc54212259ed3d4f00071c

def sum_array(a):
    """Sums the elements of an array.

    Args:
        a (array): An array of numbers. The numbrs can be negative or non-integer.

    Returns:
        float: The sum of the elements in the array. If the array does not contain any elements, return 0.
    """
    if len(a) == 0 :
        return 0
    result = 0
    for i in a :
        result += i
    return result