import requests
from requests.compat import urljoin
from bs4 import BeautifulSoup

URL = 'https://books.toscrape.com/index.html'

class WebsiteCategories:

   
    def __init__(self, soup, url=URL):
        self.url = url
        self.soup = soup
        self.get_categories_list(soup)
    
    website_requested = requests.get(url=URL)
    soup = BeautifulSoup(website_requested.content, 'html.parser')
    CSV_HEADER = ["product_page_url", "universal_product_code (upc)", "title",
                  "price_including_tax", "price_excluding_tax", "number_available",
                  "product_description", "category", "review_rating", "image_url"]


    def get_categories_list(self, soup):
        # gets website categories links
        categories_pagination = soup.find("div", class_="side_categories")
        categories_links_list = []
        li_cat_pagination = categories_pagination.find_all("li")
        for li in li_cat_pagination:
            a = li.find('a')
            link = a['href']
            categories_links = urljoin('https://books.toscrape.com/', link)
            categories_links_list.append(categories_links)
        del categories_links_list[0]
        return categories_links_list
