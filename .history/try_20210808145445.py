

class Pet:

    def __init__(self, nm, words=["woof", "arf", "yip"]):
        self.name = nm
        self.words = words

    def speak(self):
        my_words = ''
        for w in self.words:
            my_words += w + " "
        return "I can say " + my_words

    def teach(self, new_word):
        self.words.append(new_word)

fido = Pet("fido")
rufus = Pet("rufus")

print(fido.speak())
print(rufus.speak())






