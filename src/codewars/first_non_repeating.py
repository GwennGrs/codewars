# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e

def first_non_repeating_letter(s):
    """Return the first letter that is not repeated in our string.

    Args:
        s (str): String to analyze.

    Returns:
        str: The first non repeating letter or an empty string if there is none.
    """
    dic = {}
    for i, letter in enumerate(s.lower()):
        if letter in dic.keys():
            dic[letter].append(i)
        else : 
            dic[letter] = [i]
        print(dic[letter])
    for letter in dic.keys():
        if len(dic[letter]) == 1:
            return s[dic[letter][0]]
    return ""