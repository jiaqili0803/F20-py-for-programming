'''
Objects
    Almost Everything in Python is an object
    library 里面都是objects
    function返回的也是object
'''
print(type(date_now))  #用type()来判断object的类型
<class 'datetime.datetime'>

#eg
import datetime #package name
date_now = datetime.datetime.now() 
#date_now is an object 
#datetime is a type(aka class),(but happens to be same as package name) 
# now() is a function
print(date_now.year)
print(date_now.month)
print(date_now.day)
#year, month, and day are attributes (aka variables) of datetime type(aka class)
print(date_now)
date_now = date_now.replace(2019, day=8) # first param is year
# replace() is a method on the class
print(date_now)



'''
Class
    ‘append’ is a method on the list class
    ‘find’ is a method on the str class
'''
