from unittest import TestCase, main
from project.railway_station import RailwayStation
from collections import deque


class TestRailwayStation(TestCase):

    def setUp(self):
        self.railway_station = RailwayStation("Station 1")

    def test_init(self):
        self.assertEqual("Station 1", self.railway_station.name)
        self.assertEqual(deque(), self.railway_station.arrival_trains)
        self.assertEqual(deque(), self.railway_station.departure_trains)

    def test_name_setter_if_the_name_has_less_than_three_symbols_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.railway_station.name = "St"

        expected = "Name should be more than 3 symbols!"

        self.assertEqual(expected, str(ve.exception))

    def test_name_setter_if_the_name_has_exactly_three_symbols_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.railway_station.name = "Sta"

        expected = "Name should be more than 3 symbols!"

        self.assertEqual(expected, str(ve.exception))

    def test_new_arrival_on_board(self):
        self.railway_station.arrival_trains = deque(["T1", "T2"])

        self.railway_station.new_arrival_on_board("T3")

        self.assertEqual(deque(["T1", "T2", "T3"]), self.railway_station.arrival_trains)

    def test_train_has_arrived_if_there_are_other_trains_to_arrive_first(self):
        self.railway_station.new_arrival_on_board("T1")
        self.railway_station.new_arrival_on_board("T2")
        self.railway_station.new_arrival_on_board("T3")

        result = self.railway_station.train_has_arrived("T2")
        expected = f"There are other trains to arrive before T2."

        self.assertEqual(expected, result)

    def test_train_has_arrived_successfully(self):
        self.railway_station.new_arrival_on_board("T1")
        self.railway_station.new_arrival_on_board("T2")
        self.railway_station.new_arrival_on_board("T3")

        result = self.railway_station.train_has_arrived("T1")
        expected = "T1 is on the platform and will leave in 5 minutes."

        self.assertEqual(expected, result)
        self.assertEqual(deque(["T2", "T3"]), self.railway_station.arrival_trains)
        self.assertEqual(deque(["T1"]), self.railway_station.departure_trains)

    def test_train_has_left_not_successful(self):
        self.railway_station.new_arrival_on_board("T1")
        self.railway_station.new_arrival_on_board("T2")
        self.railway_station.new_arrival_on_board("T3")
        self.railway_station.new_arrival_on_board("T4")
        self.railway_station.new_arrival_on_board("T5")

        self.railway_station.train_has_arrived("T1")
        self.railway_station.train_has_arrived("T2")
        self.assertEqual(deque(["T3", "T4", "T5"]), self.railway_station.arrival_trains)
        self.assertEqual(deque(["T1", "T2"]), self.railway_station.departure_trains)

        result = self.railway_station.train_has_left("T3")

        self.assertFalse(result)
        self.assertEqual(deque(["T1", "T2"]), self.railway_station.departure_trains)

    def test_train_has_left_successfully(self):
        self.railway_station.new_arrival_on_board("T1")
        self.railway_station.new_arrival_on_board("T2")
        self.railway_station.new_arrival_on_board("T3")

        self.railway_station.train_has_arrived("T1")
        self.railway_station.train_has_arrived("T2")

        result = self.railway_station.train_has_left("T1")

        self.assertTrue(result)
        self.assertEqual(deque(["T2"]), self.railway_station.departure_trains)


if __name__ == "__main__":
    main()