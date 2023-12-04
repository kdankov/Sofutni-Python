from unittest import TestCase, main
from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):

    def setUp(self):
        self.driver = TruckDriver('Ivan', 10)

    def test_init(self):
        self.assertEqual('Ivan', self.driver.name)
        self.assertEqual(10, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_setter_if_less_than_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1

        self.assertEqual('Ivan went bankrupt.', str(ve.exception))

    def test_add_cargo_offer_if_cargo_location_already_exists_raises_exception(self):
        self.driver.available_cargos = {'Sofia', 500}

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer('Sofia', 500)

        self.assertEqual('Cargo offer is already added.', str(ex.exception))

    def test_add_cargo_offer_successfully(self):
        result = self.driver.add_cargo_offer('Sofia', 500)

        expected = 'Cargo for 500 to Sofia was added as an offer.'
        self.assertEqual(expected, result)
        self.assertEqual({'Sofia': 500}, self.driver.available_cargos)

    def test_drive_best_cargo_offer_if_there_are_no_offers_available_raises_value_error(self):
        result = self.driver.drive_best_cargo_offer()

        self.assertEqual('There are no offers available.', result)

    def test_drive_best_cargo_offer_successfully(self):
        self.driver.available_cargos = {'Sofia': 10, 'Burgas': 100}
        result = self.driver.drive_best_cargo_offer()

        expected = 'Ivan is driving 100 to Burgas.'

        self.assertEqual(expected, result)
        self.assertEqual(1000, self.driver.earned_money)
        self.assertEqual(100, self.driver.miles)

    def test_check_activities_when_driving_over_10k_miles(self):
        self.driver.available_cargos = {'Italy': 10_000}
        result = self.driver.drive_best_cargo_offer()

        expected = 'Ivan is driving 10000 to Italy.'
        self.assertEqual(expected, result)

        earned_money = 10000 * 10 - 40 * 20 - 10 * 45 - 6 * 500 - 7500
        self.assertEqual(earned_money, self.driver.earned_money)

    def test_repr_dunder(self):
        self.driver.available_cargos = {'Italy': 10_000}
        self.driver.drive_best_cargo_offer()

        expected = 'Ivan has 10000 miles behind his back.'
        self.assertEqual(expected, self.driver.__repr__())


if __name__ == '__main__':
    main()