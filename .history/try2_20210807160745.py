# BEGIN CLASS DEFINITION
class Dog: #大写，Longer names use CamelCase
           #class body is indented
    def __init__(self, nm, br): #constructor method/function，call class时候必用到；self必须是第一个parameter，self refers to the current object；所以only pass two parameters（nm, br）
        self.name = nm  #attribute 
        self.breed = br  #attribute 

    def describe(self): #another method/function
        return self.name + ' is a ' + self.breed  #可以用constructor里面的attributes

# END CLASS DEFINITION

d1 = Dog('Fido', 'German Shepherd')  #instantiate实例化两个objects；两个参数带入（nm, br），d1就可用了
d2 = Dog('Rufus', 'Lhasa Apso')
print (d1.name, 'is a', d1.breed) #可以调用d1.name，这些attributes
print (d2.name, 'is a', d2.breed)


d3 = Dog('Benny', 'Mutt') #实例化
print(d3.describe()) #调用function
d3.breed = 'Labradoodle' #
print(d3.describe())