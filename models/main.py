from models.book import Book


# When dummy books from csv the number of their copies don't apply.
# Keeping the function in the code but commented out

# Book.instantiate_from_csv()
book1 = Book("Sandas History", "D. Malachovskis", 2009)
book2 = Book("Sandas History", "R. Malachovskis", 2008)
book3 = Book("Sandas History", "K. Malachovskis", 2007)
book4 = Book("Harry Potter", "J. K. Rowling", 1997)

# book2.add_book()
# book3.add_book()
# book4.add_book()

# Methods:
book1.add_book()
book1.borrow_book()
book1.return_book()
book1.search_book("Sandas History")
