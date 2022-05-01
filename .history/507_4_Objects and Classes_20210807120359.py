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
    Def:
    A class是a type of objects的规范，它保证所有objects都具有相同的结构。All objects of a particular class将具有same attributes和same methods。使得在其他地方使用这些objects变得更加容易。
    
    比喻来说：
    您可以将class视为一种生产objects的工厂。除了生成objects并声明它们做什么之外，class本身不会在您的代码中执行任何操作。obejcts在进行实际工作。
    
    ‘append’ is a method on the list class
    ‘find’ is a method on the str class
'''
