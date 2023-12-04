from unittest import TestCase, main
from project.toy_store import ToyStore


class TestToyStore(TestCase):
    def setUp(self):
        self.toy_store = ToyStore()

    def test_init(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None
        }, self.toy_store.toy_shelf)

    def test_add_toy_if_shelf_does_not_exist_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('H', 'toy1')

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_if_the_toy_already_exists_in_the_shelf_raises_exception(self):
        self.toy_store.toy_shelf['A'] = 'toy1'

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('A', 'toy1')

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_if_the_shelf_is_taken_raises_exception(self):
        self.toy_store.toy_shelf['A'] = 'toy2'

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('A', 'toy1')

        self.assertEqual('Shelf is already taken!', str(ex.exception))

    def test_add_toy_successfully(self):
        result = self.toy_store.add_toy('A', 'toy1')

        self.assertEqual('Toy:toy1 placed successfully!', result)
        self.assertEqual(self.toy_store.toy_shelf['A'], 'toy1')

    def test_remove_toy_if_shelf_does_not_exist_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('H', 'toy1')

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_if_toy_does_not_exist_in_the_shelf_raises_exception(self):
        self.toy_store.add_toy('A', 'Toy2')
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('A', 'toy1')

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_successfully(self):
        self.toy_store.toy_shelf['A'] = 'toy1'

        result = self.toy_store.remove_toy('A', 'toy1')

        self.assertEqual('Remove toy:toy1 successfully!', result)
        self.assertEqual(self.toy_store.toy_shelf['A'], None)

if __name__ == '__main__':
    main()