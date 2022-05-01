import time

import requests
from bs4 import BeautifulSoup

url = 'https://www.nps.gov/index.htm'

## Make the soup for the Courses page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')



places_b = soup.find('ul', class_='dropdown-menu SearchBar-keywordSearch')
places = places_b.find_all('li', recursive=False)
print(places)

<li><a href="/state/wy/index.htm">Wyoming</a></li>

for place in places:
    place.split(NAME_NUMBER_DIVIDER)[1].strip())
