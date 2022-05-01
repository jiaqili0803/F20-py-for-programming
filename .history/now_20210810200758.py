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
    
    

def build_state_url_dict():
    ''' Make a dictionary that maps state name to state page url from "https://www.nps.gov"

    Parameters
    ----------
    None

    Returns
    -------
    dict
        key is a state name and value is the url
        e.g. {'michigan':'https://www.nps.gov/state/mi/index.htm', ...}
    '''
    pass
