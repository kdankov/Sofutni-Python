from unittest import TestCase, main
from project.bookstore import Bookstore


class TestBookstore(TestCase):

    def setUp(self):
        self.bookstore = Bookstore(5)

    def test_init(self):
        self.assertEqual(5, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_books_limit_setter_if_the_limit_is_equal_to_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0

        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test_books_limit_setter_if_the_limit_is_less_than_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = -5

        self.assertEqual("Books limit of -5 is not valid", str(ve.exception))

    def test_receive_book_if_there_is_not_enough_space_in_the_bookstore_raises_exception(self):
        self.bookstore.receive_book("GoT I", 1)
        self.bookstore.receive_book("Harry Potter", 2)

        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("Fight Club", 3)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_successfully(self):
        self.bookstore.receive_book("Fight Club", 2)

        result = self.bookstore.receive_book("Fight Club", 2)

        expected = "4 copies of Fight Club are available in the bookstore."

        self.assertEqual(expected, result)
        self.assertEqual(4, self.bookstore.availability_in_store_by_book_titles["Fight Club"])

    def test_sell_book_if_book_is_not_available_raises_exception(self):
        self.bookstore.receive_book("Fight Club", 1)

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Silence Of The Lambs", 1)
        
        self.assertEqual("Book Silence Of The Lambs doesn't exist!", str(ex.exception))

    def test_sell_book_if_there_are_not_enough_copies_raises_exception(self):
        self.bookstore.receive_book("Fight Club", 1)

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Fight Club", 2)

        self.assertEqual("Fight Club has not enough copies to sell. Left: 1", str(ex.exception))

    def test_sell_book_successfully(self):
        self.bookstore.receive_book("Fight Club", 3)
        self.bookstore.receive_book("Silence Of The Lambs", 2)

        result = self.bookstore.sell_book("Fight Club", 3)

        self.assertEqual("Sold 3 copies of Fight Club", result)
        self.assertEqual(3, self.bookstore.total_sold_books)
        self.assertEqual({"Fight Club": 0, "Silence Of The Lambs": 2}, self.bookstore.availability_in_store_by_book_titles)

    def test_len_dunder(self):
        self.bookstore.receive_book("Fight Club", 1)
        self.bookstore.receive_book("Silence Of The Lambs", 2)
        self.bookstore.sell_book("Silence Of The Lambs", 1)
        self.assertEqual(2, len(self.bookstore))

    def test_len_dunder_when_the_store_is_empty(self):
        self.assertEqual(0, len(self.bookstore))

    def test_str_dunder(self):
        self.bookstore.receive_book("Fight Club", 1)
        self.bookstore.receive_book("Silence Of The Lambs", 3)
        self.bookstore.sell_book("Silence Of The Lambs", 2)
        self.bookstore.receive_book("Interstellar", 1)
        self.bookstore.sell_book("Interstellar", 1)

        expected = """Total sold books: 3
Current availability: 2
 - Fight Club: 1 copies
 - Silence Of The Lambs: 1 copies
 - Interstellar: 0 copies"""
        self.assertEqual(expected, str(self.bookstore))

    def test_representation_with_no_data(self):
        expected = """Total sold books: 0
Current availability: 0"""
        self.assertEqual(expected, str(self.bookstore))


if __name__ == "__main__":
    main()
