#request 数据from API
import requests

BASE_URL = "https://swapi.dev/api/people" 
resp = requests.get(BASE_URL)
results_object = resp.json() # same as json.loads(resp.text)

people_list = results_object["results"] #把关于人物信息的"results"列表提取
#print(people_list[0]) # print the first person in the list

#name and eye color of the fourth person
print(people_list[3]['name']&['eye_color']) 
exit()

