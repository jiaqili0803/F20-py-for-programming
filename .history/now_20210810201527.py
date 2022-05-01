import requests
from bs4 import BeautifulSoup

## Make the soup
url = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup) ## sanity check, delete after it checks out


def extract_course_number_name(soup):
    return(soup
        .find(class_=COURSE_DETAILS_DIV_CLASS)
        .find(NAME_NUMBER_CONTAINER_TAG)
        .text.strip())
    
dropdown_list = "dropdown-menu SearchBar-keywordSearch"
each_place_tag = 'li'   

def build_state_url_dict(soup):
    return(soup.find(class = dropdown_list).find(each_place_tag).text.strip())
    
    
    
    ''' 

    Returns
    -------
    dict
    e.g. {'michigan':'https://www.nps.gov/state/mi/index.htm', ...}
    '''
    pass
