def values_of_b(dict_list):
    """
    Parameters
    ----------
    dict_list
        a list of dictionaries

    Returns
    -------
        a list of all of the values associated with
        the key 'b' in any of the provided dictionaries
    """

    b_list = []
    for i in dict_list:
        b_list.append(i['b'])
    return b_list
        




list_of_dicts = [{'a':1,'b':2,"d":11}, 
                 {'a':4,'b':5,"d":12}, 
                 {'a':7,'b':8,"d":11}]

print(values_of_b(list_of_dicts))
