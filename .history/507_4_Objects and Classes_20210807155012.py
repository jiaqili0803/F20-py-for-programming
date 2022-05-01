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
# now() is a function on the class
print(date_now.year)
print(date_now.month)
print(date_now.day)
#year, month, and day are attributes (aka variables) of datetime type(aka class)
#object.year, 可以调出

print(date_now)
date_now = date_now.replace(2019, day=8) # first param is year
# replace() is a method/function on the class
print(date_now)



'''
Class
    Def:
    A class是a type of objects的规范，它保证所有objects都具有相同的结构。
    具有same attributes和same methods。
    使得在其他地方使用这些objects变得更加容易。
    使您的代码更具可读性、可重用性和可维护性，将逻辑相关的东西收集在一起
    
    比喻来说：
    您可以将class视为一种生产objects的工厂。除了生成objects并声明它们做什么之外，class本身不会在您的代码中执行任何操作。obejcts在进行实际工作。
    
    举例：
    ‘append’ is a method/funct on the list class
    ‘find’ is a method/funct on the str class
'''

# BEGIN CLASS DEFINITION
class Dog: #大写，Longer names use CamelCase

  def __init__(self, nm, br):
    self.name = nm
    self.breed = br
# END CLASS DEFINITION

d1 = Dog('Fido', 'German Shepherd')  #instantiate实例化两个objects
d2 = Dog('Rufus', 'Lhasa Apso')
print (d1.name, 'is a', d1.breed)
print (d2.name, 'is a', d2.breed)