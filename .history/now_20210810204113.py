import time

import requests
from bs4 import BeautifulSoup

url = 'https://www.nps.gov/index.htm'

## Make the soup for the Courses page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
#print()

## For each course listed
places_b = soup.find('ul', class_='dropdown-menu SearchBar-keywordSearch')


places = places_b.find_all('li', recursive=False)
print(places)

'''
for course_listing_div in course_listing_divs:

    ## extract the course details URL
    course_link_tag = course_listing_div.find('a')
    course_details_path = course_link_tag['href']
    course_details_url = BASE_URL + course_details_path

    ## Make the soup for course details
    response = requests.get(course_details_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    ## extract course number and name
    number_name = soup.find(class_='grid--3col-2').find('h1')
    print(number_name.text.strip())

    ## extract course description
    desc = soup.find(class_='grid--3col-2').find('p')
    #print(desc.text.strip())

    ## extract credit hours
    credits = soup.find(class_='credit-hours').find('span')
    print('Credits:', credits.text.strip())

    ## extract prereqs
    prereqs_div = soup.find(class_='prerequisites-enforced')
    if (prereqs_div is not None):
        prereqs = prereqs_div.find_all('li')
        for p in prereqs:
            print('Prereq:', p.text.strip())

    print('-' * 40)

    time.sleep(1)


=========================
    
dropdown_list = "dropdown-menu SearchBar-keywordSearch"
each_place_tag = 'li'   

def build_state_url_dict(soup):
    dict = {}
    list = soup.find(class_= dropdown_list).find(each_place_tag).text.strip()
    
    return list
   
   
    '''



 #number_name.split(NAME_NUMBER_DIVIDER)[1].strip()
