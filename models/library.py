class Library:

    def __init__(self, title: str, author: str, year: int, copies_available=0):
        # Validate arguments
        assert year >= 0, f"Year {year} can't be negative"
        assert copies_available >= 0, f"Copies available - {copies_available}, cannot be less than zero"

        # Assign to self
        self.__title = title
        self.__author = author
        self.__year = year
        self.copies_available = copies_available

    # Property = Read-Only attribute
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__title}', '{self.__author}', {self.__year})"
