import time
from bs4 import BeautifulSoup
from selenium import webdriver
from .scrap import *
from .exceptions import *
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.common.exceptions import TimeoutException


parser_logger = logging.getLogger(__name__)

class Parser:
    def __init__(self, site_url):
        self.site_url = site_url

    def run(self):
        try:            
            parser_logger.info(f"Выполняется получение кода страницы для сайта: {self.site_url}") 

            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36")
            driver = webdriver.Chrome(options=options)

            driver.get(self.site_url)
            wait = WebDriverWait(driver, timeout=20, poll_frequency=1, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1, h2, h3')))

            html_source = driver.page_source
            soup = BeautifulSoup(html_source, "html.parser")

            title = get_title(soup)
            description = get_description(soup)
            keywords = get_keywords(soup)
            headers = get_header(soup)
            images = get_images(soup)
        except TimeoutException:
            parser_logger.exception("TimeoutException", exc_info=True)
            with open('exc.html', 'a', encoding='utf-8') as f:
                f.write(driver.page_source)
            raise
        except ParserError:
            parser_logger.exception("ParserError", exc_info=True)
            raise
        else:
            parser_logger.info("Парсер отработал, данные получены")
            return {
                'title': title,
                'description': description,
                'keywords': keywords,
                'headers': headers,
                'images': images,
            }
        finally:
            driver.close()
            driver.quit()
