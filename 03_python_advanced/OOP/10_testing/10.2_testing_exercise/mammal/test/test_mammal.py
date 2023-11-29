from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal('Savage', 'Dog', 'Bark')

    def test_init(self):
        self.assertEqual('Savage', self.mammal.name)
        self.assertEqual('Dog', self.mammal.type)
        self.assertEqual('Bark', self.mammal.sound)

    def test_get_kingdom(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_make_sound(self):
        result = self.mammal.make_sound()

        self.assertEqual('Savage makes Bark', result)

    def test_info(self):
        result = self.mammal.info()

        self.assertEqual('Savage is of type Dog', result)


if __name__ == '__main__':
    main()