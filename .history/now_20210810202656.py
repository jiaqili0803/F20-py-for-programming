import requests
from bs4 import BeautifulSoup
import time

    
dropdown_list = "dropdown-menu SearchBar-keywordSearch"
each_place_tag = 'li'   

def build_state_url_dict(soup):
    dict = {}
    list = soup.find(class_= dropdown_list).find(each_place_tag).text.strip()
    
    return list
   
   
    
print()


 #number_name.split(NAME_NUMBER_DIVIDER)[1].strip()
    
    ''' 

    Returns
    -------
    dict
    e.g. {'michigan':'https://www.nps.gov/state/mi/index.htm', ...}
    '''
   
