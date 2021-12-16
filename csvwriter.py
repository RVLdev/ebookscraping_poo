import csv

from booksscraper import BooksScraper
from categoryscraper import CategoryScraper


class CsvWriter:
	category_name = CategoryScraper.get_category_name()
	CSV_HEADER = ["product_page_url", "universal_product_code (upc)", "title",
				"price_including_tax", "price_excluding_tax", "number_available",
				"product_description", "category", "review_rating", "image_url"]
	data = BooksScraper.__transform_datascraped_to_dataset()

	@classmethod
	def create_csv_file(category_name, csv_header=CSV_HEADER):
		with open(category_name+".csv", 'w', newline='',
				  encoding="utf-8") as csv_file:
			writer = csv.DictWriter(csv_file, fieldnames=csv_header, delimiter=',')
			writer.writeheader()

	@classmethod
	def fill_in_csv_file(category_name, data, csv_header=CSV_HEADER):
	    with open(category_name+".csv", 'a', newline='',
	              encoding="utf-8") as csv_file:
	        writer = csv.DictWriter(csv_file, fieldnames=csv_header, delimiter=',')
			writer.writerow(data)
