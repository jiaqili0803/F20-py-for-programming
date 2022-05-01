'''
Refactor of starwars3.py to avoid hardcoding of species IDs
willy nilly throughout the code. Instead the speciesID-to-name 
mappings are managed by the function species_name.
'''

import requests

BASE_URL = "https://swapi.dev/api/people" 

SPECIES = {
    'https://swapi.dev/api/species/1/': 'Human',
    'https://swapi.dev/api/species/2/': 'Droid'
    }


def species_name(species_id):

    if species_id in SPECIES:
        return SPECIES[species_id]
    else:
        return 'Unknown'


class Character:


    def __init__(self, nm='', sp='', character_data=None):
        if (character_data is None):
            self.name = nm
            self.species = sp
        else:
            self.name = character_data['name']
            self.species = species_name(character_data["species"])


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

resp = requests.get(BASE_URL)
results_object = resp.json() 
people_list = results_object["results"]

characters = []
for p in people_list:
    if species_name(p["species"]) == "Human":
        characters.append(Human(character_data=p))
    else:   
        characters.append(Character(character_data=p))

for c in characters:
    print(c.info())









