""" BROUILLON_P2_POO.PY - essai class Categorie(s) v 10 12 """
import requests
from bs4 import BeautifulSoup
from requests.compat import urljoin
from booksscraper import BooksScraper

URL = 'https://books.toscrape.com/index.html'

 
class CategoryScraper:
    """récupère les urls des livres de toutes les pages d'UNE catégorie """
    def __init__(self, urlpages_list, category_link, books_pagination):
        self.urlpages_list = urlpages_list
        self.category_link = category_link
        self.books_pagination = books_pagination
        books_pagination = self.soup_pcat.find_all("h3")
        self.get_urls_books(urlpages_list, books_pagination)

        # resquest
        category_pages_requested = requests.get(urlp)
        categories_links_requested = requests.get(category_link)

        # BS4 /soup
        soup_pcat = BeautifulSoup(category_pages_requested.content, 'html.parser')
        soup_categories_links = BeautifulSoup(categories_links_requested.content, 'html.parser')

    def get_urls_books(self, urlpages_list, books_pagination):
        # get books links (of all pages) of one category
        books_links_list = []
        for urlp in urlpages_list:
            books_links_list.append(self.get_categorypage_books(books_pagination))
        return books_links_list

    def get_categorypage_books(self,  books_pagination):
        # get books links of one page of one category
        for book in books_pagination:
            a = book.find('a')
            b_link = a['href']
            book_link = b_link.replace("../../../",
                                        'https://books.toscrape.com/catalogue/')
        return book_link

    def get_url_category_pages_list(self, category_link, nbpages):
        # get url of the pages of one category (urlpages_list)
        urlpages_list = []
        urlpages_list.append(category_link)
        if nbpages > 1:
            for i in range(2, (nbpages+1)):
                urlpage = category_link.replace("index", "page-"+str(i))
                urlpages_list.append(urlpage)
        return urlpages_list

    def get_books_pagination(self, soup_pcat):
        books_pagination = soup_pcat.find_all("h3")
        return books_pagination

    def get_nb_pages(self, books_qty):
        if (int(books_qty)) % 20 == 0:
            return(int(books_qty))/20
        return((int(books_qty))//20)+1

    def get_books_qty(self, soup_categories_links):
        books_qty = soup_categories_links.find_all("strong")[1].text
        return books_qty

    def get_category_name(self, category_pagination):
        return(category_pagination.text)
    
    def get_category_pagination(self, soup_categories_links):
        category_pagination = soup_categories_links.find('li', class_='active')
        return category_pagination

 

# MAIN P2

# Category name
"""category_name = get_category_name(category_pagination)

# Urls of Category pages
urlpages_list = get_url_category_pages_list(category_link, nbpages)

# Urls of books
books_links_list = get_urls_books(urlpages_list)"""





"""-----------liste des catégories (urls de leurs 1ères pages)---------
URL = 'https://books.toscrape.com/index.html'
	website_requested = requests.get(url=URL)
	soup = BeautifulSoup(website_requested.content, 'html.parser')
	CSV_HEADER = ["product_page_url", "universal_product_code (upc)", "title",
				"price_including_tax", "price_excluding_tax", "number_available",
				"product_description", "category", "review_rating", "image_url"]

 def __init__(self, urlpages_list, category_link, books_pagination):
        self.category_link = category_link
        self.get_urls_books(urlpages_list, books_pagination)
        self.books_pagination = books_pagination
        books_pagination = self.soup_pcat.find_all("h3")






def get_categories_links_list(soup):
	# liste des catégories (urls de leurs 1ères pages)
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

    # main P2
    # Links of all categories
    categories_links_list = get_categories_links_list(soup)       
-----"""
