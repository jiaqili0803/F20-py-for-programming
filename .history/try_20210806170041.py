
def change_it(the_list):
    the_list.append('d')
g_list = ['a', 'b', 'c']
change_it(g_list)
print(g_list) # prints "['a', 'b', 'c', 'd']"
