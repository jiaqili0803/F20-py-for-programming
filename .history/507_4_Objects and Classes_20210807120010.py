'''
Objects
    Almost Everything in Python is an object
    library里面都是objects
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
    DEF:
    A class is a specification for a type of object that guarantees that all objects will have the same structure. All objects of a particular class will have the same attributes and the same methods, which makes it much easier to write code that uses those objects elsewhere in your code. 
    
    比喻：
    You can think of a class as a kind of factory that produces objects. The class itself doesn’t do anything in your code other than produce objects and declare what they do. The objects are what actually do the work.
    
    ‘append’ is a method on the list class
    ‘find’ is a method on the str class
'''
