list_of_dicts = [{'a':1,'b':2,"d":11}, 
                 {'a':4,'b':5,"d":12}, 
                 {'a':7,'b':8,"d":11}]

def values_of_d(dict_list):
    d_list = []
    for i in dict_list:
        d_list.append(i['d'])
    return d_list
        
    


print(values_of_d(list_of_dicts))
        
