import time
from bs4 import BeautifulSoup
from selenium import webdriver
from .scrap import *
from .exceptions import *
import logging


parser_logger = logging.getLogger(__name__)
parser_logger.setLevel(logging.INFO)

parser_handler = logging.FileHandler(f"{__name__}.log", mode='w', encoding='utf-8')
parser_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

parser_handler.setFormatter(parser_formatter)
parser_logger.addHandler(parser_handler)

class Parser:
    def __init__(self, site_url):
        self.site_url = site_url

    def run(self):
        try:            
            parser_logger.info(f"Выполняется получение кода страницы для сайта: {self.site_url}") 

            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome(options=options)
            driver.get(self.site_url)
            html_source = driver.page_source
            soup = BeautifulSoup(html_source, "html.parser")

            parser_logger.info("Запускается поиск title")

            title = get_title(soup)
        except ParserError as e:
            parser_logger.exception("ParserError", exc_info=True)
            raise
        else:
            parser_logger.info("Парсер отработал, данные получены")
            return {
                'title': title,
                'description': f"Описание для {self.site_url}",
                'keywords': f"Ключевые слова для {self.site_url}",
            }
        finally:
            driver.quit()
