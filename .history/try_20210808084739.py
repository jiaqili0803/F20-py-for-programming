def count_values(the_dict):
    count = {}
    for i in the_dict.values():
        count[i] = count.get(i,0) + 1
    return count


values = {'a':8, 'b':2, 'c':7, 
          'd':14, 'e':17, 'f':8, 
          'g':7, 'h':8, 'i':14}
value2 = {}
value3 = {'a':'apple', 'b':'banana', 'c':'apple'}


print(count_values(values))
#print(count_values(value2))
#print(count_values(value3))
        
