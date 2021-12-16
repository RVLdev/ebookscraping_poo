import requests
from bs4 import BeautifulSoup

from book import Book


class BooksScraper:
    # récupère les données de tous les livres d'une seule page d'une catégorie
	def __init__(self, books_links_list):
		self.get_books_data(books_links_list)

	def get_books_data(self, books_links_list):
        books = []
		for urll in books_links_list:
            books.append(self.get_book_data(urll))   
	    return books
        
    def get_book_data(self, urll):
		# request
        product = requests.get(urll)

        #scrap BS4
        datascraped = self.__scrap_book_datas(product)

        # set dict  
        data = self.__transform_datascraped_to_dataset(urll, datascraped)

        return Book(data)

    def __scrap_book_datas(self, product):
        datascraped = []
		datascraped['soup_product'] = BeautifulSoup(product.content, 'html.parser')
        datascraped['title_pagination'] = soup_product.find('h1')
        datascraped['values_pagination'] = soup_product.find_all("td")
        datascraped['description_pagination'] = soup_product.find("p", class_="")
        datascraped['product_category_pagination'] = soup_product.find_all('li')
        datascraped['stars'] = soup_product.find("p", class_="star-rating")
        datascraped['cover_page_pagination'] = soup_product.find("div", class_="item active")
        return datascraped

    def __transform_datascraped_to_dataset(self, urll, datascraped):
		data = Book.create_datas_model()
        data['product_page_url'] = urll
        data["title"] = self.get_title(datascraped['title_pagination'])
        data["universal_product_code (upc)"] = self.get_upc(datascraped['values_pagination'])
        data["price_including_tax"] = self.get_price_inc_tax(datascraped['values_pagination'])
        data["price_excluding_tax"] = self.get_price_excl_tax(datascraped['values_pagination'])
        data["number_available"] = self.get_availability(datascraped['values_pagination'])
        data["product_description"] = self.get_descripton(datascraped['description_pagination'])
        data["category"] = self.get_category(datascraped['product_category_pagination'])
        data["review_rating"] = self.get_rating(datascraped['stars'])
        data["image_url"] = self.get_cover_page(datascraped['cover_page_pagination'])
        return data

    def get_title(self, title_pagination):
        return(title_pagination.text)

    def get_upc(self, values_pagination):
        caracteristics = []
        for value in values_pagination:
            (caracteristics.append(value.string))
        return(caracteristics[0])

    def get_price_inc_tax(self, values_pagination):
        caracteristics = []
        for value in values_pagination:
            (caracteristics.append(value.string))
        return(caracteristics[3])

    def get_price_excl_tax(self, values_pagination):
        caracteristics = []
        for value in values_pagination:
            (caracteristics.append(value.string))
        return(caracteristics[2])

    def get_availability(self, values_pagination):
        caracteristics = []
        for value in values_pagination:
            (caracteristics.append(value.string))
        return(caracteristics[5])

    def get_descripton(self, description_pagination):
        if description_pagination is not None:
            return(description_pagination.text)
        return("No description")

    def get_category(self, product_category_pagination):
        return((product_category_pagination[2].text))

    def get_rating(self, stars):
        return((str(stars).split(" ")[2])[:-5])

    def get_cover_page(self, cover_page_pagination):
        pict = cover_page_pagination.find('img')
        picture_link = pict['src']
        return(urljoin('https://books.toscrape.com', picture_link))
        