def total_len(str_list):
    """
    Parameters
    ----------
    strings
        a list of strings

    Returns
    -------
        the total length of every string in
        that list added together
    """
    words_len = 0
    for word in str_list:
        print(len(word))
        words_len += len(word)
    return words_len








print((total_len(['hi', 'heisman']))) #9
print(total_len(['yo', 'hi', ''])) #4
