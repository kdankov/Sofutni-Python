from unittest import TestCase, main
from project.library import Library


class TestLibrary(TestCase):

    def setUp(self):
        self.library = Library("ABCD")
        
        self.test_lib = Library("ABC")
        self.test_lib.books_by_authors = {"J.K.Rowling": ["Harry Potter"], "Steven King": ["It"]}
        self.test_lib.readers = {"Ivan": [], "Georgi": []}

    def test_init(self):
        self.assertEqual("ABCD", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_setter_if_name_is_empty_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test_lib.name = ''

        expected = "Name cannot be empty string!"

        self.assertEqual(expected, str(ve.exception))

    def test_add_book_if_author_does_not_exist(self):
        self.test_lib.add_book("Tolkien", "Lord Of The Rings")

        self.assertEqual({"J.K.Rowling": ["Harry Potter"], "Steven King": ["It"], "Tolkien": ["Lord Of The Rings"]},
                         self.test_lib.books_by_authors)

    def test_add_book_if_author_already_exists(self):
        self.test_lib.add_book("J.K.Rowling", "The Cuckoo's Calling")

        self.assertEqual({"J.K.Rowling": ["Harry Potter", "The Cuckoo's Calling"], "Steven King": ["It"]},
                         self.test_lib.books_by_authors)

    def test_add_book_if_book_already_exists(self):
        self.test_lib.add_book("J.K.Rowling", "Harry Potter")

        self.assertEqual({"J.K.Rowling": ["Harry Potter"], "Steven King": ["It"]}, self.test_lib.books_by_authors)

    def test_add_reader_if_reader_is_already_registered(self):
        result = self.test_lib.add_reader("Ivan")

        expected = "Ivan is already registered in the ABC library."

        self.assertEqual(expected, result)

    def test_add_reader_successfully(self):
        self.test_lib.add_reader("Stefan")

        self.assertEqual({"Ivan": [], "Georgi": [], "Stefan": []}, self.test_lib.readers)

    def test_rent_book_if_reader_is_not_registered(self):
        result = self.test_lib.rent_book("Stefan", "Steven King", "It")

        expected = "Stefan is not registered in the ABC Library."

        self.assertEqual(expected, result)

    def test_rent_book_if_book_author_does_not_exist(self):
        result = self.test_lib.rent_book("Ivan", "Tolkien", "Lord Of The Rings")

        expected = "ABC Library does not have any Tolkien's books."

        self.assertEqual(expected, result)

    def test_rent_book_if_book_does_not_exist(self):
        result = self.test_lib.rent_book("Ivan", "Steven King", "The Shining")

        expected = """ABC Library does not have Steven King's "The Shining"."""

        self.assertEqual(expected, result)

    def test_rent_book_successfully(self):
        self.test_lib.rent_book("Ivan", "Steven King", "It")

        self.assertEqual({"Ivan": [{"Steven King": "It"}], "Georgi": []}, self.test_lib.readers)
        self.assertEqual({"J.K.Rowling": ["Harry Potter"], "Steven King": []}, self.test_lib.books_by_authors)


if __name__ == "__main__":
    main()

