##加入subclass Human
import requests

class Character:   #superclass
    def __init__(self, nm='', sp='', character_data=None): 
        #character_data=None 则是手动输入的两例情况；else是从API抓下来的info输入进class的情况
        if (character_data is None):
            self.name = nm
            self.species = sp
        else:
            self.name = character_data['name']
            
            if character_data["species"] == []:
                    self.species = "Unknown"
            else:
                if (character_data["species"][0]
                        == "https://swapi.dev/api/species/1/"):
                    self.species = "Human"
                elif (character_data["species"][0]
                        == "https://swapi.dev/api/species/2/"):
                    self.species = "Droid"
                else:
                    self.species = "Unknown"
                
    def info(self):
        return self.name + " is a " + self.species


class Human(Character):  #subclass
    
    def __init__(self, nm='', hc='Unkonwn', character_data=None): 
        #不要sp，加hc='Unkonwn'
        super().__init__(nm, 'Human', character_data=character_data) #继承的时候要说明sp是固定'Human'
        if (character_data is None): #手动的
            self.hair_color = hc
        else: #从api导入
            self.hair_color = character_data['hair_color']


    def info(self):
        return super().info() + " who has " + self.hair_color + " hair" 
        # 继承super().info() ，改动一点


#### Testing the Character class
luke = Human("Luke Skywalker (Test)", "sandy")
c3po = Character("C3PO (Test)", "Droid")
print(luke.info())
print(c3po.info())

#### Fetching Character data from swapi.co
BASE_URL = "https://swapi.dev/api/people" 

resp = requests.get(BASE_URL)
results_object = resp.json() 
people_list = results_object["results"]

characters = []
for p in people_list:  #两种情况：属于sub子类 或者只属于大类Character
    if p["species"] == "https://swapi.dev/api/species/1/":
        characters.append(Human(character_data=p)) 
        #第一种，则append进 Human子类的return
    else:   
        characters.append(Character(character_data=p))
        #第二种，则append进 Character大类的return

for c in characters:
    print(c.info())  #打印出来


