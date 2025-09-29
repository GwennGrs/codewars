# https://www.codewars.com/kata/55c6126177c9441a570000cc

def order_weight(strng):
    """Weight sorted by the sum of its digits.
    If two numbers have the same weight we class them as if they were strings (alphabetical ordering).

    Args:
        strng (str): String of weights(number)

    Returns:
        string: Weights ordered
    """
    result = []
    a = list(sorted(strng.split(), key = (lambda x : (sum(map(int, x)), x))))
    
    result = ""
    for lettre in a:
        result = result + lettre + " "
    return result[:-1]