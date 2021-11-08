import csv

from models.library import Library


class Book(Library):
    all = []

    def __init__(self, title: str, author: str, year: int):
        # Call to super function to have access to all attributes/methods
        super().__init__(
            title, author, year
        )

    # Read from books.csv
    @classmethod
    def instantiate_from_csv(cls):
        with open('../data/books.csv', 'r') as f:
            reader = csv.DictReader(f)
            books = list(reader)

        for book in books:
            Book(
                title=book.get('title'),
                author=book.get('author'),
                year=int(book.get('year'))
            )

    def add_book(self):
        self.copies_available += 1
        Book.all.append(self)
        return self

    def borrow_book(self):
        if self.copies_available >= 1:
            self.copies_available -= 1
            return f"{self.title} borrowed. {self.copies_available} left"
        else:
            return "No more books left"

    def return_book(self):
        self.copies_available += 1
        return f"{self.title} returned, {self.copies_available} in stock"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.year == other.year

    @staticmethod
    def search_book(search_query):
        results = []
        for x in Book.all:  # Loop through all books
            if search_query == x.title or search_query == x.author:  # Check if tile/author matches
                results.append(x)  # If it's a match, append it to results array
        if not results:  # If list is empty, print Nothing found
            print("Nothing found")
        else:  # If list is filled, sort by year
            results.sort(key=lambda y: y.year, reverse=True)
            print(results)
