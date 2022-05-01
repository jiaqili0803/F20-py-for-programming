def num_long_words(sentence):
    """
    Parameters
    ----------
    sentence
        a string

    Returns
    -------
        the number of words within that string whose
        length is greater than 5
    """
    count = 0
    for i in sentence.split():
        if len(i) > 7:
            count = count + 1
    return count




s = "this is my superduper short sentence"

print(num_long_words(s)) # prints 2

