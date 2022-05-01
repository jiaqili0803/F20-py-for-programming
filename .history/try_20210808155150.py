##用 starwars API 创建角色class

#先手动创建两个instance试一下对不对
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

#request 数据from API
import requests

BASE_URL = "https://swapi.dev/api/people" 
resp = requests.get(BASE_URL)
results_object = resp.json() # same as json.loads(resp.text)
print(results_object)

people_list = results_object["results"] #把关于人物信息的"results"列表提取
print(people_list[0]) # print the first person in the list


#name and eye color of the fourth person
print(people_list[3]['name']&['eye_color']) 
exit()








