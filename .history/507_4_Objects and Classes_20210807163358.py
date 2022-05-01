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
           #class body is indented
    def __init__(self, nm, br): #constructor method/function，call class时候必用到；self必须是第一个parameter，self refers to the current object；所以only pass two parameters（nm, br）
        self.name = nm  #attribute 
        self.breed = br  #attribute 

    def describe(self): #def another method/function
        return self.name + ' is a ' + self.breed  #可以用constructor里面的attributes
# END CLASS DEFINITION

d1 = Dog('Fido', 'German Shepherd')  #instantiate实例化两个objects；两个参数带入（nm, br），d1就可用了
d2 = Dog('Rufus', 'Lhasa Apso')
print (d1.name, 'is a', d1.breed) #可以调用d1.name，这些attributes
print (d2.name, 'is a', d2.breed)

d3 = Dog('Benny', 'Mutt') #实例化
print(d3.describe()) #调用function
d3.breed = 'Labradoodle' #改了d3这个object的 attribute的输入
print(d3.describe()) #print结果是改成功的，但是其他objects d1,d2都没变



'''
Class Attributes vs Instance Attributes的 不同和联系
'''

class Dog:

    large_dogs = ['German Shepherd', 'Golden Retriever',
                  'Rottweiler', 'Collie',
                  'Mastiff', 'Great Dane']
    small_dogs = ['Lhasa Apso', 'Yorkshire Terrier',
                  'Beagle', 'Dachshund', 'Shih Tzu']
    
    #class attributes：large_dogs，small_dogs；他们belong to the entire class；not attached to self、instance
    #class attributes 对不同instance是不变的一样的；比如all 3 dogs have same values for large_dogs and small_dogs
    
    #instance attributes：name and breed；对不同instance有不同value；比如不同dog有different values for name and breed
    
    #instance也可以访问class attributes
    
    
    def __init__(self, nm, br):
        self.name = nm
        self.breed = br


    def speak(self):
        if self.breed in Dog.large_dogs:
            print('woof')
        elif self.breed in Dog.small_dogs:
            print('yip')
        else:
            print('rrrrr')


d1 = Dog('Fido', 'German Shepherd')
d2 = Dog('Rufus', 'Lhasa Apso')
d3 = Dog('Fred', 'Mutt')

d1.speak()
d2.speak()
d3.speak()