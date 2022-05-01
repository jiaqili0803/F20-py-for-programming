#用 starwars API 创建角色class
class Character:

    def __init__(self, nm, sp):
        self.name = nm
        self.species = sp

    def info(self)
        return self.name + " is a " + self.species

luke = Character("Luke Skywalker", "Human")
c3po = Character("C3PO", "Droid")

print(luke.info())
print(c3po.info())








