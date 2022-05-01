def create_address_book(list_of_entries):
    """
    Parameters
    ----------
    list_of_entries
        a list of tuples, where the first item is a first name,
        the second item is a last name, and the third item is an
        address for that person

    Returns
    -------
        a dictionary where the keys are full names
        (first name then last name) and the values
        are addresses
    """
    dict ={}
    for tuple in list_of_entries:
        key = tuple[0] + ' ' + tuple[1] 
        value = tuple[2]
        dict[key] = value
            
    return dict
    
create_address_book([('Jay', 'Gatsby', '20 W. Egg Avenue'),
                     ('Daisy', 'Buchanan', '55 E. Egg Lane'),
                     ('Nick', 'Carraway', '18 W. Egg Avenue'),
                     ('Myrtle', 'Wilson', '10 Main St')])
