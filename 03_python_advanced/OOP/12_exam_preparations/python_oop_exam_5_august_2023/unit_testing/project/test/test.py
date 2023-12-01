from unittest import TestCase, main
from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):

    def setUp(self):
        self.car = SecondHandCar('E39', 'Sedan', 100_000, 6000.0)

    def test_init(self):
        self.assertEqual('E39', self.car.model)
        self.assertEqual('Sedan', self.car.car_type)
        self.assertEqual(100_000, self.car.mileage)
        self.assertEqual(6000.0, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_setter_if_price_is_less_or_equal_to_one_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_mileage_setter_if_mileage_is_less_or_equal_to_100_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_set_promotional_price_if_the_new_price_is_equal_or_less_than_the_old_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(6000.0)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price_successfully(self):
        result = self.car.set_promotional_price(5000.0)

        self.assertEqual('The promotional price has been successfully set.', result)
        self.assertEqual(5000.0, self.car.price)

    def test_need_repair_if_repair_price_if_more_than_half_of_the_car_price(self):
        result = self.car.need_repair(3001.0, 'engine change')

        self.assertEqual('Repair is impossible!', result)

    def test_need_repair_successfully(self):
        result = self.car.need_repair(2000.0, 'engine change')

        self.assertEqual('Price has been increased due to repair charges.', result)
        self.assertEqual(8000.0, self.car.price)
        self.assertIn('engine change', self.car.repairs)

    def test_greater_than_dunder_if_car_types_are_not_the_same(self):
        self.car2 = SecondHandCar('GT3-RS', 'Sport car', 100_000, 200_000.0)
        result = self.car > self.car2

        self.assertEqual('Cars cannot be compared. Type mismatch!', result)

    def test_greater_than_dunder_if_car_types_are_the_same(self):
        self.car2 = SecondHandCar('E39', 'Sedan', 100_000, 8000.0)
        self.assertFalse(self.car > self.car2)

    def test_str_dunder(self):
        expected = """Model E39 | Type Sedan | Milage 100000km
Current price: 6000.00 | Number of Repairs: 0"""

        self.assertEqual(expected, self.car.__str__())


if __name__ == '__main__':
    main()