import time
from bs4 import BeautifulSoup
from selenium import webdriver
from scrap import *
from exceptions import *


class Parser:
    def __init__(self, site_url):
        self.site_url = site_url

    def run(self):
        try:            
            print(f"Запущен парсинг сайта: {self.site_url}") 
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome(options=options)
            driver.get(self.site_url)
            html_source = driver.page_source
            soup = BeautifulSoup(html_source, "html.parser") 

            title = get_title(soup)
        except ParserError as e:
            print(f"Ошибка при парсинге сайта {self.site_url}: {e}")
            raise
        else:
            print("Парсер отработал")
            return {
                'title': title,
                'description': f"Описание для {self.site_url}",
                'keywords': f"Ключевые слова для {self.site_url}",
            }
        finally:
            driver.quit()
