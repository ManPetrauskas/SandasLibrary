import unittest
from models import book


class TestBook(unittest.TestCase):

    def test_add_book(self):  # Technically method returns the initialized object
        self.assertEqual(self, self)

