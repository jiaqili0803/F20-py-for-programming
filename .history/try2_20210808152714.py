import json

import requests

BASE_URL = "http://swapi.co/api/people" # only interested in people
resp = requests.get(BASE_URL)
results_object = json.loads(resp.text) 
print(results_object)
#exit()
