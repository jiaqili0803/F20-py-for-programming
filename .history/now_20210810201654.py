import requests
from bs4 import BeautifulSoup



def extract_course_number_name(soup):
    return(soup
        .find(class_=COURSE_DETAILS_DIV_CLASS)
        .find(NAME_NUMBER_CONTAINER_TAG)
        .text.strip())
    
dropdown_list = "dropdown-menu SearchBar-keywordSearch"
each_place_tag = 'li'   

def build_state_url_dict(soup):
    return(soup
        .find(class = dropdown_list)
        .find(each_place_tag)
        .text.strip())
    
    
    
    ''' 

    Returns
    -------
    dict
    e.g. {'michigan':'https://www.nps.gov/state/mi/index.htm', ...}
    '''
    pass
