from unittest import TestCase, main
from project.movie import Movie


class TestMovie(TestCase):

    def setUp(self):
        self.movie = Movie("Fight Club", 1999, 8.8)

    def test_init(self):
        self.assertEqual("Fight Club", self.movie.name)
        self.assertEqual(1999, self.movie.year)
        self.assertEqual(8.8, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_setter_if_name_is_empty_string_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''

        expected = "Name cannot be an empty string!"

        self.assertEqual(expected, str(ve.exception))

    def test_year_setter_if_year_is_less_than_1887_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886

        expected = "Year is not valid!"

        self.assertEqual(expected, str(ve.exception))

    def test_add_actor_if_actor_already_exists(self):
        self.movie.actors = ["Brad Pitt"]

        result = self.movie.add_actor("Brad Pitt")
        expected = "Brad Pitt is already added in the list of actors!"

        self.assertEqual(expected, result)

    def test_add_actor_successfully(self):
        self.movie.add_actor("Brad Pitt")
        self.movie.add_actor("Edward Norton")

        self.assertEqual(["Brad Pitt", "Edward Norton"], self.movie.actors)

    def test_greater_than_dunder_if_movie_rating_is_bigger_than_the_other_movie_rating(self):
        movie2 = Movie("Interstellar", 2014, 8.7)

        result = self.movie > movie2
        expected = '"Fight Club" is better than "Interstellar"'

        self.assertEqual(expected, result)

    def test_greater_than_dunder_if_movie_rating_is_less_than_the_other_movie_rating(self):
        movie2 = Movie("The Shawshank Redemption", 1994, 9.3)

        result = self.movie > movie2
        expected = '"The Shawshank Redemption" is better than "Fight Club"'

        self.assertEqual(expected, result)

    def test_repr_dunder(self):
        self.movie.add_actor("Brad Pitt")
        self.movie.add_actor("Edward Norton")
        self.movie.add_actor("Helena Bonham Carter")

        expected = """Name: Fight Club
Year of Release: 1999
Rating: 8.80
Cast: Brad Pitt, Edward Norton, Helena Bonham Carter"""

        self.assertEqual(expected, self.movie.__repr__())

    def test_repr_dunder_with_no_actors(self):
        expected = """Name: Fight Club
Year of Release: 1999
Rating: 8.80
Cast: """

        self.assertEqual(expected, self.movie.__repr__())


if __name__ == "__main__":
    main()
