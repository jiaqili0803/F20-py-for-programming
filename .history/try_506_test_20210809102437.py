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
    words = ''
    for word in str_list:
        len(words) += len(word)
    return len(words)








print((total_len(['hi', 'heisman']))) #9
print(total_len(['yo', 'hi', ''])) #4
