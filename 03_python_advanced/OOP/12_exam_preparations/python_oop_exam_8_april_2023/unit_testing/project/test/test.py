from unittest import TestCase, main
from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):

    def setUp(self):
        self.tennis_player = TennisPlayer('Rafael', 37, 500)

    def test_init(self):
        self.assertEqual('Rafael', self.tennis_player.name)
        self.assertEqual(37, self.tennis_player.age)
        self.assertEqual(500, self.tennis_player.points)
        self.assertEqual([], self.tennis_player.wins)

    def test_name_setter_if_name_length_is_less_than_or_equal_to_two_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.name = 'Ra'

        self.assertEqual('Name should be more than 2 symbols!', str(ve.exception))

    def test_age_setter_if_age_is_less_than_eighteen_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.age = 17

        self.assertEqual('Players must be at least 18 years of age!', str(ve.exception))

    def test_add_new_win_if_tournament_has_already_been_won(self):
        self.tennis_player.wins = ['Australian Open']

        result = self.tennis_player.add_new_win('Australian Open')
        expected = 'Australian Open has been already added to the list of wins!'

        self.assertEqual(expected, result)

    def test_add_new_win_successfully(self):
        self.tennis_player.add_new_win('Australian Open')

        self.assertEqual(['Australian Open'], self.tennis_player.wins)

    def test_less_than_dunder_if_player_points_are_less_than_the_other_player_points(self):
        tennis_player2 = TennisPlayer('Roger', 42, 600)

        result = self.tennis_player < tennis_player2
        expected = 'Roger is a top seeded player and he/she is better than Rafael'
        self.assertEqual(expected, result)

    def test_less_than_dunder_if_player_points_are_more_than_the_other_player_points(self):
        tennis_player2 = TennisPlayer('Roger', 42, 400)

        result = self.tennis_player < tennis_player2
        expected = 'Rafael is a better player than Roger'

        self.assertEqual(expected, result)

    def test_str_dunder(self):
        self.tennis_player.add_new_win('Australian Open')
        self.tennis_player.add_new_win('Wimbledon')

        expected = (f'Tennis Player: Rafael\n'
                    f'Age: 37\n'
                    f'Points: 500.0\n'
                    f'Tournaments won: Australian Open, Wimbledon')

        self.assertEqual(expected, self.tennis_player.__str__())


if __name__ == '__main__':
    main()
