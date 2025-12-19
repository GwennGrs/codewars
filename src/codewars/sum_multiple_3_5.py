"""
https://www.codewars.com/kata/514b92a657cdc65150000006
"""

def sum_multiples_3_5(n):
    """Sums all the multiplies of 3 or 5 below n

    Args:
        n (int): The upper limit. If n is negative, return 0.

    Returns:
        int: Sums of all our multiples below n.
    """
    total = 0
    if n < 0:
        return total
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total
