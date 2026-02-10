from bs4 import BeautifulSoup


def get_title(soup):
    title = soup.find('title')
    title = title.text

    return title