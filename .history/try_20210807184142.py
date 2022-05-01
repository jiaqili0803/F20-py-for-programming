
class Animal:
  legs = 4

  def __init__(self, nm):
    self.name = nm

  def get_num_legs(self):
    return self.legs     #?? 如果这里写Animal.legs 那就不会根据instance不同而变化了
  
  def greeting(self):
    return "cowers"

class Dog(Animal):

  def __init__(self, nm, br):
    super().__init__(nm)
    self.breed = br

  def greeting(self):
    return "wags"

class Cow(Animal):
  pass

class Bird(Animal):
  legs = 2

class Spider(Animal): 
  legs = 8
  
class Labrador(Dog):
    def __init__(self, nm):
        super().__init__(nm, 'Labrador') #?? 'Labrador'是br，是固定的

    def greeting(self):
        return super().greeting() + " enthusiastically"

d1 = Dog('Fido',  'Dachsund')
c1 = Cow('Bessie')
b1 = Bird('Polly')
s1 = Spider('Charlotte')

l1 = Labrador('ella')

animals = [d1, c1, b1, s1, l1]
for a in animals:
  print (a.name, 'has', a.get_num_legs(), 'legs and', a.greeting())



a = Labrador("Midnight")
print(a.greeting())
