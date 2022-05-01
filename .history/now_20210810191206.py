

import requests
from bs4 import BeautifulSoup

## Make the soup
url = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup) ## sanity check, delete after it checks out
