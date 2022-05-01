

class Pet:

    def __init__(self, nm, words=["woof", "arf", "yip"]): #default parameter is global variable
        self.name = nm
        self.words = words

    def speak(self):
        my_words = ''
        for w in self.words:
            my_words += w + " "
        return "I can say " + my_words

    def teach(self, new_word):
        self.words.append(new_word) #modified that global variable;所有使用那个default parametr的instance都会被影响

fido = Pet("fido")
rufus = Pet("rufus")
polly = Pet("polly", ["cracker", "pirate", "rrrr"])

print(fido.speak())
fido.teach('ella')
print(rufus.speak())
print(fido.speak())

print(polly.speak())






