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
    
# Add oportunity to get headers, ... (need to change model ParsedData, add a multidata field, make migrations)

def get_header(soup):
    try:
        header_list = []
        scrap_logger.info(f"Запущен поиск тэга h1")
        headers = soup.find_all('h1')
        for header in headers:
            if header:
                header = header.text
                header_list.append(header)
            else:
                header = 'No header found'
                header_list.append(header)
    except Exception as e:
        scrap_logger.exception(f"{e}", exc_info=True)
        raise TagNameNotExist from e
    else:
        return header_list
    
def get_images(soup):
    try:
        image_list = []
        scrap_logger.info(f"Запущен поиск тэга img")
        images = soup.find_all('img')
        for image in images:
            if image:
                image_dict = {
                    'src': image.get('src', 'No image found'),
                    'alt': image.get('alt', 'No alt text found')
                }
                image_list.append(image_dict)
            else:
                image = 'No image found'
                image_list.append(image)
    except Exception as e:
        scrap_logger.exception(f"{e}", exc_info=True)
        raise TagNameNotExist from e
    else:
        return image_list