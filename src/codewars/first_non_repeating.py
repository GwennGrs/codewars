"""
# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e
"""

def first_non_repeating_letter(s):
    """Return the first letter that is not repeated in our string.

    Args:
        s (str): String to analyze.

    Returns:
        str: The first non repeating letter or an empty string if there is none.
    """
    dic = {}
    for i, letter in enumerate(s.lower()):
        if letter in dic:
            dic[letter].append(i)
        else :
            dic[letter] = [i]
    for letter, value in dic.items():
        if len(value) == 1:
            return s[value[0]]
    return ""
