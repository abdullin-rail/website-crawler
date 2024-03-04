import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import requests

# Selenium init (Chrome)
service = Service('./chromedriver')
options = Options()
options.headless = True
driver = webdriver.Chrome(service=service, options=options)


def get_links(url: str, base_url: str):
    """
    Function for getting links from url
    """
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    links = soup.find_all('a', href=True)
    filtered_links = []
    for link in links:
        href = link['href']
        if is_absolute(href):
            parsed_href = urlparse(href)
            parsed_base_url = urlparse(base_url)
            if parsed_href.netloc == parsed_base_url.netloc:
                filtered_links.append(href)
        else:
            abs_link = urljoin(url, href)
            if urlparse(abs_link).netloc == urlparse(base_url).netloc:
                filtered_links.append(abs_link)
    return filtered_links

def is_absolute(url: str):
    return bool(urlparse(url).netloc)

def crawl_site(start_url: str, base_url: str):
    """
    Function for create sitemap
    :return: sitemap(dict) and error_pages[]
    """
    visited = set()
    queue = [start_url]
    sitemap = {}

    error_pages = []

    while queue:
        url = queue.pop(0)
        if url in visited:
            continue

        response = requests.get(url)
        if response.status_code != 200:
            # print(f"Страница {url} имеет статус код {response.status_code}")
            error_pages.append((url, response.status_code))

        visited.add(url)
        links = get_links(url,base_url)

        sitemap[url] = links

        for link in links:

            if is_absolute(link):
                queue.append(link)
            else:
                abs_link = urljoin(url, link)
                queue.append(abs_link)

    return sitemap, error_pages


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python3 main.py <WEBSITE_START_PAGE_URL>")
        sys.exit(1)

    start_url = sys.argv[1]
    base_url = start_url

    site_map, error_pages = crawl_site(start_url, base_url=base_url)
    for page, links in site_map.items():
        print(f"Page: {page}")
        print("Links on this page:")
        for link in links:
            print(f"  - {link}")

    print("Pages with errors (status code != 200) ")
    for page, status_code in error_pages:
        print(f"  - {page} - {status_code}")

