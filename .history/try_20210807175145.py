
class Animal:
  legs = 4

  def __init__(self, nm):
    self.name = nm

  def get_num_legs(self):
    return self.legs
  
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

d1 = Dog('Fido',  'Dachsund')
c1 = Cow('Bessie')
b1 = Bird('Polly')
s1 = Spider('Charlotte')

animals = [d1, c1, b1, s1]
for a in animals:
  print (a.name, 'has', a.get_num_legs(), 'legs and', a.greeting())


class Labrador(Dog):
def __init__(self, nm):
    super().__init__(nm, 'Labrador')

def greeting(self):
    return super().greeting() + " enthusiastically"
