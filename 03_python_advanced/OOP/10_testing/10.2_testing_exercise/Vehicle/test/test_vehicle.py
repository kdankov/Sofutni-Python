from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    fuel = 5.0
    horse_power = 150.0

    def setUp(self):
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    def test_init(self):
        self.assertEqual(self.fuel, self.vehicle.fuel)
        self.assertEqual(self.fuel, self.vehicle.capacity)
        self.assertEqual(self.horse_power, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_attributes_types(self):
        self.assertTrue(isinstance(self.vehicle.fuel, float))
        self.assertTrue(isinstance(self.vehicle.capacity, float))
        self.assertTrue(isinstance(self.vehicle.horse_power, float))
        self.assertTrue(isinstance(self.vehicle.fuel_consumption, float))

    def test_drive_with_not_enough_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(5)

        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_drive_with_enough_fuel(self):
        self.vehicle.drive(3)

        self.assertEqual(1.25, self.vehicle.fuel)

    def test_refuel_with_too_much_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(5)

        self.assertEqual('Too much fuel', str(ex.exception))

    def test_refuel_with_proper_quantity(self):
        self.vehicle.drive(4)

        self.vehicle.refuel(5)

        self.assertEqual(5, self.vehicle.fuel)

    def test_str(self):
        expected = f'The vehicle has 150.0 ' \
                f'horse power with 5.0 fuel left and 1.25 fuel consumption'

        self.assertEqual(expected, self.vehicle.__str__())


if __name__ == '__main__':
    main()