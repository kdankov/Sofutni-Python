from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):

    def setUp(self):
        self.robot = ClimbingRobot("Mountain", "Arm", 100, 1024)

    def test_init(self):
        self.assertEqual(self.robot.ALLOWED_CATEGORIES, ['Mountain', 'Alpine', 'Indoor', 'Bouldering'])
        self.assertEqual(self.robot.category, "Mountain")
        self.assertEqual(self.robot.part_type, "Arm")
        self.assertEqual(self.robot.capacity, 100)
        self.assertEqual(self.robot.memory, 1024)
        self.assertEqual(self.robot.installed_software, [])

    def test_category_setter_if_category_is_not_valid_raises_value_error(self):
        self.robot.category = "Alpine"
        self.assertEqual(self.robot.category, "Alpine")

        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Invalid Category"

        self.assertEqual(str(ve.exception), f"Category should be one of {self.robot.ALLOWED_CATEGORIES}")
        self.assertEqual(self.robot.category, "Alpine")

    def test_get_used_capacity(self):
        self.assertEqual(self.robot.get_used_capacity(), 0)
        self.robot.install_software({"name": "TestSoftware", "capacity_consumption": 20, "memory_consumption": 50})
        self.assertEqual(self.robot.get_used_capacity(), 20)

    def test_get_available_capacity(self):
        self.assertEqual(self.robot.get_available_capacity(), 100)
        self.robot.install_software({"name": "TestSoftware", "capacity_consumption": 20, "memory_consumption": 50})
        self.assertEqual(self.robot.get_available_capacity(), 80)

    def test_get_used_memory(self):
        self.assertEqual(self.robot.get_used_memory(), 0)
        self.robot.install_software({"name": "TestSoftware", "capacity_consumption": 20, "memory_consumption": 50})
        self.assertEqual(self.robot.get_used_memory(), 50)

    def test_get_available_memory(self):
        self.assertEqual(self.robot.get_available_memory(), 1024)
        self.robot.install_software({"name": "TestSoftware", "capacity_consumption": 20, "memory_consumption": 50})
        self.assertEqual(self.robot.get_available_memory(), 974)

    def test_install_software_successfully(self):
        result = self.robot.install_software(
            {"name": "TestSoftware", "capacity_consumption": 20, "memory_consumption": 50})
        expected = "Software 'TestSoftware' successfully installed on Mountain part."

        self.assertEqual(expected, result)
        self.assertEqual(self.robot.installed_software,
                         [{"name": "TestSoftware", "capacity_consumption": 20, "memory_consumption": 50}])

    def test_install_software_with_the_biggest_possible_values(self):
        result = self.robot.install_software(
            {"name": "TestSoftware", "capacity_consumption": 100, "memory_consumption": 1024})
        expected = "Software 'TestSoftware' successfully installed on Mountain part."

        self.assertEqual(expected, result)
        self.assertEqual(self.robot.installed_software,
                         [{"name": "TestSoftware", "capacity_consumption": 100, "memory_consumption": 1024}])

    def test_install_software_if_there_is_insufficient_capacity(self):
        self.assertEqual(
            self.robot.install_software({"name": "TestSoftware", "capacity_consumption": 20, "memory_consumption": 50}),
            f"Software 'TestSoftware' successfully installed on Mountain part.")

        result = self.robot.install_software(
                {"name": "TestSoftware", "capacity_consumption": 100, "memory_consumption": 50})
        expected = "Software 'TestSoftware' cannot be installed on Mountain part."

        self.assertEqual(expected, result)

    def test_install_software_if_there_is_insufficient_memory(self):
        self.assertEqual(
            self.robot.install_software({"name": "TestSoftware", "capacity_consumption": 20, "memory_consumption": 50}),
            f"Software 'TestSoftware' successfully installed on Mountain part.")

        result = result = self.robot.install_software(
                {"name": "TestSoftware", "capacity_consumption": 20, "memory_consumption": 1024})
        expected = "Software 'TestSoftware' cannot be installed on Mountain part."

        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
