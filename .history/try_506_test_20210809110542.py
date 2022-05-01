#13
a_list = [1,2]
other_list = [5,6,7,8]

a_list += [3,4]

final_list = a_list[2:]+other_list[:2]
print(final_list)   #3456
