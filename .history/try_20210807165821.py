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


kennel = [      
    Dog('Fido', 'German Shepherd', 4),    
    Dog('Rufus', 'Lhasa Apso', 7),
    Dog('Fred', 'Mutt', 11)
    ]

for dog in kennel:
    dog.print_dog_years()  #调用每一个 Dog('Fido', 'German Shepherd', 4)，的class内函数print_dog_years()
    
for dog in kennel:
    print_dog_years(dog) #如果不加dog.，相当于没调用class，也就不认识print_dog_years这个class内的函数
    




