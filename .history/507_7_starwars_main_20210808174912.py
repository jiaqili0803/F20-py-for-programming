import requests

import starwars_character  # import进来我们定义的这个module

#### Fetching Character data from swapi.co
BASE_URL = "https://swapi.dev/api/people" # only interested in people

resp = requests.get(BASE_URL)
results_object = resp.json() 
people_list = results_object["results"]
characters = []
for p in people_list:
    characters.append(starwars_character.Character(character_data=p))
    # the original line ：
    #       characters.append(Character(character_data=p))
    # the modified line：
    #
    
for c in characters:
    print(c.info())
