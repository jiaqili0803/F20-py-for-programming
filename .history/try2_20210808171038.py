import requests

class Character:


    def __init__(self, nm='', sp='', character_data=None):
        if (character_data is None):
            self.name = nm
            self.species = sp
        else:
            self.name = character_data['name']
            if (character_data["species"][0] 
                    == "https://swapi.co/api/species/1/"):
                self.species = "Human"
            elif (character_data["species"][0]
                    == "https://swapi.co/api/species/2/"):
                self.species = "Droid"
            else:
                self.species = "Unknown"
                

    def info(self):
        return self.name + " is a " + self.species


class Human(Character):


    def __init__(self, nm='', hc='Unkonwn', character_data=None):
        super().__init__(nm, 'Human', character_data=character_data)
        if (character_data is None):
            self.hair_color = hc
        else:
            self.hair_color = character_data['hair_color']


    def info(self):
        return super().info() + " who has " + self.hair_color + " hair"



#### Testing the Character class
luke = Human("Luke Skywalker (Test)", "sandy")
c3po = Character("C3PO (Test)", "Droid")

print(luke.info())
print(c3po.info())


#### Fetching Character data from swapi.co
BASE_URL = "http://swapi.co/api/people" # only interested in people

resp = requests.get(BASE_URL)
results_object = resp.json() 
people_list = results_object["results"]
characters = []
for p in people_list:
    if p["species"][0] == "https://swapi.co/api/species/1/":
        characters.append(Human(character_data=p))
    else:   
        characters.append(Character(character_data=p))

for c in characters:
    print(c.info())


