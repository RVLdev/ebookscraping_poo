class Book:

	def __init__(self, datas = None):
		if datas:
			self.datas = datas
		else:
			self.datas = {
		        "product_page_url": None,
		        "universal_product_code (upc)": None,
		        "title": None,
		        "price_including_tax": None,
		        "price_excluding_tax": None,
		        "number_available": None,
		        "product_description": None,
		        "category": None,
		        "review_rating": None,
		        "image_url": None
		    }

	@classmethod
	def create_datas_model(cls):
		return {
	        "product_page_url": None,
	        "universal_product_code (upc)": None,
	        "title": None,
	        "price_including_tax": None,
	        "price_excluding_tax": None,
	        "number_available": None,
	        "product_description": None,
	        "category": None,
	        "review_rating": None,
	        "image_url": None
	    }

if __name__ == "__main__":
	b = Book()
	print(b.datas)