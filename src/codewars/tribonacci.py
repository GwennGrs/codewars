# https://www.codewars.com/kata/556deca17c58da83c00002db

def tribonacci(signature, n):
    """Generates a Tribonacci sequence. Starting with the given signature, each number is the sum of the previous three.

    Args:
        signature (array of int): The three initial numbers non-negative.
        n (int): The length of the sequence to generate

    Returns:
        array: Tribonacci sequence of length n starting with signature
    """
    for i in range(n-3):
        signature.append(signature[-1] + signature[-2] + signature[-3])
    return signature[0:n]