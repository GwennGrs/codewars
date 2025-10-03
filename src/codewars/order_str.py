# https://www.codewars.com/kata/55c45be3b2079eccff00010f

def order(sentence):
    """Order the words based on the number they contain.

    Args:
        sentence (str): A sequence of words containing a single number each. Numbers goes from 1 to 9. The sentence can be empty.

    Returns:
        str: The sequence of the words ordered. An empty string if the input is an empty string.
    """
    sentence2 = sentence.split()
    rslt = ""
    for i in range(len(sentence2)):
        for j in sentence2:
            if(str(i+1) in j):
                rslt = rslt + j + " "
    return rslt[:-1]