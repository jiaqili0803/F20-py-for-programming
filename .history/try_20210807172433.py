
class Animal:
    def __init__(self, nm):
        self.name = nm
        self.legs = 4

    def get_num_legs(self):
        return self.legs

class Bird(Animal):
    def __init__(self, nm):
        self.name = nm
        self.legs = 2

class Spider(Animal):
    def __init__(self, nm):
        self.name = nm
        self.legs = 8

a1 = Animal('Annie')
b1 = Bird('Polly')
s1 = Spider('Charlotte')
animals = [a1, b1, s1]

for a in animals:
    print(a.name, 'has', a.get_num_legs(), 'legs')
