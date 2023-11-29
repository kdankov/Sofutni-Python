from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero('Hero', 5, 100, 10)
        self.enemy = Hero('Enemy', 5, 100, 10)

    def testInit(self):
        self.assertEqual('Hero', self.hero.username)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(10, self.hero.damage)

    def test_battle_when_both_usernames_are_equal_raises_exception(self):
        self.enemy.username = self.hero.username

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_battle_if_hero_health_is_less_than_or_equal_to_zero_raises_value_error(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        expected = 'Your health is lower than or equal to 0. You need to rest'
        self.assertEqual(expected, str(ve.exception))

    def test_battle_if_enemy_health_is_less_than_or_equal_to_zero_raises_value_error(self):
        self.enemy.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        expected = 'You cannot fight Enemy. He needs to rest'
        self.assertEqual(expected, str(ve.exception))

    def test_battle_is_draw_when_both_heroes_health_is_less_than_or_equal_to_zero(self):
        self.hero.damage = 150
        self.enemy.damage = 150

        result = self.hero.battle(self.enemy)

        self.assertEqual('Draw', result)

    def test_battle_if_hero_wins(self):
        self.hero.damage = 100
        self.enemy.damage = 10

        result = self.hero.battle(self.enemy)

        self.assertEqual('You win', result)
        self.assertEqual(6, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(105, self.hero.damage)

    def test_battle_if_enemy_wins(self):
        self.hero_damage = 10
        self.enemy.damage = 100

        result = self.hero.battle(self.enemy)

        self.assertEqual('You lose', result)
        self.assertEqual(6, self.enemy.level)
        self.assertEqual(55, self.enemy.health)
        self.assertEqual(105, self.enemy.damage)

    def test_str(self):
        expected = f'Hero Hero: 5 lvl\n' \
               f'Health: 100\n' \
               f'Damage: 10\n'

        self.assertEqual(expected, str(self.hero))


if __name__ == '__main__':
    main()