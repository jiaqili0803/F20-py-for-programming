'''
Objects
    Def: Objects are (potentially) complex data structures that collect related attributes and methods into coherent, uniform bundles.
    
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
    可以自己define一个class

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
    def __init__(self, nm, br): #constructor method/function，规定了objects都有一样的结构(self, nm, br, a)
    #call class时候必用到；
    #self必须是第一个parameter，self refers to the current object；
    #所以only pass two parameters（nm, br）
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

    large_dogs = ['German Shepherd', 'Golden Retriever', #class attributes
                  'Rottweiler', 'Collie',
                  'Mastiff', 'Great Dane']
    small_dogs = ['Lhasa Apso', 'Yorkshire Terrier',
                  'Beagle', 'Dachshund', 'Shih Tzu']
    
    #class attributes：large_dogs，small_dogs；
    #   他们belong to the entire class，可以放在method外面；
    #   not attached to self、instance
    #   对不同instance是不变的一样的；比如all 3 dogs have same values for           large_dogs and small_dogs
    #   use class（也可以用object/instance） name to call: Dog.large_dogs、d1.large_dogs（这样也可以）
    #   can be used to declare constants
    
    #instance attributes：name and breed；
    #   must attached to self、instance
    #   对不同instance有不同value；比如不同dog有different values for name and breed
    #   use self、instance to call: self.breed
    
    #instance也可以访问class attributes
    
    
    def __init__(self, nm, br):
        self.name = nm
        self.breed = br


    def speak(self):
        if self.breed in Dog.large_dogs: #call class attribute
            print('woof')
        elif self.breed in Dog.small_dogs:
            print('yip')
        else:
            print('rrrrr')


d1 = Dog('Fido', 'German Shepherd') #实例化
d2 = Dog('Rufus', 'Lhasa Apso')
d3 = Dog('Fred', 'Mutt')

d1.speak()  #object/instance.method 调用method
d2.speak()
d3.speak()

#注意如果作出改动！
#object.class attribute 改动， 全局的class attribute都被改了
d1.large_dogs.append('Doberman')
print(d3.large_dogs) 
#object.instance attribute 改动， 只改动这一个instance的值
d3.breed = 'Labradoodle' #改了d3这个object的attribute的输入




'''
通过使用class，简化一类objects的使用code（有same attributes and methods）
'''

class Dog:

    large_dogs = ['German Shepherd', 'Golden Retriever',
                  'Rottweiler', 'Collie',
                  'Mastiff', 'Great Dane']
    small_dogs = ['Lhasa Apso', 'Yorkshire Terrier',
                  'Beagle', 'Dachshund', 'Shih Tzu']

    def __init__(self, nm, br, a):
        self.name = nm
        self.breed = br
        self.age = a

    def speak(self):
        if self.breed in Dog.large_dogs:
            print('woof')
        elif self.breed in Dog.small_dogs:
            print('yip')
        else:
            print('rrrrr')
            
    def print_dog_years(self):
        '''prints a dog's name and age in dog years
        dog years = actual years * 7
        
        Parameters
        ----------
        dog : Dog
            The dog to print
            
        Returns
        -------
        name: name of the dog
        age: age in dog years = actual years * 7
        '''
        print(self.name)
        print(self.age*7)

kennel = [          #这一list结构相同的，直接用class一起实例化出来
    Dog('Fido', 'German Shepherd',4),
    Dog('Rufus', 'Lhasa Apso',7),
    Dog('Fred', 'Mutt',11)
    ]

for dog in kennel:  #再通过loop，得到每一个object/instance的speak（）function调用结果
    dog.speak()      #统一方式操作复杂objects，太棒了！
    dog.print_dog_years() 

    print_dog_years(dog) #error: 如果不加dog.这个object/instance，相当于没调用class，也就不认识print_dog_years这个class内的函数
    
    
    
    
'''
Class Docstrings 也需要做docu！（着重说明instance attributes）   
'''
#比如
class Dog:
    '''A dog that speaks!
    
    Attributes
    ----------
    name : string
        The dog's name
    breed : string
        The dog's breed, as defined by https://www.akc.org/dog-breeds/
    '''