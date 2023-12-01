from unittest import TestCase, main
from project.robot import Robot


class TestRobot(TestCase):

    def setUp(self):
        self.robot = Robot('1', 'Military', 5, 500)

    def test_init(self):
        self.assertEqual('1', self.robot.robot_id)
        self.assertEqual('Military', self.robot.category)
        self.assertEqual(5, self.robot.available_capacity)
        self.assertEqual(500, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_category_setter_if_category_is_not_valid_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = 'AI'

        self.assertEqual("Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'", str(ve.exception))

    def test_price_if_price_is_less_than_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -10

        self.assertEqual('Price cannot be negative!', str(ve.exception))

    def test_upgrade_if_hardware_component_exists(self):
        self.robot.hardware_upgrades = ['Jetpack']
        result = self.robot.upgrade('Jetpack', 100.0)

        self.assertEqual('Robot 1 was not upgraded.', result)

    def test_upgrade_successfully(self):
        result = self.robot.upgrade('Jetpack', 100.0)

        self.assertEqual('Robot 1 was upgraded with Jetpack.', result)
        self.assertEqual(['Jetpack'], self.robot.hardware_upgrades)
        self.assertEqual(650.0, self.robot.price)

    def test_update_not_successful_if_the_version_is_lower_than_the_current_one(self):
        self.robot.software_updates = [1.5]

        result = self.robot.update(1.3, 4)

        self.assertEqual('Robot 1 was not updated.', result)

    def test_update_not_successful_if_the_needed_capacity_is_more_than_the_available_capacity(self):
        self.robot.software_updates = [1.5]

        result = self.robot.update(1.6, 8)

        self.assertEqual('Robot 1 was not updated.', result)

    def test_update_successfully(self):
        self.robot.software_updates = [1.5]

        result = self.robot.update(1.6, 4)

        self.assertEqual(f'Robot 1 was updated to version 1.6.', result)
        self.assertEqual([1.5, 1.6], self.robot.software_updates)
        self.assertEqual(1, self.robot.available_capacity)

    def test_greater_than_dunder_when_the_robot_is_more_expensive_than_the_other_one(self):
        robot2 = Robot('2', 'Military', 5, 100)

        result = self.robot > robot2

        self.assertEqual(f'Robot with ID 1 is more expensive than Robot with ID 2.', result)

    def test_greater_than_dunder_when_the_robot_is_as_equally_expensive_as_the_other_one(self):
        robot2 = Robot('2', 'Military', 5, 500)

        result = self.robot > robot2

        self.assertEqual(f'Robot with ID 1 costs equal to Robot with ID 2.', result)

    def test_greater_than_dunder_when_the_robot_is_cheaper_than_the_other_one(self):
        robot2 = Robot('2', 'Military', 5, 1000)

        result = self.robot > robot2

        self.assertEqual(f'Robot with ID 1 is cheaper than Robot with ID 2.', result)


if __name__ == '__main__':
    main()