'''
Class 和 Subclass：
    1. class括号里写了superclass，会自动继承所有（除了override的部分）
    
    2. 想继承的部分 需要做些改动：e.g. super().__init__(nm)；super().greeting()
    
    3. 执行、实例化的时候，自动优先subclass，找不到的再superclass
'''



class Animal:
    legs = 4 #class attributes
    def __init__(self, nm):
        self.name = nm

    def get_num_legs(self):
        return self.legs  #?? 如果这里写Animal.legs 那就不会根据instance不同而变化了；这里意思是return self.legs，然后就去所在instance找legs return

    def greeting(self):
        return "cowers"

class Dog(Animal): #the subclass of Animal, Animal is superclass

    def __init__(self, nm, br): #parm多一个br
        super().__init__(nm) #call the superclass的__init__保持不变
        self.breed = br #多加一个br

    def greeting(self):
        return "wags"

class Cow(Animal): #the subclass of Animal
    pass

class Bird(Animal): #the subclass of Animal
    legs = 2

class Spider(Animal):  #the subclass of Animal
    legs = 8
  
class Labrador(Dog): #the subclass of Dog of Animal
    def __init__(self, nm): #parm少了一个br，因为不需要，所以不继承
        super().__init__(nm, 'Labrador') #?? 'Labrador'是br，是固定的，call superclass的时候需要符合他的parms，写出来

    def greeting(self):
        return super().greeting() + " enthusiastically" #call superclass 的 greeting()；还可以继续DIY

#实例化
d1 = Dog('Fido',  'Dachsund') 
c1 = Cow('Bessie')
b1 = Bird('Polly')
s1 = Spider('Charlotte')

l1 = Labrador('ella')

animals = [d1, c1, b1, s1, l1] #批量loop
for a in animals: 
    print (a.name, 'has', a.get_num_legs(), 'legs and', a.greeting())

