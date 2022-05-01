'''
Objects
    Almost Everything in Python is an object
    library 里面都是objects
    function返回的也是object
'''  
import datetime #package name

date_now = datetime.datetime.now() 
#date_now is an object 
#datetime is a type,(but happens to be same as package name) 
# now() is a function

print(date_now.year)
print(date_now.month)
print(date_now.day)

print(date_now)
date_now = date_now.replace(2019, day=8) # first param is year
print(date_now)
'''
Class
    ‘append’ is a method on the list class
    ‘find’ is a method on the str class
'''