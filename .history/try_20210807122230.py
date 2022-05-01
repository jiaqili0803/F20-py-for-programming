
# BEGIN CLASS DEFINITION
class Dog:

    def __init__(self, nm, br):
        self.name = nm
        self.breed = br

    def describe(self):
        return self.name + ' is a ' + self.breed

# END CLASS DEFINITION

d3 = Dog('Benny', 'Mutt')
print(d3.describe())
d3.breed = 'Labradoodle'
print(d3.describe())
