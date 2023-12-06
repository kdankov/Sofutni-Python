from unittest import TestCase, main
from project.plantation import Plantation


class TestPlantation(TestCase):

    def setUp(self):
        self.plantation = Plantation(5)

    def test_init(self):
        self.assertEqual(5, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_setter_if_size_is_less_than_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1

        expected = "Size must be positive number!"

        self.assertEqual(expected, str(ve.exception))

    def test_hire_worker_if_worker_is_already_hired_raises_value_error(self):
        self.plantation.workers = ["Ivan"]

        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Ivan")

        expected = "Worker already hired!"

        self.assertEqual(expected, str(ve.exception))

    def test_hire_worker_successfully(self):
        self.plantation.workers = ["Ivan"]

        result = self.plantation.hire_worker("Georgi")
        expected = "Georgi successfully hired."

        self.assertEqual(expected, result)
        self.assertEqual(["Ivan", "Georgi"], self.plantation.workers)
    
    def test_len_dunder(self):
        self.plantation.plants = {
            "Ivan": ["Mushroom", "Begonia", "Sunflower"],
            "Georgi": ["Tulip", "Chrysanthemum"]
        }

        self.assertEqual(5, len(self.plantation))

    def test_len_dunder_when_the_plantation_is_empty(self):
        self.assertEqual(0, len(self.plantation))

    def test_planting_if_worker_is_not_hired_raises_value_error(self):
        self.plantation.hire_worker("Ivan")

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Georgi", "Mushroom")

        expected = "Worker with name Georgi is not hired!"

        self.assertEqual(expected, str(ve.exception))

    def test_planting_if_the_plantation_is_full_raises_value_error(self):
        self.plantation.workers = ["Ivan"]
        self.plantation.plants = {"Ivan": ["Mushroom"]}
        self.plantation.size = 1

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Ivan", "Sunflower")

        expected = "The plantation is full!"

        self.assertEqual(expected, str(ve.exception))

    def test_planting_if_the_worker_is_hired_and_it_is_not_his_first_planting(self):
        self.plantation.hire_worker("Ivan")
        self.plantation.plants = {"Ivan": ["Mushroom"]}

        result = self.plantation.planting("Ivan", "Sunflower")
        expected = "Ivan planted Sunflower."

        self.assertEqual(expected, result)
        self.assertEqual(["Mushroom", "Sunflower"], self.plantation.plants["Ivan"])

    def test_planting_if_the_worker_is_hired_and_it_is_his_first_planting(self):
        self.plantation.hire_worker("Ivan")
        
        result = self.plantation.planting("Ivan", "Mushroom")
        expected = "Ivan planted it's first Mushroom."

        self.assertEqual(expected, result)
        self.assertEqual(["Mushroom"], self.plantation.plants["Ivan"])

    def test_str_dunder(self):
        self.plantation.hire_worker("Ivan")
        self.plantation.hire_worker("Georgi")
        self.plantation.planting("Ivan", "Mushroom")
        self.plantation.planting("Ivan", "Tulip")
        self.plantation.planting("Georgi", "Sunflower")
        self.plantation.planting("Georgi", "Chrysanthemum")

        expected = """Plantation size: 5
Ivan, Georgi
Ivan planted: Mushroom, Tulip
Georgi planted: Sunflower, Chrysanthemum"""

        self.assertEqual(expected, self.plantation.__str__())

    def test_str_dunder_with_no_data(self):
        expected = "Plantation size: 5\n"

        self.assertEqual(expected, self.plantation.__str__())

    def test_repr_dunder(self):
        self.plantation.hire_worker("Ivan")
        self.plantation.hire_worker("Georgi")

        expected = """Size: 5
Workers: Ivan, Georgi"""

        self.assertEqual(expected, self.plantation.__repr__())

    def test_repr_dunder_with_no_data(self):
        expected = """Size: 5
Workers: """

        self.assertEqual(expected, self.plantation.__repr__())


if __name__ == "__main__":
    main()
