from bs4 import BeautifulSoup
from exceptions import *


def get_title(soup):
    try:
        title = soup.find('title')
        title = title.text
    except Exception as e:
        print(e)
        raise TagNameNotExist from e
    else:
        return title