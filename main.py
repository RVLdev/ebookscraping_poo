from booksscraper import BooksScraper
from csvWriter import CsvWriter

class Main:

	def __init__(self):
		self.launch()
		
	def launch(self):
		books_content = BooksScraper(books_links_list, category_name)
		self.write_csv_datas(books_content)

	def write_csv_datas(self, books_content):
		for book in books_content:
			CsvWriter.fill_in_csv_file(book_content)


if __name__ == "__main__":
	Main()