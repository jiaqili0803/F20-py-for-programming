import requests


class Character:
    
    def __init__(self, nm='', sp='', character_data=None): 
        #character_data=None 则是手动输入的两例情况；else是从API抓下来的info输入进class的情况
        if (character_data is None):
            self.name = nm
            self.species = sp
        else:
            self.name = character_data['name']
            if character_data["species"] == None:
                    self.species = "Unknown"
            else:
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


#### Testing the Character class 用两个手动的
luke = Character("Luke Skywalker (Test)", "Human")
c3po = Character("C3PO (Test)", "Droid")
print(luke.info())
print(c3po.info())


#### Fetching Character data from swapi.co
BASE_URL = "https://swapi.dev/api/people" 

resp = requests.get(BASE_URL)
results_object = resp.json() 
people_list = results_object["results"]

characters = []
for p in people_list: #API中每个people的data，用Character class，append他们的info到characters = []里面；每个p用loop分别输入character_data这个参数里
    characters.append(Character(character_data=p))

for c in characters:
    print(c.info()) #再把每个打出来


