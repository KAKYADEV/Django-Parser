from bs4 import BeautifulSoup
from .exceptions import *
import logging


scrap_logger = logging.getLogger(__name__)
scrap_logger.setLevel(logging.INFO)

scrap_handler = logging.FileHandler(f"{__name__}.log", mode='w', encoding='utf-8')
scrap_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

scrap_handler.setFormatter(scrap_formatter)
scrap_logger.addHandler(scrap_handler)


def get_title(soup):
    try:
        scrap_logger.info(f"Запущен поиск тэга title")
        title = soup.find('title')
        if title:
            title = title.text
        else:
            title = 'No title found'
    except Exception as e:
        scrap_logger.exception(f"{e}", exc_info=True)
        raise TagNameNotExist from e
    else:
        return title
    
def get_description(soup):
    try:
        scrap_logger.info(f"Запущен поиск description")
        description = soup.find('meta', attrs={'name': 'description'})
        if description:
            description = description.get('content', 'No description found')
        else:
            description = 'No description found'
    except Exception as e:
        scrap_logger.exception(f"{e}", exc_info=True)
        raise TagNameNotExist from e
    else:
        return description
    
def get_keywords(soup):
    try:
        scrap_logger.info(f"Запущен поиск keywords")
        keywords = soup.find('meta', attrs={'name': 'keywords'})
        if keywords:
            keywords = keywords.get('content', 'No keywords found')
        else:
            keywords = 'No keywords found'
    except Exception as e:
        scrap_logger.exception(f"{e}", exc_info=True)
        raise TagNameNotExist from e
    else:
        return keywords